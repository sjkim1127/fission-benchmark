"""Radare2 + r2ghidra decompiler HTTP API server with batch support."""
import base64
import re
import tempfile
import time
from pathlib import Path
from typing import List, Optional

import r2pipe
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="radare2-decompiler", version="1.0")


class DecompileRequest(BaseModel):
    binary_b64: str
    addr: str


class DecompileResponse(BaseModel):
    decompiler: str = "radare2"
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
    decompiler: str = "radare2"
    results: List[DecompileResultItem]
    time_ms: int


def clean_r2_output(code: str) -> str:
    """Remove r2-specific noise: comment headers, address annotations, and preamble."""
    lines = code.splitlines()
    cleaned = []
    for line in lines:
        if re.match(r"\s*/\*\s*(r2dec|nocode|WARNING|XREFS|Function|/tmp|/proc)", line):
            continue
        if re.match(r"\s*#include\s*<", line):
            continue
        cleaned.append(line)
    return "\n".join(cleaned).strip()


@app.get("/health")
def health():
    return {"status": "ok", "decompiler": "radare2+r2ghidra", "version": "latest"}


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
    with tempfile.NamedTemporaryFile(suffix=".bin", delete=False) as f:
        f.write(binary_bytes)
        tmp_path = f.name

    start = time.monotonic()
    r2 = None
    results = []
    try:
        r2 = r2pipe.open(tmp_path, flags=["-2"])  # -2: suppress stderr
        r2.cmd("aaa")  # full analysis exactly once for the batch

        for addr in req.addresses:
            try:
                r2.cmd(f"s {addr}")
                name_info = r2.cmdj("afij") or []
                name = name_info[0].get("name", f"fcn.{addr}") if name_info else f"fcn.{addr}"

                code = r2.cmd("pdgd")  # decompile with ghidra backend
                if not code.strip():
                    results.append(DecompileResultItem(addr=addr, name=name, error="empty output"))
                    continue

                code = clean_r2_output(code)
                results.append(DecompileResultItem(addr=addr, name=name, code=code))
            except Exception as item_err:
                results.append(DecompileResultItem(addr=addr, error=str(item_err)))

        elapsed = int((time.monotonic() - start) * 1000)
        return BatchDecompileResponse(results=results, time_ms=elapsed)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if r2:
            r2.quit()
        Path(tmp_path).unlink(missing_ok=True)
