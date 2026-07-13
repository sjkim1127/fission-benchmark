"""RetDec decompiler HTTP adapter.

Contract: POST /decompile {binary_b64, addr} → single-function C with address anchor.
RetDec emits whole-program C with ``// Address range: 0xSTART - 0xEND`` markers;
we slice the matching function for the requested VA.
"""
from __future__ import annotations

import base64
import os
import re
import subprocess
import tempfile
import time
from pathlib import Path
from typing import List, Optional, Tuple

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from boundary import (
    address_hex_forms,
    extract_braced_unit,
    extract_function_by_name_patterns,
    inject_address_anchor,
    parse_addr_int,
    rewrite_function_name,
)

app = FastAPI(title="retdec-decompiler", version="1.0")

RETDEC_BIN = os.environ.get("RETDEC_BIN", "retdec-decompiler")
# Optional: prefer range-limited decompile when size unknown use a window.
SELECT_WINDOW = int(os.environ.get("RETDEC_SELECT_WINDOW", "0"), 0)  # 0 = full binary

# // Address range: 0x4015b0 - 0x4015d5
# // Address range: 4015b0-4015d5
ADDR_RANGE_RE = re.compile(
    r"(?im)^//\s*Address range:\s*(0x)?([0-9a-fA-F]+)\s*-\s*(0x)?([0-9a-fA-F]+)\s*$"
)
FUNC_DEF_RE = re.compile(
    r"(?m)^\s*(?:[\w_][\w\s_*\(\),]*\s+)?([A-Za-z_][\w]*)\s*\([^;{}]*\)\s*\{"
)
CONTROL = frozenset({"if", "for", "while", "switch", "do", "return", "sizeof"})


class DecompileRequest(BaseModel):
    binary_b64: str
    addr: str


class DecompileResponse(BaseModel):
    decompiler: str = "retdec"
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
    decompiler: str = "retdec"
    results: List[DecompileResultItem]
    time_ms: int


def _version_string() -> str:
    try:
        proc = subprocess.run(
            [RETDEC_BIN, "--version"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        text = (proc.stdout or proc.stderr or "").strip()
        for line in text.splitlines():
            if "version" in line.lower():
                return line.strip()[:80]
        return text.splitlines()[0][:80] if text else "unknown"
    except Exception as exc:
        return f"error:{exc}"


@app.get("/health")
def health():
    path = Path(RETDEC_BIN)
    # also resolve from PATH
    which = subprocess.run(["which", "retdec-decompiler"], capture_output=True, text=True)
    ok = path.exists() or which.returncode == 0
    return {
        "status": "ok" if ok else "error",
        "decompiler": "retdec",
        "version": _version_string() if ok else "missing",
        "bin": RETDEC_BIN,
    }


def validate_address(addr: str) -> int:
    if not addr or not str(addr).strip():
        raise HTTPException(status_code=400, detail="Address cannot be empty")
    try:
        return parse_addr_int(addr)
    except ValueError:
        raise HTTPException(status_code=400, detail=f"Invalid address format: {addr}")


def run_retdec(binary_path: Path, *, select_start: Optional[int] = None) -> str:
    """Run retdec-decompiler; return C source text."""
    with tempfile.TemporaryDirectory(prefix="retdec_") as tmp:
        out_c = Path(tmp) / "out.c"
        cmd = [
            RETDEC_BIN,
            "--output",
            str(out_c),
            "--cleanup",
            "--silent",
            str(binary_path),
        ]
        # Optional window around requested entry (experimental speedup).
        if select_start is not None and SELECT_WINDOW > 0:
            end = select_start + SELECT_WINDOW
            cmd[1:1] = [
                "--select-ranges",
                f"0x{select_start:x}-0x{end:x}",
            ]
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300,
            cwd=tmp,
        )
        if out_c.is_file() and out_c.stat().st_size > 0:
            return out_c.read_text(errors="replace")
        # RetDec sometimes writes beside input
        sibling = binary_path.with_suffix(binary_path.suffix + ".c")
        if sibling.is_file():
            return sibling.read_text(errors="replace")
        detail = (proc.stderr or proc.stdout or "retdec failed").strip()
        raise RuntimeError(detail[:2000] or f"retdec exit {proc.returncode}")


def _addr_int_forms(addr: str) -> set:
    forms = set()
    try:
        v = parse_addr_int(addr)
    except Exception:
        return forms
    forms.add(v)
    for base in (0x140000000, 0x400000, 0x10000000):
        if v >= base:
            forms.add(v - base)
        forms.add(v + base)  # rarely needed
    # strip high bits sometimes used in comments
    forms.add(v & 0xFFFFFFFF)
    forms.add(v & 0xFFFFF)
    return forms


def list_address_ranges(code: str) -> List[Tuple[int, int, int]]:
    """Return list of (start, end, comment_line_start_index)."""
    out: List[Tuple[int, int, int]] = []
    for m in ADDR_RANGE_RE.finditer(code):
        try:
            start = int(m.group(2), 16)
            end = int(m.group(4), 16)
        except ValueError:
            continue
        if end < start:
            start, end = end, start
        out.append((start, end, m.start()))
    return out


def extract_function_at_addr(code: str, addr: str) -> Tuple[str, str]:
    """Extract (name, body) for requested address from RetDec C dump."""
    if not code or not code.strip():
        return "", "empty retdec output"

    targets = _addr_int_forms(addr)
    ranges = list_address_ranges(code)

    # Prefer range whose start matches entry; else containing range.
    best_pos = None
    for start, end, pos in ranges:
        if start in targets or any(start <= t < end or start <= t <= end for t in targets):
            # exact start wins
            if start in targets:
                best_pos = pos
                break
            if best_pos is None:
                best_pos = pos
    if best_pos is not None:
        # Find first function definition after the address comment.
        window = code[best_pos : best_pos + 8000]
        m = FUNC_DEF_RE.search(window)
        if m and m.group(1) not in CONTROL:
            abs_start = best_pos + m.start()
            body = extract_braced_unit(code, abs_start)
            if body:
                return m.group(1), body

    # Fallback: name patterns fun_*/function_* with hex forms
    names: List[str] = []
    for hf in address_hex_forms(addr):
        h = hf[2:] if hf.lower().startswith("0x") else hf
        names.extend(
            [
                f"function_{h}",
                f"function_{h.lower()}",
                f"fun_{h}",
                f"func_{h}",
                f"sub_{h}",
            ]
        )
    try:
        bare = f"{parse_addr_int(addr):x}"
        names.extend([f"function_{bare}", f"fun_{bare}"])
    except Exception:
        pass
    name, body = extract_function_by_name_patterns(code, names)
    if body:
        return name, body

    return "", f"Function at {addr} not found in RetDec address-range output"


def normalize_unit(name: str, body: str, addr: str) -> Tuple[str, str]:
    stable = f"fun_{parse_addr_int(addr):x}"
    if name and name != stable:
        body = rewrite_function_name(body, name, stable)
    body = inject_address_anchor(body, addr, "retdec")
    return stable, body


def parse_functions_inventory(code: str) -> list:
    """Build GET /functions inventory from address-range comments."""
    res = []
    seen = set()
    for start, end, pos in list_address_ranges(code):
        key = f"0x{start:x}"
        if key in seen:
            continue
        window = code[pos : pos + 4000]
        m = FUNC_DEF_RE.search(window)
        name = m.group(1) if m and m.group(1) not in CONTROL else f"fun_{start:x}"
        seen.add(key)
        res.append(
            {
                "address": key,
                "name": name,
                "size": max(0, end - start),
                "kind": "function",
            }
        )
    return res


@app.get("/functions")
def functions(binary: str):
    if not binary or not binary.strip():
        raise HTTPException(status_code=400, detail="Binary path cannot be empty")
    resolved = "/" + binary if binary.startswith("corpus/") else binary
    if not os.path.exists(resolved):
        raise HTTPException(status_code=404, detail=f"Binary not found: {resolved}")
    try:
        code = run_retdec(Path(resolved))
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
    return parse_functions_inventory(code)


@app.post("/decompile", response_model=DecompileResponse)
def decompile(req: DecompileRequest):
    batch = BatchDecompileRequest(binary_b64=req.binary_b64, addresses=[req.addr])
    start = time.monotonic()
    try:
        resp = decompile_batch(batch)
        elapsed = int((time.monotonic() - start) * 1000)
        item = resp.results[0]
        if item.error:
            return DecompileResponse(name="?", code="", time_ms=elapsed, error=item.error)
        return DecompileResponse(name=item.name, code=item.code, time_ms=elapsed)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@app.post("/decompile_batch", response_model=BatchDecompileResponse)
def decompile_batch(req: BatchDecompileRequest):
    try:
        binary_bytes = base64.b64decode(req.binary_b64, validate=True)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid base64 payload")

    start = time.monotonic()
    with tempfile.NamedTemporaryFile(suffix=".bin", delete=False) as f:
        f.write(binary_bytes)
        tmp_path = Path(f.name)

    results: List[DecompileResultItem] = []
    try:
        valid_addrs: List[str] = []
        for addr in req.addresses:
            try:
                validate_address(addr)
                valid_addrs.append(addr)
            except HTTPException as he:
                results.append(DecompileResultItem(addr=addr, error=str(he.detail)))

        if not valid_addrs:
            elapsed = int((time.monotonic() - start) * 1000)
            return BatchDecompileResponse(results=results, time_ms=elapsed)

        # One full decompilation for the whole binary (shared dump).
        try:
            code = run_retdec(tmp_path)
        except Exception as exc:
            err = str(exc)
            for addr in valid_addrs:
                results.append(
                    DecompileResultItem(addr=addr, name=f"fun_{addr}", error=err)
                )
            elapsed = int((time.monotonic() - start) * 1000)
            return BatchDecompileResponse(results=results, time_ms=elapsed)

        for addr in valid_addrs:
            name, body = extract_function_at_addr(code, addr)
            if not body:
                results.append(
                    DecompileResultItem(
                        addr=addr,
                        name=f"fun_{parse_addr_int(addr):x}",
                        error=name or "extraction failed",
                    )
                )
                continue
            stable, normalized = normalize_unit(name, body, addr)
            results.append(
                DecompileResultItem(addr=addr, name=stable, code=normalized)
            )
        elapsed = int((time.monotonic() - start) * 1000)
        return BatchDecompileResponse(results=results, time_ms=elapsed)
    finally:
        try:
            tmp_path.unlink()
        except OSError:
            pass
