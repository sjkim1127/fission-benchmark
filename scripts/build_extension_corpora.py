#!/usr/bin/env python3
"""Build realworld multi-TU, adversarial CFF, and multi-ISA (ELF) fixtures."""
from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MINGW = shutil.which("x86_64-w64-mingw32-gcc")
STRIP = shutil.which("x86_64-w64-mingw32-strip") or shutil.which("strip")
CLANG = shutil.which("clang")


def run(cmd: list[str]) -> None:
    print("+", " ".join(cmd))
    subprocess.run(cmd, check=True)


def build_realworld() -> None:
    if not MINGW:
        print("skip realworld: no mingw")
        return
    src = ROOT / "corpus/realworld/source"
    bin_dir = ROOT / "corpus/realworld/binaries"
    man_dir = ROOT / "corpus/realworld/manifests"
    bin_dir.mkdir(parents=True, exist_ok=True)
    man_dir.mkdir(parents=True, exist_ok=True)
    out = bin_dir / "util_app_gcc_O0.exe"
    run(
        [
            MINGW,
            "-O0",
            "-g",
            str(src / "util_lib.c"),
            str(src / "util_main.c"),
            "-o",
            str(out),
        ]
    )
    strip_out = bin_dir / "util_app_gcc_O0_strip.exe"
    shutil.copy2(out, strip_out)
    if STRIP:
        run([STRIP, str(strip_out)])

    # Addresses: parse via nm if available, else leave 0 for inventory-only
    subjects = []
    nm = shutil.which("x86_64-w64-mingw32-nm") or shutil.which("nm")
    addrs: dict[str, str] = {}
    if nm:
        r = subprocess.run([nm, str(out)], capture_output=True, text=True)
        for line in r.stdout.splitlines():
            parts = line.split()
            if len(parts) >= 3 and parts[1].lower() in {"t", "t"}:
                name = parts[2].lstrip("_")
                addrs[name] = f"0x{parts[0]}"
    for name in ("app_process", "util_hash", "util_clamp", "util_count_bits", "main"):
        addr = addrs.get(name) or addrs.get("_" + name) or "0x0"
        subjects.append(
            {
                "name": name,
                "binary": f"binaries/{out.name}",
                "addr": addr if addr.startswith("0x") else f"0x{addr}",
                "arch": "x86_64",
                "compiler": "gcc",
                "opt": "O0",
                "track": "realworld_multi_tu",
            }
        )
        subjects.append(
            {
                "name": name,
                "binary": f"binaries/{strip_out.name}",
                "addr": addr if addr.startswith("0x") else f"0x{addr}",
                "arch": "x86_64",
                "compiler": "gcc",
                "opt": "O0+strip",
                "track": "realworld_multi_tu_strip",
                "unstripped_binary": f"corpus/realworld/binaries/{out.name}",
            }
        )
    manifest = {
        "_comment": "Multi-TU realworld fixture (util_lib + util_main)",
        "track": "realworld",
        "functions": subjects,
    }
    path = man_dir / "util_multi_tu.json"
    path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {path} ({len(subjects)} subjects)")


def build_adversarial() -> None:
    if not MINGW:
        print("skip adversarial: no mingw")
        return
    src = ROOT / "corpus/adversarial/source/cff_toy.c"
    bin_dir = ROOT / "corpus/adversarial/binaries"
    man_dir = ROOT / "corpus/adversarial/manifests"
    bin_dir.mkdir(parents=True, exist_ok=True)
    man_dir.mkdir(parents=True, exist_ok=True)
    out = bin_dir / "cff_toy_gcc_O0.exe"
    run([MINGW, "-O0", str(src), "-o", str(out)])
    nm = shutil.which("x86_64-w64-mingw32-nm") or shutil.which("nm")
    addr = "0x0"
    if nm:
        r = subprocess.run([nm, str(out)], capture_output=True, text=True)
        for line in r.stdout.splitlines():
            if "cff_classify" in line:
                parts = line.split()
                if len(parts) >= 3:
                    addr = f"0x{parts[0]}"
                    break
    man = {
        "track": "adversarial",
        "functions": [
            {
                "name": "cff_classify",
                "binary": f"binaries/{out.name}",
                "addr": addr,
                "arch": "x86_64",
                "compiler": "gcc",
                "opt": "O0",
                "track": "adversarial_cff",
            }
        ],
    }
    path = man_dir / "cff_toy.json"
    path.write_text(json.dumps(man, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {path}")


def build_multi_isa() -> None:
    """ELF x86_64 via clang if available (arm64 needs cross sysroot — scaffold binary optional)."""
    if not CLANG:
        print("skip multi_isa: no clang")
        return
    src = ROOT / "corpus/multi_isa/source"
    src.mkdir(parents=True, exist_ok=True)
    cfile = src / "hello_elf.c"
    cfile.write_text(
        "int add(int a, int b) { return a + b; }\nint main(void) { return add(2, 3); }\n",
        encoding="utf-8",
    )
    bin_dir = ROOT / "corpus/multi_isa/binaries"
    man_dir = ROOT / "corpus/multi_isa/manifests"
    bin_dir.mkdir(parents=True, exist_ok=True)
    man_dir.mkdir(parents=True, exist_ok=True)
    out = bin_dir / "hello_elf_x86_64"
    try:
        run([CLANG, "-O0", str(cfile), "-o", str(out)])
    except subprocess.CalledProcessError as exc:
        print("multi_isa build failed:", exc)
        return
    man = {
        "track": "multi_isa",
        "functions": [
            {
                "name": "add",
                "binary": f"binaries/{out.name}",
                "addr": "0x0",
                "arch": "x86_64",
                "compiler": "clang",
                "opt": "O0",
                "format": "elf",
                "note": "ELF fixture; oracle PE path does not apply — structural stages only",
            }
        ],
    }
    path = man_dir / "hello_elf.json"
    path.write_text(json.dumps(man, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {path}")


def main() -> None:
    build_realworld()
    build_adversarial()
    build_multi_isa()


if __name__ == "__main__":
    main()
