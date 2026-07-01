# Dev vs Holdout Overfitting Report

- Dev results: `results/dev_latest.json`  
- Holdout results: `results/holdout_latest.json`  
- Overfitting threshold: **10.0pp** drop

## Summary by Decompiler

| Decompiler | Dev N | Dev Composite | Holdout N | Holdout Composite | Drop (pp) | Flag |
|---|---|---|---|---|---|---|
| **angr** | 140 | 0.119 | — | — | — | ⚠️ No holdout data |
| **boomerang** | 140 | 0.039 | — | — | — | ⚠️ No holdout data |
| **radare2** | 140 | 0.136 | — | — | — | ⚠️ No holdout data |
| **reko** | 140 | 0.123 | — | — | — | ⚠️ No holdout data |
| **snowman** | 140 | 0.000 | — | — | — | ⚠️ No holdout data |
