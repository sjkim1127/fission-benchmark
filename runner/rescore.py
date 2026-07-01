"""
Re-score existing benchmark results with the new composite scoring formula.

Usage:
    python runner/rescore.py [--input results/latest.json] [--show-top 10]

This script reads a previous JSON result file, applies the new composite_score formula
(semantic*0.70 + sim*0.20 + (1-structural_penalty)*0.10), and outputs a ranking diff table
comparing old source_similarity ranks vs new composite_score ranks.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from scoring import compute_composite, compute_structural_penalty, WEIGHT_SEMANTIC, WEIGHT_SIMILARITY, WEIGHT_STRUCTURAL


def rescore(input_path: Path, show_top: int = 20) -> None:
    raw = json.loads(input_path.read_text())

    if not raw:
        print("No results found.")
        return

    # Load source metrics if available
    metrics_path = Path(__file__).parent.parent / "corpus" / "source_metrics.json"
    src_gotos: dict[str, int] = {}
    src_depths: dict[str, int] = {}
    if metrics_path.exists():
        data = json.loads(metrics_path.read_text())
        src_gotos = data.get("goto_counts", {})
        src_depths = data.get("nesting_depths", {})

    # Build enriched records
    records = []
    for r in raw:
        fn = r.get("function_name", "")
        sem = r.get("semantic_score", 0.0)
        sim = r.get("source_similarity", 0.0)
        gotos = r.get("goto_count", 0)
        depth = r.get("nesting_depth", 0)
        error = r.get("error")

        sp = compute_structural_penalty(
            gotos, depth,
            src_gotos.get(fn, 0),
            src_depths.get(fn, 0),
        )
        composite = compute_composite(sem, sim, sp) if not error else 0.0

        records.append({
            **r,
            "structural_penalty": sp,
            "composite_score": composite,
        })

    # Group by (function_name, compiler_variant) and compute old vs new ranks
    groups: dict[tuple, list[dict]] = defaultdict(list)
    for r in records:
        key = (r["function_name"], r["compiler_variant"])
        groups[key].append(r)

    print(f"\n{'='*90}")
    print("  RESCORE DIFF  |  Old rank = source_similarity rank  |  New rank = composite_score rank")
    print(f"  Weights: semantic={WEIGHT_SEMANTIC:.0%}  similarity={WEIGHT_SIMILARITY:.0%}  structural={WEIGHT_STRUCTURAL:.0%}")
    print(f"{'='*90}")
    print(f"{'Function':20s} {'Variant':16s} {'Decomp':10s} {'OldSim':8s} {'OldRk':6s} {'NewCmp':8s} {'NewRk':6s} {'Δ':4s}  {'Change':20s}")
    print(f"{'-'*20} {'-'*16} {'-'*10} {'-'*8} {'-'*6} {'-'*8} {'-'*6} {'-'*4}  {'-'*20}")

    total_moves = 0
    rows_printed = 0

    for (fn_name, variant), group in sorted(groups.items()):
        valid = [r for r in group if not r.get("error")]
        if not valid:
            continue

        # Old ranking: by source_similarity desc
        old_sorted = sorted(valid, key=lambda x: x["source_similarity"], reverse=True)
        old_ranks = {r["decompiler"]: i+1 for i, r in enumerate(old_sorted)}

        # New ranking: by composite_score desc
        new_sorted = sorted(valid, key=lambda x: x["composite_score"], reverse=True)
        new_ranks = {r["decompiler"]: i+1 for i, r in enumerate(new_sorted)}

        for r in sorted(valid, key=lambda x: old_ranks[x["decompiler"]]):
            d = r["decompiler"]
            old_rk = old_ranks[d]
            new_rk = new_ranks[d]
            delta = old_rk - new_rk  # positive = moved up
            change = ""
            if delta > 0:
                change = f"↑ +{delta} (promoted)"
                total_moves += 1
            elif delta < 0:
                change = f"↓ {delta} (demoted)"
                total_moves += 1

            print(
                f"{fn_name:20s} {variant:16s} {d:10s} "
                f"{r['source_similarity']:8.3f} {old_rk:6d} "
                f"{r['composite_score']:8.3f} {new_rk:6d} "
                f"{delta:+4d}  {change:20s}"
            )
            rows_printed += 1
            if rows_printed >= show_top and show_top > 0:
                break

        if rows_printed >= show_top and show_top > 0:
            break

    print(f"\n{'='*90}")
    print(f"Total rank changes: {total_moves} / {len(records)}")

    # Summary by decompiler
    print(f"\n{'='*50}")
    print("  AGGREGATE SUMMARY BY DECOMPILER")
    print(f"{'='*50}")
    print(f"{'Decomp':12s} {'AvgOldSim':10s} {'AvgNewCmp':10s} {'Δ':8s}")
    print(f"{'-'*12} {'-'*10} {'-'*10} {'-'*8}")

    by_d: dict[str, list] = defaultdict(list)
    for r in records:
        if not r.get("error"):
            by_d[r["decompiler"]].append(r)

    rows_by_d = []
    for d, rs in by_d.items():
        avg_sim = sum(r["source_similarity"] for r in rs) / len(rs)
        avg_comp = sum(r["composite_score"] for r in rs) / len(rs)
        rows_by_d.append((d, avg_sim, avg_comp))

    rows_by_d.sort(key=lambda x: x[2], reverse=True)
    for d, avg_sim, avg_comp in rows_by_d:
        delta = avg_comp - avg_sim
        print(f"{d:12s} {avg_sim:10.3f} {avg_comp:10.3f} {delta:+8.3f}")

    print("\n📝 Note: negative Δ means composite is lower than similarity (semantic failures penalized)")
    print("📝 Note: positive Δ means composite is higher (strong semantic scores lift ranking)")


def main():
    parser = argparse.ArgumentParser(description="Re-score existing benchmark results with composite formula")
    parser.add_argument(
        "--input",
        default="results/latest.json",
        help="Path to benchmark JSON result file (default: results/latest.json)",
    )
    parser.add_argument(
        "--show-top",
        type=int,
        default=0,
        help="Limit rows printed (0 = all)",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: {input_path} not found.", file=sys.stderr)
        sys.exit(1)

    rescore(input_path, show_top=args.show_top)


if __name__ == "__main__":
    main()
