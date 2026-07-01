"""IR invariant runner."""
from __future__ import annotations

from pathlib import Path

import typer

from benchmark.common.io import write_jsonl
from benchmark.common.providers import run_json_provider
from benchmark.common.result import error_result
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject
from benchmark.common.subjects import load_subjects

app = typer.Typer(pretty_exceptions_enable=False)


def violations_from(payload: object) -> list:
    if isinstance(payload, dict) and isinstance(payload.get("violations"), list):
        return payload["violations"]
    if isinstance(payload, list):
        return payload
    return [{"kind": "invalid_payload", "detail": "expected object with violations list"}]


def metrics_from(payload: object) -> dict[str, int | float | str]:
    if isinstance(payload, dict) and isinstance(payload.get("metrics"), dict):
        metrics = payload["metrics"]
        return {
            str(k): v
            for k, v in metrics.items()
            if isinstance(v, (int, float, str)) and not isinstance(v, bool)
        }
    return {}


def compare_invariants(
    subject: BenchmarkSubject,
    candidate_name: str,
    payload: object,
) -> BenchmarkResult:
    violations = violations_from(payload)
    metrics = metrics_from(payload)
    metrics["violation_count"] = len(violations)
    if not violations:
        return BenchmarkResult(
            subject=subject,
            stage="ir_invariants",
            status="match",
            reference="invariants",
            candidate=candidate_name,
            actual=payload,
            metrics=metrics,
        )

    first = violations[0] if isinstance(violations[0], dict) else {}
    return BenchmarkResult(
        subject=subject,
        stage="ir_invariants",
        status="mismatch",
        reference="invariants",
        candidate=candidate_name,
        mismatch_kind=str(first.get("kind", "invariant_violation")),
        actual=payload,
        metrics=metrics,
    )


@app.command()
def main(
    candidate_command: str = typer.Option(..., help="Command template producing invariant JSON"),
    candidate_name: str = typer.Option("fission"),
    corpus: str = typer.Option("dev"),
    output: Path = typer.Option(Path("results/ir_invariants/latest.jsonl")),
    limit: int | None = typer.Option(None),
    timeout: float = typer.Option(30.0),
):
    rows: list[BenchmarkResult] = []
    subjects = load_subjects(corpus)
    if limit is not None:
        subjects = subjects[:limit]

    for subject in subjects:
        try:
            payload = run_json_provider(candidate_command, subject, timeout)
            rows.append(compare_invariants(subject, candidate_name, payload))
        except Exception as exc:
            rows.append(error_result(subject, "ir_invariants", "invariants", candidate_name, str(exc)))

    write_jsonl(output, rows)
    typer.echo(f"Wrote {len(rows)} IR invariant rows to {output}")


if __name__ == "__main__":
    app()
