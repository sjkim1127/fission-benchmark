import subprocess
from pathlib import Path

from runner.differential_oracle import (
    ORACLE_SUBJECT_ORIGINAL_BINARY,
    aggregate_oracle_evidence,
    build_differential_translation_unit,
    build_original_binary_translation_unit,
    extract_function_signature,
    function_addr_to_rva,
    parse_differential_output,
    pe_image_base,
)
from runner.test_wrappers import TEST_WRAPPERS


def test_differential_translation_unit_executes_reference_and_candidate(tmp_path: Path) -> None:
    source = build_differential_translation_unit(
        "clamp",
        "static int clamp(int value, int lo, int hi) { return value < lo ? lo : value > hi ? hi : value; }",
        "static int clamp(int value, int lo, int hi) { return value; }",
        TEST_WRAPPERS["clamp"],
    )
    source_path = tmp_path / "oracle.c"
    binary_path = tmp_path / "oracle"
    source_path.write_text(source, encoding="utf-8")
    subprocess.run(["gcc", str(source_path), "-o", str(binary_path)], check=True)
    execution = subprocess.run([str(binary_path)], check=True, capture_output=True, text=True)

    result = parse_differential_output(execution.stdout, len(TEST_WRAPPERS["clamp"]))
    assert result.category == "assertion_fail"
    assert result.cases_passed == 4
    assert result.cases_total == 6


def test_differential_output_rejects_reference_failure() -> None:
    result = parse_differential_output("CASE 0 1 1\n", 1)
    assert result.category == "fixture_error"


def test_oracle_evidence_is_derived_from_tested_rows() -> None:
    evidence = {
        "mode": "differential",
        "valid": True,
        "oracle_subject": "source_recompile",
        "target_abi": "windows-x86_64",
        "compiler": "x86_64-w64-mingw32-gcc",
        "compiler_version": "gcc 13",
        "runner": "wine",
        "wrapper_sha256": "a" * 64,
        "reference_binary_sha256": "b" * 64,
    }
    aggregate = aggregate_oracle_evidence([{
        "decompiler": "fission",
        "function_name": "clamp",
        "compiler_variant": "gcc -O0",
        "error": None,
        "semantic_score": 1.0,
        "fail_category": "",
        "oracle_evidence": evidence,
    }])

    assert aggregate["valid"] is True
    assert aggregate["tested_rows"] == 1
    assert len(aggregate["row_evidence_sha256"]) == 64


def test_oracle_evidence_rejects_missing_row_proof() -> None:
    aggregate = aggregate_oracle_evidence([{
        "decompiler": "fission",
        "function_name": "clamp",
        "compiler_variant": "gcc -O0",
        "error": None,
        "semantic_score": 1.0,
        "fail_category": "",
        "oracle_evidence": {},
    }])

    # Invalid aggregate still carries full identity keys so official envelopes
    # satisfy schema; validity remains false without row-level proof.
    assert aggregate["mode"] == "differential"
    assert aggregate["valid"] is False
    assert aggregate["tested_rows"] == 1
    assert aggregate["oracle_subject"] == "original_binary"
    assert len(aggregate["wrapper_sha256"]) == 64
    assert len(aggregate["row_evidence_sha256"]) == 64


def test_rename_accepts_synthetic_proc_names() -> None:
    from runner.differential_oracle import _rename_function

    code = "/** address: 0x160b */\nvoid proc_0x0000160b()\n{\n    return;\n}\n"
    out = _rename_function(code, "classify_range", "oracle_candidate_classify_range")
    assert "oracle_candidate_classify_range" in out
    assert "proc_0x0000160b" not in out


def test_extract_function_signature_handles_pointers_and_void() -> None:
    clamp = extract_function_signature(
        "int clamp(int value, int lo, int hi) { return value; }",
        "clamp",
    )
    assert clamp.return_type == "int"
    assert clamp.param_names == "value, lo, hi"
    assert clamp.is_void is False

    rev = extract_function_signature(
        "void reverse_string(char *str, size_t length) { (void)str; (void)length; }",
        "reverse_string",
    )
    assert rev.is_void is True
    assert rev.param_names == "str, length"


def _require_sample_pe() -> Path:
    pe_path = Path("corpus/dev/binaries/control_flow_gcc_O0.exe")
    if not pe_path.is_file():
        pe_path = Path("corpus/holdout/binaries/control_flow_gcc_O0.exe")
    if not pe_path.is_file():
        import pytest

        pytest.skip("corpus PE binaries not built (run scripts/build_corpus.py)")
    return pe_path


def test_function_addr_to_rva_uses_pe_image_base() -> None:
    pe = _require_sample_pe().read_bytes()
    image_base = pe_image_base(pe)
    assert image_base == 0x140000000
    assert function_addr_to_rva(pe, "0x140001530") == 0x1530
    assert function_addr_to_rva(pe, "0x1530") == 0x1530


def test_original_binary_translation_unit_embeds_pe_loader_and_rva() -> None:
    pe = _require_sample_pe().read_bytes()
    source = build_original_binary_translation_unit(
        "clamp",
        "int clamp(int value, int lo, int hi) { return value < lo ? lo : value > hi ? hi : value; }",
        "int clamp(int value, int lo, int hi) { return value; }",
        TEST_WRAPPERS["clamp"],
        function_addr="0x14000155f",
        pe_bytes=pe,
    )
    assert "oracle_pe_load" in source
    assert "oracle_pe_fn" in source
    assert "DWORD rva =" in source
    assert "oracle_candidate_clamp" in source
    assert ORACLE_SUBJECT_ORIGINAL_BINARY  # constant import sanity


def test_original_binary_aggregate_subject_is_exact() -> None:
    evidence = {
        "mode": "differential",
        "valid": True,
        "oracle_subject": ORACLE_SUBJECT_ORIGINAL_BINARY,
        "target_abi": "windows-x86_64",
        "compiler": "x86_64-w64-mingw32-gcc",
        "compiler_version": "gcc 13",
        "runner": "wine",
        "wrapper_sha256": "a" * 64,
        "reference_binary_sha256": "b" * 64,
    }
    aggregate = aggregate_oracle_evidence([{
        "decompiler": "fission",
        "function_name": "clamp",
        "compiler_variant": "gcc -O0",
        "error": None,
        "semantic_score": 1.0,
        "fail_category": "",
        "oracle_evidence": evidence,
    }])
    assert aggregate["valid"] is True
    assert aggregate["oracle_subject"] == ORACLE_SUBJECT_ORIGINAL_BINARY
