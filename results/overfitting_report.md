# Dev vs Holdout Overfitting Report

- Dev results: `results/dev_latest.json`  
- Holdout results: `results/holdout_latest.json`  
- Overfitting threshold: **10.0pp** drop

## Summary by Decompiler

| Decompiler | Dev N | Dev Correctness | Holdout N | Holdout Correctness | Drop (pp) | Flag |
|---|---|---|---|---|---|---|
| **angr** | 10 | 0.764 | — | — | — | ⚠️ No holdout data |
| **boomerang** | 7 | 0.150 | — | — | — | ⚠️ No holdout data |
| **fission** | 10 | 0.266 | — | — | — | ⚠️ No holdout data |
| **ghidra** | 10 | 0.260 | — | — | — | ⚠️ No holdout data |
| **radare2** | 10 | 0.150 | — | — | — | ⚠️ No holdout data |
| **reko** | 10 | 0.150 | — | — | — | ⚠️ No holdout data |
| **revng** | 9 | 0.147 | — | — | — | ⚠️ No holdout data |
| **snowman** | 10 | 0.149 | — | — | — | ⚠️ No holdout data |
