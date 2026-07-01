"""Ghidra headless decompiler and parity diagnostic API server."""
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

app = FastAPI(title="ghidra-decompiler", version="1.0")
GHIDRA_HOME = Path("/opt/ghidra")
GHIDRA_HEADLESS = GHIDRA_HOME / "support" / "analyzeHeadless"
SCRIPT_DIR = Path("/opt/ghidra_scripts")

class DecompileRequest(BaseModel):
    binary_b64: str
    addr: str

class DecompileResponse(BaseModel):
    decompiler: str = "ghidra"
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
    decompiler: str = "ghidra"
    results: List[DecompileResultItem]
    time_ms: int

@app.get("/health")
def health():
    return {"status": "ok", "decompiler": "ghidra", "version": "12.0"}

def run_export_parity(binary_path: str, mode: str, addr: str = ""):
    if binary_path.startswith("corpus/"):
        binary_path = "/" + binary_path
    
    with tempfile.TemporaryDirectory() as tmpdir:
        project_dir = Path(tmpdir) / "proj"
        project_dir.mkdir()
        
        args = [
            str(GHIDRA_HEADLESS), str(project_dir), "TempProject",
            "-import", binary_path,
            "-scriptPath", str(SCRIPT_DIR),
            "-postScript", "ExportParity.java", mode, addr,
            "-deleteProject"
        ]
        result = subprocess.run(args, capture_output=True, text=True, timeout=120)
        for line in result.stdout.splitlines():
            if line.startswith("===RESULT==="):
                res = json.loads(line.replace("===RESULT===", ""))
                if isinstance(res, dict) and "error" in res:
                    raise HTTPException(status_code=500, detail=res["error"])
                return res
        raise HTTPException(status_code=500, detail=f"Headless script failed: {result.stderr or result.stdout}")

@app.get("/functions")
def functions(binary: str):
    return run_export_parity(binary, "functions")

@app.get("/disasm")
def disasm(binary: str, addr: str):
    return run_export_parity(binary, "disasm", addr)

@app.get("/decode")
def decode(binary: str, addr: str):
    # Map Ghidra disasm output to decode schema
    disasm_data = run_export_parity(binary, "disasm", addr)
    res = []
    for inst in disasm_data:
        b = inst.get("bytes", "")
        res.append({
            "address": inst.get("address"),
            "bytes": b,
            "length": inst.get("length", len(b) // 2),
            "mnemonic": inst.get("mnemonic", ""),
            "prefixes": [],
            "modrm": None,
            "sib": None,
            "displacement": None,
            "immediate": None
        })
    return res

@app.get("/pcode")
def pcode(binary: str, addr: str):
    return run_export_parity(binary, "pcode", addr)

@app.get("/cfg")
def cfg(binary: str, addr: str):
    return run_export_parity(binary, "cfg", addr)

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
        project_dir = Path(tmpdir) / "proj"
        project_dir.mkdir()

        start = time.monotonic()
        args = [
            str(GHIDRA_HEADLESS), str(project_dir), "TempProject",
            "-import", str(binary_path),
            "-scriptPath", str(SCRIPT_DIR),
            "-postScript", "DecompileFunction.java",
        ] + req.addresses + [
            "-scriptlog", str(Path(tmpdir) / "script.log"),
            "-deleteProject",
        ]

        result = subprocess.run(args, capture_output=True, text=True, timeout=300)
        elapsed = int((time.monotonic() - start) * 1000)

        for line in result.stdout.splitlines():
            if line.startswith("===BATCH_RESULT==="):
                try:
                    res_json = line.replace("===BATCH_RESULT===", "").strip()
                    if res_json.endswith("(GhidraScript)"):
                        res_json = res_json[:-len("(GhidraScript)")].strip()
                    res_list = json.loads(res_json)
                    return BatchDecompileResponse(results=res_list, time_ms=elapsed)
                except Exception as e:
                    raise HTTPException(status_code=500, detail=f"Failed to parse GhidraScript JSON: {str(e)}")

        raise HTTPException(status_code=500, detail=f"Ghidra batch decompilation script output marker not found. Output: {result.stdout}")
