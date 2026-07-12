"""Type recovery parity — tokens + struct field layout IoU vs Ghidra."""
from __future__ import annotations

from pathlib import Path
from typing import Any, Optional

import typer

from benchmark.common.compare_guards import empty_pair_result
from benchmark.common.http_stage import run_http_pair_stage
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject
from benchmark.common.set_compare import as_str_set, jaccard

app = typer.Typer(pretty_exceptions_enable=False)
STAGE = "type_parity"


def _type_tokens(payload: object) -> set[str]:
    if not isinstance(payload, dict):
        return set()
    if payload.get("status") in {"error", "not_implemented"}:
        return set()
    tokens: list[str] = []
    if payload.get("return_type"):
        tokens.append(f"ret:{str(payload.get('return_type')).lower()}")
    for p in payload.get("parameters") or []:
        if isinstance(p, dict) and p.get("type") is not None:
            tokens.append(f"p{p.get('index')}:{str(p.get('type')).lower()}")
    return as_str_set(tokens)


def _field_keys(payload: object) -> set[str]:
    """Canonical field keys: struct|offset|size (name optional soft match)."""
    if not isinstance(payload, dict):
        return set()
    out: set[str] = set()
    for st in payload.get("structs") or []:
        if not isinstance(st, dict):
            continue
        sname = str(st.get("name") or "struct").lower()
        for f in st.get("fields") or []:
            if not isinstance(f, dict):
                continue
            off = int(f.get("offset") or 0)
            size = int(f.get("size") or 0)
            fname = str(f.get("name") or "").lower()
            # Hard key: layout position; soft includes name for dual metric
            out.add(f"{sname}|{off}|{size}")
            if fname:
                out.add(f"{sname}|{off}|{size}|{fname}")
    return out


def _layout_keys_hard(payload: object) -> set[str]:
    if not isinstance(payload, dict):
        return set()
    out: set[str] = set()
    for st in payload.get("structs") or []:
        if not isinstance(st, dict):
            continue
        sname = str(st.get("name") or "struct").lower()
        for f in st.get("fields") or []:
            if not isinstance(f, dict):
                continue
            out.add(f"{sname}|{int(f.get('offset') or 0)}|{int(f.get('size') or 0)}")
    return out


def compare_types(
    subject: BenchmarkSubject,
    reference_name: str,
    candidate_name: str,
    expected: object,
    actual: object,
) -> BenchmarkResult:
    guarded = empty_pair_result(
        subject, STAGE, reference_name, candidate_name, expected, actual  # type: ignore[arg-type]
    )
    if guarded is not None:
        return guarded

    exp_tok = _type_tokens(expected)
    act_tok = _type_tokens(actual)
    exp_layout = _layout_keys_hard(expected)
    act_layout = _layout_keys_hard(actual)
    tok_j = jaccard(exp_tok, act_tok)
    layout_j = jaccard(exp_layout, act_layout) if (exp_layout or act_layout) else None

    metrics: dict[str, Any] = {
        "type_token_jaccard": tok_j,
        "field_layout_jaccard": layout_j if layout_j is not None else 1.0,
        "ref_structs": len((expected or {}).get("structs") or []) if isinstance(expected, dict) else 0,
        "cand_structs": len((actual or {}).get("structs") or []) if isinstance(actual, dict) else 0,
        "ref_fields": len(exp_layout),
        "cand_fields": len(act_layout),
        "shared_fields": len(exp_layout & act_layout),
        "layout_surface": (
            (expected or {}).get("layout_surface")
            if isinstance(expected, dict)
            else None
        ),
    }

    # Primary: if either side exposes structs, require layout jaccard == 1.0
    # (field offsets+sizes). Else fall back to type-token equality.
    if exp_layout or act_layout:
        if exp_layout == act_layout:
            status = "match"
            kind = None
        else:
            status = "mismatch"
            kind = "field_layout"
    else:
        if exp_tok == act_tok:
            status = "match"
            kind = None
        else:
            status = "mismatch"
            kind = "type_set"

    return BenchmarkResult(
        subject=subject,
        stage=STAGE,  # type: ignore[arg-type]
        status=status,  # type: ignore[arg-type]
        reference=reference_name,
        candidate=candidate_name,
        mismatch_kind=kind,
        expected=expected,
        actual=actual,
        metrics=metrics,
    )


@app.command()
def main(
    reference_http: str = typer.Option("ghidra"),
    candidate_http: str = typer.Option("fission"),
    corpus: str = typer.Option("dev"),
    output: Path = typer.Option(Path("results/type_parity/latest.jsonl")),
    limit: Optional[int] = typer.Option(None),
    timeout: float = typer.Option(90.0),
):
    run_http_pair_stage(
        stage=STAGE,
        compare=compare_types,
        reference_http=reference_http,
        candidate_http=candidate_http,
        corpus=corpus,
        output=output,
        limit=limit,
        timeout=timeout,
    )


if __name__ == "__main__":
    app()
