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
BATCH_MARKER = "===BATCH_RESULT==="

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

def _extract_marked_json_line(text: str, marker: str) -> object | None:
    for line in text.splitlines():
        marker_index = line.find(marker)
        if marker_index < 0:
            continue
        payload = line[marker_index + len(marker):].strip()
        if payload.endswith("(GhidraScript)"):
            payload = payload[:-len("(GhidraScript)")].strip()
        return json.loads(payload)
    return None

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

@app.get("/health")
def health():
    return {"status": "ok", "decompiler": "ghidra", "version": "12.0"}

def run_export_parity(binary_path: str, mode: str, addr: str = ""):
    if not binary_path or not binary_path.strip():
        raise HTTPException(status_code=400, detail="Binary path cannot be empty")
    resolved = "/" + binary_path if binary_path.startswith("corpus/") else binary_path
    if not os.path.exists(resolved):
        raise HTTPException(status_code=404, detail=f"Binary not found: {resolved}")
    binary_path = resolved
    
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
            idx = line.find("===RESULT===")
            if idx >= 0:
                payload = line[idx + len("===RESULT==="):].strip()
                if payload.endswith("(GhidraScript)"):
                    payload = payload[:-len("(GhidraScript)")].strip()
                res = json.loads(payload)
                if isinstance(res, dict) and "error" in res:
                    raise HTTPException(status_code=500, detail=res["error"])
                return res
        raise HTTPException(status_code=500, detail=f"Headless script failed: {result.stderr or result.stdout}")

@app.get("/functions")
def functions(binary: str):
    return run_export_parity(binary, "functions")

@app.get("/disasm")
def disasm(binary: str, addr: str):
    validate_address(addr)
    return run_export_parity(binary, "disasm", addr)

@app.get("/decode")
def decode(binary: str, addr: str):
    validate_address(addr)
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
    validate_address(addr)
    return run_export_parity(binary, "pcode", addr)

@app.get("/cfg")
def cfg(binary: str, addr: str):
    validate_address(addr)
    return run_export_parity(binary, "cfg", addr)

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

def _run_ghidra_headless(binary_bytes: bytes, addresses: List[str]) -> List[DecompileResultItem]:
    with tempfile.TemporaryDirectory() as tmpdir:
        binary_path = Path(tmpdir) / "target.bin"
        binary_path.write_bytes(binary_bytes)
        project_dir = Path(tmpdir) / "proj"
        project_dir.mkdir()

        args = [
            str(GHIDRA_HEADLESS), str(project_dir), "TempProject",
            "-import", str(binary_path),
            "-scriptPath", str(SCRIPT_DIR),
            "-postScript", "DecompileFunction.java",
        ] + addresses + [
            "-scriptlog", str(Path(tmpdir) / "script.log"),
            "-deleteProject",
        ]

        script_log = Path(tmpdir) / "script.log"
        result = subprocess.run(args, capture_output=True, text=True, timeout=300)

        parse_sources = [result.stdout, result.stderr]
        if script_log.exists():
            parse_sources.append(script_log.read_text(errors="replace"))

        for source in parse_sources:
            res_list = None
            try:
                res_list = _extract_marked_json_line(source, BATCH_MARKER)
            except Exception:
                pass
            if res_list is not None:
                items = []
                for item in res_list:
                    items.append(DecompileResultItem(
                        addr=item.get("addr") or item.get("address"),
                        name=item.get("name", "?"),
                        code=item.get("code", ""),
                        error=item.get("error")
                    ))
                return items
        
        raise RuntimeError(f"Ghidra script failed or marker not found. Exit code {result.returncode}")

@app.post("/decompile_batch", response_model=BatchDecompileResponse)
def decompile_batch(req: BatchDecompileRequest):
    try:
        binary_bytes = base64.b64decode(req.binary_b64, validate=True)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid base64 payload")
        
    start = time.monotonic()
    try:
        results = _run_ghidra_headless(binary_bytes, req.addresses)
    except Exception:
        results = []
        for addr in req.addresses:
            try:
                single_results = _run_ghidra_headless(binary_bytes, [addr])
                if single_results:
                    results.append(single_results[0])
                else:
                    results.append(DecompileResultItem(addr=addr, error="Empty result returned"))
            except Exception as se:
                results.append(DecompileResultItem(addr=addr, error=f"Headless script failed: {str(se)}"))
                
    elapsed = int((time.monotonic() - start) * 1000)
    return BatchDecompileResponse(results=results, time_ms=elapsed)
