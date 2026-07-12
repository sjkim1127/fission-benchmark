"""Data-flow sink parity — RETURN/STORE sink sets vs Ghidra."""
from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer

from benchmark.common.http_stage import run_http_pair_stage
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject
from benchmark.common.set_compare import as_str_set, compare_payload_sets, jaccard

app = typer.Typer(pretty_exceptions_enable=False)
STAGE = "dataflow_parity"


def _sinks(payload: object) -> set[str]:
    if not isinstance(payload, dict):
        return set()
    tokens = list(payload.get("return_sinks") or []) + list(payload.get("store_sinks") or [])
    return as_str_set(tokens)


def compare_dataflow(
    subject: BenchmarkSubject,
    reference_name: str,
    candidate_name: str,
    expected: object,
    actual: object,
) -> BenchmarkResult:
    row = compare_payload_sets(
        subject,
        STAGE,
        reference_name,
        candidate_name,
        expected,
        actual,
        extract=_sinks,
        mismatch_kind="sink_set",
    )
    # Dual: return-only Jaccard for canary triage
    exp_ret = as_str_set((expected or {}).get("return_sinks") or []) if isinstance(expected, dict) else set()
    act_ret = as_str_set((actual or {}).get("return_sinks") or []) if isinstance(actual, dict) else set()
    metrics = dict(row.metrics or {})
    metrics["return_jaccard"] = jaccard(exp_ret, act_ret)
    return BenchmarkResult(
        subject=row.subject,
        stage=row.stage,
        status=row.status,
        reference=row.reference,
        candidate=row.candidate,
        mismatch_kind=row.mismatch_kind,
        expected=row.expected,
        actual=row.actual,
        metrics=metrics,
        error=row.error,
    )


@app.command()
def main(
    reference_http: str = typer.Option("ghidra"),
    candidate_http: str = typer.Option("fission"),
    corpus: str = typer.Option("dev"),
    output: Path = typer.Option(Path("results/dataflow_parity/latest.jsonl")),
    limit: Optional[int] = typer.Option(None),
    timeout: float = typer.Option(90.0),
):
    run_http_pair_stage(
        stage=STAGE,
        compare=compare_dataflow,
        reference_http=reference_http,
        candidate_http=candidate_http,
        corpus=corpus,
        output=output,
        limit=limit,
        timeout=timeout,
    )


if __name__ == "__main__":
    app()
