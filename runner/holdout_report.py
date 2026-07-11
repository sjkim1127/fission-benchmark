"""
Holdout overfitting report: compare Dev vs Holdout correctness scores.

Usage:
    python runner/holdout_report.py --dev results/dev_latest.json --holdout results/holdout_latest.json

Outputs a comparison table and flags decompilers with ≥10pp drop as potential overfitters.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path

try:
    from .run_validity import load_result_file
except ImportError:
    from run_validity import load_result_file

# Threshold in percentage points: if holdout drops by more than this, flag overfitting
OVERFITTING_THRESHOLD_PP = 10.0

def load_results(path: Path) -> list[dict]:
    return load_result_file(path).rows


def aggregate_by_decompiler(results: list[dict]) -> dict[str, dict]:
    """Aggregate scores per decompiler."""
    by_d: dict[str, list] = defaultdict(list)
    for r in results:
        if not r.get("error"):
            by_d[r["decompiler"]].append(r)

    agg = {}
    for d, rs in by_d.items():
        correctness = [r["correctness_score"] for r in rs if r.get("correctness_score") is not None]
        sims = [r.get("source_similarity", 0.0) for r in rs]
        sems = [r["semantic_score"] for r in rs if r.get("semantic_score") is not None]
        agg[d] = {
            "count": len(rs),
            "correctness_tested": len(correctness),
            "semantic_tested": len(sems),
            "avg_correctness": sum(correctness) / len(correctness) if correctness else None,
            "avg_similarity": sum(sims) / len(sims),
            "avg_semantic": sum(sems) / len(sems) if sems else None,
        }
    return agg


def compute_per_function_comparison(
    dev: list[dict], holdout: list[dict]
) -> list[dict]:
    """Per-function correctness score comparison (dev vs holdout, per decompiler)."""
    def build_index(results: list[dict]) -> dict[tuple, float]:
        idx = {}
        for r in results:
            if not r.get("error"):
                key = (r["decompiler"], r["function_name"])
                scores = idx.setdefault(key, [])
                if r.get("correctness_score") is not None:
                    scores.append(r["correctness_score"])
        return {k: sum(v) / len(v) for k, v in idx.items() if v}

    dev_idx = build_index(dev)
    holdout_idx = build_index(holdout)

    all_keys = set(dev_idx) | set(holdout_idx)
    rows = []
    for key in sorted(all_keys):
        dev_correctness = dev_idx.get(key, None)
        holdout_correctness = holdout_idx.get(key, None)
        if dev_correctness is not None and holdout_correctness is not None:
            drop = (dev_correctness - holdout_correctness) * 100.0  # positive = holdout is worse
            rows.append({
                "decompiler": key[0],
                "function": key[1],
                "dev_correctness": dev_correctness,
                "holdout_correctness": holdout_correctness,
                "drop_pp": drop,
                "flag": "🔴 overfit" if drop >= OVERFITTING_THRESHOLD_PP else "",
            })
    return sorted(rows, key=lambda r: r["drop_pp"], reverse=True)


def generate_report(
    dev_path: Path,
    holdout_path: Path,
    output_path: Path | None = None,
    json_output_path: Path | None = None,
) -> dict:
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

    header = "| Decompiler | Dev N | Dev Correctness | Holdout N | Holdout Correctness | Drop (pp) | Flag |"
    sep    = "|---|---|---|---|---|---|---|"
    lines.append(header)
    lines.append(sep)

    overfit_flags = []
    for d in all_decompilers:
        dev_d = dev_agg.get(d, {})
        ho_d = holdout_agg.get(d, {})
        dev_correctness = dev_d.get("avg_correctness", None)
        holdout_correctness = ho_d.get("avg_correctness", None)

        if dev_correctness is not None and holdout_correctness is not None:
            drop = (dev_correctness - holdout_correctness) * 100.0
            flag = "🔴 Overfitting" if drop >= OVERFITTING_THRESHOLD_PP else "✅"
            if drop >= OVERFITTING_THRESHOLD_PP:
                overfit_flags.append(d)
        else:
            drop = 0.0
            flag = "⚠️ No holdout data" if holdout_correctness is None else "⚠️ No dev data"

        dev_correctness_str = f"{dev_correctness:.3f}" if dev_correctness is not None else "—"
        holdout_correctness_str = f"{holdout_correctness:.3f}" if holdout_correctness is not None else "—"
        drop_str = f"{drop:+.1f}pp" if (dev_correctness is not None and holdout_correctness is not None) else "—"

        lines.append(
            f"| **{d}** | {dev_d.get('count', '—')} | {dev_correctness_str} "
            f"| {ho_d.get('count', '—')} | {holdout_correctness_str} | {drop_str} | {flag} |"
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
                f"| {r['dev_correctness']:.3f} | {r['holdout_correctness']:.3f} | {r['drop_pp']:+.1f}pp |"
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

    report = {
        "schema_version": 1,
        "passed": not overfit_flags,
        "threshold_pp": OVERFITTING_THRESHOLD_PP,
        "dev_envelope_sha256": hashlib.sha256(dev_path.read_bytes()).hexdigest(),
        "holdout_envelope_sha256": hashlib.sha256(holdout_path.read_bytes()).hexdigest(),
        "flagged_decompilers": overfit_flags,
        "dev": dev_agg,
        "holdout": holdout_agg,
    }
    if json_output_path:
        json_output_path.parent.mkdir(parents=True, exist_ok=True)
        json_output_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def main():
    parser = argparse.ArgumentParser(description="Generate Dev vs Holdout overfitting report")
    parser.add_argument("--dev", required=True, help="Path to dev corpus benchmark JSON")
    parser.add_argument("--holdout", required=True, help="Path to holdout corpus benchmark JSON")
    parser.add_argument("--output", default=None, help="Optional output Markdown path")
    parser.add_argument("--json-output", default=None, help="Machine-readable gate evidence")
    args = parser.parse_args()

    report = generate_report(
        dev_path=Path(args.dev),
        holdout_path=Path(args.holdout),
        output_path=Path(args.output) if args.output else None,
        json_output_path=Path(args.json_output) if args.json_output else None,
    )
    if not report["passed"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
