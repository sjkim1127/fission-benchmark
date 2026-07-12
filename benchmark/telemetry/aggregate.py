"""Aggregate layered benchmark JSONL telemetry."""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

import typer

import os

from benchmark.common.io import read_jsonl

app = typer.Typer(pretty_exceptions_enable=False)

STAGE_ORDER = (
    "assembly_parity",
    "decode_parity",
    "pcode_parity",
    "cfg_parity",
    "function_discovery",
    "ir_invariants",
    "golden_repros",
)

# Stages excluded from publishable primary rates until a real surface exists.
NON_PUBLISHABLE_STAGES = frozenset({"decode_parity"})


def aggregate_rows(rows: list[dict]) -> dict:
    by_stage: Counter[str] = Counter()
    by_status: Counter[str] = Counter()
    by_mismatch_kind: Counter[str] = Counter()
    by_variant: Counter[str] = Counter()
    # stage -> status -> count
    stage_status: dict[str, Counter[str]] = defaultdict(Counter)
    stage_mismatch: dict[str, Counter[str]] = defaultdict(Counter)
    pair_counts: Counter[str] = Counter()

    for row in rows:
        subject = row.get("subject", {}) or {}
        stage = str(row.get("stage", "unknown"))
        status = str(row.get("status", "unknown"))
        mismatch_kind = row.get("mismatch_kind") or "none"
        variant = f"{subject.get('compiler', '?')} {subject.get('opt', '?')}"
        pair = f"{row.get('reference', '?')}→{row.get('candidate', '?')}"

        by_stage[stage] += 1
        by_status[status] += 1
        by_mismatch_kind[str(mismatch_kind)] += 1
        by_variant[variant] += 1
        stage_status[stage][status] += 1
        if status == "mismatch":
            stage_mismatch[stage][str(mismatch_kind)] += 1
        pair_counts[pair] += 1

    stages_detail = {}
    for stage in sorted(set(list(STAGE_ORDER) + list(by_stage.keys())), key=lambda s: (STAGE_ORDER.index(s) if s in STAGE_ORDER else 99, s)):
        if stage not in by_stage:
            continue
        statuses = dict(stage_status[stage])
        total = by_stage[stage]
        match = statuses.get("match", 0)
        mismatch = statuses.get("mismatch", 0)
        skipped = statuses.get("skipped", 0)
        fetch_error = statuses.get("fetch_error", 0)
        both_empty = statuses.get("both_empty_invalid", 0)
        ref_empty = statuses.get("reference_empty", 0)
        cand_empty = statuses.get("candidate_empty", 0)
        errorish = total - match - mismatch
        comparable = match + mismatch
        # Reliability: coverage of attempts that produced a quality signal.
        usable_coverage = round(comparable / total, 4) if total else None
        # Does NOT drop infra failures — lower when adapters fail.
        match_rate_attempted = round(match / total, 4) if total else None
        stages_detail[stage] = {
            "total": total,
            "match": match,
            "mismatch": mismatch,
            "skipped": skipped,
            "fetch_error": fetch_error,
            "both_empty_invalid": both_empty,
            "reference_empty": ref_empty,
            "candidate_empty": cand_empty,
            "error_or_other": errorish,
            # Historical name: among scored (match|mismatch) only.
            "match_rate": round(match / comparable, 4) if comparable else None,
            "mismatch_rate": round(mismatch / comparable, 4) if comparable else None,
            "match_rate_comparable": round(match / comparable, 4) if comparable else None,
            "match_rate_attempted": match_rate_attempted,
            "usable_coverage": usable_coverage,
            "by_status": dict(sorted(statuses.items())),
            "by_mismatch_kind": dict(sorted(stage_mismatch[stage].items())),
        }

    # Run-level reliability rollup (excludes skipped-only stages from quality).
    total_rows = len(rows)
    total_match = by_status.get("match", 0)
    total_mismatch = by_status.get("mismatch", 0)
    total_comparable = total_match + total_mismatch
    total_fetch = by_status.get("fetch_error", 0)
    reliability = {
        "usable_coverage": round(total_comparable / total_rows, 4) if total_rows else None,
        "match_rate_comparable": (
            round(total_match / total_comparable, 4) if total_comparable else None
        ),
        "match_rate_attempted": round(total_match / total_rows, 4) if total_rows else None,
        "fetch_error_rate": round(total_fetch / total_rows, 4) if total_rows else None,
        "skipped_rate": (
            round(by_status.get("skipped", 0) / total_rows, 4) if total_rows else None
        ),
    }

    # Publishable view: drop stub/non-primary stages (e.g. decode until real).
    publishable_stages = {
        k: v for k, v in stages_detail.items() if k not in NON_PUBLISHABLE_STAGES
    }
    pub_match = sum(int(v.get("match") or 0) for v in publishable_stages.values())
    pub_mismatch = sum(int(v.get("mismatch") or 0) for v in publishable_stages.values())
    pub_total = sum(int(v.get("total") or 0) for v in publishable_stages.values())
    pub_comparable = pub_match + pub_mismatch
    canonicalize_mode = (
        (os.environ.get("PARITY_CANONICALIZE_MODE") or "loose").strip().lower()
    )
    if canonicalize_mode not in {"loose", "strict"}:
        canonicalize_mode = "loose"

    return {
        "schema": "parity-telemetry-v2",
        "total_rows": total_rows,
        "by_stage": dict(sorted(by_stage.items())),
        "by_status": dict(sorted(by_status.items())),
        "by_mismatch_kind": dict(sorted(by_mismatch_kind.items())),
        "by_variant": dict(sorted(by_variant.items())),
        "by_pair": dict(sorted(pair_counts.items())),
        "stages": stages_detail,
        "reliability": reliability,
        "canonicalize_mode": canonicalize_mode,
        "non_publishable_stages": sorted(NON_PUBLISHABLE_STAGES),
        "publishable": {
            "stages": publishable_stages,
            "total_rows": pub_total,
            "match": pub_match,
            "mismatch": pub_mismatch,
            "match_rate_comparable": (
                round(pub_match / pub_comparable, 4) if pub_comparable else None
            ),
            "usable_coverage": (
                round(pub_comparable / pub_total, 4) if pub_total else None
            ),
        },
    }


@app.command()
def main(
    inputs: list[Path] = typer.Argument(None, help="Input JSONL result files"),
    output: Path = typer.Option(Path("results/telemetry/latest.json")),
    dashboard_copy: Path = typer.Option(
        Path("public/parity-telemetry.json"),
        help="Optional Next.js static copy for the parity dashboard panel",
    ),
    auto_discover: bool = typer.Option(
        True,
        help="If no inputs, discover results/*_parity/latest.jsonl and golden_repros",
    ),
):
    paths = list(inputs or [])
    if not paths and auto_discover:
        root = Path("results")
        for stage in STAGE_ORDER:
            candidate = root / stage / "latest.jsonl"
            if candidate.is_file():
                paths.append(candidate)

    rows: list[dict] = []
    for path in paths:
        rows.extend(read_jsonl(path))

    summary = aggregate_rows(rows)
    summary["sources"] = [str(p) for p in paths]
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(summary, indent=2, sort_keys=True) + "\n"
    output.write_text(payload, encoding="utf-8")
    if dashboard_copy:
        dashboard_copy.parent.mkdir(parents=True, exist_ok=True)
        dashboard_copy.write_text(payload, encoding="utf-8")
    typer.echo(f"Wrote telemetry summary for {len(rows)} rows to {output}")
    if dashboard_copy:
        typer.echo(f"Dashboard copy: {dashboard_copy}")


if __name__ == "__main__":
    app()
