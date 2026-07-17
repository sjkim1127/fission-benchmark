# Multi-ISA track

**Status:** active via tagged variants on the **dev** C corpus (not a separate
orphan tree). Prefer `corpus/dev` + `--profile multi_isa`.

| Slice | Arch / format | Compiler id | Notes |
|-------|---------------|-------------|--------|
| PE x64 / m32 | windows PE | `gcc`, `gcc-m32`, `clang` | Semantic (wine) |
| ELF x86_64 | linux ELF | `gcc-elf` | Decompile / structural; PE oracle N/A |
| ELF aarch64 | linux ELF | `gcc-aarch64` | Built with `aarch64-linux-gnu-gcc` (+ static) |

```bash
# Docker corpus-builder (has mingw + aarch64 cross + qemu-user-static)
docker compose --profile tools run --rm --build corpus-builder \
  python3 scripts/build_matrix.py --split dev --languages c

python runner/runner.py --corpus dev --profile multi_isa \
  --decompilers fission,ghidra --run-mode smoke
```

Do **not** blend untagged PE+ELF into one official ranking mean. Rows carry
`isa` / `format` / `abi_profile` for pivots. Headline ranking remains **core C PE**.
