"""Go corpus family + lang_go profile."""
from __future__ import annotations

from pathlib import Path

from runner.corpus import Corpus
from runner.matrix_profile import get_profile
from runner.test_wrappers import TEST_WRAPPERS

ROOT = Path(__file__).resolve().parents[1]


def test_go_patterns_package_exists() -> None:
    pkg = ROOT / "corpus/dev/source/go/patterns"
    man = ROOT / "corpus/dev/manifests/go_patterns.json"
    assert (pkg / "main.go").is_file()
    assert (pkg / "go.mod").is_file()
    assert man.is_file()
    text = (pkg / "main.go").read_text(encoding="utf-8")
    assert "//export go_add_ints" in text
    assert "package main" in text


def test_go_functions_load_as_go_language() -> None:
    c = Corpus.load_all("dev")
    go_fns = [f for f in c.functions if f.language == "go"]
    expected = {
        "go_add_ints",
        "go_clamp_int",
        "go_max3",
        "go_count_bits",
        "go_dot_product",
        "go_cstr_len",
        "go_sum_range",
        "go_saturating_add",
    }
    names = {f.name for f in go_fns}
    assert expected <= names
    for fn in go_fns:
        if fn.name in expected:
            assert "patterns" in fn.source
            assert all(v.compiler == "go" for v in fn.compiler_variants)
            assert all(v.format == "pe" for v in fn.compiler_variants)


def test_lang_go_profile_selects_go_only() -> None:
    c = Corpus.load_all("dev").apply_profile("lang_go")
    assert c.functions
    assert all(f.language == "go" for f in c.functions)
    assert all(
        v.compiler == "go" and v.opt in {"noopt", "default"}
        for f in c.functions
        for v in f.compiler_variants
    )


def test_go_wrappers_present() -> None:
    for name in (
        "go_add_ints",
        "go_clamp_int",
        "go_max3",
        "go_count_bits",
        "go_dot_product",
        "go_cstr_len",
        "go_sum_range",
        "go_saturating_add",
    ):
        assert name in TEST_WRAPPERS
        assert len(TEST_WRAPPERS[name]) >= 5


def test_lang_go_profile_documented() -> None:
    prof = get_profile("lang_go")
    assert prof is not None
    assert "go" in prof["languages"]
    assert "go_add_ints" in (prof.get("function_allowlist") or [])
