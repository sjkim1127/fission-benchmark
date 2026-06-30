"""
fission-benchmark runner
Sends decompile requests to all containers in parallel and collects results.

Usage:
  python runner/runner.py --corpus dev
  python runner/runner.py --corpus dev --limit 1 --decompilers fission,ghidra
  python runner/runner.py --use-holdout   # only for release evaluation
"""
from __future__ import annotations

import asyncio
import base64
import json
import sys
import time
from dataclasses import asdict
from pathlib import Path
from typing import Optional

import httpx
import typer

sys.path.insert(0, str(Path(__file__).parent))
from corpus import CORPUS_ROOT, Corpus
from scoring import (
    FunctionScore,
    assign_consensus_ranks,
    source_similarity,
    structural_score,
)
from report import generate_report

app = typer.Typer(pretty_exceptions_enable=False)

DECOMPILERS: dict[str, str] = {
    "fission":  "http://localhost:8000",
    "ghidra":   "http://localhost:8001",
    "retdec":   "http://localhost:8002",
    "radare2":  "http://localhost:8003",
}

RESULTS_DIR = Path(__file__).parent.parent / "results"
RESULTS_DIR.mkdir(exist_ok=True)


async def call_decompiler(
    client: httpx.AsyncClient,
    name: str,
    base_url: str,
    binary_path: Path,
    addr: str,
    timeout: float = 180.0,
) -> dict:
    binary_b64 = base64.b64encode(binary_path.read_bytes()).decode()
    try:
        resp = await client.post(
            f"{base_url}/decompile",
            json={"binary_b64": binary_b64, "addr": addr},
            timeout=timeout,
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"name": "?", "code": "", "time_ms": 0, "error": str(e), "decompiler": name}


async def run_all(
    functions: list,
    decompilers: dict[str, str],
    corpus_split: str,
    limit: int | None,
) -> list[FunctionScore]:
    scores: list[FunctionScore] = []

    fn_list = functions[:limit] if limit else functions

    async with httpx.AsyncClient() as client:
        for fn in fn_list:
            source_path = CORPUS_ROOT / corpus_split / fn.source
            source_code = source_path.read_text(errors="replace") if source_path.exists() else ""

            for variant in fn.compiler_variants:
                binary_path = CORPUS_ROOT / corpus_split / variant.binary
                if not binary_path.exists():
                    typer.echo(f"  [SKIP] binary not found: {binary_path}", err=True)
                    continue

                variant_label = f"{variant.compiler} {variant.opt}"
                typer.echo(f"▶ {fn.name} [{variant_label}]")

                # Parallel decompile requests
                # We need an addr per variant — stored in manifest (see corpus schema)
                addr = getattr(variant, "addr", "0x0")

                tasks = {
                    dname: call_decompiler(client, dname, url, binary_path, addr)
                    for dname, url in decompilers.items()
                }
                results = await asyncio.gather(*tasks.values())
                result_map = dict(zip(tasks.keys(), results))

                for dname, res in result_map.items():
                    code = res.get("code", "")
                    sim = source_similarity(source_code, code) if source_code else 0.0
                    gotos, depth = structural_score(code)
                    scores.append(FunctionScore(
                        decompiler=dname,
                        function_name=fn.name,
                        compiler_variant=variant_label,
                        source_similarity=sim,
                        goto_count=gotos,
                        nesting_depth=depth,
                        time_ms=res.get("time_ms", 0),
                        error=res.get("error"),
                    ))
                    status = "✓" if not res.get("error") else "✗"
                    typer.echo(f"  {status} {dname:10s} sim={sim:.3f} gotos={gotos} {res.get('time_ms',0)}ms")

    return assign_consensus_ranks(scores)


@app.command()
def main(
    corpus: str = typer.Option("dev", help="Corpus split to use: dev or holdout"),
    use_holdout: bool = typer.Option(False, "--use-holdout", help="Evaluate holdout set (release only)"),
    limit: Optional[int] = typer.Option(None, help="Limit number of functions"),
    decompilers: Optional[str] = typer.Option(None, help="Comma-separated list of decompilers"),
    output: Optional[Path] = typer.Option(None, help="Output JSON path"),
):
    if use_holdout:
        corpus = "holdout"
        typer.echo("⚠️  Running holdout evaluation — results are final", err=True)

    selected = DECOMPILERS
    if decompilers:
        selected = {k: v for k, v in DECOMPILERS.items() if k in decompilers.split(",")}
        typer.echo(f"Using decompilers: {list(selected)}")

    typer.echo(f"Loading corpus: {corpus}")
    c = Corpus.load_all(split=corpus)
    typer.echo(f"  {len(c.functions)} functions loaded")

    start = time.monotonic()
    scores = asyncio.run(run_all(c.functions, selected, corpus, limit))
    elapsed = time.monotonic() - start

    # Save raw JSON
    ts = time.strftime("%Y%m%d_%H%M%S")
    out_path = output or (RESULTS_DIR / f"{ts}.json")
    raw = [asdict(s) for s in scores]
    out_path.write_text(json.dumps(raw, indent=2))
    typer.echo(f"\n✅ Results saved to {out_path} ({elapsed:.1f}s)")

    # Save latest.json symlink
    (RESULTS_DIR / "latest.json").unlink(missing_ok=True)
    (RESULTS_DIR / "latest.json").write_text(json.dumps(raw, indent=2))

    # Generate report
    generate_report(scores, corpus_split=corpus)
    typer.echo("📊 Report generated: results/latest.md, docs/index.html")


if __name__ == "__main__":
    app()
