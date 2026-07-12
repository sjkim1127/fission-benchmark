"""Unit tests for adapter boundary helpers (host copy)."""
from pathlib import Path
import importlib.util
import sys

import pytest

ROOT = Path(__file__).resolve().parent.parent
BOUNDARY_PATH = ROOT / "docker" / "common" / "boundary.py"


@pytest.fixture(scope="module")
def boundary():
    spec = importlib.util.spec_from_file_location("boundary_helpers", BOUNDARY_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules["boundary_helpers"] = mod
    spec.loader.exec_module(mod)
    return mod


def test_address_hex_forms_include_rva(boundary) -> None:
    forms = {f.lower() for f in boundary.address_hex_forms("0x140001530")}
    assert "140001530" in forms or "0x140001530" in forms
    # PE32+ common image base → RVA 0x1530
    assert any(f.removeprefix("0x") in {"1530", "00001530"} for f in forms)


def test_extract_function_by_name_patterns(boundary) -> None:
    code = """
int fun_other(void) { return 1; }
int fun_140001530(unsigned x) {
    return x;
}
"""
    name, body = boundary.extract_function_by_name_patterns(
        code, ["fun_140001530", "fun_401530"]
    )
    assert name == "fun_140001530"
    assert "return x" in body
    assert "fun_other" not in body


def test_inject_address_anchor(boundary) -> None:
    code = "int foo(void) { return 0; }"
    out = boundary.inject_address_anchor(code, "0x401000", "test")
    assert "/* address: 0x401000" in out
    assert "foo" in out


def test_pe_symbol_names_for_m32_count_bits() -> None:
    """COFF symbols on unstripped MinGW PE must resolve function VAs."""
    import importlib.util

    helper_path = ROOT / "docker" / "snowman" / "disasm_helper.py"
    # disasm_helper imports capstone/pefile — skip if unavailable in env
    try:
        import pefile  # noqa: F401
    except ImportError:
        pytest.skip("pefile not installed")

    # Load only the pure helpers by exec'ing symbol functions via import if deps present
    try:
        import capstone  # noqa: F401
        from elftools.elf.elffile import ELFFile  # noqa: F401
    except ImportError:
        pytest.skip("capstone/pyelftools not installed")

    spec = importlib.util.spec_from_file_location("snowman_disasm_helper", helper_path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)

    binary = ROOT / "corpus" / "holdout" / "binaries" / "control_flow_gcc-m32_O0.exe"
    if not binary.exists():
        pytest.skip("holdout m32 binary missing")

    names = mod.symbol_names_for_address(binary.read_bytes(), "0x4015b0")
    assert "_count_bits" in names or "count_bits" in names
    syms = mod.list_pe_function_symbols(binary.read_bytes())
    assert any(va == 0x4015B0 and "count_bits" in name for va, name in syms)
