# Fission Benchmark Report

**Measured at:** not recorded
**Rendered at:** 2026-07-11 06:01 UTC
**Corpus:** `dev`
**Functions evaluated:** 1

---

## ✅ VALID RUN

> Fission 1/1 (100.0%), all-backend 1/1 (100.0%)

## Summary — Correctness Score

> Readability metrics are recorded as unvalidated raw proxies. They are not combined into a final readability score until the human validation study is complete.

| Decompiler | Attempted | Output Valid | Output Fail | Compile Fail | Runtime Fail | Timeout | No Wrapper | Avg Correctness | Avg Similarity | Semantic Pass |
| ---|---|---|---|---|---|---|---|---|---|--- |
| **fission** | 1 | 1 | 0 | — | — | — | — | 0.920 | 0.800 | 100.0% |

---

## Per-Function Results

### `foo`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.920 | 0.800 | 100.0% | — | 0 | 0 | — | 100ms | ✅ |

---

## Overfitting Analysis

Functions where **all** decompilers scored below 0.3 are marked as objectively hard.
Functions where **only Fission** scored below 0.3 are marked as quality gaps.

✅ No significant quality gaps detected.