"""Render benchmark report artifacts from a saved JSON result file.

This script is NON-DESTRUCTIVE by default: it never modifies the input file.
Use --write-normalized to write a normalised copy, or --update-latest to copy
the normalised result to results/latest.json.

Measured-at timestamp
---------------------
If the input is in envelope format (schema_version >= 2), the ``run.finished_at``
field is extracted and shown in the report header as "Measured at".
For legacy flat-list files the timestamp is shown as "unknown (legacy)".
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from dataclasses import asdict
from dataclasses import fields
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from report import generate_report, generate_markdown, generate_html
from output_diagnostics import analyze_output_diagnostics, invalid_output_reason
from readability import summarize_readability_proxy_score
from semantic import verify_semantic_correctness
from test_wrappers import TEST_WRAPPERS
from scoring import FunctionScore, assign_consensus_ranks, check_uses_intrinsics
from run_validity import load_result_file


def _normalise_scores(data: list[dict]) -> list[FunctionScore]:
    """Convert raw row dicts to FunctionScore objects with re-scoring."""
    score_fields = {field.name for field in fields(FunctionScore)}
    scores = [
        FunctionScore(**{k: v for k, v in row.items() if k in score_fields})
        for row in data
    ]
    code_counts = Counter(
        score.decompiled_code.strip()
        for score in scores
        if score.decompiled_code.strip()
    )
    for score in scores:
        if not score.correctness_score and score.composite_score:
            score.correctness_score = score.composite_score
        if score.correctness_rank is None and score.consensus_rank is not None:
            score.correctness_rank = score.consensus_rank
        if score.readability_metrics and score.readability_proxy_score is None:
            score.readability_proxy_score = summarize_readability_proxy_score(
                score.readability_metrics
            )
        if score.decompiled_code and not score.output_diagnostics:
            score.output_diagnostics = analyze_output_diagnostics(
                score.function_name,
                score.decompiler,
                score.decompiled_code,
            )
        if score.decompiled_code and not score.error:
            reason = invalid_output_reason(
                score.output_diagnostics,
                score.decompiled_code,
                duplicate_count=code_counts.get(score.decompiled_code.strip(), 0),
            )
            if reason:
                score.error = reason
                score.semantic_error = reason
                score.fail_category = "adapter_error"
                score.readability_metrics = {}
                score.readability_proxy_score = None
                score.ast_similarity = {}
        if score.error:
            score.semantic_error = score.semantic_error or score.error
            score.fail_category = score.fail_category or "adapter_error"
            score.source_similarity = 0.0
            score.goto_count = 0
            score.nesting_depth = 0
            score.semantic_score = 0.0
            score.cases_passed = 0
            score.cases_total = 0
            score.correctness_score = 0.0
            score.composite_score = 0.0
            score.correctness_rank = None
            score.consensus_rank = None
        elif score.fail_category == "no_wrapper" and score.function_name in TEST_WRAPPERS:
            (
                score.semantic_score,
                score.semantic_error,
                score.fail_category,
                score.cases_passed,
                score.cases_total,
            ) = verify_semantic_correctness(score.function_name, score.decompiled_code)
        if score.decompiled_code and not score.uses_intrinsics:
            score.uses_intrinsics = check_uses_intrinsics(score.decompiled_code)

    metrics_path = Path(__file__).parent.parent / "corpus" / "source_metrics.json"
    if metrics_path.exists():
        metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
        return assign_consensus_ranks(
            scores,
            source_goto_counts=metrics.get("goto_counts", {}),
            source_nesting_depths=metrics.get("nesting_depths", {}),
        )
    return assign_consensus_ranks(scores)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Render benchmark dashboard from saved results (NON-DESTRUCTIVE by default)"
    )
    parser.add_argument("--input", required=True, type=Path, help="Input JSON results file")
    parser.add_argument("--corpus", required=True, help="Corpus label to show in the report")
    parser.add_argument(
        "--update-latest",
        action="store_true",
        help="Copy the normalised JSON to results/latest.json and regenerate latest.md / docs/index.html",
    )
    parser.add_argument(
        "--write-normalized",
        type=Path,
        default=None,
        help="Write the normalised (re-scored) rows to this path without touching --input",
    )
    args = parser.parse_args()

    # ── Load without modifying the input file ─────────────────────────────────
    rows, is_legacy = load_result_file(args.input)

    # Extract provenance from envelope when available
    measured_at: str | None = None
    if not is_legacy:
        raw = json.loads(args.input.read_text(encoding="utf-8"))
        run_meta = raw.get("run", {})
        measured_at = run_meta.get("finished_at") or run_meta.get("started_at")

    if is_legacy:
        measured_at_label = "unknown (legacy)"
    else:
        measured_at_label = measured_at or "not recorded"

    # ── Normalise / re-score ───────────────────────────────────────────────────
    scores = _normalise_scores(rows)

    # ── Generate report artifacts ──────────────────────────────────────────────
    # Pass measured_at and legacy flag so the banner is correct.
    generate_report(
        scores,
        corpus_split=args.corpus,
        measured_at=measured_at_label,
        legacy=is_legacy,
    )

    # ── Write normalised JSON only if explicitly requested ─────────────────────
    # NEVER write back to args.input.
    serialized = json.dumps([asdict(score) for score in scores], indent=2)

    if args.write_normalized:
        args.write_normalized.parent.mkdir(parents=True, exist_ok=True)
        args.write_normalized.write_text(serialized, encoding="utf-8")
        print(f"Normalised rows written to {args.write_normalized}")

    if args.update_latest:
        latest_path = Path("results/latest.json")
        latest_path.parent.mkdir(exist_ok=True)
        latest_path.write_text(serialized, encoding="utf-8")
        print(f"results/latest.json updated ({len(scores)} rows)")

    print(
        f"Rendered {len(scores)} rows from {args.input} as corpus {args.corpus!r} "
        f"(measured_at={measured_at_label!r}, legacy={is_legacy})"
    )


if __name__ == "__main__":
    main()
