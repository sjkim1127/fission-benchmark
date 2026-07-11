from types import SimpleNamespace

from runner.semantic import extract_function_declaration, verify_semantic_correctness
from runner.test_wrappers import TEST_WRAPPERS


def test_extract_function_declaration_preserves_signature() -> None:
    declaration = extract_function_declaration(
        "identity",
        "int identity(int value) { return value; }",
    )

    assert declaration == "extern int identity(int value);\n"


def test_semantic_verification_compiles_once_and_runs_each_case(monkeypatch) -> None:
    calls: list[list[str]] = []

    def fake_run(command, **_kwargs):
        calls.append(command)
        if command[0] == "gcc":
            return SimpleNamespace(returncode=0, stderr="", stdout="")
        return SimpleNamespace(returncode=0, stderr="", stdout="")

    monkeypatch.setattr("runner.semantic.subprocess.run", fake_run)

    result = verify_semantic_correctness(
        "clamp",
        "int clamp(int value, int lo, int hi) { return value < lo ? lo : value > hi ? hi : value; }",
    )

    assert result == (1.0, None, "", 6, 6)
    gcc_calls = [command for command in calls if command[0] == "gcc"]
    runtime_calls = [command for command in calls if command[0] != "gcc"]
    assert "-c" in gcc_calls[0]
    assert len(gcc_calls) == 1 + len(TEST_WRAPPERS["clamp"])
    assert len(runtime_calls) == len(TEST_WRAPPERS["clamp"])
