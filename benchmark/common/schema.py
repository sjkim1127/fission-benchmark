"""Shared schemas for layered benchmark stages."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

BenchmarkStage = Literal[
    "assembly_parity",
    "decode_parity",
    "pcode_parity",
    "cfg_parity",
    "function_discovery",
    "ir_invariants",
    "golden_repros",
    "telemetry",
    "decompiler_quality",
]

BenchmarkStatus = Literal["match", "mismatch", "error", "skipped"]


@dataclass(frozen=True)
class BenchmarkSubject:
    binary: str
    function: str
    addr: str
    arch: str
    compiler: str
    opt: str
    corpus_split: str = "dev"


@dataclass(frozen=True)
class BenchmarkResult:
    subject: BenchmarkSubject
    stage: BenchmarkStage
    status: BenchmarkStatus
    reference: str
    candidate: str
    mismatch_kind: str | None = None
    expected: Any = None
    actual: Any = None
    metrics: dict[str, int | float | str] = field(default_factory=dict)
    error: str | None = None


@dataclass(frozen=True)
class AssemblyInstruction:
    address: str
    bytes: str
    mnemonic: str
    operands: str = ""
    length: int | None = None
    fallthrough: str | None = None
    branch_target: str | None = None


@dataclass(frozen=True)
class DecodedInstruction:
    address: str
    bytes: str
    length: int
    mnemonic: str | None = None
    operands: str | None = None
    prefixes: list[str] = field(default_factory=list)
    modrm: str | None = None
    sib: str | None = None
    displacement: str | None = None
    immediate: str | None = None


@dataclass(frozen=True)
class PcodeVarnode:
    space: str
    offset: str
    size: int


@dataclass(frozen=True)
class PcodeOp:
    op: str
    inputs: list[PcodeVarnode] = field(default_factory=list)
    output: PcodeVarnode | None = None
    seq: int | None = None


@dataclass(frozen=True)
class CfgGraph:
    blocks: list[dict[str, Any]] = field(default_factory=list)
    edges: list[dict[str, Any]] = field(default_factory=list)


@dataclass(frozen=True)
class FunctionSymbol:
    address: str
    name: str | None = None
    size: int | None = None
    kind: str | None = None
