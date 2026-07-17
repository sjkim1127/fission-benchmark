#!/usr/bin/env python3
"""Resolve a small PE subject for speed smoke from the dev corpus.

Prints shell-friendly lines:
  BINARY=...
  ADDRS=0x...,0x...
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    # Prefer a small C PE with multiple functions (add_ints etc. live in small family).
    candidates = [
        ROOT / "corpus/dev/binaries/c/small_gcc_O0.exe",
        ROOT / "corpus/dev/binaries/c/c_small_gcc_O0.exe",
        ROOT / "corpus/dev/binaries/c/patterns_gcc_O0.exe",
    ]
    # Also scan any *gcc_O0.exe under c/
    c_dir = ROOT / "corpus/dev/binaries/c"
    if c_dir.is_dir():
        for p in sorted(c_dir.glob("*gcc_O0.exe")):
            if p not in candidates:
                candidates.append(p)

    binary: Path | None = None
    for p in candidates:
        if p.is_file() and p.stat().st_size > 0:
            binary = p
            break
    if binary is None:
        print("FAIL: no PE binary under corpus/dev/binaries/c", file=sys.stderr)
        return 1

    # Collect up to 4 function addrs from manifests that reference this binary.
    rel = str(binary.relative_to(ROOT / "corpus/dev")).replace("\\", "/")
    addrs: list[str] = []
    man_dir = ROOT / "corpus/dev/manifests"
    for man in sorted(man_dir.glob("*.json")):
        try:
            data = json.loads(man.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        for fn in data.get("functions") or []:
            for var in fn.get("compiler_variants") or []:
                b = str(var.get("binary") or "").replace("\\", "/")
                if b != rel and not b.endswith(binary.name):
                    continue
                addr = str(var.get("addr") or "").strip()
                if addr and addr not in ("0x0", "0"):
                    addrs.append(addr)
                if len(addrs) >= 4:
                    break
            if len(addrs) >= 4:
                break
        if len(addrs) >= 4:
            break

    if not addrs:
        # Fallback placeholder — microbench will fail clearly if wrong.
        print(f"WARN: no addrs in manifests for {rel}; using empty", file=sys.stderr)
        print(f"BINARY={binary}")
        print("ADDRS=")
        return 1

    print(f"BINARY={binary}")
    print(f"ADDRS={','.join(addrs[:4])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
