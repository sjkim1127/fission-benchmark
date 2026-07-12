"""Type recovery parity — return/param types vs Ghidra."""
from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer

from benchmark.common.http_stage import run_http_pair_stage
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject
from benchmark.common.set_compare import as_str_set, compare_payload_sets

app = typer.Typer(pretty_exceptions_enable=False)
STAGE = "type_parity"


def _type_tokens(payload: object) -> set[str]:
    if not isinstance(payload, dict):
        return set()
    if payload.get("status") in {"error", "not_implemented"}:
        return set()
    tokens: list[str] = []
    if payload.get("return_type"):
        tokens.append(f"ret:{payload.get('return_type')}")
    for p in payload.get("parameters") or []:
        if isinstance(p, dict) and p.get("type") is not None:
            tokens.append(f"p{p.get('index')}:{p.get('type')}")
    return as_str_set(tokens)


def compare_types(
    subject: BenchmarkSubject,
    reference_name: str,
    candidate_name: str,
    expected: object,
    actual: object,
) -> BenchmarkResult:
    return compare_payload_sets(
        subject,
        STAGE,
        reference_name,
        candidate_name,
        expected,
        actual,
        extract=_type_tokens,
        mismatch_kind="type_set",
    )


@app.command()
def main(
    reference_http: str = typer.Option("ghidra"),
    candidate_http: str = typer.Option("fission"),
    corpus: str = typer.Option("dev"),
    output: Path = typer.Option(Path("results/type_parity/latest.jsonl")),
    limit: Optional[int] = typer.Option(None),
    timeout: float = typer.Option(90.0),
):
    run_http_pair_stage(
        stage=STAGE,
        compare=compare_types,
        reference_http=reference_http,
        candidate_http=candidate_http,
        corpus=corpus,
        output=output,
        limit=limit,
        timeout=timeout,
    )


if __name__ == "__main__":
    app()
