"""rev.ng decompiler HTTP API server."""
import base64
import re
import subprocess
import tempfile
import time
from pathlib import Path

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
    error: str | None = None


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
    binary_bytes = base64.b64decode(req.binary_b64)
    with tempfile.TemporaryDirectory() as tmpdir:
        binary_path = Path(tmpdir) / "target.bin"
        output_path = Path(tmpdir) / "target.c"
        binary_path.write_bytes(binary_bytes)

        start = time.monotonic()
        result = subprocess.run(
            [
                "revng",
                "artifact",
                "decompile-to-single-file",
                str(binary_path),
                f"--entry={req.addr}",
                "--analyze",
                f"-o={output_path}",
            ],
            capture_output=True,
            text=True,
            timeout=240,
        )
        elapsed = int((time.monotonic() - start) * 1000)

        if result.returncode != 0:
            raise HTTPException(status_code=500, detail=result.stderr[:500])

        code = strip_ptml(output_path.read_text(errors="replace")) if output_path.exists() else ""
        if not code.strip():
            return DecompileResponse(
                name=f"func_{req.addr}",
                code="",
                time_ms=elapsed,
                error="empty output",
            )

        return DecompileResponse(name=f"func_{req.addr}", code=code, time_ms=elapsed)
