#!/usr/bin/env python3
"""Archive a multi-decomp dashboard envelope into the per-release history set.

Every "Update dashboard multi-decomp envelope" CI step overwrites
public/benchmark-latest.json in place (see benchmark.yml) -- there is no
retained history beyond git blobs. This script copies the *current* envelope
into public/benchmark-history/<fission_version>.json (keyed by
toolchain.fission_version) and keeps public/benchmark-history/index.json (a
version-sorted list) in sync, so the dashboard can load "current vs previous
release" without needing git access at request time (the deployed dashboard
fetches over HTTPS from raw.githubusercontent.com / Vercel's public/, not a
git checkout).

Usage:
    # Archive the current public/benchmark-latest.json (what CI calls):
    python3 scripts/archive_benchmark_history.py

    # One-off backfill from git history (already-superseded versions only
    # exist as old commits of public/benchmark-latest.json):
    python3 scripts/archive_benchmark_history.py --backfill
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LATEST_PATH = REPO_ROOT / "public" / "benchmark-latest.json"
HISTORY_DIR = REPO_ROOT / "public" / "benchmark-history"
INDEX_PATH = HISTORY_DIR / "index.json"

_VERSION_RE = re.compile(r"^v?(\d+)\.(\d+)\.(\d+)$")


def version_sort_key(version: str) -> tuple:
    m = _VERSION_RE.match(version)
    if not m:
        # Unparseable versions sort first (oldest/lowest priority).
        return (-1, -1, -1, version)
    return (int(m.group(1)), int(m.group(2)), int(m.group(3)), "")


def write_index(versions: set[str]) -> None:
    ordered = sorted(versions, key=version_sort_key)
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(json.dumps(ordered, indent=2) + "\n", encoding="utf-8")
    print(f"index.json: {ordered}")


def archive_envelope(envelope: dict, source_label: str) -> str | None:
    version = (envelope.get("toolchain") or {}).get("fission_version")
    if not version:
        print(f"SKIP {source_label}: no toolchain.fission_version", file=sys.stderr)
        return None
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    out_path = HISTORY_DIR / f"{version}.json"
    out_path.write_text(json.dumps(envelope, indent=2) + "\n", encoding="utf-8")
    print(f"archived {source_label} -> {out_path} (fission_version={version})")
    return version


def cmd_archive_current() -> int:
    if not LATEST_PATH.exists():
        print(f"ERROR: {LATEST_PATH} does not exist", file=sys.stderr)
        return 1
    envelope = json.loads(LATEST_PATH.read_text(encoding="utf-8"))
    version = archive_envelope(envelope, str(LATEST_PATH))
    if version is None:
        return 1
    versions = {p.stem for p in HISTORY_DIR.glob("*.json") if p.stem != "index"}
    write_index(versions)
    return 0


def cmd_backfill() -> int:
    """One-off: walk git history of public/benchmark-latest.json and archive
    the most recent snapshot for every distinct fission_version seen, so
    already-superseded releases (whose only trace is an old commit) get a
    permanent, independently-fetchable archive entry too."""
    log = subprocess.run(
        ["git", "log", "--format=%H", "--", "public/benchmark-latest.json"],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()

    seen_versions: set[str] = set()
    archived: set[str] = set()
    for commit in log:  # newest first -> first hit per version is its final state
        show = subprocess.run(
            ["git", "show", f"{commit}:public/benchmark-latest.json"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        if show.returncode != 0:
            continue
        try:
            envelope = json.loads(show.stdout)
        except json.JSONDecodeError:
            continue
        version = (envelope.get("toolchain") or {}).get("fission_version")
        if not version or version in seen_versions:
            continue
        seen_versions.add(version)
        out_path = HISTORY_DIR / f"{version}.json"
        if out_path.exists():
            continue
        archive_envelope(envelope, f"{commit[:8]}:public/benchmark-latest.json")
        archived.add(version)

    versions = {p.stem for p in HISTORY_DIR.glob("*.json") if p.stem != "index"}
    write_index(versions)
    print(f"backfilled {len(archived)} version(s): {sorted(archived, key=version_sort_key)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--backfill",
        action="store_true",
        help="Backfill from git history instead of archiving the current envelope",
    )
    args = parser.parse_args()
    return cmd_backfill() if args.backfill else cmd_archive_current()


if __name__ == "__main__":
    raise SystemExit(main())
