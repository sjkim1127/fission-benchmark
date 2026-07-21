# Dev vs Holdout Overfitting Report

- Dev results: `results/dev_publish.json`  
- Holdout results: `results/holdout_latest.json`  
- Overfitting threshold: **10.0pp** drop

## Summary by Decompiler

| Decompiler | Dev N | Dev Correctness | Holdout N | Holdout Correctness | Drop (pp) | Flag |
|---|---|---|---|---|---|---|
| **fission** | 210 | 0.564 | 29 | 0.563 | +0.1pp | ✅ |
| **ghidra** | 215 | 0.773 | 30 | 0.784 | -1.2pp | ✅ |
