"""angr decompiler HTTP API server with batch support."""
import base64
import tempfile
import time
from pathlib import Path
from typing import List, Optional

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
    decompiler: str = "angr"
    results: List[DecompileResultItem]
    time_ms: int


@app.get("/health")
def health():
    return {"status": "ok", "decompiler": "angr", "version": angr.__version__}


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
    results = []
    try:
        project = angr.Project(tmp_path, auto_load_libs=False)
        cfg = project.analyses.CFGFast(normalize=True, data_references=True)
        for addr_str in req.addresses:
            try:
                addr = int(addr_str, 16)
                function = cfg.kb.functions.get(addr)
                if function is None:
                    results.append(DecompileResultItem(addr=addr_str, error=f"function not found at {addr_str}"))
                    continue

                decompilation = project.analyses.Decompiler(function, cfg=cfg.model)
                codegen = getattr(decompilation, "codegen", None)
                code = getattr(codegen, "text", "") if codegen is not None else ""

                if not code.strip():
                    results.append(DecompileResultItem(addr=addr_str, name=function.name, error="empty output"))
                    continue

                results.append(DecompileResultItem(addr=addr_str, name=function.name, code=code))
            except Exception as item_err:
                results.append(DecompileResultItem(addr=addr_str, error=str(item_err)))

        elapsed = int((time.monotonic() - start) * 1000)
        return BatchDecompileResponse(results=results, time_ms=elapsed)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    finally:
        Path(tmp_path).unlink(missing_ok=True)
