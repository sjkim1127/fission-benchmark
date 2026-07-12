"""Call-graph parity — callee address sets vs Ghidra."""
from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer

from benchmark.common.http_stage import run_http_pair_stage
from benchmark.common.providers import normalize_address
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject
from benchmark.common.set_compare import compare_payload_sets

app = typer.Typer(pretty_exceptions_enable=False)
STAGE = "callgraph_parity"


def _callees(payload: object) -> set[str]:
    if not isinstance(payload, dict):
        return set()
    out: set[str] = set()
    for c in payload.get("callees") or []:
        try:
            out.add(normalize_address(str(c)))
        except Exception:
            text = str(c).strip().lower()
            if text:
                out.add(text)
    return out


def compare_callgraph(
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
        extract=_callees,
        mismatch_kind="callee_set",
    )


@app.command()
def main(
    reference_http: str = typer.Option("ghidra"),
    candidate_http: str = typer.Option("fission"),
    corpus: str = typer.Option("dev"),
    output: Path = typer.Option(Path("results/callgraph_parity/latest.jsonl")),
    limit: Optional[int] = typer.Option(None),
    timeout: float = typer.Option(90.0),
):
    run_http_pair_stage(
        stage=STAGE,
        compare=compare_callgraph,
        reference_http=reference_http,
        candidate_http=candidate_http,
        corpus=corpus,
        output=output,
        limit=limit,
        timeout=timeout,
    )


if __name__ == "__main__":
    app()
