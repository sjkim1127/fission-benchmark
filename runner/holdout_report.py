"""
Holdout overfitting report: compare Dev vs Holdout composite scores.

Usage:
    python runner/holdout_report.py --dev results/dev_latest.json --holdout results/holdout_latest.json

Outputs a comparison table and flags decompilers with ≥10pp drop as potential overfitters.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

# Threshold in percentage points: if holdout drops by more than this, flag overfitting
OVERFITTING_THRESHOLD_PP = 10.0


def load_results(path: Path) -> list[dict]:
    return json.loads(path.read_text())


def aggregate_by_decompiler(results: list[dict]) -> dict[str, dict]:
    """Aggregate scores per decompiler."""
    by_d: dict[str, list] = defaultdict(list)
    for r in results:
        if not r.get("error"):
            by_d[r["decompiler"]].append(r)

    agg = {}
    for d, rs in by_d.items():
        composites = [r.get("composite_score", 0.0) for r in rs]
        sims = [r.get("source_similarity", 0.0) for r in rs]
        sems = [r.get("semantic_score", 0.0) for r in rs]
        agg[d] = {
            "count": len(rs),
            "avg_composite": sum(composites) / len(composites),
            "avg_similarity": sum(sims) / len(sims),
            "avg_semantic": sum(sems) / len(sems),
        }
    return agg


def compute_per_function_comparison(
    dev: list[dict], holdout: list[dict]
) -> list[dict]:
    """Per-function composite score comparison (dev vs holdout, per decompiler)."""
    def build_index(results: list[dict]) -> dict[tuple, float]:
        idx = {}
        for r in results:
            if not r.get("error"):
                key = (r["decompiler"], r["function_name"])
                scores = idx.setdefault(key, [])
                scores.append(r.get("composite_score", 0.0))
        return {k: sum(v) / len(v) for k, v in idx.items()}

    dev_idx = build_index(dev)
    holdout_idx = build_index(holdout)

    all_keys = set(dev_idx) | set(holdout_idx)
    rows = []
    for key in sorted(all_keys):
        d_comp = dev_idx.get(key, None)
        h_comp = holdout_idx.get(key, None)
        if d_comp is not None and h_comp is not None:
            drop = (d_comp - h_comp) * 100.0  # positive = holdout is worse
            rows.append({
                "decompiler": key[0],
                "function": key[1],
                "dev_composite": d_comp,
                "holdout_composite": h_comp,
                "drop_pp": drop,
                "flag": "🔴 overfit" if drop >= OVERFITTING_THRESHOLD_PP else "",
            })
    return sorted(rows, key=lambda r: r["drop_pp"], reverse=True)


def generate_report(dev_path: Path, holdout_path: Path, output_path: Path | None = None) -> None:
    dev_results = load_results(dev_path)
    holdout_results = load_results(holdout_path)

    dev_agg = aggregate_by_decompiler(dev_results)
    holdout_agg = aggregate_by_decompiler(holdout_results)

    all_decompilers = sorted(set(dev_agg) | set(holdout_agg))

    lines = []
    lines.append("# Dev vs Holdout Overfitting Report")
    lines.append("")
    lines.append(f"- Dev results: `{dev_path}`  ")
    lines.append(f"- Holdout results: `{holdout_path}`  ")
    lines.append(f"- Overfitting threshold: **{OVERFITTING_THRESHOLD_PP}pp** drop")
    lines.append("")
    lines.append("## Summary by Decompiler")
    lines.append("")

    header = "| Decompiler | Dev N | Dev Composite | Holdout N | Holdout Composite | Drop (pp) | Flag |"
    sep    = "|---|---|---|---|---|---|---|"
    lines.append(header)
    lines.append(sep)

    overfit_flags = []
    for d in all_decompilers:
        dev_d = dev_agg.get(d, {})
        ho_d = holdout_agg.get(d, {})
        dev_comp = dev_d.get("avg_composite", None)
        ho_comp = ho_d.get("avg_composite", None)

        if dev_comp is not None and ho_comp is not None:
            drop = (dev_comp - ho_comp) * 100.0
            flag = "🔴 Overfitting" if drop >= OVERFITTING_THRESHOLD_PP else "✅"
            if drop >= OVERFITTING_THRESHOLD_PP:
                overfit_flags.append(d)
        else:
            drop = 0.0
            flag = "⚠️ No holdout data" if ho_comp is None else "⚠️ No dev data"

        dev_comp_str = f"{dev_comp:.3f}" if dev_comp is not None else "—"
        ho_comp_str = f"{ho_comp:.3f}" if ho_comp is not None else "—"
        drop_str = f"{drop:+.1f}pp" if (dev_comp is not None and ho_comp is not None) else "—"

        lines.append(
            f"| **{d}** | {dev_d.get('count', '—')} | {dev_comp_str} "
            f"| {ho_d.get('count', '—')} | {ho_comp_str} | {drop_str} | {flag} |"
        )

    lines.append("")

    # Per-function comparison
    fn_rows = compute_per_function_comparison(dev_results, holdout_results)
    worst = [r for r in fn_rows if r["drop_pp"] >= OVERFITTING_THRESHOLD_PP]

    if worst:
        lines.append("## 🔴 Worst Overfitting Cases")
        lines.append("")
        lines.append("| Decompiler | Function | Dev | Holdout | Drop (pp) |")
        lines.append("|---|---|---|---|---|")
        for r in worst[:20]:
            lines.append(
                f"| {r['decompiler']} | `{r['function']}` "
                f"| {r['dev_composite']:.3f} | {r['holdout_composite']:.3f} | {r['drop_pp']:+.1f}pp |"
            )
        lines.append("")

    # Terminal output
    print("\n" + "\n".join(lines))

    if overfit_flags:
        print(f"\n⚠️  OVERFITTING ALERT: {', '.join(overfit_flags)} dropped ≥{OVERFITTING_THRESHOLD_PP}pp on holdout")
        print("   This suggests optimization/tuning to the dev corpus. Review these decompilers.")
    else:
        print(f"\n✅ No overfitting detected (all decompilers within {OVERFITTING_THRESHOLD_PP}pp on holdout)")

    # Save report
    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text("\n".join(lines), encoding="utf-8")
        print(f"\n📝 Report saved to {output_path}")

    # Exit with non-zero if any overfitting detected (for CI gate)
    if overfit_flags:
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Generate Dev vs Holdout overfitting report")
    parser.add_argument("--dev", required=True, help="Path to dev corpus benchmark JSON")
    parser.add_argument("--holdout", required=True, help="Path to holdout corpus benchmark JSON")
    parser.add_argument("--output", default=None, help="Optional output Markdown path")
    args = parser.parse_args()

    generate_report(
        dev_path=Path(args.dev),
        holdout_path=Path(args.holdout),
        output_path=Path(args.output) if args.output else None,
    )


if __name__ == "__main__":
    main()
