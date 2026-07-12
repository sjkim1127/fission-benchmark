#!/usr/bin/env python3
"""Build stripped PE copies of selected dev binaries for the strip track.

Copies PE from corpus/dev/binaries, runs mingw strip, writes a realworld
manifest with the same function addresses (strip does not relocate code).
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEV_BIN = ROOT / "corpus" / "dev" / "binaries"
DEV_MANIFESTS = ROOT / "corpus" / "dev" / "manifests"
OUT_BIN = ROOT / "corpus" / "realworld" / "binaries"
OUT_MAN = ROOT / "corpus" / "realworld" / "manifests"


def find_strip() -> str:
    for name in ("x86_64-w64-mingw32-strip", "i686-w64-mingw32-strip", "strip"):
        p = shutil.which(name)
        if p:
            return p
    raise SystemExit("No strip tool found (install mingw-w64 strip)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--sources",
        default="control_flow,math",
        help="Comma-separated source stems to strip (default: control_flow,math)",
    )
    args = parser.parse_args()
    stems = [s.strip() for s in args.sources.split(",") if s.strip()]
    strip_bin = find_strip()
    OUT_BIN.mkdir(parents=True, exist_ok=True)
    OUT_MAN.mkdir(parents=True, exist_ok=True)

    # Collect functions from dev manifests for selected stems.
    subjects: list[dict] = []
    for man_path in sorted(DEV_MANIFESTS.glob("*.json")):
        data = json.loads(man_path.read_text(encoding="utf-8"))
        for fn in data.get("functions") or []:
            name = fn.get("name")
            for var in fn.get("compiler_variants") or []:
                binary = str(var.get("binary") or "")
                stem = Path(binary).name
                # match control_flow_gcc_O0.exe against stems
                if not any(stem.startswith(s + "_") or s in stem for s in stems):
                    continue
                if not stem.endswith(".exe"):
                    continue
                src = DEV_BIN / stem
                if not src.is_file():
                    continue
                out_name = stem.replace(".exe", "_strip.exe")
                dst = OUT_BIN / out_name
                if not dst.is_file() or dst.stat().st_mtime < src.stat().st_mtime:
                    shutil.copy2(src, dst)
                    subprocess.run([strip_bin, str(dst)], check=True)
                subjects.append(
                    {
                        "name": name,
                        "binary": f"binaries/{out_name}",
                        "addr": var.get("addr"),
                        "arch": "x86_64" if "m32" not in stem else "x86",
                        "compiler": var.get("compiler"),
                        "opt": (var.get("opt") or "") + "+strip",
                        "unstripped_binary": f"corpus/dev/binaries/{stem}",
                    }
                )

    manifest = {
        "_comment": "Auto-generated strip track from dev PE (seeded by build_strip_corpus.py)",
        "track": "strip",
        "functions": subjects,
    }
    out_path = OUT_MAN / "strip_from_dev.json"
    out_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(subjects)} strip subjects → {out_path}")
    print(f"Binaries under {OUT_BIN}")


if __name__ == "__main__":
    main()
