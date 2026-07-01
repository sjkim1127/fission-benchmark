# Fission Benchmark Report

**Generated:** 2026-07-01 17:59 UTC  
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
| fission | gcc -O0 | 0.179 | 0 | #2 | 0 | 2 | 800ms | ✓ |
| fission | gcc-m32 -O0 | 0.450 | 0 | #2 | 0 | 1 | 773ms | ✓ |
| fission | gcc -O2 | 0.535 | 0 | #2 | 0 | 1 | 813ms | ✓ |
| fission | gcc-m32 -O2 | 0.368 | 0 | #2 | 0 | 1 | 794ms | ✓ |
| ghidra | gcc -O0 | 0.421 | 0 | #1 | 0 | 2 | 9894ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.590 | 1 | #1 | 0 | 2 | 9902ms | ✓ |
| ghidra | gcc -O2 | 0.582 | 1 | #1 | 0 | 2 | 9895ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.731 | 1 | #1 | 0 | 2 | 9898ms | ✓ |

### `count_bits`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.118 | 0 | #2 | 1 | 2 | 800ms | ✓ |
| fission | gcc-m32 -O0 | 0.102 | 0 | #2 | 1 | 2 | 773ms | ✓ |
| fission | gcc -O2 | 0.133 | 1 | #2 | 0 | 3 | 813ms | ✓ |
| fission | gcc-m32 -O2 | 0.123 | 0 | #2 | 0 | 3 | 794ms | ✓ |
| ghidra | gcc -O0 | 0.688 | 0 | #1 | 0 | 2 | 9894ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.755 | 1 | #1 | 0 | 2 | 9902ms | ✓ |
| ghidra | gcc -O2 | 0.609 | 1 | #1 | 0 | 2 | 9895ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.609 | 1 | #1 | 0 | 2 | 9898ms | ✓ |

### `signum`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.057 | 0 | #2 | 0 | 3 | 800ms | ✓ |
| fission | gcc-m32 -O0 | 0.321 | 0 | #2 | 0 | 3 | 773ms | ✓ |
| fission | gcc -O2 | 0.489 | 0 | #2 | 0 | 1 | 813ms | ✓ |
| fission | gcc-m32 -O2 | 0.094 | 0 | #2 | 0 | 3 | 794ms | ✓ |
| ghidra | gcc -O0 | 0.375 | 0 | #1 | 0 | 3 | 9894ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.611 | 1 | #1 | 0 | 3 | 9902ms | ✓ |
| ghidra | gcc -O2 | 0.492 | 1 | #1 | 0 | 2 | 9895ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.583 | 1 | #1 | 0 | 2 | 9898ms | ✓ |

---

## Overfitting Analysis

Functions where **all** decompilers scored below 0.3 are marked as objectively hard.
Functions where **only Fission** scored below 0.3 are marked as quality gaps.

**Fission quality gaps (1):** `count_bits`