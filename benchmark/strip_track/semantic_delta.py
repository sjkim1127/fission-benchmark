"""Strip semantic Δ — compare unstripped vs stripped discovery recall.

Uses strip_from_dev.json + optional semantic scores from envelopes when present.
Primary metric: manifest_recall on strip PEs (already in strip_discovery) and a
Δ note vs unstripped function_discovery inventory when available.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

import typer

from benchmark.common.io import write_jsonl
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject

app = typer.Typer(pretty_exceptions_enable=False)
STAGE = "strip_semantic_delta"


@app.command()
def main(
    strip_jsonl: Path = typer.Option(Path("results/strip_discovery/latest.jsonl")),
    unstripped_jsonl: Path = typer.Option(Path("results/function_discovery/latest.jsonl")),
    output: Path = typer.Option(Path("results/strip_semantic_delta/latest.jsonl")),
    rebuild_strip: bool = typer.Option(
        False, help="Ignored flag kept for CLI stability; run strip_track first"
    ),
    limit: Optional[int] = typer.Option(None),
):
    _ = rebuild_strip, limit
    if not strip_jsonl.is_file():
        typer.echo(
            f"Missing {strip_jsonl}; run: python -m benchmark.strip_track.run",
            err=True,
        )
        raise typer.Exit(1)

    strip_rows = []
    if strip_jsonl.is_file():
        for line in strip_jsonl.read_text(encoding="utf-8").splitlines():
            if line.strip():
                strip_rows.append(json.loads(line))

    unstripped_recall = None
    if unstripped_jsonl.is_file():
        recalls = []
        for line in unstripped_jsonl.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            m = row.get("metrics") or {}
            if "presence_recall" in m:
                recalls.append(float(m["presence_recall"]))
            elif "manifest_recall" in m:
                recalls.append(float(m["manifest_recall"]))
        if recalls:
            unstripped_recall = sum(recalls) / len(recalls)

    out: list[BenchmarkResult] = []
    strip_recalls = []
    for row in strip_rows:
        subj_d = row.get("subject") or {}
        subj = BenchmarkSubject(
            binary=str(subj_d.get("binary") or ""),
            function=str(subj_d.get("function") or ""),
            addr=str(subj_d.get("addr") or "0x0"),
            arch=str(subj_d.get("arch") or "x86_64"),
            compiler=str(subj_d.get("compiler") or "unknown"),
            opt=str(subj_d.get("opt") or "strip"),
            corpus_split="realworld",
        )
        m = row.get("metrics") or {}
        recall = m.get("manifest_recall")
        if recall is not None:
            strip_recalls.append(float(recall))
        delta = None
        if recall is not None and unstripped_recall is not None:
            delta = round(float(recall) - unstripped_recall, 4)
        out.append(
            BenchmarkResult(
                subject=subj,
                stage=STAGE,  # type: ignore[arg-type]
                status=row.get("status") or "mismatch",  # type: ignore[arg-type]
                reference="ghidra",
                candidate="fission",
                mismatch_kind=row.get("mismatch_kind"),
                metrics={
                    "strip_manifest_recall": recall,
                    "unstripped_presence_recall_mean": unstripped_recall,
                    "discovery_delta": delta,
                    "strip": 1,
                },
                error=row.get("error"),
            )
        )

    # Aggregate footer
    if strip_recalls:
        mean_s = sum(strip_recalls) / len(strip_recalls)
        agg = BenchmarkSubject(
            binary="(aggregate)",
            function="(strip_delta)",
            addr="0x0",
            arch="na",
            compiler="na",
            opt="strip",
            corpus_split="realworld",
        )
        out.append(
            BenchmarkResult(
                subject=agg,
                stage=STAGE,  # type: ignore[arg-type]
                status="match",
                reference="ghidra",
                candidate="fission",
                metrics={
                    "strip_manifest_recall_mean": round(mean_s, 4),
                    "unstripped_presence_recall_mean": unstripped_recall,
                    "discovery_delta_mean": (
                        round(mean_s - unstripped_recall, 4)
                        if unstripped_recall is not None
                        else None
                    ),
                    "n_strip_bins": len(strip_recalls),
                },
            )
        )
        typer.echo(
            f"strip recall mean={mean_s:.3f} unstripped={unstripped_recall} "
            f"delta={None if unstripped_recall is None else mean_s - unstripped_recall}"
        )

    write_jsonl(output, out)
    typer.echo(f"Wrote {len(out)} strip_semantic_delta rows → {output}")


if __name__ == "__main__":
    app()
