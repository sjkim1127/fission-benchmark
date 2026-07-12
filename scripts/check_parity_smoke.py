#!/usr/bin/env python3
"""Conservative CI gate for layered parity smoke/full telemetry.

Fails on infrastructure / reliability failures that would make published
rates untrustworthy. Legitimate Ghidra↔Fission *mismatches* are quality
signals and do not fail this gate.

Defaults are intentionally strict (no leniency).

Usage:
  python scripts/check_parity_smoke.py results/telemetry/latest.json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Stages that must produce usable quality signal (match|mismatch).
REQUIRED_STAGES = (
    "assembly_parity",
    "cfg_parity",
    "pcode_parity",
    "function_discovery",
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "telemetry",
        type=Path,
        nargs="?",
        default=Path("results/telemetry/latest.json"),
    )
    parser.add_argument(
        "--min-comparable",
        type=int,
        default=5,
        help="Minimum match+mismatch rows required per required stage",
    )
    parser.add_argument(
        "--min-usable-coverage",
        type=float,
        default=0.90,
        help="Minimum (match+mismatch)/total per required stage",
    )
    parser.add_argument(
        "--max-fetch-error-rate",
        type=float,
        default=0.10,
        help="Maximum fetch_error/total per required stage",
    )
    parser.add_argument(
        "--require-strict",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Require canonicalize_mode=strict (default true)",
    )
    args = parser.parse_args(argv)

    if not args.telemetry.is_file():
        print(f"FAIL missing telemetry: {args.telemetry}", file=sys.stderr)
        return 1

    data = json.loads(args.telemetry.read_text(encoding="utf-8"))
    stages = data.get("stages") or {}
    errors: list[str] = []

    if int(data.get("total_rows") or 0) < 1:
        errors.append("total_rows == 0")

    mode = data.get("canonicalize_mode")
    if args.require_strict and mode != "strict":
        errors.append(f"canonicalize_mode={mode!r}; require strict")

    for stage in REQUIRED_STAGES:
        detail = stages.get(stage)
        if not detail:
            errors.append(f"{stage}: missing from telemetry")
            continue
        total = int(detail.get("total") or 0)
        match = int(detail.get("match") or 0)
        mismatch = int(detail.get("mismatch") or 0)
        comparable = match + mismatch
        fetch_error = int(detail.get("fetch_error") or 0)
        if comparable < args.min_comparable:
            errors.append(
                f"{stage}: comparable rows {comparable} < {args.min_comparable} "
                f"(match={match}, mismatch={mismatch}, "
                f"error_or_other={detail.get('error_or_other')}) — likely infra/fetch failure"
            )
        if total > 0:
            coverage = comparable / total
            if coverage < args.min_usable_coverage:
                errors.append(
                    f"{stage}: usable_coverage {coverage:.3f} < {args.min_usable_coverage} "
                    f"(comparable={comparable}, total={total}) — rates not trustworthy"
                )
            fe_rate = fetch_error / total
            if fe_rate > args.max_fetch_error_rate:
                errors.append(
                    f"{stage}: fetch_error_rate {fe_rate:.3f} > {args.max_fetch_error_rate} "
                    f"(fetch_error={fetch_error}, total={total})"
                )

    # Hard fail if *everything* is fetch/error
    by_status = data.get("by_status") or {}
    usable = int(by_status.get("match") or 0) + int(by_status.get("mismatch") or 0)
    if usable < 1:
        errors.append("no match/mismatch rows at all — adapters likely unreachable")

    # Decode must not contribute false quality matches
    dec = stages.get("decode_parity") or {}
    if int(dec.get("match") or 0) > 0:
        errors.append("decode_parity match rows forbidden under stub policy")

    # Reliability rollup if present
    rel = data.get("reliability") or {}
    if rel.get("usable_coverage") is not None and float(rel["usable_coverage"]) < 0.5:
        errors.append(
            f"run usable_coverage {rel['usable_coverage']} < 0.5 — overall not trustworthy"
        )

    if errors:
        for err in errors:
            print(f"FAIL {err}", file=sys.stderr)
        return 1

    print(
        f"OK parity smoke (conservative): total={data.get('total_rows')} "
        f"usable={usable} mode={mode} stages={list(stages.keys())}"
    )
    if rel:
        print(
            f"  reliability: coverage={rel.get('usable_coverage')} "
            f"match_attempted={rel.get('match_rate_attempted')} "
            f"fetch_error_rate={rel.get('fetch_error_rate')}"
        )
    for stage, detail in sorted(stages.items()):
        print(
            f"  {stage}: match_rate={detail.get('match_rate')} "
            f"match_rate_attempted={detail.get('match_rate_attempted')} "
            f"usable_coverage={detail.get('usable_coverage')} "
            f"total={detail.get('total')}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
