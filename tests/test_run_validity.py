"""Unit tests for runner.run_validity — 9 required cases.

Run with: pytest tests/test_run_validity.py -v
"""
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "runner"))
import run_validity as rv


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_row(decompiler="fission", error=None, fail_category=None):
    return {
        "decompiler": decompiler,
        "function_name": "fixture",
        "compiler_variant": "gcc -O0",
        "error": error,
        "fail_category": fail_category,
        "source_similarity": 0.0,
        "semantic_score": None,
        "correctness_score": None,
        "correctness_rank": None,
        "structural_penalty": 0.0,
        "time_ms": 0,
        "cases_passed": 0,
        "cases_total": 0,
    }


def _fission_rows(total, clean):
    rows = []
    for i in range(clean):
        rows.append(_make_row("fission"))
    for i in range(total - clean):
        rows.append(_make_row("fission", error="adapter crash"))
    return rows


def _other_rows(decompiler, total, clean):
    rows = []
    for i in range(clean):
        rows.append(_make_row(decompiler))
    for i in range(total - clean):
        rows.append(_make_row(decompiler, error="error"))
    return rows


# ---------------------------------------------------------------------------
# Test 1: Fission 100%, overall 83.7% -> INVALID
# ---------------------------------------------------------------------------


def test_fission_100_overall_83_invalid():
    """Current published result: Fission 84/84 but retdec 0/84 => 83.7% overall => INVALID."""
    rows = _fission_rows(84, 84)  # Fission 100%
    rows += _other_rows("ghidra", 84, 84)
    rows += _other_rows("angr", 84, 81)
    rows += _other_rows("radare2", 84, 84)
    rows += _other_rows("revng", 84, 75)
    rows += _other_rows("snowman", 84, 84)
    rows += _other_rows("retdec", 84, 0)  # All adapter errors

    verdict = rv.evaluate_run(rows)
    # 492 / 588 = 83.67% -- below 90%
    assert not verdict.valid
    assert "backend_coverage_below_threshold" in verdict.reasons
    assert verdict.overall.ratio < 0.90


# ---------------------------------------------------------------------------
# Test 2: Fission 90%, overall 90% -> VALID
# ---------------------------------------------------------------------------


def test_fission_90_overall_90_valid():
    fission = _fission_rows(10, 9)  # 90%
    others = _other_rows("ghidra", 10, 9)  # 90%
    verdict = rv.evaluate_run(fission + others)
    assert verdict.valid
    assert verdict.reasons == ()


# ---------------------------------------------------------------------------
# Test 3: Fission 89.9% -> INVALID
# ---------------------------------------------------------------------------


def test_fission_89_invalid():
    # 89 clean out of 100 => 89% < 90%
    rows = _fission_rows(100, 89) + _other_rows("ghidra", 100, 100)
    verdict = rv.evaluate_run(rows)
    assert not verdict.valid
    assert "fission_coverage_below_threshold" in verdict.reasons


# ---------------------------------------------------------------------------
# Test 4: Overall 89.9% -> INVALID
# ---------------------------------------------------------------------------


def test_overall_89_invalid():
    # Fission 100%, but a secondary backend is completely dead
    rows = _fission_rows(10, 10)
    rows += _other_rows("snowman", 100, 89)  # 89% overall (and pulls total below)
    # total = 110, clean = 10 + 89 = 99 => 90% exactly — need to make it fail
    # Let's use 10 fission + 90 snowman (9 clean) => 19/100 = 19%
    rows2 = _fission_rows(10, 10) + _other_rows("snowman", 90, 79)
    # total=100, clean = 10+79 = 89 < 90%
    verdict2 = rv.evaluate_run(rows2)
    assert not verdict2.valid
    assert "backend_coverage_below_threshold" in verdict2.reasons


# ---------------------------------------------------------------------------
# Test 5: error="Address missing from batch result" is output failure
# ---------------------------------------------------------------------------


def test_address_missing_is_output_failure():
    row = {
        "decompiler": "fission",
        "error": "Address missing from batch result",
        "fail_category": None,
    }
    assert rv.is_output_failure(row)


# ---------------------------------------------------------------------------
# Test 6: semantic compile_error + error=None is NOT output failure
# ---------------------------------------------------------------------------


def test_compile_error_with_no_error_field_is_not_output_failure():
    """Compile failure means decompiler produced code, just didn't compile."""
    row = {
        "decompiler": "fission",
        "error": None,
        "fail_category": "compile_error",
        "semantic_error": "gcc: error: ...",
    }
    # Must NOT be an output failure (code was produced)
    assert not rv.is_output_failure(row)


# ---------------------------------------------------------------------------
# Test 7: legacy flat-list -> official=false, provenance incomplete
# ---------------------------------------------------------------------------


def test_legacy_flat_list_is_invalid(tmp_path):
    flat = [_make_row("fission") for _ in range(10)]
    path = tmp_path / "legacy.json"
    path.write_text(json.dumps(flat))

    loaded = rv.load_result_file(path)
    assert loaded.legacy is True

    verdict = rv.evaluate_run(loaded)
    assert not verdict.valid
    assert "legacy_flat_list" in verdict.reasons


# ---------------------------------------------------------------------------
# Test 8: workflow verdict == evaluate_run verdict (single source of truth)
# ---------------------------------------------------------------------------


def test_workflow_and_report_share_same_verdict():
    """Simulate both workflow gate and report generating the same verdict."""
    rows = _fission_rows(84, 84)  # Fission perfect
    rows += _other_rows("retdec", 84, 0)  # retdec dead

    # Same function used in both paths
    verdict_workflow = rv.evaluate_run(rows)
    verdict_report = rv.evaluate_run(rows)

    assert verdict_workflow.valid == verdict_report.valid
    assert verdict_workflow.reasons == verdict_report.reasons
    assert verdict_workflow.overall.ratio == verdict_report.overall.ratio


# ---------------------------------------------------------------------------
# Test 9: render_report does NOT modify input file
# ---------------------------------------------------------------------------


def test_render_report_does_not_modify_input(tmp_path):
    """load_result_file must not write to the source path."""
    rows = [_make_row("fission"), _make_row("ghidra")]
    path = tmp_path / "result.json"
    original_content = json.dumps(rows)
    path.write_text(original_content)

    # Just loading must not change the file
    loaded = rv.load_result_file(path)
    assert path.read_text() == original_content, (
        "load_result_file must not modify the input file"
    )

    # build_envelope also must not touch the file
    rv.build_envelope(loaded.rows)
    assert path.read_text() == original_content, (
        "build_envelope must not modify the input file"
    )


def test_canonical_schema_rejects_missing_row_identity(tmp_path):
    envelope = rv.build_envelope([_make_row("fission")], run_meta={"official": False})
    del envelope["rows"][0]["function_name"]
    path = tmp_path / "malformed.json"
    path.write_text(json.dumps(envelope), encoding="utf-8")
    with pytest.raises(ValueError, match="function_name"):
        rv.load_result_file(path)


# ---------------------------------------------------------------------------
# Bonus: envelope round-trip preserves row count and validity field
# ---------------------------------------------------------------------------


def test_envelope_validity_field():
    rows = _fission_rows(10, 10) + _other_rows("ghidra", 10, 10)
    envelope = rv.build_envelope(rows)

    assert envelope["schema_version"] == 2
    assert envelope["validity"]["valid"] is True
    assert envelope["validity"]["fission_coverage"] == 1.0
    assert envelope["validity"]["backend_coverage"] == 1.0
    assert len(envelope["rows"]) == 20


def test_envelope_invalid_marks_correctly():
    rows = _fission_rows(10, 10) + _other_rows("retdec", 10, 0)
    envelope = rv.build_envelope(rows)

    assert envelope["validity"]["valid"] is False
    assert "backend_coverage_below_threshold" in envelope["validity"]["reasons"]


def test_matrix_missing_backend():
    rows = _fission_rows(10, 10)
    envelope = rv.build_envelope(rows, matrix={"expected_decompilers": ["fission", "ghidra"]})
    assert envelope["validity"]["valid"] is False
    assert "backend_missing" in envelope["validity"]["reasons"]


def test_matrix_row_count_mismatch():
    rows = _fission_rows(10, 10)
    envelope = rv.build_envelope(rows, matrix={"expected_rows": 20})
    assert envelope["validity"]["valid"] is False
    assert "matrix_completeness_mismatch" in envelope["validity"]["reasons"]

# ---------------------------------------------------------------------------
# Test 10: Official=false -> INVALID
# ---------------------------------------------------------------------------

def test_official_false_invalid():
    """official=False → valid=True but publishable=False (non_official_run in publish_reasons)."""
    rows = _fission_rows(10, 10)
    envelope = rv.build_envelope(rows, run_meta={"official": False})
    loaded = rv.LoadedResult(rows=envelope["rows"], envelope=envelope, legacy=False)
    verdict = rv.evaluate_run(loaded)
    # Measurement is valid; but not publishable
    assert verdict.valid
    assert not verdict.publishable
    assert "non_official_run" in verdict.publish_reasons
    assert "non_official_run" not in verdict.reasons

# ---------------------------------------------------------------------------
# Test 11: legacy_source=true -> INVALID
# ---------------------------------------------------------------------------

def test_legacy_source_invalid():
    """legacy_source=True → valid=True but publishable=False (legacy_source in publish_reasons)."""
    rows = _fission_rows(10, 10)
    envelope = rv.build_envelope(rows, run_meta={"legacy_source": True})
    loaded = rv.LoadedResult(rows=envelope["rows"], envelope=envelope, legacy=False)
    verdict = rv.evaluate_run(loaded)
    # Measurement quality is fine; provenance is the blocker
    assert verdict.valid
    assert not verdict.publishable
    assert "legacy_source" in verdict.publish_reasons
    assert "legacy_source" not in verdict.reasons

# ---------------------------------------------------------------------------
# Test 12: Matrix mismatch with identical row counts
# ---------------------------------------------------------------------------

def test_matrix_missing_and_unexpected_cells():
    """Exact expected_cells: duplicate row + missing cell detected."""
    rows = [
        {"decompiler": "fission", "function_name": "f1", "compiler_variant": "gcc -O1"},
        {"decompiler": "fission", "function_name": "f1", "compiler_variant": "gcc -O1"},  # Duplicate
    ]
    # Expected: f1(gcc -O1) and f2(gcc -O1)
    expected_cells = [
        {"decompiler": "fission", "function_name": "f1", "compiler_variant": "gcc -O1"},
        {"decompiler": "fission", "function_name": "f2", "compiler_variant": "gcc -O1"},
    ]
    matrix = {
        "expected_rows": 2,
        "expected_decompilers": ["fission"],
        "expected_cells": expected_cells,
    }
    envelope = rv.build_envelope(rows, matrix=matrix)
    loaded = rv.LoadedResult(rows=envelope["rows"], envelope=envelope, legacy=False)
    verdict = rv.evaluate_run(loaded)
    assert not verdict.valid
    assert "matrix_missing_cells" in verdict.reasons
    assert "matrix_duplicate_cells" in verdict.reasons

# ---------------------------------------------------------------------------
# Test 13: Single backend at 80% coverage with an overall coverage > 90% -> INVALID
# ---------------------------------------------------------------------------

def test_single_backend_under_90_fails():
    fission_rows = _fission_rows(100, 100)
    # Total = 110. Clean = 108. Ratio = 98.1%
    ghidra_rows = _other_rows("ghidra", 10, 8) # 80%
    rows = fission_rows + ghidra_rows
    
    matrix = {
        "expected_decompilers": ["fission", "ghidra"],
    }
    envelope = rv.build_envelope(rows, matrix=matrix)
    loaded = rv.LoadedResult(rows=envelope["rows"], envelope=envelope, legacy=False)
    verdict = rv.evaluate_run(loaded)
    
    assert verdict.overall.ratio > 0.90
    assert not verdict.valid
    assert "backend_coverage_below_threshold" in verdict.reasons

# ---------------------------------------------------------------------------
# P0.6.2 Tests
# ---------------------------------------------------------------------------

def test_valid_smoke_is_not_publishable():
    """Smoke run (official=False) → valid=True but publishable=False."""
    rows = _fission_rows(10, 10) + _other_rows("ghidra", 10, 10)
    envelope = rv.build_envelope(rows, run_meta={"official": False})
    loaded = rv.LoadedResult(rows=envelope["rows"], envelope=envelope, legacy=False)
    verdict = rv.evaluate_run(loaded)
    assert verdict.valid, "Measurement should be valid"
    assert not verdict.publishable, "Smoke should not be publishable"
    assert "non_official_run" in verdict.publish_reasons
    assert "non_official_run" not in verdict.reasons  # not a measurement failure


def test_official_without_matrix_is_not_publishable():
    rows = _fission_rows(10, 10) + _other_rows("ghidra", 10, 10)
    for row in rows:
        row.update(semantic_score=1.0, cases_passed=1, cases_total=1)
    envelope = rv.build_envelope(
        rows,
        run_meta={
            "run_id": "official-test",
            "started_at": "2026-01-01T00:00:00Z",
            "finished_at": "2026-01-01T00:01:00Z",
            "runner_commit": "abc123",
            "corpus": "locked-holdout",
            "official": True,
            "profile": "realistic",
            "limits": {"limit": None, "variant_limit": None, "function": None},
        },
        toolchain={"runner_commit": "abc123"},
    )
    loaded = rv.LoadedResult(rows=envelope["rows"], envelope=envelope, legacy=False)
    verdict = rv.evaluate_run(loaded)
    assert not verdict.valid
    assert not verdict.publishable
    assert "official_matrix_missing" in verdict.reasons


def test_official_exact_matrix_is_candidate_valid_but_needs_final_gate():
    row = _make_row("fission")
    row.update(semantic_score=1.0, correctness_score=1.0, cases_passed=1, cases_total=1)
    cell = {key: row[key] for key in ("decompiler", "function_name", "compiler_variant")}
    envelope = rv.build_envelope(
        [row],
        run_meta={
            "run_id": "official-test",
            "started_at": "2026-01-01T00:00:00Z",
            "finished_at": "2026-01-01T00:01:00Z",
            "runner_commit": "abc123",
            "corpus": "dev",
            "official": True,
            "profile": "realistic",
            "limits": {"limit": None, "variant_limit": None, "function": None},
        },
        toolchain={"runner_commit": "abc123"},
        matrix={
            "expected_decompilers": ["fission"],
            "expected_rows": 1,
            "observed_rows": 1,
            "expected_cells": [cell],
        },
        oracle={
            "mode": "differential", "valid": True,
            "target_abi": "windows-x86_64", "compiler": "mingw",
            "compiler_version": "1", "runner": "wine",
            "wrapper_sha256": "a" * 64, "reference_binary_sha256": "b" * 64,
        },
    )
    verdict = rv.evaluate_run(rv.LoadedResult(rows=[row], envelope=envelope, legacy=False))
    assert verdict.valid
    assert verdict.matrix_valid
    assert verdict.semantic_harness_valid
    assert not verdict.publishable
    assert "final_publication_gate_required" in verdict.publish_reasons


def test_missing_official_flag_is_not_publishable():
    rows = _fission_rows(1, 1)
    envelope = rv.build_envelope(rows)
    verdict = rv.evaluate_run(rv.LoadedResult(rows=rows, envelope=envelope, legacy=False))
    assert verdict.valid
    assert not verdict.publishable
    assert "official_flag_missing" in verdict.publish_reasons


def test_exact_heterogeneous_matrix_cells():
    """Functions with different variant sets: exact cell check, no false positives."""
    # fn1 has gcc-O0 and clang-O2; fn2 has only gcc-O0
    expected_cells = [
        {"decompiler": "fission", "function_name": "fn1", "compiler_variant": "gcc -O0"},
        {"decompiler": "fission", "function_name": "fn1", "compiler_variant": "clang -O2"},
        {"decompiler": "fission", "function_name": "fn2", "compiler_variant": "gcc -O0"},
    ]
    rows = [
        {"decompiler": "fission", "function_name": "fn1", "compiler_variant": "gcc -O0", "error": None},
        {"decompiler": "fission", "function_name": "fn1", "compiler_variant": "clang -O2", "error": None},
        {"decompiler": "fission", "function_name": "fn2", "compiler_variant": "gcc -O0", "error": None},
    ]
    matrix = {"expected_cells": expected_cells, "expected_decompilers": ["fission"], "expected_rows": 3}
    envelope = rv.build_envelope(rows, run_meta={"official": True}, matrix=matrix)
    loaded = rv.LoadedResult(rows=envelope["rows"], envelope=envelope, legacy=False)
    verdict = rv.evaluate_run(loaded)
    # No matrix errors expected
    assert "matrix_missing_cells" not in verdict.reasons
    assert "matrix_unexpected_cells" not in verdict.reasons
    assert "matrix_duplicate_cells" not in verdict.reasons


def test_exact_cells_missing_detected():
    """Missing cell in exact list is flagged."""
    expected_cells = [
        {"decompiler": "fission", "function_name": "fn1", "compiler_variant": "gcc -O0"},
        {"decompiler": "fission", "function_name": "fn2", "compiler_variant": "gcc -O0"},  # missing
    ]
    rows = [
        {"decompiler": "fission", "function_name": "fn1", "compiler_variant": "gcc -O0", "error": None},
    ]
    matrix = {"expected_cells": expected_cells, "expected_decompilers": ["fission"], "expected_rows": 2}
    envelope = rv.build_envelope(rows, run_meta={"official": True}, matrix=matrix)
    loaded = rv.LoadedResult(rows=envelope["rows"], envelope=envelope, legacy=False)
    verdict = rv.evaluate_run(loaded)
    assert "matrix_missing_cells" in verdict.reasons


def test_official_with_empty_expected_cells_is_not_publishable():
    row = _make_row("fission")
    envelope = rv.build_envelope(
        [row],
        run_meta={"official": True},
        matrix={"expected_rows": 0, "observed_rows": 1, "expected_cells": []},
    )
    verdict = rv.evaluate_run(rv.LoadedResult(rows=[row], envelope=envelope, legacy=False))
    assert "official_matrix_missing" in verdict.reasons


def test_expected_matrix_duplicate_is_rejected():
    row = _make_row("fission")
    cell = {key: row[key] for key in ("decompiler", "function_name", "compiler_variant")}
    envelope = rv.build_envelope(
        [row],
        run_meta={"official": True},
        matrix={"expected_rows": 2, "observed_rows": 1, "expected_cells": [cell, cell]},
    )
    verdict = rv.evaluate_run(rv.LoadedResult(rows=[row], envelope=envelope, legacy=False))
    assert "matrix_duplicate_expected_cells" in verdict.reasons


def test_malformed_observed_identity_is_rejected():
    row = _make_row("fission")
    row["compiler_variant"] = ""
    envelope = rv.build_envelope(
        [row],
        run_meta={"official": True},
        matrix={
            "expected_rows": 1,
            "observed_rows": 1,
            "expected_cells": [{
                "decompiler": "fission",
                "function_name": "fixture",
                "compiler_variant": "gcc -O0",
            }],
        },
    )
    verdict = rv.evaluate_run(rv.LoadedResult(rows=[row], envelope=envelope, legacy=False))
    assert "matrix_malformed_observed_cell" in verdict.reasons


def test_smoke_cli_exits_zero(tmp_path):
    """CLI returns exit code 0 for a valid smoke run (publishable=False)."""
    rows = _fission_rows(10, 10) + _other_rows("ghidra", 10, 10)
    envelope = rv.build_envelope(rows, run_meta={"official": False})
    p = tmp_path / "smoke.json"
    import json
    p.write_text(json.dumps(envelope), encoding="utf-8")
    ret = rv.main([str(p)])
    assert ret == 0, "Smoke run should exit 0 (measurement valid)"


def test_invalid_measurement_cli_exits_one(tmp_path):
    """CLI returns exit code 1 when measurement quality fails."""
    # Fission coverage below threshold
    rows = _fission_rows(10, 5) + _other_rows("ghidra", 10, 10)  # 50% fission
    envelope = rv.build_envelope(rows, run_meta={"official": True})
    p = tmp_path / "bad.json"
    import json
    p.write_text(json.dumps(envelope), encoding="utf-8")
    ret = rv.main([str(p)])
    assert ret == 1, "Invalid measurement should exit 1"
