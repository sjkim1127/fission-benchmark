"""CFG parity runner — default reference: Ghidra HTTP, candidate: Fission HTTP."""
from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer

from benchmark.common.compare_guards import empty_pair_result
from benchmark.common.parity_cli import run_pair_stage
from benchmark.common.providers import canonicalize_cfg
from benchmark.common.result import error_result  # noqa: F401 — re-export style
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject

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
    guarded = empty_pair_result(
        subject, "cfg_parity", reference_name, candidate_name, expected, actual
    )
    if guarded is not None:
        return guarded
    expected_norm = canonicalize_cfg(expected)
    actual_norm = canonicalize_cfg(actual)
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
                "block_count": count_items(expected_norm, "blocks"),
                "edge_count": count_items(expected_norm, "edges"),
            },
        )

    mismatch_kind = "cfg_shape"
    if count_items(expected_norm, "blocks") != count_items(actual_norm, "blocks"):
        mismatch_kind = "block_count"
    elif count_items(expected_norm, "edges") != count_items(actual_norm, "edges"):
        mismatch_kind = "edge_count"
    else:
        # Same counts but different connectivity / block spans.
        exp_starts = {
            b.get("start")
            for b in (expected_norm.get("blocks") or [])
            if isinstance(b, dict)
        }
        act_starts = {
            b.get("start")
            for b in (actual_norm.get("blocks") or [])
            if isinstance(b, dict)
        }
        if exp_starts != act_starts:
            mismatch_kind = "block_set"
        else:
            mismatch_kind = "edge_set"

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
            "expected_block_count": count_items(expected_norm, "blocks"),
            "actual_block_count": count_items(actual_norm, "blocks"),
            "expected_edge_count": count_items(expected_norm, "edges"),
            "actual_edge_count": count_items(actual_norm, "edges"),
        },
    )


@app.command()
def main(
    reference_http: Optional[str] = typer.Option("ghidra", "--reference-http"),
    candidate_http: Optional[str] = typer.Option("fission", "--candidate-http"),
    reference_command: Optional[str] = typer.Option(None),
    candidate_command: Optional[str] = typer.Option(None),
    reference_name: str = typer.Option("ghidra"),
    candidate_name: str = typer.Option("fission"),
    corpus: str = typer.Option("dev"),
    output: Path = typer.Option(Path("results/cfg_parity/latest.jsonl")),
    limit: Optional[int] = typer.Option(None),
    timeout: float = typer.Option(60.0),
):
    """Compare basic blocks and edges. Defaults: Ghidra vs Fission over HTTP."""
    if reference_command:
        reference_http = None
    if candidate_command:
        candidate_http = None
    run_pair_stage(
        stage="cfg_parity",
        compare=compare_cfg,
        reference_http=reference_http,
        candidate_http=candidate_http,
        reference_command=reference_command,
        candidate_command=candidate_command,
        reference_name=reference_name,
        candidate_name=candidate_name,
        corpus=corpus,
        output=output,
        limit=limit,
        timeout=timeout,
    )


if __name__ == "__main__":
    app()
