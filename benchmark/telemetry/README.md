# Telemetry

Aggregates JSONL rows emitted by benchmark stages. The first version tracks:

- row count by stage
- row count by status
- row count by mismatch kind
- row count by compiler/optimization variant

Run example:

```bash
python -m benchmark.telemetry.aggregate \
  results/decode_parity/latest.jsonl \
  results/assembly_parity/latest.jsonl \
  results/pcode_parity/latest.jsonl \
  results/cfg_parity/latest.jsonl \
  results/function_discovery/latest.jsonl \
  results/ir_invariants/latest.jsonl \
  results/golden_repros/latest.jsonl \
  --output results/telemetry/latest.json
```
