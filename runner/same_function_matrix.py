"""Same-function matrix: official infra axis for multi-decompiler honesty.

Request contract
----------------
Each result row is one request ``(binary, addr)`` (function entry VA).  The
benchmark asks every decompiler for **that** function — not a whole-program
dump (cf. Dogbolt / decompiler-explorer).

Diagnostic statuses (from ``output_diagnostics.status``)
--------------------------------------------------------
* ``direct_function``       — single target-like unit with name and/or address
* ``needs_normalization``   — target-like but soft harness blockers remain
* ``boundary_mismatch``     — output is not the requested function
* ``whole_program_output``  — multi-function / truncated dump
* ``no_output``             — empty or sentinel adapter output

Primary rate (publication auxiliary)
------------------------------------
::

    same_function_rate =
        direct_function
        / (direct_function + boundary_*)

where ``boundary_*`` =
``boundary_mismatch ∪ whole_program_output ∪ no_output``.

``needs_normalization`` is reported separately and included only in the
**loose** rate (secondary):

::

    same_function_loose_rate =
        (direct_function + needs_normalization)
        / (direct_function + needs_normalization + boundary_*)

Cohorts
-------
* **core** — fission, ghidra (publication / validity core)
* **multi** — all other adapters in the run
* **all** — every decompiler present
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

MATRIX_SCHEMA = "same-function-matrix-v1"

CORE_DECOMPILERS = frozenset({"fission", "ghidra"})

# Status taxonomy for the same-function contract.
STATUS_DIRECT = "direct_function"
STATUS_NEEDS_NORM = "needs_normalization"
STATUS_BOUNDARY = "boundary_mismatch"
STATUS_WHOLE = "whole_program_output"
STATUS_NO_OUTPUT = "no_output"
STATUS_UNKNOWN = "unknown"

BOUNDARY_STATUSES = frozenset({STATUS_BOUNDARY, STATUS_WHOLE, STATUS_NO_OUTPUT})
SAME_OK_STRICT = frozenset({STATUS_DIRECT})
SAME_OK_LOOSE = frozenset({STATUS_DIRECT, STATUS_NEEDS_NORM})

ALL_STATUSES = (
    STATUS_DIRECT,
    STATUS_NEEDS_NORM,
    STATUS_BOUNDARY,
    STATUS_WHOLE,
    STATUS_NO_OUTPUT,
    STATUS_UNKNOWN,
)

CONTRACT = {
    "request": "(binary, addr)",
    "description": (
        "Each row is one decompile request for a single function entry. "
        "Success means the adapter returned that function unit, not a "
        "whole-program dump (DCE/Dogbolt-style)."
    ),
    "statuses": list(ALL_STATUSES),
    "boundary_statuses": sorted(BOUNDARY_STATUSES),
    "same_function_rate": (
        "direct_function / (direct_function + boundary_mismatch "
        "+ whole_program_output + no_output)"
    ),
    "same_function_loose_rate": (
        "(direct_function + needs_normalization) / "
        "(direct_function + needs_normalization + boundary_*)"
    ),
    "core_decompilers": sorted(CORE_DECOMPILERS),
}


def classify_row_status(row: Mapping[str, Any]) -> str:
    """Map a result row to a same-function status bucket."""
    diagnostics = row.get("output_diagnostics") or {}
    status = str(diagnostics.get("status") or "").strip()
    if status in {
        STATUS_DIRECT,
        STATUS_NEEDS_NORM,
        STATUS_BOUNDARY,
        STATUS_WHOLE,
        STATUS_NO_OUTPUT,
    }:
        return status
    # No diagnostics: treat empty/error adapter outcomes as no_output.
    error = row.get("error")
    code = (row.get("code") or row.get("decompiled_code") or "").strip()
    if error or not code:
        return STATUS_NO_OUTPUT
    return STATUS_UNKNOWN


def _empty_status_counts() -> dict[str, int]:
    return {status: 0 for status in ALL_STATUSES}


def _rates_from_counts(counts: Mapping[str, int]) -> dict[str, Any]:
    direct = int(counts.get(STATUS_DIRECT) or 0)
    needs = int(counts.get(STATUS_NEEDS_NORM) or 0)
    boundary = sum(int(counts.get(s) or 0) for s in BOUNDARY_STATUSES)
    strict_den = direct + boundary
    loose_den = direct + needs + boundary
    classified = sum(int(counts.get(s) or 0) for s in ALL_STATUSES)
    return {
        "direct_function": direct,
        "needs_normalization": needs,
        "boundary_star": boundary,
        "same_function_rate": (
            round(direct / strict_den, 4) if strict_den else None
        ),
        "same_function_loose_rate": (
            round((direct + needs) / loose_den, 4) if loose_den else None
        ),
        "classified_rows": classified,
        "strict_denominator": strict_den,
        "loose_denominator": loose_den,
    }


def _cohort_for(decompiler: str) -> str:
    return "core" if decompiler in CORE_DECOMPILERS else "multi"


def build_same_function_matrix(
    rows: Iterable[Mapping[str, Any]],
    *,
    core_decompilers: frozenset[str] = CORE_DECOMPILERS,
) -> dict[str, Any]:
    """Build the same-function matrix block from result rows."""
    by_decompiler_counts: dict[str, dict[str, int]] = defaultdict(_empty_status_counts)
    cohort_counts: dict[str, dict[str, int]] = {
        "core": _empty_status_counts(),
        "multi": _empty_status_counts(),
        "all": _empty_status_counts(),
    }
    # Pivot: decompiler × function_name status mode (majority) + counts
    cell: dict[tuple[str, str], dict[str, int]] = defaultdict(_empty_status_counts)
    # Address-anchor evidence among classified rows
    addr_hits = 0
    name_hits = 0
    diag_rows = 0

    decompilers_seen: set[str] = set()
    n_rows = 0

    for row in rows:
        n_rows += 1
        decompiler = str(row.get("decompiler") or "unknown")
        decompilers_seen.add(decompiler)
        status = classify_row_status(row)
        by_decompiler_counts[decompiler][status] += 1
        cohort = "core" if decompiler in core_decompilers else "multi"
        cohort_counts[cohort][status] += 1
        cohort_counts["all"][status] += 1

        fn = str(row.get("function_name") or row.get("function") or "?")
        cell[(decompiler, fn)][status] += 1

        diagnostics = row.get("output_diagnostics") or {}
        if diagnostics:
            diag_rows += 1
            if diagnostics.get("expected_address_present"):
                addr_hits += 1
            if diagnostics.get("target_name_present"):
                name_hits += 1

    by_decompiler: dict[str, Any] = {}
    matrix_rows: list[dict[str, Any]] = []
    for decompiler in sorted(by_decompiler_counts):
        counts = by_decompiler_counts[decompiler]
        rates = _rates_from_counts(counts)
        entry = {
            "decompiler": decompiler,
            "cohort": "core" if decompiler in core_decompilers else "multi",
            "by_status": dict(counts),
            **rates,
        }
        by_decompiler[decompiler] = entry
        matrix_rows.append(
            {
                "decompiler": decompiler,
                "cohort": entry["cohort"],
                **{s: counts[s] for s in ALL_STATUSES},
                "same_function_rate": rates["same_function_rate"],
                "same_function_loose_rate": rates["same_function_loose_rate"],
            }
        )

    cohorts: dict[str, Any] = {}
    for name, counts in cohort_counts.items():
        rates = _rates_from_counts(counts)
        cohorts[name] = {
            "by_status": dict(counts),
            **rates,
            "decompilers": sorted(
                d
                for d in decompilers_seen
                if (
                    name == "all"
                    or (name == "core" and d in core_decompilers)
                    or (name == "multi" and d not in core_decompilers)
                )
            ),
        }

    # Compact function × decompiler matrix: only functions with ≥1 non-direct
    # or all functions with status summary string per decompiler.
    functions = sorted({fn for (_, fn) in cell})
    function_matrix: list[dict[str, Any]] = []
    for fn in functions:
        entry: dict[str, Any] = {"function_name": fn, "by_decompiler": {}}
        for decompiler in sorted(decompilers_seen):
            counts = cell.get((decompiler, fn))
            if not counts or sum(counts.values()) == 0:
                continue
            # Dominant status
            dominant = max(ALL_STATUSES, key=lambda s: (counts[s], s == STATUS_DIRECT))
            if counts[dominant] == 0:
                dominant = STATUS_UNKNOWN
            entry["by_decompiler"][decompiler] = {
                "by_status": {s: counts[s] for s in ALL_STATUSES if counts[s]},
                "dominant": dominant,
                "same_function": dominant in SAME_OK_STRICT,
            }
        if entry["by_decompiler"]:
            function_matrix.append(entry)

    return {
        "schema": MATRIX_SCHEMA,
        "contract": CONTRACT,
        "totals": {
            "rows": n_rows,
            "decompilers": sorted(decompilers_seen),
            "core_decompilers": sorted(core_decompilers & decompilers_seen),
            "multi_decompilers": sorted(decompilers_seen - core_decompilers),
            "rows_with_diagnostics": diag_rows,
            "address_anchor_rate": (
                round(addr_hits / diag_rows, 4) if diag_rows else None
            ),
            "name_anchor_rate": (
                round(name_hits / diag_rows, 4) if diag_rows else None
            ),
        },
        "cohorts": cohorts,
        "by_decompiler": by_decompiler,
        "matrix": {
            "status_columns": list(ALL_STATUSES),
            "rows": matrix_rows,
        },
        "by_function": function_matrix,
    }


def render_markdown(matrix: Mapping[str, Any]) -> str:
    """Human-readable Markdown report for CI / publication appendix."""
    lines: list[str] = []
    lines.append("# Same-function matrix")
    lines.append("")
    lines.append("Request contract: **`(binary, addr)`** — one function entry per row.")
    lines.append("")
    lines.append(
        "Primary rate: `same_function_rate = direct_function / "
        "(direct_function + boundary_*)`"
    )
    lines.append("")
    lines.append(
        "where `boundary_*` = `boundary_mismatch` ∪ `whole_program_output` ∪ `no_output`."
    )
    lines.append("")

    totals = matrix.get("totals") or {}
    lines.append("## Totals")
    lines.append("")
    lines.append(f"- Rows: **{totals.get('rows', 0)}**")
    lines.append(f"- Decompilers: {', '.join(totals.get('decompilers') or [])}")
    lines.append(
        f"- Address anchor rate (among rows with diagnostics): "
        f"**{totals.get('address_anchor_rate')}**"
    )
    lines.append("")

    lines.append("## Cohorts (core vs multi)")
    lines.append("")
    lines.append(
        "| Cohort | direct | needs_norm | boundary_* | same_function_rate | loose_rate | decompilers |"
    )
    lines.append(
        "|--------|-------:|-----------:|-----------:|-------------------:|-----------:|-------------|"
    )
    for name in ("core", "multi", "all"):
        c = (matrix.get("cohorts") or {}).get(name) or {}
        st = c.get("by_status") or {}
        boundary = sum(int(st.get(s) or 0) for s in BOUNDARY_STATUSES)
        lines.append(
            "| {name} | {d} | {n} | {b} | {r} | {lr} | {tools} |".format(
                name=name,
                d=st.get(STATUS_DIRECT, 0),
                n=st.get(STATUS_NEEDS_NORM, 0),
                b=boundary,
                r=c.get("same_function_rate"),
                lr=c.get("same_function_loose_rate"),
                tools=", ".join(c.get("decompilers") or []),
            )
        )
    lines.append("")

    lines.append("## By decompiler")
    lines.append("")
    lines.append(
        "| Decompiler | Cohort | direct | needs_norm | boundary | whole | no_out | "
        "same_fn_rate | loose_rate |"
    )
    lines.append(
        "|------------|--------|-------:|-----------:|---------:|------:|-------:|"
        "-------------:|-----------:|"
    )
    for row in (matrix.get("matrix") or {}).get("rows") or []:
        lines.append(
            "| {dec} | {coh} | {d} | {n} | {b} | {w} | {no} | {r} | {lr} |".format(
                dec=row.get("decompiler"),
                coh=row.get("cohort"),
                d=row.get(STATUS_DIRECT, 0),
                n=row.get(STATUS_NEEDS_NORM, 0),
                b=row.get(STATUS_BOUNDARY, 0),
                w=row.get(STATUS_WHOLE, 0),
                no=row.get(STATUS_NO_OUTPUT, 0),
                r=row.get("same_function_rate"),
                lr=row.get("same_function_loose_rate"),
            )
        )
    lines.append("")

    lines.append("## Notes")
    lines.append("")
    lines.append(
        "- **Core** (fission, ghidra) is the publication-proven cohort; "
        "**multi** is matrix width / adapter honesty."
    )
    lines.append(
        "- This axis is **not** a semantic pass-rate substitute — it proves "
        "whether tools decompiled the **requested** function."
    )
    lines.append(
        "- Dogbolt/DCE whole-program dumps are intentionally out of contract."
    )
    lines.append("")
    return "\n".join(lines)


def matrix_from_envelope(envelope: Mapping[str, Any]) -> dict[str, Any]:
    rows = list(envelope.get("rows") or [])
    matrix = build_same_function_matrix(rows)
    run = envelope.get("run") or {}
    matrix["run"] = {
        "run_id": run.get("run_id"),
        "corpus": run.get("corpus"),
        "official": run.get("official"),
        "profile": run.get("profile") or run.get("run_mode"),
    }
    return matrix


def load_rows_from_path(path: Path) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Load rows + envelope stub from a result JSON (v2 envelope or flat list)."""
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return list(data), {"rows": data, "run": {}}
    if isinstance(data, dict):
        rows = data.get("rows")
        if rows is None and isinstance(data.get("scores"), list):
            rows = data["scores"]
        return list(rows or []), data
    raise ValueError(f"Unsupported result shape in {path}")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Build same-function matrix report from a benchmark result JSON "
            "(request contract: binary+addr)."
        )
    )
    parser.add_argument(
        "results",
        type=Path,
        nargs="+",
        help="One or more result envelope JSON files",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Write JSON matrix (single input) or combined report",
    )
    parser.add_argument(
        "--markdown",
        type=Path,
        help="Write Markdown summary",
    )
    parser.add_argument(
        "--print",
        dest="do_print",
        action="store_true",
        help="Print Markdown to stdout",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    reports: list[dict[str, Any]] = []
    for path in args.results:
        rows, envelope = load_rows_from_path(path)
        matrix = build_same_function_matrix(rows)
        run = envelope.get("run") or {}
        matrix["source"] = str(path)
        matrix["run"] = {
            "run_id": run.get("run_id"),
            "corpus": run.get("corpus"),
            "official": run.get("official"),
        }
        reports.append(matrix)

    if len(reports) == 1:
        payload: Any = reports[0]
        md = render_markdown(reports[0])
    else:
        payload = {
            "schema": MATRIX_SCHEMA,
            "contract": CONTRACT,
            "reports": reports,
        }
        md_parts = [render_markdown(r) for r in reports]
        md = "\n---\n\n".join(md_parts)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
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
