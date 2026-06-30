"""Assembly parity runner."""
from __future__ import annotations

from pathlib import Path

import typer

from benchmark.common.io import write_jsonl
from benchmark.common.providers import canonicalize, run_json_provider
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject
from benchmark.common.subjects import load_subjects

app = typer.Typer(pretty_exceptions_enable=False)


def compare_assembly(
    subject: BenchmarkSubject,
    reference_name: str,
    candidate_name: str,
    expected: object,
    actual: object,
) -> BenchmarkResult:
    expected_norm = canonicalize(expected)
    actual_norm = canonicalize(actual)
    if expected_norm == actual_norm:
        return BenchmarkResult(
            subject=subject,
            stage="assembly_parity",
            status="match",
            reference=reference_name,
            candidate=candidate_name,
            expected=expected,
            actual=actual,
            metrics={"instruction_count": len(expected) if isinstance(expected, list) else 0},
        )

    mismatch_kind = "instruction_sequence"
    if isinstance(expected_norm, list) and isinstance(actual_norm, list):
        if len(expected_norm) != len(actual_norm):
            mismatch_kind = "instruction_count"

    return BenchmarkResult(
        subject=subject,
        stage="assembly_parity",
        status="mismatch",
        reference=reference_name,
        candidate=candidate_name,
        mismatch_kind=mismatch_kind,
        expected=expected,
        actual=actual,
        metrics={
            "expected_instruction_count": len(expected) if isinstance(expected, list) else 0,
            "actual_instruction_count": len(actual) if isinstance(actual, list) else 0,
        },
    )


@app.command()
def main(
    reference_command: str = typer.Option(..., help="Command template producing reference JSON"),
    candidate_command: str = typer.Option(..., help="Command template producing candidate JSON"),
    reference_name: str = typer.Option("reference"),
    candidate_name: str = typer.Option("candidate"),
    corpus: str = typer.Option("dev"),
    output: Path = typer.Option(Path("results/assembly_parity/latest.jsonl")),
    limit: int | None = typer.Option(None),
    timeout: float = typer.Option(30.0),
):
    rows: list[BenchmarkResult] = []
    subjects = load_subjects(corpus)
    if limit is not None:
        subjects = subjects[:limit]

    for subject in subjects:
        try:
            expected = run_json_provider(reference_command, subject, timeout)
            actual = run_json_provider(candidate_command, subject, timeout)
            rows.append(compare_assembly(subject, reference_name, candidate_name, expected, actual))
        except Exception as exc:
            rows.append(
                BenchmarkResult(
                    subject=subject,
                    stage="assembly_parity",
                    status="error",
                    reference=reference_name,
                    candidate=candidate_name,
                    error=str(exc),
                )
            )

    write_jsonl(output, rows)
    typer.echo(f"Wrote {len(rows)} assembly parity rows to {output}")


if __name__ == "__main__":
    app()
