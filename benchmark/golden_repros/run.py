"""Golden repro runner — fixed regression / known-gap canaries."""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Optional

import typer

from benchmark.abi_parity.run import compare_abi
from benchmark.assembly_parity.run import compare_assembly
from benchmark.cfg_parity.run import compare_cfg
from benchmark.common.http_providers import fetch_parity_json
from benchmark.common.io import write_jsonl
from benchmark.common.providers import canonicalize, run_json_provider
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject
from benchmark.dataflow_parity.run import compare_dataflow
from benchmark.decode_parity.run import compare_decode
from benchmark.function_discovery.run import compare_functions
from benchmark.pcode_parity.run import compare_pcode

app = typer.Typer(pretty_exceptions_enable=False)

COMPARE = {
    "abi_parity": compare_abi,
    "assembly_parity": compare_assembly,
    "dataflow_parity": compare_dataflow,
    "decode_parity": compare_decode,
    "pcode_parity": compare_pcode,
    "cfg_parity": compare_cfg,
    "function_discovery": compare_functions,
}


def subject_from_case(case: dict[str, Any]) -> BenchmarkSubject:
    return BenchmarkSubject(
        binary=str(case["binary"]),
        function=str(case.get("function", case.get("name", "unknown"))),
        addr=str(case.get("addr", "0x0")),
        arch=str(case.get("arch", "unknown")),
        compiler=str(case.get("compiler", "unknown")),
        opt=str(case.get("opt", "unknown")),
        corpus_split=str(case.get("corpus_split", "dev")),
    )


def evaluate_case(case: dict[str, Any], timeout: float) -> BenchmarkResult:
    """Evaluate one golden case (HTTP pair, command, or expected payload)."""
    subject = subject_from_case(case)
    stage = str(case.get("stage") or "golden_repros")
    reference = str(case.get("reference_http") or case.get("reference") or "expected")
    candidate = str(case.get("candidate_http") or case.get("candidate") or "fission")
    expect_status = case.get("expect_status")  # match | mismatch | None (exact payload)
    expect_kind = case.get("expect_mismatch_kind")

    # Optional per-case canonicalize mode (e.g. pcode opcode-normalization lock
    # uses loose; publishable full runs use strict via env).
    prev_mode = os.environ.get("PARITY_CANONICALIZE_MODE")
    case_mode = case.get("canonicalize_mode")
    if case_mode:
        os.environ["PARITY_CANONICALIZE_MODE"] = str(case_mode)

    try:
        return _evaluate_case_body(
            case,
            subject,
            stage,
            reference,
            candidate,
            expect_status,
            expect_kind,
            timeout,
            case_mode=str(case_mode) if case_mode else None,
        )
    finally:
        if case_mode is not None:
            if prev_mode is None:
                os.environ.pop("PARITY_CANONICALIZE_MODE", None)
            else:
                os.environ["PARITY_CANONICALIZE_MODE"] = prev_mode


def _evaluate_case_body(
    case: dict[str, Any],
    subject: BenchmarkSubject,
    stage: str,
    reference: str,
    candidate: str,
    expect_status: Any,
    expect_kind: Any,
    timeout: float,
    *,
    case_mode: str | None,
) -> BenchmarkResult:
    # Path A: HTTP reference vs candidate for a named stage
    if case.get("reference_http") and case.get("candidate_http") and stage in COMPARE:
        expected = fetch_parity_json(case["reference_http"], stage, subject, timeout=timeout)
        actual = fetch_parity_json(case["candidate_http"], stage, subject, timeout=timeout)
        result = COMPARE[stage](subject, reference, candidate, expected, actual)
        # Override stage label to golden_repros while preserving mismatch_kind
        if expect_status is None:
            return BenchmarkResult(
                subject=result.subject,
                stage="golden_repros",
                status=result.status,
                reference=result.reference,
                candidate=result.candidate,
                mismatch_kind=result.mismatch_kind,
                expected=result.expected,
                actual=result.actual,
                metrics={
                    **result.metrics,
                    "parity_stage": stage,
                    "canonicalize_mode": case_mode or os.environ.get("PARITY_CANONICALIZE_MODE", "loose"),
                },
                error=result.error,
            )
        # Known-gap canary: pass if status/kind match expectation
        status_ok = result.status == expect_status
        kind_ok = True
        if expect_kind is not None:
            kind_ok = (result.mismatch_kind or "") == expect_kind
        passed = status_ok and kind_ok
        return BenchmarkResult(
            subject=subject,
            stage="golden_repros",
            status="match" if passed else "mismatch",
            reference=reference,
            candidate=candidate,
            mismatch_kind=None if passed else "golden_expectation",
            expected={
                "expect_status": expect_status,
                "expect_mismatch_kind": expect_kind,
            },
            actual={
                "status": result.status,
                "mismatch_kind": result.mismatch_kind,
            },
            metrics={
                "parity_stage": stage,
                "observed_status": result.status,
                "observed_mismatch_kind": result.mismatch_kind or "",
                "canonicalize_mode": case_mode
                or os.environ.get("PARITY_CANONICALIZE_MODE", "loose"),
            },
            error=None if passed else (
                f"expected status={expect_status!r} kind={expect_kind!r}, "
                f"got status={result.status!r} kind={result.mismatch_kind!r}"
            ),
        )

    # Path B: command template producing actual; compare to expected payload
    if case.get("command"):
        actual = run_json_provider(str(case["command"]), subject, timeout)
        expected = case.get("expected")
        expected_norm = canonicalize(expected)
        actual_norm = canonicalize(actual)
        status = "match" if expected_norm == actual_norm else "mismatch"
        return BenchmarkResult(
            subject=subject,
            stage="golden_repros",
            status=status,
            reference=str(case.get("reference", "expected")),
            candidate=candidate,
            mismatch_kind=None if status == "match" else str(case.get("mismatch_kind", "golden_repro")),
            expected=expected,
            actual=actual,
            metrics={"case_count": 1},
        )

    raise ValueError("case needs reference_http+candidate_http+stage or command+expected")


@app.command()
def main(
    manifest: Path = typer.Argument(
        Path("benchmark/golden_repros/manifest.json"),
        help="Golden repro manifest JSON",
    ),
    output: Path = typer.Option(Path("results/golden_repros/latest.jsonl")),
    timeout: float = typer.Option(90.0),
    limit: Optional[int] = typer.Option(None),
):
    if not manifest.is_file():
        typer.echo(f"manifest not found: {manifest}", err=True)
        raise typer.Exit(1)

    data = json.loads(manifest.read_text(encoding="utf-8"))
    cases = list(data.get("cases") or [])
    if limit is not None:
        cases = cases[:limit]

    rows: list[BenchmarkResult] = []
    for case in cases:
        subject = subject_from_case(case)
        try:
            rows.append(evaluate_case(case, timeout))
        except Exception as exc:
            rows.append(
                BenchmarkResult(
                    subject=subject,
                    stage="golden_repros",
                    status="error",
                    reference=str(case.get("reference_http") or case.get("reference") or "expected"),
                    candidate=str(case.get("candidate_http") or case.get("candidate") or "fission"),
                    error=str(exc),
                )
            )

    write_jsonl(output, rows)
    matched = sum(1 for r in rows if r.status == "match")
    typer.echo(
        f"Wrote {len(rows)} golden repro rows to {output} "
        f"(match={matched}, other={len(rows) - matched})"
    )
    # Non-zero exit if any unexpected failure (for CI canaries)
    if any(r.status in {"mismatch", "error"} for r in rows):
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
