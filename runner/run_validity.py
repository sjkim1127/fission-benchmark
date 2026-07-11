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
``evaluate_run(rows)``      -- returns a :class:`RunValidity` dataclass
``RunValidity``             -- frozen dataclass with .valid, .fission, .overall, .reasons
``Coverage``                -- frozen dataclass with .attempted, .clean, .ratio

CLI usage (from benchmark.yml)
-------------------------------
    python -m runner.run_validity results/dev_latest.json \\
        --github-env   "$GITHUB_ENV" \\
        --github-summary "$GITHUB_STEP_SUMMARY"

Exit code 0 = VALID, 1 = INVALID.
"""
from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping

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
    * ``"no_fission_rows"``                -- no Fission rows in results
    * ``"fission_coverage_below_threshold"`` -- Fission < FISSION_MIN_COVERAGE
    * ``"no_result_rows"``                 -- result set is empty
    * ``"backend_coverage_below_threshold"`` -- overall < BACKEND_MIN_COVERAGE
    * ``"legacy_flat_list"``               -- result loaded from legacy format
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
    """Return True when a result row failed at the adapter/output layer.

    Any non-null ``error`` field -- from the adapter, CLI, HTTP layer, address
    resolution, or result post-processing -- means the row did not produce
    usable output.

    ``fail_category == "adapter_error"`` is also treated as a failure even if
    ``error`` is somehow absent (defensive).

    Semantic-level failures (``fail_category`` in ``compile_error``,
    ``runtime_error``, ``timeout``, ``no_wrapper``) are intentionally NOT
    treated as output failures -- the decompiler returned code; it just did not
    compile or pass tests.
    """
    return bool(row.get("error")) or row.get("fail_category") == "adapter_error"


def evaluate_run(
    rows: Iterable[Mapping[str, Any]],
    *,
    legacy: bool = False,
) -> RunValidity:
    """Evaluate whether a benchmark run meets publishability thresholds.

    Parameters
    ----------
    rows:
        Iterable of result-row dicts (the ``"rows"`` field in envelope format,
        or the flat list in legacy format).
    legacy:
        When True the run is marked with ``"legacy_flat_list"`` reason and
        ``valid`` is always False, regardless of coverage numbers.
    """
    rows = list(rows)

    def _coverage(items):
        attempted = len(items)
        clean = sum(1 for r in items if not is_output_failure(r))
        ratio = clean / attempted if attempted else 0.0
        return Coverage(attempted=attempted, clean=clean, ratio=ratio)

    fission_rows = [r for r in rows if r.get("decompiler") == "fission"]
    fission_cov = _coverage(fission_rows)
    overall_cov = _coverage(rows)

    reasons = []

    if legacy:
        reasons.append("legacy_flat_list")
        return RunValidity(
            valid=False,
            fission=fission_cov,
            overall=overall_cov,
            reasons=tuple(reasons),
        )

    if not fission_cov.attempted:
        reasons.append("no_fission_rows")
    elif fission_cov.ratio < FISSION_MIN_COVERAGE:
        reasons.append("fission_coverage_below_threshold")

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


def load_result_file(path: Path):
    """Load a result JSON file and return (rows, is_legacy).

    Supports envelope format (schema_version >= 2) and legacy flat-list.
    """
    raw = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(raw, list):
        return raw, True
    if isinstance(raw, dict) and "rows" in raw:
        return raw["rows"], False
    raise ValueError(
        f"Unrecognised result format in {path}: "
        f"expected a list or an envelope dict with 'rows'."
    )


def build_envelope(
    rows,
    *,
    run_meta=None,
    toolchain=None,
):
    """Wrap flat rows in the v2 envelope format."""
    import time as _time

    validity = evaluate_run(rows)

    return {
        "schema_version": 2,
        "run": run_meta or {},
        "toolchain": toolchain or {},
        "validity": {
            "valid": validity.valid,
            "fission_coverage": round(validity.fission.ratio, 4),
            "fission_attempted": validity.fission.attempted,
            "fission_clean": validity.fission.clean,
            "backend_coverage": round(validity.overall.ratio, 4),
            "backend_attempted": validity.overall.attempted,
            "backend_clean": validity.overall.clean,
            "reasons": list(validity.reasons),
        },
        "rendered_at": _time.strftime("%Y-%m-%dT%H:%M:%SZ", _time.gmtime()),
        "rows": rows,
    }


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
        rows, is_legacy = load_result_file(args.result_json)
    except Exception as exc:
        print(f"::error::Cannot read {args.result_json}: {exc}", file=sys.stderr)
        return 1

    # Allow threshold overrides
    import runner.run_validity as _self
    _self.FISSION_MIN_COVERAGE = args.fission_min_coverage
    _self.BACKEND_MIN_COVERAGE = args.backend_min_coverage

    verdict = evaluate_run(rows, legacy=is_legacy)
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
