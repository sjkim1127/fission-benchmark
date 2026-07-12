"""PE/ELF symbol inventories as optional function-discovery ground truth.

When binaries are unstripped, COFF/ELF symbols provide a third reference
independent of Ghidra — useful for strip-delta and adapter honesty checks.
"""
from __future__ import annotations

import struct
from pathlib import Path
from typing import Any, List, Tuple, Union


def _decode_coff_name(name_bytes: bytes, data: bytes, strtab_off: int) -> str:
    if name_bytes[0:4] == b"\x00\x00\x00\x00":
        str_off = struct.unpack_from("<I", name_bytes, 4)[0]
        end = data.find(b"\x00", strtab_off + str_off)
        if end < 0:
            end = strtab_off + str_off + 64
        return data[strtab_off + str_off : end].decode("utf-8", "replace")
    return name_bytes.split(b"\x00")[0].decode("utf-8", "replace")


def list_pe_function_symbols(binary: Union[str, Path, bytes]) -> List[Tuple[int, str]]:
    """Sorted (VA, name) for PE COFF + export symbols."""
    if isinstance(binary, (bytes, bytearray)):
        data = bytes(binary)
    else:
        data = Path(binary).read_bytes()
    if data[:2] != b"MZ":
        return []
    try:
        import pefile
    except ImportError:
        return []
    try:
        pe = pefile.PE(data=data, fast_load=True)
        pe.parse_data_directories(
            directories=[pefile.DIRECTORY_ENTRY["IMAGE_DIRECTORY_ENTRY_EXPORT"]]
        )
    except Exception:
        return []

    image_base = pe.OPTIONAL_HEADER.ImageBase
    out: List[Tuple[int, str]] = []
    seen: set[tuple[int, str]] = set()

    if hasattr(pe, "DIRECTORY_ENTRY_EXPORT"):
        for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
            if exp.address is None:
                continue
            name = (
                exp.name.decode("utf-8", "replace")
                if exp.name
                else f"func_{exp.address:x}"
            )
            va = image_base + exp.address
            key = (va, name)
            if key not in seen:
                seen.add(key)
                out.append((va, name))

    ptr = pe.FILE_HEADER.PointerToSymbolTable
    n = pe.FILE_HEADER.NumberOfSymbols
    if ptr and n and ptr + n * 18 <= len(data):
        strtab_off = ptr + n * 18
        i = 0
        while i < n:
            off = ptr + i * 18
            entry = data[off : off + 18]
            if len(entry) < 18:
                break
            name_bytes = entry[0:8]
            value = struct.unpack_from("<I", entry, 8)[0]
            section = struct.unpack_from("<h", entry, 12)[0]
            storage = entry[16]
            naux = entry[17]
            name = _decode_coff_name(name_bytes, data, strtab_off)
            if storage in (2, 3) and section > 0 and section <= len(pe.sections):
                if name and not name.startswith("."):
                    sec = pe.sections[section - 1]
                    va = image_base + sec.VirtualAddress + value
                    key = (va, name)
                    if key not in seen:
                        seen.add(key)
                        out.append((va, name))
            i += 1 + naux

    out.sort(key=lambda item: (item[0], item[1]))
    return out


def pe_symbol_inventory(binary_path: str | Path) -> list[dict[str, Any]]:
    """Adapter-shaped inventory list for compare_functions."""
    return [
        {
            "address": f"0x{va:x}",
            "name": name,
            "size": 0,
            "kind": "function",
            "source": "pe_coff",
        }
        for va, name in list_pe_function_symbols(binary_path)
    ]


def inventory_from_addresses(
    addresses: list[str],
    *,
    name_prefix: str = "manifest_",
) -> list[dict[str, Any]]:
    """Build a minimal inventory from corpus manifest entry VAs."""
    out: list[dict[str, Any]] = []
    seen: set[str] = set()
    for addr in addresses:
        key = str(addr or "").strip().lower()
        if not key or key in seen:
            continue
        seen.add(key)
        out.append(
            {
                "address": addr if str(addr).lower().startswith("0x") else f"0x{addr}",
                "name": f"{name_prefix}{key}",
                "size": 0,
                "kind": "function",
                "source": "manifest",
            }
        )
    return out
