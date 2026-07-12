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
``RunValidity``             -- frozen dataclass:
    .valid         -- True if measurement quality thresholds pass (matrix+coverage)
    .publishable   -- True if valid AND official AND no provenance issues
    .fission/.overall -- Coverage stats
    .reasons       -- measurement failure codes
    .publish_reasons -- publish-only failure codes (non_official_run, legacy_source)
``Coverage``                -- frozen dataclass with .attempted, .clean, .ratio
``LoadedResult``            -- dataclass containing rows, envelope, and legacy flag

CLI usage (from benchmark.yml)
-------------------------------
    python -m runner.run_validity results/dev_latest.json \
        --github-env   "$GITHUB_ENV" \
        --github-summary "$GITHUB_STEP_SUMMARY"

Exit code 0 = measurement valid (or smoke), 1 = INVALID measurement.
"""
from __future__ import annotations

import json
import sys
from functools import lru_cache
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
SCHEMA_PATH = Path(__file__).parent.parent / "schemas" / "benchmark-envelope-v2.schema.json"


@lru_cache(maxsize=1)
def _envelope_validator():
    from jsonschema import Draft202012Validator

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def validate_envelope_schema(envelope: Mapping[str, Any]) -> None:
    """Validate an envelope against the canonical repository schema."""
    errors = sorted(_envelope_validator().iter_errors(envelope), key=lambda error: list(error.path))
    if errors:
        error = errors[0]
        location = ".".join(str(part) for part in error.absolute_path) or "<root>"
        raise ValueError(f"Benchmark envelope schema error at {location}: {error.message}")


def oracle_evidence_valid(envelope: Mapping[str, Any] | None) -> bool:
    try:
        from .differential_oracle import aggregate_oracle_evidence
    except ImportError:
        from differential_oracle import aggregate_oracle_evidence

    oracle = envelope.get("oracle", {}) if envelope else {}
    required = (
        "oracle_subject", "target_abi", "compiler", "compiler_version", "runner",
        "wrapper_sha256", "reference_binary_sha256",
    )
    declared_valid = (
        oracle.get("valid") is True
        and oracle.get("mode") == "differential"
        and oracle.get("oracle_subject") == "original_binary"
        and all(isinstance(oracle.get(field), str) and oracle[field] for field in required)
    )
    if not declared_valid or not envelope:
        return False
    derived = aggregate_oracle_evidence(list(envelope.get("rows", [])))
    linked_fields = (*required, "row_evidence_sha256", "tested_rows")
    return derived.get("valid") is True and all(
        oracle.get(field) == derived.get(field) for field in linked_fields
    )


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
    """Result of :func:`evaluate_run`.

    Two-tier verdict:
    * ``valid``       -- measurement quality OK (matrix + coverage thresholds)
    * ``publishable`` -- valid AND official run AND no provenance issues

    A smoke run produces ``valid=True, publishable=False``.
    An invalid measurement produces ``valid=False, publishable=False``.
    """

    valid: bool
    """True when measurement quality thresholds pass (matrix + coverage)."""

    publishable: bool
    """True when valid AND official AND no provenance issues."""

    fission: Coverage
    """Fission-specific coverage."""

    overall: Coverage
    """Coverage across all backends including Fission."""

    reasons: tuple
    """Machine-readable measurement failure codes when ``valid`` is False.

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
    """

    publish_reasons: tuple = ()
    """Publish-only failure codes (do not affect ``valid``).

    Possible values:
    * ``"non_official_run"``  -- run_mode != official
    * ``"legacy_source"``     -- result predates envelope format
    """

    matrix_valid: bool = False
    adapter_output_valid: bool = False
    semantic_harness_valid: bool = False
    semantic_coverage_valid: bool = False
    semantic_result_valid: bool = False
    provenance_valid: bool = False
    artifact_valid: bool = False
    official_profile_valid: bool = False
    holdout_valid: bool = False
    semantic_attempted: int = 0
    semantic_tested: int = 0

    def summary_line(self) -> str:
        """One-line human-readable summary for GITHUB_STEP_SUMMARY / logs."""
        cov = (
            f"Fission {self.fission.clean}/{self.fission.attempted} "
            f"({self.fission.ratio * 100:.1f}%), "
            f"all-backend {self.overall.clean}/{self.overall.attempted} "
            f"({self.overall.ratio * 100:.1f}%)"
        )
        if not self.valid:
            return f"INVALID MEASUREMENT [{', '.join(self.reasons)}] -- {cov}"
        if not self.publishable:
            return f"EXECUTION VALID [{', '.join(self.publish_reasons)}] -- {cov} -- NOT PUBLISHABLE"
        return f"VALID -- {cov}"


def validity_dict(verdict: RunValidity) -> dict[str, Any]:
    """Serialize the complete, stage-separated verdict contract."""
    return {
        "valid": verdict.valid,
        "publishable": verdict.publishable,
        "matrix_valid": verdict.matrix_valid,
        "adapter_output_valid": verdict.adapter_output_valid,
        "semantic_harness_valid": verdict.semantic_harness_valid,
        "semantic_coverage_valid": verdict.semantic_coverage_valid,
        "semantic_result_valid": verdict.semantic_result_valid,
        "provenance_valid": verdict.provenance_valid,
        "artifact_valid": verdict.artifact_valid,
        "official_profile_valid": verdict.official_profile_valid,
        "holdout_valid": verdict.holdout_valid,
        "semantic_attempted": verdict.semantic_attempted,
        "semantic_tested": verdict.semantic_tested,
        "fission_coverage": round(verdict.fission.ratio, 4),
        "fission_attempted": verdict.fission.attempted,
        "fission_clean": verdict.fission.clean,
        "backend_coverage": round(verdict.overall.ratio, 4),
        "backend_attempted": verdict.overall.attempted,
        "backend_clean": verdict.overall.clean,
        "reasons": list(verdict.reasons),
        "publish_reasons": list(verdict.publish_reasons),
    }


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
    fission_min_coverage: float | None = None,
    backend_min_coverage: float | None = None,
) -> RunValidity:
    """Evaluate whether a benchmark run meets publishability thresholds.

    Parameters
    ----------
    result:
        A LoadedResult containing envelope and rows, or an Iterable of result-row dicts.
    legacy:
        If result is an Iterable, this marks whether it is legacy. If result is
        LoadedResult, the legacy flag on LoadedResult takes precedence.
    fission_min_coverage:
        Override the Fission minimum coverage threshold. Defaults to the module-level
        ``FISSION_MIN_COVERAGE`` constant.
    backend_min_coverage:
        Override the all-backend minimum coverage threshold. Defaults to the module-level
        ``BACKEND_MIN_COVERAGE`` constant.
    """
    if isinstance(result, LoadedResult):
        rows = list(result.rows)
        is_legacy = result.legacy
        envelope = result.envelope
    else:
        rows = list(result)
        is_legacy = legacy
        envelope = None

    # Use caller-supplied thresholds or fall back to module-level constants.
    _fission_min = fission_min_coverage if fission_min_coverage is not None else FISSION_MIN_COVERAGE
    _backend_min = backend_min_coverage if backend_min_coverage is not None else BACKEND_MIN_COVERAGE

    def _coverage(items):
        attempted = len(items)
        clean = sum(1 for r in items if not is_output_failure(r))
        ratio = clean / attempted if attempted else 0.0
        return Coverage(attempted=attempted, clean=clean, ratio=ratio)

    fission_rows = [r for r in rows if r.get("decompiler") == "fission"]
    fission_cov = _coverage(fission_rows)
    overall_cov = _coverage(rows)

    reasons: list[str] = []

    if is_legacy:
        reasons.append("legacy_flat_list")
        return RunValidity(
            valid=False,
            publishable=False,
            fission=fission_cov,
            overall=overall_cov,
            reasons=tuple(reasons),
            publish_reasons=("legacy_source",),
        )

    publish_reasons: list[str] = []
    run_meta = envelope.get("run", {}) if envelope else {}
    if run_meta.get("legacy_source"):
        publish_reasons.append("legacy_source")
    if "official" not in run_meta:
        publish_reasons.append("official_flag_missing")
    elif run_meta.get("official") is False:
        publish_reasons.append("non_official_run")

    matrix = envelope.get("matrix", {}) if envelope else {}
    expected_rows = matrix.get("expected_rows")
    expected_cells_list: list[dict] | None = matrix.get("expected_cells")
    # Legacy fallback: Cartesian product from lists (used in older envelopes)
    expected_decompilers = matrix.get("expected_decompilers")

    official_requested = run_meta.get("official") is True
    if official_requested and not expected_cells_list:
        reasons.append("official_matrix_missing")

    if expected_rows is not None and len(rows) != expected_rows:
        reasons.append("matrix_completeness_mismatch")

    if expected_cells_list is not None:
        expected_identities = [
            (c.get("decompiler"), c.get("function_name"), c.get("compiler_variant"))
            for c in expected_cells_list
        ]
        malformed_expected = [identity for identity in expected_identities if not all(identity)]
        expected_cells = {identity for identity in expected_identities if all(identity)}
        if malformed_expected:
            reasons.append("matrix_malformed_expected_cell")
        if len(expected_cells) != len(expected_identities):
            reasons.append("matrix_duplicate_expected_cells")
        if expected_rows != len(expected_cells_list):
            reasons.append("matrix_expected_rows_mismatch")
        if matrix.get("observed_rows") != len(rows):
            reasons.append("matrix_observed_rows_mismatch")

        observed_cells: set = set()
        duplicates: set = set()
        malformed_observed = False
        for r in rows:
            d = r.get("decompiler")
            f = r.get("function_name")
            v = r.get("compiler_variant")
            if d and f and v:
                cell = (d, f, v)
                if cell in observed_cells:
                    duplicates.add(cell)
                observed_cells.add(cell)
            else:
                malformed_observed = True
        missing_cells = expected_cells - observed_cells
        unexpected_cells = observed_cells - expected_cells
        if missing_cells:
            reasons.append("matrix_missing_cells")
        if unexpected_cells:
            reasons.append("matrix_unexpected_cells")
        if duplicates:
            reasons.append("matrix_duplicate_cells")
        if malformed_observed:
            reasons.append("matrix_malformed_observed_cell")

    if not fission_cov.attempted:
        reasons.append("no_fission_rows")
    elif fission_cov.ratio < _fission_min:
        reasons.append("fission_coverage_below_threshold")

    if expected_decompilers:
        for d in expected_decompilers:
            d_rows = [r for r in rows if r.get("decompiler") == d]
            if not d_rows:
                if "backend_missing" not in reasons:
                    reasons.append("backend_missing")
            else:
                d_cov = _coverage(d_rows)
                if d_cov.ratio < _backend_min:
                    if "backend_coverage_below_threshold" not in reasons:
                        reasons.append("backend_coverage_below_threshold")
    else:
        # Fallback if no matrix provided
        if not overall_cov.attempted:
            reasons.append("no_result_rows")
        elif overall_cov.ratio < _backend_min:
            reasons.append("backend_coverage_below_threshold")

    matrix_failure_codes = {
        "matrix_completeness_mismatch", "matrix_missing_cells",
        "matrix_unexpected_cells", "matrix_duplicate_cells", "backend_missing",
        "official_matrix_missing", "matrix_malformed_expected_cell",
        "matrix_duplicate_expected_cells", "matrix_expected_rows_mismatch",
        "matrix_observed_rows_mismatch", "matrix_malformed_observed_cell",
    }
    matrix_valid = not any(reason in matrix_failure_codes for reason in reasons)
    adapter_output_valid = not any(
        reason in {
            "no_fission_rows", "fission_coverage_below_threshold",
            "no_result_rows", "backend_coverage_below_threshold",
        }
        for reason in reasons
    )
    measurement_valid = not reasons

    clean_rows = [row for row in rows if not is_output_failure(row)]
    semantic_attempted = len(clean_rows)
    tested_rows = [
        row for row in clean_rows
        if row.get("semantic_score") is not None and row.get("fail_category") != "no_wrapper"
    ]
    semantic_tested = len(tested_rows)
    semantic_coverage_valid = (
        semantic_attempted > 0 and semantic_tested == semantic_attempted
    )
    if not semantic_coverage_valid:
        publish_reasons.append("semantic_coverage_incomplete")

    semantic_result_valid = all(
        isinstance(row.get("semantic_score"), (int, float))
        and 0.0 <= float(row["semantic_score"]) <= 1.0
        and int(row.get("cases_passed", 0)) <= int(row.get("cases_total", 0))
        for row in tested_rows
    )
    if not semantic_result_valid:
        publish_reasons.append("semantic_result_malformed")

    semantic_harness_valid = oracle_evidence_valid(envelope)
    if not semantic_harness_valid:
        publish_reasons.append("oracle_abi_unverified")

    limits = run_meta.get("limits") or {}
    official_profile_valid = (
        run_meta.get("official") is True
        and all(limits.get(key) in (None, 0, "", "0") for key in ("limit", "variant_limit", "function"))
        and run_meta.get("profile") == "realistic"
    )
    if not official_profile_valid:
        publish_reasons.append("official_profile_invalid")

    holdout_valid = False
    publish_reasons.append("final_publication_gate_required")

    required_run_fields = ("run_id", "started_at", "finished_at", "runner_commit", "corpus", "official")
    toolchain = envelope.get("toolchain", {}) if envelope else {}
    provenance_valid = bool(envelope) and all(run_meta.get(key) is not None for key in required_run_fields) and bool(toolchain.get("runner_commit"))
    if not provenance_valid:
        publish_reasons.append("provenance_incomplete")

    artifact_valid = bool(envelope and envelope.get("schema_version") == 2 and rows and run_meta.get("run_id"))
    if not artifact_valid:
        publish_reasons.append("artifact_invalid")

    publish_reasons = list(dict.fromkeys(publish_reasons))
    return RunValidity(
        valid=measurement_valid,
        publishable=(
            measurement_valid
            and matrix_valid
            and adapter_output_valid
            and semantic_harness_valid
            and semantic_coverage_valid
            and semantic_result_valid
            and provenance_valid
            and artifact_valid
            and official_profile_valid
            and holdout_valid
            and not publish_reasons
        ),
        fission=fission_cov,
        overall=overall_cov,
        reasons=tuple(reasons),
        publish_reasons=tuple(publish_reasons),
        matrix_valid=matrix_valid,
        adapter_output_valid=adapter_output_valid,
        semantic_harness_valid=semantic_harness_valid,
        semantic_coverage_valid=semantic_coverage_valid,
        semantic_result_valid=semantic_result_valid,
        provenance_valid=provenance_valid,
        artifact_valid=artifact_valid,
        official_profile_valid=official_profile_valid,
        holdout_valid=holdout_valid,
        semantic_attempted=semantic_attempted,
        semantic_tested=semantic_tested,
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
        validate_envelope_schema(raw)
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
    oracle=None,
    cfg_jsonl=None,
    holdout_status=None,
):
    """Wrap flat rows in the v2 envelope format.

    Attaches the standard-set ``summary`` block (MVP semantic/coverage/taxonomy/
    runtime + optional CFG secondary + cross-variant extension).
    """
    import time as _time

    try:
        from .standard_summary import attach_summary_to_envelope
    except ImportError:
        from standard_summary import attach_summary_to_envelope

    # Temporarily construct an envelope dict so evaluate_run can check matrix
    temp_envelope = {
        "schema_version": 2,
        "run": run_meta or {},
        "toolchain": toolchain or {},
        "matrix": matrix or {},
        "oracle": oracle or {"mode": "example_cases", "valid": False},
        "rows": list(rows),
    }

    # Annotate taxonomy + summary before validity so rows are self-describing.
    attach_summary_to_envelope(
        temp_envelope,
        cfg_jsonl=cfg_jsonl,
        holdout_status=holdout_status,
    )

    loaded = LoadedResult(rows=temp_envelope["rows"], envelope=temp_envelope, legacy=False)
    validity = evaluate_run(loaded)

    temp_envelope["validity"] = validity_dict(validity)
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

    # Pass thresholds as parameters — never mutate module-level globals.
    verdict = evaluate_run(
        loaded,
        fission_min_coverage=args.fission_min_coverage,
        backend_min_coverage=args.backend_min_coverage,
    )
    summary = verdict.summary_line()
    print(summary)

    measurement_val = "true" if verdict.valid else "false"
    publishable_val = "true" if verdict.publishable else "false"
    _write_line(args.github_env, f"MEASUREMENT_VALID={measurement_val}")
    _write_line(args.github_env, f"RUN_PUBLISHABLE={publishable_val}")
    # Legacy compat alias
    _write_line(args.github_env, f"FISSION_RUN_VALID={measurement_val}")

    if not verdict.valid:
        for reason in verdict.reasons:
            _write_line(
                args.github_summary,
                f"\n## ⛔ INVALID MEASUREMENT [{reason}]\n\n{summary}\n",
            )
        return 1

    if not verdict.publishable:
        _write_line(
            args.github_summary,
            f"\n## ✅ VALID SMOKE [{', '.join(verdict.publish_reasons)}]\n\n{summary}\n",
        )
        return 0

    _write_line(args.github_summary, f"\n## ✅ VALID Fission Gate: {summary}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
