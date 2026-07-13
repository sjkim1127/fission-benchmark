"""Shared Capstone PE/ELF disassembly helper for basic decompiler containers."""
from __future__ import annotations

import struct
from pathlib import Path
from typing import Union

from capstone import CS_ARCH_X86, CS_MODE_32, CS_MODE_64, Cs
import pefile
from elftools.elf.elffile import ELFFile


def _decode_coff_name(name_bytes, data, strtab_off):
    # type: (bytes, bytes, int) -> str
    if name_bytes[0:4] == b"\x00\x00\x00\x00":
        str_off = struct.unpack_from("<I", name_bytes, 4)[0]
        end = data.find(b"\x00", strtab_off + str_off)
        if end < 0:
            end = strtab_off + str_off + 64
        return data[strtab_off + str_off : end].decode("utf-8", "replace")
    return name_bytes.split(b"\x00")[0].decode("utf-8", "replace")


def list_pe_function_symbols(binary: Union[str, Path, bytes]):
    # type: (Union[str, Path, bytes]) -> List[Tuple[int, str]]
    """Return sorted (VA, symbol_name) for PE COFF/export function-like symbols."""
    if isinstance(binary, (bytes, bytearray)):
        data = bytes(binary)
    else:
        data = Path(binary).read_bytes()
    if data[:2] != b"MZ":
        return []
    try:
        pe = pefile.PE(data=data, fast_load=True)
        pe.parse_data_directories(
            directories=[
                pefile.DIRECTORY_ENTRY["IMAGE_DIRECTORY_ENTRY_EXPORT"],
            ]
        )
    except Exception:
        return []

    image_base = pe.OPTIONAL_HEADER.ImageBase
    out = []  # type: List[Tuple[int, str]]
    seen = set()  # type: set

    # Export table (always useful; often empty for our MinGW corpus)
    if hasattr(pe, "DIRECTORY_ENTRY_EXPORT"):
        for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
            if exp.address is None:
                continue
            name = (
                exp.name.decode("utf-8", "replace")
                if exp.name
                else "func_{:x}".format(exp.address)
            )
            va = image_base + exp.address
            key = (va, name)
            if key not in seen:
                seen.add(key)
                out.append((va, name))

    # COFF symbol table (MinGW keeps this on unstripped PE)
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
            # typ = struct.unpack_from("<H", entry, 14)[0]
            storage = entry[16]
            naux = entry[17]
            name = _decode_coff_name(name_bytes, data, strtab_off)
            # External (2) or static (3) defined in a real section
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


def symbol_names_for_address(binary, addr):
    # type: (Union[str, Path, bytes], Union[str, int]) -> List[str]
    """Likely C identifier spellings for a PE symbol at addr."""
    if isinstance(addr, str):
        text = addr.strip()
        if text.lower().startswith("0x"):
            target = int(text, 16)
        else:
            try:
                target = int(text, 10)
            except ValueError:
                target = int(text, 16)
    else:
        target = int(addr)

    names = []  # type: List[str]
    for va, name in list_pe_function_symbols(binary):
        if va != target:
            continue
        names.append(name)
        if name.startswith("_") and len(name) > 1:
            names.append(name[1:])
        elif not name.startswith("_"):
            names.append("_" + name)
        # MinGW sometimes has @N stdcall decoration
        if "@" in name:
            bare = name.split("@", 1)[0]
            names.append(bare)
            if bare.startswith("_"):
                names.append(bare[1:])
    # de-dupe preserve order
    out = []  # type: List[str]
    seen = set()
    for n in names:
        if n and n not in seen:
            seen.add(n)
            out.append(n)
    return out


def get_file_offset(binary_path: str, addr: int) -> int:
    data = Path(binary_path).read_bytes()
    if data[:2] == b'MZ':
        pe = pefile.PE(data=data)
        rva = addr - pe.OPTIONAL_HEADER.ImageBase
        return pe.get_offset_from_rva(rva)
    elif data[:4] == b'\x7fELF':
        with open(binary_path, 'rb') as f:
            elffile = ELFFile(f)
            for segment in elffile.iter_segments():
                if segment['p_type'] == 'PT_LOAD':
                    start = segment['p_vaddr']
                    end = start + segment['p_memsz']
                    if start <= addr < end:
                        return segment['p_offset'] + (addr - start)
    return -1

def disassemble(binary_path: str, addr_hex: str, arch: str) -> list:
    addr = int(addr_hex, 16)
    offset = get_file_offset(binary_path, addr)
    if offset == -1:
        return []
    data = Path(binary_path).read_bytes()
    chunk = data[offset : offset + 512]
    
    if "64" in arch or arch == "x86_64":
        md = Cs(CS_ARCH_X86, CS_MODE_64)
    else:
        md = Cs(CS_ARCH_X86, CS_MODE_32)
        
    res = []
    terminal_mnemonics = {"ret", "retn", "hlt", "ud2"}
    for inst in md.disasm(chunk, addr):
        mnemonic = inst.mnemonic.lower()
        res.append({
            "address": f"0x{inst.address:x}",
            "bytes": inst.bytes.hex(),
            "mnemonic": mnemonic,
            "operands": inst.op_str,
            "length": inst.size,
            "fallthrough": f"0x{inst.address + inst.size:x}",
            "branch_target": None
        })
        if mnemonic in terminal_mnemonics:
            break
    return res

def get_functions(binary_path: str) -> list:
    res = []
    data = Path(binary_path).read_bytes()
    if data[:2] == b'MZ':
        # Prefer COFF + export symbols (unstripped MinGW corpus)
        for va, name in list_pe_function_symbols(data):
            res.append({
                "address": "0x{:x}".format(va),
                "name": name,
                "size": 0,
                "kind": "function",
            })
        if res:
            return res
        pe = pefile.PE(data=data)
        if hasattr(pe, 'DIRECTORY_ENTRY_EXPORT'):
            for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
                res.append({
                    "address": f"0x{pe.OPTIONAL_HEADER.ImageBase + exp.address:x}",
                    "name": exp.name.decode("utf-8") if exp.name else f"func_{exp.address:x}",
                    "size": 0,
                    "kind": "function"
                })
    elif data[:4] == b'\x7fELF':
        with open(binary_path, 'rb') as f:
            elffile = ELFFile(f)
            symtab = elffile.get_section_by_name('.symtab')
            if symtab:
                for sym in symtab.iter_symbols():
                    if sym['st_info']['type'] == 'STT_FUNC':
                        res.append({
                            "address": f"0x{sym['st_value']:x}",
                            "name": sym.name,
                            "size": sym['st_size'],
                            "kind": "function"
                        })
    return res
