<div align="center">

# fission-benchmark

**Multi-decompiler comparison benchmark for [Fission](https://github.com/sjkim1127/Fission)**

Fission · Ghidra · Boomerang · Radare2+r2ghidra · angr · Snowman · rev.ng · Reko

[![Benchmark](https://github.com/sjkim1127/fission-benchmark/actions/workflows/benchmark.yml/badge.svg)](https://github.com/sjkim1127/fission-benchmark/actions/workflows/benchmark.yml)
[![Docker Build](https://github.com/sjkim1127/fission-benchmark/actions/workflows/build-check.yml/badge.svg)](https://github.com/sjkim1127/fission-benchmark/actions/workflows/build-check.yml)

📊 **[Live Dashboard →](https://sjkim1127.github.io/fission-benchmark/)**

</div>

---

## Overview

Each decompiler runs in an isolated Docker container exposing a uniform HTTP API.
A Python runner sends decompile requests in parallel, scores results against original C source, and generates a comparative report.

```
Binary + Source (ground truth)
        ↓
┌──────────────────────────────────────────────────────────────┐
│  runner.py  (parallel httpx requests)                        │
│  Fission :8000 · Ghidra :8001 · Boomerang :8002 · Radare2    │
│  angr :8004 · Snowman :8005 · rev.ng :8006 · Reko :8008      │
└──────────────────────────────┬───────────────────────────────┘
                               │
                     ↓
              scoring.py (source similarity + consensus)
                     ↓
              report.py → results/latest.md + docs/index.html
```

## Overfitting Prevention (3-Layer)

| Layer | Mechanism |
|---|---|
| **Train/Holdout** | 80/20 function-level split (fixed seed). Use `--corpus holdout` for holdout evaluation. |
| **Cross-compiler** | Same source compiled with gcc -O0 and gcc -O2 — evaluated independently |
| **Multi-decompiler consensus** | If all decompilers score low → `⚪ Universally low (harness)`. Only Fission low → quality gap. |

> **Current status**: holdout manifests are present but empty.
> The overfitting report will show `No holdout data` for all decompilers until holdout binaries are built.
> `--corpus holdout` works correctly once manifests are populated.

## Quick Start

### Requirements

- Docker + Docker Compose
- Python 3.11+
- GCC-compatible C compiler + `nm` (for corpus binary/address generation), or the Dockerized corpus builder below
- `pip install -e ".[dev]"`

### Run

```bash
# Build decompiler containers
docker compose build

# Build corpus binaries and populate per-function addresses
python scripts/build_corpus.py --split dev

# On macOS/Apple Silicon, build Windows x86-64 PE corpus binaries instead.
# Benchmark runs use the latest Fission release and this cross-built corpus path by default.
docker compose --profile tools run --rm corpus-builder

# Start containers
docker compose up -d

# Wait for health checks
curl http://localhost:8001/health  # Ghidra
curl http://localhost:8002/health  # Boomerang
curl http://localhost:8003/health  # Radare2

# Run benchmark (dev corpus)
python runner/runner.py --corpus dev

# Results
cat results/latest.md
open docs/index.html
```

### Options

```bash
# Single function smoke test
python runner/runner.py --corpus dev --limit 1

# Specific decompilers only
python runner/runner.py --corpus dev --decompilers fission,ghidra

# Full core decompiler set
python runner/runner.py --corpus dev --decompilers fission,ghidra,boomerang,radare2,angr,snowman,revng,reko

# Skip a specific decompiler via environment variable
FISSION_ENDPOINT=skip python runner/runner.py --corpus dev
GHIDRA_ENDPOINT=skip python runner/runner.py --corpus dev

# Point a decompiler at a custom endpoint
GHIDRA_ENDPOINT=http://localhost:9001 python runner/runner.py --corpus dev
FISSION_ENDPOINT=http://localhost:9000 python runner/runner.py --corpus dev

# Any {NAME}_ENDPOINT variable is supported:
# BOOMERANG_ENDPOINT, RADARE2_ENDPOINT, ANGR_ENDPOINT,
# SNOWMAN_ENDPOINT, REVNG_ENDPOINT, REKO_ENDPOINT

# Holdout evaluation (release only — never during development)
python runner/runner.py --corpus holdout

# Full corpus (dev + holdout combined)
python runner/runner.py --corpus full
```

### Local Fission build (quality loop only)

CI and GitHub Pages always use a **GitHub Release** Fission bake
(`FISSION_SOURCE=release`). For day-to-day decompiler work you can mount a
**current Linux `fission_cli` + `utils/`** into the same adapter:

```bash
# 1) Build / collect a Linux ELF CLI + utils (not macOS Mach-O).
#    Prefer CD-equivalent target: x86_64-unknown-linux-gnu
#    Order: FISSION_LINUX_CLI → existing target/… → cargo zigbuild → Docker
scripts/prepare_local_fission.sh
#    optional: FISSION_ROOT=/path/to/Fission
#    optional: FISSION_LINUX_CLI=/path/to/linux/fission_cli
#    optional: FISSION_FORCE_DOCKER_BUILD=1
#    macOS tip: brew install zig && cargo install cargo-zigbuild --locked

# 2) Start only the Fission adapter with the local overlay
set -a && source .env.local && set +a
docker compose -f docker-compose.yml -f docker-compose.local.yml \
  --profile local up -d --build fission

# 3) Confirm provenance
curl -s "http://localhost:${FISSION_HOST_PORT:-8007}/health"
# → "source": "local", "git_sha": "...", "release_version": "local-<sha>"

# 4) Measure into a non-latest path (do not overwrite official latest)
python runner/runner.py --corpus dev --decompilers fission \
  --output "results/local_${FISSION_GIT_SHA}.json"
```

**Rules**

| Path | Fission binary | Results |
|---|---|---|
| CI / Pages / `results/latest.*` | Release tag only | Official timeline |
| Local quality loop | Current build (Linux ELF) | `results/local_<sha>.json` only |

Local mode requires a **Linux ELF** matching the compose platform
(`linux/amd64` by default). Host macOS arm64 binaries will not run in the
container; `prepare_local_fission.sh` cross-builds via Docker when needed.

## Repository Layout

```
fission-benchmark/
├── benchmark/
│   ├── KNOWN_ISSUES.md  Infrastructure freeze policy and remaining trust gaps
│   ├── decode_parity/    Instruction decoder parity runner
│   ├── assembly_parity/  Instruction listing parity runner
│   ├── pcode_parity/     Raw p-code parity runner
│   ├── cfg_parity/       Basic block/edge parity runner
│   ├── function_discovery/  Binary-level function discovery parity
│   ├── ir_invariants/    Fission-internal IR invariant checks
│   ├── golden_repros/    Fixed regression canary runner
│   ├── telemetry/        JSONL result aggregation
│   ├── readability/      Readability proxy metrics and human-study plan
│   ├── decompiler_quality/  Current output-quality stage marker
│   └── common/           Shared schemas, providers, JSONL helpers
├── docker/
│   ├── ghidra/      Ghidra 12.x headless + FastAPI
│   ├── retdec/      RetDec 5.x + FastAPI
│   ├── radare2/     Radare2 + r2ghidra + FastAPI
│   ├── fission/     Fission CLI + FastAPI (release bake; local mount overlay)
│   ├── angr/        angr decompiler + FastAPI
│   ├── snowman/     Snowman/nocode + FastAPI
│   ├── revng/       rev.ng + FastAPI
│   └── reko/        Reko + FastAPI
├── runner/
│   ├── runner.py    Main orchestrator
│   ├── corpus.py    Corpus management + holdout split
│   ├── scoring.py   Source similarity + structural scoring
│   ├── readability.py  AST-based readability proxy metrics
│   └── report.py    Markdown + HTML report generation
├── scripts/
│   └── build_corpus.py  Compile corpus binaries + update function addresses
├── corpus/
│   ├── dev/         80% — development corpus (source + manifests)
│   └── holdout/     20% — holdout corpus (release evaluation only)
├── docs/            GitHub Pages dashboard (auto-generated)
├── results/         Benchmark results (auto-committed by CI)
└── .github/
    └── workflows/
        ├── benchmark.yml     Weekly run + Pages deploy
        └── build-check.yml   Docker build validation
```

## Fission Release Tracking

CI sets `FISSION_SOURCE=release` and uses `FISSION_VERSION=latest` by default,
so scheduled and manual benchmark runs pull the latest published Fission release
only. The `/health` probe must report `"source": "release"` (CI fails on
`local-*`). The benchmark workflow also accepts a cross-repository dispatch
event so the Fission release pipeline can trigger a run immediately after
publishing:

```bash
gh api repos/sjkim1127/fission-benchmark/dispatches \
  -f event_type=fission-release \
  -f client_payload='{"fission_version":"v0.1.2"}'
```

Manual workflow runs can override `fission_version` with a specific tag for
reproducibility.

## API Contract

All decompiler containers expose:

```
POST /decompile
Body:     { "binary_b64": "<base64>", "addr": "0x1400010a0" }
Response: { "decompiler": "ghidra", "name": "fibonacci", "code": "...", "time_ms": 120, "error": null }

GET /health
Response: { "status": "ok", "decompiler": "ghidra", "version": "12.0" }

# Fission also reports provenance:
# { "status": "ok", "decompiler": "fission", "version": "...",
#   "release_version": "v0.1.2"|"local-<sha>",
#   "source": "release"|"local", "git_sha": "<optional>" }
```

## Adding a New Decompiler

1. Create `docker/<name>/Dockerfile` + `server.py` implementing the API contract above
2. Add the service to `docker-compose.yml` on the next available port
3. Add to `DECOMPILERS` dict in `runner/runner.py`
4. Add to `build-check.yml` matrix

## Core Open-Source Backends

The benchmark treats every configured open-source backend as part of the core
comparison set. Individual services can still be skipped explicitly for local
debugging with `*_ENDPOINT=skip` or by passing a narrower `--decompilers` list.

| Backend | Port | Notes |
|---|---:|---|
| `angr` | 8004 | Python API, function-address oriented, useful independent baseline |
| `snowman` | 8005 | Uses `nocode`; legacy baseline, x86-64 image is amd64-only |
| `revng` | 8006 | Uses `decompile-to-single-file`; output is whole-program oriented |
| `reko` | 8008 | Reko decompiler baseline |

Hosted CI runs the full core set by default and pulls prebuilt GHCR images when
available before falling back to local builds.

## Layered Quality Gates

Decompiler similarity is the final benchmark layer. Lower-level gates should be
run first when diagnosing Fission regressions:

1. `benchmark/assembly_parity` compares instruction bytes, mnemonics, operands,
   lengths, and branch targets from two assembly-listing providers.
2. `benchmark/decode_parity` compares decode fields such as instruction length,
   prefixes, ModRM/SIB, displacement, and immediate values.
3. `benchmark/pcode_parity` compares raw p-code op sequences from two providers,
   typically Ghidra raw p-code vs Fission SLEIGH runtime output.
4. `benchmark/cfg_parity` compares basic blocks and control-flow edges.
5. `benchmark/function_discovery` compares binary-level function discovery.
6. `benchmark/ir_invariants` checks Fission internal IR/NIR/HIR invariants
   without an external reference provider.
7. `benchmark/golden_repros` runs fixed regression canaries.
8. `benchmark/telemetry` aggregates JSONL rows by stage, status, mismatch kind,
   compiler, and optimization level.
9. `runner/` remains the decompiler-output quality benchmark.

Benchmark infrastructure is currently in reliability-maintenance mode. Before
adding new axes, default decompilers, or composite rankings, check
`benchmark/KNOWN_ISSUES.md`; the preferred next step is to turn confirmed
benchmark failures into Fission-side fixes and golden repros.

Parity runners accept command templates. Templates can use corpus subject fields
such as `{binary}`, `{addr}`, `{function}`, `{compiler}`, and `{opt}` and must
print JSON to stdout.

```bash
python -m benchmark.assembly_parity.run \
  --reference-command 'python tools/ref_asm.py {binary} {addr}' \
  --candidate-command 'python tools/fission_asm.py {binary} {addr}'

python -m benchmark.decode_parity.run \
  --reference-command 'python tools/ref_decode.py {binary} {addr}' \
  --candidate-command 'python tools/fission_decode.py {binary} {addr}'

python -m benchmark.pcode_parity.run \
  --reference-command 'python tools/ghidra_pcode.py {binary} {addr}' \
  --candidate-command 'python tools/fission_pcode.py {binary} {addr}'

python -m benchmark.cfg_parity.run \
  --reference-command 'python tools/ref_cfg.py {binary} {addr}' \
  --candidate-command 'python tools/fission_cfg.py {binary} {addr}'

python -m benchmark.function_discovery.run \
  --reference-command 'python tools/ref_functions.py {binary}' \
  --candidate-command 'python tools/fission_functions.py {binary}'

python -m benchmark.ir_invariants.run \
  --candidate-command 'python tools/fission_ir_invariants.py {binary} {addr}'

python -m benchmark.golden_repros.run benchmark/golden_repros/manifest.json

python -m benchmark.telemetry.aggregate \
  results/decode_parity/latest.jsonl \
  results/assembly_parity/latest.jsonl \
  results/pcode_parity/latest.jsonl
```

## Adding Corpus Cases

1. Add a C source file under `corpus/dev/source/`
2. Add a manifest under `corpus/dev/manifests/` with one entry per function
3. Use stable compiler variants such as `gcc -O0` and `gcc -O2`
4. Run `python scripts/build_corpus.py --split dev` before benchmarking

The build script compiles ignored local binaries under `corpus/dev/binaries/`
and refreshes each variant `addr` using `nm`. The runner scores against the
matching source function, not the whole source file.

## Scoring Metrics

| Metric | Description |
|---|---|
| **Source Similarity** | `difflib.SequenceMatcher` ratio vs normalized original C source (primary) |
| **Goto Count** | Fewer is better — indicates better control-flow recovery |
| **Nesting Depth** | Max `{` depth — high values indicate poor structuring |
| **Consensus Rank** | Rank among all decompilers by similarity for the same function |

## License

AGPL-3.0-or-later
