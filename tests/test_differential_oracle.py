import subprocess
from pathlib import Path

from runner.differential_oracle import (
    aggregate_oracle_evidence,
    build_differential_translation_unit,
    parse_differential_output,
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

    assert aggregate == {"mode": "differential", "valid": False, "tested_rows": 1}
