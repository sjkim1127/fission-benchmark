from benchmark.common.schema import BenchmarkSubject
from benchmark.metadata_parity.run import compare_metadata


SUBJECT = BenchmarkSubject(
    binary="binaries/sample.exe",
    function="(metadata)",
    addr="0x0",
    arch="x86_64",
    compiler="gcc",
    opt="O0",
)


def payload(*, functions=(0x1000,), block_size=0x100):
    return {
        "schema": "test-v1",
        "binary": {
            "bitness": 64,
            "image_base": 0x1000,
            "language_id": "x86:LE:64:default",
        },
        "memory_blocks": [
            {
                "start": 0x1000,
                "size": block_size,
                "permissions": {"read": True, "write": False, "execute": True},
            }
        ],
        "functions": [{"entry": entry} for entry in functions],
        "symbols": [{"address": 0x1000}],
        "relocations": [{"address": 0x1020}],
    }


def test_metadata_exact_match():
    row = compare_metadata(SUBJECT, "ghidra", "fission", payload(), payload())
    assert row.status == "match"
    assert row.metrics["function_entry_jaccard"] == 1.0


def test_metadata_reports_first_structural_mismatch():
    row = compare_metadata(
        SUBJECT,
        "ghidra",
        "fission",
        payload(functions=(0x1000, 0x1010)),
        payload(functions=(0x1000,)),
    )
    assert row.status == "mismatch"
    assert row.mismatch_kind == "function_entries"
    assert row.metrics["function_entry_jaccard"] == 0.5


def test_metadata_missing_schema_is_not_a_match():
    row = compare_metadata(SUBJECT, "ghidra", "fission", payload(), {})
    assert row.status == "candidate_empty"
