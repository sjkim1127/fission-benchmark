# Fission Benchmark Report

**Generated:** 2026-07-01 18:19 UTC  
**Corpus:** `dev`  
**Functions evaluated:** 1

---

## Summary — Average Source Similarity

| Decompiler | Avg Similarity | Semantic Pass | Functions |
| ---|---|---|--- |
| **fission** | 0.119 | 25.0% | 4 |
| **boomerang** | 0.045 | 0.0% | 4 |

---

## Per-Function Results

### `count_bits`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| boomerang | gcc -O0 | 0.088 | 0 | #2 | 2 | 2 | 189ms | ✓ |
| boomerang | gcc-m32 -O0 | 0.002 | 0 | #2 | 8 | 8 | 1653ms | ✓ |
| boomerang | gcc -O2 | 0.088 | 0 | #2 | 2 | 2 | 177ms | ✓ |
| boomerang | gcc-m32 -O2 | 0.002 | 0 | #2 | 8 | 8 | 1623ms | ✓ |
| fission | gcc -O0 | 0.118 | 0 | #1 | 1 | 2 | 1832ms | ✓ |
| fission | gcc-m32 -O0 | 0.102 | 0 | #1 | 1 | 2 | 1778ms | ✓ |
| fission | gcc -O2 | 0.133 | 1 | #1 | 0 | 3 | 1847ms | ✓ |
| fission | gcc-m32 -O2 | 0.123 | 0 | #1 | 0 | 3 | 1778ms | ✓ |

---

## Overfitting Analysis

Functions where **all** decompilers scored below 0.3 are marked as objectively hard.
Functions where **only Fission** scored below 0.3 are marked as quality gaps.

**Objectively hard functions (1):** `count_bits`