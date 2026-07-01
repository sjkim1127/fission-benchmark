"""Ghidra headless decompiler HTTP API server."""
import base64
import json
import os
import subprocess
import tempfile
import time
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="ghidra-decompiler", version="1.0")
GHIDRA_HOME = Path("/opt/ghidra")
GHIDRA_HEADLESS = GHIDRA_HOME / "support" / "analyzeHeadless"
SCRIPT_DIR = Path("/opt/ghidra_scripts")


class DecompileRequest(BaseModel):
    binary_b64: str
    addr: str


class DecompileResponse(BaseModel):
    decompiler: str = "ghidra"
    name: str
    code: str
    time_ms: int
    error: str | None = None


@app.get("/health")
def health():
    return {"status": "ok", "decompiler": "ghidra", "version": "12.0"}


@app.post("/decompile", response_model=DecompileResponse)
def decompile(req: DecompileRequest):
    binary_bytes = base64.b64decode(req.binary_b64)
    with tempfile.TemporaryDirectory() as tmpdir:
        binary_path = Path(tmpdir) / "target.bin"
        binary_path.write_bytes(binary_bytes)
        project_dir = Path(tmpdir) / "proj"
        project_dir.mkdir()

        start = time.monotonic()
        result = subprocess.run(
            [
                str(GHIDRA_HEADLESS), str(project_dir), "TempProject",
                "-import", str(binary_path),
                "-scriptPath", str(SCRIPT_DIR),
                "-postScript", "DecompileFunction.java", req.addr,
                "-scriptlog", str(Path(tmpdir) / "script.log"),
                "-deleteProject",
            ],
            env=os.environ,
            capture_output=True, text=True, timeout=180,
        )
        elapsed = int((time.monotonic() - start) * 1000)

        # Ghidra prefixes script output with log metadata in headless mode.
        for line in result.stdout.splitlines():
            line = line.strip()
            json_start = line.find("{")
            if json_start >= 0:
                json_end = line.rfind("}")
                if json_end < json_start:
                    continue
                try:
                    data = json.loads(line[json_start:json_end + 1])
                    if "error" in data:
                        return DecompileResponse(name="?", code="", time_ms=elapsed, error=data["error"])
                    return DecompileResponse(name=data["name"], code=data["code"], time_ms=elapsed)
                except json.JSONDecodeError:
                    pass

        detail = (result.stderr + "\n" + result.stdout)[-2000:]
        raise HTTPException(status_code=500, detail=detail)
