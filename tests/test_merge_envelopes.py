"""Envelope merge for full_matrix fan-out."""
from __future__ import annotations

import json
from pathlib import Path

from scripts.merge_envelopes import merge_envelopes


def _mini_env(rows: list[dict], profile: str) -> dict:
    return {
        "schema_version": 2,
        "run": {
            "official": False,
            "matrix_profile": profile,
            "profile": "diagnostic",
            "corpus": "dev",
            "run_id": f"run-{profile}",
            "started_at": "2026-01-01T00:00:00Z",
            "finished_at": "2026-01-01T00:01:00Z",
            "runner_commit": "abc",
            "limits": {},
        },
        "toolchain": {"runner_commit": "abc"},
        "matrix": {
            "expected_decompilers": ["fission"],
            "expected_cells": [],
            "expected_rows": 0,
            "observed_rows": len(rows),
        },
        "oracle": {"mode": "example_cases", "valid": False},
        "rows": rows,
    }


def test_merge_envelopes_concat_and_dedupe() -> None:
    a = _mini_env(
        [
            {
                "decompiler": "fission",
                "function_name": "count_bits",
                "compiler_variant": "gcc -O0",
                "semantic_score": 1.0,
                "cases_passed": 6,
                "cases_total": 6,
                "time_ms": 10,
                "error": None,
                "fail_category": "ok",
                "source_similarity": 0.1,
                "goto_count": 0,
                "nesting_depth": 1,
            }
        ],
        "core_c_pe",
    )
    b = _mini_env(
        [
            {
                "decompiler": "fission",
                "function_name": "count_bits",
                "compiler_variant": "gcc -O0",
                "semantic_score": 0.5,  # duplicate key — ignored
                "cases_passed": 3,
                "cases_total": 6,
                "time_ms": 10,
                "error": None,
                "fail_category": "assertion_fail",
                "source_similarity": 0.1,
                "goto_count": 0,
                "nesting_depth": 1,
            },
            {
                "decompiler": "fission",
                "function_name": "cpp_add_ints",
                "compiler_variant": "g++ -O0",
                "semantic_score": 1.0,
                "cases_passed": 6,
                "cases_total": 6,
                "time_ms": 12,
                "error": None,
                "fail_category": "ok",
                "source_similarity": 0.2,
                "goto_count": 0,
                "nesting_depth": 1,
            },
        ],
        "lang_cpp",
    )
    merged = merge_envelopes([a, b], source_labels=["core_c_pe", "lang_cpp"])
    assert len(merged["rows"]) == 2
    names = {r["function_name"] for r in merged["rows"]}
    assert names == {"count_bits", "cpp_add_ints"}
    # First slice wins on duplicate
    cb = next(r for r in merged["rows"] if r["function_name"] == "count_bits")
    assert cb["semantic_score"] == 1.0
    assert merged["run"]["matrix_profile"] == "full_matrix"
    assert merged["run"]["merged_from"] == ["core_c_pe", "lang_cpp"]
    assert merged["matrix"]["expected_rows"] == 2
    assert "summary" in merged
    assert "validity" in merged


def test_merge_envelopes_cli(tmp_path: Path) -> None:
    a = tmp_path / "a.json"
    b = tmp_path / "b.json"
    out = tmp_path / "out.json"
    a.write_text(
        json.dumps(
            _mini_env(
                [
                    {
                        "decompiler": "fission",
                        "function_name": "a",
                        "compiler_variant": "gcc -O0",
                        "semantic_score": 1.0,
                        "cases_passed": 1,
                        "cases_total": 1,
                        "time_ms": 1,
                        "error": None,
                        "fail_category": "ok",
                        "source_similarity": 0.0,
                        "goto_count": 0,
                        "nesting_depth": 0,
                    }
                ],
                "core_c_pe",
            )
        )
    )
    b.write_text(
        json.dumps(
            _mini_env(
                [
                    {
                        "decompiler": "fission",
                        "function_name": "b",
                        "compiler_variant": "gcc -O0",
                        "semantic_score": 1.0,
                        "cases_passed": 1,
                        "cases_total": 1,
                        "time_ms": 1,
                        "error": None,
                        "fail_category": "ok",
                        "source_similarity": 0.0,
                        "goto_count": 0,
                        "nesting_depth": 0,
                    }
                ],
                "lang_rust",
            )
        )
    )
    from scripts.merge_envelopes import main

    assert main([str(a), str(b), "-o", str(out)]) == 0
    merged = json.loads(out.read_text())
    assert len(merged["rows"]) == 2
