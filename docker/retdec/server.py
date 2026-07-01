"""RetDec decompiler HTTP API server."""
import base64
import re
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


def extract_function_at_addr(c_code: str, addr: str) -> str:
    """Try to extract a function near the given address from retdec output.
    RetDec generates the whole file — we return the full output for scoring."""
    # Normalize addr to both 0x-prefixed and plain hex
    return c_code


@app.get("/health")
def health():
    return {"status": "ok", "decompiler": "retdec", "version": "5.0"}


@app.post("/decompile", response_model=DecompileResponse)
def decompile(req: DecompileRequest):
    binary_bytes = base64.b64decode(req.binary_b64)
    with tempfile.TemporaryDirectory() as tmpdir:
        # RetDec v5 requires .exe extension for PE files — use .exe unconditionally
        # since our corpus is Windows PE binaries
        binary_path = Path(tmpdir) / "target.exe"
        binary_path.write_bytes(binary_bytes)
        out_c = Path(tmpdir) / "target.c"

        start = time.monotonic()
        result = subprocess.run(
            [str(RETDEC_BIN), str(binary_path), "-o", str(out_c),
             "--select-ranges", f"{req.addr}-{hex(int(req.addr, 16) + 0x1000)}"],  # decompile range
            capture_output=True, text=True, timeout=120,
        )
        elapsed = int((time.monotonic() - start) * 1000)

        detail = (result.stderr + "\n" + result.stdout).strip()

        # RetDec may still succeed with non-zero exit for partial decompilation
        if result.returncode != 0 and not out_c.exists():
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

        name = f"func_{req.addr}"
        return DecompileResponse(name=name, code=code, time_ms=elapsed)
