"""Function discovery benchmark: dual metrics, PE oracle, report."""
from __future__ import annotations

from pathlib import Path

from benchmark.common.schema import BenchmarkSubject
from benchmark.function_discovery.pe_oracle import (
    inventory_from_addresses,
    pe_symbol_inventory,
)
from benchmark.function_discovery.run import (
    SCORED_AS,
    compare_functions,
    function_addresses,
    inventory_dual_metrics,
    normalize_function_address,
)
from runner.function_discovery_report import (
    REPORT_SCHEMA,
    build_discovery_report,
    render_markdown,
)


def subject() -> BenchmarkSubject:
    return BenchmarkSubject(
        binary="binaries/control_flow_gcc_O0.exe",
        function="*",
        addr="0x0",
        arch="x86_64",
        compiler="gcc",
        opt="-O0",
        corpus_split="dev",
    )


def test_inventory_dual_metrics_precision_recall_f1() -> None:
    ref = {"0x1000", "0x2000", "0x3000"}
    cand = {"0x1000", "0x2000", "0x4000"}
    m = inventory_dual_metrics(ref, cand, manifest_addrs={"0x1000", "0x9999"})
    assert m["presence_recall"] == round(2 / 3, 4)
    assert m["presence_precision"] == round(2 / 3, 4)
    assert m["presence_f1"] == round(2 * (2 / 3) * (2 / 3) / (4 / 3), 4)
    assert m["missing_function_count"] == 1
    assert m["extra_function_count"] == 1
    assert m["manifest_recall"] == 0.5
    assert m["scored_as"] == SCORED_AS


def test_compare_functions_always_emits_dual_and_scored_as() -> None:
    expected = [
        {"address": "0x1000", "name": "main"},
        {"address": "0x2000", "name": "foo"},
    ]
    actual = [{"address": "0x1000", "name": "main"}]
    result = compare_functions(subject(), "ghidra", "fission", expected, actual)
    assert result.status == "mismatch"
    assert result.metrics["scored_as"] == SCORED_AS
    assert result.metrics["presence_recall"] == 0.5
    assert result.metrics["presence_precision"] == 1.0
    assert result.metrics["presence_f1"] == round(2 * 1.0 * 0.5 / 1.5, 4)


def test_compare_functions_match_with_address_padding() -> None:
    result = compare_functions(
        subject(),
        "ghidra",
        "fission",
        [{"address": "0x140001530", "name": "count_bits"}],
        [{"address": "0x0000000140001530", "name": "count_bits"}],
    )
    assert result.status == "match"
    assert result.metrics["presence_recall"] == 1.0
    assert result.metrics["presence_jaccard"] == 1.0


def test_empty_candidate_is_not_match_but_has_dual() -> None:
    result = compare_functions(
        subject(),
        "ghidra",
        "fission",
        [{"address": "0x1", "name": "a"}],
        [],
    )
    assert result.status == "candidate_empty"
    assert result.metrics["scored_as"] == SCORED_AS
    assert result.metrics["presence_recall"] == 0.0


def test_manifest_recall_attached() -> None:
    result = compare_functions(
        subject(),
        "ghidra",
        "fission",
        [
            {"address": "0x1000", "name": "a"},
            {"address": "0x2000", "name": "b"},
        ],
        [{"address": "0x1000", "name": "a"}],
        manifest_addrs={"0x1000", "0x2000"},
    )
    assert result.metrics["manifest_recall"] == 0.5
    assert result.metrics["manifest_subject_count"] == 2


def test_pe_symbol_inventory_holdout_m32() -> None:
    binary = (
        Path(__file__).resolve().parents[1]
        / "corpus"
        / "holdout"
        / "binaries"
        / "control_flow_gcc-m32_O0.exe"
    )
    if not binary.exists():
        return
    inv = pe_symbol_inventory(binary)
    addrs = function_addresses(inv)
    # Unstripped MinGW control_flow should expose count_bits etc.
    assert any("count_bits" in str(item.get("name") or "") for item in inv)
    assert normalize_function_address("0x4015b0") in addrs or any(
        "4015b0" in a for a in addrs
    )


def test_inventory_from_addresses() -> None:
    inv = inventory_from_addresses(["0x4015b0", "0x4015b0", "0x4015d6"])
    assert len(inv) == 2
    assert function_addresses(inv) == {
        normalize_function_address("0x4015b0"),
        normalize_function_address("0x4015d6"),
    }


def test_discovery_report_cohorts() -> None:
    rows = [
        {
            "stage": "function_discovery",
            "candidate": "fission",
            "status": "match",
            "metrics": {
                "scored_as": "ghidra_inventory",
                "presence_recall": 1.0,
                "presence_precision": 0.9,
                "presence_f1": 0.9474,
                "presence_jaccard": 0.9,
                "manifest_recall": 1.0,
            },
        },
        {
            "stage": "function_discovery",
            "candidate": "snowman",
            "status": "mismatch",
            "mismatch_kind": "function_set",
            "metrics": {
                "scored_as": "ghidra_inventory",
                "presence_recall": 0.5,
                "presence_precision": 0.8,
                "presence_f1": 0.6154,
                "presence_jaccard": 0.4,
                "manifest_recall": 1.0,
            },
        },
        {
            "stage": "function_discovery",
            "candidate": "fission",
            "status": "mismatch",
            "metrics": {
                "scored_as": "ghidra_inventory",
                "presence_recall": 0.8,
                "presence_precision": 0.8,
                "presence_f1": 0.8,
                "presence_jaccard": 0.7,
                "manifest_recall": 1.0,
            },
        },
    ]
    report = build_discovery_report(rows)
    assert report["schema"] == REPORT_SCHEMA
    assert report["by_candidate"]["fission"]["cohort"] == "core"
    assert report["by_candidate"]["snowman"]["cohort"] == "multi"
    # ghidra self-check would be "reference" cohort
    ghidra_row = {
        "stage": "function_discovery",
        "candidate": "ghidra",
        "status": "match",
        "metrics": {
            "scored_as": "ghidra_inventory",
            "presence_recall": 1.0,
            "presence_precision": 1.0,
            "presence_f1": 1.0,
            "presence_jaccard": 1.0,
            "manifest_recall": 1.0,
        },
    }
    report2 = build_discovery_report(rows + [ghidra_row])
    assert report2["by_candidate"]["ghidra"]["cohort"] == "reference"
    # fission: 1 match + 1 mismatch → set_match_rate 0.5
    assert report["by_candidate"]["fission"]["set_match_rate"] == 0.5
    assert report["by_candidate"]["fission"]["dual"]["mean_presence_recall"] == 0.9
    md = render_markdown(report)
    assert "Function discovery" in md
    assert "fission" in md
