"""Function discovery parity runner."""
from __future__ import annotations

from pathlib import Path

import typer

from benchmark.common.binaries import load_binary_subjects
from benchmark.common.io import write_jsonl
from benchmark.common.providers import canonicalize, run_json_provider
from benchmark.common.result import error_result
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject

app = typer.Typer(pretty_exceptions_enable=False)


def function_addresses(functions: object) -> set[str]:
    if not isinstance(functions, list):
        return set()
    addresses: set[str] = set()
    for fn in functions:
        if isinstance(fn, dict) and fn.get("address") is not None:
            addresses.add(str(fn["address"]).lower())
    return addresses


def compare_functions(
    subject: BenchmarkSubject,
    reference_name: str,
    candidate_name: str,
    expected: object,
    actual: object,
) -> BenchmarkResult:
    expected_norm = canonicalize(expected)
    actual_norm = canonicalize(actual)
    expected_addrs = function_addresses(expected_norm)
    actual_addrs = function_addresses(actual_norm)

    if expected_norm == actual_norm:
        status = "match"
        mismatch_kind = None
    elif expected_addrs != actual_addrs:
        status = "mismatch"
        mismatch_kind = "function_set"
    else:
        status = "mismatch"
        mismatch_kind = "function_metadata"

    return BenchmarkResult(
        subject=subject,
        stage="function_discovery",
        status=status,
        reference=reference_name,
        candidate=candidate_name,
        mismatch_kind=mismatch_kind,
        expected=expected,
        actual=actual,
        metrics={
            "expected_function_count": len(expected_addrs),
            "actual_function_count": len(actual_addrs),
            "missing_function_count": len(expected_addrs - actual_addrs),
            "extra_function_count": len(actual_addrs - expected_addrs),
        },
    )


@app.command()
def main(
    reference_command: str = typer.Option(..., help="Command template producing reference JSON"),
    candidate_command: str = typer.Option(..., help="Command template producing candidate JSON"),
    reference_name: str = typer.Option("reference"),
    candidate_name: str = typer.Option("fission"),
    corpus: str = typer.Option("dev"),
    output: Path = typer.Option(Path("results/function_discovery/latest.jsonl")),
    limit: int | None = typer.Option(None),
    timeout: float = typer.Option(60.0),
):
    rows: list[BenchmarkResult] = []
    subjects = load_binary_subjects(corpus)
    if limit is not None:
        subjects = subjects[:limit]

    for subject in subjects:
        try:
            expected = run_json_provider(reference_command, subject, timeout)
            actual = run_json_provider(candidate_command, subject, timeout)
            rows.append(compare_functions(subject, reference_name, candidate_name, expected, actual))
        except Exception as exc:
            rows.append(
                error_result(subject, "function_discovery", reference_name, candidate_name, str(exc))
            )

    write_jsonl(output, rows)
    typer.echo(f"Wrote {len(rows)} function discovery rows to {output}")


if __name__ == "__main__":
    app()
