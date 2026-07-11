"""
Semantic verification engine.
Compiles decompiled functions and runs them against unit test wrappers.
"""
import asyncio
import re
import subprocess
import tempfile
from pathlib import Path
try:
    from .test_wrappers import TEST_WRAPPERS
except ImportError:  # Direct script/module execution from runner/.
    from test_wrappers import TEST_WRAPPERS

STANDARD_HEADER = """
#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

// Common decompiler types
typedef uint8_t byte;
typedef uint16_t word;
typedef uint32_t dword;
typedef uint64_t qword;
typedef int32_t undefined4;
typedef int64_t undefined8;
typedef int16_t undefined2;
typedef int8_t undefined1;
typedef int32_t undefined;

typedef unsigned int uint;
typedef unsigned long ulong;
typedef unsigned short ushort;
typedef unsigned char uchar;
typedef unsigned long long ulonglong;
typedef long long longlong;

// Structures used in corpus
typedef struct Pair {
    int key;
    int value;
} Pair;

// SLEIGH/Fission intrinsics — type-generic computation-based implementations
#define __carry(a, b)   (__builtin_add_overflow((a), (b), &(__typeof__(a)){0}))
#define __borrow(a, b)  ((a) < (b))
// Signed overflow detection: result sign differs from both operands' sign
#define __scarry(a, b)  (__builtin_add_overflow(((__typeof__(a))(a)), ((__typeof__(a))(b)), &((__typeof__(a)){0})))
#define __sborrow(a, b) (__builtin_sub_overflow(((__typeof__(a))(a)), ((__typeof__(a))(b)), &((__typeof__(a)){0})))

#define __popcount(x) __builtin_popcount(x)
"""


def extract_function_declaration(
    func_name: str,
    decompiled_code: str,
) -> str | None:
    """Extract the target definition's signature as an extern declaration."""
    names = [f"_{func_name}", func_name]
    for name in names:
        pattern = re.compile(
            rf"(?m)^[ \t]*(?P<signature>[^;{{}}\n]*\b{re.escape(name)}\s*\([^;{{}}]*\))\s*\{{"
        )
        match = pattern.search(decompiled_code)
        if match:
            signature = " ".join(match.group("signature").split())
            if signature.startswith("static "):
                return None
            return f"extern {signature};\n"
    return None


def verify_semantic_correctness(
    func_name: str,
    decompiled_code: str,
) -> tuple[float | None, str | None, str, int, int]:
    """
    Verify correctness of decompiled code by running all test cases.

    Returns:
        (score, error_detail, fail_category, cases_passed, cases_total)

    score: fraction of test cases passed (0.0–1.0)
    fail_category: one of:
        "no_wrapper"      — no test wrapper defined for this function
        "compile_error"   — GCC compilation failed
        "timeout"         — compilation or runtime exceeded time limit
        "runtime_error"   — binary exited with non-zero code (assertion failed or crash)
        "assertion_fail"  — all cases ran but at least one returned non-zero
        ""                — fully passed
    """
    if func_name not in TEST_WRAPPERS:
        # "no_wrapper" means the function is untestable, not that it failed.
        # Return None semantic_score so correctness ranking can treat this separately.
        return None, f"No test wrapper defined for function {func_name}", "no_wrapper", 0, 0

    if not decompiled_code.strip():
        return 0.0, "Empty decompilation output", "compile_error", 0, 0

    cases = TEST_WRAPPERS[func_name]
    if not cases:
        return None, "No test cases defined", "no_wrapper", 0, 0

    cases_total = len(cases)
    cases_passed = 0
    last_error = None
    last_category = ""

    # If the decompiler prefixed the function name with an underscore (common in 32-bit PE symbols),
    # define an alias so the test wrapper compiles successfully.
    alias = ""
    if f" _{func_name}" in decompiled_code or f" *_{func_name}" in decompiled_code:
        alias = f"#define {func_name} _{func_name}\n"

    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        declaration = extract_function_declaration(func_name, decompiled_code)
        if declaration is None:
            return 0.0, "Target function declaration not found", "compile_error", 0, cases_total
        function_file = tmpdir_path / "decompiled_function.c"
        function_object = tmpdir_path / "decompiled_function.o"
        function_file.write_text(STANDARD_HEADER + "\n" + decompiled_code, encoding="utf-8")

        try:
            result = subprocess.run(
                [
                    "gcc",
                    "-w",
                    "-O0",
                    "-c",
                    str(function_file),
                    "-o",
                    str(function_object),
                ],
                capture_output=True,
                text=True,
                timeout=5.0,
            )
            if result.returncode != 0:
                error = f"Compilation failed:\n{result.stderr[:300]}"
                return 0.0, error, "compile_error", 0, cases_total
        except subprocess.TimeoutExpired:
            return 0.0, "Compilation timed out (5s)", "timeout", 0, cases_total
        except Exception as e:
            return 0.0, f"Compiler execution failed: {e}", "compile_error", 0, cases_total

        for i, case_main in enumerate(cases):
            wrapper_file = tmpdir_path / f"wrapper_{i}.c"
            bin_file = tmpdir_path / f"semantic_case_{i}"
            wrapper_file.write_text(
                STANDARD_HEADER + "\n" + alias + declaration + case_main,
                encoding="utf-8",
            )
            try:
                result = subprocess.run(
                    [
                        "gcc",
                        "-w",
                        "-O0",
                        str(wrapper_file),
                        str(function_object),
                        "-o",
                        str(bin_file),
                    ],
                    capture_output=True,
                    text=True,
                    timeout=5.0,
                )
                if result.returncode != 0:
                    last_error = f"Case {i}: Compilation failed:\n{result.stderr[:300]}"
                    last_category = "compile_error"
                    continue
            except subprocess.TimeoutExpired:
                last_error = f"Case {i}: Compilation timed out (5s)"
                last_category = "timeout"
                continue
            except Exception as e:
                last_error = f"Case {i}: Compiler execution failed: {e}"
                last_category = "compile_error"
                continue

            # Run
            try:
                run_res = subprocess.run(
                    [str(bin_file)],
                    capture_output=True,
                    text=True,
                    timeout=2.0,
                )
                if run_res.returncode == 0:
                    cases_passed += 1
                else:
                    last_error = f"Case {i}: Runtime failed (exit code {run_res.returncode})"
                    last_category = "runtime_error"
            except subprocess.TimeoutExpired:
                last_error = f"Case {i}: Runtime timed out (2s) — potential infinite loop"
                last_category = "timeout"
            except Exception as e:
                last_error = f"Case {i}: Runtime execution failed: {e}"
                last_category = "runtime_error"

    score = cases_passed / cases_total if cases_total > 0 else 0.0

    if cases_passed == cases_total:
        return score, None, "", cases_passed, cases_total
    else:
        return score, last_error, last_category or "assertion_fail", cases_passed, cases_total


async def verify_semantic_correctness_async(
    func_name: str,
    decompiled_code: str,
) -> tuple[float | None, str | None, str, int, int]:
    """Async wrapper for verify_semantic_correctness.

    Runs the blocking GCC compilation and execution in a thread pool so that the
    asyncio event loop is not blocked during parallel batch decompilation scoring.
    Use this from async contexts (runner.py decompile_batch_and_score).
    """
    return await asyncio.to_thread(verify_semantic_correctness, func_name, decompiled_code)
