#!/usr/bin/env python3
"""Analyze Phase 3 readability study responses (no composite score)."""
from __future__ import annotations

import argparse
import json
import statistics
from collections import defaultdict
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("responses", nargs="+", type=Path, help="Response JSON files")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("benchmark/readability/study_pack/analysis_latest.json"),
    )
    args = parser.parse_args()

    by_dec: dict[str, list[float]] = defaultdict(list)
    by_dec_time: dict[str, list[float]] = defaultdict(list)
    prefs: dict[str, int] = defaultdict(int)
    n_part = 0
    pilot = True

    for path in args.responses:
        data = json.loads(path.read_text(encoding="utf-8"))
        n_part += 1
        pilot = pilot and bool(data.get("pilot", True))
        if data.get("preference"):
            prefs[str(data["preference"])] += 1
        for item in data.get("items") or []:
            d = str(item.get("decompiler") or "?")
            by_dec[d].append(float(item.get("accuracy") or 0))
            by_dec_time[d].append(float(item.get("time_sec") or 0))

    summary = {
        "schema": "readability-study-analysis-v1",
        "participants": n_part,
        "pilot": pilot,
        "by_decompiler": {},
        "preference_counts": dict(prefs),
        "composite_published": False,
        "note": "Composite forbidden until composite_decision.md is updated with correlations.",
    }
    for d, acc in sorted(by_dec.items()):
        times = by_dec_time[d]
        summary["by_decompiler"][d] = {
            "n_items": len(acc),
            "mean_accuracy": round(statistics.mean(acc), 4) if acc else None,
            "mean_time_sec": round(statistics.mean(times), 2) if times else None,
        }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
