#!/usr/bin/env python3
"""Extract golden repro cases from parity JSONL mismatches.

Creates/updates ``benchmark/golden_repros/manifest.json`` with HTTP-based
canaries that lock known Ghidra→Fission gaps (cfg/pcode) so regressions are
tracked even before they are fixed.

Usage:
  python scripts/extract_golden_repros.py \\
    --inputs results/cfg_parity/latest.jsonl results/pcode_parity/latest.jsonl \\
    --output benchmark/golden_repros/manifest.json \\
    --stages cfg_parity,pcode_parity \\
    --limit-per-stage 5
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", nargs="+", type=Path, required=True)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("benchmark/golden_repros/manifest.json"),
    )
    parser.add_argument(
        "--stages",
        default="cfg_parity,pcode_parity",
        help="Comma-separated stages to freeze",
    )
    parser.add_argument("--limit-per-stage", type=int, default=5)
    parser.add_argument(
        "--candidate",
        default="fission",
        help="Only freeze rows for this candidate",
    )
    args = parser.parse_args(argv)

    wanted = {s.strip() for s in args.stages.split(",") if s.strip()}
    by_stage: dict[str, list[dict]] = defaultdict(list)

    for path in args.inputs:
        if not path.is_file():
            print(f"skip missing {path}")
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            if row.get("status") != "mismatch":
                continue
            if row.get("stage") not in wanted:
                continue
            if row.get("candidate") != args.candidate:
                continue
            by_stage[str(row["stage"])].append(row)

    cases = []
    for stage, rows in sorted(by_stage.items()):
        # Prefer diverse functions
        seen_fn: set[str] = set()
        selected = []
        for row in rows:
            fn = (row.get("subject") or {}).get("function") or ""
            if fn in seen_fn:
                continue
            seen_fn.add(fn)
            selected.append(row)
            if len(selected) >= args.limit_per_stage:
                break
        for row in selected:
            sub = row.get("subject") or {}
            binary = sub.get("binary") or ""
            # Prefer corpus-relative path
            if not str(binary).startswith("corpus/") and "corpus/" in str(binary):
                binary = "corpus/" + str(binary).split("corpus/", 1)[1]
            name = f"{stage}__{sub.get('function')}__{sub.get('compiler')}{sub.get('opt')}".replace(
                " ", ""
            )
            cases.append({
                "name": name,
                "stage": stage,
                "binary": binary,
                "function": sub.get("function"),
                "addr": sub.get("addr"),
                "arch": sub.get("arch", "x86_64"),
                "compiler": sub.get("compiler", "gcc"),
                "opt": sub.get("opt", "-O0"),
                "corpus_split": "dev",
                "reference_http": row.get("reference", "ghidra"),
                "candidate_http": row.get("candidate", "fission"),
                "expect_status": "mismatch",
                "expect_mismatch_kind": row.get("mismatch_kind") or "golden_repro",
                "notes": (
                    f"Frozen known gap: {row.get('reference')}→{row.get('candidate')} "
                    f"{stage} {row.get('mismatch_kind')}"
                ),
            })

    payload = {
        "_comment": (
            "Golden canaries for known Fission parity gaps vs Ghidra. "
            "expect_status=mismatch locks the gap until a fix lands; then update "
            "the case to expect_status=match."
        ),
        "schema": "golden-repros-v1",
        "cases": cases,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {len(cases)} cases to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
