from types import SimpleNamespace

from runner.semantic import build_single_translation_unit, verify_semantic_correctness
from runner.test_wrappers import TEST_WRAPPERS


def test_single_translation_unit_preserves_static_target() -> None:
    source = build_single_translation_unit(
        "identity",
        "static int identity(int value) { return value; }",
        ["int main() { return identity(1) == 1 ? 0 : 1; }"],
    )

    assert "static int identity" in source
    assert "static int semantic_case_0(void)" in source
    assert source.count("int main(void)") == 1


def test_semantic_verification_compiles_once_and_runs_each_case(monkeypatch) -> None:
    calls: list[list[str]] = []

    def fake_run(command, **_kwargs):
        calls.append(command)
        if command[0] == "gcc":
            return SimpleNamespace(returncode=0, stderr="", stdout="")
        output = "\n".join(
            f"CASE {index} 0" for index in range(len(TEST_WRAPPERS["clamp"]))
        )
        return SimpleNamespace(returncode=0, stderr="", stdout=output)

    monkeypatch.setattr("runner.semantic.subprocess.run", fake_run)

    result = verify_semantic_correctness(
        "clamp",
        "int clamp(int value, int lo, int hi) { return value < lo ? lo : value > hi ? hi : value; }",
    )

    assert result == (1.0, None, "", 6, 6)
    gcc_calls = [command for command in calls if command[0] == "gcc"]
    runtime_calls = [command for command in calls if command[0] != "gcc"]
    assert "-c" not in gcc_calls[0]
    assert len(gcc_calls) == 1
    assert len(runtime_calls) == 1
