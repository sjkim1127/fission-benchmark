"""Tests for the same-function matrix (MVP-0 infra axis)."""
from __future__ import annotations

from runner.same_function_matrix import (
    BOUNDARY_STATUSES,
    MATRIX_SCHEMA,
    build_same_function_matrix,
    classify_row_status,
    render_markdown,
)
from runner.standard_summary import build_standard_summary


def _row(decompiler: str, status: str, **extra):
    item = {
        "decompiler": decompiler,
        "function_name": extra.pop("function_name", "count_bits"),
        "compiler_variant": extra.pop("compiler_variant", "gcc -O0"),
        "error": extra.pop("error", None),
        "output_diagnostics": {
            "status": status,
            "expected_address_present": status == "direct_function",
            "target_name_present": status == "direct_function",
        },
    }
    item.update(extra)
    return item


def test_classify_row_status_uses_diagnostics() -> None:
    assert classify_row_status(_row("fission", "direct_function")) == "direct_function"
    assert classify_row_status(_row("snowman", "whole_program_output")) == "whole_program_output"
    assert classify_row_status({"error": "boom"}) == "no_output"
    assert classify_row_status({"error": None, "code": ""}) == "no_output"


def test_same_function_rate_definition() -> None:
    rows = [
        _row("fission", "direct_function"),
        _row("fission", "direct_function", function_name="clamp"),
        _row("fission", "boundary_mismatch", function_name="signum"),
        _row("snowman", "direct_function"),
        _row("snowman", "no_output", function_name="clamp", error="extract failed"),
        _row("snowman", "whole_program_output", function_name="signum"),
        _row("ghidra", "needs_normalization"),
        _row("ghidra", "direct_function", function_name="clamp"),
        _row("radare2", "needs_normalization"),
    ]
    matrix = build_same_function_matrix(rows)
    assert matrix["schema"] == MATRIX_SCHEMA

    # fission: 2 direct + 1 boundary → rate 2/3
    fis = matrix["by_decompiler"]["fission"]
    assert fis["cohort"] == "core"
    assert fis["same_function_rate"] == round(2 / 3, 4)
    assert fis["by_status"]["direct_function"] == 2
    assert fis["by_status"]["boundary_mismatch"] == 1

    # snowman: 1 direct + 2 boundary_* (no_output + whole) → 1/3
    sn = matrix["by_decompiler"]["snowman"]
    assert sn["cohort"] == "multi"
    assert sn["same_function_rate"] == round(1 / 3, 4)
    assert sn["boundary_star"] == 2

    # ghidra: 1 direct + 0 boundary; needs_norm not in strict den → 1/1
    gh = matrix["by_decompiler"]["ghidra"]
    assert gh["same_function_rate"] == 1.0
    assert gh["same_function_loose_rate"] == 1.0  # 2/2

    core = matrix["cohorts"]["core"]
    # core rows: fission 3 + ghidra 2 = 5; direct: 2+1=3; boundary: 1; needs: 1
    # strict: 3/(3+1)=0.75
    assert core["same_function_rate"] == 0.75
    assert set(core["decompilers"]) == {"fission", "ghidra"}

    multi = matrix["cohorts"]["multi"]
    assert "snowman" in multi["decompilers"]
    assert "radare2" in multi["decompilers"]

    # boundary_* definition
    assert BOUNDARY_STATUSES == {
        "boundary_mismatch",
        "whole_program_output",
        "no_output",
    }


def test_matrix_table_rows_align_with_by_decompiler() -> None:
    rows = [
        _row("fission", "direct_function"),
        _row("angr", "boundary_mismatch"),
    ]
    matrix = build_same_function_matrix(rows)
    table = {r["decompiler"]: r for r in matrix["matrix"]["rows"]}
    assert table["fission"]["same_function_rate"] == 1.0
    assert table["angr"]["same_function_rate"] == 0.0
    assert table["angr"]["boundary_mismatch"] == 1


def test_standard_summary_embeds_same_function() -> None:
    rows = [
        _row("fission", "direct_function"),
        _row("ghidra", "direct_function"),
        _row("snowman", "whole_program_output"),
    ]
    summary = build_standard_summary(rows)
    sf = summary["mvp"]["same_function"]
    assert sf["schema"] == MATRIX_SCHEMA
    assert sf["contract"]["request"] == "(binary, addr)"
    assert "fission" in sf["by_decompiler"]
    assert sf["cohorts"]["core"]["same_function_rate"] == 1.0
    assert sf["cohorts"]["multi"]["same_function_rate"] == 0.0
    md = render_markdown(build_same_function_matrix(rows))
    assert "Same-function matrix" in md
    assert "same_function_rate" in md
