# Benchmark-first operating guide

This repository’s job is to be a **reliable measuring instrument** for decompiler
quality. Fission product work is secondary to measurement honesty here.

## Priority order

1. **Semantic evidence** (`original_binary` oracle) is the only ranking axis.
2. **Coverage + fail taxonomy** make denominators honest.
3. **Holdout + publication gate** protect against overfitting and bad publishes.
4. **CFG / runtime / cross-variant** are secondary or extension analysis.
5. Similarity / readability proxies are diagnostics only.

## Standard set contract

Every modern result envelope should carry:

```json
"summary": { "schema": "standard-set-v1", "mvp": { "by_decompiler": { ... } } }
```

Built by `runner/standard_summary.py` and attached in `build_envelope()`.

| Tier | Metric |
|------|--------|
| MVP-1 | Semantic pass rate |
| MVP-2 | Coverage |
| MVP-3 | Fail taxonomy |
| MVP-4 | CFG match (optional) |
| MVP-5 | Runtime |
| EXT-6 | Holdout / overfit |
| EXT-7 | Cross-compiler × opt |
| EXT-8 | Human study pack |
| EXT-9 | `corpus/realworld/` track |

## Local loop (measurement quality)

```bash
pip install -e ".[dev]"
docker compose build oracle   # after oracle changes
docker compose up -d          # decompilers + oracle as needed

# Candidate runs — never overwrite official latest without the gate
ORACLE_ENDPOINT=http://localhost:8010 python runner/runner.py \
  --corpus dev --run-mode smoke --output results/dev_latest.json

python scripts/check_benchmark_path.py results/dev_latest.json

# Official path (full matrix, no --limit)
ORACLE_ENDPOINT=http://localhost:8010 python runner/runner.py \
  --corpus dev --run-mode official --output results/dev_latest.json
ORACLE_ENDPOINT=http://localhost:8010 python runner/runner.py \
  --corpus holdout --run-mode official --output results/holdout_latest.json
python runner/holdout_report.py \
  --dev results/dev_latest.json --holdout results/holdout_latest.json \
  --json-output results/overfitting_report.json
python -m runner.publication_gate \
  --dev results/dev_latest.json \
  --holdout results/holdout_latest.json \
  --overfitting results/overfitting_report.json \
  --output results/publication-verdict.json
```

## Do / don’t

| Do | Don’t |
|----|--------|
| Fix adapters, boundaries, wrappers, oracle | Rank by source similarity |
| Keep `no_wrapper` visible | Treat untested as decompiler fail |
| Use holdout only for release evaluation | Tune Fission against holdout |
| Commit standard-set summary in envelopes | Promote `results/local_*.json` or legacy lists |
| Prefer taxonomy buckets for triage | Hide whole-program rows as “clean” |

## Offline contract check

```bash
python scripts/check_benchmark_path.py results/dev_latest.json
python scripts/check_benchmark_path.py --repair results/dev_latest.envelope.json
```

## Layered parity (Ghidra reference)

```bash
export FISSION_HOST_PORT=8007
# Smoke (CI default): 3 subjects
python -m runner.run_parity --corpus dev --limit 3 --decompilers fission,ghidra
python scripts/check_parity_smoke.py results/telemetry/latest.json

# Larger batch
python -m runner.run_parity --corpus dev --limit 20 --decompilers fission,ghidra
python -m benchmark.telemetry.aggregate  # → public/parity-telemetry.json

# Freeze known CFG/pcode gaps
python scripts/extract_golden_repros.py \
  --inputs results/cfg_parity/latest.jsonl results/pcode_parity/latest.jsonl
python -m benchmark.golden_repros.run
```

Dashboard panel: **Layered parity · Ghidra reference** (reads `/parity-telemetry.json`).

Ideas for the next axes: `docs/NEXT_BENCHMARK_IDEAS.md`.

## Related files

- `runner/standard_summary.py` — MVP aggregation
- `runner/run_parity.py` / `benchmark/*_parity` — layered stages
- `runner/run_validity.py` / `publication_gate.py` — quality gates
- `runner/differential_oracle.py` + `docker/oracle/` — original_binary
- `benchmark/KNOWN_ISSUES.md` — freeze policy
- `docs/NEXT_BENCHMARK_IDEAS.md` — roadmap
