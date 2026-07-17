"""Rust corpus family + lang_rust profile."""
from __future__ import annotations

from pathlib import Path

from runner.corpus import Corpus
from runner.matrix_profile import get_profile
from runner.test_wrappers import TEST_WRAPPERS

ROOT = Path(__file__).resolve().parents[1]


def test_rust_patterns_source_exists() -> None:
    src = ROOT / "corpus/dev/source/rust/patterns.rs"
    man = ROOT / "corpus/dev/manifests/rust_patterns.json"
    assert src.is_file()
    assert man.is_file()
    text = src.read_text(encoding="utf-8")
    assert "#[no_mangle]" in text
    assert 'extern "C"' in text
    assert "fn rust_add_ints" in text


def test_rust_functions_load_as_rust_language() -> None:
    c = Corpus.load_all("dev")
    rust = [f for f in c.functions if f.language == "rust"]
    expected = {
        "rust_add_ints",
        "rust_clamp_int",
        "rust_max3",
        "rust_count_bits",
        "rust_dot_product",
        "rust_cstr_len",
        "rust_sum_range",
        "rust_saturating_add",
    }
    names = {f.name for f in rust}
    assert expected <= names
    for fn in rust:
        if fn.name in expected:
            assert fn.source.endswith("patterns.rs")
            assert all(v.compiler == "rustc" for v in fn.compiler_variants)
            assert all(v.format == "pe" for v in fn.compiler_variants)


def test_lang_rust_profile_selects_rust_only() -> None:
    c = Corpus.load_all("dev").apply_profile("lang_rust")
    assert c.functions
    assert all(f.language == "rust" for f in c.functions)
    assert all(
        v.compiler == "rustc" and v.opt in {"-O0", "-O2"}
        for f in c.functions
        for v in f.compiler_variants
    )


def test_rust_wrappers_present() -> None:
    for name in (
        "rust_add_ints",
        "rust_clamp_int",
        "rust_max3",
        "rust_count_bits",
        "rust_dot_product",
        "rust_cstr_len",
        "rust_sum_range",
        "rust_saturating_add",
    ):
        assert name in TEST_WRAPPERS
        assert len(TEST_WRAPPERS[name]) >= 5


def test_lang_rust_profile_documented() -> None:
    prof = get_profile("lang_rust")
    assert prof is not None
    assert "rust" in prof["languages"]
    assert "rust_add_ints" in (prof.get("function_allowlist") or [])
