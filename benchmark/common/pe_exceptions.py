"""Parse PE exception directories (x64 RUNTIME_FUNCTION / .pdata).

Used by SEH parity so both adapters and offline stages share one truth source
for the PE on disk — independent of decompiler recovery quality.
"""
from __future__ import annotations

import struct
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class RuntimeFunction:
    begin_rva: int
    end_rva: int
    unwind_rva: int

    @property
    def begin_va(self) -> int:
        return self.begin_rva  # caller adds image base if needed

    def covers_rva(self, rva: int) -> bool:
        return self.begin_rva <= rva < self.end_rva


def _u16(data: bytes, off: int) -> int:
    return struct.unpack_from("<H", data, off)[0]


def _u32(data: bytes, off: int) -> int:
    return struct.unpack_from("<I", data, off)[0]


def parse_pe_runtime_functions(pe_path: str | Path) -> dict[str, Any]:
    """Return RUNTIME_FUNCTION table + image base for a PE file."""
    path = Path(pe_path)
    data = path.read_bytes()
    if len(data) < 0x40 or data[:2] != b"MZ":
        return {"status": "error", "error": "not a PE", "functions": [], "image_base": 0}

    e_lfanew = _u32(data, 0x3C)
    if data[e_lfanew : e_lfanew + 4] != b"PE\0\0":
        return {"status": "error", "error": "bad PE signature", "functions": [], "image_base": 0}

    coff = e_lfanew + 4
    machine = _u16(data, coff)
    num_sections = _u16(data, coff + 2)
    size_opt = _u16(data, coff + 16)
    opt = coff + 20
    magic = _u16(data, opt)
    if magic == 0x20B:  # PE32+
        image_base = struct.unpack_from("<Q", data, opt + 24)[0]
        # DataDirectory starts at opt+112 for PE32+
        dd_off = opt + 112
    elif magic == 0x10B:  # PE32
        image_base = _u32(data, opt + 28)
        dd_off = opt + 96
    else:
        return {"status": "error", "error": f"unknown optional magic {magic:#x}", "functions": [], "image_base": 0}

    # Exception directory is index 3
    if dd_off + 8 * 4 + 8 > len(data):
        return {"status": "error", "error": "truncated data dirs", "functions": [], "image_base": image_base}
    exc_rva = _u32(data, dd_off + 3 * 8)
    exc_size = _u32(data, dd_off + 3 * 8 + 4)

    # Map RVA -> file offset via sections
    sec_table = opt + size_opt
    sections: list[tuple[int, int, int]] = []  # rva, vsize, raw
    for i in range(num_sections):
        s = sec_table + i * 40
        if s + 40 > len(data):
            break
        vsize = _u32(data, s + 8)
        rva = _u32(data, s + 12)
        raw_size = _u32(data, s + 16)
        raw = _u32(data, s + 20)
        sections.append((rva, max(vsize, raw_size), raw))

    def rva_to_off(rva: int) -> int | None:
        for srva, sz, raw in sections:
            if srva <= rva < srva + sz:
                return raw + (rva - srva)
        return None

    functions: list[dict[str, Any]] = []
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

    return {
        "status": "ok",
        "machine": machine,
        "image_base": image_base,
        "exception_rva": exc_rva,
        "exception_size": exc_size,
        "function_count": len(functions),
        "functions": functions,
        "source": "pe_pdata",
    }


def function_unwind_info(pe_path: str | Path, func_addr: str) -> dict[str, Any]:
    """Lookup RUNTIME_FUNCTION covering a VA (0x14000… or RVA)."""
    table = parse_pe_runtime_functions(pe_path)
    if table.get("status") != "ok":
        return {**table, "has_unwind": False, "covering": None}
    base = int(table["image_base"])
    text = str(func_addr).strip().lower()
    if text.startswith("0x"):
        va = int(text, 16)
    else:
        va = int(text, 16)
    # Heuristic: if address looks like absolute VA, convert to RVA
    rva = va - base if va >= base else va
    covering = None
    for fn in table["functions"]:
        if fn["begin_rva"] <= rva < fn["end_rva"]:
            covering = fn
            break
    return {
        "status": "ok",
        "address": f"0x{va:x}",
        "rva": rva,
        "has_unwind": covering is not None,
        "covering": covering,
        "program_runtime_function_count": table["function_count"],
        "image_base": base,
        "source": "pe_pdata",
        "seh_surface": "runtime_function",
    }
