"""Boomerang decompiler and parity diagnostic API server."""
import base64
import os
import re
import subprocess
import tempfile
import time
from pathlib import Path
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import disasm_helper

app = FastAPI(title="boomerang-decompiler", version="1.0")

class DecompileRequest(BaseModel):
    binary_b64: str
    addr: str

class DecompileResponse(BaseModel):
    decompiler: str = "boomerang"
    name: str
    code: str
    time_ms: int
    error: Optional[str] = None

class BatchDecompileRequest(BaseModel):
    binary_b64: str
    addresses: List[str]

class DecompileResultItem(BaseModel):
    addr: str
    name: str = "?"
    code: str = ""
    error: Optional[str] = None

class BatchDecompileResponse(BaseModel):
    decompiler: str = "boomerang"
    results: List[DecompileResultItem]
    time_ms: int

@app.get("/health")
def health():
    return {"status": "ok", "decompiler": "boomerang", "version": "latest"}

def validate_address(addr: str) -> int:
    if not addr or not addr.strip():
        raise HTTPException(status_code=400, detail="Address cannot be empty")
    try:
        if addr.lower().startswith("0x"):
            return int(addr, 16)
        try:
            return int(addr, 10)
        except ValueError:
            return int(addr, 16)
    except ValueError:
        raise HTTPException(status_code=400, detail=f"Invalid address format: {addr}")

def resolve_binary(binary: str) -> str:
    if not binary or not binary.strip():
        raise HTTPException(status_code=400, detail="Binary path cannot be empty")
    resolved = "/" + binary if binary.startswith("corpus/") else binary
    if not os.path.exists(resolved):
        raise HTTPException(status_code=404, detail=f"Binary not found: {resolved}")
    return resolved

@app.get("/functions")
def functions(binary: str):
    return disasm_helper.get_functions(resolve_binary(binary))

@app.get("/disasm")
def disasm(binary: str, addr: str, arch: str = "x86_64"):
    validate_address(addr)
    return disasm_helper.disassemble(resolve_binary(binary), addr, arch)

@app.get("/decode")
def decode(binary: str, addr: str, arch: str = "x86_64"):
    validate_address(addr)
    disasm_data = disasm(binary, addr, arch)
    res = []
    for inst in disasm_data:
        res.append({
            "address": inst.get("address"),
            "bytes": inst.get("bytes"),
            "length": inst.get("length"),
            "mnemonic": inst.get("mnemonic"),
            "prefixes": [],
            "modrm": None,
            "sib": None,
            "displacement": None,
            "immediate": None
        })
    return res

@app.get("/pcode")
def pcode(binary: str, addr: str):
    return []

@app.get("/cfg")
def cfg(binary: str, addr: str):
    validate_address(addr)
    return {"blocks": [], "edges": []}

def address_aliases(addr: str) -> set[str]:
    try:
        value = int(addr, 16) if addr.lower().startswith("0x") else int(addr)
    except ValueError:
        return {addr.lower()}

    aliases = {f"{value:x}", f"{value:08x}", f"0x{value:x}", f"0x{value:08x}"}
    if value >= 0x100000000:
        rva = value & 0xFFFFF
        aliases.update({f"{rva:x}", f"{rva:08x}", f"0x{rva:x}", f"0x{rva:08x}"})
    return {alias.lower() for alias in aliases}

def extract_function_by_address(code: str, addr: str) -> tuple[str, str]:
    """Extract one Boomerang function by the address comment above it."""
    aliases = address_aliases(addr)
    marker_re = re.compile(r"/\*\*\s*address:\s*(0x[0-9a-fA-F]+|[0-9a-fA-F]+)\s*\*/")
    markers = list(marker_re.finditer(code))

    for idx, marker in enumerate(markers):
        marker_addr = marker.group(1).lower()
        marker_value = marker_addr[2:] if marker_addr.startswith("0x") else marker_addr
        marker_aliases = {marker_addr, marker_value, f"0x{marker_value.lstrip('0') or '0'}", marker_value.lstrip("0") or "0"}
        if aliases.isdisjoint(marker_aliases):
            continue

        start = marker.start()
        end = markers[idx + 1].start() if idx + 1 < len(markers) else len(code)
        chunk = code[start:end].strip()
        name_match = re.search(r"\b([A-Za-z_]\w*)\s*\([^;{}]*\)\s*\{", chunk)
        return (name_match.group(1) if name_match else f"proc_{addr}", chunk)

    return "", f"Function at address {addr} not found in Boomerang address comments"

@app.post("/decompile", response_model=DecompileResponse)
def decompile(req: DecompileRequest):
    validate_address(req.addr)
    batch_req = BatchDecompileRequest(binary_b64=req.binary_b64, addresses=[req.addr])
    start = time.monotonic()
    try:
        resp = decompile_batch(batch_req)
        elapsed = int((time.monotonic() - start) * 1000)
        item = resp.results[0]
        if item.error:
            return DecompileResponse(name="?", code="", time_ms=elapsed, error=item.error)
        return DecompileResponse(name=item.name, code=item.code, time_ms=elapsed)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/decompile_batch", response_model=BatchDecompileResponse)
def decompile_batch(req: BatchDecompileRequest):
    try:
        binary_bytes = base64.b64decode(req.binary_b64, validate=True)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid base64 payload")
    with tempfile.TemporaryDirectory() as tmpdir:
        binary_path = Path(tmpdir) / "target.bin"
        binary_path.write_bytes(binary_bytes)
        start = time.monotonic()
        args = ["boomerang-cli"]
        for addr in req.addresses:
            try:
                val = int(addr, 16) if addr.lower().startswith("0x") else int(addr)
                args.extend(["-E", f"0x{val:x}"])
            except ValueError:
                pass
        args.append(str(binary_path))

        result = subprocess.run(
            args,
            cwd=tmpdir,
            capture_output=True, text=True, timeout=120
        )
        code_parts = []
        for root, dirs, files in os.walk(tmpdir):
            for file in sorted(files):
                if file.endswith(".c"):
                    content = (Path(root) / file).read_text(errors="replace")
                    code_parts.append(f"/* File: {file} */\n{content}")
        code = "\n\n".join(code_parts)
        elapsed = int((time.monotonic() - start) * 1000)
        results = []
        for addr in req.addresses:
            if not code:
                results.append(DecompileResultItem(
                    addr=addr,
                    name=f"fcn.{addr}",
                    error=f"Decompilation failed: {result.stderr or result.stdout}"
                ))
                continue

            fn_name, fn_code = extract_function_by_address(code, addr)
            if not fn_code or fn_code.startswith("Function at address"):
                results.append(DecompileResultItem(addr=addr, name=fn_name or f"fcn.{addr}", error=fn_code))
                continue

            results.append(DecompileResultItem(
                addr=addr,
                name=fn_name,
                code=fn_code,
            ))
        return BatchDecompileResponse(results=results, time_ms=elapsed)
