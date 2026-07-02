"""Diagnostics for decompiler output shape and harnessability."""
from __future__ import annotations

import re
from typing import Any


FUNCTION_DEF_RE = re.compile(
    r"(?m)^\s*(?:[\w_][\w\s_*\(\),]*\s+)?([A-Za-z_][\w.]*)\s*\([^;{}]*\)\s*\{"
)
CONTROL_KEYWORDS = {"if", "for", "while", "switch", "do"}
EMPTY_OUTPUT_SENTINELS = {
    "angr decompilation empty",
}


def _function_definitions(code: str) -> list[str]:
    return [
        match.group(1)
        for match in FUNCTION_DEF_RE.finditer(code)
        if match.group(1) not in CONTROL_KEYWORDS
    ]


def _address_aliases(addr: str | None) -> set[str]:
    if not addr:
        return set()
    try:
        value = int(addr, 16) if addr.lower().startswith("0x") else int(addr)
    except ValueError:
        return {addr.lower()}

    aliases = {f"{value:x}", f"0x{value:x}"}
    if value >= 0x100000000:
        rva = value & 0xFFFFF
        aliases.update({f"{rva:x}", f"0x{rva:x}", f"0x{rva:08x}"})
    return aliases


def _contains_expected_address(code: str, addr: str | None) -> bool:
    aliases = _address_aliases(addr)
    lowered = code.lower()
    return any(alias in lowered for alias in aliases)


def analyze_output_diagnostics(
    function_name: str,
    decompiler: str,
    code: str,
    expected_addr: str | None = None,
) -> dict[str, Any]:
    """Return raw diagnostics describing whether output looks like one target C function."""
    normalized = (code or "").strip().lower()
    if not normalized or normalized in EMPTY_OUTPUT_SENTINELS:
        return {
            "status": "no_output",
            "issues": ["no_output", "empty_decompiler_sentinel"] if normalized else ["no_output"],
            "function_definition_count": 0,
            "target_name_present": False,
            "expected_address_present": False,
            "harness_blockers": [],
        }

    definitions = _function_definitions(code)
    target_name_re = re.compile(rf"\b_?{re.escape(function_name)}\b")
    target_name_present = bool(target_name_re.search(code))
    expected_address_present = _contains_expected_address(code, expected_addr)
    dotted_names = sorted(set(re.findall(r"\b(?:dbg|sym)\.[A-Za-z_][\w.]*", code)))
    revng_abi = "_ABI(" in code or "_REG(" in code or "_STACK" in code
    ghidra_register_inputs = sorted(set(re.findall(r"\bin_[A-Z0-9_]+\b", code)))
    truncated = len(code) >= 7900
    whole_program_like = truncated or len(definitions) > 3

    issues: list[str] = []
    harness_blockers: list[str] = []

    if not target_name_present:
        issues.append("target_name_missing")
    if expected_addr and not expected_address_present:
        issues.append("expected_address_missing")
    if whole_program_like:
        issues.append("whole_program_or_truncated_output")
    if dotted_names:
        issues.append("non_c_identifier_names")
        harness_blockers.append("dotted_function_names")
    if revng_abi:
        issues.append("revng_abi_macros")
        harness_blockers.append("revng_abi_types")
    if ghidra_register_inputs:
        issues.append("register_pseudo_inputs")
        harness_blockers.append("register_pseudo_inputs")

    single_target_like = (target_name_present or expected_address_present) and not whole_program_like
    if single_target_like and not harness_blockers:
        status = "direct_function"
    elif single_target_like:
        status = "needs_normalization"
    elif whole_program_like:
        status = "whole_program_output"
    else:
        status = "boundary_mismatch"

    return {
        "status": status,
        "issues": issues,
        "function_definition_count": len(definitions),
        "function_definitions_sample": definitions[:5],
        "target_name_present": target_name_present,
        "expected_address_present": expected_address_present,
        "whole_program_like": whole_program_like,
        "truncated_output": truncated,
        "harness_blockers": harness_blockers,
        "dotted_names_sample": dotted_names[:5],
        "register_inputs_sample": ghidra_register_inputs[:5],
        "decompiler": decompiler,
    }


def invalid_output_reason(
    diagnostics: dict[str, Any],
    code: str,
    duplicate_count: int = 1,
) -> str | None:
    """Return an adapter-level error when output is not a usable target function."""
    status = diagnostics.get("status")
    issues = diagnostics.get("issues", [])

    if status == "no_output":
        return "No decompiler output for target function"
    if status == "whole_program_output":
        return "Decompiler returned whole-program or truncated output, not a target function"
    if status == "boundary_mismatch":
        return "Decompiler output does not match requested function name or address"
    if (
        duplicate_count > 1
        and len((code or "").strip()) > 128
        and any(issue in issues for issue in ("target_name_missing", "expected_address_missing"))
    ):
        return f"Identical non-target output reused for {duplicate_count} requested functions"
    return None
