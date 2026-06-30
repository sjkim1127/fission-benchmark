"""Snowman/nocode decompiler HTTP API server."""
import base64
import os
import subprocess
import tempfile
import time
from pathlib import Path
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

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


@app.get("/health")
def health():
    result = subprocess.run(
        [SNOWMAN_BIN, "--help"],
        capture_output=True,
        text=True,
        timeout=10,
    )
    version = "unknown"
    for line in result.stdout.splitlines():
        if line.startswith("Version:"):
            version = line.split(":", 1)[1].strip()
            break
    return {"status": "ok", "decompiler": "snowman", "version": version}


@app.post("/decompile", response_model=DecompileResponse)
def decompile(req: DecompileRequest):
    binary_bytes = base64.b64decode(req.binary_b64)
    with tempfile.NamedTemporaryFile(suffix=".bin", delete=False) as f:
        f.write(binary_bytes)
        tmp_path = f.name

    start = time.monotonic()
    try:
        result = subprocess.run(
            [SNOWMAN_BIN, f"--from={req.addr}", "--print-cxx=-", tmp_path],
            capture_output=True,
            text=True,
            timeout=180,
        )
        elapsed = int((time.monotonic() - start) * 1000)

        if result.returncode != 0:
            return DecompileResponse(
                name=f"func_{req.addr}",
                code="",
                time_ms=elapsed,
                error=(result.stderr or result.stdout or "snowman failed")[:500],
            )

        code = result.stdout.strip()
        if not code:
            return DecompileResponse(
                name=f"func_{req.addr}",
                code="",
                time_ms=elapsed,
                error="empty output",
            )

        return DecompileResponse(name=f"func_{req.addr}", code=code, time_ms=elapsed)
    finally:
        path = Path(tmp_path)
        if path.exists():
            path.unlink()
