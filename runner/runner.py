"""Benchmark runner to decompile and score binaries."""
import asyncio
import base64
from collections import Counter
import hashlib
import json
import os
import sys
import time
import uuid
from datetime import datetime, timezone
from dataclasses import asdict
from pathlib import Path
from typing import List

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
from semantic import verify_semantic_correctness_async
from differential_oracle import aggregate_oracle_evidence, verify_with_oracle
from readability import analyze_readability, ast_structure_similarity, summarize_readability_proxy_score
from output_diagnostics import analyze_output_diagnostics, invalid_output_reason
from run_validity import build_envelope
from test_wrappers import TEST_WRAPPERS
import subprocess

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


def format_semantic_score(score: float | None) -> str:
    """Format semantic evidence without treating an untestable row as failure."""
    return "n/a" if score is None else f"{score:.2f}"


def build_expected_cells(
    functions: list,
    decompiler_names: list[str],
    variant_limit: int | None,
) -> list[dict[str, str]]:
    """Build the exact matrix from the same function list passed to run_all."""
    cells = []
    for function in functions:
        variants = function.compiler_variants[:variant_limit] if variant_limit else function.compiler_variants
        for variant in variants:
            for decompiler in decompiler_names:
                cells.append({
                    "decompiler": decompiler,
                    "function_name": function.name,
                    "compiler_variant": f"{variant.compiler} {variant.opt}",
                })
    return cells


def fission_toolchain_metadata() -> dict[str, str]:
    """Return local/release Fission provenance exported by the adapter setup."""
    git_sha = os.environ.get("FISSION_GIT_SHA", "")
    version = (
        os.environ.get("FISSION_VERSION")
        or os.environ.get("FISSION_RELEASE_VERSION")
        or (f"local-{git_sha}" if git_sha else "unknown")
    )
    return {
        "fission_version": version,
        "fission_git_sha": git_sha,
        "fission_source": os.environ.get("FISSION_SOURCE", "unknown"),
        "fission_source_fingerprint": os.environ.get(
            "FISSION_SOURCE_FINGERPRINT", ""
        ),
    }


def _load_source_metrics() -> None:
    """Load precomputed source-level structural metrics if available."""
    metrics_path = Path(__file__).parent.parent / "corpus" / "source_metrics.json"
    if metrics_path.exists():
        data = json.loads(metrics_path.read_text())
        SOURCE_GOTO_COUNTS.update(data.get("goto_counts", {}))
        SOURCE_NESTING_DEPTHS.update(data.get("nesting_depths", {}))


# Module-level flag to ensure .env is only parsed once per process.
_ENV_LOADED = False


def configured_decompilers() -> dict[str, str]:
    """Get configured decompiler HTTP endpoints from environment.

    Each decompiler's endpoint can be overridden with the ``{NAME}_ENDPOINT``
    environment variable (e.g. ``GHIDRA_ENDPOINT=http://host:9001``).
    Setting any endpoint to ``skip`` (case-insensitive) excludes that
    decompiler from the run without requiring changes to ``--decompilers``.
    """
    global _ENV_LOADED
    if not _ENV_LOADED:
        # Load .env once if it exists in the workspace root.
        env_path = Path(__file__).resolve().parents[1] / ".env"
        if env_path.exists():
            for line in env_path.read_text().splitlines():
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    val_str = val.strip().strip(chr(39) + chr(34))
                    os.environ.setdefault(key.strip(), val_str)
        _ENV_LOADED = True

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
    oracle_endpoint: str | None,
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

        oracle_evidence = {}
        if not error and oracle_endpoint and fn.name in TEST_WRAPPERS:
            binary_bytes = binary_path.read_bytes()
            differential = await verify_with_oracle(
                client,
                oracle_endpoint,
                function_name=fn.name,
                reference_code=function_source,
                candidate_code=semantic_code,
                cases=TEST_WRAPPERS[fn.name],
                compiler_variant=variant_label,
                reference_binary_sha256=hashlib.sha256(binary_bytes).hexdigest(),
                # Always bind official oracle evidence to the corpus PE under test.
                reference_binary_b64=base64.b64encode(binary_bytes).decode("ascii"),
                function_addr=variant.addr,
            )
            sem_score = differential.score
            sem_err = differential.error
            fail_cat = differential.category
            cases_passed = differential.cases_passed
            cases_total = differential.cases_total
            oracle_evidence = differential.evidence or {}
        elif not error:
            sem_score, sem_err, fail_cat, cases_passed, cases_total = await verify_semantic_correctness_async(
                fn.name, semantic_code
            )
        else:
            sem_score, sem_err, fail_cat, cases_passed, cases_total = 0.0, error, "adapter_error", 0, 0

        # C-2: prefer per-item timing from adapter if provided, fall back to apportioned batch time.
        item_time_ms = item.get("time_ms")
        if item_time_ms is not None:
            fn_time_ms = int(item_time_ms)
        else:
            fn_time_ms = data.get("time_ms", 0) // max(len(targets), 1)

        fn_scores.append(FunctionScore(
            decompiler=dname,
            function_name=fn.name,
            compiler_variant=variant_label,
            source_similarity=sim,
            goto_count=gotos,
            nesting_depth=depth,
            time_ms=fn_time_ms,
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
            oracle_evidence=oracle_evidence,
        ))

        # Direct feedback output
        status = "✓" if not error else "✗"
        cat_tag = f" [{fail_cat}]" if fail_cat else ""
        sem_text = format_semantic_score(sem_score)
        typer.echo(
            f"  {status} {dname:10s} {fn.name:15s} [{variant_label}] "
            f"sim={sim:.3f} sem={sem_text} ({cases_passed}/{cases_total} cases){cat_tag} gotos={gotos}"
        )

    return fn_scores


async def run_all(
    functions: list,
    decompilers: dict[str, str],
    corpus_split: str,
    limit: int | None,
    variant_limit: int | None,
    oracle_endpoint: str | None,
) -> list[FunctionScore]:
    fn_list = functions  # [:limit] already applied by caller — do not slice again
    all_scores: list[FunctionScore] = []

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
                for dname in decompilers:
                    all_scores.append(FunctionScore(
                        decompiler=dname,
                        function_name=fn.name,
                        compiler_variant=f"{variant.compiler} {variant.opt}",
                        source_similarity=0.0,
                        goto_count=0,
                        nesting_depth=0,
                        time_ms=0,
                        error=f"Missing binary: {variant.binary}",
                        semantic_error=f"Missing binary: {variant.binary}",
                        fail_category="fixture_error",
                    ))
                continue

            for dname, url in decompilers.items():
                key = (dname, url, binary_path)
                if key not in groups:
                    groups[key] = []
                groups[key].append((fn, variant, function_source))

    concurrency = os.cpu_count() or 4
    sem = asyncio.Semaphore(concurrency)
    typer.echo(f"Starting batch benchmark run with concurrency limit of {concurrency} workers.")

    async with httpx.AsyncClient() as client:
        tasks = []
        for (dname, url, binary_path), targets in groups.items():
            tasks.append(
                decompile_batch_and_score(
                    client, dname, url, binary_path, targets, sem, oracle_endpoint
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
    corpus: str = typer.Option(
        "dev", "--corpus", help="Which corpus split to evaluate (e.g. dev, holdout)"
    ),
    limit: int | None = typer.Option(
        None, help="Limit number of functions evaluated (for testing)"
    ),
    variant_limit: int | None = typer.Option(
        None, help="Limit compiler variants evaluated per function (for testing)"
    ),
    function: str | None = typer.Option(
        None, help="Evaluate only a specific function by name"
    ),
    decompilers: str | None = typer.Option(
        None, help="Comma-separated list of decompilers to run"
    ),
    output: str | None = typer.Option(
        None, help="Path to save JSON output (defaults to results/TIMESTAMP.json)"
    ),
    run_mode: str = typer.Option(
        "smoke", help="Execution mode: smoke, local, or official"
    ),
) -> None:
    """Run benchmark evaluation pipeline."""
    started_at = datetime.now(timezone.utc)
    start_monotonic = time.monotonic()
    _load_source_metrics()

    if run_mode == "official" and any((limit, variant_limit, function)):
        raise typer.BadParameter(
            "official runs cannot use --limit, --variant-limit, or --function"
        )

    # Select decompilers
    all_dec = configured_decompilers()
    if decompilers:
        selected = [d.strip() for d in decompilers.split(",")]
        dec_map = {}
        for d in selected:
            if d not in all_dec:
                raise typer.BadParameter(f"Requested decompiler '{d}' is not configured or is skipped.")
            dec_map[d] = all_dec[d]
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

    fn_list = selected_functions[:limit] if limit else selected_functions
    expected_functions = len(fn_list)

    # Build exact expected_cells list (per function x variant x decompiler)
    # Avoids Cartesian product assumptions when functions have different variants.
    expected_cells = build_expected_cells(fn_list, list(dec_map), variant_limit)

    expected_rows = len(expected_cells)

    # Run event loop
    oracle_endpoint = os.environ.get("ORACLE_ENDPOINT")
    if run_mode == "official" and not oracle_endpoint:
        raise typer.BadParameter("official runs require ORACLE_ENDPOINT")
    scores = asyncio.run(
        run_all(fn_list, dec_map, corpus, limit, variant_limit, oracle_endpoint)
    )

    elapsed = time.monotonic() - start_monotonic
    finished_at = datetime.now(timezone.utc)

    # Save JSON and generate report
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    results_dir = Path(__file__).parent.parent / "results"
    results_dir.mkdir(exist_ok=True)

    # Save definitive run results
    if output:
        json_path = Path(output)
    else:
        json_path = results_dir / f"{timestamp}.json"
    serialized = [asdict(s) for s in scores]
    
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()
    except Exception:
        commit = "unknown"

    oracle = aggregate_oracle_evidence(serialized)
    manifest_hash = hashlib.sha256()
    manifest_paths = sorted((CORPUS_ROOT / corpus / "manifests").glob("*.json"))
    for manifest_path in manifest_paths:
        manifest_hash.update(manifest_path.name.encode("utf-8"))
        manifest_hash.update(manifest_path.read_bytes())

    envelope = build_envelope(
        serialized,
        run_meta={
            "run_id": str(uuid.uuid4()),
            "started_at": started_at.isoformat().replace("+00:00", "Z"),
            "finished_at": finished_at.isoformat().replace("+00:00", "Z"),
            "duration_ms": round(elapsed * 1000),
            "runner_commit": commit,
            "corpus": corpus,
            "corpus_manifest_sha256": manifest_hash.hexdigest(),
            "official": run_mode == "official",
            "requested_run_mode": run_mode,
            # Official publication requires profile=realistic with no focus limits.
            "profile": "realistic" if run_mode == "official" else "diagnostic",
            "limits": {
                "limit": limit,
                "variant_limit": variant_limit,
                "function": function
            }
        },
        toolchain={
            **fission_toolchain_metadata(),
            "runner_commit": commit,
            "runner_os": sys.platform,
            "python_version": sys.version.split()[0],
            "ci": os.environ.get("CI", "false"),
            "github_run_id": os.environ.get("GITHUB_RUN_ID", ""),
            "github_actor": os.environ.get("GITHUB_ACTOR", ""),
        },
        matrix={
            "expected_decompilers": list(dec_map.keys()),
            "expected_functions": expected_functions,
            "expected_rows": expected_rows,
            "expected_cells": expected_cells,
            "observed_rows": len(serialized),
        },
        oracle=oracle,
    )

    json_path.write_text(json.dumps(envelope, indent=2), encoding="utf-8")

    typer.echo(f"\n✅ Results saved to {json_path} ({elapsed:.1f}s)")
    typer.echo("Candidate result saved; publication requires runner/publication_gate.py.")


if __name__ == "__main__":
    app()
