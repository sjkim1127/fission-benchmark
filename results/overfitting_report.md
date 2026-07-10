# Dev vs Holdout Overfitting Report

- Dev results: `results/dev_latest.json`  
- Holdout results: `results/holdout_latest.json`  
- Overfitting threshold: **10.0pp** drop

## Summary by Decompiler

| Decompiler | Dev N | Dev Correctness | Holdout N | Holdout Correctness | Drop (pp) | Flag |
|---|---|---|---|---|---|---|
| **angr** | 10 | 0.787 | — | — | — | ⚠️ No holdout data |
| **boomerang** | 9 | 0.119 | — | — | — | ⚠️ No holdout data |
| **fission** | 10 | 0.267 | — | — | — | ⚠️ No holdout data |
| **ghidra** | 10 | 0.234 | — | — | — | ⚠️ No holdout data |
| **radare2** | 10 | 0.133 | — | — | — | ⚠️ No holdout data |
| **reko** | 10 | 0.121 | — | — | — | ⚠️ No holdout data |
| **revng** | 9 | 0.093 | — | — | — | ⚠️ No holdout data |
| **snowman** | 10 | 0.101 | — | — | — | ⚠️ No holdout data |
