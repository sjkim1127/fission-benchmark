"""Raw p-code parity runner — default reference: Ghidra HTTP, candidate: Fission HTTP."""
from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer

from benchmark.common.compare_guards import empty_pair_result
from benchmark.common.parity_cli import run_pair_stage
from benchmark.common.providers import canonicalize_pcode
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject

app = typer.Typer(pretty_exceptions_enable=False)


def compare_pcode(
    subject: BenchmarkSubject,
    reference_name: str,
    candidate_name: str,
    expected: object,
    actual: object,
) -> BenchmarkResult:
    guarded = empty_pair_result(
        subject, "pcode_parity", reference_name, candidate_name, expected, actual
    )
    if guarded is not None:
        return guarded
    expected_norm = canonicalize_pcode(expected)
    actual_norm = canonicalize_pcode(actual)
    if expected_norm == actual_norm:
        return BenchmarkResult(
            subject=subject,
            stage="pcode_parity",
            status="match",
            reference=reference_name,
            candidate=candidate_name,
            expected=expected,
            actual=actual,
            metrics={"op_count": len(expected) if isinstance(expected, list) else 0},
        )

    mismatch_kind = "op_sequence"
    if isinstance(expected_norm, list) and isinstance(actual_norm, list):
        if len(expected_norm) != len(actual_norm):
            mismatch_kind = "op_count"
        else:
            kind_diff = False
            varnode_diff = False
            for exp_op, act_op in zip(expected_norm, actual_norm):
                if not isinstance(exp_op, dict) or not isinstance(act_op, dict):
                    continue
                if exp_op.get("op") != act_op.get("op"):
                    kind_diff = True
                    break
                if exp_op.get("inputs") != act_op.get("inputs") or exp_op.get(
                    "output"
                ) != act_op.get("output"):
                    varnode_diff = True
            if kind_diff:
                mismatch_kind = "op_kind"
            elif varnode_diff:
                mismatch_kind = "varnode"

    return BenchmarkResult(
        subject=subject,
        stage="pcode_parity",
        status="mismatch",
        reference=reference_name,
        candidate=candidate_name,
        mismatch_kind=mismatch_kind,
        expected=expected,
        actual=actual,
        metrics={
            "expected_op_count": len(expected) if isinstance(expected, list) else 0,
            "actual_op_count": len(actual) if isinstance(actual, list) else 0,
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
    output: Path = typer.Option(Path("results/pcode_parity/latest.jsonl")),
    limit: Optional[int] = typer.Option(None),
    timeout: float = typer.Option(60.0),
):
    """Compare raw p-code op sequences. Defaults: Ghidra vs Fission over HTTP."""
    if reference_command:
        reference_http = None
    if candidate_command:
        candidate_http = None
    run_pair_stage(
        stage="pcode_parity",
        compare=compare_pcode,
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
