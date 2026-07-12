# Function discovery benchmark

**What it measures:** can each tool **find functions** in a PE/ELF binary?

This is the **function-finding** track (inventory parity). It is **not** the
same-function decompile matrix (`runner/same_function_matrix.py`), which checks
that a `(binary, addr)` decompile request returns that single function.

## Contract

| Item | Definition |
|------|------------|
| **Unit** | One binary variant (compiler × opt), not one corpus function |
| **Request** | Adapter `GET /functions` → JSON list of `{address, name, size?, kind?}` |
| **Primary** | Normalized **address-set equality** (reference vs candidate) |
| **Dual** | `presence_recall`, `presence_precision`, `presence_f1`, `presence_jaccard` |
| **Manifest** | Optional `manifest_recall` = corpus subject VAs found by candidate |
| **Scoring tag** | `metrics.scored_as` ∈ `{ghidra_inventory, pe_symbol_inventory, manifest_inventory}` |

Exact set equality is **strict** (CRT / padding / heuristics often differ). Use
**dual recall/precision** for triage; use set match as an inventory canary.

### References

| Mode | Flag | Ground truth |
|------|------|----------------|
| Ghidra inventory (default) | `--reference-mode http` | Tool-relative reference |
| PE COFF / exports | `--reference-mode pe_symbols` | Unstripped symbols |
| Corpus manifests | `--reference-mode manifest` | Subject entry VAs only |

## Run

```bash
# Core: Ghidra vs Fission (default ports; set FISSION_HOST_PORT=8007 if needed)
export FISSION_HOST_PORT=8007
python -m benchmark.function_discovery.run --corpus dev --limit 5

# Multi-candidate discovery matrix
python -m benchmark.function_discovery.run \
  --corpus holdout \
  --candidates fission,radare2,snowman,boomerang,reko \
  --limit 10 \
  --summary-json results/function_discovery/summary.json \
  --summary-md results/function_discovery/summary.md

# Unstripped PE symbol oracle
python -m benchmark.function_discovery.run \
  --reference-mode pe_symbols \
  --candidates fission,ghidra \
  --limit 5

# Report only (from existing JSONL)
python -m runner.function_discovery_report \
  results/function_discovery/latest.jsonl \
  -o results/function_discovery/report.json \
  --markdown results/function_discovery/report.md --print
```

Also run as part of the unified layered suite:

```bash
python -m runner.run_parity --corpus dev --limit 5 --decompilers fission,ghidra
```

## Outputs

* `results/function_discovery/latest.jsonl` — one row per (binary × candidate)
* `results/function_discovery/summary.{json,md}` — cohort / candidate matrix
* Telemetry: `benchmark.telemetry.aggregate` → `dual.mean_presence_recall`, etc.

## Reliability rules

* Empty inventories are **never** matches (`both_empty_invalid` / empty sides).
* Rows without modern `scored_as` are flagged `legacy_presence_rows` by telemetry.
* Near-100% set match **without** dual metrics fails `scripts/check_reliability.py`.

## Related

* `runner/same_function_matrix.py` — decompile boundary honesty `(binary, addr)`
* `benchmark/strip_track/` — discovery on stripped PE
* `docs/BENCHMARK_OPERATING.md` — operating guide
