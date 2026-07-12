#!/usr/bin/env python3
"""Lock a deterministic 80/20 holdout split from the current dev corpus.

Moves function entries (not source ownership) from ``corpus/dev/manifests`` into
``corpus/holdout/manifests`` using the same seed/ratio as ``runner.corpus``.

Shared source files and built binaries needed by holdout functions are copied
into ``corpus/holdout/{source,binaries}/``. Dev keeps its remaining functions and
existing binaries.

Usage:
  python scripts/populate_holdout.py           # apply split
  python scripts/populate_holdout.py --dry-run # preview only

After applying, rebuild holdout binaries if addresses need refresh:
  python scripts/build_corpus.py --split holdout
  # or: docker compose --profile tools run --rm corpus-builder
  #     with CORPUS_SPLIT=holdout
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import shutil
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from runner.corpus import (  # noqa: E402
    CORPUS_ROOT,
    HOLDOUT_RATIO,
    HOLDOUT_SEED,
)


def _load_manifest_functions(manifest_path: Path) -> list[dict]:
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    return list(data.get("functions", []))


def _write_manifest(path: Path, functions: list[dict], comment: str) -> None:
    payload = {
        "_comment": comment,
        "functions": functions,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def _copy_if_exists(src: Path, dst: Path) -> bool:
    if not src.exists():
        return False
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.is_dir():
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
    else:
        shutil.copy2(src, dst)
    return True


def plan_split(
    *,
    seed: int = HOLDOUT_SEED,
    holdout_ratio: float = HOLDOUT_RATIO,
) -> tuple[dict[str, list[dict]], dict[str, list[dict]], list[tuple[str, str]]]:
    """Return (dev_by_manifest, holdout_by_manifest, holdout_name_source_pairs)."""
    dev_manifest_dir = CORPUS_ROOT / "dev" / "manifests"
    by_manifest: dict[str, list[dict]] = {}
    indexed: list[tuple[str, dict]] = []

    for manifest in sorted(dev_manifest_dir.glob("*.json")):
        functions = _load_manifest_functions(manifest)
        by_manifest[manifest.name] = functions
        for fn in functions:
            indexed.append((manifest.name, fn))

    if not indexed:
        raise SystemExit("No functions found under corpus/dev/manifests")

    # Match runner.corpus.split_corpus_to_holdout ordering: hash name, then shuffle.
    indexed_sorted = sorted(
        indexed,
        key=lambda item: hashlib.sha256(item[1]["name"].encode()).hexdigest(),
    )
    rng = random.Random(seed)
    rng.shuffle(indexed_sorted)

    n_holdout = max(1, int(len(indexed_sorted) * holdout_ratio))
    holdout_items = indexed_sorted[:n_holdout]
    holdout_names = {fn["name"] for _, fn in holdout_items}

    dev_by: dict[str, list[dict]] = defaultdict(list)
    holdout_by: dict[str, list[dict]] = defaultdict(list)
    holdout_pairs: list[tuple[str, str]] = []

    for manifest_name, functions in by_manifest.items():
        for fn in functions:
            if fn["name"] in holdout_names:
                holdout_by[manifest_name].append(fn)
                holdout_pairs.append((fn["name"], fn.get("source", "")))
            else:
                dev_by[manifest_name].append(fn)

    return dict(dev_by), dict(holdout_by), sorted(holdout_pairs)


def apply_split(
    dev_by: dict[str, list[dict]],
    holdout_by: dict[str, list[dict]],
    *,
    dry_run: bool = False,
) -> None:
    dev_manifest_dir = CORPUS_ROOT / "dev" / "manifests"
    holdout_manifest_dir = CORPUS_ROOT / "holdout" / "manifests"
    holdout_source_dir = CORPUS_ROOT / "holdout" / "source"
    holdout_bin_dir = CORPUS_ROOT / "holdout" / "binaries"
    dev_root = CORPUS_ROOT / "dev"

    comment = (
        f"Holdout locked with seed={HOLDOUT_SEED} ratio={HOLDOUT_RATIO}. "
        "Do not use holdout functions during development."
    )

    # Collect assets referenced by holdout functions.
    sources: set[str] = set()
    binaries: set[str] = set()
    for functions in holdout_by.values():
        for fn in functions:
            if fn.get("source"):
                sources.add(fn["source"])
            for variant in fn.get("compiler_variants", []):
                if variant.get("binary"):
                    binaries.add(variant["binary"])

    if dry_run:
        print("[dry-run] would rewrite manifests and copy assets")
        print(f"  holdout sources: {sorted(sources)}")
        print(f"  holdout binaries: {sorted(binaries)}")
        return

    # Clear previous holdout manifests so stale locked functions disappear.
    if holdout_manifest_dir.exists():
        for path in holdout_manifest_dir.glob("*.json"):
            path.unlink()

    for manifest_name, functions in sorted(dev_by.items()):
        _write_manifest(
            dev_manifest_dir / manifest_name,
            functions,
            "Dev split after holdout lock. Generated by scripts/populate_holdout.py",
        )

    for manifest_name, functions in sorted(holdout_by.items()):
        if not functions:
            continue
        _write_manifest(
            holdout_manifest_dir / manifest_name,
            functions,
            comment,
        )

    # Delete emptied dev manifests (every function moved to holdout).
    for manifest_name, functions in list(dev_by.items()):
        if not functions:
            (dev_manifest_dir / manifest_name).unlink(missing_ok=True)

    for rel in sorted(sources):
        src = dev_root / rel
        dst = CORPUS_ROOT / "holdout" / rel
        if not _copy_if_exists(src, dst):
            print(f"warning: missing source {rel}", file=sys.stderr)

    for rel in sorted(binaries):
        src = dev_root / rel
        dst = CORPUS_ROOT / "holdout" / rel
        if not _copy_if_exists(src, dst):
            print(
                f"warning: missing binary {rel} — run build_corpus.py --split holdout",
                file=sys.stderr,
            )

    holdout_source_dir.mkdir(parents=True, exist_ok=True)
    holdout_bin_dir.mkdir(parents=True, exist_ok=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the planned holdout lock without writing files",
    )
    parser.add_argument("--seed", type=int, default=HOLDOUT_SEED)
    parser.add_argument("--ratio", type=float, default=HOLDOUT_RATIO)
    parser.add_argument(
        "--force",
        action="store_true",
        help="Allow re-locking even if corpus/holdout/manifests already has JSON",
    )
    args = parser.parse_args(argv)

    existing_holdout = list((CORPUS_ROOT / "holdout" / "manifests").glob("*.json"))
    if existing_holdout and not args.force and not args.dry_run:
        print(
            "error: holdout manifests already exist "
            f"({len(existing_holdout)} files). Re-running would split the "
            "already-reduced dev set again. Use --force only if you intend to "
            "rebuild the lock from the current dev manifests.",
            file=sys.stderr,
        )
        return 1

    dev_by, holdout_by, holdout_pairs = plan_split(
        seed=args.seed,
        holdout_ratio=args.ratio,
    )
    n_dev = sum(len(v) for v in dev_by.values())
    n_holdout = sum(len(v) for v in holdout_by.values())

    print(f"seed={args.seed} ratio={args.ratio}")
    print(f"dev functions: {n_dev}")
    print(f"holdout functions: {n_holdout}")
    print("holdout lock:")
    for name, source in holdout_pairs:
        print(f"  {name:24} {source}")

    apply_split(dev_by, holdout_by, dry_run=args.dry_run)
    if args.dry_run:
        print("dry-run complete (no files written)")
        return 0

    print("holdout manifests written under corpus/holdout/manifests/")
    print("dev manifests updated under corpus/dev/manifests/")
    print("next: python scripts/build_corpus.py --split holdout  # if binaries missing")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
