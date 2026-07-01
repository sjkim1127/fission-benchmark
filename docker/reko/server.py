"""FastAPI wrapper server for Reko decompiler CLI."""
import base64
import json
import os
import re
import subprocess
import tempfile
import time
from pathlib import Path
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="reko-decompiler", version="1.0")

# Reko paths inside container
REKO_DIR = Path("/opt/reko")
REKO_BIN = REKO_DIR / "decompile.dll"


class DecompileRequest(BaseModel):
    binary_b64: str
    addr: str


class DecompileResponse(BaseModel):
    decompiler: str = "reko"
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
    decompiler: str = "reko"
    results: List[DecompileResultItem]
    time_ms: int


@app.get("/health")
def health():
    # Verify dotnet and reko DLL are present
    if not REKO_BIN.exists():
        return {"status": "error", "error": "Reko binary decompile.dll missing"}
    return {"status": "ok", "decompiler": "reko", "version": "latest"}


def extract_function_by_address(c_file_path: Path, addr_int: int) -> tuple[str, str]:
    """
    Search Reko C output for a function corresponding to the given absolute address.

    Looks for Reko's address comment above the function, e.g.:
    // 0000000140001530: void rc4_init(...)
    or
    // 004015B0: void _rc4_init(...)
    """
    if not c_file_path.exists():
        return "", f"Source file {c_file_path.name} not found"

    code = c_file_path.read_text(errors="replace")

    # Match: // [hex_address]: [anything] [function_name] ( [anything] )
    # e.g., // 004015B0: void _rc4_init(Stack (arr byte) dwArg04, ...)
    pattern = re.compile(
        r'//\s*([0-9a-fA-F]+):\s*(?:[\w\s\*(),]+?)\s*(\w+)\s*\([^)]*\)',
        re.MULTILINE
    )

    matches = pattern.findall(code)
    fn_name = None

    for addr_hex, name in matches:
        try:
            val = int(addr_hex, 16)
            if val == addr_int:
                fn_name = name
                break
        except ValueError:
            continue

    if not fn_name:
        return "", f"Function at address {addr_int:#x} not matched in Reko address comments"

    # Search for the function definition of fn_name:
    # e.g. void _rc4_init(...) {
    fn_pattern = re.compile(rf'(?:^|\n)\s*[\w\s\*]+?\b{re.escape(fn_name)}\s*\([^;{{}}]*\)\s*\{{')
    match = fn_pattern.search(code)
    if not match:
        return fn_name, f"Function definition for {fn_name} ({addr_int:#x}) not found in code"

    # Balance braces to extract the function body
    brace_start = code.find("{", match.end() - 1)
    if brace_start == -1:
        return fn_name, f"Brace start not found for function {fn_name}"

    body = ""
    depth = 0
    for idx in range(brace_start, len(code)):
        ch = code[idx]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                body = code[match.start() : idx + 1].strip()
                break

    if not body:
        return fn_name, f"Balanced brace matching failed for function {fn_name}"

    return fn_name, body


@app.post("/decompile", response_model=DecompileResponse)
def decompile(req: DecompileRequest):
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
    
    # We must decompile in a unique temporary directory to avoid conflicts
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        tmp_binary = tmpdir_path / "target.bin"
        tmp_binary.write_bytes(binary_bytes)

        start = time.monotonic()
        results = []

        try:
            # Run Reko command line decompiler
            env = os.environ.copy()
            env["DOTNET_ROLL_FORWARD"] = "Major"
            
            result = subprocess.run(
                ["dotnet", str(REKO_BIN), str(tmp_binary)],
                cwd=tmpdir,
                env=env,
                capture_output=True,
                text=True,
                timeout=180,
            )
            
            # Reko generates target.reko/ folder in the same directory
            reko_dir = tmpdir_path / "target.reko"
            c_files = list(reko_dir.glob("*_text.c")) or list(reko_dir.glob("*.c"))
            
            # Find the primary C file (prefer *_text.c or first .c)
            c_file = None
            for cf in c_files:
                if cf.name.endswith("_text.c"):
                    c_file = cf
                    break
            if not c_file and c_files:
                c_file = c_files[0]

            for addr in req.addresses:
                try:
                    # Resolve address to integer
                    addr_int = int(addr, 16) if addr.lower().startswith("0x") else int(addr)
                    
                    if not c_file:
                        results.append(DecompileResultItem(
                            addr=addr,
                            error=f"No C output generated by Reko. Stderr: {result.stderr[:500]}"
                        ))
                        continue

                    fn_name, code = extract_function_by_address(c_file, addr_int)
                    if not code:
                        results.append(DecompileResultItem(addr=addr, error=f"Function body extraction failed at address {addr_int:#x}"))
                    else:
                        results.append(DecompileResultItem(addr=addr, name=fn_name, code=code))
                except Exception as e:
                    results.append(DecompileResultItem(addr=addr, error=str(e)))

        except subprocess.TimeoutExpired:
            for addr in req.addresses:
                results.append(DecompileResultItem(addr=addr, error="Reko decompile timed out (180s)"))
        except Exception as e:
            for addr in req.addresses:
                results.append(DecompileResultItem(addr=addr, error=f"Internal wrapper error: {e}"))

        elapsed = int((time.monotonic() - start) * 1000)
        return BatchDecompileResponse(results=results, time_ms=elapsed)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
