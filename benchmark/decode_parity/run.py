"""Instruction decode parity runner."""
from __future__ import annotations

from pathlib import Path

import typer

from benchmark.common.io import write_jsonl
from benchmark.common.providers import canonicalize, run_json_provider
from benchmark.common.result import error_result
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject
from benchmark.common.subjects import load_subjects

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
    expected_norm = canonicalize(expected)
    actual_norm = canonicalize(actual)
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
    reference_command: str = typer.Option(..., help="Command template producing reference JSON"),
    candidate_command: str = typer.Option(..., help="Command template producing candidate JSON"),
    reference_name: str = typer.Option("reference"),
    candidate_name: str = typer.Option("fission"),
    corpus: str = typer.Option("dev"),
    output: Path = typer.Option(Path("results/decode_parity/latest.jsonl")),
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
            rows.append(compare_decode(subject, reference_name, candidate_name, expected, actual))
        except Exception as exc:
            rows.append(error_result(subject, "decode_parity", reference_name, candidate_name, str(exc)))

    write_jsonl(output, rows)
    typer.echo(f"Wrote {len(rows)} decode parity rows to {output}")


if __name__ == "__main__":
    app()
