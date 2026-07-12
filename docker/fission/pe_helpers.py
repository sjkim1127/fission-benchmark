"""PE helpers bundled into the Fission adapter image (no host package dependency)."""
from __future__ import annotations

import re
import struct
from pathlib import Path
from typing import Any


def _u16(data: bytes, off: int) -> int:
    return struct.unpack_from("<H", data, off)[0]


def _u32(data: bytes, off: int) -> int:
    return struct.unpack_from("<I", data, off)[0]


def pe_image_base(data: bytes) -> int:
    if len(data) < 0x40 or data[:2] != b"MZ":
        return 0
    e_lfanew = _u32(data, 0x3C)
    if data[e_lfanew : e_lfanew + 4] != b"PE\0\0":
        return 0
    opt = e_lfanew + 24
    magic = _u16(data, opt)
    if magic == 0x20B:
        return struct.unpack_from("<Q", data, opt + 24)[0]
    if magic == 0x10B:
        return _u32(data, opt + 28)
    return 0


def pe_sections(data: bytes) -> list[tuple[int, int, int]]:
    e_lfanew = _u32(data, 0x3C)
    coff = e_lfanew + 4
    num = _u16(data, coff + 2)
    size_opt = _u16(data, coff + 16)
    sec = coff + 20 + size_opt
    out = []
    for i in range(num):
        s = sec + i * 40
        vsize = _u32(data, s + 8)
        rva = _u32(data, s + 12)
        raw_size = _u32(data, s + 16)
        raw = _u32(data, s + 20)
        out.append((rva, max(vsize, raw_size), raw))
    return out


def file_off_to_va(data: bytes, off: int) -> int | None:
    base = pe_image_base(data)
    for rva, sz, raw in pe_sections(data):
        if raw <= off < raw + sz:
            return base + rva + (off - raw)
    return None


def extract_ascii_strings(data: bytes, min_len: int = 4) -> list[tuple[int, str]]:
    out = []
    for m in re.finditer(rb"[\x20-\x7e]{" + str(min_len).encode() + rb",}", data):
        try:
            out.append((m.start(), m.group().decode("ascii")))
        except Exception:
            continue
    return out


def strings_in_pe(path: str) -> list[dict]:
    data = Path(path).read_bytes()
    out = []
    for off, text in extract_ascii_strings(data):
        va = file_off_to_va(data, off)
        if va is None:
            continue
        out.append({"address": f"0x{va:x}", "text": text, "file_offset": off})
    return out


def strings_referenced_by_disasm(pe_strings: list[dict], disasm: list) -> list[str]:
    va_to_text = {}
    for s in pe_strings:
        try:
            va_to_text[int(str(s["address"]), 16)] = s["text"]
        except Exception:
            continue
    found: set[str] = set()
    for inst in disasm or []:
        if not isinstance(inst, dict):
            continue
        ops = str(inst.get("operands") or "")
        for m in re.finditer(r"0x([0-9a-fA-F]+)", ops):
            try:
                val = int(m.group(0), 16)
            except Exception:
                continue
            if val in va_to_text:
                found.add(va_to_text[val])
        for m in re.finditer(r'"([^"\\]{2,80})"', ops):
            found.add(m.group(1))
    return sorted(found)


def strings_from_decomp_code(code: str) -> list[str]:
    return sorted({m.group(1) for m in re.finditer(r'"([^"\\]{2,120})"', code or "")})


def function_unwind_info(pe_path: str, func_addr: str) -> dict[str, Any]:
    data = Path(pe_path).read_bytes()
    if len(data) < 0x40 or data[:2] != b"MZ":
        return {"status": "error", "error": "not a PE", "has_unwind": False, "covering": None}
    e_lfanew = _u32(data, 0x3C)
    if data[e_lfanew : e_lfanew + 4] != b"PE\0\0":
        return {"status": "error", "error": "bad PE", "has_unwind": False, "covering": None}
    coff = e_lfanew + 4
    size_opt = _u16(data, coff + 16)
    opt = coff + 20
    magic = _u16(data, opt)
    if magic == 0x20B:
        image_base = struct.unpack_from("<Q", data, opt + 24)[0]
        dd_off = opt + 112
    elif magic == 0x10B:
        image_base = _u32(data, opt + 28)
        dd_off = opt + 96
    else:
        return {"status": "error", "error": "bad magic", "has_unwind": False, "covering": None}
    exc_rva = _u32(data, dd_off + 3 * 8)
    exc_size = _u32(data, dd_off + 3 * 8 + 4)
    sections = pe_sections(data)

    def rva_to_off(rva: int) -> int | None:
        for srva, sz, raw in sections:
            if srva <= rva < srva + sz:
                return raw + (rva - srva)
        return None

    functions = []
    if exc_rva and exc_size >= 12:
        off = rva_to_off(exc_rva)
        if off is not None:
            end = min(off + exc_size, len(data))
            cur = off
            while cur + 12 <= end:
                begin = _u32(data, cur)
                end_r = _u32(data, cur + 4)
                unwind = _u32(data, cur + 8)
                if begin == 0 and end_r == 0:
                    break
                functions.append(
                    {
                        "begin_rva": begin,
                        "end_rva": end_r,
                        "unwind_info_rva": unwind,
                        "begin_va": f"0x{image_base + begin:x}",
                        "end_va": f"0x{image_base + end_r:x}",
                    }
                )
                cur += 12

    text = str(func_addr).strip().lower()
    va = int(text, 16)
    rva = va - image_base if va >= image_base else va
    covering = None
    for fn in functions:
        if fn["begin_rva"] <= rva < fn["end_rva"]:
            covering = fn
            break
    return {
        "status": "ok",
        "address": f"0x{va:x}",
        "rva": rva,
        "has_unwind": covering is not None,
        "covering": covering,
        "program_runtime_function_count": len(functions),
        "program_eh_symbol_count": len(functions),
        "image_base": image_base,
        "source": "pe_pdata",
        "seh_surface": "runtime_function",
        "is_thunk": False,
        "no_return": False,
        "convention": "unknown",
    }
