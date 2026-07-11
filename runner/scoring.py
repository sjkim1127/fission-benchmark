"""
Scoring engine for multi-decompiler comparison.

Metrics:
  1. source_similarity  — normalized edit distance vs original C source
  2. semantic_score     — fraction of test cases passed (0.0–1.0)
  3. structural_penalty — relative goto/nesting increase vs original source
  4. correctness_score  — semantic-gated correctness ranking metric
  5. correctness_rank   — relative correctness position among all decompilers
"""
from __future__ import annotations

import difflib
import re
from dataclasses import dataclass, field
from typing import Any


# Intrinsic functions that may affect semantic score validity
INTRINSIC_NAMES = {"__carry", "__scarry", "__sborrow", "__borrow"}


@dataclass
class FunctionScore:
    decompiler: str
    function_name: str
    compiler_variant: str       # e.g. "gcc -O2"
    source_similarity: float    # 0.0 – 1.0
    goto_count: int
    nesting_depth: int
    time_ms: int
    error: str | None = None
    semantic_score: float = 0.0         # fraction of test cases passed (0.0–1.0)
    semantic_error: str | None = None
    fail_category: str | None = None    # compile_error|runtime_error|timeout|assertion_fail|no_wrapper
    cases_passed: int = 0               # number of test cases passed
    cases_total: int = 0                # total number of test cases
    structural_penalty: float = 0.0     # 0.0–1.0 based on relative goto/nesting delta
    correctness_score: float = 0.0      # semantic-gated correctness score
    correctness_rank: int | None = None # set after all decompilers run
    readability_proxy_score: float | None = None  # unvalidated proxy evidence only
    composite_score: float = 0.0        # deprecated alias for correctness_score
    consensus_rank: int | None = None   # deprecated alias for correctness_rank
    uses_intrinsics: bool = False       # True if decompiled code uses __carry/__scarry etc.
    decompiled_code: str = ""           # primary surface used for scoring (NIR for Fission)
    # Dual NIR/HIR surfaces when the adapter provides them (Fission dual printers).
    # Semantic oracle always scores NIR; readability proxies prefer HIR.
    decompiled_code_nir: str = ""
    decompiled_code_hir: str = ""
    pseudocode_layer: str = ""          # adapter-reported layer selection, e.g. "nir"
    readability_metrics: dict[str, Any] = field(default_factory=dict)
    # Optional second readability pass on HIR (when dual surfaces differ).
    readability_metrics_hir: dict[str, Any] = field(default_factory=dict)
    readability_proxy_score_hir: float | None = None
    ast_similarity: dict[str, Any] = field(default_factory=dict)
    output_diagnostics: dict[str, Any] = field(default_factory=dict)


# ── Correctness Score ─────────────────────────────────────────────────────────

# Weights for the correctness formula.
#
# Readability proxies and Phase 2 AST source-similarity evidence are deliberately
# excluded from correctness ranking. They remain separately reported evidence
# until the human comprehension study validates a future readability composite.
WEIGHT_SEMANTIC = 0.80
WEIGHT_AST = 0.0
WEIGHT_READABILITY = 0.0
WEIGHT_SIMILARITY = 0.10
WEIGHT_STRUCTURAL = 0.10

# If semantic == 0, correctness is capped at this value.
SEMANTIC_ZERO_CAP = 0.15


def compute_correctness_score(
    semantic_score: float,
    source_similarity: float,
    structural_penalty: float,
    ast_score: float = 0.0,
    readability_score: float = 0.0,
) -> float:
    """
    Compute semantic-gated correctness score.

    Formula: sem * 0.80 + sim * 0.10 + (1 - structural_penalty) * 0.10

    Gating: if semantic_score == 0.0, correctness cannot exceed SEMANTIC_ZERO_CAP (0.15).
    This ensures that a binary that compiles/runs but fails all tests, or fails to
    compile entirely, cannot be ranked above a binary that passes even one test case.

    The ast_score and readability_score parameters are accepted for compatibility
    with older callers, but they do not affect correctness_score.
    """
    _ = ast_score, readability_score
    raw = (
        semantic_score * WEIGHT_SEMANTIC
        + source_similarity * WEIGHT_SIMILARITY
        + (1.0 - structural_penalty) * WEIGHT_STRUCTURAL
    )
    if semantic_score == 0.0:
        return round(min(raw, SEMANTIC_ZERO_CAP), 4)
    return round(raw, 4)


def compute_composite(
    semantic_score: float,
    source_similarity: float,
    structural_penalty: float,
) -> float:
    """Deprecated compatibility wrapper for compute_correctness_score."""
    return compute_correctness_score(semantic_score, source_similarity, structural_penalty)


# ── Structural Penalty ────────────────────────────────────────────────────────

def compute_structural_penalty(
    goto_count: int,
    nesting_depth: int,
    source_goto_count: int = 0,
    source_nesting_depth: int = 0,
) -> float:
    """
    Compute structural penalty based on relative increase vs original source.

    If the original source already uses gotos, no penalty for matching count.
    Penalty increases linearly: 5 extra gotos → 100% goto penalty.
    """
    goto_delta = max(0, goto_count - source_goto_count)
    goto_pen = min(goto_delta / 5.0, 1.0)

    depth_delta = max(0, nesting_depth - source_nesting_depth)
    depth_pen = min(depth_delta / 3.0, 1.0)

    return round(goto_pen * 0.7 + depth_pen * 0.3, 4)


# ── Normalizers & Similarity ──────────────────────────────────────────────────

def normalize_code(code: str) -> str:
    """Strip comments, normalize whitespace, lowercase identifiers."""
    code = re.sub(r"/\*.*?\*/", "", code, flags=re.DOTALL)
    code = re.sub(r"//[^\n]*", "", code)
    code = re.sub(r"\s+", " ", code).strip().lower()
    return code


def source_similarity(source: str, decompiled: str) -> float:
    """Normalized SequenceMatcher ratio on normalized code."""
    if not decompiled.strip():
        return 0.0
    a = normalize_code(source)
    b = normalize_code(decompiled)
    return round(difflib.SequenceMatcher(None, a, b).ratio(), 4)


def extract_function_source(source: str, function_name: str) -> str:
    """
    Extract one C function body from a source file.

    This deliberately avoids a full C parser, but it handles the corpus style:
    top-level function definitions with balanced braces and no preprocessor tricks
    inside signatures. If extraction fails, callers can fall back to whole-file
    source so benchmark runs keep producing data.
    """
    pattern = re.compile(
        rf"(^|\n)\s*[\w\s\*]+?\b{re.escape(function_name)}\s*\([^;{{}}]*\)\s*\{{",
        re.MULTILINE,
    )
    match = pattern.search(source)
    if not match:
        return ""

    start = match.start()
    brace_start = source.find("{", match.end() - 1)
    if brace_start == -1:
        return ""

    depth = 0
    for idx in range(brace_start, len(source)):
        ch = source[idx]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return source[start : idx + 1].strip()
    return ""


def check_uses_intrinsics(code: str) -> bool:
    """Return True if decompiled code uses any SLEIGH intrinsic functions."""
    for name in INTRINSIC_NAMES:
        if name in code:
            return True
    return False


def count_gotos(code: str) -> int:
    return len(re.findall(r"\bgoto\b", code))


def measure_nesting_depth(code: str) -> int:
    """Estimate maximum nesting depth by brace counting."""
    depth = 0
    max_depth = 0
    for ch in code:
        if ch == "{":
            depth += 1
            max_depth = max(max_depth, depth)
        elif ch == "}":
            depth = max(0, depth - 1)
    return max_depth


def structural_score(code: str) -> tuple[int, int]:
    """Returns (goto_count, max_nesting_depth)."""
    return count_gotos(code), measure_nesting_depth(code)


# ── Consensus Ranking ─────────────────────────────────────────────────────────

def assign_consensus_ranks(
    scores: list[FunctionScore],
    source_goto_counts: dict[str, int] | None = None,
    source_nesting_depths: dict[str, int] | None = None,
) -> list[FunctionScore]:
    """
    For the same function+variant, rank decompilers by correctness_score desc.

    Also assigns structural_penalty and correctness_score for each score entry.

    Consensus interpretation:
      - All decompilers rank low  → objectively hard function
      - Only Fission ranks low    → Fission quality issue
    """
    from collections import defaultdict

    src_gotos = source_goto_counts or {}
    src_depths = source_nesting_depths or {}

    # First pass: compute structural penalty and correctness score for each entry.
    for s in scores:
        if s.error is None:
            s.structural_penalty = compute_structural_penalty(
                s.goto_count,
                s.nesting_depth,
                src_gotos.get(s.function_name, 0),
                src_depths.get(s.function_name, 0),
            )
            s.correctness_score = compute_correctness_score(
                s.semantic_score,
                s.source_similarity,
                s.structural_penalty,
            )
            s.composite_score = s.correctness_score
            s.uses_intrinsics = s.uses_intrinsics or check_uses_intrinsics(s.decompiled_code)

    # Group by (function_name, compiler_variant)
    groups: dict[tuple, list[FunctionScore]] = defaultdict(list)
    for s in scores:
        groups[(s.function_name, s.compiler_variant)].append(s)

    result = []
    for group in groups.values():
        valid = [s for s in group if s.error is None]
        # Rank by correctness_score descending (semantic-gated).
        valid.sort(key=lambda s: s.correctness_score, reverse=True)
        current_rank = 1
        for idx, s in enumerate(valid):
            if idx > 0 and s.correctness_score < valid[idx - 1].correctness_score:
                current_rank = idx + 1
            s.correctness_rank = current_rank
            s.consensus_rank = current_rank
        # errored entries get no rank
        result.extend(group)

    return result


# ── Consensus Badge ───────────────────────────────────────────────────────────

def get_consensus_badge(
    function_name: str,
    compiler_variant: str,
    scores: list[FunctionScore],
    fission_decompiler_name: str = "fission",
    low_threshold: float = 0.20,
) -> str:
    """
    Return a consensus badge for a function+variant group.

    🔴 Fission-only gap: Fission is low but others are not
    ⚪ Universally low (harness): All decompilers are low under the current
        test harness — may indicate a common wrapper/ABI issue rather than
        an objectively hard function
    🟢 Fission leads: Fission is #1
    """
    group = [
        s for s in scores
        if s.function_name == function_name
        and s.compiler_variant == compiler_variant
        and s.error is None
    ]
    if not group:
        return ""

    fission_scores = [s for s in group if s.decompiler == fission_decompiler_name]
    other_scores = [s for s in group if s.decompiler != fission_decompiler_name]

    if not fission_scores:
        return ""

    fission_correctness = fission_scores[0].correctness_score
    others_correctness = [s.correctness_score for s in other_scores]

    # Fission leads
    if fission_scores[0].correctness_rank == 1:
        return "🟢 Fission leads"

    # All decompilers low under the current harness
    all_low = fission_correctness < low_threshold and all(c < low_threshold for c in others_correctness)
    if all_low:
        return "⚪ Universally low (harness)"

    # Fission-only gap: Fission is low, but at least one other is clearly higher
    others_avg = sum(others_correctness) / len(others_correctness) if others_correctness else 0.0
    if fission_correctness < low_threshold and others_avg > low_threshold * 2:
        return "🔴 Fission-only gap"

    return ""
