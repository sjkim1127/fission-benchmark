"""Instruction decode parity runner — default: Ghidra vs Fission over HTTP."""
from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer

from benchmark.common.compare_guards import empty_pair_result, guard_decode_stub
from benchmark.common.parity_cli import run_pair_stage
from benchmark.common.providers import canonicalize, canonicalize_assembly_list
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject

app = typer.Typer(pretty_exceptions_enable=False)


def decode_mismatch_kind(expected_norm: object, actual_norm: object) -> str:
    if not isinstance(expected_norm, list) or not isinstance(actual_norm, list):
        return "decode_shape"
    if len(expected_norm) != len(actual_norm):
        return "instruction_count"
    for exp_inst, act_inst in zip(expected_norm, actual_norm):
        if not isinstance(exp_inst, dict) or not isinstance(act_inst, dict):
            return "decode_shape"
        for field, kind in (
            ("length", "instruction_length"),
            ("prefixes", "prefixes"),
            ("modrm", "modrm"),
            ("sib", "sib"),
            ("displacement", "displacement"),
            ("immediate", "immediate"),
            ("bytes", "instruction_bytes"),
        ):
            if exp_inst.get(field) != act_inst.get(field):
                return kind
    return "decode_sequence"


def compare_decode(
    subject: BenchmarkSubject,
    reference_name: str,
    candidate_name: str,
    expected: object,
    actual: object,
) -> BenchmarkResult:
    guarded = empty_pair_result(
        subject, "decode_parity", reference_name, candidate_name, expected, actual
    )
    if guarded is not None:
        return guarded
    # Both adapters currently stub decode from disasm — do not score as quality.
    stub = guard_decode_stub(subject, reference_name, candidate_name, expected, actual)
    if stub is not None:
        return stub
    # Reuse assembly byte/mnemonic normalization then full field compare.
    expected_norm = canonicalize(canonicalize_assembly_list(expected))
    actual_norm = canonicalize(canonicalize_assembly_list(actual))
    if expected_norm == actual_norm:
        return BenchmarkResult(
            subject=subject,
            stage="decode_parity",
            status="match",
            reference=reference_name,
            candidate=candidate_name,
            expected=expected,
            actual=actual,
            metrics={"instruction_count": len(expected) if isinstance(expected, list) else 0},
        )

    return BenchmarkResult(
        subject=subject,
        stage="decode_parity",
        status="mismatch",
        reference=reference_name,
        candidate=candidate_name,
        mismatch_kind=decode_mismatch_kind(expected_norm, actual_norm),
        expected=expected,
        actual=actual,
        metrics={
            "expected_instruction_count": len(expected) if isinstance(expected, list) else 0,
            "actual_instruction_count": len(actual) if isinstance(actual, list) else 0,
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
    output: Path = typer.Option(Path("results/decode_parity/latest.jsonl")),
    limit: Optional[int] = typer.Option(None),
    timeout: float = typer.Option(60.0),
):
    if reference_command:
        reference_http = None
    if candidate_command:
        candidate_http = None
    run_pair_stage(
        stage="decode_parity",
        compare=compare_decode,
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
