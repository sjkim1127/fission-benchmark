"""Shared reliability guards for parity comparators.

Prevents empty/stub payloads from becoming false matches when stage CLIs or
golden paths call compare_* without the unified runner's FetchResult gate.
"""
from __future__ import annotations

from typing import Any

from benchmark.common.schema import BenchmarkResult, BenchmarkSubject


def is_empty_list_payload(payload: object) -> bool:
    return not isinstance(payload, list) or len(payload) == 0


def is_empty_cfg_payload(payload: object) -> bool:
    if not isinstance(payload, dict):
        return True
    blocks = payload.get("blocks") or []
    edges = payload.get("edges") or []
    return not blocks and not edges


def is_empty_stage_payload(stage: str, payload: object) -> bool:
    if stage in {
        "assembly_parity",
        "decode_parity",
        "pcode_parity",
        "function_discovery",
    }:
        return is_empty_list_payload(payload)
    if stage == "cfg_parity":
        return is_empty_cfg_payload(payload)
    return payload is None


def empty_pair_result(
    subject: BenchmarkSubject,
    stage: str,
    reference_name: str,
    candidate_name: str,
    expected: object,
    actual: object,
) -> BenchmarkResult | None:
    """Return an invalid-result row when either side is empty; else None.

    Empty-vs-empty must never count as match (both_empty_invalid).
    """
    exp_empty = is_empty_stage_payload(stage, expected)
    act_empty = is_empty_stage_payload(stage, actual)
    if not exp_empty and not act_empty:
        return None
    if exp_empty and act_empty:
        return BenchmarkResult(
            subject=subject,
            stage=stage,  # type: ignore[arg-type]
            status="both_empty_invalid",
            reference=reference_name,
            candidate=candidate_name,
            expected=expected,
            actual=actual,
            error="Both reference and candidate payloads are empty — not a valid match",
            metrics={"empty_guard": 1},
        )
    if exp_empty:
        return BenchmarkResult(
            subject=subject,
            stage=stage,  # type: ignore[arg-type]
            status="reference_empty",
            reference=reference_name,
            candidate=candidate_name,
            expected=expected,
            actual=actual,
            error="Reference payload empty",
            metrics={"empty_guard": 1},
        )
    return BenchmarkResult(
        subject=subject,
        stage=stage,  # type: ignore[arg-type]
        status="candidate_empty",
        reference=reference_name,
        candidate=candidate_name,
        expected=expected,
        actual=actual,
        error="Candidate payload empty",
        metrics={"empty_guard": 1},
    )


def decode_surface_is_stub(payload: object) -> bool:
    """True when decode list has no real decode fields (modrm/sib/imm/prefixes).

    Both Ghidra and Fission currently derive decode from disasm with null
    structural fields — that must not inflate primary quality rates.
    """
    if not isinstance(payload, list) or not payload:
        return True
    structural = ("modrm", "sib", "displacement", "immediate", "prefixes")
    for inst in payload:
        if not isinstance(inst, dict):
            continue
        for key in structural:
            val = inst.get(key)
            if key == "prefixes":
                if isinstance(val, list) and len(val) > 0:
                    return False
            elif val is not None and val != "" and val != []:
                return False
    return True


def guard_decode_stub(
    subject: BenchmarkSubject,
    reference_name: str,
    candidate_name: str,
    expected: object,
    actual: object,
) -> BenchmarkResult | None:
    """Skip decode_parity when neither side exposes a real decode surface."""
    if not (decode_surface_is_stub(expected) and decode_surface_is_stub(actual)):
        return None
    n = len(expected) if isinstance(expected, list) else 0
    return BenchmarkResult(
        subject=subject,
        stage="decode_parity",
        status="skipped",
        reference=reference_name,
        candidate=candidate_name,
        mismatch_kind="decode_surface_stub",
        expected=expected,
        actual=actual,
        metrics={
            "instruction_count": n,
            "decode_surface": "stub",
            "reliability": "not_scored",
        },
        error=(
            "Decode surface is derived from disasm (no modrm/sib/disp/imm); "
            "stage skipped for reliability — not counted as match"
        ),
    )


def cfg_invariant_violations(cfg: object) -> list[dict[str, Any]]:
    """Structural IR checks for a single CFG payload (no reference needed)."""
    violations: list[dict[str, Any]] = []
    if not isinstance(cfg, dict):
        return [{"kind": "invalid_cfg_payload"}]
    blocks = cfg.get("blocks") if isinstance(cfg.get("blocks"), list) else []
    edges = cfg.get("edges") if isinstance(cfg.get("edges"), list) else []
    if not blocks:
        violations.append({"kind": "empty_cfg_blocks"})
        return violations
    starts = set()
    for b in blocks:
        if not isinstance(b, dict):
            violations.append({"kind": "invalid_block"})
            continue
        start = b.get("start")
        if start is None or start == "":
            violations.append({"kind": "block_missing_start"})
        else:
            starts.add(str(start).lower())
    for e in edges:
        if not isinstance(e, dict):
            violations.append({"kind": "invalid_edge"})
            continue
        src = e.get("source")
        tgt = e.get("target")
        if src is None or tgt is None:
            violations.append({"kind": "edge_missing_endpoint"})
            continue
        # Only require source in block starts (targets may be external)
        if str(src).lower() not in starts:
            violations.append(
                {
                    "kind": "edge_source_not_in_blocks",
                    "source": str(src),
                }
            )
    return violations
