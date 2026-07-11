"""Shared run-validity engine for the Fission benchmark.

This module is the single source of truth for whether a benchmark run is
considered VALID.  It is used by:

* ``runner/runner.py``        -- to embed validity into the result envelope
* ``runner/render_report.py`` -- to re-evaluate validity when rendering
* ``runner/report.py``        -- to render the VALID/INVALID banner
* ``.github/workflows/benchmark.yml`` -- via ``python -m runner.run_validity``

Public API
----------
``is_output_failure(row)``  -- True when a row failed at the adapter/output layer
``evaluate_run(result)``    -- returns a :class:`RunValidity` dataclass
``RunValidity``             -- frozen dataclass with .valid, .fission, .overall, .reasons
``Coverage``                -- frozen dataclass with .attempted, .clean, .ratio
``LoadedResult``            -- dataclass containing rows, envelope, and legacy flag

CLI usage (from benchmark.yml)
-------------------------------
    python -m runner.run_validity results/dev_latest.json \
        --github-env   "$GITHUB_ENV" \
        --github-summary "$GITHUB_STEP_SUMMARY"

Exit code 0 = VALID, 1 = INVALID.
"""
from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Optional

# ---------------------------------------------------------------------------
# Thresholds
# ---------------------------------------------------------------------------

#: Minimum fraction of Fission rows that must have no output error.
FISSION_MIN_COVERAGE: float = 0.90

#: Minimum fraction of ALL rows (across all backends) with no output error.
BACKEND_MIN_COVERAGE: float = 0.90


# ---------------------------------------------------------------------------
# Core data types
# ---------------------------------------------------------------------------


@dataclass
class LoadedResult:
    """Result loaded from JSON, preserving envelope structure."""
    rows: list[dict]
    envelope: Optional[dict]
    legacy: bool


@dataclass(frozen=True)
class Coverage:
    """Per-group adapter/output coverage statistics."""

    attempted: int
    """Total rows attempted (including errors)."""

    clean: int
    """Rows that have no output error (``is_output_failure`` returns False)."""

    ratio: float
    """``clean / attempted`` (0.0 when attempted == 0)."""


@dataclass(frozen=True)
class RunValidity:
    """Result of :func:`evaluate_run`."""

    valid: bool
    """True when all coverage thresholds are met and the run is publishable."""

    fission: Coverage
    """Fission-specific coverage."""

    overall: Coverage
    """Coverage across all backends including Fission."""

    reasons: tuple
    """Machine-readable failure codes when ``valid`` is False.

    Possible values:
    * ``"no_fission_rows"``
    * ``"fission_coverage_below_threshold"``
    * ``"no_result_rows"``
    * ``"backend_coverage_below_threshold"``
    * ``"backend_missing"``
    * ``"matrix_completeness_mismatch"``
    * ``"matrix_missing_cells"``
    * ``"matrix_unexpected_cells"``
    * ``"matrix_duplicate_cells"``
    * ``"legacy_flat_list"``
    * ``"legacy_source"``
    * ``"non_official_run"``
    """

    def summary_line(self) -> str:
        """One-line human-readable summary for GITHUB_STEP_SUMMARY / logs."""
        if self.valid:
            return (
                f"VALID -- Fission {self.fission.clean}/{self.fission.attempted} "
                f"({self.fission.ratio * 100:.1f}%), "
                f"all-backend {self.overall.clean}/{self.overall.attempted} "
                f"({self.overall.ratio * 100:.1f}%)"
            )
        return (
            f"INVALID [{', '.join(self.reasons)}] -- "
            f"Fission {self.fission.clean}/{self.fission.attempted} "
            f"({self.fission.ratio * 100:.1f}%), "
            f"all-backend {self.overall.clean}/{self.overall.attempted} "
            f"({self.overall.ratio * 100:.1f}%)"
        )


# ---------------------------------------------------------------------------
# Core logic
# ---------------------------------------------------------------------------


def is_output_failure(row: Mapping[str, Any]) -> bool:
    """Return True when a result row failed at the adapter/output layer."""
    return bool(row.get("error")) or row.get("fail_category") == "adapter_error"


def evaluate_run(
    result: LoadedResult | Iterable[Mapping[str, Any]],
    *,
    legacy: bool = False,
) -> RunValidity:
    """Evaluate whether a benchmark run meets publishability thresholds.

    Parameters
    ----------
    result:
        A LoadedResult containing envelope and rows, or an Iterable of result-row dicts.
    legacy:
        If result is an Iterable, this marks whether it is legacy. If result is
        LoadedResult, the legacy flag on LoadedResult takes precedence.
    """
    if isinstance(result, LoadedResult):
        rows = list(result.rows)
        is_legacy = result.legacy
        envelope = result.envelope
    else:
        rows = list(result)
        is_legacy = legacy
        envelope = None

    def _coverage(items):
        attempted = len(items)
        clean = sum(1 for r in items if not is_output_failure(r))
        ratio = clean / attempted if attempted else 0.0
        return Coverage(attempted=attempted, clean=clean, ratio=ratio)

    fission_rows = [r for r in rows if r.get("decompiler") == "fission"]
    fission_cov = _coverage(fission_rows)
    overall_cov = _coverage(rows)

    reasons = []

    if is_legacy:
        reasons.append("legacy_flat_list")
        return RunValidity(
            valid=False,
            fission=fission_cov,
            overall=overall_cov,
            reasons=tuple(reasons),
        )

    run_meta = envelope.get("run", {}) if envelope else {}
    if run_meta.get("legacy_source"):
        reasons.append("legacy_source")
    if run_meta.get("official") is False:
        reasons.append("non_official_run")

    matrix = envelope.get("matrix", {}) if envelope else {}
    expected_rows = matrix.get("expected_rows")
    expected_decompilers = matrix.get("expected_decompilers")
    expected_functions_list = matrix.get("expected_functions_list")
    expected_variants_list = matrix.get("expected_variants_list")

    if expected_rows is not None and len(rows) != expected_rows:
        reasons.append("matrix_completeness_mismatch")

    if expected_decompilers and expected_functions_list and expected_variants_list:
        expected_cells = set()
        for d in expected_decompilers:
            for f in expected_functions_list:
                for v in expected_variants_list:
                    expected_cells.add((d, f, v))

        observed_cells = set()
        duplicates = set()
        for r in rows:
            d = r.get("decompiler")
            f = r.get("function_name")
            v = r.get("compiler_variant")
            if d and f and v:
                cell = (d, f, v)
                if cell in observed_cells:
                    duplicates.add(cell)
                observed_cells.add(cell)

        missing_cells = expected_cells - observed_cells
        unexpected_cells = observed_cells - expected_cells
        
        if missing_cells:
            reasons.append("matrix_missing_cells")
        if unexpected_cells:
            reasons.append("matrix_unexpected_cells")
        if duplicates:
            reasons.append("matrix_duplicate_cells")

    if not fission_cov.attempted:
        reasons.append("no_fission_rows")
    elif fission_cov.ratio < FISSION_MIN_COVERAGE:
        reasons.append("fission_coverage_below_threshold")

    if expected_decompilers:
        for d in expected_decompilers:
            d_rows = [r for r in rows if r.get("decompiler") == d]
            if not d_rows:
                if "backend_missing" not in reasons:
                    reasons.append("backend_missing")
            else:
                d_cov = _coverage(d_rows)
                if d_cov.ratio < BACKEND_MIN_COVERAGE:
                    if "backend_coverage_below_threshold" not in reasons:
                        reasons.append("backend_coverage_below_threshold")
    else:
        # Fallback if no matrix provided
        if not overall_cov.attempted:
            reasons.append("no_result_rows")
        elif overall_cov.ratio < BACKEND_MIN_COVERAGE:
            reasons.append("backend_coverage_below_threshold")

    return RunValidity(
        valid=not reasons,
        fission=fission_cov,
        overall=overall_cov,
        reasons=tuple(reasons),
    )


# ---------------------------------------------------------------------------
# Envelope helpers
# ---------------------------------------------------------------------------


def load_result_file(path: Path) -> LoadedResult:
    """Load a result JSON file and return a LoadedResult.

    Supports envelope format (schema_version >= 2) and legacy flat-list.
    """
    raw = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(raw, list):
        return LoadedResult(rows=raw, envelope=None, legacy=True)
    if isinstance(raw, dict):
        if raw.get("schema_version") != 2:
            raise ValueError(f"Unsupported or missing schema_version in {path}")
        if not isinstance(raw.get("rows"), list):
            raise ValueError(f"Envelope rows must be a list in {path}")
        return LoadedResult(rows=raw["rows"], envelope=raw, legacy=False)
    raise ValueError(
        f"Unrecognised result format in {path}: "
        f"expected a list or an envelope dict with 'rows'."
    )


def build_envelope(
    rows,
    *,
    run_meta=None,
    toolchain=None,
    matrix=None,
):
    """Wrap flat rows in the v2 envelope format."""
    import time as _time

    # Temporarily construct an envelope dict so evaluate_run can check matrix
    temp_envelope = {
        "schema_version": 2,
        "run": run_meta or {},
        "toolchain": toolchain or {},
        "matrix": matrix or {},
        "rows": rows,
    }
    
    loaded = LoadedResult(rows=rows, envelope=temp_envelope, legacy=False)
    validity = evaluate_run(loaded)

    temp_envelope["validity"] = {
        "valid": validity.valid,
        "fission_coverage": round(validity.fission.ratio, 4),
        "fission_attempted": validity.fission.attempted,
        "fission_clean": validity.fission.clean,
        "backend_coverage": round(validity.overall.ratio, 4),
        "backend_attempted": validity.overall.attempted,
        "backend_clean": validity.overall.clean,
        "reasons": list(validity.reasons),
    }
    temp_envelope["rendered_at"] = _time.strftime("%Y-%m-%dT%H:%M:%SZ", _time.gmtime())
    
    return temp_envelope


# ---------------------------------------------------------------------------
# CLI entry point (used from benchmark.yml)
# ---------------------------------------------------------------------------


def _write_line(path, text):
    if path:
        with open(path, "a", encoding="utf-8") as f:
            f.write(text + "\n")


def main(argv=None):
    """CLI: evaluate a result JSON and exit 0 (VALID) or 1 (INVALID)."""
    import argparse

    parser = argparse.ArgumentParser(
        prog="python -m runner.run_validity",
        description="Evaluate benchmark run validity.",
    )
    parser.add_argument("result_json", type=Path, help="Path to result JSON file")
    parser.add_argument("--github-env", default=None)
    parser.add_argument("--github-summary", default=None)
    parser.add_argument(
        "--fission-min-coverage", type=float, default=FISSION_MIN_COVERAGE
    )
    parser.add_argument(
        "--backend-min-coverage", type=float, default=BACKEND_MIN_COVERAGE
    )
    args = parser.parse_args(argv)

    try:
        loaded = load_result_file(args.result_json)
    except Exception as exc:
        print(f"::error::Cannot read {args.result_json}: {exc}", file=sys.stderr)
        return 1

    # Allow threshold overrides
    import runner.run_validity as _self
    _self.FISSION_MIN_COVERAGE = args.fission_min_coverage
    _self.BACKEND_MIN_COVERAGE = args.backend_min_coverage

    verdict = evaluate_run(loaded)
    summary = verdict.summary_line()
    print(summary)

    env_val = "true" if verdict.valid else "false"
    _write_line(args.github_env, f"FISSION_RUN_VALID={env_val}")

    if verdict.valid:
        _write_line(args.github_summary, f"\n## VALID Fission Gate: {summary}\n")
    else:
        for reason in verdict.reasons:
            _write_line(
                args.github_summary,
                f"\n## INVALID RUN [{reason}]\n\n{summary}\n",
            )
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
