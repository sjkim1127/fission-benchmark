from benchmark.assembly_parity.run import compare_assembly
from benchmark.cfg_parity.run import compare_cfg
from benchmark.common.http_providers import corpus_relative_binary
from benchmark.common.providers import (
    canonicalize_cfg,
    canonicalize_pcode,
    normalize_pcode_op,
)
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
    expected = [
        {"address": "0x1000", "bytes": "90", "mnemonic": "nop"},
        {"address": "0x1001", "bytes": "c3", "mnemonic": "ret"},
    ]
    actual = [{"address": "0x1000", "bytes": "90", "mnemonic": "nop"}]

    result = compare_assembly(subject(), "ref", "candidate", expected, actual)

    assert result.status == "mismatch"
    assert result.mismatch_kind == "instruction_count"


def test_assembly_empty_candidate_is_not_scored_mismatch() -> None:
    """Empty candidate must not look like a quality mismatch (reliability)."""
    expected = [{"address": "0x1000", "bytes": "90", "mnemonic": "nop"}]
    result = compare_assembly(subject(), "ref", "candidate", expected, [])
    assert result.status == "candidate_empty"


def test_assembly_normalizes_spaced_bytes_and_case() -> None:
    expected = [{"address": "0x140001560", "bytes": "4889e5", "mnemonic": "MOV", "operands": "MOV RBP,RSP"}]
    actual = [{"address": "0x140001560", "bytes": "48 89 e5", "mnemonic": "mov", "operands": "RBP,RSP"}]
    assert compare_assembly(subject(), "ghidra", "fission", expected, actual).status == "match"


def test_cfg_canonicalize_sorts_blocks() -> None:
    a = {"blocks": [{"start": "0x20", "end": "0x21"}, {"start": "0x10", "end": "0x11"}], "edges": []}
    b = {"blocks": [{"start": "0x10", "end": "0x11"}, {"start": "0x20", "end": "0x21"}], "edges": []}
    assert canonicalize_cfg(a) == canonicalize_cfg(b)


def test_corpus_relative_binary() -> None:
    assert corpus_relative_binary("binaries/foo.exe", "dev") == "corpus/dev/binaries/foo.exe"
    assert corpus_relative_binary("corpus/dev/binaries/foo.exe", "dev").startswith("corpus/")


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


def test_normalize_pcode_op_collapses_naming_styles() -> None:
    assert normalize_pcode_op("INT_SUB") == normalize_pcode_op("IntSub")
    assert normalize_pcode_op("INT_SUB") == normalize_pcode_op("INTSUB")
    assert normalize_pcode_op("BOOL_NEGATE") == normalize_pcode_op("BoolNegate")
    assert normalize_pcode_op("POPCOUNT") == normalize_pcode_op("PopCount")


def test_pcode_compare_matches_ghidra_vs_fission_spelling() -> None:
    """Ghidra SNAKE_CASE and Fission CamelCase with different STORE space ids."""
    expected = [
        {
            "seq": 0,
            "op": "INT_SUB",
            "output": {"space": "register", "offset": "0x20", "size": 8},
            "inputs": [
                {"space": "register", "offset": "0x20", "size": 8},
                {"space": "const", "offset": "0x8", "size": 8},
            ],
        },
        {
            "seq": 1,
            "op": "STORE",
            "output": None,
            "inputs": [
                {"space": "const", "offset": "0x1b1", "size": 8},
                {"space": "register", "offset": "0x20", "size": 8},
                {"space": "unique", "offset": "0x4f900", "size": 8},
            ],
        },
    ]
    actual = [
        {
            "seq": 0,
            "op": "IntSub",
            "output": {"space": "register", "offset": "0x20", "size": 8},
            "inputs": [
                {"space": "register", "offset": "0x20", "size": 8},
                {"space": "const", "offset": "0x8", "size": 8},
            ],
        },
        {
            "seq": 1,
            "op": "Store",
            "output": None,
            "inputs": [
                {"space": "const", "offset": "0x3", "size": 8},
                {"space": "register", "offset": "0x20", "size": 8},
                {"space": "unique", "offset": "0x4f900", "size": 8},
            ],
        },
    ]
    assert canonicalize_pcode(expected) == canonicalize_pcode(actual)
    assert compare_pcode(subject(), "ghidra", "fission", expected, actual).status == "match"


def test_pcode_compare_still_flags_real_varnode_diffs() -> None:
    expected = [
        {
            "seq": 0,
            "op": "COPY",
            "output": {"space": "register", "offset": "0x0", "size": 8},
            "inputs": [{"space": "register", "offset": "0x28", "size": 8}],
        }
    ]
    actual = [
        {
            "seq": 0,
            "op": "Copy",
            "output": {"space": "register", "offset": "0x0", "size": 8},
            "inputs": [{"space": "register", "offset": "0x30", "size": 8}],
        }
    ]
    result = compare_pcode(subject(), "ghidra", "fission", expected, actual)
    assert result.status == "mismatch"
    assert result.mismatch_kind == "varnode"


def test_cfg_compare_detects_edge_count_mismatch() -> None:
    expected = {"blocks": [{"start": "0x1000"}], "edges": [{"source": "0x1000", "target": "0x1010"}]}
    actual = {"blocks": [{"start": "0x1000"}], "edges": []}

    result = compare_cfg(subject(), "ref", "fission", expected, actual)

    assert result.status == "mismatch"
    assert result.mismatch_kind == "edge_count"


def test_function_discovery_detects_function_set_mismatch() -> None:
    expected = [{"address": "0x1000", "name": "main"}, {"address": "0x2000", "name": "foo"}]
    actual = [{"address": "0x1000", "name": "main"}]

    result = compare_functions(subject(), "ref", "fission", expected, actual)

    assert result.status == "mismatch"
    assert result.mismatch_kind == "function_set"


def test_function_discovery_empty_is_invalid_not_match() -> None:
    result = compare_functions(subject(), "ref", "fission", [{"address": "0x1", "name": "a"}], [])
    assert result.status == "candidate_empty"


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
            "reference": "ghidra",
            "candidate": "fission",
        },
        {
            "subject": {"compiler": "gcc", "opt": "-O2"},
            "stage": "assembly_parity",
            "status": "match",
            "mismatch_kind": None,
            "reference": "ghidra",
            "candidate": "fission",
        },
    ]

    summary = aggregate_rows(rows)

    assert summary["total_rows"] == 2
    assert summary["schema"] == "parity-telemetry-v2"
    assert "reliability" in summary
    assert "match_rate_attempted" in summary["stages"]["assembly_parity"]
    assert summary["by_stage"] == {"assembly_parity": 1, "pcode_parity": 1}
    assert summary["by_status"] == {"match": 1, "mismatch": 1}
    assert summary["by_mismatch_kind"] == {"none": 1, "op_kind": 1}
    assert summary["by_variant"] == {"gcc -O2": 2}
    assert summary["stages"]["assembly_parity"]["match_rate"] == 1.0
    assert summary["stages"]["pcode_parity"]["mismatch_rate"] == 1.0
