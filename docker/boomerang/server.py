"""Boomerang decompiler HTTP API server with batch support."""
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

        start = time.monotonic()
        result = subprocess.run(
            ["boomerang-cli", str(binary_path)],
            cwd=tmpdir,
            capture_output=True, text=True, timeout=120
        )

        # Walk and collect all .c files
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
            results.append(DecompileResultItem(
                addr=addr,
                name=f"fcn.{addr}",
                code=code if code else "",
                error=None if code else f"Decompilation failed: {result.stderr or result.stdout}"
            ))

        return BatchDecompileResponse(results=results, time_ms=elapsed)
