"""Generic HTTP parity stage CLI runner."""
from __future__ import annotations

from pathlib import Path
from typing import Callable, Optional

import typer

from benchmark.common.http_providers import ensure_fission_port, fetch_parity_json
from benchmark.common.io import write_jsonl
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject
from benchmark.common.subjects import load_subjects


def run_http_pair_stage(
    *,
    stage: str,
    compare: Callable[
        [BenchmarkSubject, str, str, object, object], BenchmarkResult
    ],
    reference_http: str = "ghidra",
    candidate_http: str = "fission",
    corpus: str = "dev",
    output: Path,
    limit: Optional[int] = None,
    timeout: float = 90.0,
) -> list[BenchmarkResult]:
    ensure_fission_port()
    subjects = load_subjects(corpus)
    if limit is not None:
        subjects = subjects[:limit]
    rows: list[BenchmarkResult] = []
    for subject in subjects:
        try:
            try:
                exp = fetch_parity_json(reference_http, stage, subject, timeout=timeout)
            except Exception as exc:
                exp = {"status": "error", "error": str(exc)}
            try:
                act = fetch_parity_json(candidate_http, stage, subject, timeout=timeout)
            except Exception as exc:
                act = {"status": "error", "error": str(exc)}
            rows.append(compare(subject, reference_http, candidate_http, exp, act))
        except Exception as exc:
            rows.append(
                BenchmarkResult(
                    subject=subject,
                    stage=stage,  # type: ignore[arg-type]
                    status="error",
                    reference=reference_http,
                    candidate=candidate_http,
                    error=str(exc),
                )
            )
    write_jsonl(output, rows)
    matched = sum(1 for r in rows if r.status == "match")
    typer.echo(f"Wrote {len(rows)} {stage} rows (match={matched}) → {output}")
    return rows
