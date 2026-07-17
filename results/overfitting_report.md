# Dev vs Holdout Overfitting Report

- Dev results: `results/dev_publish.json`  
- Holdout results: `results/holdout_latest.json`  
- Overfitting threshold: **10.0pp** drop

## Summary by Decompiler

| Decompiler | Dev N | Dev Correctness | Holdout N | Holdout Correctness | Drop (pp) | Flag |
|---|---|---|---|---|---|---|
| **fission** | 200 | 0.587 | 29 | 0.605 | -1.7pp | ✅ |
| **ghidra** | 215 | 0.773 | 30 | 0.751 | +2.1pp | ✅ |
