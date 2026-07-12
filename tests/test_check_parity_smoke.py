import importlib.util
import json
from pathlib import Path


def test_check_parity_smoke_ok(tmp_path: Path) -> None:

    path = Path(__file__).resolve().parents[1] / "scripts" / "check_parity_smoke.py"
    spec = importlib.util.spec_from_file_location("check_parity_smoke", path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    telemetry = {
        "total_rows": 6,
        "by_status": {"match": 4, "mismatch": 2},
        "reliability": {
            "usable_coverage": 1.0,
            "match_rate_attempted": 0.66,
            "fetch_error_rate": 0.0,
        },
        "stages": {
            "assembly_parity": {
                "total": 2,
                "match": 2,
                "mismatch": 0,
                "fetch_error": 0,
                "error_or_other": 0,
                "match_rate": 1.0,
                "mismatch_rate": 0.0,
                "usable_coverage": 1.0,
                "match_rate_attempted": 1.0,
            },
            "cfg_parity": {
                "total": 2,
                "match": 1,
                "mismatch": 1,
                "fetch_error": 0,
                "error_or_other": 0,
                "match_rate": 0.5,
                "mismatch_rate": 0.5,
                "usable_coverage": 1.0,
                "match_rate_attempted": 0.5,
            },
            "pcode_parity": {
                "total": 2,
                "match": 1,
                "mismatch": 1,
                "fetch_error": 0,
                "error_or_other": 0,
                "match_rate": 0.5,
                "mismatch_rate": 0.5,
                "usable_coverage": 1.0,
                "match_rate_attempted": 0.5,
            },
        },
    }
    p = tmp_path / "t.json"
    p.write_text(json.dumps(telemetry), encoding="utf-8")
    assert mod.main([str(p)]) == 0


def test_check_parity_smoke_fails_when_all_errors(tmp_path: Path) -> None:
    import importlib.util

    path = Path(__file__).resolve().parents[1] / "scripts" / "check_parity_smoke.py"
    spec = importlib.util.spec_from_file_location("check_parity_smoke2", path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    telemetry = {
        "total_rows": 3,
        "by_status": {"fetch_error": 3},
        "reliability": {"usable_coverage": 0.0, "fetch_error_rate": 1.0},
        "stages": {
            "assembly_parity": {
                "total": 1,
                "match": 0,
                "mismatch": 0,
                "fetch_error": 1,
                "error_or_other": 1,
                "match_rate": None,
                "mismatch_rate": None,
                "usable_coverage": 0.0,
            },
            "cfg_parity": {
                "total": 1,
                "match": 0,
                "mismatch": 0,
                "fetch_error": 1,
                "error_or_other": 1,
                "match_rate": None,
                "mismatch_rate": None,
                "usable_coverage": 0.0,
            },
            "pcode_parity": {
                "total": 1,
                "match": 0,
                "mismatch": 0,
                "fetch_error": 1,
                "error_or_other": 1,
                "match_rate": None,
                "mismatch_rate": None,
                "usable_coverage": 0.0,
            },
        },
    }
    p = tmp_path / "bad.json"
    p.write_text(json.dumps(telemetry), encoding="utf-8")
    assert mod.main([str(p)]) == 1
