# Golden Repros

Fixed canaries for the integrated benchmark workspace. Two modes:

1. **Known-gap locks** — HTTP Ghidra vs Fission where we *expect* a mismatch
   kind (CFG/pcode gaps). Fails CI if the gap *changes unexpectedly* or infra
   breaks.
2. **Exact payload locks** — `command` + `expected` JSON for narrow bugs that
   must not regress once fixed.

## Manifest

Generated/updated from parity JSONL:

```bash
python scripts/extract_golden_repros.py \
  --inputs results/cfg_parity/latest.jsonl results/pcode_parity/latest.jsonl \
  --output benchmark/golden_repros/manifest.json \
  --limit-per-stage 5
```

Example case:

```json
{
  "name": "cfg_parity__count_bits__gcc-O0",
  "stage": "cfg_parity",
  "binary": "corpus/dev/binaries/control_flow_gcc_O0.exe",
  "function": "count_bits",
  "addr": "0x140001530",
  "reference_http": "ghidra",
  "candidate_http": "fission",
  "expect_status": "mismatch",
  "expect_mismatch_kind": "edge_set"
}
```

## Run

```bash
export FISSION_HOST_PORT=8007
python -m benchmark.golden_repros.run benchmark/golden_repros/manifest.json
```

Exit code 1 if any case does not meet its expectation (for CI canaries).
