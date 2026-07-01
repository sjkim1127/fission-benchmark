<div align="center">

# fission-benchmark

**Multi-decompiler comparison benchmark for [Fission](https://github.com/sjkim1127/Fission)**

Fission · Ghidra · Radare2+r2ghidra · optional angr/Snowman/rev.ng

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
┌───────────────────────────────────────────────────────┐
│  runner.py  (parallel httpx requests)                 │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  │
│  │ Fission │  │ Ghidra  │  │Radare2  │  │
│  │ :8000   │  │ :8001   │  │ :8003   │  │
│  └────┬────┘  └────┬────┘  └────┬────┘  │
│  optional: angr :8004 · Snowman :8005 · rev.ng :8006   │
└───────┼────────────┼────────────┼─────────────┼───────┘
        └─────────────────────────┘
                     ↓
              scoring.py (source similarity + consensus)
                     ↓
              report.py → results/latest.md + docs/index.html
```

## Overfitting Prevention (3-Layer)

| Layer | Mechanism |
|---|---|
| **Train/Holdout** | 80/20 function-level split (fixed seed). Holdout requires `--use-holdout` flag. |
| **Cross-compiler** | Same source compiled with gcc -O0 and gcc -O2 — evaluated independently |
| **Multi-decompiler consensus** | If all decompilers score low → objectively hard. Only Fission low → quality gap. |

## Quick Start

### Requirements

- Docker + Docker Compose
- Python 3.11+
- GCC-compatible C compiler + `nm` (for corpus binary/address generation), or the Dockerized corpus builder below
- `pip install httpx fastapi uvicorn jinja2 rich typer`

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

# Experimental open-source backends
docker compose --profile experimental build angr snowman revng
docker compose --profile experimental up -d angr snowman revng
python runner/runner.py --corpus dev --decompilers fission,ghidra,angr,snowman,revng

# Skip an unavailable service, or point one at a custom endpoint
FISSION_ENDPOINT=skip python runner/runner.py --corpus dev
GHIDRA_ENDPOINT=http://localhost:9001 python runner/runner.py --corpus dev

# Holdout evaluation (release only — never during development)
python runner/runner.py --use-holdout
```

## Repository Layout

```
fission-benchmark/
├── benchmark/
│   ├── decode_parity/    Instruction decoder parity runner
│   ├── assembly_parity/  Instruction listing parity runner
│   ├── pcode_parity/     Raw p-code parity runner
│   ├── cfg_parity/       Basic block/edge parity runner
│   ├── function_discovery/  Binary-level function discovery parity
│   ├── ir_invariants/    Fission-internal IR invariant checks
│   ├── golden_repros/    Fixed regression canary runner
│   ├── telemetry/        JSONL result aggregation
│   ├── decompiler_quality/  Current output-quality stage marker
│   └── common/           Shared schemas, providers, JSONL helpers
├── docker/
│   ├── ghidra/      Ghidra 12.x headless + FastAPI
│   ├── retdec/      RetDec 5.x + FastAPI
│   ├── radare2/     Radare2 + r2ghidra + FastAPI
│   ├── fission/     Fission CLI + FastAPI (downloads from Releases)
│   ├── angr/        Optional angr decompiler + FastAPI
│   ├── snowman/     Optional Snowman/nocode + FastAPI
│   └── revng/       Optional rev.ng + FastAPI
├── runner/
│   ├── runner.py    Main orchestrator
│   ├── corpus.py    Corpus management + holdout split
│   ├── scoring.py   Source similarity + structural scoring
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

CI uses `FISSION_VERSION=latest` by default, so scheduled and manual benchmark
runs pull the latest published Fission release. The benchmark workflow also
accepts a cross-repository dispatch event so the Fission release pipeline can
trigger a run immediately after publishing:

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
```

## Adding a New Decompiler

1. Create `docker/<name>/Dockerfile` + `server.py` implementing the API contract above
2. Add the service to `docker-compose.yml` on the next available port
3. Add to `DECOMPILERS` dict in `runner/runner.py`
4. Add to `build-check.yml` matrix

## Optional Open-Source Backends

The default benchmark keeps the stable baseline to Fission, Ghidra, and
Radare2+r2ghidra. These optional backends are available for local experiments
and self-hosted runners:

| Backend | Port | Notes |
|---|---:|---|
| `angr` | 8004 | Python API, function-address oriented, useful independent baseline |
| `snowman` | 8005 | Uses `nocode`; legacy baseline, x86-64 image is amd64-only |
| `revng` | 8006 | Uses `decompile-to-single-file`; output is whole-program oriented |

Optional backends are not selected unless `--decompilers` names them or their
`*_ENDPOINT` environment variable is set. This keeps hosted CI from pulling
large experimental images by default.

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
