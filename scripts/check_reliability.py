#!/usr/bin/env python3
"""Conservative reliability gate for parity telemetry.

Policy: no leniency. Fail on anything that could inflate trustworthiness of
published rates. Does *not* require Fission to match Ghidra — mismatches are
allowed quality signals. Infra failure, stub scoring, and mode drift fail hard.

Usage:
  python scripts/check_reliability.py results/telemetry/latest.json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PRIMARY = ("assembly_parity", "pcode_parity", "cfg_parity", "function_discovery")
DEMOTED = ("decode_parity", "ir_invariants", "golden_repros")


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
        default=0.95,
        help="Min usable_coverage for each primary stage (conservative default 0.95)",
    )
    parser.add_argument(
        "--max-fetch-error-rate",
        type=float,
        default=0.05,
        help="Max fetch_error/total per primary stage",
    )
    parser.add_argument(
        "--max-global-fetch-error-rate",
        type=float,
        default=0.05,
        help="Max overall reliability.fetch_error_rate",
    )
    parser.add_argument(
        "--require-strict",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Require canonicalize_mode=strict (default: true)",
    )
    parser.add_argument(
        "--min-primary-comparable",
        type=int,
        default=5,
        help="Minimum match+mismatch rows per primary stage (assembly/pcode/cfg)",
    )
    parser.add_argument(
        "--min-primary-comparable-fd",
        type=int,
        default=1,
        help=(
            "Minimum match+mismatch rows for function_discovery. "
            "Defaults to 1 because this stage is per-binary, not per-function."
        ),
    )
    args = parser.parse_args(argv)

    if not args.telemetry.is_file():
        print(f"FAIL missing telemetry: {args.telemetry}", file=sys.stderr)
        return 1

    data = json.loads(args.telemetry.read_text(encoding="utf-8"))
    stages = data.get("stages") or {}
    by_status = data.get("by_status") or {}
    errors: list[str] = []

    # --- Mode ---
    mode = data.get("canonicalize_mode")
    if args.require_strict and mode != "strict":
        errors.append(
            f"canonicalize_mode={mode!r} but conservative policy requires strict"
        )
    if mode not in {"loose", "strict", None}:
        errors.append(f"unknown canonicalize_mode={mode!r}")

    policy = data.get("reliability_policy") or data.get("policy")
    if policy and policy not in {"conservative", "strict"}:
        errors.append(f"reliability_policy={policy!r} is not conservative")

    # --- Empty false-match classes must never appear as match ---
    if int(by_status.get("match") or 0) > 0 and int(by_status.get("both_empty_invalid") or 0) < 0:
        pass  # unreachable; both_empty is separate status
    # Ensure we are not scoring empty as match via missing stage data
    for stage, detail in stages.items():
        st = detail.get("by_status") or {}
        if int(st.get("match") or 0) > 0 and int(detail.get("total") or 0) == int(
            st.get("both_empty_invalid") or 0
        ):
            errors.append(f"{stage}: impossible match-only-on-empty configuration")

    # --- Publishable headline composition ---
    pub = data.get("publishable") or {}
    pub_stages = set((pub.get("stages") or {}).keys())
    for bad in DEMOTED:
        if bad in pub_stages:
            errors.append(f"publishable headline still includes demoted stage {bad}")

    for need in PRIMARY:
        detail = stages.get(need)
        if not detail:
            errors.append(f"primary stage missing from telemetry: {need}")
            continue
        total = int(detail.get("total") or 0)
        match = int(detail.get("match") or 0)
        mismatch = int(detail.get("mismatch") or 0)
        comparable = match + mismatch
        fetch_error = int(detail.get("fetch_error") or 0)
        if total > 0 and need not in pub_stages:
            errors.append(f"primary stage {need} missing from publishable headline")
        if comparable < (args.min_primary_comparable_fd if need == "function_discovery" else args.min_primary_comparable):
            errors.append(
                f"{need}: comparable {comparable} < "
                f"{args.min_primary_comparable_fd if need == 'function_discovery' else args.min_primary_comparable}"
            )
        cov = detail.get("usable_coverage")
        if total > 0 and cov is not None and float(cov) < args.min_primary_coverage:
            errors.append(
                f"{need}: usable_coverage {cov} < {args.min_primary_coverage}"
            )
        if total > 0:
            fe_rate = fetch_error / total
            if fe_rate > args.max_fetch_error_rate:
                errors.append(
                    f"{need}: fetch_error_rate {fe_rate:.4f} > {args.max_fetch_error_rate}"
                )
        if detail.get("primary_quality") is False:
            errors.append(f"{need}: primary_quality flag is false")

    # --- Decode: zero scored matches under stub policy ---
    dec = stages.get("decode_parity") or {}
    if int(dec.get("match") or 0) > 0:
        errors.append(
            "decode_parity has match rows — stub decode must be skipped, never match"
        )
    if int(dec.get("total") or 0) > 0 and int(dec.get("skipped") or 0) == 0:
        # All decode rows should be skipped while surface is stub
        comparable_dec = int(dec.get("match") or 0) + int(dec.get("mismatch") or 0)
        if comparable_dec > 0:
            errors.append(
                "decode_parity has scored comparable rows without skipped-only policy"
            )

    # --- Function discovery: inventory only ---
    fd = stages.get("function_discovery") or {}
    if int(fd.get("legacy_presence_rows") or 0) > 0:
        errors.append(
            "function_discovery has legacy presence-scored rows; re-run inventory parity"
        )
    # Reject near-100% inventory match with zero dual (suspicious under-discovery collusion)
    if (
        (fd.get("match_rate") or 0) >= 0.99
        and int(fd.get("total") or 0) >= 10
        and not (fd.get("dual") or {})
    ):
        errors.append(
            "function_discovery ~100% without dual recall metrics — untrusted"
        )

    # --- Pcode dual metrics required ---
    pcode = stages.get("pcode_parity") or {}
    comparable_p = int(pcode.get("match") or 0) + int(pcode.get("mismatch") or 0)
    dual = pcode.get("dual") or (pub.get("pcode_dual") or {})
    if comparable_p >= args.min_primary_comparable and not dual:
        errors.append(
            "pcode_parity lacks dual metrics (opcode/loose/strict) — re-run parity"
        )
    # If primary match_rate is high under strict, dual must not contradict with
    # missing opcode metrics (leniency smell)
    if dual and comparable_p >= args.min_primary_comparable:
        strict_full = dual.get("strict_full_match_rate")
        status_rate = pcode.get("match_rate")
        if (
            status_rate is not None
            and strict_full is not None
            and abs(float(status_rate) - float(strict_full)) > 0.05
            and mode == "strict"
        ):
            errors.append(
                f"pcode match_rate {status_rate} disagrees with strict_full_match_rate "
                f"{strict_full} under strict mode"
            )

    # --- Global fetch health ---
    rel = data.get("reliability") or {}
    gfe = rel.get("fetch_error_rate")
    if gfe is not None and float(gfe) > args.max_global_fetch_error_rate:
        errors.append(
            f"global fetch_error_rate {gfe} > {args.max_global_fetch_error_rate}"
        )

    # --- Critique warnings that imply scoring dishonesty → hard fail ---
    for w in (data.get("reliability_critique") or {}).get("warnings") or []:
        text = str(w).lower()
        if any(
            k in text
            for k in (
                "presence scoring",
                "legacy presence",
                "presence-scored",
                "double-empty",
                "both empty",
            )
        ):
            errors.append(f"reliability_critique hard-fail: {w}")

    # --- IR must stay demoted ---
    if "ir_invariants" in pub_stages:
        errors.append("ir_invariants must not be in publishable headline")

    if errors:
        for e in errors:
            print(f"FAIL {e}", file=sys.stderr)
        print(
            f"FAIL reliability gate: {len(errors)} error(s), policy=conservative",
            file=sys.stderr,
        )
        return 1

    # Soft notes (non-fatal) for operator awareness only
    for w in (data.get("reliability_critique") or {}).get("warnings") or []:
        print(f"NOTE {w}", file=sys.stderr)

    print(
        f"OK reliability (conservative): mode={mode} "
        f"headline_match_rate={pub.get('match_rate_comparable')} "
        f"primary={sorted(pub_stages)}"
    )
    if dual:
        print(
            f"  pcode dual: opcode={dual.get('opcode_sequence_match_rate')} "
            f"loose_full={dual.get('loose_full_match_rate')} "
            f"strict_full={dual.get('strict_full_match_rate')}"
        )
    fd_dual = (stages.get("function_discovery") or {}).get("dual") or {}
    if fd_dual:
        print(
            f"  fd dual: presence_recall={fd_dual.get('mean_presence_recall')} "
            f"manifest_recall={fd_dual.get('mean_manifest_recall')} "
            f"(set match_rate={fd.get('match_rate')})"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
