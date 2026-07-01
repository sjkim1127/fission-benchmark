"""Shared result construction helpers."""
from __future__ import annotations

from benchmark.common.schema import BenchmarkResult, BenchmarkStage, BenchmarkSubject


def error_result(
    subject: BenchmarkSubject,
    stage: BenchmarkStage,
    reference: str,
    candidate: str,
    error: str,
) -> BenchmarkResult:
    return BenchmarkResult(
        subject=subject,
        stage=stage,
        status="error",
        reference=reference,
        candidate=candidate,
        error=error,
    )
