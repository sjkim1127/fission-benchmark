"""ABI / calling-convention parity — Ghidra storage vs Fission recovered slots."""
from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer

from benchmark.common.http_providers import fetch_parity_json
from benchmark.common.io import write_jsonl
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject
from benchmark.common.subjects import load_subjects

app = typer.Typer(pretty_exceptions_enable=False)

STAGE = "abi_parity"


def _is_implemented(payload: object) -> bool:
    if not isinstance(payload, dict):
        return False
    if payload.get("status") in {"not_implemented", "unsupported", "empty", "error"}:
        return False
    params = payload.get("parameters")
    return isinstance(params, list)


# Common x64 / x86 register aliases for location equality.
_REG_ALIASES = {
    "ecx": "rcx",
    "edx": "rdx",
    "r8d": "r8",
    "r9d": "r9",
    "eax": "rax",
    "ebx": "rbx",
    "esi": "rsi",
    "edi": "rdi",
    "esp": "rsp",
    "ebp": "rbp",
}


def _norm_loc(loc: object) -> str:
    text = str(loc or "").strip().lower()
    text = text.replace("register:", "").replace("reg:", "")
    # Ghidra may emit RCX / rcx / RCX:0
    text = text.split(":")[-1]
    return _REG_ALIASES.get(text, text)


def _param_locations(payload: object) -> list[str]:
    if not isinstance(payload, dict):
        return []
    params = payload.get("parameters") or []
    if not isinstance(params, list):
        return []
    out = []
    for p in params:
        if isinstance(p, dict):
            out.append(_norm_loc(p.get("location")))
    return out


def compare_abi(
    subject: BenchmarkSubject,
    reference_name: str,
    candidate_name: str,
    expected: object,
    actual: object,
) -> BenchmarkResult:
    if not _is_implemented(expected) and not _is_implemented(actual):
        return BenchmarkResult(
            subject=subject,
            stage=STAGE,  # type: ignore[arg-type]
            status="skipped",
            reference=reference_name,
            candidate=candidate_name,
            mismatch_kind="abi_surface_pending",
            expected=expected,
            actual=actual,
            metrics={"abi_surface": "not_implemented"},
            error="ABI surface not implemented on adapters — stage not scored",
        )
    if not _is_implemented(expected):
        return BenchmarkResult(
            subject=subject,
            stage=STAGE,  # type: ignore[arg-type]
            status="reference_empty",
            reference=reference_name,
            candidate=candidate_name,
            expected=expected,
            actual=actual,
            error="Reference ABI empty/not_implemented",
        )
    if not _is_implemented(actual):
        return BenchmarkResult(
            subject=subject,
            stage=STAGE,  # type: ignore[arg-type]
            status="candidate_empty",
            reference=reference_name,
            candidate=candidate_name,
            expected=expected,
            actual=actual,
            error="Candidate ABI empty/not_implemented",
        )

    exp_locs = _param_locations(expected)
    act_locs = _param_locations(actual)
    exp_n = len(exp_locs)
    act_n = len(act_locs)
    # Compare prefix of min length for location sequence; also param counts.
    n = min(exp_n, act_n)
    loc_match = exp_locs[:n] == act_locs[:n] and exp_n == act_n
    count_match = exp_n == act_n

    if loc_match and count_match:
        status = "match"
        kind = None
    elif not count_match:
        status = "mismatch"
        kind = "abi_param_count"
    else:
        status = "mismatch"
        kind = "abi_locations"

    return BenchmarkResult(
        subject=subject,
        stage=STAGE,  # type: ignore[arg-type]
        status=status,
        reference=reference_name,
        candidate=candidate_name,
        mismatch_kind=kind,
        expected=expected,
        actual=actual,
        metrics={
            "ref_param_count": exp_n,
            "cand_param_count": act_n,
            "shared_prefix": n,
            "location_prefix_match": 1 if exp_locs[:n] == act_locs[:n] else 0,
        },
    )


@app.command()
def main(
    reference_http: str = typer.Option("ghidra"),
    candidate_http: str = typer.Option("fission"),
    corpus: str = typer.Option("dev"),
    output: Path = typer.Option(Path("results/abi_parity/latest.jsonl")),
    limit: Optional[int] = typer.Option(None),
    timeout: float = typer.Option(60.0),
):
    rows: list[BenchmarkResult] = []
    subjects = load_subjects(corpus)
    if limit is not None:
        subjects = subjects[:limit]
    for subject in subjects:
        try:
            try:
                exp = fetch_parity_json(reference_http, STAGE, subject, timeout=timeout)
            except Exception as exc:
                exp = {"status": "error", "error": str(exc), "parameters": []}
            try:
                act = fetch_parity_json(candidate_http, STAGE, subject, timeout=timeout)
            except Exception as exc:
                act = {"status": "error", "error": str(exc), "parameters": []}
            rows.append(compare_abi(subject, reference_http, candidate_http, exp, act))
        except Exception as exc:
            rows.append(
                BenchmarkResult(
                    subject=subject,
                    stage=STAGE,  # type: ignore[arg-type]
                    status="error",
                    reference=reference_http,
                    candidate=candidate_http,
                    error=str(exc),
                )
            )
    write_jsonl(output, rows)
    matched = sum(1 for r in rows if r.status == "match")
    skipped = sum(1 for r in rows if r.status == "skipped")
    typer.echo(
        f"Wrote {len(rows)} abi rows (match={matched}, skipped={skipped}) to {output}"
    )


if __name__ == "__main__":
    app()
