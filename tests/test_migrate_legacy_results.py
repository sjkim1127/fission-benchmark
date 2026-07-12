import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _load_migrate_module():
    path = ROOT / "scripts" / "migrate_legacy_results.py"
    spec = importlib.util.spec_from_file_location("migrate_legacy_results", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_migrate_legacy_flat_list_is_non_publishable(tmp_path: Path) -> None:
    rows = [
        {
            "decompiler": "fission",
            "function_name": "clamp",
            "compiler_variant": "gcc -O0",
            "source_similarity": 0.5,
            "goto_count": 0,
            "nesting_depth": 1,
            "time_ms": 10,
            "error": None,
            "semantic_score": 1.0,
            "correctness_score": 1.0,
        }
    ]
    path = tmp_path / "legacy.json"
    path.write_text(json.dumps(rows), encoding="utf-8")

    migrate = _load_migrate_module().migrate
    envelope = migrate(path)

    assert envelope["schema_version"] == 2
    assert envelope["validity"]["publishable"] is False
    assert len(envelope["rows"]) == 1
    assert envelope["run"]["run_mode"] == "legacy_migration"
