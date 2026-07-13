"""Tests for scripts/check_dashboard_data.py."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "check_dashboard_data.py"


def _load_mod():
    spec = importlib.util.spec_from_file_location("check_dashboard_data", SCRIPT)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _envelope(rows: int = 3, valid: bool = True) -> dict:
    return {
        "schema_version": 2,
        "run": {"corpus": "dev", "official": False},
        "toolchain": {},
        "matrix": {
            "expected_decompilers": ["fission"],
            "expected_cells": [],
            "expected_rows": rows,
            "observed_rows": rows,
        },
        "oracle": {"mode": "example_cases", "valid": False},
        "validity": {
            "valid": valid,
            "publishable": False,
            "reasons": [],
            "publish_reasons": ["final_publication_gate_required"],
        },
        "rows": [
            {
                "decompiler": "fission",
                "function_name": f"fn{i}",
                "compiler_variant": "gcc -O0",
                "semantic_score": 1.0,
                "correctness_score": 1.0,
                "source_similarity": 0.0,
                "time_ms": 1,
            }
            for i in range(rows)
        ],
    }


def test_evaluate_envelope_ok():
    mod = _load_mod()
    errs = mod.evaluate_envelope(
        _envelope(5, True), source="t", min_rows=1, require_valid=True
    )
    assert errs == []


def test_evaluate_envelope_empty_rows():
    mod = _load_mod()
    errs = mod.evaluate_envelope(
        _envelope(0, True), source="t", min_rows=1, require_valid=True
    )
    assert any("rows=0" in e for e in errs)


def test_evaluate_envelope_min_decompilers():
    mod = _load_mod()
    # single-tool envelope fails multi requirement
    errs = mod.evaluate_envelope(
        _envelope(5, True),
        source="t",
        min_rows=1,
        require_valid=True,
        min_decompilers=8,
    )
    assert any("min_decompilers" in e for e in errs)


def test_main_fails_without_local_data(tmp_path: Path):
    mod = _load_mod()
    # empty root — no results/
    rc = mod.main(["--root", str(tmp_path), "--min-rows", "1"])
    assert rc == 1


def test_main_ok_with_dev_latest(tmp_path: Path):
    mod = _load_mod()
    results = tmp_path / "results"
    results.mkdir()
    (results / "dev_latest.json").write_text(
        json.dumps(_envelope(12, True)), encoding="utf-8"
    )
    rc = mod.main(
        [
            "--root",
            str(tmp_path),
            "--min-rows",
            "10",
            "--require-valid",
        ]
    )
    assert rc == 0


def test_repo_has_displayable_data_or_skip():
    """If this checkout tracks display data, the gate must pass locally."""
    mod = _load_mod()
    candidates = [
        ROOT / "public" / "benchmark-latest.json",
        ROOT / "results" / "latest.json",
        ROOT / "results" / "dev_latest.json",
    ]
    if not any(p.is_file() for p in candidates):
        pytest.skip("no local display envelope in this checkout")
    rc = mod.main(["--root", str(ROOT), "--min-rows", "1"])
    assert rc == 0
