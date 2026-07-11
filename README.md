<div align="center">

# fission-benchmark

**Multi-decompiler comparison benchmark for [Fission](https://github.com/sjkim1127/Fission)**

Fission · Ghidra · Radare2+r2ghidra · angr · Snowman · rev.ng · RetDec · Reko

[![Benchmark](https://github.com/sjkim1127/fission-benchmark/actions/workflows/benchmark.yml/badge.svg)](https://github.com/sjkim1127/fission-benchmark/actions/workflows/benchmark.yml)
[![Docker Build](https://github.com/sjkim1127/fission-benchmark/actions/workflows/build-check.yml/badge.svg)](https://github.com/sjkim1127/fission-benchmark/actions/workflows/build-check.yml)

📊 **[Live Dashboard →](https://fission-benchmark.vercel.app)**

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
│  Fission :8000 · Ghidra :8001 · RetDec :8002 · Radare2 :8003 │
│  angr :8004 · Snowman :8005 · rev.ng :8006 · Reko :8008      │
└──────────────────────────────┬───────────────────────────────┘
                               │
                     ↓
              scoring.py  (correctness score + consensus)
                     ↓
              render_report.py → results/latest.md + docs/index.html
                     ↓
              Vercel (official runs only) → fission-benchmark.vercel.app
```

## Run Validity

Every result file is evaluated by a two-tier verdict:

| Tier | Meaning | CLI exit |
|---|---|---|
| `valid` | Measurement quality OK — matrix complete, Fission ≥ 90%, all-backend ≥ 90% | — |
| `publishable` | `valid` AND `--run-mode official` AND no provenance issues | required for Vercel deploy |

A **smoke run** (`--run-mode smoke`, default on push) produces `valid=True, publishable=False` — workflow is green but nothing is published. An **official run** (`--run-mode official`, weekly schedule or manual dispatch) must also pass the publishability gate before deploying.

```bash
# Evaluate a result file directly
python -m runner.run_validity results/dev_latest.json \
  --github-env "$GITHUB_ENV" \
  --github-summary "$GITHUB_STEP_SUMMARY"
# Emits: MEASUREMENT_VALID=true/false, RUN_PUBLISHABLE=true/false
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
docker compose --profile tools run --rm corpus-builder

# Start containers
docker compose up -d

# Wait for health checks
curl http://localhost:8001/health  # Ghidra
curl http://localhost:8003/health  # Radare2

# Run benchmark (smoke, candidate JSON only — does not overwrite latest.*)
python runner/runner.py --corpus dev

# Run and publish to latest.* (local use only)
python runner/runner.py --corpus dev --publish

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
python runner/runner.py --corpus dev \
  --decompilers fission,ghidra,retdec,radare2,angr,snowman,revng,reko

# Skip a specific decompiler via environment variable
FISSION_ENDPOINT=skip python runner/runner.py --corpus dev
GHIDRA_ENDPOINT=skip python runner/runner.py --corpus dev

# Point a decompiler at a custom endpoint
GHIDRA_ENDPOINT=http://localhost:9001 python runner/runner.py --corpus dev
FISSION_ENDPOINT=http://localhost:9000 python runner/runner.py --corpus dev

# Any {NAME}_ENDPOINT variable is supported:
# RETDEC_ENDPOINT, RADARE2_ENDPOINT, ANGR_ENDPOINT,
# SNOWMAN_ENDPOINT, REVNG_ENDPOINT, REKO_ENDPOINT

# Holdout evaluation (release only — never during development)
python runner/runner.py --corpus holdout

# Full corpus (dev + holdout combined)
python runner/runner.py --corpus full

# Explicit run mode
python runner/runner.py --corpus dev --run-mode official  # marks as publishable candidate
python runner/runner.py --corpus dev --run-mode smoke     # default, no publish gate
python runner/runner.py --corpus dev --run-mode local     # local dev, non-official

# Save to a custom path (never overwrites latest.*)
python runner/runner.py --corpus dev \
  --output results/dev_latest.json --no-publish

# Render report from a saved result file
python runner/render_report.py \
  --input results/dev_latest.json \
  --corpus dev \
  --update-latest   # promotes to latest.json + latest.md + docs/index.html
```

### Local Fission build (quality loop only)

CI always uses a **GitHub Release** Fission bake (`FISSION_SOURCE=release`).
For day-to-day decompiler work you can mount a **current Linux `fission_cli` + `utils/`** into the same adapter:

```bash
# 1) Build / collect a Linux ELF CLI + utils (not macOS Mach-O).
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
  --output "results/local_${FISSION_GIT_SHA}.json" --no-publish
```

**Rules**

| Path | Fission binary | Results |
|---|---|---|
| CI official run → Vercel | Release tag only | Official timeline |
| Local quality loop | Current build (Linux ELF) | `results/local_<sha>.json` only |

## Repository Layout

```
fission-benchmark/
├── benchmark/
│   ├── KNOWN_ISSUES.md   Infrastructure freeze policy and remaining trust gaps
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
│   ├── runner.py         Main orchestrator (--corpus, --run-mode, --no-publish)
│   ├── corpus.py         Corpus management + holdout split
│   ├── scoring.py        Correctness score + structural metrics
│   ├── run_validity.py   Shared validity engine (measurement_valid / publishable)
│   ├── render_report.py  Non-destructive report renderer (--update-latest)
│   ├── readability.py    AST-based readability proxy metrics
│   └── report.py         Markdown + HTML report generation
├── scripts/
│   └── build_corpus.py   Compile corpus binaries + update function addresses
├── corpus/
│   ├── dev/         80% — development corpus (source + manifests)
│   └── holdout/     20% — holdout corpus (release evaluation only)
├── docs/            Dashboard static files (committed by CI, served via Vercel)
├── results/         Benchmark results (auto-committed by official CI runs)
├── tests/           Unit and integration tests
│   ├── test_run_validity.py      Validity engine tests (28 cases)
│   ├── test_render_report.py     Legacy correctness migration tests
│   └── test_report_integration.py  Report generation integration tests
├── vercel.json      Vercel static site config (serves docs/)
└── .github/
    └── workflows/
        ├── benchmark.yml     Smoke (push) + official (schedule/dispatch) runs
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

## CI Workflow

| Trigger | Run mode | Publishes? |
|---|---|---|
| `push` to `main` | `smoke` | No — candidate JSON only |
| Weekly schedule (`cron`) | `official` | Yes — if measurement valid |
| Manual dispatch | `official` | Yes — if measurement valid |
| `fission-release` dispatch | `official` | Yes — if measurement valid |

Official runs that pass the validity gate commit `results/` + `docs/` and deploy to **https://fission-benchmark.vercel.app** via Vercel CLI.

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
| `ghidra` | 8001 | Ghidra 12.x headless, primary reference baseline |
| `retdec` | 8002 | RetDec 5.x |
| `radare2` | 8003 | Radare2 + r2ghidra |
| `angr` | 8004 | Python API, function-address oriented |
| `snowman` | 8005 | Uses `nocode`; legacy baseline, amd64-only |
| `revng` | 8006 | Uses `decompile-to-single-file`; whole-program oriented |
| `reko` | 8008 | Reko decompiler |

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
`benchmark/KNOWN_ISSUES.md`.

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
| **Correctness Score** | `0.9 × semantic_score + 0.1 × source_similarity` — primary ranking metric |
| **Semantic Score** | Functional equivalence via test-case execution |
| **Source Similarity** | `difflib.SequenceMatcher` ratio vs normalized original C source |
| **Structural Penalty** | Penalty for goto count and nesting depth |
| **Consensus Rank** | Rank among all decompilers by correctness score for the same function |

## Result Envelope Format

All result files use a versioned envelope (`schema_version: 2`):

```json
{
  "schema_version": 2,
  "run": {
    "started_at": "2026-07-11T00:00:00Z",
    "finished_at": "2026-07-11T00:05:00Z",
    "duration_ms": 300000,
    "runner_commit": "abc1234",
    "corpus": "dev",
    "official": true
  },
  "matrix": {
    "expected_decompilers": ["fission", "ghidra"],
    "expected_cells": [
      { "decompiler": "fission", "function_name": "foo", "compiler_variant": "gcc -O0" }
    ],
    "expected_rows": 2,
    "observed_rows": 2
  },
  "validity": {
    "valid": true,
    "publishable": true,
    "fission_coverage": 1.0,
    "reasons": [],
    "publish_reasons": []
  },
  "rows": [ ... ]
}
```

Legacy flat-list files are supported for rendering but are always marked `publishable: false`.

## License

AGPL-3.0-or-later
