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

// Structures used in corpus
typedef struct Pair {
    int key;
    int value;
} Pair;
"""

def verify_semantic_correctness(func_name: str, decompiled_code: str) -> float:
    """
    Verify correctness of decompiled code.
    Returns 1.0 if correct (compiles and passes all tests), 0.0 otherwise.
    """
    if func_name not in TEST_WRAPPERS:
        return 0.0
        
    if not decompiled_code.strip():
        return 0.0

    # Ghidra and others sometimes output comments or headers before function code.
    # The scoring engine's extract_function_source strips some of it, but we prepend headers anyway.
    source = STANDARD_HEADER + "\n" + decompiled_code + "\n" + TEST_WRAPPERS[func_name]

    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        c_file = tmpdir_path / "test.c"
        bin_file = tmpdir_path / "test"
        
        c_file.write_text(source, encoding="utf-8")
        
        # Compile using host gcc
        try:
            # -w suppresses all warnings
            # -O0 compiles faster and avoids compiler optimization transformations
            result = subprocess.run(
                ["gcc", "-w", "-O0", str(c_file), "-o", str(bin_file)],
                capture_output=True,
                text=True,
                timeout=5.0
            )
            if result.returncode != 0:
                # Compilation failed
                return 0.0
        except Exception:
            # Compiler not found or timeout
            return 0.0
            
        # Run binary
        try:
            run_res = subprocess.run(
                [str(bin_file)],
                capture_output=True,
                timeout=1.0
            )
            if run_res.returncode == 0:
                return 1.0
        except Exception:
            # Timeout (infinite loop) or crash
            return 0.0
            
    return 0.0
