# Throughput / resource budget

**Status:** extension product metric (not correctness ranking).

Records wall-clock decompile (or disasm fallback) times and emits p50/p95
aggregates per decompiler.

```bash
python -m benchmark.throughput.run --limit 20 --decompilers fission,ghidra
```
