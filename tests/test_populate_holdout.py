import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _load_module():
    path = ROOT / "scripts" / "populate_holdout.py"
    spec = importlib.util.spec_from_file_location("populate_holdout", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_plan_split_is_deterministic_and_disjoint() -> None:
    mod = _load_module()
    dev_a, hold_a, pairs_a = mod.plan_split()
    dev_b, hold_b, pairs_b = mod.plan_split()

    assert pairs_a == pairs_b
    holdout_names = {name for name, _ in pairs_a}
    assert holdout_names
    dev_names = {fn["name"] for functions in dev_a.values() for fn in functions}
    assert holdout_names.isdisjoint(dev_names)

    # Re-planning against already-split corpus should keep the same lock set
    # only when run against a fresh unsplit tree; after apply, names live in
    # separate dirs. Here we only assert the plan itself is stable.
    assert sum(len(v) for v in hold_a.values()) == len(holdout_names)
