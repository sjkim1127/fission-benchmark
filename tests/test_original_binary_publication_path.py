"""End-to-end publication path with original_binary oracle evidence (no Wine)."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from runner.differential_oracle import ORACLE_SUBJECT_ORIGINAL_BINARY, aggregate_oracle_evidence
from runner.holdout_report import generate_report
from runner.publication_gate import evaluate_publication
from runner.run_validity import LoadedResult, build_envelope, evaluate_run, oracle_evidence_valid


def _row(decompiler: str, function_name: str, corpus: str, binary_hash: str) -> dict:
    evidence = {
        "mode": "differential",
        "valid": True,
        "oracle_subject": ORACLE_SUBJECT_ORIGINAL_BINARY,
        "target_abi": "windows-x86_64",
        "compiler": "x86_64-w64-mingw32-gcc",
        "compiler_version": "gcc (GCC) 12",
        "runner": "wine",
        "wrapper_sha256": "a" * 64,
        "reference_binary_sha256": binary_hash,
        "function_addr": "0x140001000",
        "function_rva": "0x1000",
    }
    return {
        "decompiler": decompiler,
        "function_name": function_name,
        "compiler_variant": "gcc -O0",
        "error": None,
        "fail_category": "",
        "source_similarity": 0.5,
        "semantic_score": 1.0,
        "correctness_score": 1.0,
        "correctness_rank": 1,
        "structural_penalty": 0.0,
        "time_ms": 10,
        "cases_passed": 5,
        "cases_total": 5,
        "oracle_evidence": evidence,
    }


def _envelope(corpus: str, run_id: str, rows: list[dict], manifest_hash: str) -> dict:
    cells = [
        {
            "decompiler": row["decompiler"],
            "function_name": row["function_name"],
            "compiler_variant": row["compiler_variant"],
        }
        for row in rows
    ]
    return build_envelope(
        rows,
        run_meta={
            "run_id": run_id,
            "started_at": "2026-07-12T00:00:00Z",
            "finished_at": "2026-07-12T00:05:00Z",
            "runner_commit": "abc1234",
            "corpus": corpus,
            "corpus_manifest_sha256": manifest_hash,
            "official": True,
            "profile": "realistic",
            "limits": {"limit": None, "variant_limit": None, "function": None},
        },
        toolchain={"runner_commit": "abc1234", "fission_source": "release"},
        matrix={
            "expected_decompilers": sorted({row["decompiler"] for row in rows}),
            "expected_rows": len(rows),
            "observed_rows": len(rows),
            "expected_cells": cells,
        },
        oracle=aggregate_oracle_evidence(rows),
    )


def test_original_binary_evidence_satisfies_oracle_gate() -> None:
    rows = [_row("fission", "clamp", "dev", "b" * 64)]
    envelope = _envelope("dev", "dev-run", rows, "c" * 64)
    assert envelope["oracle"]["oracle_subject"] == ORACLE_SUBJECT_ORIGINAL_BINARY
    assert oracle_evidence_valid(envelope) is True
    verdict = evaluate_run(LoadedResult(rows=rows, envelope=envelope, legacy=False))
    assert verdict.valid is True
    assert verdict.semantic_harness_valid is True
    assert verdict.official_profile_valid is True
    # Single-artifact evaluate_run still requires the final multi-file gate.
    assert "final_publication_gate_required" in verdict.publish_reasons
    assert verdict.publishable is False


def test_full_publication_gate_with_original_binary_and_holdout(tmp_path: Path) -> None:
    binary_hash = "d" * 64
    manifest_hash = "e" * 64
    dev_rows = [
        _row("fission", "clamp", "dev", binary_hash),
        _row("ghidra", "clamp", "dev", binary_hash),
    ]
    holdout_rows = [
        _row("fission", "max", "holdout", binary_hash),
        _row("ghidra", "max", "holdout", binary_hash),
    ]
    dev_path = tmp_path / "dev.json"
    holdout_path = tmp_path / "holdout.json"
    overfit_path = tmp_path / "overfit.json"
    dev_path.write_text(
        json.dumps(_envelope("dev", "dev-run", dev_rows, manifest_hash)),
        encoding="utf-8",
    )
    holdout_path.write_text(
        json.dumps(_envelope("holdout", "holdout-run", holdout_rows, manifest_hash)),
        encoding="utf-8",
    )

    report = generate_report(
        dev_path=dev_path,
        holdout_path=holdout_path,
        json_output_path=overfit_path,
    )
    assert report["passed"] is True
    assert report["dev_envelope_sha256"] == hashlib.sha256(dev_path.read_bytes()).hexdigest()
    assert report["holdout_envelope_sha256"] == hashlib.sha256(holdout_path.read_bytes()).hexdigest()

    verdict = evaluate_publication(dev_path, holdout_path, overfit_path)
    assert verdict["reasons"] == []
    assert verdict["publishable"] is True
