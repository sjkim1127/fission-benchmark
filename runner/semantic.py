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

// SLEIGH/Fission intrinsics stubs
#define __carry(a, b) 0
#define __scarry(a, b) 0
#define __sborrow(a, b) 0
#define __borrow(a, b) 0
#define __popcount(x) __builtin_popcount(x)
"""

def verify_semantic_correctness(func_name: str, decompiled_code: str) -> tuple[float, str | None]:
    """
    Verify correctness of decompiled code.
    Returns (score, error_detail). Score is 1.0 on success, 0.0 on failure.
    """
    if func_name not in TEST_WRAPPERS:
        return 0.0, f"No test wrapper defined for function {func_name}"
        
    if not decompiled_code.strip():
        return 0.0, "Empty decompilation output"

    # If the decompiler prefixed the function name with an underscore (common in 32-bit PE symbols),
    # define an alias so the test wrapper compiles successfully.
    alias = ""
    if f" _{func_name}" in decompiled_code or f" *_{func_name}" in decompiled_code:
        alias = f"#define {func_name} _{func_name}\n"
    
    source = STANDARD_HEADER + "\n" + alias + decompiled_code + "\n" + TEST_WRAPPERS[func_name]

    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        c_file = tmpdir_path / "test.c"
        bin_file = tmpdir_path / "test"
        
        c_file.write_text(source, encoding="utf-8")
        
        # Compile using host gcc
        try:
            result = subprocess.run(
                ["gcc", "-w", "-O0", str(c_file), "-o", str(bin_file)],
                capture_output=True,
                text=True,
                timeout=5.0
            )
            if result.returncode != 0:
                return 0.0, f"Compilation failed:\n{result.stderr}"
        except subprocess.TimeoutExpired:
            return 0.0, "Compilation timed out (5s limit)"
        except Exception as e:
            return 0.0, f"Compiler execution failed: {e}"
            
        # Run binary
        try:
            run_res = subprocess.run(
                [str(bin_file)],
                capture_output=True,
                text=True,
                timeout=1.0
            )
            if run_res.returncode == 0:
                return 1.0, None
            else:
                return 0.0, f"Runtime verification failed (exit code {run_res.returncode})"
        except subprocess.TimeoutExpired:
            return 0.0, "Runtime verification timed out (1.0s limit) - potential infinite loop"
        except Exception as e:
            return 0.0, f"Runtime execution failed: {e}"
            
    return 0.0, "Unknown verification error"
