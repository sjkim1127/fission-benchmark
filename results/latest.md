# Fission Benchmark Report

**Generated:** 2026-07-01 18:06 UTC  
**Corpus:** `dev`  
**Functions evaluated:** 3

---

## Summary — Average Source Similarity

| Decompiler | Avg Similarity | Semantic Pass | Functions |
| ---|---|---|--- |
| **ghidra** | 0.587 | 75.0% | 12 |
| **fission** | 0.248 | 8.3% | 12 |

---

## Per-Function Results

### `clamp`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.179 | 0 | #2 | 0 | 2 | 5556ms | ✓ |
| fission | gcc-m32 -O0 | 0.450 | 0 | #2 | 0 | 1 | 5159ms | ✓ |
| fission | gcc -O2 | 0.535 | 0 | #2 | 0 | 1 | 5286ms | ✓ |
| fission | gcc-m32 -O2 | 0.368 | 0 | #2 | 0 | 1 | 5088ms | ✓ |
| ghidra | gcc -O0 | 0.421 | 0 | #1 | 0 | 2 | 15574ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.590 | 1 | #1 | 0 | 2 | 13873ms | ✓ |
| ghidra | gcc -O2 | 0.582 | 1 | #1 | 0 | 2 | 15684ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.731 | 1 | #1 | 0 | 2 | 13268ms | ✓ |

### `count_bits`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.118 | 0 | #2 | 1 | 2 | 5556ms | ✓ |
| fission | gcc-m32 -O0 | 0.102 | 0 | #2 | 1 | 2 | 5159ms | ✓ |
| fission | gcc -O2 | 0.133 | 1 | #2 | 0 | 3 | 5286ms | ✓ |
| fission | gcc-m32 -O2 | 0.123 | 0 | #2 | 0 | 3 | 5088ms | ✓ |
| ghidra | gcc -O0 | 0.688 | 0 | #1 | 0 | 2 | 15574ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.755 | 1 | #1 | 0 | 2 | 13873ms | ✓ |
| ghidra | gcc -O2 | 0.609 | 1 | #1 | 0 | 2 | 15684ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.609 | 1 | #1 | 0 | 2 | 13268ms | ✓ |

### `signum`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.057 | 0 | #2 | 0 | 3 | 5556ms | ✓ |
| fission | gcc-m32 -O0 | 0.321 | 0 | #2 | 0 | 3 | 5159ms | ✓ |
| fission | gcc -O2 | 0.489 | 0 | #2 | 0 | 1 | 5286ms | ✓ |
| fission | gcc-m32 -O2 | 0.094 | 0 | #2 | 0 | 3 | 5088ms | ✓ |
| ghidra | gcc -O0 | 0.375 | 0 | #1 | 0 | 3 | 15574ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.611 | 1 | #1 | 0 | 3 | 13873ms | ✓ |
| ghidra | gcc -O2 | 0.492 | 1 | #1 | 0 | 2 | 15684ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.583 | 1 | #1 | 0 | 2 | 13268ms | ✓ |

---

## Overfitting Analysis

Functions where **all** decompilers scored below 0.3 are marked as objectively hard.
Functions where **only Fission** scored below 0.3 are marked as quality gaps.

**Fission quality gaps (1):** `count_bits`