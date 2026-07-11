"""Target-ABI differential harness construction and result parsing."""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from typing import Any

try:
    from .semantic import STANDARD_HEADER
except ImportError:
    from semantic import STANDARD_HEADER


@dataclass(frozen=True)
class DifferentialResult:
    score: float
    category: str
    error: str | None
    cases_passed: int
    cases_total: int
    evidence: dict[str, Any] | None = None


def _rename_function(code: str, function_name: str, replacement: str) -> str:
    pattern = re.compile(rf"\b_?{re.escape(function_name)}\b")
    renamed, count = pattern.subn(replacement, code)
    if count == 0:
        raise ValueError(f"target function {function_name!r} not found")
    return renamed


def build_differential_translation_unit(
    function_name: str,
    reference_code: str,
    candidate_code: str,
    cases: list[str],
) -> str:
    """Build one program that executes reference and candidate under one ABI."""
    reference_name = f"oracle_reference_{function_name}"
    candidate_name = f"oracle_candidate_{function_name}"
    reference = _rename_function(reference_code, function_name, reference_name)
    candidate = _rename_function(candidate_code, function_name, candidate_name)

    case_functions = []
    dispatch = []
    for index, case in enumerate(cases):
        for label, target_name in (("reference", reference_name), ("candidate", candidate_name)):
            renamed = _rename_function(case, function_name, target_name)
            renamed, count = re.subn(
                r"\bint\s+main\s*\(\s*(?:void)?\s*\)",
                f"static int oracle_case_{label}_{index}(void)",
                renamed,
                count=1,
            )
            if count != 1:
                raise ValueError(f"semantic case {index} does not define one int main()")
            case_functions.append(renamed)
        dispatch.append(
            "  ref_rc = oracle_case_reference_{0}(); cand_rc = oracle_case_candidate_{0}(); "
            'printf("CASE {0} %d %d\\n", ref_rc, cand_rc);'.format(index)
        )

    dispatcher = "\n".join([
        "int main(void) {",
        "  int ref_rc = 0;",
        "  int cand_rc = 0;",
        *dispatch,
        "  return 0;",
        "}",
    ])
    return "\n".join([
        STANDARD_HEADER,
        reference,
        candidate,
        *case_functions,
        dispatcher,
    ])


def parse_differential_output(stdout: str, cases_total: int) -> DifferentialResult:
    observed: dict[int, tuple[int, int]] = {}
    for line in stdout.splitlines():
        match = re.fullmatch(r"CASE (\d+) (-?\d+) (-?\d+)", line.strip())
        if match:
            observed[int(match.group(1))] = (int(match.group(2)), int(match.group(3)))
    if len(observed) != cases_total:
        return DifferentialResult(0.0, "runtime_error", f"oracle emitted {len(observed)}/{cases_total} cases", 0, cases_total)
    reference_failures = [index for index, (ref, _) in observed.items() if ref != 0]
    if reference_failures:
        return DifferentialResult(0.0, "fixture_error", f"reference cases failed: {reference_failures}", 0, cases_total)
    passed = sum(candidate == 0 for _, candidate in observed.values())
    category = "" if passed == cases_total else "assertion_fail"
    error = None if not category else f"candidate passed {passed}/{cases_total} cases"
    return DifferentialResult(passed / cases_total if cases_total else 0.0, category, error, passed, cases_total)


def wrapper_sha256(cases: list[str]) -> str:
    return hashlib.sha256("\0".join(cases).encode("utf-8")).hexdigest()


def _aggregate_hash(values: list[str]) -> str:
    return hashlib.sha256("\0".join(sorted(values)).encode("utf-8")).hexdigest()


def aggregate_oracle_evidence(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """Aggregate row evidence without trusting a caller-provided validity flag."""
    tested_rows = [
        row
        for row in rows
        if not row.get("error")
        and row.get("semantic_score") is not None
        and row.get("fail_category") != "no_wrapper"
    ]
    evidence = [row.get("oracle_evidence") for row in tested_rows]
    valid = bool(tested_rows) and all(
        isinstance(item, dict)
        and item.get("valid") is True
        and item.get("mode") == "differential"
        for item in evidence
    )
    valid_items = [item for item in evidence if isinstance(item, dict)]
    required = (
        "oracle_subject",
        "target_abi",
        "compiler",
        "compiler_version",
        "runner",
        "wrapper_sha256",
        "reference_binary_sha256",
    )
    valid = valid and all(
        isinstance(item.get(field), str) and item[field]
        for item in valid_items
        for field in required
    )
    if not valid:
        return {"mode": "differential", "valid": False, "tested_rows": len(tested_rows)}

    identity_evidence = []
    for row, item in zip(tested_rows, valid_items, strict=True):
        identity_evidence.append({
            "decompiler": row["decompiler"],
            "function_name": row["function_name"],
            "compiler_variant": row["compiler_variant"],
            "evidence": item,
        })
    evidence_json = json_dumps_canonical(identity_evidence)
    return {
        "mode": "differential",
        "valid": True,
        "oracle_subject": ",".join(
            sorted({item["oracle_subject"] for item in valid_items})
        ),
        "target_abi": ",".join(sorted({item["target_abi"] for item in valid_items})),
        "compiler": ",".join(sorted({item["compiler"] for item in valid_items})),
        "compiler_version": " | ".join(sorted({item["compiler_version"] for item in valid_items})),
        "runner": ",".join(sorted({item["runner"] for item in valid_items})),
        "wrapper_sha256": _aggregate_hash([item["wrapper_sha256"] for item in valid_items]),
        "reference_binary_sha256": _aggregate_hash(
            [item["reference_binary_sha256"] for item in valid_items]
        ),
        "row_evidence_sha256": hashlib.sha256(evidence_json.encode("utf-8")).hexdigest(),
        "tested_rows": len(tested_rows),
    }


def json_dumps_canonical(value: Any) -> str:
    import json

    return json.dumps(value, sort_keys=True, separators=(",", ":"))


async def verify_with_oracle(
    client: Any,
    endpoint: str,
    *,
    function_name: str,
    reference_code: str,
    candidate_code: str,
    cases: list[str],
    compiler_variant: str,
    reference_binary_sha256: str,
) -> DifferentialResult:
    """Execute a differential harness through the target-ABI oracle service."""
    try:
        response = await client.post(
            f"{endpoint.rstrip('/')}/verify",
            json={
                "function_name": function_name,
                "reference_code": reference_code,
                "candidate_code": candidate_code,
                "cases": cases,
                "compiler_variant": compiler_variant,
                "reference_binary_sha256": reference_binary_sha256,
            },
            timeout=120.0,
        )
        response.raise_for_status()
        payload = response.json()
    except Exception as exc:
        return DifferentialResult(0.0, "oracle_error", str(exc), 0, len(cases), None)

    evidence = payload.get("evidence")
    if not isinstance(evidence, dict) or evidence.get("valid") is not True:
        return DifferentialResult(
            0.0,
            "oracle_error",
            str(payload.get("error") or "oracle returned invalid evidence"),
            0,
            len(cases),
            evidence if isinstance(evidence, dict) else None,
        )
    return DifferentialResult(
        float(payload.get("score", 0.0)),
        str(payload.get("category") or ""),
        payload.get("error"),
        int(payload.get("cases_passed", 0)),
        int(payload.get("cases_total", len(cases))),
        evidence,
    )
