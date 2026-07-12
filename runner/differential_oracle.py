"""Target-ABI differential harness construction and result parsing."""
from __future__ import annotations

import hashlib
import re
import struct
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    from .semantic import STANDARD_HEADER
except ImportError:
    from semantic import STANDARD_HEADER

ORACLE_SUBJECT_SOURCE_RECOMPILE = "source_recompile"
ORACLE_SUBJECT_ORIGINAL_BINARY = "original_binary"

_PE_LOADER_SNIPPET: str | None = None


def pe_loader_snippet() -> str:
    """Return the MinGW/Wine PE mapper snippet embedded into original-binary TUs."""
    global _PE_LOADER_SNIPPET
    if _PE_LOADER_SNIPPET is None:
        candidates = [
            Path(__file__).resolve().parent.parent / "docker" / "oracle" / "pe_loader_snippet.c",
            Path("/app/pe_loader_snippet.c"),
        ]
        for path in candidates:
            if path.is_file():
                _PE_LOADER_SNIPPET = path.read_text(encoding="utf-8")
                break
        else:
            raise FileNotFoundError("pe_loader_snippet.c not found for original_binary oracle")
    return _PE_LOADER_SNIPPET


@dataclass(frozen=True)
class DifferentialResult:
    score: float
    category: str
    error: str | None
    cases_passed: int
    cases_total: int
    evidence: dict[str, Any] | None = None


@dataclass(frozen=True)
class FunctionSignature:
    return_type: str
    function_name: str
    params: str
    param_names: str
    is_void: bool


def _rename_function(code: str, function_name: str, replacement: str) -> str:
    pattern = re.compile(rf"\b_?{re.escape(function_name)}\b")
    renamed, count = pattern.subn(replacement, code)
    if count == 0:
        raise ValueError(f"target function {function_name!r} not found")
    return renamed


def extract_function_signature(reference_code: str, function_name: str) -> FunctionSignature:
    """Parse a C function definition signature from extracted reference source."""
    stripped = re.sub(r"/\*.*?\*/", "", reference_code, flags=re.DOTALL)
    stripped = re.sub(r"//[^\n]*", "", stripped)
    pattern = re.compile(
        rf"(?P<ret>[\w\s\*]+?)\b{re.escape(function_name)}\s*\((?P<params>[^;{{]*)\)\s*\{{",
        re.DOTALL,
    )
    match = pattern.search(stripped)
    if not match:
        raise ValueError(f"cannot parse signature for {function_name!r}")
    return_type = " ".join(match.group("ret").split())
    # Drop storage-class noise from return type.
    for prefix in ("static ", "inline ", "extern "):
        if return_type.startswith(prefix):
            return_type = return_type[len(prefix) :].strip()
    params = " ".join(match.group("params").split()).strip()
    if not params or params == "void":
        param_names = ""
    else:
        names: list[str] = []
        depth = 0
        current: list[str] = []
        for ch in params:
            if ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
            if ch == "," and depth == 0:
                part = "".join(current).strip()
                if part:
                    names.append(_param_name(part))
                current = []
            else:
                current.append(ch)
        tail = "".join(current).strip()
        if tail:
            names.append(_param_name(tail))
        if any(not name for name in names):
            raise ValueError(f"cannot extract parameter names for {function_name!r}")
        param_names = ", ".join(names)
    is_void = return_type == "void"
    return FunctionSignature(return_type, function_name, params or "void", param_names, is_void)


def _param_name(decl: str) -> str:
    cleaned = decl.strip()
    if not cleaned or cleaned == "void":
        return ""
    # Strip trailing array declarators: name[10]
    cleaned = re.sub(r"\[.*?\]", "", cleaned).strip()
    # Function pointer: type (*name)(...)
    fp = re.search(r"\(\s*\*\s*([A-Za-z_]\w*)\s*\)", cleaned)
    if fp:
        return fp.group(1)
    tokens = re.findall(r"[A-Za-z_]\w*", cleaned)
    if not tokens:
        return ""
    return tokens[-1]


def pe_image_base(pe_bytes: bytes) -> int:
    """Return PE Preferred ImageBase from a PE image."""
    if len(pe_bytes) < 0x40 or pe_bytes[:2] != b"MZ":
        raise ValueError("not a PE image")
    e_lfanew = struct.unpack_from("<I", pe_bytes, 0x3C)[0]
    if pe_bytes[e_lfanew : e_lfanew + 4] != b"PE\x00\x00":
        raise ValueError("missing PE signature")
    magic = struct.unpack_from("<H", pe_bytes, e_lfanew + 24)[0]
    if magic == 0x20B:  # PE32+
        return struct.unpack_from("<Q", pe_bytes, e_lfanew + 24 + 24)[0]
    if magic == 0x10B:  # PE32
        return struct.unpack_from("<I", pe_bytes, e_lfanew + 24 + 28)[0]
    raise ValueError(f"unsupported optional-header magic {magic:#x}")


def function_addr_to_rva(pe_bytes: bytes, addr: str) -> int:
    """Convert a manifest VA/RVA address string to an image RVA."""
    value = int(addr, 16) if addr.lower().startswith("0x") else int(addr)
    image_base = pe_image_base(pe_bytes)
    if value >= image_base:
        return value - image_base
    return value


def _build_case_functions(
    function_name: str,
    reference_name: str,
    candidate_name: str,
    cases: list[str],
) -> tuple[list[str], list[str]]:
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
    return case_functions, dispatch


def build_differential_translation_unit(
    function_name: str,
    reference_code: str,
    candidate_code: str,
    cases: list[str],
) -> str:
    """Build one program that executes source-recompiled reference and candidate."""
    reference_name = f"oracle_reference_{function_name}"
    candidate_name = f"oracle_candidate_{function_name}"
    reference = _rename_function(reference_code, function_name, reference_name)
    candidate = _rename_function(candidate_code, function_name, candidate_name)
    case_functions, dispatch = _build_case_functions(
        function_name, reference_name, candidate_name, cases
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


def build_original_binary_translation_unit(
    function_name: str,
    reference_code: str,
    candidate_code: str,
    cases: list[str],
    *,
    function_addr: str,
    pe_bytes: bytes,
    pe_path: str = "reference.exe",
) -> str:
    """Build a differential TU whose reference side calls into the original PE.

    The original PE is loaded under Wine via a minimal mapper. Test wrappers still
    exercise C-level calling convention; the candidate is recompiled decompilation.
    """
    sig = extract_function_signature(reference_code, function_name)
    rva = function_addr_to_rva(pe_bytes, function_addr)
    reference_name = f"oracle_reference_{function_name}"
    candidate_name = f"oracle_candidate_{function_name}"
    candidate = _rename_function(candidate_code, function_name, candidate_name)

    args = sig.param_names
    call = f"oracle_pe_fn({args})" if args else "oracle_pe_fn()"
    if sig.is_void:
        reference_stub = "\n".join([
            f"typedef void (*oracle_pe_fn_t)({sig.params});",
            "static oracle_pe_fn_t oracle_pe_fn;",
            f"static void {reference_name}({sig.params}) {{",
            f"  {call};",
            "}",
        ])
    else:
        reference_stub = "\n".join([
            f"typedef {sig.return_type} (*oracle_pe_fn_t)({sig.params});",
            "static oracle_pe_fn_t oracle_pe_fn;",
            f"static {sig.return_type} {reference_name}({sig.params}) {{",
            f"  return {call};",
            "}",
        ])

    case_functions, dispatch = _build_case_functions(
        function_name, reference_name, candidate_name, cases
    )
    dispatcher = "\n".join([
        "int main(void) {",
        "  int ref_rc = 0;",
        "  int cand_rc = 0;",
        "  OraclePeImage image = {0};",
        f'  if (oracle_pe_load("{pe_path}", &image) != 0) {{',
        '    fprintf(stderr, "oracle pe load failed\\n");',
        "    return 90;",
        "  }",
        f"  DWORD rva = {rva}u;",
        "  if (!rva) {",
        '    fprintf(stderr, "oracle pe rva invalid\\n");',
        "    oracle_pe_free(&image);",
        "    return 91;",
        "  }",
        "  oracle_pe_fn = (oracle_pe_fn_t)(image.base + rva);",
        *dispatch,
        "  oracle_pe_free(&image);",
        "  return 0;",
        "}",
    ])
    return "\n".join([
        STANDARD_HEADER,
        pe_loader_snippet(),
        reference_stub,
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
    # Always emit full identity fields so official envelopes satisfy schema even
    # when valid=false (partial/incomplete row evidence). Publication still
    # requires valid=true via oracle_evidence_valid.
    complete_items = [
        item
        for item in valid_items
        if isinstance(item.get("oracle_subject"), str)
        and item.get("oracle_subject")
        and isinstance(item.get("target_abi"), str)
        and item.get("target_abi")
        and isinstance(item.get("compiler"), str)
        and item.get("compiler")
        and isinstance(item.get("compiler_version"), str)
        and item.get("compiler_version")
        and isinstance(item.get("runner"), str)
        and item.get("runner")
        and isinstance(item.get("wrapper_sha256"), str)
        and item.get("wrapper_sha256")
        and isinstance(item.get("reference_binary_sha256"), str)
        and item.get("reference_binary_sha256")
    ]
    identity_evidence = []
    for row, item in zip(tested_rows, valid_items, strict=True):
        identity_evidence.append({
            "decompiler": row["decompiler"],
            "function_name": row["function_name"],
            "compiler_variant": row["compiler_variant"],
            "evidence": item,
        })
    evidence_json = json_dumps_canonical(identity_evidence)
    empty = "0" * 64
    if complete_items:
        subjects = sorted({item["oracle_subject"] for item in complete_items})
        # Schema enum is a single subject; prefer original_binary when present.
        subject = (
            "original_binary"
            if "original_binary" in subjects
            else subjects[0]
        )
        return {
            "mode": "differential",
            "valid": valid,
            "oracle_subject": subject,
            "target_abi": ",".join(sorted({item["target_abi"] for item in complete_items})),
            "compiler": ",".join(sorted({item["compiler"] for item in complete_items})),
            "compiler_version": " | ".join(
                sorted({item["compiler_version"] for item in complete_items})
            ),
            "runner": ",".join(sorted({item["runner"] for item in complete_items})),
            "wrapper_sha256": _aggregate_hash(
                [item["wrapper_sha256"] for item in complete_items]
            ),
            "reference_binary_sha256": _aggregate_hash(
                [item["reference_binary_sha256"] for item in complete_items]
            ),
            "row_evidence_sha256": hashlib.sha256(evidence_json.encode("utf-8")).hexdigest(),
            "tested_rows": len(tested_rows),
        }
    return {
        "mode": "differential",
        "valid": False,
        "oracle_subject": "original_binary",
        "target_abi": "unknown",
        "compiler": "unknown",
        "compiler_version": "unknown",
        "runner": "unknown",
        "wrapper_sha256": empty,
        "reference_binary_sha256": empty,
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
    reference_binary_b64: str | None = None,
    function_addr: str | None = None,
) -> DifferentialResult:
    """Execute a differential harness through the target-ABI oracle service.

    When ``reference_binary_b64`` and ``function_addr`` are provided the oracle
    uses ``oracle_subject=original_binary`` (PE-anchored reference). Otherwise it
    falls back to source recompilation evidence.
    """
    payload = {
        "function_name": function_name,
        "reference_code": reference_code,
        "candidate_code": candidate_code,
        "cases": cases,
        "compiler_variant": compiler_variant,
        "reference_binary_sha256": reference_binary_sha256,
    }
    if reference_binary_b64 and function_addr:
        payload["reference_binary_b64"] = reference_binary_b64
        payload["function_addr"] = function_addr
    try:
        # Wine is process-serialized per ABI inside the oracle; under concurrent
        # official matrix load a request may wait several minutes in queue.
        response = await client.post(
            f"{endpoint.rstrip('/')}/verify",
            json=payload,
            timeout=300.0,
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
