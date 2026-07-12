#!/usr/bin/env python3
"""CI gate for layered parity smoke telemetry.

Fails on infrastructure / reliability failures that would make published
rates untrustworthy. Legitimate Ghidra↔Fission *mismatches* are quality
signals and do not fail this gate.

Usage:
  python scripts/check_parity_smoke.py results/telemetry/latest.json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Stages that must produce usable quality signal (match|mismatch) when not skipped.
REQUIRED_STAGES = (
    "assembly_parity",
    "cfg_parity",
    "pcode_parity",
)

# Decode may be entirely skipped when adapters only stub disasm→decode.
OPTIONAL_STAGES = (
    "decode_parity",
    "function_discovery",
    "ir_invariants",
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
        default=1,
        help="Minimum match+mismatch rows required per required stage",
    )
    parser.add_argument(
        "--min-usable-coverage",
        type=float,
        default=0.5,
        help=(
            "Minimum (match+mismatch)/total per required stage. "
            "Protects against inflate-by-dropping-fetch-errors."
        ),
    )
    parser.add_argument(
        "--max-fetch-error-rate",
        type=float,
        default=0.35,
        help="Maximum fetch_error/total per required stage (infra health)",
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

    # Reliability rollup if present (telemetry v2)
    rel = data.get("reliability") or {}
    if rel.get("usable_coverage") is not None and float(rel["usable_coverage"]) < 0.3:
        errors.append(
            f"run usable_coverage {rel['usable_coverage']} < 0.3 — overall not trustworthy"
        )

    if errors:
        for err in errors:
            print(f"FAIL {err}", file=sys.stderr)
        return 1

    print(
        f"OK parity smoke: total={data.get('total_rows')} "
        f"usable={usable} stages={list(stages.keys())}"
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
    # Warn (non-fatal) if decode is still a scored twin of assembly
    dec = stages.get("decode_parity") or {}
    if int(dec.get("match") or 0) + int(dec.get("mismatch") or 0) > 0:
        if int(dec.get("skipped") or 0) == 0:
            print(
                "WARN decode_parity is still scored (expected stub skip). "
                "Adapters may have grown a real decode surface — verify intentionally.",
                file=sys.stderr,
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
