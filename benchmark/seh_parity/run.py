"""SEH / unwind parity — RUNTIME_FUNCTION coverage + flags."""
from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer

from benchmark.common.compare_guards import empty_pair_result
from benchmark.common.http_stage import run_http_pair_stage
from benchmark.common.pe_exceptions import function_unwind_info
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject

app = typer.Typer(pretty_exceptions_enable=False)
STAGE = "seh_parity"


def compare_seh(
    subject: BenchmarkSubject,
    reference_name: str,
    candidate_name: str,
    expected: object,
    actual: object,
) -> BenchmarkResult:
    guarded = empty_pair_result(
        subject, STAGE, reference_name, candidate_name, expected, actual  # type: ignore[arg-type]
    )
    if guarded is not None:
        return guarded
    if not isinstance(expected, dict) or not isinstance(actual, dict):
        return BenchmarkResult(
            subject=subject,
            stage=STAGE,  # type: ignore[arg-type]
            status="error",
            reference=reference_name,
            candidate=candidate_name,
            error="non-object seh payload",
        )

    # PE file is ground truth when available on disk
    pe_truth = None
    try:
        pe_path = subject.binary
        if not pe_path.startswith("/") and not Path(pe_path).is_file():
            # try relative
            cand = Path(pe_path)
            if not cand.is_file():
                cand = Path.cwd() / pe_path
            pe_path = str(cand)
        if Path(pe_path).is_file():
            pe_truth = function_unwind_info(pe_path, subject.addr)
    except Exception:
        pe_truth = None

    exp_uw = bool(expected.get("has_unwind"))
    act_uw = bool(actual.get("has_unwind"))
    if pe_truth and pe_truth.get("status") == "ok":
        truth_uw = bool(pe_truth.get("has_unwind"))
    else:
        truth_uw = exp_uw  # prefer reference

    metrics = {
        "ref_has_unwind": int(exp_uw),
        "cand_has_unwind": int(act_uw),
        "pe_has_unwind": int(truth_uw) if pe_truth else None,
        "ref_surface": str(expected.get("seh_surface") or ""),
        "cand_surface": str(actual.get("seh_surface") or ""),
        "ref_runtime_functions": int(
            expected.get("program_runtime_function_count")
            or expected.get("program_eh_symbol_count")
            or 0
        ),
        "cand_runtime_functions": int(
            actual.get("program_runtime_function_count")
            or actual.get("program_eh_symbol_count")
            or 0
        ),
    }

    # Primary: candidate agrees with PE truth (or reference) on has_unwind
    if act_uw == truth_uw:
        status = "match"
        kind = None
    else:
        status = "mismatch"
        kind = "unwind_coverage"

    return BenchmarkResult(
        subject=subject,
        stage=STAGE,  # type: ignore[arg-type]
        status=status,  # type: ignore[arg-type]
        reference=reference_name,
        candidate=candidate_name,
        mismatch_kind=kind,
        expected=expected,
        actual=actual,
        metrics=metrics,
    )


@app.command()
def main(
    reference_http: str = typer.Option("ghidra"),
    candidate_http: str = typer.Option("fission"),
    corpus: str = typer.Option("dev"),
    output: Path = typer.Option(Path("results/seh_parity/latest.jsonl")),
    limit: Optional[int] = typer.Option(None),
    timeout: float = typer.Option(90.0),
):
    run_http_pair_stage(
        stage=STAGE,
        compare=compare_seh,
        reference_http=reference_http,
        candidate_http=candidate_http,
        corpus=corpus,
        output=output,
        limit=limit,
        timeout=timeout,
    )


if __name__ == "__main__":
    app()
