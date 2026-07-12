"""ABI / calling-convention parity (scaffold).

Skipped until both adapters implement a real /abi surface. Never scores empty
or not_implemented payloads as match.
"""
from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer

from benchmark.common.http_providers import fetch_parity_json
from benchmark.common.io import write_jsonl
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject
from benchmark.common.subjects import load_subjects

app = typer.Typer(pretty_exceptions_enable=False)

STAGE = "abi_parity"


def _is_implemented(payload: object) -> bool:
    if not isinstance(payload, dict):
        return False
    if payload.get("status") in {"not_implemented", "unsupported", "empty"}:
        return False
    params = payload.get("parameters")
    return isinstance(params, list) and len(params) > 0


def compare_abi(
    subject: BenchmarkSubject,
    reference_name: str,
    candidate_name: str,
    expected: object,
    actual: object,
) -> BenchmarkResult:
    if not _is_implemented(expected) and not _is_implemented(actual):
        return BenchmarkResult(
            subject=subject,
            stage=STAGE,  # type: ignore[arg-type]
            status="skipped",
            reference=reference_name,
            candidate=candidate_name,
            mismatch_kind="abi_surface_pending",
            expected=expected,
            actual=actual,
            metrics={"abi_surface": "not_implemented"},
            error="ABI surface not implemented on adapters — stage not scored",
        )
    if not _is_implemented(expected):
        return BenchmarkResult(
            subject=subject,
            stage=STAGE,  # type: ignore[arg-type]
            status="reference_empty",
            reference=reference_name,
            candidate=candidate_name,
            expected=expected,
            actual=actual,
            error="Reference ABI empty/not_implemented",
        )
    if not _is_implemented(actual):
        return BenchmarkResult(
            subject=subject,
            stage=STAGE,  # type: ignore[arg-type]
            status="candidate_empty",
            reference=reference_name,
            candidate=candidate_name,
            expected=expected,
            actual=actual,
            error="Candidate ABI empty/not_implemented",
        )
    # Structural equality on normalized parameters when both present.
    exp_p = (expected or {}).get("parameters") if isinstance(expected, dict) else None
    act_p = (actual or {}).get("parameters") if isinstance(actual, dict) else None
    match = exp_p == act_p and (
        (expected or {}).get("return") == (actual or {}).get("return")
        if isinstance(expected, dict) and isinstance(actual, dict)
        else False
    )
    return BenchmarkResult(
        subject=subject,
        stage=STAGE,  # type: ignore[arg-type]
        status="match" if match else "mismatch",
        reference=reference_name,
        candidate=candidate_name,
        mismatch_kind=None if match else "abi_parameters",
        expected=expected,
        actual=actual,
        metrics={
            "ref_param_count": len(exp_p) if isinstance(exp_p, list) else 0,
            "cand_param_count": len(act_p) if isinstance(act_p, list) else 0,
        },
    )


@app.command()
def main(
    reference_http: str = typer.Option("ghidra"),
    candidate_http: str = typer.Option("fission"),
    corpus: str = typer.Option("dev"),
    output: Path = typer.Option(Path("results/abi_parity/latest.jsonl")),
    limit: Optional[int] = typer.Option(None),
    timeout: float = typer.Option(30.0),
):
    rows: list[BenchmarkResult] = []
    subjects = load_subjects(corpus)
    if limit is not None:
        subjects = subjects[:limit]
    for subject in subjects:
        try:
            # fetch_parity_json will fail until STAGE_ENDPOINT has abi — catch as skip
            try:
                exp = fetch_parity_json(reference_http, STAGE, subject, timeout=timeout)
            except Exception:
                exp = {"status": "not_implemented"}
            try:
                act = fetch_parity_json(candidate_http, STAGE, subject, timeout=timeout)
            except Exception:
                act = {"status": "not_implemented"}
            rows.append(compare_abi(subject, reference_http, candidate_http, exp, act))
        except Exception as exc:
            rows.append(
                BenchmarkResult(
                    subject=subject,
                    stage=STAGE,  # type: ignore[arg-type]
                    status="error",
                    reference=reference_http,
                    candidate=candidate_http,
                    error=str(exc),
                )
            )
    write_jsonl(output, rows)
    skipped = sum(1 for r in rows if r.status == "skipped")
    typer.echo(f"Wrote {len(rows)} abi rows ({skipped} skipped pending surface) to {output}")


if __name__ == "__main__":
    app()
