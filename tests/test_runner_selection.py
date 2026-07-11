from dataclasses import dataclass

import pytest

from runner.runner import (
    build_expected_cells,
    filter_functions,
    fission_toolchain_metadata,
    format_semantic_score,
)


@dataclass
class FunctionStub:
    name: str


def test_filter_functions_preserves_manifest_order() -> None:
    functions = [
        FunctionStub("alpha"),
        FunctionStub("beta"),
        FunctionStub("gamma"),
    ]

    selected = filter_functions(functions, "gamma,alpha")

    assert [fn.name for fn in selected] == ["alpha", "gamma"]


def test_filter_functions_rejects_unknown_names() -> None:
    functions = [FunctionStub("alpha")]

    with pytest.raises(ValueError, match=r"unknown function\(s\): missing"):
        filter_functions(functions, "missing")


def test_filter_functions_without_filter_returns_all() -> None:
    functions = [FunctionStub("alpha"), FunctionStub("beta")]

    assert filter_functions(functions, None) is functions


@pytest.mark.parametrize(
    ("score", "expected"),
    [(None, "n/a"), (0.0, "0.00"), (1.0, "1.00"), (1 / 3, "0.33")],
)
def test_format_semantic_score_preserves_untestable_state(
    score: float | None,
    expected: str,
) -> None:
    assert format_semantic_score(score) == expected


def test_fission_toolchain_metadata_uses_local_bundle_provenance(monkeypatch) -> None:
    monkeypatch.delenv("FISSION_VERSION", raising=False)
    monkeypatch.delenv("FISSION_RELEASE_VERSION", raising=False)
    monkeypatch.setenv("FISSION_GIT_SHA", "abc12345")
    monkeypatch.setenv("FISSION_SOURCE", "local")
    monkeypatch.setenv("FISSION_SOURCE_FINGERPRINT", "fingerprint")

    assert fission_toolchain_metadata() == {
        "fission_version": "local-abc12345",
        "fission_git_sha": "abc12345",
        "fission_source": "local",
        "fission_source_fingerprint": "fingerprint",
    }


def test_expected_cells_use_limited_execution_function_set() -> None:
    @dataclass
    class VariantStub:
        compiler: str
        opt: str

    @dataclass
    class PlannedFunctionStub:
        name: str
        compiler_variants: list[VariantStub]

    variant = VariantStub("gcc", "-O0")
    functions = [
        PlannedFunctionStub("first", [variant]),
        PlannedFunctionStub("second", [variant]),
    ]
    cells = build_expected_cells(functions[:1], ["fission", "ghidra"], 1)

    assert cells == [
        {"decompiler": "fission", "function_name": "first", "compiler_variant": "gcc -O0"},
        {"decompiler": "ghidra", "function_name": "first", "compiler_variant": "gcc -O0"},
    ]
