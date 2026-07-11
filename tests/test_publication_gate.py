import hashlib
import json
from pathlib import Path

from runner.holdout_report import aggregate_by_decompiler
from runner.publication_gate import evaluate_publication
from runner.run_validity import build_envelope


def _candidate(corpus: str, run_id: str) -> dict:
    row = {
        "decompiler": "fission",
        "function_name": f"{corpus}_function",
        "compiler_variant": "gcc -O0",
        "error": None,
        "fail_category": "",
        "source_similarity": 0.5,
        "semantic_score": 1.0,
        "correctness_score": 1.0,
        "correctness_rank": 1,
        "structural_penalty": 0.0,
        "time_ms": 1,
        "cases_passed": 1,
        "cases_total": 1,
    }
    cell = {key: row[key] for key in ("decompiler", "function_name", "compiler_variant")}
    return build_envelope(
        [row],
        run_meta={
            "run_id": run_id,
            "started_at": "2026-01-01T00:00:00Z",
            "finished_at": "2026-01-01T00:01:00Z",
            "runner_commit": "abc123",
            "corpus": corpus,
            "corpus_manifest_sha256": "c" * 64,
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


def _write_json(path: Path, value: dict) -> str:
    path.write_text(json.dumps(value), encoding="utf-8")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_publication_gate_links_dev_holdout_and_overfitting(tmp_path: Path) -> None:
    dev_path = tmp_path / "dev.json"
    holdout_path = tmp_path / "holdout.json"
    overfit_path = tmp_path / "overfit.json"
    dev_hash = _write_json(dev_path, _candidate("dev", "dev-run"))
    holdout_hash = _write_json(holdout_path, _candidate("holdout", "holdout-run"))
    _write_json(overfit_path, {
        "passed": True,
        "dev_envelope_sha256": dev_hash,
        "holdout_envelope_sha256": holdout_hash,
    })

    verdict = evaluate_publication(dev_path, holdout_path, overfit_path)
    assert verdict["publishable"] is True
    assert verdict["reasons"] == []


def test_publication_gate_rejects_unlinked_overfitting_evidence(tmp_path: Path) -> None:
    dev_path = tmp_path / "dev.json"
    holdout_path = tmp_path / "holdout.json"
    overfit_path = tmp_path / "overfit.json"
    _write_json(dev_path, _candidate("dev", "dev-run"))
    _write_json(holdout_path, _candidate("holdout", "holdout-run"))
    _write_json(overfit_path, {
        "passed": True,
        "dev_envelope_sha256": "0" * 64,
        "holdout_envelope_sha256": "0" * 64,
    })

    verdict = evaluate_publication(dev_path, holdout_path, overfit_path)
    assert verdict["publishable"] is False
    assert "overfitting_dev_hash_mismatch" in verdict["reasons"]


def test_holdout_aggregation_ignores_unmeasured_correctness() -> None:
    aggregate = aggregate_by_decompiler([
        {"decompiler": "fission", "error": None, "correctness_score": None, "semantic_score": None, "source_similarity": 0.5},
        {"decompiler": "fission", "error": None, "correctness_score": 1.0, "semantic_score": 1.0, "source_similarity": 0.5},
    ])
    assert aggregate["fission"]["correctness_tested"] == 1
    assert aggregate["fission"]["avg_correctness"] == 1.0
