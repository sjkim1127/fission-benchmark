"""Aggregate layered benchmark JSONL telemetry."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

import typer

from benchmark.common.io import read_jsonl

app = typer.Typer(pretty_exceptions_enable=False)


def aggregate_rows(rows: list[dict]) -> dict:
    by_stage: Counter[str] = Counter()
    by_status: Counter[str] = Counter()
    by_mismatch_kind: Counter[str] = Counter()
    by_variant: Counter[str] = Counter()

    for row in rows:
        subject = row.get("subject", {})
        stage = row.get("stage", "unknown")
        status = row.get("status", "unknown")
        mismatch_kind = row.get("mismatch_kind") or "none"
        variant = f"{subject.get('compiler', '?')} {subject.get('opt', '?')}"

        by_stage[stage] += 1
        by_status[status] += 1
        by_mismatch_kind[mismatch_kind] += 1
        by_variant[variant] += 1

    return {
        "total_rows": len(rows),
        "by_stage": dict(sorted(by_stage.items())),
        "by_status": dict(sorted(by_status.items())),
        "by_mismatch_kind": dict(sorted(by_mismatch_kind.items())),
        "by_variant": dict(sorted(by_variant.items())),
    }


@app.command()
def main(
    inputs: list[Path] = typer.Argument(..., help="Input JSONL result files"),
    output: Path = typer.Option(Path("results/telemetry/latest.json")),
):
    rows: list[dict] = []
    for path in inputs:
        rows.extend(read_jsonl(path))

    summary = aggregate_rows(rows)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    typer.echo(f"Wrote telemetry summary for {len(rows)} rows to {output}")


if __name__ == "__main__":
    app()
