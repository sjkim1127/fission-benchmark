"""Ghidra headless decompiler HTTP API server with batch support."""
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


@app.post("/decompile", response_model=DecompileResponse)
def decompile(req: DecompileRequest):
    # Backward compatibility
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
        # Build analyzeHeadless arguments passing all addresses
        args = [
            str(GHIDRA_HEADLESS), str(project_dir), "TempProject",
            "-import", str(binary_path),
            "-scriptPath", str(SCRIPT_DIR),
            "-postScript", "DecompileFunction.java",
        ] + req.addresses + [
            "-scriptlog", str(Path(tmpdir) / "script.log"),
            "-deleteProject",
        ]

        result = subprocess.run(
            args,
            env=os.environ,
            capture_output=True, text=True, timeout=300,
        )
        elapsed = int((time.monotonic() - start) * 1000)

        # Parse batch stdout looking for the ===BATCH_RESULT=== marker
        for line in result.stdout.splitlines():
            line = line.strip()
            marker = "===BATCH_RESULT==="
            if marker in line:
                try:
                    # Extract the exact JSON array between [ and ] to avoid suffixes like ' (GhidraScript)'
                    start_idx = line.find("[")
                    end_idx = line.rfind("]")
                    if start_idx == -1 or end_idx == -1 or end_idx < start_idx:
                        raise ValueError("Invalid array format in batch result line")
                    json_str = line[start_idx:end_idx + 1]
                    data = json.loads(json_str)
                    results = []
                    for item in data:
                        results.append(DecompileResultItem(
                            addr=item.get("addr"),
                            name=item.get("name", "?"),
                            code=item.get("code", ""),
                            error=item.get("error")
                        ))
                    return BatchDecompileResponse(results=results, time_ms=elapsed)
                except (json.JSONDecodeError, ValueError) as e:
                    raise HTTPException(status_code=500, detail=f"Failed to decode batch JSON: {e}\nStdout: {result.stdout[:500]}")

        detail = (result.stderr + "\n" + result.stdout)[-2000:]
        raise HTTPException(status_code=500, detail=f"Batch marker not found in output.\nLog details:\n{detail}")
