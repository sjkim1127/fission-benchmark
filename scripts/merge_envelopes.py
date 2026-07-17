#!/usr/bin/env python3
"""Merge multiple benchmark envelope JSON files into one.

Used by full_matrix fan-out: each profile writes a slice, then this script
rebuilds matrix + standard summary + validity for the combined rows.

Publication ranking should still prefer the core_c_pe slice; the merged
envelope is for multi-language / multi-ISA diagnostic dashboards.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


def _load(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected envelope object")
    if "rows" not in data:
        raise ValueError(f"{path}: missing rows")
    return data


def _row_key(row: dict[str, Any]) -> tuple[str, str, str]:
    return (
        str(row.get("decompiler") or ""),
        str(row.get("function_name") or ""),
        str(row.get("compiler_variant") or ""),
    )


def merge_envelopes(
    envelopes: list[dict[str, Any]],
    *,
    source_labels: list[str] | None = None,
) -> dict[str, Any]:
    if not envelopes:
        raise ValueError("no envelopes to merge")

    rows: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str]] = set()
    for env in envelopes:
        for row in env.get("rows") or []:
            if not isinstance(row, dict):
                continue
            key = _row_key(row)
            if not all(key) or key in seen:
                continue
            seen.add(key)
            rows.append(row)

    # Matrix from observed cells (fan-out slices are already complete per slice).
    expected_cells = [
        {
            "decompiler": d,
            "function_name": f,
            "compiler_variant": v,
        }
        for (d, f, v) in sorted(seen)
    ]
    expected_decompilers = sorted({c["decompiler"] for c in expected_cells})

    base_run = dict(envelopes[0].get("run") or {})
    base_toolchain = dict(envelopes[0].get("toolchain") or {})
    # Prefer any official=true meta if present.
    for env in envelopes:
        run = env.get("run") or {}
        if run.get("official") is True:
            base_run = dict(run)
            base_toolchain = dict(env.get("toolchain") or base_toolchain)
            break

    labels = source_labels or [
        str((e.get("run") or {}).get("matrix_profile") or f"slice{i}")
        for i, e in enumerate(envelopes)
    ]
    base_run["matrix_profile"] = "full_matrix"
    base_run["merged_from"] = labels
    limits = dict(base_run.get("limits") or {})
    limits["matrix_profile"] = "full_matrix"
    limits["merged_slices"] = labels
    base_run["limits"] = limits

    # Oracle: keep first differential/original_binary evidence if any.
    oracle = {"mode": "example_cases", "valid": False}
    for env in envelopes:
        cand = env.get("oracle") or {}
        if cand.get("valid") and cand.get("oracle_subject") == "original_binary":
            oracle = dict(cand)
            break
        if cand.get("mode") == "differential":
            oracle = dict(cand)

    matrix = {
        "expected_decompilers": expected_decompilers,
        "expected_cells": expected_cells,
        "expected_rows": len(expected_cells),
        "observed_rows": len(rows),
    }

    from runner.run_validity import build_envelope

    return build_envelope(
        rows,
        run_meta=base_run,
        toolchain=base_toolchain,
        matrix=matrix,
        oracle=oracle,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "inputs",
        nargs="+",
        type=Path,
        help="Envelope JSON paths (order preserved for merged_from labels)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        required=True,
        help="Merged envelope output path",
    )
    parser.add_argument(
        "--label",
        action="append",
        default=[],
        help="Optional label per input (repeatable; defaults to matrix_profile)",
    )
    args = parser.parse_args(argv)

    envs = [_load(p) for p in args.inputs]
    labels = args.label if args.label else None
    if labels and len(labels) != len(envs):
        parser.error("--label count must match number of inputs")

    merged = merge_envelopes(envs, source_labels=labels)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(merged, indent=2) + "\n", encoding="utf-8")
    n = len(merged.get("rows") or [])
    valid = (merged.get("validity") or {}).get("valid")
    print(f"Merged {len(envs)} envelopes → {args.output} ({n} rows, valid={valid})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
