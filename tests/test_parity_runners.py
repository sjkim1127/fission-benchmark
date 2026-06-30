from benchmark.assembly_parity.run import compare_assembly
from benchmark.common.schema import BenchmarkSubject
from benchmark.pcode_parity.run import compare_pcode
from benchmark.telemetry.aggregate import aggregate_rows


def subject() -> BenchmarkSubject:
    return BenchmarkSubject(
        binary="bin",
        function="fn",
        addr="0x1000",
        arch="x86_64",
        compiler="gcc",
        opt="-O2",
    )


def test_assembly_compare_detects_instruction_count_mismatch() -> None:
    expected = [{"address": "0x1000", "bytes": "90", "mnemonic": "nop"}]
    actual = []

    result = compare_assembly(subject(), "ref", "candidate", expected, actual)

    assert result.status == "mismatch"
    assert result.mismatch_kind == "instruction_count"


def test_pcode_compare_detects_op_kind_mismatch() -> None:
    expected = [{"seq": 0, "op": "COPY", "inputs": []}]
    actual = [{"seq": 0, "op": "STORE", "inputs": []}]

    result = compare_pcode(subject(), "ghidra", "fission", expected, actual)

    assert result.status == "mismatch"
    assert result.mismatch_kind == "op_kind"


def test_telemetry_aggregate_counts_stage_status_and_variant() -> None:
    rows = [
        {
            "subject": {"compiler": "gcc", "opt": "-O2"},
            "stage": "pcode_parity",
            "status": "mismatch",
            "mismatch_kind": "op_kind",
        }
    ]

    summary = aggregate_rows(rows)

    assert summary["total_rows"] == 1
    assert summary["by_stage"] == {"pcode_parity": 1}
    assert summary["by_status"] == {"mismatch": 1}
    assert summary["by_mismatch_kind"] == {"op_kind": 1}
    assert summary["by_variant"] == {"gcc -O2": 1}
