"""Shared function-boundary helpers for decompiler adapters.

Copied into adapter images (some still on Python 3.7 — keep syntax compatible).
"""
from __future__ import annotations

import re
from typing import Iterable, List, Optional, Set, Tuple, Union


CONTROL_KEYWORDS = frozenset({"if", "for", "while", "switch", "do", "return", "sizeof"})

FUNCTION_DEF_RE = re.compile(
    r"(?m)^\s*(?:[\w_][\w\s_*\(\),]*\s+)?([A-Za-z_][\w.]*)\s*\([^;{}]*\)\s*\{"
)


def parse_addr_int(addr):
    # type: (str) -> int
    text = (addr or "").strip()
    if text.lower().startswith("0x"):
        return int(text, 16)
    try:
        return int(text, 10)
    except ValueError:
        return int(text, 16)


def address_hex_forms(addr):
    # type: (Union[str, int]) -> List[str]
    """Likely spellings of a function entry in tool output (VA / RVA / padding)."""
    value = parse_addr_int(str(addr)) if not isinstance(addr, int) else addr
    forms = [
        "{:x}".format(value),
        "{:X}".format(value),
        "{:08x}".format(value),
        "{:016x}".format(value),
        "0x{:x}".format(value),
        "0x{:08x}".format(value),
    ]  # type: List[str]
    for base in (0x140000000, 0x400000, 0x10000000):
        if value >= base:
            rva = value - base
            if 0 < rva < 0x10000000:
                forms.extend(
                    [
                        "{:x}".format(rva),
                        "{:08x}".format(rva),
                        "0x{:x}".format(rva),
                        "0x{:08x}".format(rva),
                    ]
                )
    forms.extend(["{:x}".format(value & 0xFFFFF), "{:x}".format(value & 0xFFFFFF)])
    stripped = "{:x}".format(value).lstrip("0") or "0"
    forms.append(stripped)
    out = []  # type: List[str]
    seen = set()  # type: Set[str]
    for f in forms:
        key = f.lower()
        if key not in seen:
            seen.add(key)
            out.append(f)
    return out


def extract_braced_unit(code, match_start, brace_pos=None):
    # type: (str, int, Optional[int]) -> str
    if brace_pos is None:
        brace_pos = code.find("{", match_start)
    if brace_pos < 0:
        return ""
    depth = 0
    for idx in range(brace_pos, len(code)):
        ch = code[idx]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return code[match_start : idx + 1].strip()
    return ""


def extract_function_by_name_patterns(code, name_patterns):
    # type: (str, Iterable[str]) -> Tuple[str, str]
    """Return (matched_name, body) for the first matching function definition."""
    for name in name_patterns:
        if not name:
            continue
        # Avoid str.format — pattern contains literal braces.
        pat = re.compile(
            r"(?ms)(?:^|\n)[^\n;{}]*\b"
            + re.escape(name)
            + r"\s*\([^;{}]*\)\s*\{"
        )
        match = pat.search(code)
        if not match:
            continue
        body = extract_braced_unit(code, match.start())
        if body:
            return name, body
    return "", ""


def inject_address_anchor(code, addr, tool_name=""):
    # type: (str, str, str) -> str
    """Ensure diagnostics can see the requested entry address."""
    if not code or not code.strip():
        return code
    aliases = {a.lower() for a in address_hex_forms(addr)}
    lowered = code.lower()
    if any(a in lowered for a in aliases):
        if "/* address:" not in lowered[:200]:
            return "/* address: {} */\n{}".format(addr, code)
        return code
    header = "/* address: {} */".format(addr)
    if tool_name:
        header = "/* address: {} | adapter: {} */".format(addr, tool_name)
    return "{}\n{}".format(header, code)


def rewrite_function_name(code, old_name, new_name):
    # type: (str, str, str) -> str
    if not old_name or old_name == new_name:
        return code
    return re.sub(r"\b" + re.escape(old_name) + r"\b", new_name, code)


def strip_leading_macros(code, prefixes):
    # type: (str, Iterable[str]) -> str
    lines = code.splitlines()
    out = []
    for line in lines:
        if any(line.strip().startswith(p) for p in prefixes):
            continue
        out.append(line)
    return "\n".join(out)


def count_function_defs(code):
    # type: (str) -> int
    return sum(
        1
        for m in FUNCTION_DEF_RE.finditer(code or "")
        if m.group(1) not in CONTROL_KEYWORDS
    )
