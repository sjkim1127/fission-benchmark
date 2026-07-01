"""RetDec decompiler HTTP API server."""
import base64
import subprocess
import tempfile
import time
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="retdec-decompiler", version="1.0")
RETDEC_BIN = Path("/opt/retdec/retdec-decompiler")


class DecompileRequest(BaseModel):
    binary_b64: str
    addr: str


class DecompileResponse(BaseModel):
    decompiler: str = "retdec"
    name: str
    code: str
    time_ms: int
    error: str | None = None


@app.get("/health")
def health():
    return {"status": "ok", "decompiler": "retdec", "version": "5.0"}


@app.post("/decompile", response_model=DecompileResponse)
def decompile(req: DecompileRequest):
    binary_bytes = base64.b64decode(req.binary_b64)
    with tempfile.TemporaryDirectory() as tmpdir:
        binary_path = Path(tmpdir) / "target.exe"
        binary_path.write_bytes(binary_bytes)
        out_c = Path(tmpdir) / "target.c"

        start = time.monotonic()
        result = subprocess.run(
            [str(RETDEC_BIN), str(binary_path), "-o", str(out_c)],
            capture_output=True, text=True, timeout=120,
        )
        elapsed = int((time.monotonic() - start) * 1000)

        detail = (result.stderr + "\n" + result.stdout).strip()
        if result.returncode != 0:
            return DecompileResponse(
                name=f"func_{req.addr}",
                code="",
                time_ms=elapsed,
                error=detail[:500] or f"retdec exited with {result.returncode}",
            )

        code = out_c.read_text(errors="replace") if out_c.exists() else ""
        if not code.strip():
            return DecompileResponse(
                name=f"func_{req.addr}",
                code="",
                time_ms=elapsed,
                error=detail[:500] or "retdec produced no output",
            )

        # Extract function name from addr hint
        name = f"func_{req.addr}"
        return DecompileResponse(name=name, code=code, time_ms=elapsed)
