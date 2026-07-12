# Optimization cliff matrix

**Status:** extension analysis.

Pivots envelope semantic/correctness scores by `-O0`/`-O2` (etc.) and reports
O0→O2 drop per decompiler.

```bash
python -m benchmark.opt_cliff.run --envelope results/dev_latest.json
```
