# Fission Benchmark Report

**Generated:** 2026-07-02 11:02 UTC
**Corpus:** `dev`
**Functions evaluated:** 1

---

## Summary — Correctness Score

> Readability metrics are recorded as unvalidated raw proxies. They are not combined into a final readability score until the human validation study is complete.

| Decompiler | Correctness | Similarity | Semantic Pass | Functions |
| ---|---|---|---|--- |
| **angr** | 0.922 | 0.609 | 100.0% | 1 |
| **fission** | 0.343 | 0.118 | 33.3% | 1 |
| **ghidra** | 0.150 | 0.688 | 0.0% | 1 |
| **radare2** | 0.150 | 0.638 | 0.0% | 1 |
| **snowman** | 0.150 | 0.556 | 0.0% | 1 |
| **reko** | 0.150 | 0.408 | 0.0% | 1 |

---

## Per-Function Results

### `count_bits`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.922 | 0.609 | 100.0% (6/6) | #1 | 0 | 2 | GNR 0.33<br>type 0.50<br>expr 0.86<br>cf 1.00<br>art 0 | 496ms | ✅ |
| fission | gcc -O0 | 0.343 | 0.118 | 33.3% (2/6) ⚠️intrin | #2 | 1 | 2 | GNR 0.31<br>type 0.50<br>expr 0.62<br>cf 0.50<br>art 6 | 2486ms | 🟠 runtime |
| ghidra | gcc -O0 | 0.150 | 0.688 | 0.0% (0/6) | #3 | 0 | 2 | GNR 0.14<br>type 0.50<br>expr 0.85<br>cf 1.00<br>art 2 | 25089ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.150 | 0.638 | 0.0% (0/6) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 524ms | 🔴 compile |
| snowman | gcc -O0 | 0.150 | 0.556 | 0.0% (0/6) | #3 | 0 | 2 | GNR 0.79<br>type 0.50<br>expr 0.78<br>cf 1.00<br>art 0 | 396ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.408 | 0.0% (0/6) | #3 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 2775ms | 🔴 compile |
| boomerang | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 128ms | ❌ Function at address 0x14000153 |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 24578ms | ❌ Decompiler output does not mat |

---

## Overfitting Analysis

Functions where **all** decompilers scored below 0.3 are marked as objectively hard.
Functions where **only Fission** scored below 0.3 are marked as quality gaps.

✅ No significant quality gaps detected.