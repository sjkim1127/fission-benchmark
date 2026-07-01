"""Golden repro runner."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import typer

from benchmark.common.io import write_jsonl
from benchmark.common.providers import canonicalize, run_json_provider
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject

app = typer.Typer(pretty_exceptions_enable=False)


def subject_from_case(case: dict[str, Any]) -> BenchmarkSubject:
    return BenchmarkSubject(
        binary=str(case["binary"]),
        function=str(case.get("function", case["name"])),
        addr=str(case["addr"]),
        arch=str(case.get("arch", "unknown")),
        compiler=str(case.get("compiler", "unknown")),
        opt=str(case.get("opt", "unknown")),
        corpus_split=str(case.get("corpus_split", "golden")),
    )


def compare_golden(case: dict[str, Any], actual: object) -> BenchmarkResult:
    subject = subject_from_case(case)
    expected = case.get("expected")
    expected_norm = canonicalize(expected)
    actual_norm = canonicalize(actual)
    status = "match" if expected_norm == actual_norm else "mismatch"
    return BenchmarkResult(
        subject=subject,
        stage="golden_repros",
        status=status,
        reference=str(case.get("reference", "expected")),
        candidate=str(case.get("candidate", "fission")),
        mismatch_kind=None if status == "match" else str(case.get("mismatch_kind", "golden_repro")),
        expected=expected,
        actual=actual,
        metrics={"case_count": 1},
        error=None,
    )


@app.command()
def main(
    manifest: Path = typer.Argument(..., help="Golden repro manifest JSON"),
    output: Path = typer.Option(Path("results/golden_repros/latest.jsonl")),
    timeout: float = typer.Option(30.0),
):
    data = json.loads(manifest.read_text())
    rows: list[BenchmarkResult] = []
    for case in data.get("cases", []):
        subject = subject_from_case(case)
        try:
            actual = run_json_provider(str(case["command"]), subject, timeout)
            rows.append(compare_golden(case, actual))
        except Exception as exc:
            rows.append(
                BenchmarkResult(
                    subject=subject,
                    stage="golden_repros",
                    status="error",
                    reference=str(case.get("reference", "expected")),
                    candidate=str(case.get("candidate", "fission")),
                    error=str(exc),
                )
            )

    write_jsonl(output, rows)
    typer.echo(f"Wrote {len(rows)} golden repro rows to {output}")


if __name__ == "__main__":
    app()
