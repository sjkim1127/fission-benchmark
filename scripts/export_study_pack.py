#!/usr/bin/env python3
"""Export decompiled snippets for the human readability study pack (scaffold).

Usage:
  python scripts/export_study_pack.py \\
    --input results/dev_latest.json \\
    --functions benchmark/readability/study_pack/functions.json \\
    --output benchmark/readability/study_pack/exports/
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from runner.run_validity import load_result_file  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument(
        "--functions",
        type=Path,
        default=ROOT / "benchmark/readability/study_pack/functions.json",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "benchmark/readability/study_pack/exports",
    )
    args = parser.parse_args(argv)

    spec = json.loads(args.functions.read_text(encoding="utf-8"))
    names = {c["name"] for c in spec.get("candidates", []) if c.get("name")}
    if not names:
        print("error: no candidates in functions.json", file=sys.stderr)
        return 1

    loaded = load_result_file(args.input)
    args.output.mkdir(parents=True, exist_ok=True)
    written = 0
    for row in loaded.rows:
        if row.get("function_name") not in names:
            continue
        if row.get("error"):
            continue
        code = row.get("decompiled_code") or ""
        if not code.strip():
            continue
        decomp = row.get("decompiler", "unknown")
        fn = row.get("function_name")
        variant = str(row.get("compiler_variant", "default")).replace(" ", "_")
        path = args.output / decomp / f"{fn}__{variant}.c"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(code, encoding="utf-8")
        written += 1

    meta = {
        "source": str(args.input),
        "functions": sorted(names),
        "files_written": written,
        "note": "Study export only — not a readability score.",
    }
    (args.output / "export_meta.json").write_text(
        json.dumps(meta, indent=2) + "\n", encoding="utf-8"
    )
    print(f"wrote {written} snippets under {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
