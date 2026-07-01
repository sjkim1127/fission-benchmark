# Fission Benchmark Report

**Generated:** 2026-07-01 19:59 UTC  
**Corpus:** `dev`  
**Functions evaluated:** 6

---

## Summary — Average Source Similarity

| Decompiler | Composite ⭐ | Similarity | Semantic Pass | Functions |
| ---|---|---|---|--- |
| **fission** | 0.000 | 0.160 | 0.0% | 6 |
| **ghidra** | 0.000 | 0.429 | 0.0% | 6 |
| **boomerang** | 0.000 | 0.041 | 0.0% | 6 |
| **radare2** | 0.000 | 0.008 | 0.0% | 6 |
| **angr** | 0.000 | 0.556 | 100.0% | 6 |
| **snowman** | 0.000 | 0.001 | 0.0% | 5 |
| **revng** | 0.000 | 0.001 | 0.0% | 5 |

---

## Per-Function Results

### `checksum` ⚪ Universally hard
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.000 | 0.103 | 0.0% | #3 | 2 | 2 | 5077ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.668 | 0.0% | #1 | 0 | 2 | 5578ms | ✅ |
| boomerang | gcc -O0 | 0.000 | 0.026 | 0.0% | #4 | 2 | 2 | 45ms | ✅ |
| radare2 | gcc -O0 | 0.000 | 0.012 | 0.0% | #5 | 0 | 0 | 106ms | ✅ |
| angr | gcc -O0 | 0.000 | 0.567 | 100.0% | #2 | 0 | 2 | 399ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 227 | 7 | 473ms | ✅ |
| revng | gcc -O0 | 0.000 | 0.001 | 0.0% | #7 | 0 | 10 | 42220ms | ✅ |

### `clamp` ⚪ Universally hard
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.000 | 0.414 | 0.0% | #3 | 0 | 1 | 5077ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.421 | 0.0% | #2 | 0 | 2 | 5578ms | ✅ |
| boomerang | gcc -O0 | 0.000 | 0.035 | 0.0% | #4 | 2 | 2 | 45ms | ✅ |
| radare2 | gcc -O0 | 0.000 | 0.005 | 0.0% | #5 | 0 | 0 | 106ms | ✅ |
| angr | gcc -O0 | 0.000 | 0.708 | 100.0% | #1 | 0 | 2 | 399ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 227 | 7 | 473ms | ✅ |
| revng | gcc -O0 | 0.000 | 0.001 | 0.0% | #7 | 0 | 10 | 42220ms | ✅ |

### `classify_range` ⚪ Universally hard
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.000 | 0.093 | 0.0% | #3 | 9 | 2 | 5077ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.167 | 0.0% | #2 | 0 | 3 | 5578ms | ✅ |
| boomerang | gcc -O0 | 0.000 | 0.033 | 0.0% | #4 | 2 | 2 | 45ms | ✅ |
| radare2 | gcc -O0 | 0.000 | 0.008 | 0.0% | #5 | 0 | 0 | 106ms | ✅ |
| angr | gcc -O0 | 0.000 | 0.182 | 100.0% | #1 | 0 | 2 | 399ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 227 | 7 | 473ms | ✅ |
| revng | gcc -O0 | 0.000 | 0.001 | 0.0% | #7 | 0 | 10 | 42220ms | ✅ |

### `count_bits` ⚪ Universally hard
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.000 | 0.135 | 0.0% | #3 | 2 | 2 | 5077ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.688 | 0.0% | #1 | 0 | 2 | 5578ms | ✅ |
| boomerang | gcc -O0 | 0.000 | 0.088 | 0.0% | #4 | 2 | 2 | 45ms | ✅ |
| radare2 | gcc -O0 | 0.000 | 0.009 | 0.0% | #5 | 0 | 0 | 106ms | ✅ |
| angr | gcc -O0 | 0.000 | 0.609 | 100.0% | #2 | 0 | 2 | 399ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 227 | 7 | 473ms | ✅ |
| revng | gcc -O0 | 0.000 | 0.001 | 0.0% | #7 | 0 | 10 | 42220ms | ✅ |

### `saturating_add` ⚪ Universally hard
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.000 | 0.063 | 0.0% | #3 | 3 | 2 | 5077ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.252 | 0.0% | #2 | 0 | 3 | 5578ms | ✅ |
| boomerang | gcc -O0 | 0.000 | 0.026 | 0.0% | #4 | 2 | 2 | 45ms | ✅ |
| radare2 | gcc -O0 | 0.000 | 0.011 | 0.0% | #5 | 0 | 0 | 106ms | ✅ |
| angr | gcc -O0 | 0.000 | 0.769 | 100.0% | #1 | 0 | 1 | 399ms | ✅ |

### `signum` ⚪ Universally hard
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.000 | 0.149 | 0.0% | #3 | 2 | 2 | 5077ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.375 | 0.0% | #2 | 0 | 3 | 5578ms | ✅ |
| boomerang | gcc -O0 | 0.000 | 0.037 | 0.0% | #4 | 2 | 2 | 45ms | ✅ |
| radare2 | gcc -O0 | 0.000 | 0.004 | 0.0% | #5 | 0 | 0 | 106ms | ✅ |
| angr | gcc -O0 | 0.000 | 0.503 | 100.0% | #1 | 0 | 1 | 399ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 227 | 7 | 473ms | ✅ |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | #7 | 0 | 10 | 42220ms | ✅ |

---

## Overfitting Analysis

Functions where **all** decompilers scored below 0.3 are marked as objectively hard.
Functions where **only Fission** scored below 0.3 are marked as quality gaps.

**Objectively hard functions (6):** `count_bits`, `clamp`, `signum`, `checksum`, `classify_range`, `saturating_add`