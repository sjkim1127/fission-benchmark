"""Multi-ISA ELF variants + multi_isa profile."""
from __future__ import annotations

from runner.corpus import Corpus
from runner.matrix_profile import get_profile


def test_control_flow_has_elf_x64_and_aarch64_variants() -> None:
    c = Corpus.load_all("dev")
    by_name = {f.name: f for f in c.functions}
    for name in ("count_bits", "clamp", "signum"):
        fn = by_name[name]
        keys = {(v.compiler, v.opt, v.format, v.isa) for v in fn.compiler_variants}
        assert ("gcc-elf", "-O0", "elf", "x86_64") in keys
        assert ("gcc-elf", "-O2", "elf", "x86_64") in keys
        assert ("gcc-aarch64", "-O0", "elf", "aarch64") in keys
        assert ("gcc-aarch64", "-O2", "elf", "aarch64") in keys
        # PE still present
        assert any(v.format == "pe" for v in fn.compiler_variants)


def test_multi_isa_profile_includes_elf_and_pe() -> None:
    c = Corpus.load_all("dev").apply_profile("multi_isa")
    names = {f.name for f in c.functions}
    assert names == {"count_bits", "clamp", "signum"}
    formats = {v.format for f in c.functions for v in f.compiler_variants}
    isas = {v.isa for f in c.functions for v in f.compiler_variants}
    compilers = {v.compiler for f in c.functions for v in f.compiler_variants}
    assert "pe" in formats
    assert "elf" in formats
    assert "x86_64" in isas
    assert "aarch64" in isas or "x86_32" in isas
    assert "gcc-elf" in compilers
    assert "gcc-aarch64" in compilers


def test_multi_isa_profile_documented() -> None:
    prof = get_profile("multi_isa")
    assert prof is not None
    assert "elf" in prof["formats"]
    assert "gcc-aarch64" in prof["compilers"]
    assert "count_bits" in (prof.get("function_allowlist") or [])
