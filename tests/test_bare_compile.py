"""Unit tests for bare-compile and quality-extension aggregates."""
from __future__ import annotations

from runner.bare_compile import (
    aggregate_bare_compile,
    aggregate_readability_axis,
    aggregate_track_taxonomy,
    classify_isa_format,
    classify_track,
    try_bare_compile,
)
from runner.standard_summary import build_standard_summary


def test_bare_compile_accepts_simple_function() -> None:
    code = "int add(int a, int b) { return a + b; }\n"
    result = try_bare_compile(code)
    assert result["ok"] is True
    assert result["category"] == "ok"


def test_bare_compile_rejects_garbage() -> None:
    result = try_bare_compile("this is not c {{{{")
    assert result["ok"] is False
    assert result["category"] in {"compile_error", "timeout"}


def test_classify_track_realworld_and_isa() -> None:
    assert (
        classify_track(
            binary="corpus/realworld/binaries/util_main.exe",
            function_name="util_hash",
            corpus="realworld",
        )
        == "realworld"
    )
    assert classify_track(binary="binaries/control_flow_gcc_O2.exe", function_name="clamp") == "dev"
    assert classify_isa_format("hello_elf_x86_64")["format"] in {"elf", "unknown"}
    assert classify_isa_format("foo.exe")["format"] == "pe"


def test_standard_summary_includes_extensions() -> None:
    rows = [
        {
            "decompiler": "fission",
            "function_name": "clamp",
            "compiler_variant": "gcc -O0",
            "error": None,
            "fail_category": "",
            "semantic_score": 1.0,
            "goto_count": 0,
            "nesting_depth": 1,
            "decompiled_code": "int clamp(int v,int lo,int hi){return v;}\n",
            "bare_compile": {"ok": True, "category": "ok", "error": None},
            "track": "dev",
            "isa_format": {"isa": "x86_64", "format": "pe"},
            "binary": "binaries/control_flow_gcc_O0.exe",
            "readability_metrics": {
                "structured_control_flow": {"raw": {"goto_count": 0}},
                "expression_complexity": {
                    "raw": {"temporary_identifier_loc_ratio": 0.1}
                },
            },
            "readability_proxy_score": 0.8,
            "output_diagnostics": {"status": "direct_function"},
        },
        {
            "decompiler": "fission",
            "function_name": "util_hash",
            "compiler_variant": "gcc -O2",
            "error": None,
            "fail_category": "timeout",
            "semantic_score": 0.0,
            "goto_count": 2,
            "track": "realworld",
            "bare_compile": {"ok": False, "category": "compile_error", "error": "x"},
            "isa_format": {"isa": "x86_64", "format": "pe"},
            "binary": "corpus/realworld/binaries/x.exe",
            "decompiled_code": "int util_hash(){ zf = 1; goto L; L: return 0; }\n",
            "output_diagnostics": {"status": "direct_function"},
        },
    ]
    summary = build_standard_summary(rows)
    assert "bare_compile" in summary["extensions"]
    assert "readability_axis" in summary["extensions"]
    assert "tracks" in summary["extensions"]
    bare = summary["extensions"]["bare_compile"]["by_decompiler"]["fission"]
    assert bare["attempted"] == 2
    assert bare["ok"] == 1
    tracks = summary["extensions"]["tracks"]["by_track"]
    assert "dev" in tracks
    assert "realworld" in tracks
    assert summary["diagnostics"]["bare_compile"]["ranking"] is False


def test_aggregate_helpers_do_not_rank() -> None:
    rows = [
        {
            "decompiler": "ghidra",
            "bare_compile": {"ok": True, "category": "ok"},
            "goto_count": 1,
            "decompiled_code": "int f(){ return 0; }",
            "semantic_score": 1.0,
            "track": "dev",
        }
    ]
    assert aggregate_bare_compile(rows)["ranking"] is False
    assert aggregate_readability_axis(rows)["ranking"] is False
    assert aggregate_track_taxonomy(rows)["ranking"] is False
