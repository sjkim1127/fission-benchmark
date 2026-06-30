"""angr decompiler HTTP API server."""
import base64
import tempfile
import time
from pathlib import Path

import angr
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="angr-decompiler", version="1.0")


class DecompileRequest(BaseModel):
    binary_b64: str
    addr: str


class DecompileResponse(BaseModel):
    decompiler: str = "angr"
    name: str
    code: str
    time_ms: int
    error: str | None = None


@app.get("/health")
def health():
    return {"status": "ok", "decompiler": "angr", "version": angr.__version__}


@app.post("/decompile", response_model=DecompileResponse)
def decompile(req: DecompileRequest):
    binary_bytes = base64.b64decode(req.binary_b64)
    with tempfile.NamedTemporaryFile(suffix=".bin", delete=False) as f:
        f.write(binary_bytes)
        tmp_path = f.name

    start = time.monotonic()
    try:
        addr = int(req.addr, 16)
        project = angr.Project(tmp_path, auto_load_libs=False)
        cfg = project.analyses.CFGFast(normalize=True, data_references=True)
        function = cfg.kb.functions.get(addr)
        if function is None:
            raise HTTPException(status_code=404, detail=f"function not found at {req.addr}")

        decompilation = project.analyses.Decompiler(function, cfg=cfg.model)
        codegen = getattr(decompilation, "codegen", None)
        code = getattr(codegen, "text", "") if codegen is not None else ""
        elapsed = int((time.monotonic() - start) * 1000)

        if not code.strip():
            return DecompileResponse(
                name=function.name,
                code="",
                time_ms=elapsed,
                error="empty output",
            )

        return DecompileResponse(name=function.name, code=code, time_ms=elapsed)
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    finally:
        Path(tmp_path).unlink(missing_ok=True)
