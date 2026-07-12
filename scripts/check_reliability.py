#!/usr/bin/env python3
"""Fail CI when parity telemetry would mislead about quality.

Checks structural honesty of rates, not that Fission matches Ghidra.

Usage:
  python scripts/check_reliability.py results/telemetry/latest.json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PRIMARY = ("assembly_parity", "pcode_parity", "cfg_parity", "function_discovery")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "telemetry",
        type=Path,
        nargs="?",
        default=Path("results/telemetry/latest.json"),
    )
    parser.add_argument(
        "--min-primary-coverage",
        type=float,
        default=0.85,
        help="Min usable_coverage for each primary stage",
    )
    args = parser.parse_args(argv)

    if not args.telemetry.is_file():
        print(f"FAIL missing telemetry: {args.telemetry}", file=sys.stderr)
        return 1

    data = json.loads(args.telemetry.read_text(encoding="utf-8"))
    stages = data.get("stages") or {}
    errors: list[str] = []
    warnings: list[str] = list((data.get("reliability_critique") or {}).get("warnings") or [])

    pub = data.get("publishable") or {}
    pub_stages = set((pub.get("stages") or {}).keys())
    # Headline must not include demoted stages.
    for bad in ("decode_parity", "ir_invariants", "golden_repros"):
        if bad in pub_stages:
            errors.append(f"publishable headline still includes demoted stage {bad}")
    for need in PRIMARY:
        if need not in pub_stages and need in stages:
            # Only require presence when the run emitted that stage.
            if int((stages.get(need) or {}).get("total") or 0) > 0 and need not in pub_stages:
                errors.append(f"primary stage {need} missing from publishable headline")

    for stage in PRIMARY:
        detail = stages.get(stage)
        if not detail:
            errors.append(f"primary stage missing: {stage}")
            continue
        cov = detail.get("usable_coverage")
        if cov is not None and float(cov) < args.min_primary_coverage:
            errors.append(
                f"{stage}: usable_coverage {cov} < {args.min_primary_coverage}"
            )
        if not detail.get("primary_quality", stage in PRIMARY):
            errors.append(f"{stage}: primary_quality flag missing/false")

    # Decode must not be scored as quality match.
    dec = stages.get("decode_parity") or {}
    if int(dec.get("match") or 0) > 0 and int(dec.get("skipped") or 0) == 0:
        # Real decode surface might exist — warn only
        warnings.append(
            "decode_parity has scored matches; verify real decode fields exist"
        )
    elif int(dec.get("match") or 0) > 0 and int(dec.get("skipped") or 0) > 0:
        # mixed — suspicious
        errors.append("decode_parity has both match and skipped rows — inconsistent")

    # Legacy presence scoring must not dominate function_discovery.
    fd = stages.get("function_discovery") or {}
    if int(fd.get("legacy_presence_rows") or 0) > 0:
        errors.append(
            "function_discovery has legacy presence-scored rows; re-run inventory parity"
        )

    # Pcode dual metrics required after dual-metric rollout when comparable > 0
    pcode = stages.get("pcode_parity") or {}
    comparable = int(pcode.get("match") or 0) + int(pcode.get("mismatch") or 0)
    dual = pcode.get("dual") or (pub.get("pcode_dual") or {})
    if comparable >= 5 and not dual:
        warnings.append(
            "pcode_parity lacks dual metrics (re-run parity after dual-metric deploy)"
        )

    mode = data.get("canonicalize_mode")
    if mode not in {"loose", "strict"}:
        warnings.append(f"unknown canonicalize_mode={mode!r}")

    for w in warnings:
        print(f"WARN {w}", file=sys.stderr)

    if errors:
        for e in errors:
            print(f"FAIL {e}", file=sys.stderr)
        return 1

    print(
        f"OK reliability: mode={mode} "
        f"headline_match_rate={pub.get('match_rate_comparable')} "
        f"primary={sorted(pub_stages)} "
        f"critique_warnings={len(warnings)}"
    )
    if dual:
        print(
            f"  pcode dual: opcode={dual.get('opcode_sequence_match_rate')} "
            f"loose_full={dual.get('loose_full_match_rate')} "
            f"strict_full={dual.get('strict_full_match_rate')}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
