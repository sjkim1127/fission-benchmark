"""SEH / unwind surface parity (flags-level until full RUNTIME_FUNCTION lands)."""
from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer

from benchmark.common.compare_guards import empty_pair_result
from benchmark.common.http_stage import run_http_pair_stage
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject

app = typer.Typer(pretty_exceptions_enable=False)
STAGE = "seh_parity"


def compare_seh(
    subject: BenchmarkSubject,
    reference_name: str,
    candidate_name: str,
    expected: object,
    actual: object,
) -> BenchmarkResult:
    guarded = empty_pair_result(
        subject, STAGE, reference_name, candidate_name, expected, actual  # type: ignore[arg-type]
    )
    if guarded is not None:
        return guarded
    if not isinstance(expected, dict) or not isinstance(actual, dict):
        return BenchmarkResult(
            subject=subject,
            stage=STAGE,  # type: ignore[arg-type]
            status="error",
            reference=reference_name,
            candidate=candidate_name,
            error="non-object seh payload",
        )
    # Compare structural flags only (honest partial surface).
    keys = ("is_thunk", "no_return")
    exp_flags = {k: bool(expected.get(k)) for k in keys}
    act_flags = {k: bool(actual.get(k)) for k in keys}
    metrics = {
        "ref_eh_symbols": int(expected.get("program_eh_symbol_count") or 0),
        "cand_eh_symbols": int(actual.get("program_eh_symbol_count") or 0),
        "ref_surface": str(expected.get("seh_surface") or ""),
        "cand_surface": str(actual.get("seh_surface") or ""),
    }
    if exp_flags == act_flags:
        return BenchmarkResult(
            subject=subject,
            stage=STAGE,  # type: ignore[arg-type]
            status="match",
            reference=reference_name,
            candidate=candidate_name,
            expected=expected,
            actual=actual,
            metrics=metrics,
        )
    return BenchmarkResult(
        subject=subject,
        stage=STAGE,  # type: ignore[arg-type]
        status="mismatch",
        reference=reference_name,
        candidate=candidate_name,
        mismatch_kind="seh_flags",
        expected=expected,
        actual=actual,
        metrics=metrics,
    )


@app.command()
def main(
    reference_http: str = typer.Option("ghidra"),
    candidate_http: str = typer.Option("fission"),
    corpus: str = typer.Option("dev"),
    output: Path = typer.Option(Path("results/seh_parity/latest.jsonl")),
    limit: Optional[int] = typer.Option(None),
    timeout: float = typer.Option(90.0),
):
    run_http_pair_stage(
        stage=STAGE,
        compare=compare_seh,
        reference_http=reference_http,
        candidate_http=candidate_http,
        corpus=corpus,
        output=output,
        limit=limit,
        timeout=timeout,
    )


if __name__ == "__main__":
    app()
