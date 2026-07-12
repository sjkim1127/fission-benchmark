import json
from unittest.mock import mock_open, patch

from runner.graph_utils import generate_mermaid
from runner.run_parity import run_parity_benchmarks

def test_mermaid_generation_basic():
    cfg = {
        "blocks": [
            {"addr": "0x1000", "size": 10, "instructions": ["nop", "ret"]},
            {"start": "0x2000", "size": 20, "instructions": ["mov eax, 1"]}
        ],
        "edges": [
            {"src": "0x1000", "dst": "0x2000"}
        ]
    }
    other_cfg = {
        "blocks": [
            {"addr": "0x1000", "size": 10, "instructions": ["nop", "ret"]},
            {"start": "0x2000", "size": 15, "instructions": ["mov eax, 1"]} # size mismatch
        ],
        "edges": [] # missing edge
    }

    # Generate reference mermaid
    ref_mermaid = generate_mermaid(cfg, other_cfg)
    
    # Assertions
    assert "graph TD" in ref_mermaid
    assert 'B_0x1000["0x1000<br/>10 bytes<br/>nop<br/>ret"]' in ref_mermaid
    assert 'B_0x2000["0x2000<br/>20 bytes<br/>mov eax, 1"]' in ref_mermaid
    assert "style B_0x1000 fill:#d5e8d4,stroke:#82b366" in ref_mermaid
    assert "style B_0x2000 fill:#fff2cc,stroke:#d6b656" in ref_mermaid
    assert "B_0x1000 --> B_0x2000" in ref_mermaid
    assert "linkStyle 0 stroke:#ff5555" in ref_mermaid

def test_mermaid_generation_missing_block():
    cfg = {
        "blocks": [{"addr": "0x1000", "size": 10, "instructions": []}],
        "edges": []
    }
    other_cfg = {
        "blocks": [],
        "edges": []
    }
    
    ref_mermaid = generate_mermaid(cfg, other_cfg)
    assert "style B_0x1000 fill:#ffcccc,stroke:#ff0000" in ref_mermaid

@patch("runner.run_parity.fetch_parity_data")
@patch("benchmark.common.subjects.load_subjects")
def test_run_parity_writes_mismatch_json(mock_load_subjects, mock_fetch, tmp_path):
    from benchmark.common.schema import BenchmarkSubject
    from runner.run_parity import FetchResult

    mock_load_subjects.return_value = [
        BenchmarkSubject(
            binary=str(tmp_path / "corpus" / "dev" / "binaries" / "mock_bin.exe"),
            function="test_func",
            addr="0x1000",
            arch="x86_64",
            compiler="gcc",
            opt="-O0",
            corpus_split="dev",
        )
    ]
    # Create path so relative extraction keeps basename mock_bin.exe
    (tmp_path / "corpus" / "dev" / "binaries").mkdir(parents=True)
    (tmp_path / "corpus" / "dev" / "binaries" / "mock_bin.exe").write_bytes(b"MZ")

    def fetch_side_effect(decompiler, endpoint, binary, *args, **kwargs):
        if decompiler == "ghidra":
            if endpoint == "cfg":
                return FetchResult(
                    status="ok",
                    data={"blocks": [{"addr": "0x1000", "size": 10, "instructions": ["nop"]}], "edges": []},
                )
            if endpoint == "disasm":
                return FetchResult(
                    status="ok",
                    data=[{"address": "0x1000", "bytes": "90", "mnemonic": "nop"}],
                )
        elif decompiler == "fission":
            if endpoint == "cfg":
                return FetchResult(
                    status="ok",
                    data={
                        "blocks": [{"addr": "0x1000", "size": 12, "instructions": ["nop", "ret"]}],
                        "edges": [],
                    },
                )
            if endpoint == "disasm":
                return FetchResult(
                    status="ok",
                    data=[{"address": "0x1000", "bytes": "9090", "mnemonic": "nop"}],
                )
        if endpoint == "cfg":
            return FetchResult(status="empty", data={"blocks": [], "edges": []})
        return FetchResult(status="empty", data=[])

    mock_fetch.side_effect = fetch_side_effect

    parity_diffs_dir = tmp_path / "parity_diffs"

    with patch.dict("os.environ", {"PARITY_DIFFS_DIR": str(parity_diffs_dir)}):
        run_parity_benchmarks("dev", decompilers=["fission"])

    expected_file = parity_diffs_dir / "mock_bin.exe" / "test_func" / "fission.json"
    assert expected_file.exists()

    with open(expected_file) as f:
        data = json.load(f)

    assert "reference_cfg" in data
    assert "candidate_cfg" in data
    assert "reference_disasm" in data
    assert "candidate_disasm" in data
    assert "mismatch_info" in data
    assert "reference_mermaid" in data
    assert "candidate_mermaid" in data

    assert data["reference_cfg"]["blocks"][0]["size"] == 10
    assert data["candidate_cfg"]["blocks"][0]["size"] == 12
    assert "nop" in data["reference_mermaid"]
    assert "ret" in data["candidate_mermaid"]
