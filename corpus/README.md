# Corpus layout (multi-language matrix)

## Layout

```text
corpus/
  matrix/
    profiles.yaml      # smoke / core_c_pe / opt_cliff / lang_* / full_matrix
    toolchains.yaml    # compile recipes (gcc/clang/g++/rustc/go × isa×format)
  dev/ | holdout/
    source/
      c/               # C sources (primary semantic cohort)
      cpp/             # C++ (rolling out)
      rust/            # Rust (rolling out)
      go/              # Go (rolling out)
    manifests/         # per-family JSON (function → variants + addrs)
    binaries/          # gitignored; built by scripts/build_matrix.py
    inventory.json     # optional toolchain fingerprint after build
```

## Profiles

Run / build with a profile to avoid Cartesian explosion:

```bash
export BENCHMARK_PROFILE=smoke
python runner/runner.py --corpus dev --profile smoke --decompilers fission,ghidra

# Build only variants needed for a profile (optional)
python scripts/build_matrix.py --split dev --profile core_c_pe
```

| Profile | Role |
|---------|------|
| `smoke` | Push CI — small C PE O0 slice |
| `core_c_pe` | Official C PE ranking cohort (O0/O2, x64+m32) |
| `opt_cliff` | Full opt ladder on stress functions |
| `lang_cpp` / `lang_rust` / `lang_go` | Language tracks |
| `multi_isa` | PE+ELF / multi-arch |
| `full_matrix` | Everything present (manual / fan-out) |

## Semantic policy

- **Headline ranking** remains semantic pass rate on the **core C PE** cohort until other language oracles are measurement-valid.
- Rows should carry `language`, `isa`, `format`, `abi_profile` for pivots.
- Rust/Go native semantic uses language drivers + declared export surfaces; see `docs/BENCHMARK_OPERATING.md`.

## Build

```bash
# Docker (CI default)
docker compose --profile tools run --rm --build corpus-builder

# Host (needs mingw / toolchains)
CORPUS_TARGET=windows-x86_64 python scripts/build_matrix.py --split dev
```

Legacy entrypoint: `scripts/build_corpus.py` delegates to `build_matrix.py`.
