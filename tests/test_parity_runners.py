from benchmark.assembly_parity.run import compare_assembly
from benchmark.cfg_parity.run import compare_cfg
from benchmark.common.schema import BenchmarkSubject
from benchmark.decode_parity.run import compare_decode
from benchmark.function_discovery.run import compare_functions
from benchmark.ir_invariants.run import compare_invariants
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


def test_decode_compare_detects_sib_mismatch() -> None:
    expected = [{"address": "0x1000", "bytes": "48895c2408", "length": 5, "sib": "0x24"}]
    actual = [{"address": "0x1000", "bytes": "48895c2408", "length": 5, "sib": "0x25"}]

    result = compare_decode(subject(), "ref", "fission", expected, actual)

    assert result.status == "mismatch"
    assert result.mismatch_kind == "sib"


def test_pcode_compare_detects_op_kind_mismatch() -> None:
    expected = [{"seq": 0, "op": "COPY", "inputs": []}]
    actual = [{"seq": 0, "op": "STORE", "inputs": []}]

    result = compare_pcode(subject(), "ghidra", "fission", expected, actual)

    assert result.status == "mismatch"
    assert result.mismatch_kind == "op_kind"


def test_cfg_compare_detects_edge_count_mismatch() -> None:
    expected = {"blocks": [{"start": "0x1000"}], "edges": [{"source": "0x1000", "target": "0x1010"}]}
    actual = {"blocks": [{"start": "0x1000"}], "edges": []}

    result = compare_cfg(subject(), "ref", "fission", expected, actual)

    assert result.status == "mismatch"
    assert result.mismatch_kind == "edge_count"


def test_function_discovery_detects_function_set_mismatch() -> None:
    expected = [{"address": "0x1000", "name": "main"}]
    actual = []

    result = compare_functions(subject(), "ref", "fission", expected, actual)

    assert result.status == "mismatch"
    assert result.mismatch_kind == "function_set"


def test_ir_invariants_fail_on_violation() -> None:
    payload = {"violations": [{"kind": "dangling_edge"}], "metrics": {"block_count": 2}}

    result = compare_invariants(subject(), "fission", payload)

    assert result.status == "mismatch"
    assert result.mismatch_kind == "dangling_edge"
    assert result.metrics["violation_count"] == 1


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
