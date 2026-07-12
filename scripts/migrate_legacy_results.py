#!/usr/bin/env python3
"""Wrap a legacy flat-list benchmark result as a non-publishable envelope v2.

Legacy ``results/*.json`` files are plain lists of score rows. The dashboard and
publication gate require schema_version 2. This tool preserves the rows and
emits a candidate envelope that is **never** marked publishable (missing
official run metadata and oracle evidence).

Usage:
  python scripts/migrate_legacy_results.py results/dev_latest.json \\
      --output results/dev_latest.envelope.json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    from runner.run_validity import build_envelope, load_result_file
    from runner.scoring import compute_correctness_score
    from runner.standard_summary import attach_summary_to_envelope
except ImportError:  # pragma: no cover - direct script edge cases
    sys.path.insert(0, str(ROOT / "runner"))
    from run_validity import build_envelope, load_result_file
    from scoring import compute_correctness_score
    from standard_summary import attach_summary_to_envelope


def _normalize_row_correctness(row: dict) -> dict:
    """Force semantic-only correctness (legacy composite scores are invalid)."""
    out = dict(row)
    semantic = out.get("semantic_score")
    out["correctness_score"] = compute_correctness_score(
        semantic if semantic is not None else None,
        float(out.get("source_similarity") or 0.0),
        float(out.get("structural_penalty") or 0.0),
    )
    # composite_score is a deprecated alias
    if "composite_score" in out:
        out["composite_score"] = out["correctness_score"]
    return out


def migrate(path: Path) -> dict:
    loaded = load_result_file(path)
    if not loaded.legacy:
        if loaded.envelope is None:
            raise ValueError(f"{path} is not a recognizable result file")
        # Still rewrite correctness if a modern envelope carries composite drift.
        env = dict(loaded.envelope)
        env["rows"] = [_normalize_row_correctness(r) for r in env.get("rows") or []]
        return attach_summary_to_envelope(env)

    # Reconstruct a minimal matrix from observed rows so validity diagnostics
    # can still compute coverage; official/publishable remain false.
    expected_cells = []
    decompilers: set[str] = set()
    rows = [_normalize_row_correctness(row) for row in loaded.rows]
    for row in rows:
        decompilers.add(row.get("decompiler", ""))
        expected_cells.append({
            "decompiler": row.get("decompiler", ""),
            "function_name": row.get("function_name", ""),
            "compiler_variant": row.get("compiler_variant", ""),
        })

    return build_envelope(
        rows,
        run_meta={
            "corpus": "dev",
            "official": False,
            "run_mode": "legacy_migration",
            "run_id": f"legacy-migrate-{path.stem}",
            "notes": "Migrated from legacy flat-list; not publishable",
        },
        toolchain={"source": "legacy_migration"},
        matrix={
            "expected_decompilers": sorted(d for d in decompilers if d),
            "expected_cells": expected_cells,
            "expected_rows": len(expected_cells),
            "observed_rows": len(loaded.rows),
        },
        oracle={"mode": "example_cases", "valid": False},
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Legacy flat-list or envelope JSON")
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Destination envelope JSON (never overwrites input unless paths match)",
    )
    args = parser.parse_args(argv)

    try:
        envelope = migrate(args.input)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(envelope, indent=2) + "\n", encoding="utf-8")
    valid = envelope.get("validity", {}).get("valid")
    publishable = envelope.get("validity", {}).get("publishable")
    print(
        f"wrote {args.output} "
        f"(schema_version={envelope.get('schema_version')}, "
        f"valid={valid}, publishable={publishable}, rows={len(envelope.get('rows', []))})"
    )
    if publishable:
        print("warning: unexpected publishable=true after migration", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
