"""ELF / multi-ABI oracle profile selection."""
from __future__ import annotations

from docker.oracle import server as oracle_server


def test_compiler_profile_pe_default() -> None:
    abi, compiler, wine, runner = oracle_server.compiler_profile("gcc -O0")
    assert abi == "windows-x86_64"
    assert "mingw" in compiler
    assert runner == "wine"
    assert wine == "win64"


def test_compiler_profile_pe_m32() -> None:
    abi, compiler, wine, runner = oracle_server.compiler_profile("gcc-m32 -O0")
    assert abi == "windows-x86"
    assert runner == "wine"
    assert wine == "win32"


def test_compiler_profile_elf_x64() -> None:
    abi, compiler, wine, runner = oracle_server.compiler_profile(
        "gcc-elf -O0",
        target_abi="linux-x86_64",
        binary_format="elf",
    )
    assert abi == "linux-x86_64"
    assert compiler == "gcc"
    assert runner == "native"
    assert wine == ""


def test_compiler_profile_elf_aarch64() -> None:
    abi, compiler, wine, runner = oracle_server.compiler_profile(
        "gcc-aarch64 -O0",
        target_abi="linux-aarch64",
        binary_format="elf",
    )
    assert abi == "linux-aarch64"
    assert "aarch64" in compiler
    assert runner == "qemu"


def test_is_elf_and_pe_magic() -> None:
    assert oracle_server.is_pe_bytes(b"MZ\x90\x00")
    assert oracle_server.is_elf_bytes(b"\x7fELF\x02\x01")
    assert not oracle_server.is_pe_bytes(b"\x7fELF")
    assert not oracle_server.is_elf_bytes(b"MZ")


def test_classify_isa_prefers_explicit_tags() -> None:
    from runner.bare_compile import classify_isa_format, classify_track

    tags = classify_isa_format(
        "binaries/c/control_flow_gcc-aarch64_O0",
        isa="aarch64",
        fmt="elf",
    )
    assert tags == {"isa": "aarch64", "format": "elf"}
    track = classify_track(
        binary="binaries/c/control_flow_gcc-elf_x64_O0",
        function_name="count_bits",
        language="c",
        fmt="elf",
    )
    assert track == "multi_isa"
    assert classify_track(function_name="cpp_add_ints", language="cpp") == "lang_cpp"
    assert classify_track(function_name="rust_add_ints", language="rust") == "lang_rust"
    assert classify_track(function_name="go_add_ints", language="go") == "lang_go"
