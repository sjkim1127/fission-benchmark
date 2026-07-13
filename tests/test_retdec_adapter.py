"""Unit tests for RetDec address-range extraction (no Docker required)."""
from __future__ import annotations

import importlib.util
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_retdec_server():
    # Stub heavy deps if missing
    for mod_name in ("fastapi", "pydantic"):
        if mod_name not in sys.modules:
            m = types.ModuleType(mod_name)
            if mod_name == "fastapi":

                class FastAPI:
                    def __init__(self, *a, **k):
                        pass

                    def get(self, *a, **k):
                        def d(f):
                            return f

                        return d

                    def post(self, *a, **k):
                        def d(f):
                            return f

                        return d

                m.FastAPI = FastAPI
                m.HTTPException = type("HTTPException", (Exception,), {})
            if mod_name == "pydantic":

                class BaseModel:
                    def __init__(self, **kw):
                        for k, v in kw.items():
                            setattr(self, k, v)

                m.BaseModel = BaseModel
            sys.modules[mod_name] = m

    sys.path.insert(0, str(ROOT / "docker" / "retdec"))
    try:
        spec = importlib.util.spec_from_file_location(
            "retdec_server", ROOT / "docker" / "retdec" / "server.py"
        )
        assert spec and spec.loader
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    finally:
        sys.path.remove(str(ROOT / "docker" / "retdec"))


SAMPLE = """
// ------------------- Function Prototypes --------------------
int32_t count_bits(uint32_t a1);
int32_t clamp(uint32_t a1, uint32_t a2, uint32_t a3);

// ------------------------ Functions -------------------------

// Address range: 0x4015b0 - 0x4015d5
int32_t count_bits(uint32_t a1) {
    int32_t v1 = 0;
    while (a1 != 0) {
        v1 += a1 & 1;
        a1 >>= 1;
    }
    return v1;
}

// Address range: 0x4015d6 - 0x4015f7
int32_t clamp(uint32_t a1, uint32_t a2, uint32_t a3) {
    if (a1 < a2) {
        return a2;
    }
    if (a1 > a3) {
        return a3;
    }
    return a1;
}
"""


def test_extract_count_bits_by_address_range():
    server = load_retdec_server()
    name, body = server.extract_function_at_addr(SAMPLE, "0x4015b0")
    assert name == "count_bits"
    assert "while (a1" in body
    assert "clamp" not in body


def test_extract_clamp_and_normalize_anchor():
    server = load_retdec_server()
    name, body = server.extract_function_at_addr(SAMPLE, "0x4015d6")
    assert name == "clamp"
    stable, norm = server.normalize_unit(name, body, "0x4015d6")
    assert stable == "fun_4015d6"
    assert "/* address: 0x4015d6" in norm
    assert "fun_4015d6" in norm


def test_inventory_from_ranges():
    server = load_retdec_server()
    inv = server.parse_functions_inventory(SAMPLE)
    addrs = {x["address"] for x in inv}
    assert "0x4015b0" in addrs
    assert "0x4015d6" in addrs


def test_missing_addr_returns_error():
    server = load_retdec_server()
    name, body = server.extract_function_at_addr(SAMPLE, "0xdeadbeef")
    assert body == "" or "not found" in (name + body).lower() or name == ""
