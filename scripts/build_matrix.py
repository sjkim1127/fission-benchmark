#!/usr/bin/env python3
"""Multi-language / multi-opt corpus builder.

Extends the legacy C mingw path with:
  - optional language/isa/format tags on variants
  - inventory.json fingerprint
  - profile-aware no-op (profiles filter at run time; build still builds manifests)

Usage:
  CORPUS_TARGET=windows-x86_64 python scripts/build_matrix.py --split dev
  python scripts/build_matrix.py --split dev --languages c
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
CORPUS_ROOT = ROOT / "corpus"
CORPUS_TARGET = os.environ.get("CORPUS_TARGET", "host")
sys.path.insert(0, str(ROOT))


def target_tool(compiler: str, tool: str) -> str:
    if CORPUS_TARGET == "windows-x86_64":
        if compiler in {"gcc", "clang"}:
            if tool == "gcc":
                return "clang" if compiler == "clang" else "x86_64-w64-mingw32-gcc"
            return f"x86_64-w64-mingw32-{tool}"
        if compiler in {"gcc-m32", "clang-m32"}:
            if tool == "gcc":
                return "clang" if compiler == "clang-m32" else "i686-w64-mingw32-gcc"
            return f"i686-w64-mingw32-{tool}"
        if compiler in {"g++", "cpp", "cxx"}:
            if tool == "gcc":
                return "x86_64-w64-mingw32-g++"
            return f"x86_64-w64-mingw32-{tool}"
    if compiler in {"g++", "cpp", "cxx"} and tool == "gcc":
        return "g++"
    return compiler if tool == "gcc" else tool


def target_binary(binary: str, fmt: str = "") -> str:
    if CORPUS_TARGET == "windows-x86_64" or fmt == "pe":
        if not binary.endswith(".exe") and not binary.endswith(".dll"):
            return f"{binary}.exe"
    return binary


def compiler_binary(name: str) -> str:
    binary = shutil.which(name)
    if not binary:
        raise SystemExit(f"Compiler/tool not found on PATH: {name}")
    return binary


def compile_c_family(
    compiler: str,
    opt: str,
    source: Path,
    output: Path,
    *,
    language: str = "c",
) -> None:
    """Compile C or C++ source for CORPUS_TARGET."""
    if language == "cpp":
        selected = target_tool("g++" if compiler in {"gcc", "g++"} else compiler, "gcc")
    else:
        selected = target_tool(compiler, "gcc")
    output.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        compiler_binary(selected),
        opt,
        "-g",
        "-fno-inline",
        "-fno-omit-frame-pointer",
        "-o",
        str(output),
        str(source),
    ]
    if language == "cpp":
        cmd.insert(1, "-std=c++17")

    if compiler == "clang" and CORPUS_TARGET == "windows-x86_64":
        cmd.insert(1, "-target")
        cmd.insert(2, "x86_64-w64-mingw32")
        cmd.append("-L/usr/lib/gcc/x86_64-w64-mingw32/12-posix/")
    elif compiler == "clang-m32" and CORPUS_TARGET == "windows-x86_64":
        cmd.insert(1, "-target")
        cmd.insert(2, "i686-w64-mingw32")
        cmd.append("-L/usr/lib/gcc/i686-w64-mingw32/12-posix/")

    if compiler in {"gcc", "clang", "g++"} and CORPUS_TARGET != "windows-x86_64":
        cmd[2:2] = ["-fno-pie", "-no-pie"]

    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        if "-no-pie" not in cmd:
            print(f"Compilation error ({source.name}): {e.stderr}", file=sys.stderr)
            raise
        fallback = [part for part in cmd if part not in {"-fno-pie", "-no-pie"}]
        subprocess.run(fallback, check=True, capture_output=True, text=True)


def symbol_addresses(binary: Path, compiler: str) -> dict[str, str]:
    nm_name = target_tool(compiler if compiler not in {"g++"} else "gcc", "nm")
    # g++ still uses mingw nm
    if compiler in {"g++", "cpp", "cxx"} and CORPUS_TARGET == "windows-x86_64":
        nm_name = "x86_64-w64-mingw32-nm"
    nm = shutil.which(nm_name) or shutil.which("nm")
    if not nm:
        raise SystemExit(f"{nm_name} not found on PATH")

    proc = subprocess.run(
        [nm, "-n", str(binary)], check=True, capture_output=True, text=True
    )
    symbols: dict[str, str] = {}
    for line in proc.stdout.splitlines():
        parts = line.split()
        if len(parts) < 3:
            continue
        addr, sym_type, name = parts[-3], parts[-2], parts[-1]
        if sym_type.lower() not in {"t", "t"} and sym_type not in {"T", "t", "W", "w"}:
            # Keep text symbols; also accept some weak text.
            if sym_type not in {"T", "t", "W", "w"}:
                continue
        try:
            parsed_addr = hex(int(addr, 16))
            symbols[name] = parsed_addr
            if name.startswith("_"):
                symbols[name[1:]] = parsed_addr
            # MSVC/mingw C++ sometimes prefix
            if name.startswith("__Z") or name.startswith("_Z"):
                symbols[name] = parsed_addr
        except ValueError:
            continue
    return symbols


def _tag_variant(variant: dict[str, Any], compiler: str) -> None:
    if not variant.get("format"):
        if str(variant.get("binary", "")).endswith(".exe"):
            variant["format"] = "pe"
        else:
            variant["format"] = "elf" if CORPUS_TARGET != "windows-x86_64" else "pe"
    if not variant.get("isa"):
        variant["isa"] = (
            "x86_32" if compiler in {"gcc-m32", "clang-m32"} else "x86_64"
        )
    if not variant.get("abi_profile"):
        if variant.get("format") == "pe":
            variant["abi_profile"] = (
                "windows-x86"
                if variant.get("isa") == "x86_32"
                else "windows-x86_64"
            )
        else:
            variant["abi_profile"] = "linux-x86_64"


def build_manifest(manifest_path: Path, split: str, languages: set[str] | None) -> None:
    data = json.loads(manifest_path.read_text())
    built: set[tuple[str, str, str, str]] = set()

    for fn in data["functions"]:
        language = fn.get("language") or "c"
        if language == "c" and "/c/" not in fn.get("source", "") and not fn.get("source", "").startswith("source/c/"):
            # Allow legacy paths during migration
            language = "c"
        if languages is not None and language not in languages:
            continue
        if language not in {"c", "cpp"}:
            print(f"[skip] {fn.get('name')}: language={language} not built by C family path yet")
            continue

        source = CORPUS_ROOT / split / fn["source"]
        if not source.is_file():
            # Try migrated path source/c/<basename>
            alt = CORPUS_ROOT / split / "source" / "c" / Path(fn["source"]).name
            if alt.is_file():
                fn["source"] = str(Path("source/c") / alt.name)
                source = alt
            else:
                print(f"[warn] missing source {source}", file=sys.stderr)
                continue

        if not fn.get("language"):
            fn["language"] = language
        if not fn.get("semantic"):
            fn["semantic"] = {
                "mode": "c_wrapper",
                "wrapper_id": fn["name"],
                "oracle": "pe_wine",
            }

        for variant in fn.get("compiler_variants", []):
            compiler = variant["compiler"]
            _tag_variant(variant, compiler)
            variant["binary"] = target_binary(
                variant["binary"], variant.get("format", "")
            )
            key = (
                fn["source"],
                compiler,
                variant["opt"],
                variant["binary"],
            )
            if key in built:
                continue
            out = CORPUS_ROOT / split / variant["binary"]
            compile_c_family(
                compiler,
                variant["opt"],
                source,
                out,
                language=language if language == "cpp" else "c",
            )
            built.add(key)

    addr_cache: dict[str, dict[str, str]] = {}
    for fn in data["functions"]:
        language = fn.get("language") or "c"
        if languages is not None and language not in languages:
            continue
        if language not in {"c", "cpp"}:
            continue
        for variant in fn.get("compiler_variants", []):
            binary = variant["binary"]
            if binary not in addr_cache:
                path = CORPUS_ROOT / split / binary
                if not path.is_file():
                    continue
                addr_cache[binary] = symbol_addresses(path, variant["compiler"])
            resolved = addr_cache.get(binary, {}).get(fn["name"])
            if not resolved:
                resolved = addr_cache.get(binary, {}).get(f"_{fn['name']}")
            if resolved:
                variant["addr"] = resolved
            _tag_variant(variant, variant["compiler"])

    manifest_path.write_text(json.dumps(data, indent=2) + "\n")
    print(f"[✓] Synced manifest: {manifest_path.name}")


def write_inventory(split: str) -> None:
    split_root = CORPUS_ROOT / split
    binaries = sorted((split_root / "binaries").rglob("*")) if (split_root / "binaries").exists() else []
    files = [p for p in binaries if p.is_file()]
    h = hashlib.sha256()
    for p in files:
        h.update(p.name.encode())
        h.update(str(p.stat().st_size).encode())
    inv = {
        "split": split,
        "corpus_target": CORPUS_TARGET,
        "binary_count": len(files),
        "fingerprint": h.hexdigest()[:16],
        "builder": "build_matrix.py",
    }
    path = split_root / "inventory.json"
    path.write_text(json.dumps(inv, indent=2) + "\n")
    print(f"[✓] Wrote {path.relative_to(ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build multi-language corpus binaries")
    parser.add_argument("--split", default="dev", choices=["dev", "holdout"])
    parser.add_argument(
        "--languages",
        default="c,cpp",
        help="Comma-separated languages to build (default: c,cpp)",
    )
    parser.add_argument(
        "--profile",
        default=None,
        help="Optional profile name (informational; run-time filter is in runner)",
    )
    args = parser.parse_args()
    languages = {x.strip() for x in args.languages.split(",") if x.strip()}
    if args.profile:
        print(f"[i] profile={args.profile} (variants still built from manifests; filter at run)")

    manifests_dir = CORPUS_ROOT / args.split / "manifests"
    if not manifests_dir.is_dir():
        raise SystemExit(f"No manifests at {manifests_dir}")
    for manifest_path in sorted(manifests_dir.glob("*.json")):
        build_manifest(manifest_path, args.split, languages)
    write_inventory(args.split)


if __name__ == "__main__":
    main()
