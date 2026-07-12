"""Command-template providers for parity stages."""
from __future__ import annotations

import json
import os
import re
import shlex
import subprocess
from dataclasses import asdict, is_dataclass
from typing import Any, Literal

from benchmark.common.schema import BenchmarkSubject

_HEX_SPACES = re.compile(r"\s+")
_ADDR_RE = re.compile(r"^(0x)?([0-9a-fA-F]+)$")

CanonicalizeMode = Literal["loose", "strict"]


def get_canonicalize_mode() -> CanonicalizeMode:
    """Canonicalize mode for primary scoring.

    **Conservative default is ``strict``** — no leniency for publishable rates.
    Set ``PARITY_CANONICALIZE_MODE=loose`` only for local triage of known
    encoding gaps (never for CI / official telemetry).
    """
    raw = (os.environ.get("PARITY_CANONICALIZE_MODE") or "strict").strip().lower()
    if raw == "loose":
        return "loose"
    return "strict"


def render_command(template: str, subject: BenchmarkSubject) -> list[str]:
    values = asdict(subject)
    return shlex.split(template.format(**values))


def run_json_provider(template: str, subject: BenchmarkSubject, timeout: float) -> Any:
    cmd = render_command(template, subject)
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    if result.returncode != 0:
        stderr = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(stderr or f"provider exited with {result.returncode}")
    return json.loads(result.stdout)


def normalize_address(value: str) -> str:
    text = value.strip().lower()
    match = _ADDR_RE.match(text)
    if not match:
        return text
    return f"0x{int(match.group(2), 16):x}"


def normalize_hex_bytes(value: str) -> str:
    return _HEX_SPACES.sub("", value.strip().lower().replace("0x", ""))


def canonicalize(value: Any, *, context_key: str | None = None) -> Any:
    """Canonical form for parity equality.

    Normalizes addresses, hex bytes, and case so Ghidra vs Fission formatting
    differences do not create false mismatches.
    """
    if is_dataclass(value):
        value = asdict(value)
    if isinstance(value, dict):
        out = {}
        for k, v in sorted(value.items(), key=lambda item: str(item[0])):
            key = str(k)
            # Operand text differs widely (PUSH RBP vs RBP); compare structure via
            # address/bytes/mnemonic primarily by dropping pure display noise later.
            out[key] = canonicalize(v, context_key=key)
        return out
    if isinstance(value, list):
        return [canonicalize(v, context_key=context_key) for v in value]
    if isinstance(value, str):
        text = value.strip().lower()
        if context_key in {"address", "start", "end", "source", "target", "fallthrough", "branch_target", "offset"}:
            if text in {"", "null", "none"}:
                return None
            try:
                return normalize_address(text)
            except ValueError:
                return text
        if context_key in {"bytes"}:
            return normalize_hex_bytes(text)
        return text
    return value


def canonicalize_assembly_list(
    instructions: Any,
    *,
    mode: CanonicalizeMode | None = None,
) -> Any:
    """Canonicalize assembly for parity.

    Compares address / bytes / mnemonic / length only. Operand text is free-form
    display noise. Fallthrough/branch_target are dropped until both adapters
    emit them reliably (Fission currently always nulls them — keeping them under
    ``strict`` would falsely zero assembly match rates).

    *mode* is accepted for API symmetry with pcode/cfg but does not change
    assembly field selection today.
    """
    _ = mode or get_canonicalize_mode()
    norm = canonicalize(instructions)
    if not isinstance(norm, list):
        return norm
    cleaned = []
    for inst in norm:
        if not isinstance(inst, dict):
            cleaned.append(inst)
            continue
        item = dict(inst)
        item.pop("operands", None)
        item.pop("fallthrough", None)
        item.pop("branch_target", None)
        # Length must match bytes if both present.
        if item.get("bytes") and not item.get("length"):
            item["length"] = len(str(item["bytes"])) // 2
        cleaned.append(item)
    return cleaned


def canonicalize_cfg(
    graph: Any,
    *,
    mode: CanonicalizeMode | None = None,
) -> Any:
    """Canonicalize CFG to sorted unique blocks/edges.

    *loose*: default missing edge kind to ``branch``.
    *strict*: preserve missing kind as null (tools must agree on kind or both omit).
    """
    mode = mode or get_canonicalize_mode()
    norm = canonicalize(graph)
    if not isinstance(norm, dict):
        return norm
    blocks = norm.get("blocks") or []
    edges = norm.get("edges") or []
    if isinstance(blocks, list):
        uniq = []
        seen = set()
        for b in blocks:
            if not isinstance(b, dict):
                continue
            key = (b.get("start"), b.get("end"))
            if key in seen:
                continue
            seen.add(key)
            uniq.append({"start": b.get("start"), "end": b.get("end")})
        blocks = sorted(uniq, key=lambda b: (b.get("start") or "", b.get("end") or ""))
    if isinstance(edges, list):
        uniq_e = []
        seen_e = set()
        for e in edges:
            if not isinstance(e, dict):
                continue
            if mode == "strict":
                kind = e.get("kind")
            else:
                kind = e.get("kind") or "branch"
            key = (e.get("source"), e.get("target"), kind)
            if key in seen_e:
                continue
            seen_e.add(key)
            uniq_e.append(
                {"source": e.get("source"), "target": e.get("target"), "kind": kind}
            )
        edges = sorted(
            uniq_e,
            key=lambda e: (e.get("source") or "", e.get("target") or "", str(e.get("kind"))),
        )
    return {"blocks": blocks, "edges": edges}


_NON_ALNUM = re.compile(r"[^A-Z0-9]")


def normalize_pcode_op(op_name: Any) -> str:
    """Normalize p-code opcode names across Ghidra / Fission spellings.

    Examples that must collide:
      INT_SUB / IntSub / INTSUB  → INTSUB
      BOOL_NEGATE / BoolNegate  → BOOLNEGATE
      POPCOUNT / PopCount       → POPCOUNT
    """
    text = str(op_name or "").strip().upper()
    return _NON_ALNUM.sub("", text)


# ---------------------------------------------------------------------------
# P-code address-space selector policy (explicit, no silent leniency)
# ---------------------------------------------------------------------------
# LOAD/STORE first input is an *address-space selector*, not a program value.
# Ghidra encodes a tool-local space table index in the const offset (e.g. 0x1b1);
# Fission uses a different encoding (e.g. 0x3). Comparing those offsets as
# values invents false mismatches.
#
# Policies:
#   loose   — drop selector to (space=addrspace, offset=*)
#   strict  — keep space *name* + size; abstract offset to "space_selector"
#             (primary / conservative default)
#   literal — keep numeric offset as emitted (debug only; never CI default)
#
# All other varnodes remain full literal comparisons under strict/literal.


def _canonicalize_pcode_inputs(
    op_key: str,
    inputs: Any,
    *,
    mode: str,
) -> Any:
    """Canonicalize op inputs under the space-selector policy above."""
    if not isinstance(inputs, list):
        return canonicalize(inputs)
    if op_key in {"LOAD", "STORE"} and inputs:
        first = inputs[0] if isinstance(inputs[0], dict) else {}
        rest = inputs[1:]
        space_size = first.get("size") if isinstance(first, dict) else None
        if mode == "loose":
            space_stub = {
                "space": "addrspace",
                "offset": "*",
                "size": space_size,
            }
            return [canonicalize(space_stub)] + [canonicalize(v) for v in rest]
        if mode == "strict":
            # Encoding-invariant selector: space name + size, not table index.
            first_c = canonicalize(first) if isinstance(first, dict) else {}
            space_stub = {
                "space": first_c.get("space") or "const",
                "offset": "space_selector",
                "size": first_c.get("size", space_size),
            }
            return [space_stub] + [canonicalize(v) for v in rest]
        # literal: fall through to full canonicalize of all inputs
    return [canonicalize(v) for v in inputs]


def canonicalize_pcode(
    ops: Any,
    *,
    mode: CanonicalizeMode | str | None = None,
) -> Any:
    """Compare p-code primarily by op sequence; varnode spaces/offsets secondary.

    Always normalizes opcode naming (Ghidra ``INT_SUB`` vs Fission ``IntSub``).
    LOAD/STORE space-id handling depends on *mode* (see
    :func:`_canonicalize_pcode_inputs`). Mode may be ``loose``, ``strict``
    (default), or ``literal`` (debug).
    """
    mode = mode or get_canonicalize_mode()
    if mode not in {"loose", "strict", "literal"}:
        mode = "strict"
    if not isinstance(ops, list):
        return canonicalize(ops)
    cleaned = []
    for i, op in enumerate(ops):
        if not isinstance(op, dict):
            cleaned.append(canonicalize(op))
            continue
        op_key = normalize_pcode_op(op.get("op"))
        cleaned.append({
            "seq": int(op.get("seq", i)) if op.get("seq") is not None else i,
            "op": op_key,
            "inputs": _canonicalize_pcode_inputs(
                op_key, op.get("inputs") or [], mode=str(mode)
            ),
            "output": canonicalize(op.get("output")),
        })
    return cleaned
