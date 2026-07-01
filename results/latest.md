# Fission Benchmark Report

**Generated:** 2026-07-01 16:04 UTC  
**Corpus:** `dev`  
**Functions evaluated:** 21

---

## Summary — Average Source Similarity

| Decompiler | Avg Similarity | Functions |
| ---|---|--- |
| **ghidra** | 0.385 | 42 |
| **fission** | 0.178 | 42 |
| **radare2** | 0.006 | 42 |

---

## Per-Function Results

### `accumulate_pairs`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.128 | #2 | 2 | 2 | 3332ms | ✓ |
| fission | gcc -O2 | 0.139 | #1 | 2 | 2 | 2420ms | ✓ |
| ghidra | gcc -O0 | 0.517 | #1 | 0 | 2 | 14488ms | ✓ |
| ghidra | gcc -O2 | 0.120 | #2 | 0 | 3 | 14678ms | ✓ |
| radare2 | gcc -O0 | 0.009 | #3 | 0 | 0 | 376ms | ✓ |
| radare2 | gcc -O2 | 0.009 | #3 | 0 | 0 | 367ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 29ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 28ms | ❌ No matching plugins found for 'GCC'
No m |

### `binary_search`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.062 | #2 | 6 | 2 | 4916ms | ✓ |
| fission | gcc -O2 | 0.056 | #2 | 6 | 2 | 2781ms | ✓ |
| ghidra | gcc -O0 | 0.242 | #1 | 0 | 3 | 15179ms | ✓ |
| ghidra | gcc -O2 | 0.239 | #1 | 0 | 5 | 14636ms | ✓ |
| radare2 | gcc -O0 | 0.006 | #3 | 0 | 0 | 384ms | ✓ |
| radare2 | gcc -O2 | 0.009 | #3 | 0 | 0 | 341ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 30ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 29ms | ❌ No matching plugins found for 'GCC'
No m |

### `bubble_sort`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.008 | #2 | 4 | 2 | 4516ms | ✓ |
| fission | gcc -O2 | 0.105 | #2 | 4 | 3 | 4130ms | ✓ |
| ghidra | gcc -O0 | 0.167 | #1 | 0 | 4 | 14766ms | ✓ |
| ghidra | gcc -O2 | 0.131 | #1 | 0 | 5 | 15072ms | ✓ |
| radare2 | gcc -O0 | 0.006 | #3 | 0 | 0 | 395ms | ✓ |
| radare2 | gcc -O2 | 0.007 | #3 | 0 | 0 | 409ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 29ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 29ms | ❌ No matching plugins found for 'GCC'
No m |

### `checksum`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.103 | #2 | 2 | 2 | 2685ms | ✓ |
| fission | gcc -O2 | 0.126 | #2 | 0 | 3 | 2085ms | ✓ |
| ghidra | gcc -O0 | 0.668 | #1 | 0 | 2 | 14508ms | ✓ |
| ghidra | gcc -O2 | 0.129 | #1 | 0 | 3 | 14248ms | ✓ |
| radare2 | gcc -O0 | 0.012 | #3 | 0 | 0 | 353ms | ✓ |
| radare2 | gcc -O2 | 0.012 | #3 | 0 | 0 | 364ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 29ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 29ms | ❌ No matching plugins found for 'GCC'
No m |

### `clamp`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.179 | #2 | 0 | 2 | 2082ms | ✓ |
| fission | gcc -O2 | 0.535 | #2 | 0 | 1 | 1860ms | ✓ |
| ghidra | gcc -O0 | 0.421 | #1 | 0 | 2 | 14525ms | ✓ |
| ghidra | gcc -O2 | 0.582 | #1 | 0 | 2 | 14294ms | ✓ |
| radare2 | gcc -O0 | 0.005 | #3 | 0 | 0 | 366ms | ✓ |
| radare2 | gcc -O2 | 0.006 | #3 | 0 | 0 | 353ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 29ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 29ms | ❌ No matching plugins found for 'GCC'
No m |

### `classify_range`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.093 | #2 | 9 | 2 | 2898ms | ✓ |
| fission | gcc -O2 | 0.513 | #1 | 0 | 3 | 1974ms | ✓ |
| ghidra | gcc -O0 | 0.167 | #1 | 0 | 3 | 14463ms | ✓ |
| ghidra | gcc -O2 | 0.486 | #2 | 0 | 3 | 14506ms | ✓ |
| radare2 | gcc -O0 | 0.008 | #3 | 0 | 0 | 363ms | ✓ |
| radare2 | gcc -O2 | 0.009 | #3 | 0 | 0 | 350ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 30ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 31ms | ❌ No matching plugins found for 'GCC'
No m |

### `count_bits`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.118 | #2 | 1 | 2 | 7992ms | ✓ |
| fission | gcc -O2 | 0.133 | #2 | 0 | 3 | 2110ms | ✓ |
| ghidra | gcc -O0 | 0.688 | #1 | 0 | 2 | 19455ms | ✓ |
| ghidra | gcc -O2 | 0.609 | #1 | 0 | 2 | 14378ms | ✓ |
| radare2 | gcc -O0 | 0.009 | #3 | 0 | 0 | 378ms | ✓ |
| radare2 | gcc -O2 | 0.008 | #3 | 0 | 0 | 344ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 55ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 30ms | ❌ No matching plugins found for 'GCC'
No m |

### `factorial`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.035 | #2 | 0 | 3 | 2623ms | ✓ |
| fission | gcc -O2 | 0.244 | #1 | 1 | 2 | 2195ms | ✓ |
| ghidra | gcc -O0 | 0.335 | #1 | 0 | 2 | 14283ms | ✓ |
| ghidra | gcc -O2 | 0.212 | #2 | 0 | 3 | 14491ms | ✓ |
| radare2 | gcc -O0 | 0.004 | #3 | 0 | 0 | 381ms | ✓ |
| radare2 | gcc -O2 | 0.003 | #3 | 0 | 0 | 373ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 30ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 29ms | ❌ No matching plugins found for 'GCC'
No m |

### `fibonacci`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.044 | #2 | 0 | 3 | 2780ms | ✓ |
| fission | gcc -O2 | 0.172 | #2 | 1 | 3 | 2958ms | ✓ |
| ghidra | gcc -O0 | 0.321 | #1 | 0 | 2 | 14694ms | ✓ |
| ghidra | gcc -O2 | 0.218 | #1 | 0 | 3 | 14604ms | ✓ |
| radare2 | gcc -O0 | 0.004 | #3 | 0 | 0 | 348ms | ✓ |
| radare2 | gcc -O2 | 0.004 | #3 | 0 | 0 | 374ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 30ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 28ms | ❌ No matching plugins found for 'GCC'
No m |

### `fibonacci_iter`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.173 | #2 | 4 | 2 | 2572ms | ✓ |
| fission | gcc -O2 | 0.245 | #1 | 0 | 2 | 1943ms | ✓ |
| ghidra | gcc -O0 | 0.480 | #1 | 0 | 3 | 14564ms | ✓ |
| ghidra | gcc -O2 | 0.241 | #2 | 0 | 3 | 14416ms | ✓ |
| radare2 | gcc -O0 | 0.007 | #3 | 0 | 0 | 363ms | ✓ |
| radare2 | gcc -O2 | 0.008 | #3 | 0 | 0 | 351ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 29ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 29ms | ❌ No matching plugins found for 'GCC'
No m |

### `find_pair_value`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.095 | #2 | 3 | 2 | 2492ms | ✓ |
| fission | gcc -O2 | 0.165 | #2 | 3 | 4 | 2033ms | ✓ |
| ghidra | gcc -O0 | 0.342 | #1 | 0 | 3 | 14547ms | ✓ |
| ghidra | gcc -O2 | 0.212 | #1 | 0 | 4 | 14490ms | ✓ |
| radare2 | gcc -O0 | 0.005 | #3 | 0 | 0 | 375ms | ✓ |
| radare2 | gcc -O2 | 0.005 | #3 | 0 | 0 | 335ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 29ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 29ms | ❌ No matching plugins found for 'GCC'
No m |

### `gcd`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.081 | #2 | 1 | 2 | 2292ms | ✓ |
| fission | gcc -O2 | 0.107 | #2 | 0 | 2 | 2213ms | ✓ |
| ghidra | gcc -O0 | 0.596 | #1 | 0 | 2 | 14412ms | ✓ |
| ghidra | gcc -O2 | 0.778 | #1 | 0 | 2 | 14813ms | ✓ |
| radare2 | gcc -O0 | 0.004 | #3 | 0 | 0 | 360ms | ✓ |
| radare2 | gcc -O2 | 0.004 | #3 | 0 | 0 | 380ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 29ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 30ms | ❌ No matching plugins found for 'GCC'
No m |

### `linear_search`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.124 | #2 | 3 | 2 | 2455ms | ✓ |
| fission | gcc -O2 | 0.154 | #2 | 3 | 4 | 2094ms | ✓ |
| ghidra | gcc -O0 | 0.371 | #1 | 0 | 3 | 14662ms | ✓ |
| ghidra | gcc -O2 | 0.660 | #1 | 0 | 4 | 14852ms | ✓ |
| radare2 | gcc -O0 | 0.005 | #3 | 0 | 0 | 357ms | ✓ |
| radare2 | gcc -O2 | 0.005 | #3 | 0 | 0 | 390ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 29ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 29ms | ❌ No matching plugins found for 'GCC'
No m |

### `max`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.365 | #2 | 0 | 1 | 1882ms | ✓ |
| fission | gcc -O2 | 0.579 | #2 | 0 | 1 | 1720ms | ✓ |
| ghidra | gcc -O0 | 0.431 | #1 | 0 | 2 | 14548ms | ✓ |
| ghidra | gcc -O2 | 0.654 | #1 | 0 | 2 | 14538ms | ✓ |
| radare2 | gcc -O0 | 0.002 | #3 | 0 | 0 | 377ms | ✓ |
| radare2 | gcc -O2 | 0.002 | #3 | 0 | 0 | 375ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 30ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 29ms | ❌ No matching plugins found for 'GCC'
No m |

### `pointer_stride_sum`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.135 | #2 | 1 | 2 | 2213ms | ✓ |
| fission | gcc -O2 | 0.319 | #2 | 0 | 3 | 2091ms | ✓ |
| ghidra | gcc -O0 | 0.259 | #1 | 0 | 2 | 14624ms | ✓ |
| ghidra | gcc -O2 | 0.609 | #1 | 0 | 2 | 14616ms | ✓ |
| radare2 | gcc -O0 | 0.005 | #3 | 0 | 0 | 345ms | ✓ |
| radare2 | gcc -O2 | 0.006 | #3 | 0 | 0 | 336ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 29ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 29ms | ❌ No matching plugins found for 'GCC'
No m |

### `power`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.076 | #2 | 1 | 2 | 2346ms | ✓ |
| fission | gcc -O2 | 0.081 | #2 | 2 | 5 | 2051ms | ✓ |
| ghidra | gcc -O0 | 0.374 | #1 | 0 | 3 | 14330ms | ✓ |
| ghidra | gcc -O2 | 0.392 | #1 | 0 | 4 | 14270ms | ✓ |
| radare2 | gcc -O0 | 0.008 | #3 | 0 | 0 | 385ms | ✓ |
| radare2 | gcc -O2 | 0.008 | #3 | 0 | 0 | 370ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 30ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 30ms | ❌ No matching plugins found for 'GCC'
No m |

### `process_code`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.068 | #2 | 4 | 3 | 2311ms | ✓ |
| fission | gcc -O2 | 0.331 | #1 | 0 | 1 | 2038ms | ✓ |
| ghidra | gcc -O0 | 0.157 | #1 | 0 | 4 | 14784ms | ✓ |
| ghidra | gcc -O2 | 0.286 | #2 | 0 | 2 | 14317ms | ✓ |
| radare2 | gcc -O0 | 0.005 | #3 | 0 | 0 | 435ms | ✓ |
| radare2 | gcc -O2 | 0.006 | #3 | 0 | 0 | 329ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 30ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 31ms | ❌ No matching plugins found for 'GCC'
No m |

### `reverse_in_place`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.106 | #2 | 2 | 2 | 3793ms | ✓ |
| fission | gcc -O2 | 0.131 | #2 | 2 | 3 | 2298ms | ✓ |
| ghidra | gcc -O0 | 0.323 | #1 | 0 | 2 | 14812ms | ✓ |
| ghidra | gcc -O2 | 0.221 | #1 | 0 | 3 | 14641ms | ✓ |
| radare2 | gcc -O0 | 0.006 | #3 | 0 | 0 | 360ms | ✓ |
| radare2 | gcc -O2 | 0.006 | #3 | 0 | 0 | 368ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 30ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 31ms | ❌ No matching plugins found for 'GCC'
No m |

### `saturating_add`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.061 | #2 | 2 | 3 | 2528ms | ✓ |
| fission | gcc -O2 | 0.290 | #2 | 1 | 2 | 1923ms | ✓ |
| ghidra | gcc -O0 | 0.252 | #1 | 0 | 3 | 14597ms | ✓ |
| ghidra | gcc -O2 | 0.606 | #1 | 0 | 2 | 14598ms | ✓ |
| radare2 | gcc -O0 | 0.011 | #3 | 0 | 0 | 371ms | ✓ |
| radare2 | gcc -O2 | 0.012 | #3 | 0 | 0 | 350ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 30ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 24ms | ❌ No matching plugins found for 'GCC'
No m |

### `signum`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.057 | #2 | 0 | 3 | 1920ms | ✓ |
| fission | gcc -O2 | 0.489 | #2 | 0 | 1 | 1883ms | ✓ |
| ghidra | gcc -O0 | 0.375 | #1 | 0 | 3 | 14336ms | ✓ |
| ghidra | gcc -O2 | 0.492 | #1 | 0 | 2 | 14286ms | ✓ |
| radare2 | gcc -O0 | 0.004 | #3 | 0 | 0 | 367ms | ✓ |
| radare2 | gcc -O2 | 0.003 | #3 | 0 | 0 | 364ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 29ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 30ms | ❌ No matching plugins found for 'GCC'
No m |

### `sum_array`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.105 | #2 | 1 | 2 | 2205ms | ✓ |
| fission | gcc -O2 | 0.357 | #1 | 0 | 3 | 2090ms | ✓ |
| ghidra | gcc -O0 | 0.648 | #1 | 0 | 2 | 14764ms | ✓ |
| ghidra | gcc -O2 | 0.171 | #2 | 0 | 3 | 14450ms | ✓ |
| radare2 | gcc -O0 | 0.008 | #3 | 0 | 0 | 375ms | ✓ |
| radare2 | gcc -O2 | 0.008 | #3 | 0 | 0 | 327ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 47ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 30ms | ❌ No matching plugins found for 'GCC'
No m |

---

## Overfitting Analysis

Functions where **all** decompilers scored below 0.3 are marked as objectively hard.
Functions where **only Fission** scored below 0.3 are marked as quality gaps.

**Objectively hard functions (2):** `bubble_sort`, `binary_search`
**Fission quality gaps (12):** `count_bits`, `checksum`, `saturating_add`, `reverse_in_place`, `find_pair_value`, `accumulate_pairs`, `fibonacci`, `fibonacci_iter`, `linear_search`, `factorial`, `gcd`, `power`