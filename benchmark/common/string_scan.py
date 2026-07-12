"""ASCII string extraction + address xref helpers for string recovery."""
from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable


_PRINTABLE = re.compile(rb"[\x20-\x7e]{4,}")


def extract_ascii_strings(data: bytes, *, min_len: int = 4) -> list[tuple[int, str]]:
    """Return (file_offset, text) for ASCII runs."""
    out: list[tuple[int, str]] = []
    for m in re.finditer(rb"[\x20-\x7e]{" + str(min_len).encode() + rb",}", data):
        try:
            text = m.group().decode("ascii")
        except Exception:
            continue
        out.append((m.start(), text))
    return out


def pe_image_base(data: bytes) -> int:
    if len(data) < 0x40 or data[:2] != b"MZ":
        return 0
    e_lfanew = int.from_bytes(data[0x3C:0x40], "little")
    if data[e_lfanew : e_lfanew + 4] != b"PE\0\0":
        return 0
    opt = e_lfanew + 24
    magic = int.from_bytes(data[opt : opt + 2], "little")
    if magic == 0x20B:
        return int.from_bytes(data[opt + 24 : opt + 32], "little")
    if magic == 0x10B:
        return int.from_bytes(data[opt + 28 : opt + 32], "little")
    return 0


def pe_sections(data: bytes) -> list[tuple[int, int, int]]:
    """(rva, size, raw_offset)"""
    e_lfanew = int.from_bytes(data[0x3C:0x40], "little")
    coff = e_lfanew + 4
    num = int.from_bytes(data[coff + 2 : coff + 4], "little")
    size_opt = int.from_bytes(data[coff + 16 : coff + 18], "little")
    sec = coff + 20 + size_opt
    out = []
    for i in range(num):
        s = sec + i * 40
        vsize = int.from_bytes(data[s + 8 : s + 12], "little")
        rva = int.from_bytes(data[s + 12 : s + 16], "little")
        raw_size = int.from_bytes(data[s + 16 : s + 20], "little")
        raw = int.from_bytes(data[s + 20 : s + 24], "little")
        out.append((rva, max(vsize, raw_size), raw))
    return out


def file_off_to_va(data: bytes, off: int) -> int | None:
    base = pe_image_base(data)
    for rva, sz, raw in pe_sections(data):
        if raw <= off < raw + sz:
            return base + rva + (off - raw)
    return None


def strings_in_pe(path: str | Path) -> list[dict]:
    data = Path(path).read_bytes()
    out = []
    for off, text in extract_ascii_strings(data):
        va = file_off_to_va(data, off)
        if va is None:
            continue
        out.append({"address": f"0x{va:x}", "text": text, "file_offset": off})
    return out


def strings_referenced_by_disasm(
    pe_strings: Iterable[dict],
    disasm: list[dict],
) -> list[str]:
    """Match hex immediates / operands against known string VAs."""
    va_to_text = {}
    for s in pe_strings:
        try:
            va_to_text[int(str(s["address"]), 16)] = s["text"]
        except Exception:
            continue
    found: set[str] = set()
    for inst in disasm:
        if not isinstance(inst, dict):
            continue
        ops = str(inst.get("operands") or "") + " " + str(inst.get("bytes") or "")
        for m in re.finditer(r"0x([0-9a-fA-F]+)", ops):
            try:
                val = int(m.group(0), 16)
            except Exception:
                continue
            if val in va_to_text:
                found.add(va_to_text[val])
            # also try image-relative small matches: last 4 bytes as RVA-ish — skip
    # Also pull C string literals embedded in decompiled-looking operand text
    for inst in disasm:
        if not isinstance(inst, dict):
            continue
        ops = str(inst.get("operands") or "")
        for m in re.finditer(r'"([^"\\]{2,80})"', ops):
            found.add(m.group(1))
    return sorted(found)


def strings_from_decomp_code(code: str) -> list[str]:
    return sorted({m.group(1) for m in re.finditer(r'"([^"\\]{2,120})"', code or "")})
