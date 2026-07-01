"""Fission decompiler HTTP API server with batch support."""
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
    
    # Write binary
    with tempfile.NamedTemporaryFile(suffix=".bin", delete=False) as f_bin:
        f_bin.write(binary_bytes)
        tmp_bin_path = f_bin.name

    # Write addresses file (one hex address per line)
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
            [
                str(FISSION_BIN), "decomp", tmp_bin_path,
                "--addresses-file", tmp_addrs_path,
                "--json", "--resource-root", RESOURCE_ROOT
            ],
            capture_output=True, text=True, timeout=300, env=env,
        )
        elapsed = int((time.monotonic() - start) * 1000)

        if result.returncode != 0:
            raise HTTPException(status_code=500, detail=f"Fission CLI batch run failed: {result.stderr[:1000]}")

        try:
            data = json.loads(result.stdout)
            results = []
            for entry in data:
                results.append(DecompileResultItem(
                    addr=entry.get("address"),
                    name=entry.get("name", "?"),
                    code=entry.get("code", ""),
                    error=entry.get("error")
                ))
            return BatchDecompileResponse(results=results, time_ms=elapsed)
        except json.JSONDecodeError as e:
            raise HTTPException(status_code=500, detail=f"Failed to decode batch JSON: {e}\nStdout: {result.stdout[:500]}")
    finally:
        Path(tmp_bin_path).unlink(missing_ok=True)
        Path(tmp_addrs_path).unlink(missing_ok=True)
