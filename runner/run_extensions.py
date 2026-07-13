#!/usr/bin/env python3
"""Run all extension parity stages (ABI, types, callgraph, strings, dataflow, seh, …)."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from benchmark.abi_parity.run import compare_abi
from benchmark.callgraph_parity.run import compare_callgraph
from benchmark.common.http_providers import ensure_fission_port, fetch_parity_json
from benchmark.common.schema import BenchmarkSubject
from benchmark.common.subjects import load_subjects
from benchmark.dataflow_parity.run import compare_dataflow
from benchmark.metadata_parity.run import compare_metadata
from benchmark.seh_parity.run import compare_seh
from benchmark.string_recovery.run import compare_strings
from benchmark.telemetry.aggregate import aggregate_rows
from benchmark.type_parity.run import compare_types

STAGES = [
    ("metadata_parity", compare_metadata, True),
    ("abi_parity", compare_abi, False),
    ("type_parity", compare_types, False),
    ("callgraph_parity", compare_callgraph, False),
    ("string_recovery", compare_strings, False),
    ("dataflow_parity", compare_dataflow, False),
    ("seh_parity", compare_seh, False),
]


def _unique_binary_subjects(
    subjects: list[BenchmarkSubject],
) -> list[BenchmarkSubject]:
    seen = set()
    rows = []
    for subject in subjects:
        if subject.binary in seen:
            continue
        seen.add(subject.binary)
        rows.append(
            BenchmarkSubject(
                binary=subject.binary,
                function="(metadata)",
                addr="0x0",
                arch=subject.arch,
                compiler=subject.compiler,
                opt=subject.opt,
                corpus_split=subject.corpus_split,
            )
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", default="dev")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--timeout", type=float, default=90.0)
    parser.add_argument("--output-dir", type=Path, default=Path("results"))
    args = parser.parse_args()

    ensure_fission_port()
    subjects = load_subjects(args.corpus)
    if args.limit is not None:
        subjects = subjects[: args.limit]

    all_rows: list[dict] = []
    for stage, compare, once_per_binary in STAGES:
        rows = []
        stage_subjects = _unique_binary_subjects(subjects) if once_per_binary else subjects
        for subject in stage_subjects:
            try:
                try:
                    exp = fetch_parity_json("ghidra", stage, subject, timeout=args.timeout)
                except Exception as exc:
                    exp = {"status": "error", "error": str(exc)}
                try:
                    act = fetch_parity_json("fission", stage, subject, timeout=args.timeout)
                except Exception as exc:
                    act = {"status": "error", "error": str(exc)}
                result = compare(subject, "ghidra", "fission", exp, act)
            except Exception as exc:
                from benchmark.common.schema import BenchmarkResult

                result = BenchmarkResult(
                    subject=subject,
                    stage=stage,  # type: ignore[arg-type]
                    status="error",
                    reference="ghidra",
                    candidate="fission",
                    error=str(exc),
                )
            row = {
                "subject": {
                    "binary": result.subject.binary,
                    "function": result.subject.function,
                    "addr": result.subject.addr,
                    "arch": result.subject.arch,
                    "compiler": result.subject.compiler,
                    "opt": result.subject.opt,
                },
                "stage": result.stage,
                "status": result.status,
                "reference": result.reference,
                "candidate": result.candidate,
                "mismatch_kind": result.mismatch_kind,
                "error": result.error,
                "metrics": result.metrics,
            }
            rows.append(row)
            all_rows.append(row)
        out = args.output_dir / stage / "latest.jsonl"
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w", encoding="utf-8") as fh:
            for r in rows:
                fh.write(json.dumps(r) + "\n")
        matched = sum(1 for r in rows if r["status"] == "match")
        print(f"{stage}: {matched}/{len(rows)} match → {out}")

    summary = aggregate_rows(all_rows)
    tel = args.output_dir / "telemetry" / "extensions_latest.json"
    tel.parent.mkdir(parents=True, exist_ok=True)
    tel.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"extension telemetry → {tel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
