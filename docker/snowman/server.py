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
from boundary import (
    address_hex_forms,
    count_function_defs,
    extract_braced_unit,
    extract_function_by_name_patterns,
    inject_address_anchor,
    parse_addr_int,
    rewrite_function_name,
)

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


def validate_address(addr: str) -> int:
    if not addr or not addr.strip():
        raise HTTPException(status_code=400, detail="Address cannot be empty")
    try:
        return parse_addr_int(addr)
    except ValueError:
        raise HTTPException(status_code=400, detail=f"Invalid address format: {addr}")


def resolve_binary(binary: str) -> str:
    if not binary or not binary.strip():
        raise HTTPException(status_code=400, detail="Binary path cannot be empty")
    resolved = "/" + binary if binary.startswith("corpus/") else binary
    if not os.path.exists(resolved):
        raise HTTPException(status_code=404, detail=f"Binary not found: {resolved}")
    if os.path.getsize(resolved) == 0:
        raise HTTPException(status_code=400, detail="Binary file is empty")
    return resolved


@app.get("/functions")
def functions(binary: str):
    return disasm_helper.get_functions(resolve_binary(binary))


@app.get("/disasm")
def disasm(binary: str, addr: str, arch: str = "x86_64"):
    validate_address(addr)
    return disasm_helper.disassemble(resolve_binary(binary), addr, arch)


@app.get("/decode")
def decode(binary: str, addr: str, arch: str = "x86_64"):
    validate_address(addr)
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
            "immediate": None,
        })
    return res


@app.get("/pcode")
def pcode(binary: str, addr: str):
    return []


@app.get("/cfg")
def cfg(binary: str, addr: str):
    validate_address(addr)
    return {"blocks": [], "edges": []}


def is_whole_program_output(code: str) -> bool:
    return len(code) >= 7900 or count_function_defs(code) > 3


def _strip0x(h):
    h = h.lower()
    return h[2:] if h.startswith("0x") else h


def snowman_name_candidates(addr, binary_bytes=None):
    # type: (str, Optional[bytes]) -> List[str]
    """Possible Snowman symbol spellings for a VA/RVA (and PE symbols if known)."""
    names = []  # type: List[str]
    # PE/COFF symbols first — unstripped MinGW keeps real names (_count_bits).
    if binary_bytes:
        try:
            names.extend(disasm_helper.symbol_names_for_address(binary_bytes, addr))
        except Exception:
            pass
    for hf in address_hex_forms(addr):
        h = _strip0x(hf)
        names.extend([
            "fun_{}".format(h),
            "fun_{}".format(h.upper()),
            "fcn_{}".format(h),
            "sub_{}".format(h),
            "func_{}".format(h),
        ])
    try:
        bare = "{:x}".format(parse_addr_int(addr))
        names.append("fun_{}".format(bare))
    except Exception:
        pass
    out, seen = [], set()
    for n in names:
        if n not in seen:
            seen.add(n)
            out.append(n)
    return out


def _pe_name_variants(name):
    # type: (str) -> List[str]
    if not name:
        return []
    out = [name]
    if name.startswith("_") and len(name) > 1:
        out.append(name[1:])
    else:
        out.append("_" + name)
    if "@" in name:
        bare = name.split("@", 1)[0]
        out.append(bare)
        if bare.startswith("_") and len(bare) > 1:
            out.append(bare[1:])
    dedup, seen = [], set()
    for n in out:
        if n and n not in seen:
            seen.add(n)
            dedup.append(n)
    return dedup


def _is_trivial_stub(body):
    # type: (str) -> bool
    """True for empty/return-0 stubs Snowman emits for section labels."""
    if not body:
        return True
    # Drop comments for a crude size check
    compact = re.sub(r"/\*.*?\*/", "", body, flags=re.S)
    compact = re.sub(r"//.*?$", "", compact, flags=re.M)
    compact = re.sub(r"\s+", " ", compact).strip()
    if len(compact) < 40:
        return True
    if re.search(r"\{\s*return\s+0\s*;\s*\}", compact):
        return True
    if re.search(r"\{\s*return\s*;\s*\}", compact):
        return True
    # asm-only / bare return stubs (e.g. fpreset renamed to text)
    if re.search(r"\{\s*(?:__asm__\s*\([^;]*\)\s*;\s*)*return\s*;\s*\}", compact):
        return True
    if re.search(
        r"\{\s*(?:__asm__\s*\([^;]*\)\s*;\s*)+return\s+0\s*;\s*\}", compact
    ):
        return True
    return False


_FUNC_DEF_NAME_RE = re.compile(
    r"(?m)^\s*(?:[\w_][\w\s_*\(\),]*\s+)?([A-Za-z_][\w.]*)\s*\([^;{}]*\)\s*\{"
)


def _iter_named_function_defs(code, name):
    # type: (str, str) -> List[Tuple[int, str]]
    """All definition sites of a given identifier → (start, body)."""
    results = []  # type: List[Tuple[int, str]]
    pat = re.compile(
        r"(?ms)(?:^|\n)[^\n;{}]*\b" + re.escape(name) + r"\s*\([^;{}]*\)\s*\{"
    )
    for match in pat.finditer(code):
        body = extract_braced_unit(code, match.start())
        if body:
            results.append((match.start(), body))
    return results


def _adjacent_function_name(code, pos, direction):
    # type: (str, int, str) -> Tuple[str, int]
    """Name and start of the function definition immediately before/after pos."""
    if direction == "after":
        m = _FUNC_DEF_NAME_RE.search(code, pos)
        if not m or m.group(1) in {"if", "for", "while", "switch", "do", "return"}:
            return "", -1
        return m.group(1), m.start()
    # before: scan all defs with start < pos, take last
    best_name, best_start = "", -1
    for m in _FUNC_DEF_NAME_RE.finditer(code[:pos]):
        nm = m.group(1)
        if nm in {"if", "for", "while", "switch", "do", "return"}:
            continue
        best_name, best_start = nm, m.start()
    return best_name, best_start


def extract_text_standin(code, addr, binary_bytes):
    # type: (str, str, bytes) -> Tuple[str, str]
    """Snowman sometimes renames a PE symbol to `text` (section name collision).

    MinGW unstripped m32: `_count_bits` at .text start becomes `text`, while
    neighbors keep `_clamp` / `_signum`. Prefer the non-trivial `text` body that
    sits *immediately* next to a known PE neighbor (not merely nearby in a window).
    """
    try:
        target = parse_addr_int(addr)
        pe_syms = disasm_helper.list_pe_function_symbols(binary_bytes)
    except Exception:
        return "", ""
    if not pe_syms:
        return "", ""

    # Only apply when we expected a PE symbol here but it is not present as a def.
    pe_here = [n for va, n in pe_syms if va == target]
    if not pe_here:
        return "", ""
    for n in pe_here:
        for cand in _pe_name_variants(n):
            matched, body = extract_function_by_name_patterns(code, [cand])
            if body and not _is_trivial_stub(body):
                return matched, body

    text_defs = [
        (start, body)
        for start, body in _iter_named_function_defs(code, "text")
        if not _is_trivial_stub(body)
    ]
    if not text_defs:
        return "", ""

    def _uniq(seq):
        out, seen = [], set()
        for x in seq:
            if x not in seen:
                seen.add(x)
                out.append(x)
        return out

    # Immediate PE address neighbors (not the whole rest of the binary)
    next_by_va = _uniq([n for va, n in pe_syms if va > target])[:6]
    prev_by_va = _uniq([n for va, n in pe_syms if va < target][::-1])[:6][::-1]
    next_names = _uniq([v for n in next_by_va for v in _pe_name_variants(n)])
    prev_names = _uniq([v for n in prev_by_va for v in _pe_name_variants(n)])
    next_set = set(next_names)
    prev_set = set(prev_names)

    # (score, -gap, -start, body) — higher score wins; closer neighbor gap wins ties
    scored = []  # type: List[Tuple[int, int, int, str]]
    for start, body in text_defs:
        end = start + len(body)
        score = 0
        gap = 10**9
        adj_after, adj_after_pos = _adjacent_function_name(code, end, "after")
        adj_before, adj_before_pos = _adjacent_function_name(code, start, "before")
        if adj_after and adj_after in next_set:
            score += 5
            gap = min(gap, max(0, adj_after_pos - end))
        if adj_before and adj_before in prev_set:
            score += 4
            gap = min(gap, max(0, start - (adj_before_pos if adj_before_pos >= 0 else 0)))
        # Mild preference for mid-sized real functions over huge CRT blobs
        if 40 <= len(body) <= 2500:
            score += 1
        # Prefer bodies with control flow (real decompiled logic)
        if re.search(r"\b(while|for|if)\b", body):
            score += 1
        scored.append((score, -gap, -start, body))

    scored.sort(reverse=True)
    if scored and scored[0][0] >= 5:
        # Require a true PE-neighbor adjacency hit, not just size/control-flow bonus
        return "text", scored[0][3]
    # Single non-trivial text def is still better than whole-program failure
    if len(text_defs) == 1:
        return "text", text_defs[0][1]
    return "", ""


def extract_snowman_function(code, addr, binary_bytes=None):
    # type: (str, str, Optional[bytes]) -> Tuple[str, str]
    """Extract one Snowman function by address / PE symbol / text-standin."""
    name, body = extract_function_by_name_patterns(
        code, snowman_name_candidates(addr, binary_bytes)
    )
    if body and not _is_trivial_stub(body):
        return name, body
    # Accept trivial only if it was an exact fun_* address match (strip case rarely stub)
    if body and name.startswith(("fun_", "fcn_", "sub_", "func_")):
        return name, body

    forms = {_strip0x(f).lower() for f in address_hex_forms(addr)}
    stripped_forms = {f.lstrip("0") or "0" for f in forms}
    for match in re.finditer(
        r"(?ms)(?:^|\n)[^\n;{}]*\b((?:fun|fcn|sub|func)_([0-9A-Fa-f]+))\s*\([^;{}]*\)\s*\{",
        code,
    ):
        full, hex_part = match.group(1), match.group(2).lower()
        if hex_part in forms or hex_part.lstrip("0") in stripped_forms:
            body = extract_braced_unit(code, match.start())
            if body:
                return full, body

    if binary_bytes:
        name, body = extract_text_standin(code, addr, binary_bytes)
        if body:
            return name, body

    return "fun_{:x}".format(parse_addr_int(addr)), ""


def normalize_snowman_unit(code, addr, binary_bytes=None):
    # type: (str, str, Optional[bytes]) -> Tuple[str, str, Optional[str]]
    """Return (name, code, error). Always try single-function extraction."""
    if not code or not code.strip():
        return "fun_{}".format(addr), "", "empty snowman output"

    name, body = extract_snowman_function(code, addr, binary_bytes)
    if body:
        stable = "fun_{:x}".format(parse_addr_int(addr))
        body = rewrite_function_name(body, name, stable)
        body = inject_address_anchor(body, addr, "snowman")
        return stable, body, None

    if not is_whole_program_output(code) and count_function_defs(code) <= 1:
        stable = "fun_{:x}".format(parse_addr_int(addr))
        m = re.search(
            r"(?m)^\s*(?:[\w_][\w\s_*\(\),]*\s+)?([A-Za-z_][\w]*)\s*\([^;{}]*\)\s*\{",
            code,
        )
        if m and m.group(1) not in {"if", "for", "while", "switch"}:
            code = rewrite_function_name(code, m.group(1), stable)
        code = inject_address_anchor(code, addr, "snowman")
        return stable, code, None

    return (
        "fun_{:x}".format(parse_addr_int(addr)),
        "",
        "Snowman returned whole-program output and target function extraction failed",
    )


# Back-compat for older unit tests
def function_definition_count(code):
    # type: (str) -> int
    return count_function_defs(code)


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
    try:
        binary_bytes = base64.b64decode(req.binary_b64, validate=True)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid base64 payload")
    with tempfile.NamedTemporaryFile(suffix=".bin", delete=False) as f:
        f.write(binary_bytes)
        tmp_path = f.name

    start = time.monotonic()
    results = []
    try:
        for addr in req.addresses:
            try:
                validate_address(addr)
                # Prefer --from with original form, then RVA forms for PE tools.
                from_candidates = [addr]
                try:
                    v = parse_addr_int(addr)
                    for base in (0x140000000, 0x400000):
                        if v >= base:
                            from_candidates.append(f"0x{v - base:x}")
                except Exception:
                    pass
                raw = ""
                last_err = ""
                for from_addr in from_candidates:
                    result = subprocess.run(
                        [SNOWMAN_BIN, f"--from={from_addr}", "--print-cxx=-", tmp_path],
                        capture_output=True,
                        text=True,
                        timeout=120,
                    )
                    if result.returncode == 0 and (result.stdout or "").strip():
                        raw = result.stdout.strip()
                        break
                    last_err = result.stderr or result.stdout or "snowman failed"
                if not raw:
                    results.append(
                        DecompileResultItem(
                            addr=addr, name=f"func_{addr}", error=last_err or "empty"
                        )
                    )
                    continue
                name, code, err = normalize_snowman_unit(raw, addr, binary_bytes)
                if err:
                    results.append(
                        DecompileResultItem(addr=addr, name=name, error=err)
                    )
                else:
                    results.append(
                        DecompileResultItem(addr=addr, name=name, code=code)
                    )
            except Exception as e:
                results.append(DecompileResultItem(addr=addr, error=str(e)))
        elapsed = int((time.monotonic() - start) * 1000)
        return BatchDecompileResponse(results=results, time_ms=elapsed)
    finally:
        os.unlink(tmp_path)
