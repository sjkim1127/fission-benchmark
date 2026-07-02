"""Snowman decompiler and parity diagnostic API server."""
import base64
import os
import re
import subprocess
import tempfile
import time
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import disasm_helper

app = FastAPI(title="snowman-decompiler", version="1.0")
SNOWMAN_BIN = os.environ.get("SNOWMAN_BIN", "/snowman-master/build/nocode/nocode")

class DecompileRequest(BaseModel):
    binary_b64: str
    addr: str

class DecompileResponse(BaseModel):
    decompiler: str = "snowman"
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
    decompiler: str = "snowman"
    results: List[DecompileResultItem]
    time_ms: int

@app.get("/health")
def health():
    return {"status": "ok", "decompiler": "snowman", "version": "latest"}

def resolve_binary(binary: str) -> str:
    if binary.startswith("corpus/"):
        return "/" + binary
    return binary

@app.get("/functions")
def functions(binary: str):
    return disasm_helper.get_functions(resolve_binary(binary))

@app.get("/disasm")
def disasm(binary: str, addr: str, arch: str = "x86_64"):
    return disasm_helper.disassemble(resolve_binary(binary), addr, arch)

@app.get("/decode")
def decode(binary: str, addr: str, arch: str = "x86_64"):
    disasm_data = disasm(binary, addr, arch)
    res = []
    for inst in disasm_data:
        res.append({
            "address": inst.get("address"),
            "bytes": inst.get("bytes"),
            "length": inst.get("length"),
            "mnemonic": inst.get("mnemonic"),
            "prefixes": [],
            "modrm": None,
            "sib": None,
            "displacement": None,
            "immediate": None
        })
    return res

@app.get("/pcode")
def pcode(binary: str, addr: str):
    return []

@app.get("/cfg")
def cfg(binary: str, addr: str):
    return {"blocks": [], "edges": []}

FUNCTION_DEF_RE = re.compile(
    r"(?m)^\s*(?:[\w_][\w\s_*\(\),]*\s+)?([A-Za-z_][\w.]*)\s*\([^;{}]*\)\s*\{"
)
CONTROL_KEYWORDS = {"if", "for", "while", "switch", "do"}

def function_definition_count(code: str) -> int:
    return sum(
        1
        for match in FUNCTION_DEF_RE.finditer(code)
        if match.group(1) not in CONTROL_KEYWORDS
    )

def is_whole_program_output(code: str) -> bool:
    return len(code) >= 7900 or function_definition_count(code) > 3

def extract_snowman_function(code: str, addr_int: int) -> tuple[str, str]:
    """
    Search Snowman C++ output for the function at address addr_int.
    Snowman functions are named like: fun_[hex_address]
    e.g. fun_140001530 or fun_4015b0
    """
    hex_formats = [
        f"{addr_int:x}",
        f"{addr_int:X}",
    ]
    
    body = ""
    fn_name = f"fun_{addr_int:x}"

    for hf in hex_formats:
        # Match function definition, e.g. void fun_140001530(...) {
        fn_pattern = re.compile(
            rf"(?:^|\n)\s*[\w\s\*<>:,&]+?\bfun_{hf}\s*\([^;{{}}]*\)\s*\{{"
        )
        match = fn_pattern.search(code)
        if not match:
            continue

        fn_name = f"fun_{hf}"
        start = match.start()
        brace_start = code.find("{", match.end() - 1)
        if brace_start == -1:
            continue

        depth = 0
        for idx in range(brace_start, len(code)):
            ch = code[idx]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    body = code[start : idx + 1].strip()
                    break
        if body:
            break

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
    with tempfile.NamedTemporaryFile(suffix=".bin", delete=False) as f:
        f.write(binary_bytes)
        tmp_path = f.name

    start = time.monotonic()
    results = []
    try:
        for addr in req.addresses:
            try:
                result = subprocess.run(
                    [SNOWMAN_BIN, f"--from={addr}", "--print-cxx=-", tmp_path],
                    capture_output=True, text=True, timeout=120
                )
                if result.returncode != 0:
                    results.append(DecompileResultItem(addr=addr, name=f"func_{addr}", error=result.stderr or result.stdout))
                    continue
                code = result.stdout.strip()
                
                # Check if it contains multiple functions / whole program
                if is_whole_program_output(code):
                    try:
                        addr_int = int(addr, 16) if addr.lower().startswith("0x") else int(addr)
                        fn_name, extracted_code = extract_snowman_function(code, addr_int)
                        if extracted_code:
                            results.append(DecompileResultItem(addr=addr, name=fn_name, code=extracted_code))
                        else:
                            results.append(DecompileResultItem(
                                addr=addr,
                                name=f"func_{addr}",
                                error="Snowman returned whole-program output and target function extraction failed",
                            ))
                    except Exception as e:
                        results.append(DecompileResultItem(
                            addr=addr,
                            name=f"func_{addr}",
                            error=f"Snowman whole-program extraction error: {e}",
                        ))
                else:
                    results.append(DecompileResultItem(addr=addr, name=f"func_{addr}", code=code))
            except Exception as e:
                results.append(DecompileResultItem(addr=addr, error=str(e)))
        elapsed = int((time.monotonic() - start) * 1000)
        return BatchDecompileResponse(results=results, time_ms=elapsed)
    finally:
        os.unlink(tmp_path)
