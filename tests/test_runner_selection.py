from dataclasses import dataclass

import pytest

from runner.runner import filter_functions


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
