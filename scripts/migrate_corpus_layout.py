#!/usr/bin/env python3
"""Migrate C sources to source/c/ and expand PE opt matrix on manifests.

Safe to re-run. Does not compile (run build_matrix.py after).
"""
from __future__ import annotations

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "corpus"

# (compiler_id, opt, isa_tag, binary_suffix_without_exe)
# binary naming: binaries/c/{stem}_{compiler}_{opt_tag}.exe for x64
#                binaries/c/{stem}_{compiler-m32}_{opt_tag}.exe for m32


def expand_variants(stem: str, existing: list[dict]) -> list[dict]:
    """Produce expanded C PE variants while preserving known addrs when possible."""
    by_key: dict[tuple[str, str], dict] = {}
    for v in existing:
        by_key[(v.get("compiler", ""), v.get("opt", ""))] = dict(v)

    planned: list[tuple[str, str, str, str]] = []
    # gcc x64 full opt ladder
    for opt in ("-O0", "-O1", "-O2", "-Os", "-O3"):
        planned.append(("gcc", opt, "x86_64", f"binaries/c/{stem}_gcc_{opt.lstrip('-')}.exe"))
    # gcc m32 primary opts
    for opt in ("-O0", "-O2"):
        planned.append(
            ("gcc-m32", opt, "x86_32", f"binaries/c/{stem}_gcc-m32_{opt.lstrip('-')}.exe")
        )
    # clang x64
    for opt in ("-O0", "-O2"):
        planned.append(
            ("clang", opt, "x86_64", f"binaries/c/{stem}_clang_{opt.lstrip('-')}.exe")
        )

    out: list[dict] = []
    for compiler, opt, isa, binary in planned:
        prev = by_key.get((compiler, opt), {})
        # Map old binary names (binaries/math_gcc_O0.exe) → reuse addr if opt+compiler match
        entry = {
            "compiler": compiler,
            "opt": opt,
            "binary": binary,
            "addr": prev.get("addr", "0x0"),
            "isa": isa,
            "format": "pe",
            "abi_profile": "windows-x86" if isa == "x86_32" else "windows-x86_64",
        }
        out.append(entry)
    return out


def migrate_split(split: str) -> None:
    split_root = CORPUS / split
    src_root = split_root / "source"
    c_dir = src_root / "c"
    c_dir.mkdir(parents=True, exist_ok=True)

    # Move top-level *.c into source/c/
    if src_root.is_dir():
        for cfile in list(src_root.glob("*.c")):
            dest = c_dir / cfile.name
            if not dest.exists():
                shutil.move(str(cfile), str(dest))
                print(f"[move] {cfile.relative_to(ROOT)} -> {dest.relative_to(ROOT)}")
            else:
                cfile.unlink()
                print(f"[dedupe] removed leftover {cfile.relative_to(ROOT)}")

    man_dir = split_root / "manifests"
    if not man_dir.is_dir():
        return
    for man_path in sorted(man_dir.glob("*.json")):
        data = json.loads(man_path.read_text())
        changed = False
        for fn in data.get("functions", []):
            src = fn.get("source", "")
            # Normalize source path
            name = Path(src).name
            new_src = f"source/c/{name}"
            if fn.get("source") != new_src:
                fn["source"] = new_src
                changed = True
            if fn.get("language") != "c":
                fn["language"] = "c"
                changed = True
            if not isinstance(fn.get("semantic"), dict):
                fn["semantic"] = {
                    "mode": "c_wrapper",
                    "wrapper_id": fn["name"],
                    "oracle": "pe_wine",
                }
                changed = True
            stem = Path(name).stem  # control_flow, math, ...
            old_vars = fn.get("compiler_variants") or []
            new_vars = expand_variants(stem, old_vars)
            # Preserve addrs from old variants with same compiler+opt
            old_map = {(v.get("compiler"), v.get("opt")): v for v in old_vars}
            for v in new_vars:
                prev = old_map.get((v["compiler"], v["opt"]))
                if prev and prev.get("addr") and prev["addr"] != "0x0":
                    v["addr"] = prev["addr"]
            fn["compiler_variants"] = new_vars
            changed = True
        if changed:
            man_path.write_text(json.dumps(data, indent=2) + "\n")
            print(f"[✓] updated {man_path.relative_to(ROOT)}")


def main() -> None:
    for split in ("dev", "holdout"):
        if (CORPUS / split).is_dir():
            migrate_split(split)
    print("Done. Next: CORPUS_TARGET=windows-x86_64 python scripts/build_matrix.py --split dev")


if __name__ == "__main__":
    main()
