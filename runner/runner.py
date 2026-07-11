"""Benchmark runner to decompile and score binaries."""
import asyncio
import base64
from collections import Counter
import json
import os
import sys
import time
from dataclasses import asdict
from pathlib import Path
from typing import Optional, List

import httpx
import typer

sys.path.insert(0, str(Path(__file__).parent))
from corpus import CORPUS_ROOT, Corpus
from scoring import (
    FunctionScore,
    assign_consensus_ranks,
    check_uses_intrinsics,
    extract_function_source,
    source_similarity,
    structural_score,
)
from semantic import verify_semantic_correctness
from report import generate_report
from readability import analyze_readability, ast_structure_similarity, summarize_readability_proxy_score
from output_diagnostics import analyze_output_diagnostics, invalid_output_reason

app = typer.Typer(help="Fission decompiler benchmark runner.")

# Source-level goto/nesting counts keyed by function name.
# Populated from corpus manifest or precomputed via scripts/precompute_source_metrics.py.
SOURCE_GOTO_COUNTS: dict[str, int] = {}
SOURCE_NESTING_DEPTHS: dict[str, int] = {}


def filter_functions(functions: list, requested: str | None) -> list:
    """Select named functions while preserving corpus manifest order."""
    if not requested:
        return functions
    names = [name.strip() for name in requested.split(",") if name.strip()]
    if not names:
        raise ValueError("function filter is empty")
    requested_names = set(names)
    available_names = {fn.name for fn in functions}
    missing = sorted(requested_names - available_names)
    if missing:
        raise ValueError(f"unknown function(s): {', '.join(missing)}")
    return [fn for fn in functions if fn.name in requested_names]


def _load_source_metrics() -> None:
    """Load precomputed source-level structural metrics if available."""
    metrics_path = Path(__file__).parent.parent / "corpus" / "source_metrics.json"
    if metrics_path.exists():
        data = json.loads(metrics_path.read_text())
        SOURCE_GOTO_COUNTS.update(data.get("goto_counts", {}))
        SOURCE_NESTING_DEPTHS.update(data.get("nesting_depths", {}))


def configured_decompilers() -> dict[str, str]:
    """Get configured decompiler HTTP endpoints from environment.

    Each decompiler's endpoint can be overridden with the ``{NAME}_ENDPOINT``
    environment variable (e.g. ``GHIDRA_ENDPOINT=http://host:9001``).
    Setting any endpoint to ``skip`` (case-insensitive) excludes that
    decompiler from the run without requiring changes to ``--decompilers``.
    """
    # Automatically load .env if it exists in the workspace root
    env_path = Path(__file__).resolve().parents[1] / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, val = line.split("=", 1)
                val_str = val.strip().strip(chr(39) + chr(34))
                os.environ.setdefault(key.strip(), val_str)

    # Default local dev ports mapped in docker-compose.yml.
    # Each entry can be overridden by {NAME}_ENDPOINT environment variable.
    defaults = {
        "fission":   os.environ.get("FISSION_ENDPOINT",   "http://localhost:8000"),
        "ghidra":    os.environ.get("GHIDRA_ENDPOINT",    "http://localhost:8001"),
        "boomerang": os.environ.get("BOOMERANG_ENDPOINT", "http://localhost:8002"),
        "radare2":   os.environ.get("RADARE2_ENDPOINT",   "http://localhost:8003"),
        "angr":      os.environ.get("ANGR_ENDPOINT",      "http://localhost:8004"),
        "snowman":   os.environ.get("SNOWMAN_ENDPOINT",   "http://localhost:8005"),
        "revng":     os.environ.get("REVNG_ENDPOINT",     "http://localhost:8006"),
        "reko":      os.environ.get("REKO_ENDPOINT",      "http://localhost:8008"),
    }
    # Exclude any endpoint explicitly set to "skip".
    return {k: v for k, v in defaults.items() if v.lower() != "skip"}


async def decompile_batch_and_score(
    client: httpx.AsyncClient,
    dname: str,
    url: str,
    binary_path: Path,
    targets: List[tuple],  # list of (fn_object, variant_object, function_source)
    sem: asyncio.Semaphore,
) -> List[FunctionScore]:
    addresses = [t[1].addr for t in targets]

    try:
        binary_b64 = base64.b64encode(binary_path.read_bytes()).decode()
    except Exception as e:
        return [
            FunctionScore(
                decompiler=dname,
                function_name=t[0].name,
                compiler_variant=f"{t[1].compiler} {t[1].opt}",
                source_similarity=0.0,
                goto_count=0,
                nesting_depth=0,
                time_ms=0,
                error=f"Failed to read binary: {e}",
                semantic_error=f"Failed to read binary: {e}",
                fail_category="adapter_error",
            ) for t in targets
        ]

    # Post to batch endpoint under semaphore
    async with sem:
        try:
            resp = await client.post(
                f"{url}/decompile_batch",
                json={
                    "binary_b64": binary_b64,
                    "addresses": addresses,
                },
                timeout=300.0,
            )
            if resp.status_code != 200:
                raise Exception(f"HTTP status {resp.status_code}: {resp.text[:500]}")
            data = resp.json()
            batch_results = data.get("results", [])
        except Exception as e:
            return [
                FunctionScore(
                    decompiler=dname,
                    function_name=t[0].name,
                    compiler_variant=f"{t[1].compiler} {t[1].opt}",
                    source_similarity=0.0,
                    goto_count=0,
                    nesting_depth=0,
                    time_ms=0,
                    error=f"Batch decompile error: {e}",
                    semantic_error=f"Batch decompile error: {e}",
                    fail_category="adapter_error",
                ) for t in targets
            ]

    # Map batch results back
    results_by_addr = {item.get("addr"): item for item in batch_results}
    code_counts = Counter((item.get("code") or "").strip() for item in batch_results if (item.get("code") or "").strip())
    fn_scores = []

    for fn, variant, function_source in targets:
        variant_label = f"{variant.compiler} {variant.opt}"
        item = results_by_addr.get(variant.addr)

        if not item:
            fn_scores.append(FunctionScore(
                decompiler=dname,
                function_name=fn.name,
                compiler_variant=variant_label,
                source_similarity=0.0,
                goto_count=0,
                nesting_depth=0,
                time_ms=0,
                error="Address missing from batch result",
            ))
            continue

        code = item.get("code", "") or ""
        # Dual layers (Fission): semantic on NIR; readability prefers HIR.
        code_nir = (item.get("code_nir") or code or "")
        code_hir = (item.get("code_hir") or "")
        # Semantic / diagnostics always use NIR-faithful primary.
        semantic_code = code_nir or code
        # Readability surface: HIR when present and non-empty, else primary.
        readability_code = code_hir or semantic_code
        adapter_error = item.get("error")
        output_diagnostics = (
            analyze_output_diagnostics(fn.name, dname, semantic_code, expected_addr=variant.addr)
            if semantic_code
            else {}
        )
        output_error = invalid_output_reason(
            output_diagnostics,
            semantic_code,
            duplicate_count=code_counts.get((code or "").strip(), 0),
        ) if semantic_code else None
        error = adapter_error or output_error
        sim = (
            source_similarity(function_source, semantic_code)
            if function_source and not error
            else 0.0
        )
        gotos, depth = structural_score(semantic_code) if not error else (0, 0)
        uses_intrin = check_uses_intrinsics(semantic_code) if semantic_code else False
        # Primary readability metrics: prefer HIR for Fission dual printers.
        readability_metrics = (
            analyze_readability(readability_code, dname)
            if readability_code and not error
            else {}
        )
        readability_score = summarize_readability_proxy_score(readability_metrics)
        readability_metrics_hir = {}
        readability_score_hir = None
        if (
            not error
            and code_hir
            and code_nir
            and code_hir.strip() != code_nir.strip()
        ):
            # Explicit HIR pass when dual surfaces differ (evidence only; not ranking).
            readability_metrics_hir = analyze_readability(code_hir, dname)
            readability_score_hir = summarize_readability_proxy_score(readability_metrics_hir)
        ast_similarity = (
            ast_structure_similarity(function_source, semantic_code)
            if function_source and semantic_code and not error
            else {}
        )

        if not error:
            sem_score, sem_err, fail_cat, cases_passed, cases_total = verify_semantic_correctness(
                fn.name, semantic_code
            )
        else:
            sem_score, sem_err, fail_cat, cases_passed, cases_total = 0.0, error, "adapter_error", 0, 0

        fn_scores.append(FunctionScore(
            decompiler=dname,
            function_name=fn.name,
            compiler_variant=variant_label,
            source_similarity=sim,
            goto_count=gotos,
            nesting_depth=depth,
            time_ms=data.get("time_ms", 0) // len(targets),
            error=error,
            semantic_score=sem_score,
            semantic_error=sem_err,
            fail_category=fail_cat,
            cases_passed=cases_passed,
            cases_total=cases_total,
            uses_intrinsics=uses_intrin,
            decompiled_code=semantic_code[:8000] if semantic_code else "",
            decompiled_code_nir=code_nir[:8000] if code_nir else "",
            decompiled_code_hir=code_hir[:8000] if code_hir else "",
            pseudocode_layer=str(item.get("layer") or ""),
            readability_metrics=readability_metrics,
            readability_proxy_score=readability_score,
            readability_metrics_hir=readability_metrics_hir,
            readability_proxy_score_hir=readability_score_hir,
            ast_similarity=ast_similarity,
            output_diagnostics=output_diagnostics,
        ))

        # Direct feedback output
        status = "✓" if not error else "✗"
        cat_tag = f" [{fail_cat}]" if fail_cat else ""
        typer.echo(
            f"  {status} {dname:10s} {fn.name:15s} [{variant_label}] "
            f"sim={sim:.3f} sem={sem_score:.2f} ({cases_passed}/{cases_total} cases){cat_tag} gotos={gotos}"
        )

    return fn_scores


async def run_all(
    functions: list,
    decompilers: dict[str, str],
    corpus_split: str,
    limit: int | None,
    variant_limit: int | None,
) -> list[FunctionScore]:
    fn_list = functions[:limit] if limit else functions

    # 1. Group decompile requests by (decompiler, binary_path)
    groups = {}
    for fn in fn_list:
        source_path = CORPUS_ROOT / corpus_split / fn.source
        source_code = source_path.read_text(errors="replace") if source_path.exists() else ""
        function_source = extract_function_source(source_code, fn.name) or source_code

        variants = fn.compiler_variants[:variant_limit] if variant_limit else fn.compiler_variants
        for variant in variants:
            binary_path = CORPUS_ROOT / corpus_split / variant.binary
            if not binary_path.exists():
                continue

            for dname, url in decompilers.items():
                key = (dname, url, binary_path)
                if key not in groups:
                    groups[key] = []
                groups[key].append((fn, variant, function_source))

    # Concurrency limit based on CPU count
    concurrency = os.cpu_count() or 4
    sem = asyncio.Semaphore(concurrency)
    typer.echo(f"Starting batch benchmark run with concurrency limit of {concurrency} workers.")

    all_scores: list[FunctionScore] = []

    async with httpx.AsyncClient() as client:
        tasks = []
        for (dname, url, binary_path), targets in groups.items():
            tasks.append(
                decompile_batch_and_score(
                    client, dname, url, binary_path, targets, sem
                )
            )

        results = await asyncio.gather(*tasks)
        for r in results:
            all_scores.extend(r)

    return assign_consensus_ranks(
        all_scores,
        source_goto_counts=SOURCE_GOTO_COUNTS,
        source_nesting_depths=SOURCE_NESTING_DEPTHS,
    )


@app.command()
def run(
    corpus: str = typer.Option("dev", help="Corpus split name (dev, holdout, full)"),
    limit: Optional[int] = typer.Option(None, help="Limit number of functions analyzed"),
    variant_limit: Optional[int] = typer.Option(None, help="Limit compiler variants per function; 0 means all"),
    decompilers: Optional[str] = typer.Option(None, help="Comma-separated decompiler list"),
    function: Optional[str] = typer.Option(
        None,
        "--function",
        help="Comma-separated function names for focused regression runs",
    ),
    output: Optional[str] = typer.Option(None, help="Override output JSON path"),
    publish: bool = typer.Option(
        True,
        "--publish/--no-publish",
        help="Update results/latest.*, Markdown, and GitHub Pages output",
    ),
):
    """Run decompiler benchmark and generate report."""
    _load_source_metrics()
    start_time = time.monotonic()

    # Select decompilers
    all_dec = configured_decompilers()
    if decompilers:
        selected = [d.strip() for d in decompilers.split(",")]
        dec_map = {d: all_dec[d] for d in selected if d in all_dec}
    else:
        dec_map = all_dec

    typer.echo(f"Using decompilers: {list(dec_map.keys())}")

    # Load corpus using load_all
    c = Corpus.load_all(corpus)
    try:
        selected_functions = filter_functions(c.functions, function)
    except ValueError as exc:
        raise typer.BadParameter(str(exc), param_hint="--function") from exc
    typer.echo(f"Loading corpus: {corpus}")
    typer.echo(f"  {len(c.functions)} functions loaded")
    if function:
        typer.echo(
            "  focused functions: "
            + ", ".join(fn.name for fn in selected_functions)
        )
    if limit:
        typer.echo(f"  function limit: {limit}")
    if variant_limit:
        typer.echo(f"  variant limit per function: {variant_limit}")

    # Run event loop
    scores = asyncio.run(run_all(selected_functions, dec_map, corpus, limit, variant_limit))

    elapsed = time.monotonic() - start_time

    # Save JSON and generate report
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    results_dir = Path(__file__).parent.parent / "results"
    results_dir.mkdir(exist_ok=True)

    # Save definitive run results
    if output:
        json_path = Path(output)
    else:
        json_path = results_dir / f"{timestamp}.json"
    latest_json = results_dir / "latest.json"

    serialized = [asdict(s) for s in scores]
    json_path.write_text(json.dumps(serialized, indent=2), encoding="utf-8")
    if publish:
        latest_json.write_text(json.dumps(serialized, indent=2), encoding="utf-8")
        generate_report(scores, corpus_split=corpus)

    typer.echo(f"\n✅ Results saved to {json_path} ({elapsed:.1f}s)")
    if publish:
        typer.echo("📊 Report generated: results/latest.md, docs/index.html")
    else:
        typer.echo("Focused result only; results/latest.* and docs/index.html were not updated.")


if __name__ == "__main__":
    app()
