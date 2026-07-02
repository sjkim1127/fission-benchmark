from __future__ import annotations

import importlib.util
import sys
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


def test_revng_extracts_address_named_function() -> None:
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
