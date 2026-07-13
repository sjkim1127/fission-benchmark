"""Assembly parity runner — default reference: Ghidra HTTP, candidate: Fission HTTP."""
from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer

from benchmark.common.compare_guards import empty_pair_result
from benchmark.common.parity_cli import run_pair_stage
from benchmark.common.providers import canonicalize_assembly_list
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject

app = typer.Typer(pretty_exceptions_enable=False)


def compare_assembly(
    subject: BenchmarkSubject,
    reference_name: str,
    candidate_name: str,
    expected: object,
    actual: object,
) -> BenchmarkResult:
    guarded = empty_pair_result(
        subject, "assembly_parity", reference_name, candidate_name, expected, actual
    )
    if guarded is not None:
        return guarded
    expected_norm = canonicalize_assembly_list(expected)
    actual_norm = canonicalize_assembly_list(actual)
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

    # BUG-07 fix: sort both lists by address before comparison.
    # Both adapters should return instructions in address order but network or
    # implementation quirks can occasionally produce a different ordering.
    # Address-sorted comparison is canonical for instruction-set parity.
    def _addr_key(inst: object) -> str:
        if not isinstance(inst, dict):
            return ""
        addr = inst.get("address") or ""
        try:
            return f"{int(str(addr), 16):016x}"
        except (ValueError, TypeError):
            return str(addr)

    mismatch_kind = "instruction_sequence"
    if isinstance(expected_norm, list) and isinstance(actual_norm, list):
        expected_sorted = sorted(expected_norm, key=_addr_key)
        actual_sorted = sorted(actual_norm, key=_addr_key)
        if len(expected_sorted) != len(actual_sorted):
            mismatch_kind = "instruction_count"
        else:
            for exp, act in zip(expected_sorted, actual_sorted):
                if not isinstance(exp, dict) or not isinstance(act, dict):
                    continue
                if exp.get("bytes") != act.get("bytes"):
                    mismatch_kind = "instruction_bytes"
                    break
                if exp.get("mnemonic") != act.get("mnemonic"):
                    mismatch_kind = "mnemonic"
                    break
                if exp.get("address") != act.get("address"):
                    mismatch_kind = "address"
                    break

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
    reference_http: Optional[str] = typer.Option(
        "ghidra", "--reference-http", help="Reference decompiler HTTP adapter (default: ghidra)"
    ),
    candidate_http: Optional[str] = typer.Option(
        "fission", "--candidate-http", help="Candidate decompiler HTTP adapter (default: fission)"
    ),
    reference_command: Optional[str] = typer.Option(
        None, help="Optional command template producing reference JSON (overrides --reference-http)"
    ),
    candidate_command: Optional[str] = typer.Option(
        None, help="Optional command template producing candidate JSON (overrides --candidate-http)"
    ),
    reference_name: str = typer.Option("ghidra"),
    candidate_name: str = typer.Option("fission"),
    corpus: str = typer.Option("dev"),
    output: Path = typer.Option(Path("results/assembly_parity/latest.jsonl")),
    limit: Optional[int] = typer.Option(None),
    timeout: float = typer.Option(60.0),
):
    """Compare instruction listings. Defaults: Ghidra vs Fission over Docker HTTP APIs."""
    if reference_command:
        reference_http = None
    if candidate_command:
        candidate_http = None
    run_pair_stage(
        stage="assembly_parity",
        compare=compare_assembly,
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
