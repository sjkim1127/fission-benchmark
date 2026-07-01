"""rev.ng decompiler HTTP API server with batch support."""
import base64
import re
import subprocess
import tempfile
import time
from pathlib import Path
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="revng-decompiler", version="1.0")


class DecompileRequest(BaseModel):
    binary_b64: str
    addr: str


class DecompileResponse(BaseModel):
    decompiler: str = "revng"
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
    decompiler: str = "revng"
    results: List[DecompileResultItem]
    time_ms: int


def strip_ptml(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text)


@app.get("/health")
def health():
    result = subprocess.run(
        ["revng", "--version"],
        capture_output=True,
        text=True,
        timeout=10,
    )
    version = result.stdout.strip() or result.stderr.strip() or "unknown"
    return {"status": "ok", "decompiler": "revng", "version": version}


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
        results = []
        for addr in req.addresses:
            try:
                output_path = Path(tmpdir) / f"target_{addr}.c"
                result = subprocess.run(
                    [
                        "revng",
                        "artifact",
                        "decompile-to-single-file",
                        str(binary_path),
                        f"--entry={addr}",
                        "--analyze",
                        f"-o={output_path}",
                    ],
                    capture_output=True,
                    text=True,
                    timeout=240,
                )
                if result.returncode != 0:
                    results.append(DecompileResultItem(
                        addr=addr,
                        name=f"func_{addr}",
                        error=result.stderr[:500]
                    ))
                    continue

                code = strip_ptml(output_path.read_text(errors="replace")) if output_path.exists() else ""
                if not code.strip():
                    results.append(DecompileResultItem(addr=addr, name=f"func_{addr}", error="empty output"))
                    continue

                results.append(DecompileResultItem(addr=addr, name=f"func_{addr}", code=code))
            except Exception as e:
                results.append(DecompileResultItem(addr=addr, error=str(e)))

        elapsed = int((time.monotonic() - start) * 1000)
        return BatchDecompileResponse(results=results, time_ms=elapsed)
