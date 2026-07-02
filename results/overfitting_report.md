# Dev vs Holdout Overfitting Report

- Dev results: `results/dev_latest.json`  
- Holdout results: `results/holdout_latest.json`  
- Overfitting threshold: **10.0pp** drop

## Summary by Decompiler

| Decompiler | Dev N | Dev Composite | Holdout N | Holdout Composite | Drop (pp) | Flag |
|---|---|---|---|---|---|---|
| **angr** | 10 | 0.120 | — | — | — | ⚠️ No holdout data |
| **boomerang** | 10 | 0.076 | — | — | — | ⚠️ No holdout data |
| **fission** | 10 | 0.254 | — | — | — | ⚠️ No holdout data |
| **ghidra** | 10 | 0.232 | — | — | — | ⚠️ No holdout data |
| **radare2** | 10 | 0.144 | — | — | — | ⚠️ No holdout data |
| **reko** | 10 | 0.133 | — | — | — | ⚠️ No holdout data |
| **revng** | 9 | 0.098 | — | — | — | ⚠️ No holdout data |
| **snowman** | 10 | 0.000 | — | — | — | ⚠️ No holdout data |
