"""Fission decompiler and parity diagnostic API server."""
import base64
import json
import os
import subprocess
import tempfile
import time
from pathlib import Path
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="fission-decompiler", version="1.0")
FISSION_BIN = Path("/usr/local/bin/fission_cli")
SLEIGH_SPEC_DIR = os.environ.get("FISSION_SLEIGH_SPEC_DIR", "/sleigh-specs")
RESOURCE_ROOT = os.environ.get("FISSION_RESOURCE_ROOT", "/opt/fission-utils/utils")
GHIDRA_DATA_DIR = os.environ.get("FISSION_GHIDRA_DATA_DIR", "/opt/fission-utils/utils/ghidra-data")

class DecompileRequest(BaseModel):
    binary_b64: str
    addr: str

class DecompileResponse(BaseModel):
    decompiler: str = "fission"
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
    decompiler: str = "fission"
    results: List[DecompileResultItem]
    time_ms: int

@app.get("/health")
def health():
    version = "unknown"
    try:
        r = subprocess.run([str(FISSION_BIN), "--version"], capture_output=True, text=True, timeout=5)
        version = r.stdout.strip() or r.stderr.strip()
    except Exception:
        pass
    return {"status": "ok", "decompiler": "fission", "version": version}

def run_fission_cli(args: List[str]):
    env = {
        **os.environ,
        "FISSION_SLEIGH_SPEC_DIR": SLEIGH_SPEC_DIR,
        "FISSION_RESOURCE_ROOT": RESOURCE_ROOT,
        "FISSION_GHIDRA_DATA_DIR": GHIDRA_DATA_DIR,
    }
    result = subprocess.run([str(FISSION_BIN)] + args, env=env, capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        raise HTTPException(status_code=500, detail=result.stderr or result.stdout)
    return json.loads(result.stdout)

def resolve_binary(binary: str) -> str:
    if binary.startswith("corpus/"):
        return "/" + binary
    return binary

@app.get("/functions")
def functions(binary: str):
    bin_path = resolve_binary(binary)
    data = run_fission_cli(["list", bin_path, "--json"])
    res = []
    for item in data:
        res.append({
            "address": item.get("address"),
            "name": item.get("name"),
            "size": item.get("size", 0),
            "kind": "function" if item.get("kind") == "code" else item.get("kind", "function")
        })
    return res

@app.get("/disasm")
def disasm(binary: str, addr: str):
    bin_path = resolve_binary(binary)
    data = run_fission_cli(["disasm", bin_path, "--addr", addr, "--function", "--json"])
    res = []
    for inst in data.get("instructions", []):
        res.append({
            "address": inst.get("address"),
            "bytes": inst.get("bytes"),
            "mnemonic": inst.get("instruction", "").split()[0].lower() if inst.get("instruction") else "",
            "operands": inst.get("instruction", "").split(None, 1)[1] if len(inst.get("instruction", "").split(None, 1)) > 1 else "",
            "length": len(inst.get("bytes", "")) // 2,
            "fallthrough": None, # Fission raw instruction JSON doesn't expose fallthrough easily
            "branch_target": None
        })
    return res

@app.get("/decode")
def decode(binary: str, addr: str):
    # Decode is mapped from disassembly in same manner
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
    bin_path = resolve_binary(binary)
    data = run_fission_cli(["raw-pcode", bin_path, "--addr", addr, "--json"])
    # Map raw-pcode output to schema
    res = []
    seq = 0
    for block in data.get("raw_pcode_blocks", []):
        for op in block.get("ops", []):
            output = None
            out_node = op.get("output")
            if out_node:
                # Map space_id to string representation
                space_id = out_node.get("space_id", 0)
                space_name = "unique" if space_id == 2 else "register" if space_id == 4 else "ram" if space_id == 3 else "const" if space_id == 0 else f"space_{space_id}"
                output = {
                    "space": space_name,
                    "offset": f"0x{out_node.get('offset', 0):x}",
                    "size": out_node.get("size", 0)
                }

            inputs = []
            for node in op.get("inputs", []):
                space_id = node.get("space_id", 0)
                space_name = "unique" if space_id == 2 else "register" if space_id == 4 else "ram" if space_id == 3 else "const" if space_id == 0 else f"space_{space_id}"
                inputs.append({
                    "space": space_name,
                    "offset": f"0x{node.get('offset', 0):x}",
                    "size": node.get("size", 0)
                })

            res.append({
                "seq": seq,
                "op": op.get("asm_mnemonic", op.get("opcode")),
                "output": output,
                "inputs": inputs
            })
            seq += 1
    return res

@app.get("/cfg")
def cfg(binary: str, addr: str):
    bin_path = resolve_binary(binary)
    data = run_fission_cli(["pcode-topology", bin_path, "--addr", addr, "--json"])
    # Map pcode-topology to schema
    blocks = []
    edges = []
    for block in data.get("raw_pcode_blocks", []):
        start = f"0x{block.get('start_address', 0):x}"
        # Estimate end address using terminal instruction size or approximation
        blocks.append({
            "start": start,
            "end": start # keep simple
        })
        for succ in block.get("successors", []):
            # Resolve successor address from index
            target_block = next((b for b in data.get("raw_pcode_blocks", []) if b.get("index") == succ), None)
            if target_block:
                edges.append({
                    "source": start,
                    "target": f"0x{target_block.get('start_address', 0):x}",
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
    with tempfile.NamedTemporaryFile(suffix=".bin", delete=False) as f_bin:
        f_bin.write(binary_bytes)
        tmp_bin_path = f_bin.name
    with tempfile.NamedTemporaryFile(suffix=".txt", mode="w", delete=False) as f_addrs:
        for addr in req.addresses:
            f_addrs.write(f"{addr}\n")
        tmp_addrs_path = f_addrs.name

    env = {
        **os.environ,
        "FISSION_SLEIGH_SPEC_DIR": SLEIGH_SPEC_DIR,
        "FISSION_RESOURCE_ROOT": RESOURCE_ROOT,
        "FISSION_GHIDRA_DATA_DIR": GHIDRA_DATA_DIR,
    }
    start = time.monotonic()
    try:
        result = subprocess.run(
            [str(FISSION_BIN), "decomp", tmp_bin_path, "--batch", tmp_addrs_path, "--json"],
            env=env, capture_output=True, text=True, timeout=120
        )
        elapsed = int((time.monotonic() - start) * 1000)
        if result.returncode != 0:
            raise HTTPException(status_code=500, detail=result.stderr or result.stdout)
        res_list = json.loads(result.stdout)
        results = []
        for item in res_list:
            results.append(DecompileResultItem(
                addr=item.get("addr"),
                name=item.get("name", "?"),
                code=item.get("code", ""),
                error=item.get("error")
            ))
        return BatchDecompileResponse(results=results, time_ms=elapsed)
    finally:
        os.unlink(tmp_bin_path)
        os.unlink(tmp_addrs_path)
