"""Unit tests for Ghidra parity bundle helper logic (no Docker)."""
from runner.run_parity import (
    FetchResult,
    _as_fetch,
    _fetch_candidate_bundle,
    _fetch_ghidra_reference_bundle,
    _multi_bundle_response_to_map,
    _prefetch_candidate_multi_bundle,
)


def test_as_fetch_cfg_empty() -> None:
    r = _as_fetch({"blocks": [], "edges": []}, is_cfg=True)
    assert r.status == "empty"


def test_as_fetch_list_ok() -> None:
    r = _as_fetch([{"address": "0x1"}])
    assert r.status == "ok"


def test_bundle_split(monkeypatch) -> None:
    def fake_fetch(
        decompiler, endpoint, binary, addr="", arch="", corpus="dev", timeout=5.0, addrs=""
    ):
        if endpoint == "parity_bundle":
            return FetchResult(
                status="ok",
                data={
                    "disasm": [{"address": "0x1", "bytes": "90", "mnemonic": "nop", "length": 1}],
                    "pcode": [{"seq": 0, "op": "COPY"}],
                    "cfg": {"blocks": [{"start": "0x1", "end": "0x2"}], "edges": []},
                },
            )
        raise AssertionError(f"unexpected endpoint {endpoint}")

    monkeypatch.setattr("runner.run_parity.fetch_parity_data", fake_fetch)
    asm, dec, pcode, cfg = _fetch_ghidra_reference_bundle(
        "corpus/dev/binaries/x.exe", "0x1", "x86_64", corpus="dev", timeout=5.0
    )
    assert asm.status == "ok"
    assert dec.status == "ok"
    assert pcode.status == "ok"
    assert cfg.status == "ok"
    assert dec.data[0]["mnemonic"] == "nop"


def test_candidate_bundle_split(monkeypatch) -> None:
    def fake_fetch(
        decompiler, endpoint, binary, addr="", arch="", corpus="dev", timeout=5.0, addrs=""
    ):
        assert decompiler == "fission"
        if endpoint == "parity_bundle":
            return FetchResult(
                status="ok",
                data={
                    "disasm": [{"address": "0x2", "bytes": "c3", "mnemonic": "ret", "length": 1}],
                    "decode": [{"address": "0x2", "bytes": "c3", "mnemonic": "ret", "length": 1}],
                    "pcode": [{"seq": 0, "op": "RETURN"}],
                    "cfg": {"blocks": [{"start": "0x2", "end": "0x3"}], "edges": []},
                },
            )
        raise AssertionError(f"unexpected endpoint {endpoint}")

    monkeypatch.setattr("runner.run_parity.fetch_parity_data", fake_fetch)
    asm, dec, pcode, cfg = _fetch_candidate_bundle(
        "fission", "corpus/dev/binaries/x.exe", "0x2", "x86_64", corpus="dev", timeout=5.0
    )
    assert asm.status == "ok"
    assert dec.status == "ok"
    assert pcode.data[0]["op"] == "RETURN"
    assert cfg.status == "ok"


def test_multi_bundle_response_to_map() -> None:
    multi = FetchResult(
        status="ok",
        data={
            "by_addr": {
                "0x401000": {
                    "disasm": [{"address": "0x401000", "bytes": "90", "mnemonic": "nop"}],
                    "pcode": [{"seq": 0, "op": "COPY"}],
                    "cfg": {"blocks": [{"start": "0x401000", "end": "0x401001"}], "edges": []},
                },
                "0x401100": {"error": "boom"},
            }
        },
    )
    parsed = _multi_bundle_response_to_map(multi)
    assert parsed is not None
    assert "0x401000" in parsed
    assert parsed["0x401000"][0].status == "ok"
    assert parsed["0x401100"][0].status == "fetch_error"


def test_binary_workers_default() -> None:
    from runner import run_parity as rp

    assert rp.BINARY_WORKERS >= 1


def test_prefetch_candidate_multi_bundle(monkeypatch) -> None:
    def fake_fetch(
        decompiler, endpoint, binary, addr="", arch="", corpus="dev", timeout=5.0, addrs=""
    ):
        assert decompiler == "fission"
        if endpoint == "parity_multi_bundle":
            assert "0x1" in addrs and "0x2" in addrs
            return FetchResult(
                status="ok",
                data={
                    "by_addr": {
                        "0x1": {
                            "disasm": [{"address": "0x1", "bytes": "90", "mnemonic": "nop"}],
                            "pcode": [],
                            "cfg": {"blocks": [{"start": "0x1", "end": "0x2"}], "edges": []},
                        },
                        "0x2": {
                            "disasm": [{"address": "0x2", "bytes": "c3", "mnemonic": "ret"}],
                            "pcode": [],
                            "cfg": {"blocks": [{"start": "0x2", "end": "0x3"}], "edges": []},
                        },
                    }
                },
            )
        raise AssertionError(f"unexpected {endpoint}")

    monkeypatch.setattr("runner.run_parity.fetch_parity_data", fake_fetch)
    out = _prefetch_candidate_multi_bundle(
        "fission",
        "corpus/dev/binaries/x.exe",
        ["0x1", "0x2"],
        "x86_64",
        corpus="dev",
        timeout=5.0,
    )
    assert set(out) == {"0x1", "0x2"}
    assert out["0x1"][0].status == "ok"
