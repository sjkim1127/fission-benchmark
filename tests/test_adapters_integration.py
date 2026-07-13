import os
import base64
import pytest
import httpx
from pathlib import Path
from runner.runner import configured_decompilers

DECOMPILERS = ["fission", "reko", "snowman", "angr", "boomerang", "ghidra"]
CORPUS_BINARY = "corpus/dev/binaries/control_flow_gcc-m32_O0.exe"

# Resolve the root of the fission-benchmark workspace
ROOT = Path(__file__).resolve().parents[1]
BINARY_PATH = ROOT / CORPUS_BINARY


def get_endpoint(dname: str) -> str:
    endpoints = configured_decompilers()
    if dname not in endpoints:
        pytest.fail(f"Decompiler {dname} is not configured in runner.runner.configured_decompilers()")
    return endpoints[dname]


def check_health_or_skip(dname: str) -> str:
    endpoint = get_endpoint(dname)
    strict = os.environ.get("STRICT_INTEGRATION", "").lower() in ("true", "1", "yes")
    try:
        resp = httpx.get(f"{endpoint}/health", timeout=5.0)
        if resp.status_code == 200:
            return endpoint
        msg = f"Decompiler {dname} health returned HTTP {resp.status_code}"
    except Exception as e:
        msg = f"Decompiler {dname} health check failed: {e}"

    if strict:
        pytest.fail(msg)
    else:
        pytest.skip(msg)


@pytest.fixture(params=DECOMPILERS)
def decompiler_client(request):
    dname = request.param
    endpoint = check_health_or_skip(dname)
    return dname, endpoint


def test_health_endpoint(decompiler_client) -> None:
    dname, endpoint = decompiler_client
    resp = httpx.get(f"{endpoint}/health", timeout=120.0)
    assert resp.status_code == 200
    data = resp.json()
    assert data.get("status") == "ok" or data.get("status") == "success" or "decompiler" in data


def test_functions_endpoint(decompiler_client) -> None:
    dname, endpoint = decompiler_client
    resp = httpx.get(f"{endpoint}/functions", params={"binary": CORPUS_BINARY}, timeout=120.0)
    assert resp.status_code == 200
    funcs = resp.json()
    assert isinstance(funcs, list)

    if dname in ["fission", "reko", "angr", "ghidra"]:
        assert len(funcs) > 0

    for fn in funcs:
        assert "address" in fn
        assert "name" in fn
        assert isinstance(fn["address"], str)
        assert fn["address"].lower().startswith("0x")
        assert isinstance(fn["name"], str)


def test_decompile_batch_endpoint(decompiler_client) -> None:
    dname, endpoint = decompiler_client

    if not BINARY_PATH.exists():
        pytest.fail(f"Corpus binary not found at {BINARY_PATH}")

    binary_bytes = BINARY_PATH.read_bytes()
    binary_b64 = base64.b64encode(binary_bytes).decode()

    payload = {
        "binary_b64": binary_b64,
        "addresses": ["0x4015b0"]
    }

    resp = httpx.post(f"{endpoint}/decompile_batch", json=payload, timeout=120.0)
    assert resp.status_code == 200
    data = resp.json()

    assert "decompiler" in data
    assert data["decompiler"] == dname
    assert "results" in data
    assert isinstance(data["results"], list)
    assert len(data["results"]) == 1

    res = data["results"][0]
    assert res["addr"] == "0x4015b0"

    # All decompilers including snowman should now return successful function extraction.
    assert res.get("error") is None, f"Decompilation error for {dname}: {res.get('error')}"
    assert "code" in res
    assert isinstance(res["code"], str)
    assert len(res["code"].strip()) > 0


def test_error_missing_file(decompiler_client) -> None:
    dname, endpoint = decompiler_client
    resp = httpx.get(f"{endpoint}/functions", params={"binary": "nonexistent"}, timeout=120.0)
    assert resp.status_code == 404
    data = resp.json()
    assert "detail" in data


def test_error_empty_file(decompiler_client) -> None:
    dname, endpoint = decompiler_client
    resp = httpx.get(f"{endpoint}/functions", params={"binary": ""}, timeout=120.0)
    assert resp.status_code == 400
    data = resp.json()
    assert "detail" in data


def test_error_malformed_address(decompiler_client) -> None:
    dname, endpoint = decompiler_client
    if dname == "reko":
        pytest.skip("Reko server does not implement /disasm endpoint")

    resp = httpx.get(f"{endpoint}/disasm", params={"binary": CORPUS_BINARY, "addr": "invalid"}, timeout=120.0)
    assert resp.status_code == 400
    data = resp.json()
    assert "detail" in data


def test_error_malformed_base64(decompiler_client) -> None:
    dname, endpoint = decompiler_client
    payload = {
        "binary_b64": "invalid!",
        "addresses": ["0x4015b0"]
    }
    resp = httpx.post(f"{endpoint}/decompile_batch", json=payload, timeout=120.0)
    assert resp.status_code == 400
    data = resp.json()
    assert "detail" in data
