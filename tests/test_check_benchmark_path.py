import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _load():
    path = ROOT / "scripts" / "check_benchmark_path.py"
    spec = importlib.util.spec_from_file_location("check_benchmark_path", path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_check_benchmark_path_accepts_standard_envelope(tmp_path: Path) -> None:
    from runner.run_validity import build_envelope

    row = {
        "decompiler": "fission",
        "function_name": "clamp",
        "compiler_variant": "gcc -O0",
        "source_similarity": 0.5,
        "semantic_score": 1.0,
        "correctness_score": 1.0,
        "correctness_rank": 1,
        "structural_penalty": 0.0,
        "time_ms": 10,
        "cases_passed": 5,
        "cases_total": 5,
        "error": None,
        "fail_category": "",
    }
    envelope = build_envelope(
        [row],
        run_meta={"official": False, "corpus": "dev"},
        matrix={
            "expected_decompilers": ["fission"],
            "expected_rows": 1,
            "observed_rows": 1,
            "expected_cells": [
                {
                    "decompiler": "fission",
                    "function_name": "clamp",
                    "compiler_variant": "gcc -O0",
                }
            ],
        },
    )
    path = tmp_path / "env.json"
    path.write_text(json.dumps(envelope), encoding="utf-8")
    mod = _load()
    assert mod.main([str(path)]) == 0


def test_check_benchmark_path_flags_correctness_drift(tmp_path: Path) -> None:
    from runner.run_validity import build_envelope

    row = {
        "decompiler": "fission",
        "function_name": "clamp",
        "compiler_variant": "gcc -O0",
        "source_similarity": 0.9,
        "semantic_score": 1.0,
        "correctness_score": 1.0,
        "correctness_rank": 1,
        "structural_penalty": 0.0,
        "time_ms": 10,
        "cases_passed": 5,
        "cases_total": 5,
        "error": None,
        "fail_category": "",
    }
    envelope = build_envelope(
        [row],
        run_meta={"official": False, "corpus": "dev"},
        matrix={
            "expected_decompilers": ["fission"],
            "expected_rows": 1,
            "observed_rows": 1,
            "expected_cells": [
                {
                    "decompiler": "fission",
                    "function_name": "clamp",
                    "compiler_variant": "gcc -O0",
                }
            ],
        },
    )
    # Inject composite-style drift after envelope build.
    envelope["rows"][0]["correctness_score"] = 0.5
    envelope["rows"][0]["semantic_score"] = 1.0
    path = tmp_path / "bad.json"
    path.write_text(json.dumps(envelope), encoding="utf-8")
    mod = _load()
    assert mod.main([str(path)]) == 1
