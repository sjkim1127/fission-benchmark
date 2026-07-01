"""Radare2 + r2ghidra decompiler HTTP API server."""
import base64
import re
import tempfile
import time
from pathlib import Path

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
    error: str | None = None


def clean_r2_output(code: str) -> str:
    """Remove r2-specific noise: comment headers, address annotations, and preamble."""
    lines = code.splitlines()
    cleaned = []
    for line in lines:
        # Skip r2dec header comments (/* r2dec ... */ style)
        if re.match(r"\s*/\*\s*(r2dec|nocode|WARNING|XREFS|Function|\/tmp|\/proc)", line):
            continue
        # Skip #include lines injected by r2ghidra
        if re.match(r"\s*#include\s*<", line):
            continue
        cleaned.append(line)
    return "\n".join(cleaned).strip()


@app.get("/health")
def health():
    return {"status": "ok", "decompiler": "radare2+r2ghidra", "version": "latest"}


@app.post("/decompile", response_model=DecompileResponse)
def decompile(req: DecompileRequest):
    binary_bytes = base64.b64decode(req.binary_b64)
    with tempfile.NamedTemporaryFile(suffix=".bin", delete=False) as f:
        f.write(binary_bytes)
        tmp_path = f.name

    start = time.monotonic()
    r2 = None
    try:
        r2 = r2pipe.open(tmp_path, flags=["-2"])  # -2: suppress stderr
        r2.cmd("aaa")  # full analysis
        r2.cmd(f"s {req.addr}")
        name_info = r2.cmdj("afij") or []
        name = name_info[0].get("name", f"fcn.{req.addr}") if name_info else f"fcn.{req.addr}"

        # r2ghidra decompilation
        code = r2.cmd("pdgd")  # decompile with ghidra backend
        elapsed = int((time.monotonic() - start) * 1000)

        if not code.strip():
            return DecompileResponse(name=name, code="", time_ms=elapsed, error="empty output")

        code = clean_r2_output(code)
        return DecompileResponse(name=name, code=code, time_ms=elapsed)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if r2:
            r2.quit()
        Path(tmp_path).unlink(missing_ok=True)
