"""Fission decompiler HTTP API server."""
import base64
import json
import os
import subprocess
import tempfile
import time
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="fission-decompiler", version="1.0")
FISSION_BIN = Path("/usr/local/bin/fission_cli")
SLEIGH_SPEC_DIR = os.environ.get("FISSION_SLEIGH_SPEC_DIR", "/sleigh-specs")


class DecompileRequest(BaseModel):
    binary_b64: str
    addr: str  # hex string e.g. "0x1400010a0"


class DecompileResponse(BaseModel):
    decompiler: str = "fission"
    name: str
    code: str
    time_ms: int
    error: str | None = None


@app.get("/health")
def health():
    version = "unknown"
    try:
        r = subprocess.run([str(FISSION_BIN), "--version"], capture_output=True, text=True, timeout=5)
        version = r.stdout.strip() or r.stderr.strip()
    except Exception:
        pass
    return {"status": "ok", "decompiler": "fission", "version": version}


@app.post("/decompile", response_model=DecompileResponse)
def decompile(req: DecompileRequest):
    binary_bytes = base64.b64decode(req.binary_b64)
    with tempfile.NamedTemporaryFile(suffix=".bin", delete=False) as f:
        f.write(binary_bytes)
        tmp_path = f.name

    env = {**os.environ, "FISSION_SLEIGH_SPEC_DIR": SLEIGH_SPEC_DIR}
    start = time.monotonic()
    try:
        result = subprocess.run(
            [str(FISSION_BIN), "decomp", tmp_path, "--addr", req.addr, "--json"],
            capture_output=True, text=True, timeout=120, env=env,
        )
        elapsed = int((time.monotonic() - start) * 1000)

        if result.returncode != 0:
            raise HTTPException(status_code=500, detail=result.stderr[:500])

        data = json.loads(result.stdout)
        if isinstance(data, list):
            data = data[0]

        return DecompileResponse(
            name=data.get("name", "?"),
            code=data.get("code", ""),
            time_ms=elapsed,
            error=data.get("error"),
        )
    finally:
        Path(tmp_path).unlink(missing_ok=True)
