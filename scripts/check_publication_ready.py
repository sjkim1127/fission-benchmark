#!/usr/bin/env python3
"""Conservative structural check for official publication readiness.

Does not invent publishable=true. Verifies evidence files and holdout identity.
Pair with ``python -m runner.publication_gate`` after official runs.

Usage:
  python scripts/check_publication_ready.py \\
    --dev results/dev_latest.json \\
    --holdout results/holdout_latest.json \\
    --overfitting results/overfitting_report.json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--dev", type=Path, default=Path("results/dev_latest.json"))
    p.add_argument("--holdout", type=Path, default=Path("results/holdout_latest.json"))
    p.add_argument(
        "--overfitting", type=Path, default=Path("results/overfitting_report.json")
    )
    p.add_argument(
        "--require-official",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Require run.official / run_mode official on envelopes",
    )
    p.add_argument(
        "--allow-missing-overfitting",
        action="store_true",
        help="Only for structural holdout checks without full gate",
    )
    args = p.parse_args(argv)
    errors: list[str] = []

    for label, path in (("dev", args.dev), ("holdout", args.holdout)):
        if not path.is_file():
            errors.append(f"missing {label} envelope: {path}")
            continue
        try:
            env = _load(path)
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid {label} json: {exc}")
            continue
        # Accept envelope dict or bare list of rows (legacy).
        if isinstance(env, list):
            run = {}
            rows = env
        elif isinstance(env, dict):
            run = env.get("run") if isinstance(env.get("run"), dict) else {}
            rows = env.get("rows") if isinstance(env.get("rows"), list) else []
        else:
            errors.append(f"invalid {label} root type: {type(env).__name__}")
            continue
        if label == "holdout":
            corpus = run.get("corpus") or (
                env.get("corpus") if isinstance(env, dict) else None
            )
            if rows and corpus not in (None, "holdout"):
                errors.append(
                    f"holdout corpus identity invalid: corpus={corpus!r}"
                )
            if not rows:
                errors.append("holdout_empty: no result rows")
            if args.require_official:
                official = run.get("official")
                mode = run.get("run_mode") or run.get("mode")
                if official is not True and mode not in ("official", "Official"):
                    if run.get("status") == "skipped" or run.get("skip_reason"):
                        errors.append(
                            f"holdout not official / skipped: status={run.get('status')} "
                            f"skip_reason={run.get('skip_reason')}"
                        )
        if label == "dev" and not rows:
            errors.append("dev envelope has no rows")

    holdout_manifests = list(Path("corpus/holdout/manifests").glob("*.json"))
    if not holdout_manifests:
        errors.append("no corpus/holdout/manifests/*.json — holdout lock missing")

    if not args.allow_missing_overfitting:
        if not args.overfitting.is_file():
            errors.append(f"missing overfitting report: {args.overfitting}")
        else:
            try:
                rep = _load(args.overfitting)
                if rep.get("passed") is not True:
                    errors.append(
                        f"overfitting_failed: passed={rep.get('passed')!r}"
                    )
            except (OSError, json.JSONDecodeError) as exc:
                errors.append(f"invalid overfitting json: {exc}")

    if errors:
        for e in errors:
            print(f"FAIL {e}", file=sys.stderr)
        print(
            f"NOT PUBLICATION-READY: {len(errors)} issue(s). "
            "Run official dev+holdout, holdout_report, then publication_gate.",
            file=sys.stderr,
        )
        return 1

    print(
        "OK publication structural checks "
        f"(dev={args.dev}, holdout={args.holdout}, "
        f"manifests={len(holdout_manifests)})"
    )
    print(
        "Next: python -m runner.publication_gate "
        f"--dev {args.dev} --holdout {args.holdout} "
        f"--overfitting {args.overfitting} --output results/publication-verdict.json"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
