# Telemetry

Aggregates JSONL rows emitted by benchmark stages. The first version tracks:

- row count by stage
- row count by status
- row count by mismatch kind
- row count by compiler/optimization variant

Run example:

```bash
python -m benchmark.telemetry.aggregate \
  results/assembly_parity/latest.jsonl \
  results/pcode_parity/latest.jsonl \
  --output results/telemetry/latest.json
```
