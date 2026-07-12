"""Throughput / resource budget stage — wall times from adapter decompile.

Measures p50/p95 decompile latency per decompiler over a subject sample.
Does not rank correctness; extension product metric.
"""
from __future__ import annotations

import statistics
import time
from pathlib import Path
from typing import Optional

import requests
import typer

from benchmark.common.http_providers import (
    DEFAULT_PORTS,
    corpus_relative_binary,
    ensure_fission_port,
)
from benchmark.common.io import write_jsonl
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject
from benchmark.common.subjects import load_subjects

app = typer.Typer(pretty_exceptions_enable=False)
STAGE = "throughput"


def _percentile(sorted_vals: list[float], p: float) -> float:
    if not sorted_vals:
        return 0.0
    k = (len(sorted_vals) - 1) * p
    f = int(k)
    c = min(f + 1, len(sorted_vals) - 1)
    if f == c:
        return sorted_vals[f]
    return sorted_vals[f] + (sorted_vals[c] - sorted_vals[f]) * (k - f)


@app.command()
def main(
    decompilers: str = typer.Option("fission,ghidra"),
    corpus: str = typer.Option("dev"),
    output: Path = typer.Option(Path("results/throughput/latest.jsonl")),
    limit: Optional[int] = typer.Option(20),
    timeout: float = typer.Option(120.0),
):
    ensure_fission_port()
    subjects = load_subjects(corpus)
    if limit is not None:
        subjects = subjects[:limit]
    names = [d.strip() for d in decompilers.split(",") if d.strip()]
    host = "localhost"
    rows: list[BenchmarkResult] = []
    times: dict[str, list[float]] = {n: [] for n in names}

    for subject in subjects:
        binary = corpus_relative_binary(subject.binary, subject.corpus_split)
        for name in names:
            port = DEFAULT_PORTS.get(name, 8000)
            # Time a stable parity surface (disasm) present on all adapters.
            url = f"http://{host}:{port}/disasm"
            t0 = time.perf_counter()
            err = None
            status = "match"
            try:
                r = requests.get(
                    url,
                    params={"binary": binary, "addr": subject.addr},
                    timeout=timeout,
                )
                if not r.ok:
                    status = "error"
                    err = f"HTTP {r.status_code}: {r.text[:200]}"
            except Exception as exc:
                status = "error"
                err = str(exc)
            ms = (time.perf_counter() - t0) * 1000.0
            if status == "match":
                times[name].append(ms)
            rows.append(
                BenchmarkResult(
                    subject=subject,
                    stage=STAGE,  # type: ignore[arg-type]
                    status=status,  # type: ignore[arg-type]
                    reference="budget",
                    candidate=name,
                    metrics={"time_ms": round(ms, 2)},
                    error=err,
                )
            )

    # Summary row
    summary_subj = BenchmarkSubject(
        binary="(aggregate)",
        function="(throughput)",
        addr="0x0",
        arch="na",
        compiler="na",
        opt="na",
        corpus_split=corpus,
    )
    for name, vals in times.items():
        vals_sorted = sorted(vals)
        metrics = {
            "n": len(vals_sorted),
            "p50_ms": round(_percentile(vals_sorted, 0.5), 2) if vals_sorted else 0,
            "p95_ms": round(_percentile(vals_sorted, 0.95), 2) if vals_sorted else 0,
            "mean_ms": round(statistics.mean(vals_sorted), 2) if vals_sorted else 0,
            "max_ms": round(max(vals_sorted), 2) if vals_sorted else 0,
        }
        rows.append(
            BenchmarkResult(
                subject=summary_subj,
                stage=STAGE,  # type: ignore[arg-type]
                status="match" if vals_sorted else "error",  # type: ignore[arg-type]
                reference="budget",
                candidate=name,
                metrics=metrics,
                mismatch_kind=None if vals_sorted else "no_samples",
            )
        )
        typer.echo(f"{name}: n={metrics['n']} p50={metrics['p50_ms']}ms p95={metrics['p95_ms']}ms")

    write_jsonl(output, rows)
    typer.echo(f"Wrote {len(rows)} throughput rows → {output}")


if __name__ == "__main__":
    app()
