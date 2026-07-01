"""Snowman decompiler and parity diagnostic API server."""
import base64
import os
import subprocess
import tempfile
import time
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import disasm_helper

app = FastAPI(title="snowman-decompiler", version="1.0")
SNOWMAN_BIN = os.environ.get("SNOWMAN_BIN", "/snowman-master/build/nocode/nocode")

class DecompileRequest(BaseModel):
    binary_b64: str
    addr: str

class DecompileResponse(BaseModel):
    decompiler: str = "snowman"
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
    decompiler: str = "snowman"
    results: List[DecompileResultItem]
    time_ms: int

@app.get("/health")
def health():
    return {"status": "ok", "decompiler": "snowman", "version": "latest"}

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
    with tempfile.NamedTemporaryFile(suffix=".bin", delete=False) as f:
        f.write(binary_bytes)
        tmp_path = f.name

    start = time.monotonic()
    results = []
    try:
        for addr in req.addresses:
            try:
                result = subprocess.run(
                    [SNOWMAN_BIN, f"--from={addr}", "--print-cxx=-", tmp_path],
                    capture_output=True, text=True, timeout=120
                )
                if result.returncode != 0:
                    results.append(DecompileResultItem(addr=addr, name=f"func_{addr}", error=result.stderr or result.stdout))
                    continue
                code = result.stdout.strip()
                results.append(DecompileResultItem(addr=addr, name=f"func_{addr}", code=code))
            except Exception as e:
                results.append(DecompileResultItem(addr=addr, error=str(e)))
        elapsed = int((time.monotonic() - start) * 1000)
        return BatchDecompileResponse(results=results, time_ms=elapsed)
    finally:
        os.unlink(tmp_path)
