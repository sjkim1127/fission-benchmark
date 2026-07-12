# Layered parity benchmarks

These stages compare Fission (or another candidate) against a **reference** —
by default **Ghidra** over the Docker HTTP adapters.

| Stage | Module | Reference | Candidate | Endpoint |
|-------|--------|-----------|-----------|----------|
| Assembly | `assembly_parity` | Ghidra | Fission | `/disasm` |
| Decode | `decode_parity` | Ghidra | Fission | `/decode` |
| P-code | `pcode_parity` | Ghidra | Fission | `/pcode` |
| CFG | `cfg_parity` | Ghidra | Fission | `/cfg` |
| Functions | `function_discovery` | Ghidra | Fission | `/functions` |
| IR invariants | `ir_invariants` | (self) | Fission | local checks |

## Prerequisites

```bash
docker compose up -d ghidra fission   # or full stack
# Local fission overlay often uses port 8007:
export FISSION_HOST_PORT=8007
```

### Ghidra performance

The Ghidra adapter keeps a **persistent project cache** (`ghidra-project-cache`
volume → `/var/cache/ghidra-projects`) and exposes **`GET /parity_bundle`**:

- One headless import emits `disasm` + `pcode` + `cfg` (+ `decode` derived).
- Re-open of the same binary uses `-process` (no re-import).
- In-process cache serves identical `(binary, mode, addr)` instantly.

`runner.run_parity` prefers `/parity_bundle` for the Ghidra reference side.

## One stage (HTTP defaults)

```bash
# Ghidra vs Fission assembly parity on first 2 subjects
python -m benchmark.assembly_parity.run --limit 2

python -m benchmark.cfg_parity.run --limit 2
python -m benchmark.pcode_parity.run --limit 2
python -m benchmark.decode_parity.run --limit 2
python -m benchmark.function_discovery.run --limit 2
```

## Unified runner

```bash
# Writes results/{assembly,decode,pcode,cfg,...}_parity/latest.jsonl
# and results/telemetry/latest.json
python -m runner.run_parity --corpus dev --limit 3 --decompilers fission,ghidra
```

## Custom providers

Command templates still work when you need offline tools:

```bash
python -m benchmark.assembly_parity.run \
  --reference-command 'python tools/ref_asm.py {binary} {addr}' \
  --candidate-command 'python tools/cand_asm.py {binary} {addr}'
```

## Output

JSONL rows use `benchmark.common.schema.BenchmarkResult`:

- `status`: `match` | `mismatch` | `error` | `fetch_error` | …
- `mismatch_kind`: stage-specific (e.g. `instruction_count`, `block_set`)
- `reference` / `candidate`: tool names (usually `ghidra` / `fission`)

Telemetry aggregation:

```bash
python -m benchmark.telemetry.aggregate \
  results/assembly_parity/latest.jsonl \
  results/cfg_parity/latest.jsonl \
  --output results/telemetry/latest.json
```
