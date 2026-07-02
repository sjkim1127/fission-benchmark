from __future__ import annotations

import importlib.util
import sys
import types
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(path.parent))
    try:
        spec.loader.exec_module(module)
    finally:
        sys.path.remove(str(path.parent))
    return module


def test_fission_uses_addresses_file_batch_cli() -> None:
    server = load_module("fission_server", ROOT / "docker/fission/server.py")

    command = server.decompile_batch_command("/tmp/target.bin", "/tmp/addrs.txt")

    assert command[:3] == ["/usr/local/bin/fission_cli", "decomp", "/tmp/target.bin"]
    assert "--addresses-file" in command
    assert "/tmp/addrs.txt" in command
    assert "--batch" not in command
    assert "--json" in command


def test_fission_normalizes_new_batch_json_shape() -> None:
    server = load_module("fission_server_shape", ROOT / "docker/fission/server.py")

    payload = {
        "_meta": {"function_count": 1},
        "functions": [{"address": "0x4015b0", "name": "_fibonacci", "code": "int x;"}],
    }

    assert server.normalize_decompile_results(payload) == [
        {"address": "0x4015b0", "name": "_fibonacci", "code": "int x;"}
    ]


def test_ghidra_extracts_marker_from_info_prefixed_line() -> None:
    server = load_module("ghidra_server", ROOT / "docker/ghidra/server.py")

    text = (
        "INFO  DecompileFunction.java> ===BATCH_RESULT==="
        '[{"addr":"0x401000","name":"fn","code":"int fn(void) { return 1; }"}] '
        "(GhidraScript)"
    )

    assert server._extract_marked_json_line(text, server.BATCH_MARKER) == [
        {"addr": "0x401000", "name": "fn", "code": "int fn(void) { return 1; }"}
    ]


def test_revng_extracts_address_named_function(monkeypatch) -> None:
    monkeypatch.setitem(sys.modules, "disasm_helper", types.ModuleType("disasm_helper"))
    server = load_module("revng_server", ROOT / "docker/revng/server.py")
    code = """
#include "types-and-globals.h"

_ABI(Microsoft_x86_cdecl)
generic32_t function_0x4015b0_Code_x86(void) {
  if (segment_1.offset_4) {
    return 1;
  }
  return 0;
}

_ABI(Microsoft_x86_cdecl)
generic32_t function_0x4015e7_Code_x86(void) {
  return 2;
}
"""

    extracted = server.extract_revng_function(code, "0x4015b0")

    assert "function_0x4015b0_Code_x86" in extracted
    assert "return 1;" in extracted
    assert "function_0x4015e7_Code_x86" not in extracted


def test_revng_extracts_containing_function_for_interior_address(monkeypatch) -> None:
    monkeypatch.setitem(sys.modules, "disasm_helper", types.ModuleType("disasm_helper"))
    server = load_module("revng_server_interior", ROOT / "docker/revng/server.py")
    code = """
_ABI(raw_x86_64)
void function_0x140001520_Code_x86_64(void) {
  int local = 1;
  return;
}

_ABI(raw_x86_64)
void function_0x14000155f_Code_x86_64(void) {
  return;
}
"""

    extracted = server.extract_revng_function(code, "0x140001530")

    assert "function_0x140001520_Code_x86_64" in extracted
    assert "local = 1" in extracted
    assert "function_0x14000155f_Code_x86_64" not in extracted


def test_boomerang_extracts_function_by_rva_address(monkeypatch) -> None:
    monkeypatch.setitem(sys.modules, "disasm_helper", types.ModuleType("disasm_helper"))
    server = load_module("boomerang_server", ROOT / "docker/boomerang/server.py")
    code = """
/* File: target.c */
/** address: 0x00001181 */
void proc_0x00001181(int pc) { return; }

/** address: 0x0000155f */
int proc_0x0000155f(int value, int lo, int hi) { return value; }
"""

    name, extracted = server.extract_function_by_address(code, "0x14000155f")

    assert name == "proc_0x0000155f"
    assert "return value" in extracted
    assert "proc_0x00001181" not in extracted


def test_boomerang_extracts_function_by_32bit_pe_rva_address(monkeypatch) -> None:
    monkeypatch.setitem(sys.modules, "disasm_helper", types.ModuleType("disasm_helper"))
    server = load_module("boomerang_server_32", ROOT / "docker/boomerang/server.py")
    code = """
/** address: 0x000015d6 */
int proc_0x000015d6(int value, int lo, int hi) { return value; }
"""

    name, extracted = server.extract_function_by_address(code, "0x4015d6")

    assert name == "proc_0x000015d6"
    assert "return value" in extracted


def test_boomerang_cli_entry_address_uses_pe_rva(monkeypatch, tmp_path) -> None:
    monkeypatch.setitem(sys.modules, "disasm_helper", types.ModuleType("disasm_helper"))
    server = load_module("boomerang_server_entry", ROOT / "docker/boomerang/server.py")

    class OptionalHeader:
        ImageBase = 0x140000000
        Magic = 0x20B

    class PE:
        OPTIONAL_HEADER = OptionalHeader()

    pefile = types.ModuleType("pefile")
    pefile.PE = lambda *_args, **_kwargs: PE()
    monkeypatch.setitem(sys.modules, "pefile", pefile)

    assert server.boomerang_entry_address(tmp_path / "target.exe", "0x14000155f") == "0x155f"


def test_boomerang_cli_entry_address_keeps_pe32_va(monkeypatch, tmp_path) -> None:
    monkeypatch.setitem(sys.modules, "disasm_helper", types.ModuleType("disasm_helper"))
    server = load_module("boomerang_server_entry32", ROOT / "docker/boomerang/server.py")

    class OptionalHeader:
        ImageBase = 0x400000
        Magic = 0x10B

    class PE:
        OPTIONAL_HEADER = OptionalHeader()

    pefile = types.ModuleType("pefile")
    pefile.PE = lambda *_args, **_kwargs: PE()
    monkeypatch.setitem(sys.modules, "pefile", pefile)

    assert server.boomerang_entry_address(tmp_path / "target.exe", "0x4015d6") == "0x4015d6"


def test_boomerang_reports_missing_requested_address(monkeypatch) -> None:
    monkeypatch.setitem(sys.modules, "disasm_helper", types.ModuleType("disasm_helper"))
    server = load_module("boomerang_server_missing", ROOT / "docker/boomerang/server.py")
    code = """
/** address: 0x00001181 */
void proc_0x00001181(int pc) { return; }
"""

    name, error = server.extract_function_by_address(code, "0x14000155f")

    assert name == ""
    assert "not found" in error


def test_snowman_detects_whole_program_output(monkeypatch) -> None:
    monkeypatch.setitem(sys.modules, "disasm_helper", types.ModuleType("disasm_helper"))
    server = load_module("snowman_server", ROOT / "docker/snowman/server.py")
    code = "\n".join(f"int fun_{i}(void) {{ return {i}; }}" for i in range(5))

    assert server.function_definition_count(code) == 5
    assert server.is_whole_program_output(code) is True


def test_snowman_allows_single_function_output(monkeypatch) -> None:
    monkeypatch.setitem(sys.modules, "disasm_helper", types.ModuleType("disasm_helper"))
    server = load_module("snowman_server_single", ROOT / "docker/snowman/server.py")
    code = "int fun_14000155f(int value, int lo, int hi) { return value; }"

    assert server.function_definition_count(code) == 1
    assert server.is_whole_program_output(code) is False
