#!/usr/bin/env python3
"""
Anti-overfitting oracle for fission-benchmark.

**LEGACY / DIAGNOSTIC:** Gates below still emphasize source similarity and goto
counts from an earlier design. Official publication uses
``runner/holdout_report.py`` (semantic correctness drop ≥10pp) and
``runner/publication_gate.py``. Do not treat this checker as the release gate
until it is rewritten to semantic-first thresholds.

Usage:
  python benchmark/anti_overfit/checker.py \
      --baseline results/baseline.json \
      --candidate results/candidate.json [--decompiler fission]

Exit codes:
  0  All gates pass — candidate may be merged.
  1  One or more gates failed — candidate is rejected (overfitting or regression).

Gates (legacy similarity-era):
  1. Δavg_sim ≥ 0            No average similarity regression.
  2. Δtotal_goto ≤ 0         No increase in total goto count.
  3. regression_count == 0   No individual variant worsens beyond tolerance.
  4. improvement_count ≥ MIN_IMPROVEMENTS  Must improve at least 3 variants.

Overfitting heuristic (when both corpora available):
  If Δavg_sim(dev) > 0 and Δavg_sim(holdout) < -OVERFIT_MARGIN → flag as overfit.
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

# ── Thresholds ──────────────────────────────────────────────────────────────────

# Minimum number of variants that must *improve* for a candidate to be accepted.
# A candidate that fixes only 1 or 2 variants is almost certainly overfitting.
MIN_IMPROVEMENTS = 3

# A variant is considered "regressed" if its similarity drops by more than this.
REGRESSION_TOLERANCE = 0.01

# A variant is considered "improved" if its similarity rises by more than this.
IMPROVEMENT_THRESHOLD = 0.005

# Cross-corpus overfit detection margin.
OVERFIT_MARGIN = 0.01


@dataclass
class VariantResult:
    function_name: str
    compiler_variant: str
    similarity: float
    goto_count: int
    error: Optional[str]

    @property
    def key(self) -> str:
        return f"{self.function_name}@{self.compiler_variant}"


@dataclass
class GateResult:
    name: str
    passed: bool
    detail: str


@dataclass
class OracleResult:
    corpus: str
    delta_sim: float
    delta_goto: int
    regressions: list
    improvements: list
    gates: list = field(default_factory=list)

    @property
    def verdict(self) -> str:
        return "PASS" if all(g.passed for g in self.gates) else "FAIL"


def load_variants(path: Path, decompiler: str) -> dict:
    rows = json.loads(path.read_text())
    out = {}
    for r in rows:
        if r.get("decompiler") != decompiler:
            continue
        v = VariantResult(
            function_name=r["function_name"],
            compiler_variant=r["compiler_variant"],
            similarity=r.get("source_similarity", 0.0),
            goto_count=r.get("goto_count", 0),
            error=r.get("error"),
        )
        out[v.key] = v
    return out


def check_delta(baseline: dict, candidate: dict, corpus: str) -> OracleResult:
    sims_base = [v.similarity for v in baseline.values()]
    sims_cand = [candidate[k].similarity for k in baseline if k in candidate]
    avg_sim_base = sum(sims_base) / len(sims_base) if sims_base else 0.0
    avg_sim_cand = sum(sims_cand) / len(sims_cand) if sims_cand else 0.0
    delta_sim = avg_sim_cand - avg_sim_base

    total_goto_base = sum(v.goto_count for v in baseline.values())
    total_goto_cand = sum(candidate[k].goto_count for k in baseline if k in candidate)
    delta_goto = total_goto_cand - total_goto_base

    regressions, improvements = [], []
    for key in set(baseline) | set(candidate):
        b = baseline.get(key)
        c = candidate.get(key)
        if b is None or c is None:
            continue
        if c.error:
            regressions.append(f"{key} [error: {c.error}]")
            continue
        diff = c.similarity - b.similarity
        if diff < -REGRESSION_TOLERANCE:
            regressions.append(f"{key}: {b.similarity:.3f}→{c.similarity:.3f} ({diff:+.3f})")
        elif diff > IMPROVEMENT_THRESHOLD:
            improvements.append(f"{key}: {b.similarity:.3f}→{c.similarity:.3f} ({diff:+.3f})")

    gates = [
        GateResult("no_avg_regression",  delta_sim >= -1e-6,
                   f"Δavg_sim={delta_sim:+.4f} (required ≥ 0)"),
        GateResult("no_goto_increase",   delta_goto <= 0,
                   f"Δtotal_goto={delta_goto:+d} (required ≤ 0)"),
        GateResult("zero_regressions",   len(regressions) == 0,
                   f"{len(regressions)} regression(s): {regressions[:3]}"),
        GateResult("min_improvements",   len(improvements) >= MIN_IMPROVEMENTS,
                   f"{len(improvements)} improvement(s) ≥ {MIN_IMPROVEMENTS} required. "
                   + (f"Top: {improvements[:3]}" if improvements else "none")),
    ]
    return OracleResult(corpus, delta_sim, delta_goto, regressions, improvements, gates)


def print_result(result: OracleResult) -> None:
    icon = "✅" if result.verdict == "PASS" else "❌"
    print(f"\n{icon} [{result.corpus}] verdict: {result.verdict}")
    print(f"   Δavg_sim={result.delta_sim:+.4f}  Δgoto={result.delta_goto:+d}  "
          f"improved={len(result.improvements)}  regressed={len(result.regressions)}")
    for gate in result.gates:
        print(f"  {'✅' if gate.passed else '❌'} {gate.name}: {gate.detail}")
    if result.regressions:
        print("  Regressed:", result.regressions)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline",  required=True, type=Path)
    parser.add_argument("--candidate", required=True, type=Path)
    parser.add_argument("--decompiler", default="fission")
    parser.add_argument("--holdout", type=Path, default=None)
    parser.add_argument("--holdout-baseline", type=Path, default=None)
    args = parser.parse_args()

    baseline  = load_variants(args.baseline,  args.decompiler)
    candidate = load_variants(args.candidate, args.decompiler)
    if not baseline or not candidate:
        print("ERROR: no rows found", file=sys.stderr)
        return 1

    result = check_delta(baseline, candidate, "dev")
    print_result(result)
    overall = result.verdict == "PASS"

    if args.holdout and args.holdout_baseline:
        hb = load_variants(args.holdout_baseline, args.decompiler)
        hc = load_variants(args.holdout, args.decompiler)
        hr = check_delta(hb, hc, "holdout")
        print_result(hr)
        if result.delta_sim > 0 and hr.delta_sim < -OVERFIT_MARGIN:
            print(f"\n❌ OVERFIT: dev+{result.delta_sim:.4f} but holdout{hr.delta_sim:.4f}")
            overall = False

    print()
    if overall:
        print("✅ All gates passed — candidate may be merged.")
        return 0
    print("❌ Gate(s) failed — candidate rejected.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
