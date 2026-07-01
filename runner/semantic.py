"""
Semantic verification engine.
Compiles decompiled functions and runs them against unit test wrappers.
"""
import subprocess
import tempfile
from pathlib import Path
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

// SLEIGH/Fission intrinsics — actual computation-based implementations
// __carry: 1 if unsigned addition overflows 32-bit
static inline int __carry(unsigned int a, unsigned int b) {
    return ((uint64_t)a + (uint64_t)b) > (uint64_t)UINT_MAX ? 1 : 0;
}

// __scarry: 1 if signed addition overflows
static inline int __scarry(int a, int b) {
    long long r = (long long)a + (long long)b;
    return (r > INT_MAX || r < INT_MIN) ? 1 : 0;
}

// __sborrow: 1 if signed subtraction overflows
static inline int __sborrow(int a, int b) {
    long long r = (long long)a - (long long)b;
    return (r > INT_MAX || r < INT_MIN) ? 1 : 0;
}

// __borrow: 1 if unsigned subtraction would borrow (a < b)
static inline int __borrow(unsigned int a, unsigned int b) {
    return a < b ? 1 : 0;
}

#define __popcount(x) __builtin_popcount(x)
"""


def verify_semantic_correctness(
    func_name: str,
    decompiled_code: str,
) -> tuple[float, str | None, str, int, int]:
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
        return 0.0, f"No test wrapper defined for function {func_name}", "no_wrapper", 0, 0

    if not decompiled_code.strip():
        return 0.0, "Empty decompilation output", "compile_error", 0, 0

    cases = TEST_WRAPPERS[func_name]
    if not cases:
        return 0.0, "No test cases defined", "no_wrapper", 0, 0

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

        for i, case_main in enumerate(cases):
            source = STANDARD_HEADER + "\n" + alias + decompiled_code + "\n" + case_main
            c_file = tmpdir_path / f"test_{i}.c"
            bin_file = tmpdir_path / f"test_{i}"

            c_file.write_text(source, encoding="utf-8")

            # Compile
            try:
                result = subprocess.run(
                    ["gcc", "-w", "-O0", str(c_file), "-o", str(bin_file)],
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
