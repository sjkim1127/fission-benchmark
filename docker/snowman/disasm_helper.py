"""Shared Capstone PE/ELF disassembly helper for basic decompiler containers."""
import sys
from pathlib import Path
from capstone import *
import pefile
from elftools.elf.elffile import ELFFile

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
