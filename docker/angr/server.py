"""angr decompiler and parity diagnostic API server."""
import base64
import os
import tempfile
import time
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import angr

app = FastAPI(title="angr-decompiler", version="1.0")

class DecompileRequest(BaseModel):
    binary_b64: str
    addr: str

class DecompileResponse(BaseModel):
    decompiler: str = "angr"
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
    decompiler: str = "angr"
    results: List[DecompileResultItem]
    time_ms: int

@app.get("/health")
def health():
    return {"status": "ok", "decompiler": "angr", "version": "latest"}

def resolve_binary(binary: str) -> str:
    if binary.startswith("corpus/"):
        return "/" + binary
    return binary

@app.get("/functions")
def functions(binary: str):
    bin_path = resolve_binary(binary)
    proj = angr.Project(bin_path, auto_load_libs=False)
    proj.analyses.CFGFast()
    res = []
    for addr, func in proj.kb.functions.items():
        res.append({
            "address": f"0x{addr:x}",
            "name": func.name,
            "size": func.size,
            "kind": "function"
        })
    return res

@app.get("/disasm")
def disasm(binary: str, addr: str):
    bin_path = resolve_binary(binary)
    proj = angr.Project(bin_path, auto_load_libs=False)
    addr_val = int(addr, 16)
    try:
        block = proj.factory.block(addr_val)
        res = []
        for inst in block.capstone.insns:
            res.append({
                "address": f"0x{inst.address:x}",
                "bytes": inst.bytes.hex(),
                "mnemonic": inst.mnemonic.lower(),
                "operands": inst.op_str,
                "length": inst.size,
                "fallthrough": f"0x{inst.address + inst.size:x}",
                "branch_target": None
            })
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/decode")
def decode(binary: str, addr: str):
    disasm_data = disasm(binary, addr)
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
    bin_path = resolve_binary(binary)
    proj = angr.Project(bin_path, auto_load_libs=False)
    addr_val = int(addr, 16)
    cfg_fast = proj.analyses.CFGFast()
    func = cfg_fast.functions.get(addr_val)
    if not func:
        return {"blocks": [], "edges": []}
    blocks = []
    edges = []
    for block in func.blocks:
        blocks.append({
            "start": f"0x{block.addr:x}",
            "end": f"0x{block.addr + block.size:x}"
        })
    for src, dst in func.transition_graph.edges():
        edges.append({
            "source": f"0x{src.addr:x}",
            "target": f"0x{dst.addr:x}",
            "kind": "branch"
        })
    return {"blocks": blocks, "edges": edges}

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
        proj = angr.Project(tmp_path, auto_load_libs=False)
        proj.analyses.CFGFast()
        for addr in req.addresses:
            try:
                addr_val = int(addr, 16)
                dec = proj.analyses.Decompiler(proj.kb.functions[addr_val])
                code = dec.codegen.text if dec.codegen else "angr decompilation empty"
                results.append(DecompileResultItem(addr=addr, name=f"func_{addr}", code=code))
            except Exception as e:
                results.append(DecompileResultItem(addr=addr, error=str(e)))
        elapsed = int((time.monotonic() - start) * 1000)
        return BatchDecompileResponse(results=results, time_ms=elapsed)
    finally:
        os.unlink(tmp_path)
