"""
Precompute structural metrics (goto count, nesting depth) from corpus C source files.

Run this once after adding new corpus files:
    python scripts/precompute_source_metrics.py

Writes corpus/source_metrics.json which is loaded by runner.py at benchmark time.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

CORPUS_ROOT = Path(__file__).parent.parent / "corpus"
OUTPUT_PATH = CORPUS_ROOT / "source_metrics.json"


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


def extract_function(source: str, function_name: str) -> str:
    """Extract a function body from C source."""
    pattern = re.compile(
        rf"(^|\n)\s*[\w\s\*]+?\b{re.escape(function_name)}\s*\([^;{{}}]*\)\s*\{{",
        re.MULTILINE,
    )
    match = pattern.search(source)
    if not match:
        return ""
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
                return source[match.start():idx + 1].strip()
    return ""


def discover_source_files(corpus_root: Path = CORPUS_ROOT) -> list[Path]:
    """Return authored corpus sources, excluding generated adapter output."""
    return sorted(
        source_path
        for source_dir in corpus_root.glob("*/source")
        for source_path in source_dir.rglob("*.c")
    )


def compute_metrics(corpus_root: Path = CORPUS_ROOT) -> dict:
    """Walk all corpus C source files and compute per-function metrics."""
    goto_counts: dict[str, int] = {}
    nesting_depths: dict[str, int] = {}

    source_files = discover_source_files(corpus_root)
    if not source_files:
        print(f"No authored .c source files found under {corpus_root}")
        return {"goto_counts": {}, "nesting_depths": {}}

    print(f"Found {len(source_files)} source files")

    # Discover function names from source files
    fn_pattern = re.compile(
        r"(^|\n)\s*[\w\s\*]+?\b(\w+)\s*\([^;{}]*\)\s*\{",
        re.MULTILINE,
    )

    for src_path in source_files:
        source = src_path.read_text(errors="replace")
        matches = fn_pattern.finditer(source)
        seen_in_file = set()

        for m in matches:
            fn_name = m.group(2)
            # Skip known non-function names
            if fn_name in ("if", "else", "for", "while", "do", "switch", "return", "main"):
                continue
            if fn_name in seen_in_file:
                continue
            seen_in_file.add(fn_name)

            body = extract_function(source, fn_name)
            if not body:
                continue

            gotos = count_gotos(body)
            depth = measure_nesting_depth(body)

            # Only record if not already seen (first definition wins)
            if fn_name not in goto_counts:
                goto_counts[fn_name] = gotos
                nesting_depths[fn_name] = depth
                if gotos > 0:
                    print(f"  {src_path.name}: {fn_name} has {gotos} goto(s), depth={depth}")

    print(f"\nComputed metrics for {len(goto_counts)} functions")
    return {"goto_counts": goto_counts, "nesting_depths": nesting_depths}


def main():
    print(f"Computing source structural metrics from {CORPUS_ROOT}")
    metrics = compute_metrics()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    print(f"✅ Written to {OUTPUT_PATH}")

    # Summary
    goto_fns = {k: v for k, v in metrics["goto_counts"].items() if v > 0}
    if goto_fns:
        print(f"\nFunctions with goto in source: {list(goto_fns.keys())}")
    else:
        print("\nNo functions with goto in source (good!)")


if __name__ == "__main__":
    main()
