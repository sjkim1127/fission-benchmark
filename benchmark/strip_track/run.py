"""Strip-track discovery scaffold.

Fails closed (skipped) when no realworld/strip corpus is present — never invents
match rates from empty data.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

import typer

from benchmark.common.io import write_jsonl
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject

app = typer.Typer(pretty_exceptions_enable=False)

STAGE = "strip_discovery"
MANIFEST_DIR = Path("corpus/realworld/manifests")


def _load_manifest_subjects() -> list[BenchmarkSubject]:
    subjects: list[BenchmarkSubject] = []
    if not MANIFEST_DIR.is_dir():
        return subjects
    for path in sorted(MANIFEST_DIR.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        functions = data.get("functions") or data.get("subjects") or []
        binary = data.get("binary") or data.get("path") or ""
        if not binary or not isinstance(functions, list):
            continue
        for fn in functions:
            if not isinstance(fn, dict):
                continue
            subjects.append(
                BenchmarkSubject(
                    binary=str(binary),
                    function=str(fn.get("name") or fn.get("function") or "unknown"),
                    addr=str(fn.get("addr") or fn.get("address") or "0x0"),
                    arch=str(data.get("arch") or fn.get("arch") or "unknown"),
                    compiler=str(data.get("compiler") or "unknown"),
                    opt=str(data.get("opt") or "strip"),
                    corpus_split="realworld",
                )
            )
    return subjects


@app.command()
def main(
    output: Path = typer.Option(Path("results/strip_discovery/latest.jsonl")),
    limit: Optional[int] = typer.Option(None),
):
    subjects = _load_manifest_subjects()
    if limit is not None:
        subjects = subjects[:limit]
    rows: list[BenchmarkResult] = []
    if not subjects:
        # Single sentinel row — skipped, not match.
        dummy = BenchmarkSubject(
            binary="corpus/realworld/(none)",
            function="(no_strip_corpus)",
            addr="0x0",
            arch="unknown",
            compiler="unknown",
            opt="strip",
            corpus_split="realworld",
        )
        rows.append(
            BenchmarkResult(
                subject=dummy,
                stage=STAGE,  # type: ignore[arg-type]
                status="skipped",
                reference="ghidra",
                candidate="fission",
                mismatch_kind="strip_corpus_empty",
                metrics={"manifest_count": 0},
                error=(
                    "No realworld/strip manifests with subjects — track not activated"
                ),
            )
        )
    else:
        for subject in subjects:
            rows.append(
                BenchmarkResult(
                    subject=subject,
                    stage=STAGE,  # type: ignore[arg-type]
                    status="skipped",
                    reference="ghidra",
                    candidate="fission",
                    mismatch_kind="strip_runner_pending",
                    metrics={"note": "inventory compare not yet wired for strip PE"},
                    error="Strip discovery compare not yet implemented for populated corpus",
                )
            )
    write_jsonl(output, rows)
    typer.echo(f"Wrote {len(rows)} strip_discovery rows to {output}")


if __name__ == "__main__":
    app()
