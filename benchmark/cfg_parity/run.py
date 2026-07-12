"""CFG parity runner — default reference: Ghidra HTTP, candidate: Fission HTTP."""
from __future__ import annotations

from pathlib import Path
from typing import Any, Optional

import typer

from benchmark.common.compare_guards import empty_pair_result
from benchmark.common.parity_cli import run_pair_stage
from benchmark.common.providers import canonicalize_cfg
from benchmark.common.result import error_result  # noqa: F401 — re-export style
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject

app = typer.Typer(pretty_exceptions_enable=False)


def count_items(graph: object, key: str) -> int:
    if isinstance(graph, dict) and isinstance(graph.get(key), list):
        return len(graph[key])
    return 0


def _block_starts(graph: object) -> set[str]:
    if not isinstance(graph, dict):
        return set()
    out: set[str] = set()
    for b in graph.get("blocks") or []:
        if isinstance(b, dict) and b.get("start") is not None:
            out.add(str(b.get("start")))
    return out


def _block_spans(graph: object) -> set[tuple[str, str]]:
    if not isinstance(graph, dict):
        return set()
    out: set[tuple[str, str]] = set()
    for b in graph.get("blocks") or []:
        if isinstance(b, dict) and b.get("start") is not None:
            out.add((str(b.get("start")), str(b.get("end") or "")))
    return out


def _edge_pairs(graph: object, *, with_kind: bool) -> set[tuple]:
    if not isinstance(graph, dict):
        return set()
    out: set[tuple] = set()
    for e in graph.get("edges") or []:
        if not isinstance(e, dict):
            continue
        src, tgt = e.get("source"), e.get("target")
        if src is None or tgt is None:
            continue
        if with_kind:
            out.add((str(src), str(tgt), str(e.get("kind") or "")))
        else:
            out.add((str(src), str(tgt)))
    return out


def _jaccard(a: set, b: set) -> float:
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return round(inter / union, 4) if union else 0.0


def _cfg_dual_metrics(expected_norm: object, actual_norm: object) -> dict[str, Any]:
    """Connectivity-focused metrics (kind-agnostic edges + block spans)."""
    exp_starts = _block_starts(expected_norm)
    act_starts = _block_starts(actual_norm)
    exp_spans = _block_spans(expected_norm)
    act_spans = _block_spans(actual_norm)
    exp_edges = _edge_pairs(expected_norm, with_kind=False)
    act_edges = _edge_pairs(actual_norm, with_kind=False)
    exp_edges_k = _edge_pairs(expected_norm, with_kind=True)
    act_edges_k = _edge_pairs(actual_norm, with_kind=True)
    return {
        "block_start_jaccard": _jaccard(exp_starts, act_starts),
        "block_span_jaccard": _jaccard(exp_spans, act_spans),
        "edge_pair_jaccard": _jaccard(exp_edges, act_edges),
        "edge_kind_jaccard": _jaccard(exp_edges_k, act_edges_k),
        "ref_block_starts": len(exp_starts),
        "cand_block_starts": len(act_starts),
        "ref_edge_pairs": len(exp_edges),
        "cand_edge_pairs": len(act_edges),
        "shared_block_starts": len(exp_starts & act_starts),
        "shared_edge_pairs": len(exp_edges & act_edges),
    }


def compare_cfg(
    subject: BenchmarkSubject,
    reference_name: str,
    candidate_name: str,
    expected: object,
    actual: object,
) -> BenchmarkResult:
    guarded = empty_pair_result(
        subject, "cfg_parity", reference_name, candidate_name, expected, actual
    )
    if guarded is not None:
        return guarded
    expected_norm = canonicalize_cfg(expected)
    actual_norm = canonicalize_cfg(actual)
    dual = _cfg_dual_metrics(expected_norm, actual_norm)

    # Primary structural equality: block *entries* + kind-agnostic edges.
    # Block *end* addresses often differ by tool encoding (inclusive last-insn
    # vs terminal op) while topology is identical — do not fail primary match
    # on span-only diffs (reported in dual metrics).
    starts_eq = _block_starts(expected_norm) == _block_starts(actual_norm)
    edges_eq = _edge_pairs(expected_norm, with_kind=False) == _edge_pairs(
        actual_norm, with_kind=False
    )
    spans_eq = _block_spans(expected_norm) == _block_spans(actual_norm)

    if starts_eq and edges_eq:
        return BenchmarkResult(
            subject=subject,
            stage="cfg_parity",
            status="match",
            reference=reference_name,
            candidate=candidate_name,
            expected=expected,
            actual=actual,
            metrics={
                "block_count": count_items(expected_norm, "blocks"),
                "edge_count": count_items(expected_norm, "edges"),
                "span_encoding_diff": 0 if spans_eq else 1,
                "compare_policy": "starts_and_edge_pairs",
                **dual,
            },
        )

    if expected_norm == actual_norm:
        return BenchmarkResult(
            subject=subject,
            stage="cfg_parity",
            status="match",
            reference=reference_name,
            candidate=candidate_name,
            expected=expected,
            actual=actual,
            metrics={
                "block_count": count_items(expected_norm, "blocks"),
                "edge_count": count_items(expected_norm, "edges"),
                **dual,
            },
        )

    # Prefer structural diagnostics over raw kind noise.
    mismatch_kind = "cfg_shape"
    if count_items(expected_norm, "blocks") != count_items(actual_norm, "blocks"):
        mismatch_kind = "block_count"
    elif not starts_eq:
        mismatch_kind = "block_set"
    elif not edges_eq:
        mismatch_kind = "edge_connectivity"
    elif not spans_eq:
        mismatch_kind = "block_span"
    elif count_items(expected_norm, "edges") != count_items(actual_norm, "edges"):
        mismatch_kind = "edge_count"
    else:
        mismatch_kind = "edge_set"

    return BenchmarkResult(
        subject=subject,
        stage="cfg_parity",
        status="mismatch",
        reference=reference_name,
        candidate=candidate_name,
        mismatch_kind=mismatch_kind,
        expected=expected,
        actual=actual,
        metrics={
            "expected_block_count": count_items(expected_norm, "blocks"),
            "actual_block_count": count_items(actual_norm, "blocks"),
            "expected_edge_count": count_items(expected_norm, "edges"),
            "actual_edge_count": count_items(actual_norm, "edges"),
            **dual,
        },
    )


@app.command()
def main(
    reference_http: Optional[str] = typer.Option("ghidra", "--reference-http"),
    candidate_http: Optional[str] = typer.Option("fission", "--candidate-http"),
    reference_command: Optional[str] = typer.Option(None),
    candidate_command: Optional[str] = typer.Option(None),
    reference_name: str = typer.Option("ghidra"),
    candidate_name: str = typer.Option("fission"),
    corpus: str = typer.Option("dev"),
    output: Path = typer.Option(Path("results/cfg_parity/latest.jsonl")),
    limit: Optional[int] = typer.Option(None),
    timeout: float = typer.Option(60.0),
):
    """Compare basic blocks and edges. Defaults: Ghidra vs Fission over HTTP."""
    if reference_command:
        reference_http = None
    if candidate_command:
        candidate_http = None
    run_pair_stage(
        stage="cfg_parity",
        compare=compare_cfg,
        reference_http=reference_http,
        candidate_http=candidate_http,
        reference_command=reference_command,
        candidate_command=candidate_command,
        reference_name=reference_name,
        candidate_name=candidate_name,
        corpus=corpus,
        output=output,
        limit=limit,
        timeout=timeout,
    )


if __name__ == "__main__":
    app()
