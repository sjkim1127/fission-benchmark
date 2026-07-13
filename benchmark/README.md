# Layered parity benchmarks

These stages compare Fission (or another candidate) against a **reference** —
by default **Ghidra** over the Docker HTTP adapters.

| Stage | Module | Reference | Candidate | Endpoint | Headline? |
|-------|--------|-----------|-----------|----------|-----------|
| Assembly | `assembly_parity` | Ghidra | Fission | `/disasm` | Yes |
| Decode | `decode_parity` | — | — | retired | No |
| P-code | `pcode_parity` | Ghidra | Fission | `/pcode` | Yes |
| CFG | `cfg_parity` | Ghidra | Fission | `/cfg` | Yes |
| Functions | `function_discovery` | Ghidra | Fission | `/functions` | Yes |
| Program metadata | `metadata_parity` | Ghidra | Fission | `/metadata` | Ext |
| IR invariants | `ir_invariants` | (self) | Fission | local | No |
| ABI | `abi_parity` | Ghidra | Fission | `/abi` | Ext |
| Types | `type_parity` | Ghidra | Fission | `/types` | Ext |
| Call graph | `callgraph_parity` | Ghidra | Fission | `/callgraph` | Ext |
| Strings | `string_recovery` | Ghidra | Fission | `/strings` | Ext |
| Data-flow | `dataflow_parity` | Ghidra | Fission | `/dataflow` | Ext |
| SEH | `seh_parity` | Ghidra | Fission | `/seh` | Ext |
| Strip | `strip_track` | Ghidra | Fission | `/functions` | Ext |
| Opt cliff | `opt_cliff` | envelope pivot | — | — | Ext |
| Throughput | `throughput` | wall clock | — | `/decompile` | Ext |

```bash
# Headline layers
python -m runner.run_parity --corpus dev --limit 20 --decompilers fission,ghidra
# Extension layers
python -m runner.run_extensions --corpus dev --limit 20
# PR canary
scripts/pr_canary.sh
```

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
python -m benchmark.metadata_parity.run --limit 1
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
