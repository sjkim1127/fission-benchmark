"""Radare2 decompiler and parity diagnostic API server."""
import base64
import os
import re
import tempfile
import time
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import r2pipe
from boundary import (
    inject_address_anchor,
    parse_addr_int,
    rewrite_function_name,
)

app = FastAPI(title="radare2-decompiler", version="1.0")


class DecompileRequest(BaseModel):
    binary_b64: str
    addr: str


class DecompileResponse(BaseModel):
    decompiler: str = "radare2"
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
    decompiler: str = "radare2"
    results: List[DecompileResultItem]
    time_ms: int


@app.get("/health")
def health():
    return {"status": "ok", "decompiler": "radare2", "version": "latest"}


def resolve_binary(binary: str) -> str:
    if binary.startswith("corpus/"):
        return "/" + binary
    return binary


def run_r2_cmd(binary: str, cmd: str):
    bin_path = resolve_binary(binary)
    r2 = r2pipe.open(bin_path)
    r2.cmd("aaa")
    res = r2.cmdj(cmd)
    r2.quit()
    return res


@app.get("/functions")
def functions(binary: str):
    data = run_r2_cmd(binary, "aflj")
    res = []
    for item in data or []:
        res.append({
            "address": f"0x{item.get('offset'):x}",
            "name": item.get("name"),
            "size": item.get("size", 0),
            "kind": "function",
        })
    return res


@app.get("/disasm")
def disasm(binary: str, addr: str):
    data = run_r2_cmd(binary, f"pdfj @ {addr}")
    res = []
    if data and "ops" in data:
        for inst in data["ops"]:
            res.append({
                "address": f"0x{inst.get('offset'):x}",
                "bytes": inst.get("bytes"),
                "mnemonic": inst.get("type", ""),
                "operands": inst.get("opcode", ""),
                "length": inst.get("size"),
                "fallthrough": f"0x{inst.get('offset') + inst.get('size'):x}",
                "branch_target": None,
            })
    return res


@app.get("/decode")
def decode(binary: str, addr: str):
    disasm_data = disasm(binary, addr)
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
            "immediate": None,
        })
    return res


@app.get("/pcode")
def pcode(binary: str, addr: str):
    return []


@app.get("/cfg")
def cfg(binary: str, addr: str):
    data = run_r2_cmd(binary, f"afbj @ {addr}")
    blocks = []
    edges = []
    for block in data or []:
        start = f"0x{block.get('addr'):x}"
        blocks.append({
            "start": start,
            "end": f"0x{block.get('addr') + block.get('size'):x}",
        })
        if block.get("jump") is not None:
            edges.append({
                "source": start,
                "target": f"0x{block.get('jump'):x}",
                "kind": "branch",
            })
        if block.get("fail") is not None:
            edges.append({
                "source": start,
                "target": f"0x{block.get('fail'):x}",
                "kind": "branch",
            })
    return {"blocks": blocks, "edges": edges}


def _stable_name(addr: str) -> str:
    try:
        return f"fcn_{parse_addr_int(addr):x}"
    except Exception:
        return f"fcn_{addr.replace('0x', '')}"


def normalize_r2_decompiled(code: str, addr: str, r2_name: str | None = None) -> tuple[str, str]:
    """Strip r2 prefixes and anchor the requested entry address."""
    if not code:
        return _stable_name(addr), ""
    stable = _stable_name(addr)
    text = code
    # Common r2 name prefixes in pdg output
    candidates = []
    if r2_name:
        candidates.append(r2_name)
        candidates.append(r2_name.split(".")[-1])
    # Discover function names in output: dbg.foo, sym.bar, fcn.0040...
    for m in re.finditer(
        r"\b((?:dbg|sym|fcn|loc|entry|section)\.[\w.]+|[A-Za-z_]\w*)\s*\(",
        text,
    ):
        candidates.append(m.group(1))
    # Prefer first definition-looking name
    renamed = False
    for cand in candidates:
        if cand in {"if", "for", "while", "switch", "return"}:
            continue
        if re.search(rf"\b{re.escape(cand)}\s*\(", text):
            text = rewrite_function_name(text, cand, stable)
            renamed = True
            break
    if not renamed:
        # Force rename of first C-like def
        m = re.search(
            r"(?m)^\s*(?:[\w_][\w\s_*\(\),]*\s+)?([A-Za-z_][\w.]*)\s*\([^;{}]*\)\s*\{",
            text,
        )
        if m and m.group(1) not in {"if", "for", "while", "switch"}:
            text = rewrite_function_name(text, m.group(1), stable)
    # Strip leftover dotted identifiers that confuse diagnostics
    text = re.sub(r"\b(?:dbg|sym)\.([A-Za-z_]\w*)", r"\1", text)
    text = inject_address_anchor(text, addr, "radare2")
    return stable, text


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
        r2 = r2pipe.open(tmp_path)
        r2.cmd("aaa")
        for addr in req.addresses:
            try:
                r2.cmd(f"s {addr}")
                info = r2.cmdj("afij") or []
                r2_name = None
                if isinstance(info, list) and info:
                    r2_name = info[0].get("name")
                elif isinstance(info, dict):
                    r2_name = info.get("name")
                code = r2.cmd(f"pdg @ {addr}") or ""
                name, normalized = normalize_r2_decompiled(code, addr, r2_name)
                if not normalized.strip():
                    results.append(
                        DecompileResultItem(
                            addr=addr, name=name, error="empty radare2 pdg output"
                        )
                    )
                else:
                    results.append(
                        DecompileResultItem(addr=addr, name=name, code=normalized)
                    )
            except Exception as e:
                results.append(DecompileResultItem(addr=addr, error=str(e)))
        r2.quit()
        elapsed = int((time.monotonic() - start) * 1000)
        return BatchDecompileResponse(results=results, time_ms=elapsed)
    finally:
        os.unlink(tmp_path)
