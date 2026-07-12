"""Official function-discovery (function finding) report.

Aggregates ``function_discovery`` JSONL / BenchmarkResult rows into a
publication-style matrix:

* set match rate (strict address-set equality)
* dual presence recall / precision / F1 / Jaccard
* manifest recall (corpus subject VAs)
* core (fission) vs multi candidates when Ghidra is reference

Distinct from ``same_function_matrix`` (per-function decompile boundary).
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

REPORT_SCHEMA = "function-discovery-report-v1"
# Product under test (publication core). Ghidra as candidate is reference self-check.
CORE_CANDIDATES = frozenset({"fission"})
REFERENCE_CANDIDATES = frozenset({"ghidra"})

CONTRACT = {
    "unit": "binary_variant",
    "request": "GET /functions → inventory list",
    "primary": "normalized address-set equality (ref vs candidate)",
    "dual": [
        "presence_recall = |R∩C|/|R|",
        "presence_precision = |R∩C|/|C|",
        "presence_f1",
        "presence_jaccard",
        "manifest_recall = |manifest∩C|/|manifest|",
    ],
    "references": ["ghidra inventory", "pe_symbols (unstripped)", "manifest VAs"],
    "note": (
        "Function *finding* benchmark. Not the same-function decompile matrix "
        "(binary+addr request contract)."
    ),
}


def _row_dict(row: Any) -> dict[str, Any]:
    if isinstance(row, Mapping):
        return dict(row)
    if is_dataclass(row):
        return asdict(row)
    if hasattr(row, "__dict__"):
        return dict(vars(row))
    raise TypeError(f"unsupported row type: {type(row)!r}")


def build_discovery_report(rows: Iterable[Any]) -> dict[str, Any]:
    """Aggregate discovery rows into by-candidate and cohort tables."""
    by_cand: dict[str, list[dict[str, Any]]] = defaultdict(list)
    n = 0
    for raw in rows:
        row = _row_dict(raw)
        if str(row.get("stage") or "function_discovery") not in {
            "function_discovery",
            "strip_discovery",
            "",
        }:
            # Allow bare rows without stage from dedicated JSONL.
            if row.get("stage") and row.get("stage") != "function_discovery":
                continue
        n += 1
        cand = str(row.get("candidate") or "unknown")
        by_cand[cand].append(row)

    def _agg(tool_rows: list[dict[str, Any]]) -> dict[str, Any]:
        status_counts: dict[str, int] = defaultdict(int)
        mismatch_kinds: dict[str, int] = defaultdict(int)
        recalls: list[float] = []
        precisions: list[float] = []
        f1s: list[float] = []
        jaccards: list[float] = []
        manifest_recalls: list[float] = []
        ref_counts: list[int] = []
        cand_counts: list[int] = []
        scored_modern = 0
        for row in tool_rows:
            st = str(row.get("status") or "unknown")
            status_counts[st] += 1
            mk = row.get("mismatch_kind")
            if mk:
                mismatch_kinds[str(mk)] += 1
            metrics = row.get("metrics") or {}
            if not isinstance(metrics, dict):
                continue
            if metrics.get("scored_as") in {
                "ghidra_inventory",
                "pe_symbol_inventory",
                "manifest_inventory",
            }:
                scored_modern += 1
            if metrics.get("presence_recall") is not None:
                recalls.append(float(metrics["presence_recall"]))
            if metrics.get("presence_precision") is not None:
                precisions.append(float(metrics["presence_precision"]))
            if metrics.get("presence_f1") is not None:
                f1s.append(float(metrics["presence_f1"]))
            if metrics.get("presence_jaccard") is not None:
                jaccards.append(float(metrics["presence_jaccard"]))
            if metrics.get("manifest_recall") is not None:
                manifest_recalls.append(float(metrics["manifest_recall"]))
            if metrics.get("expected_function_count") is not None:
                ref_counts.append(int(metrics["expected_function_count"]))
            if metrics.get("actual_function_count") is not None:
                cand_counts.append(int(metrics["actual_function_count"]))

        match = status_counts.get("match", 0)
        mismatch = status_counts.get("mismatch", 0)
        comparable = match + mismatch
        attempted = len(tool_rows)

        def _mean(xs: list[float]) -> float | None:
            return round(sum(xs) / len(xs), 4) if xs else None

        return {
            "attempted": attempted,
            "match": match,
            "mismatch": mismatch,
            "comparable": comparable,
            "set_match_rate": round(match / comparable, 4) if comparable else None,
            "by_status": dict(sorted(status_counts.items())),
            "by_mismatch_kind": dict(sorted(mismatch_kinds.items())),
            "dual": {
                "n": len(recalls),
                "mean_presence_recall": _mean(recalls),
                "mean_presence_precision": _mean(precisions),
                "mean_presence_f1": _mean(f1s),
                "mean_presence_jaccard": _mean(jaccards),
                "mean_manifest_recall": _mean(manifest_recalls),
                "mean_ref_function_count": (
                    round(sum(ref_counts) / len(ref_counts), 2) if ref_counts else None
                ),
                "mean_cand_function_count": (
                    round(sum(cand_counts) / len(cand_counts), 2)
                    if cand_counts
                    else None
                ),
                "modern_scored_rows": scored_modern,
                "legacy_rows": attempted - scored_modern,
            },
        }

    def _cohort(cand: str) -> str:
        if cand in CORE_CANDIDATES:
            return "core"
        if cand in REFERENCE_CANDIDATES:
            return "reference"
        return "multi"

    by_decompiler: dict[str, Any] = {}
    matrix_rows: list[dict[str, Any]] = []
    for cand in sorted(by_cand):
        stats = _agg(by_cand[cand])
        cohort = _cohort(cand)
        entry = {"candidate": cand, "cohort": cohort, **stats}
        by_decompiler[cand] = entry
        dual = stats["dual"]
        matrix_rows.append(
            {
                "candidate": cand,
                "cohort": cohort,
                "set_match_rate": stats["set_match_rate"],
                "mean_presence_recall": dual["mean_presence_recall"],
                "mean_presence_precision": dual["mean_presence_precision"],
                "mean_presence_f1": dual["mean_presence_f1"],
                "mean_manifest_recall": dual["mean_manifest_recall"],
                "match": stats["match"],
                "mismatch": stats["mismatch"],
                "attempted": stats["attempted"],
            }
        )

    # Cohorts
    cohort_rows: dict[str, list[dict[str, Any]]] = {
        "core": [],
        "reference": [],
        "multi": [],
        "all": [],
    }
    for cand, rows_c in by_cand.items():
        cohort_rows["all"].extend(rows_c)
        cohort_rows[_cohort(cand)].extend(rows_c)

    def _cohort_candidates(name: str) -> list[str]:
        if name == "all":
            return sorted(by_cand)
        if name == "core":
            return sorted(c for c in by_cand if c in CORE_CANDIDATES)
        if name == "reference":
            return sorted(c for c in by_cand if c in REFERENCE_CANDIDATES)
        return sorted(
            c
            for c in by_cand
            if c not in CORE_CANDIDATES and c not in REFERENCE_CANDIDATES
        )

    cohorts = {
        name: {
            "candidates": _cohort_candidates(name),
            **_agg(rows_c),
        }
        for name, rows_c in cohort_rows.items()
    }

    return {
        "schema": REPORT_SCHEMA,
        "contract": CONTRACT,
        "totals": {
            "rows": n,
            "candidates": sorted(by_cand),
        },
        "cohorts": cohorts,
        "by_candidate": by_decompiler,
        "matrix": {"rows": matrix_rows},
    }


def render_markdown(report: Mapping[str, Any]) -> str:
    lines: list[str] = []
    lines.append("# Function discovery benchmark")
    lines.append("")
    lines.append(
        "Unit: **binary variant** · Primary: **address-set equality** vs reference inventory."
    )
    lines.append("")
    lines.append(
        "Dual: `presence_recall` / `precision` / `F1` / `jaccard` + optional `manifest_recall`."
    )
    lines.append("")
    totals = report.get("totals") or {}
    lines.append(
        f"Rows: **{totals.get('rows', 0)}** · Candidates: "
        f"{', '.join(totals.get('candidates') or [])}"
    )
    lines.append("")

    lines.append("## Cohorts")
    lines.append("")
    lines.append(
        "| Cohort | set_match | recall | precision | F1 | manifest_recall | candidates |"
    )
    lines.append(
        "|--------|----------:|-------:|----------:|---:|----------------:|------------|"
    )
    for name in ("core", "reference", "multi", "all"):
        c = (report.get("cohorts") or {}).get(name) or {}
        if not c.get("attempted") and name == "reference":
            continue
        d = c.get("dual") or {}
        lines.append(
            "| {n} | {sm} | {r} | {p} | {f} | {m} | {cands} |".format(
                n=name,
                sm=c.get("set_match_rate"),
                r=d.get("mean_presence_recall"),
                p=d.get("mean_presence_precision"),
                f=d.get("mean_presence_f1"),
                m=d.get("mean_manifest_recall"),
                cands=", ".join(c.get("candidates") or []),
            )
        )
    lines.append("")

    lines.append("## By candidate")
    lines.append("")
    lines.append(
        "| Candidate | Cohort | set_match | recall | precision | F1 | "
        "manifest | match/mismatch | attempted |"
    )
    lines.append(
        "|-----------|--------|----------:|-------:|----------:|---:|"
        "---------:|---------------:|----------:|"
    )
    for row in (report.get("matrix") or {}).get("rows") or []:
        lines.append(
            "| {c} | {co} | {sm} | {r} | {p} | {f} | {m} | {ma}/{mi} | {a} |".format(
                c=row.get("candidate"),
                co=row.get("cohort"),
                sm=row.get("set_match_rate"),
                r=row.get("mean_presence_recall"),
                p=row.get("mean_presence_precision"),
                f=row.get("mean_presence_f1"),
                m=row.get("mean_manifest_recall"),
                ma=row.get("match"),
                mi=row.get("mismatch"),
                a=row.get("attempted"),
            )
        )
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append(
        "- **Strict set match** is rare across tools (CRT / padding / analysis heuristics)."
    )
    lines.append(
        "- Prefer **dual recall/precision** for triage; use set match as inventory equality canary."
    )
    lines.append(
        "- Distinct from **same-function matrix** (decompile `(binary, addr)` boundary)."
    )
    lines.append("")
    return "\n".join(lines)


def load_rows(path: Path) -> list[dict[str, Any]]:
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".jsonl" or text[:1] not in "[{":
        rows = []
        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
        return rows
    data = json.loads(text)
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        return list(data.get("rows") or [])
    raise ValueError(f"unsupported shape in {path}")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Build function-discovery report from JSONL/result rows"
    )
    parser.add_argument("inputs", type=Path, nargs="+", help="JSONL or envelope JSON")
    parser.add_argument("-o", "--output", type=Path, help="Write report JSON")
    parser.add_argument("--markdown", type=Path, help="Write Markdown")
    parser.add_argument(
        "--print", dest="do_print", action="store_true", help="Print Markdown"
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    all_rows: list[dict[str, Any]] = []
    sources: list[str] = []
    for path in args.inputs:
        all_rows.extend(load_rows(path))
        sources.append(str(path))

    report = build_discovery_report(all_rows)
    report["sources"] = sources
    md = render_markdown(report)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote {args.output}")
    if args.markdown:
        args.markdown.parent.mkdir(parents=True, exist_ok=True)
        args.markdown.write_text(md, encoding="utf-8")
        print(f"Wrote {args.markdown}")
    if args.do_print or (not args.output and not args.markdown):
        print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
