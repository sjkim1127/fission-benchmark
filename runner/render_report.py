"""Render benchmark report artifacts from a saved JSON result file."""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from dataclasses import asdict
from dataclasses import fields
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from report import generate_report
from output_diagnostics import analyze_output_diagnostics, invalid_output_reason
from readability import summarize_readability_proxy_score
from semantic import verify_semantic_correctness
from test_wrappers import TEST_WRAPPERS
from scoring import FunctionScore, assign_consensus_ranks, check_uses_intrinsics


def load_scores(path: Path) -> list[FunctionScore]:
    data = json.loads(path.read_text(encoding="utf-8"))
    score_fields = {field.name for field in fields(FunctionScore)}
    scores = [FunctionScore(**{k: v for k, v in row.items() if k in score_fields}) for row in data]
    code_counts = Counter(score.decompiled_code.strip() for score in scores if score.decompiled_code.strip())
    for score in scores:
        if not score.correctness_score and score.composite_score:
            score.correctness_score = score.composite_score
        if score.correctness_rank is None and score.consensus_rank is not None:
            score.correctness_rank = score.consensus_rank
        if score.readability_metrics and score.readability_proxy_score is None:
            score.readability_proxy_score = summarize_readability_proxy_score(score.readability_metrics)
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
    parser = argparse.ArgumentParser(description="Render benchmark dashboard from saved results")
    parser.add_argument("--input", required=True, type=Path, help="Input JSON results file")
    parser.add_argument("--corpus", required=True, help="Corpus label to show in the report")
    parser.add_argument(
        "--update-latest",
        action="store_true",
        help="Also copy the input JSON to results/latest.json",
    )
    args = parser.parse_args()

    scores = load_scores(args.input)
    generate_report(scores, corpus_split=args.corpus)

    serialized = json.dumps([asdict(score) for score in scores], indent=2)
    args.input.write_text(serialized, encoding="utf-8")

    if args.update_latest:
        latest_path = Path("results/latest.json")
        latest_path.parent.mkdir(exist_ok=True)
        latest_path.write_text(serialized, encoding="utf-8")

    print(f"Rendered {len(scores)} rows from {args.input} as corpus {args.corpus!r}")


if __name__ == "__main__":
    main()
