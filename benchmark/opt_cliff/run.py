"""Optimization cliff matrix — pivot semantic scores by compiler opt level.

Reads an official/local envelope (dev_latest.json) and emits JSONL heat-map rows
plus a summary JSON. Extension analysis, not a ranking gate.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

import typer

from benchmark.common.io import write_jsonl
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject

app = typer.Typer(pretty_exceptions_enable=False)
STAGE = "opt_cliff"

_OPT_RE = re.compile(r"(-O[0-3s]|O[0-3s])", re.I)


def _opt_bucket(variant: str) -> str:
    m = _OPT_RE.search(variant or "")
    if not m:
        return "unknown"
    text = m.group(1).upper().replace("-", "")
    return text if text.startswith("O") else f"O{text}"


@app.command()
def main(
    envelope: Path = typer.Option(Path("results/dev_latest.json")),
    output: Path = typer.Option(Path("results/opt_cliff/latest.jsonl")),
    summary_json: Path = typer.Option(Path("results/opt_cliff/summary.json")),
):
    raw = json.loads(envelope.read_text(encoding="utf-8"))
    rows_in = raw.get("rows") if isinstance(raw, dict) else raw
    if not isinstance(rows_in, list):
        raise typer.BadParameter("envelope has no rows list")

    # decompiler -> opt -> scores
    bucket: dict[str, dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    out_rows: list[BenchmarkResult] = []
    for r in rows_in:
        if not isinstance(r, dict) or r.get("error"):
            continue
        score = r.get("correctness_score")
        if score is None:
            score = r.get("semantic_score")
        if score is None:
            continue
        d = str(r.get("decompiler") or "?")
        opt = _opt_bucket(str(r.get("compiler_variant") or ""))
        bucket[d][opt].append(float(score))
        subj = BenchmarkSubject(
            binary=str(r.get("binary") or ""),
            function=str(r.get("function_name") or ""),
            addr="0x0",
            arch="na",
            compiler=str(r.get("compiler_variant") or "").split()[0] if r.get("compiler_variant") else "na",
            opt=opt,
            corpus_split="dev",
        )
        out_rows.append(
            BenchmarkResult(
                subject=subj,
                stage=STAGE,  # type: ignore[arg-type]
                status="match",
                reference="oracle",
                candidate=d,
                metrics={"correctness": float(score), "opt": opt},
            )
        )

    summary: dict = {"schema": "opt-cliff-v1", "by_decompiler": {}}
    for d, opts in sorted(bucket.items()):
        summary["by_decompiler"][d] = {}
        for opt, scores in sorted(opts.items()):
            mean = sum(scores) / len(scores) if scores else None
            summary["by_decompiler"][d][opt] = {
                "n": len(scores),
                "mean_correctness": round(mean, 4) if mean is not None else None,
            }
            typer.echo(f"{d:10s} {opt:6s} n={len(scores):3d} mean={mean:.3f}" if mean is not None else f"{d} {opt} empty")

    # Cliff: O0 - O2 drop when both present
    for d, opts in summary["by_decompiler"].items():
        o0 = (opts.get("O0") or {}).get("mean_correctness")
        o2 = (opts.get("O2") or {}).get("mean_correctness")
        if o0 is not None and o2 is not None:
            opts["O0_to_O2_drop"] = round(o0 - o2, 4)

    summary_json.parent.mkdir(parents=True, exist_ok=True)
    summary_json.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    write_jsonl(output, out_rows)
    typer.echo(f"Wrote opt cliff summary → {summary_json}")


if __name__ == "__main__":
    app()
