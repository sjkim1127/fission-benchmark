"""C++ corpus family + lang_cpp profile."""
from __future__ import annotations

from pathlib import Path

from runner.corpus import Corpus
from runner.matrix_profile import get_profile
from runner.test_wrappers import TEST_WRAPPERS

ROOT = Path(__file__).resolve().parents[1]


def test_cpp_patterns_manifest_and_source_exist() -> None:
    man = ROOT / "corpus/dev/manifests/cpp_patterns.json"
    src = ROOT / "corpus/dev/source/cpp/patterns.cpp"
    assert man.is_file()
    assert src.is_file()
    text = src.read_text(encoding="utf-8")
    assert 'extern "C"' in text
    assert "namespace fission_bench" in text


def test_cpp_functions_load_as_cpp_language() -> None:
    c = Corpus.load_all("dev")
    cpp = [f for f in c.functions if f.language == "cpp"]
    names = {f.name for f in cpp}
    expected = {
        "cpp_add_ints",
        "cpp_clamp_int",
        "cpp_max3",
        "cpp_count_bits",
        "cpp_dot_product",
        "cpp_cstr_len",
        "cpp_sum_range",
    }
    assert expected <= names
    for fn in cpp:
        if fn.name in expected:
            assert fn.source.endswith("patterns.cpp")
            assert all(v.compiler == "g++" for v in fn.compiler_variants)
            assert all(v.format == "pe" for v in fn.compiler_variants)


def test_lang_cpp_profile_selects_cpp_only() -> None:
    c = Corpus.load_all("dev").apply_profile("lang_cpp")
    assert c.functions
    assert all(f.language == "cpp" for f in c.functions)
    assert all(
        v.opt in {"-O0", "-O2"} and v.compiler == "g++"
        for f in c.functions
        for v in f.compiler_variants
    )


def test_cpp_wrappers_present() -> None:
    for name in (
        "cpp_add_ints",
        "cpp_clamp_int",
        "cpp_max3",
        "cpp_count_bits",
        "cpp_dot_product",
        "cpp_cstr_len",
        "cpp_sum_range",
    ):
        assert name in TEST_WRAPPERS
        assert len(TEST_WRAPPERS[name]) >= 5


def test_lang_cpp_profile_documented() -> None:
    prof = get_profile("lang_cpp")
    assert prof is not None
    assert "cpp" in prof["languages"]
    assert "cpp_add_ints" in (prof.get("function_allowlist") or [])
