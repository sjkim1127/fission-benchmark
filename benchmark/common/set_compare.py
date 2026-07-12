"""Shared set/list comparison helpers for extension parity stages."""
from __future__ import annotations

from typing import Any, Callable, Iterable

from benchmark.common.compare_guards import empty_pair_result
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject


def jaccard(a: set[Any], b: set[Any]) -> float:
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return round(inter / union, 4) if union else 0.0


def compare_payload_sets(
    subject: BenchmarkSubject,
    stage: str,
    reference_name: str,
    candidate_name: str,
    expected: object,
    actual: object,
    *,
    extract: Callable[[object], set[Any]],
    mismatch_kind: str,
    metrics_extra: dict[str, Any] | None = None,
) -> BenchmarkResult:
    """Primary equality on extracted sets; dual metrics include Jaccard."""
    guarded = empty_pair_result(
        subject, stage, reference_name, candidate_name, expected, actual  # type: ignore[arg-type]
    )
    if guarded is not None:
        return guarded

    exp_set = extract(expected)
    act_set = extract(actual)
    metrics: dict[str, Any] = {
        "ref_count": len(exp_set),
        "cand_count": len(act_set),
        "shared": len(exp_set & act_set),
        "jaccard": jaccard(exp_set, act_set),
    }
    if metrics_extra:
        metrics.update(metrics_extra)

    if exp_set == act_set:
        return BenchmarkResult(
            subject=subject,
            stage=stage,  # type: ignore[arg-type]
            status="match",
            reference=reference_name,
            candidate=candidate_name,
            expected=expected,
            actual=actual,
            metrics=metrics,
        )
    return BenchmarkResult(
        subject=subject,
        stage=stage,  # type: ignore[arg-type]
        status="mismatch",
        reference=reference_name,
        candidate=candidate_name,
        mismatch_kind=mismatch_kind,
        expected=expected,
        actual=actual,
        metrics=metrics,
    )


def as_str_set(items: Iterable[Any]) -> set[str]:
    out: set[str] = set()
    for item in items:
        text = str(item).strip().lower()
        if text:
            out.add(text)
    return out
