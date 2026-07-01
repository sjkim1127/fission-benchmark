"""Build corpus binaries and populate manifest function addresses.

The runner expects each manifest compiler variant to point to a built binary and
to carry the function entry address for that specific binary. This script keeps
those fields reproducible as the C corpus grows.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORPUS_ROOT = ROOT / "corpus"
CORPUS_TARGET = os.environ.get("CORPUS_TARGET", "host")


def target_tool(compiler: str, tool: str) -> str:
    if CORPUS_TARGET == "windows-x86_64" and compiler in {"gcc", "clang"}:
        return f"x86_64-w64-mingw32-{tool}"
    return compiler if tool == "gcc" else tool


def target_binary(binary: str) -> str:
    if CORPUS_TARGET == "windows-x86_64" and not binary.endswith(".exe"):
        return f"{binary}.exe"
    return binary


def compiler_binary(name: str) -> str:
    binary = shutil.which(name)
    if not binary:
        raise SystemExit(f"Compiler not found on PATH: {name}")
    return binary


def compile_source(compiler: str, opt: str, source: Path, output: Path) -> None:
    selected_compiler = target_tool(compiler, "gcc")
    output.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        compiler_binary(selected_compiler),
        opt,
        "-g",
        "-fno-inline",
        "-fno-omit-frame-pointer",
        "-o",
        str(output),
        str(source),
    ]
    if compiler in {"gcc", "clang"} and CORPUS_TARGET != "windows-x86_64":
        cmd[2:2] = ["-fno-pie", "-no-pie"]

    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError:
        if "-no-pie" not in cmd:
            raise
        fallback = [part for part in cmd if part not in {"-fno-pie", "-no-pie"}]
        subprocess.run(fallback, check=True, capture_output=True, text=True)


def symbol_addresses(binary: Path, compiler: str) -> dict[str, str]:
    nm_name = target_tool(compiler, "nm")
    nm = shutil.which(nm_name)
    if not nm:
        raise SystemExit(f"{nm_name} not found on PATH")

    proc = subprocess.run([nm, "-n", str(binary)], check=True, capture_output=True, text=True)
    symbols: dict[str, str] = {}
    for line in proc.stdout.splitlines():
        parts = line.split()
        if len(parts) < 3:
            continue
        addr, sym_type, name = parts[-3], parts[-2], parts[-1]
        if sym_type.lower() != "t":
            continue
        try:
            parsed_addr = hex(int(addr, 16))
            symbols[name] = parsed_addr
            if name.startswith("_"):
                symbols[name[1:]] = parsed_addr
        except ValueError:
            continue
    return symbols


def build_manifest(manifest_path: Path, split: str) -> None:
    data = json.loads(manifest_path.read_text())
    built: set[tuple[str, str, str, str]] = set()

    for fn in data["functions"]:
        source = CORPUS_ROOT / split / fn["source"]
        for variant in fn.get("compiler_variants", []):
            variant["binary"] = target_binary(variant["binary"])
            key = (
                fn["source"],
                variant["compiler"],
                variant["opt"],
                variant["binary"],
            )
            if key in built:
                continue
            compile_source(
                variant["compiler"],
                variant["opt"],
                source,
                CORPUS_ROOT / split / variant["binary"],
            )
            built.add(key)

    addr_cache: dict[str, dict[str, str]] = {}
    for fn in data["functions"]:
        for variant in fn.get("compiler_variants", []):
            binary = variant["binary"]
            if binary not in addr_cache:
                addr_cache[binary] = symbol_addresses(CORPUS_ROOT / split / binary, variant["compiler"])
            addr = addr_cache[binary].get(fn["name"])
            if not addr:
                raise SystemExit(f"Symbol not found: {fn['name']} in {binary}")
            variant["addr"] = addr

    manifest_path.write_text(json.dumps(data, indent=2) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--split", default="dev", choices=["dev", "holdout"])
    args = parser.parse_args()

    manifest_dir = CORPUS_ROOT / args.split / "manifests"
    for manifest in sorted(manifest_dir.glob("*.json")):
        build_manifest(manifest, args.split)
        print(f"updated {manifest}")


if __name__ == "__main__":
    main()
