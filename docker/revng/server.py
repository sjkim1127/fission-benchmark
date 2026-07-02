"""rev.ng decompiler and parity diagnostic API server."""
import base64
import re
import subprocess
import tempfile
import time
from pathlib import Path
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import disasm_helper

app = FastAPI(title="revng-decompiler", version="1.0")

class DecompileRequest(BaseModel):
    binary_b64: str
    addr: str

class DecompileResponse(BaseModel):
    decompiler: str = "revng"
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
    decompiler: str = "revng"
    results: List[DecompileResultItem]
    time_ms: int

def _addr_hex(addr: str) -> str:
    try:
        return f"{int(addr, 16):x}"
    except ValueError:
        return addr.lower().removeprefix("0x")

def extract_revng_function(code: str, addr: str) -> str:
    """Extract one function from revng plain C output by its address-derived name."""
    addr_hex = _addr_hex(addr)
    match = re.search(rf"\bfunction_0x{re.escape(addr_hex)}_[A-Za-z0-9_]+\s*\(", code)
    if not match:
        return ""

    start = code.rfind("\n", 0, match.start()) + 1
    previous_end = start - 1
    previous_start = code.rfind("\n", 0, previous_end) + 1
    previous_line = code[previous_start:previous_end].strip()
    if previous_line.startswith("_ABI("):
        start = previous_start

    brace = code.find("{", match.end())
    if brace < 0:
        return code[start:code.find("\n", match.end())].strip()

    depth = 0
    for index in range(brace, len(code)):
        char = code[index]
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return code[start:index + 1].strip()
    return code[start:].strip()

@app.get("/health")
def health():
    return {"status": "ok", "decompiler": "revng", "version": "latest"}

def resolve_binary(binary: str) -> str:
    if binary.startswith("corpus/"):
        return "/" + binary
    return binary

@app.get("/functions")
def functions(binary: str):
    return disasm_helper.get_functions(resolve_binary(binary))

@app.get("/disasm")
def disasm(binary: str, addr: str, arch: str = "x86_64"):
    return disasm_helper.disassemble(resolve_binary(binary), addr, arch)

@app.get("/decode")
def decode(binary: str, addr: str, arch: str = "x86_64"):
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
    return {"blocks": [], "edges": []}

@app.post("/decompile", response_model=DecompileResponse)
def decompile(req: DecompileRequest):
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
    binary_bytes = base64.b64decode(req.binary_b64)
    with tempfile.TemporaryDirectory() as tmpdir:
        binary_path = Path(tmpdir) / "target.bin"
        binary_path.write_bytes(binary_bytes)
        ptml_path = Path(tmpdir) / "decompiled.ptml"
        start = time.monotonic()
        results = []
        try:
            artifact = subprocess.run(
                [
                    "revng",
                    "artifact",
                    "--analyze",
                    "decompile-to-single-file",
                    str(binary_path),
                    "-o",
                    str(ptml_path),
                ],
                capture_output=True,
                text=True,
                timeout=240,
            )
            if artifact.returncode != 0:
                detail = artifact.stderr or artifact.stdout or "revng artifact failed"
                results = [DecompileResultItem(addr=addr, name=f"func_{addr}", error=detail) for addr in req.addresses]
            else:
                plain = subprocess.run(
                    ["revng", "ptml", str(ptml_path)],
                    capture_output=True,
                    text=True,
                    timeout=60,
                )
                if plain.returncode != 0:
                    detail = plain.stderr or plain.stdout or "revng ptml conversion failed"
                    results = [DecompileResultItem(addr=addr, name=f"func_{addr}", error=detail) for addr in req.addresses]
                else:
                    code = plain.stdout
                    for addr in req.addresses:
                        fn_code = extract_revng_function(code, addr)
                        if fn_code:
                            results.append(DecompileResultItem(addr=addr, name=f"function_0x{_addr_hex(addr)}", code=fn_code))
                        else:
                            results.append(DecompileResultItem(addr=addr, name=f"func_{addr}", error=f"revng output did not contain function {addr}"))
        except Exception as e:
            results = [DecompileResultItem(addr=addr, name=f"func_{addr}", error=str(e)) for addr in req.addresses]
        elapsed = int((time.monotonic() - start) * 1000)
        return BatchDecompileResponse(results=results, time_ms=elapsed)
