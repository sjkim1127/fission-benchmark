"""
Scoring engine for multi-decompiler comparison.

Metrics:
  1. source_similarity  — normalized edit distance vs original C source
  2. structural_score   — goto count, nesting depth penalty
  3. consensus_rank     — relative position among all decompilers
"""
from __future__ import annotations

import difflib
import re
from dataclasses import dataclass


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
    consensus_rank: int | None = None   # set after all decompilers run


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


def assign_consensus_ranks(scores: list[FunctionScore]) -> list[FunctionScore]:
    """
    For the same function+variant, rank decompilers by source_similarity desc.
    Consensus interpretation:
      - All decompilers rank low  → objectively hard function
      - Only Fission ranks low    → Fission quality issue
    """
    # Group by (function_name, compiler_variant)
    from collections import defaultdict
    groups: dict[tuple, list[FunctionScore]] = defaultdict(list)
    for s in scores:
        groups[(s.function_name, s.compiler_variant)].append(s)

    result = []
    for group in groups.values():
        valid = [s for s in group if s.error is None]
        valid.sort(key=lambda s: s.source_similarity, reverse=True)
        for rank, s in enumerate(valid, start=1):
            s.consensus_rank = rank
        # errored entries get no rank
        result.extend(group)

    return result
