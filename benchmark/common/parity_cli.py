"""Shared Typer options for parity stage CLIs with HTTP defaults."""
from __future__ import annotations

from pathlib import Path
from typing import Any, Callable

import typer

from benchmark.common.http_providers import fetch_parity_json
from benchmark.common.io import write_jsonl
from benchmark.common.providers import run_json_provider
from benchmark.common.result import error_result
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject
from benchmark.common.subjects import load_subjects


ProviderFn = Callable[[BenchmarkSubject, float], Any]
CompareFn = Callable[[BenchmarkSubject, str, str, Any, Any], BenchmarkResult]


def load_provider(
    *,
    stage: str,
    http_tool: str | None,
    command: str | None,
    label: str,
) -> tuple[str, ProviderFn]:
    if http_tool:
        name = http_tool

        def _http(subject: BenchmarkSubject, timeout: float) -> Any:
            return fetch_parity_json(http_tool, stage, subject, timeout=timeout)

        return name, _http
    if command:
        name = label

        def _cmd(subject: BenchmarkSubject, timeout: float) -> Any:
            return run_json_provider(command, subject, timeout)

        return name, _cmd
    raise typer.BadParameter("provide either --*-http or --*-command")


def run_pair_stage(
    *,
    stage: str,
    compare: CompareFn,
    reference_http: str | None,
    candidate_http: str | None,
    reference_command: str | None,
    candidate_command: str | None,
    reference_name: str,
    candidate_name: str,
    corpus: str,
    output: Path,
    limit: int | None,
    timeout: float,
) -> None:
    """Execute reference vs candidate for each corpus subject and write JSONL."""
    if not reference_http and not reference_command:
        reference_http = "ghidra"
    if not candidate_http and not candidate_command:
        candidate_http = "fission"

    ref_label, ref_provider = load_provider(
        stage=stage,
        http_tool=reference_http,
        command=reference_command,
        label=reference_name,
    )
    cand_label, cand_provider = load_provider(
        stage=stage,
        http_tool=candidate_http,
        command=candidate_command,
        label=candidate_name,
    )

    rows: list[BenchmarkResult] = []
    subjects = load_subjects(corpus)
    if limit is not None:
        subjects = subjects[:limit]

    for subject in subjects:
        try:
            expected = ref_provider(subject, timeout)
            actual = cand_provider(subject, timeout)
            rows.append(compare(subject, ref_label, cand_label, expected, actual))
        except Exception as exc:
            rows.append(error_result(subject, stage, ref_label, cand_label, str(exc)))  # type: ignore[arg-type]

    write_jsonl(output, rows)
    typer.echo(f"Wrote {len(rows)} {stage} rows to {output} (ref={ref_label}, cand={cand_label})")
