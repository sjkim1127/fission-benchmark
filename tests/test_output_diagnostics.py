from runner.output_diagnostics import analyze_output_diagnostics, invalid_output_reason


def test_direct_function_output() -> None:
    diag = analyze_output_diagnostics("count_bits", "ghidra", "int count_bits(unsigned x) { return 0; }")

    assert diag["status"] == "direct_function"
    assert diag["target_name_present"] is True


def test_dotted_radare2_name_needs_normalization() -> None:
    diag = analyze_output_diagnostics("count_bits", "radare2", "int dbg.count_bits(unsigned x) { return 0; }")

    assert diag["status"] == "needs_normalization"
    assert "non_c_identifier_names" in diag["issues"]
    assert "dotted_function_names" in diag["harness_blockers"]


def test_revng_address_named_output_is_boundary_mismatch_for_source_name() -> None:
    code = "_ABI(raw_x86_64)\nint function_0x401000_Code_x86_64(int x) { return x; }"

    diag = analyze_output_diagnostics("count_bits", "revng", code)

    assert diag["status"] == "boundary_mismatch"
    assert "target_name_missing" in diag["issues"]
    assert "revng_abi_types" in diag["harness_blockers"]


def test_revng_address_named_output_can_be_matched_by_expected_address() -> None:
    code = "_ABI(raw_x86_64)\nint function_0x401000_Code_x86_64(int x) { return x; }"

    diag = analyze_output_diagnostics("count_bits", "revng", code, expected_addr="0x401000")

    # Address anchor + soft ABI blockers only → treated as boundary-ok
    # (adapter normalization still preferred).
    assert diag["status"] == "direct_function"
    assert diag["expected_address_present"] is True
    assert invalid_output_reason(diag, code) is None


def test_address_anchored_adapter_output_is_direct() -> None:
    code = "/* address: 0x140001530 */\nint fcn_140001530(unsigned x) { return 0; }"
    diag = analyze_output_diagnostics(
        "count_bits", "radare2", code, expected_addr="0x140001530"
    )
    assert diag["status"] == "direct_function"
    assert diag["expected_address_present"] is True
    assert invalid_output_reason(diag, code) is None


def test_whole_program_output_is_flagged() -> None:
    code = "\n".join(f"int fun_{i}(void) {{ return {i}; }}" for i in range(5))

    diag = analyze_output_diagnostics("count_bits", "snowman", code)

    assert diag["status"] == "whole_program_output"
    assert diag["function_definition_count"] == 5
    assert invalid_output_reason(diag, code) == "Decompiler returned whole-program or truncated output, not a target function"


def test_boomerang_wrong_address_is_adapter_error() -> None:
    code = """
    /* File: target.c */
    /** address: 0x00001181 */
    void proc_0x00001181(int pc) { return; }
    """

    diag = analyze_output_diagnostics("clamp", "boomerang", code, expected_addr="0x14000155f")

    assert diag["status"] == "boundary_mismatch"
    assert "expected_address_missing" in diag["issues"]
    assert invalid_output_reason(diag, code) == "Decompiler output does not match requested function name or address"


def test_empty_decompiler_sentinel_is_no_output() -> None:
    diag = analyze_output_diagnostics("clamp", "angr", "angr decompilation empty", expected_addr="0x14000155f")

    assert diag["status"] == "no_output"
    assert "empty_decompiler_sentinel" in diag["issues"]
    assert invalid_output_reason(diag, "angr decompilation empty") == "No decompiler output for target function"
