"""CFG parity runner."""
from __future__ import annotations

from pathlib import Path

import typer

from benchmark.common.io import write_jsonl
from benchmark.common.providers import canonicalize, run_json_provider
from benchmark.common.result import error_result
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject
from benchmark.common.subjects import load_subjects

app = typer.Typer(pretty_exceptions_enable=False)


def count_items(graph: object, key: str) -> int:
    if isinstance(graph, dict) and isinstance(graph.get(key), list):
        return len(graph[key])
    return 0


def compare_cfg(
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
            stage="cfg_parity",
            status="match",
            reference=reference_name,
            candidate=candidate_name,
            expected=expected,
            actual=actual,
            metrics={
                "block_count": count_items(expected, "blocks"),
                "edge_count": count_items(expected, "edges"),
            },
        )

    mismatch_kind = "cfg_shape"
    if count_items(expected, "blocks") != count_items(actual, "blocks"):
        mismatch_kind = "block_count"
    elif count_items(expected, "edges") != count_items(actual, "edges"):
        mismatch_kind = "edge_count"

    return BenchmarkResult(
        subject=subject,
        stage="cfg_parity",
        status="mismatch",
        reference=reference_name,
        candidate=candidate_name,
        mismatch_kind=mismatch_kind,
        expected=expected,
        actual=actual,
        metrics={
            "expected_block_count": count_items(expected, "blocks"),
            "actual_block_count": count_items(actual, "blocks"),
            "expected_edge_count": count_items(expected, "edges"),
            "actual_edge_count": count_items(actual, "edges"),
        },
    )


@app.command()
def main(
    reference_command: str = typer.Option(..., help="Command template producing reference JSON"),
    candidate_command: str = typer.Option(..., help="Command template producing candidate JSON"),
    reference_name: str = typer.Option("reference"),
    candidate_name: str = typer.Option("fission"),
    corpus: str = typer.Option("dev"),
    output: Path = typer.Option(Path("results/cfg_parity/latest.jsonl")),
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
            rows.append(compare_cfg(subject, reference_name, candidate_name, expected, actual))
        except Exception as exc:
            rows.append(error_result(subject, "cfg_parity", reference_name, candidate_name, str(exc)))

    write_jsonl(output, rows)
    typer.echo(f"Wrote {len(rows)} CFG parity rows to {output}")


if __name__ == "__main__":
    app()
