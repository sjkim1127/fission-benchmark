<div align="center">

# fission-benchmark

**Multi-decompiler comparison benchmark for [Fission](https://github.com/sjkim1127/Fission)**

Fission · Ghidra · RetDec · Radare2+r2ghidra

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
│  │ Fission │  │ Ghidra  │  │ RetDec  │  │Radare2  │  │
│  │ :8000   │  │ :8001   │  │ :8002   │  │ :8003   │  │
│  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘  │
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
- `pip install httpx fastapi uvicorn jinja2 rich typer`

### Run

```bash
# Build decompiler containers
docker compose build

# Start containers
docker compose up -d

# Wait for health checks
curl http://localhost:8001/health  # Ghidra
curl http://localhost:8002/health  # RetDec
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

# Holdout evaluation (release only — never during development)
python runner/runner.py --use-holdout
```

## Repository Layout

```
fission-benchmark/
├── docker/
│   ├── ghidra/      Ghidra 12.x headless + FastAPI
│   ├── retdec/      RetDec 5.x + FastAPI
│   ├── radare2/     Radare2 + r2ghidra + FastAPI
│   └── fission/     Fission CLI + FastAPI (downloads from Releases)
├── runner/
│   ├── runner.py    Main orchestrator
│   ├── corpus.py    Corpus management + holdout split
│   ├── scoring.py   Source similarity + structural scoring
│   └── report.py    Markdown + HTML report generation
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

## Scoring Metrics

| Metric | Description |
|---|---|
| **Source Similarity** | `difflib.SequenceMatcher` ratio vs normalized original C source (primary) |
| **Goto Count** | Fewer is better — indicates better control-flow recovery |
| **Nesting Depth** | Max `{` depth — high values indicate poor structuring |
| **Consensus Rank** | Rank among all decompilers by similarity for the same function |

## License

AGPL-3.0-or-later
