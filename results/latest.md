# Fission Benchmark Report

**Generated:** 2026-07-01 15:25 UTC  
**Corpus:** `dev`  
**Functions evaluated:** 21

---

## Summary — Average Source Similarity

| Decompiler | Avg Similarity | Functions |
| ---|---|--- |
| **fission** | 0.179 | 42 |
| **radare2** | 0.006 | 42 |

---

## Per-Function Results

### `accumulate_pairs`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.128 | #1 | 2 | 2 | 2536ms | ✓ |
| fission | gcc -O2 | 0.139 | #1 | 2 | 2 | 2185ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.009 | #2 | 0 | 0 | 306ms | ✓ |
| radare2 | gcc -O2 | 0.009 | #2 | 0 | 0 | 286ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `binary_search`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.062 | #1 | 6 | 2 | 4354ms | ✓ |
| fission | gcc -O2 | 0.056 | #1 | 6 | 2 | 2373ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.006 | #2 | 0 | 0 | 320ms | ✓ |
| radare2 | gcc -O2 | 0.009 | #2 | 0 | 0 | 309ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `bubble_sort`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.008 | #1 | 4 | 2 | 3324ms | ✓ |
| fission | gcc -O2 | 0.105 | #1 | 4 | 3 | 3157ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.006 | #2 | 0 | 0 | 313ms | ✓ |
| radare2 | gcc -O2 | 0.007 | #2 | 0 | 0 | 291ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `checksum`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.103 | #1 | 2 | 2 | 2362ms | ✓ |
| fission | gcc -O2 | 0.170 | #1 | 0 | 3 | 1754ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.012 | #2 | 0 | 0 | 348ms | ✓ |
| radare2 | gcc -O2 | 0.012 | #2 | 0 | 0 | 303ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `clamp`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.179 | #1 | 0 | 2 | 1672ms | ✓ |
| fission | gcc -O2 | 0.535 | #1 | 0 | 1 | 1496ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.005 | #2 | 0 | 0 | 311ms | ✓ |
| radare2 | gcc -O2 | 0.006 | #2 | 0 | 0 | 302ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `classify_range`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.093 | #1 | 9 | 2 | 2160ms | ✓ |
| fission | gcc -O2 | 0.513 | #1 | 0 | 3 | 1593ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.008 | #2 | 0 | 0 | 318ms | ✓ |
| radare2 | gcc -O2 | 0.009 | #2 | 0 | 0 | 322ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `count_bits`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.118 | #1 | 1 | 2 | 6255ms | ✓ |
| fission | gcc -O2 | 0.133 | #1 | 0 | 3 | 1809ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.009 | #2 | 0 | 0 | 318ms | ✓ |
| radare2 | gcc -O2 | 0.008 | #2 | 0 | 0 | 305ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `factorial`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.035 | #1 | 0 | 3 | 2185ms | ✓ |
| fission | gcc -O2 | 0.244 | #1 | 1 | 2 | 1748ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.004 | #2 | 0 | 0 | 294ms | ✓ |
| radare2 | gcc -O2 | 0.003 | #2 | 0 | 0 | 315ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `fibonacci`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.044 | #1 | 0 | 3 | 2347ms | ✓ |
| fission | gcc -O2 | 0.172 | #1 | 1 | 3 | 2490ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.004 | #2 | 0 | 0 | 322ms | ✓ |
| radare2 | gcc -O2 | 0.004 | #2 | 0 | 0 | 326ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `fibonacci_iter`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.176 | #1 | 4 | 2 | 2090ms | ✓ |
| fission | gcc -O2 | 0.245 | #1 | 0 | 2 | 1822ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.007 | #2 | 0 | 0 | 333ms | ✓ |
| radare2 | gcc -O2 | 0.008 | #2 | 0 | 0 | 331ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `find_pair_value`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.095 | #1 | 3 | 2 | 2079ms | ✓ |
| fission | gcc -O2 | 0.165 | #1 | 3 | 4 | 1715ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.005 | #2 | 0 | 0 | 296ms | ✓ |
| radare2 | gcc -O2 | 0.005 | #2 | 0 | 0 | 291ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `gcd`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.081 | #1 | 1 | 2 | 1974ms | ✓ |
| fission | gcc -O2 | 0.107 | #1 | 0 | 2 | 2035ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.004 | #2 | 0 | 0 | 328ms | ✓ |
| radare2 | gcc -O2 | 0.004 | #2 | 0 | 0 | 309ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `linear_search`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.124 | #1 | 3 | 2 | 2071ms | ✓ |
| fission | gcc -O2 | 0.154 | #1 | 3 | 4 | 1735ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.005 | #2 | 0 | 0 | 302ms | ✓ |
| radare2 | gcc -O2 | 0.005 | #2 | 0 | 0 | 320ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `max`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.365 | #1 | 0 | 1 | 1576ms | ✓ |
| fission | gcc -O2 | 0.579 | #1 | 0 | 1 | 1531ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.002 | #2 | 0 | 0 | 332ms | ✓ |
| radare2 | gcc -O2 | 0.002 | #2 | 0 | 0 | 314ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `pointer_stride_sum`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.135 | #1 | 1 | 2 | 1906ms | ✓ |
| fission | gcc -O2 | 0.319 | #1 | 0 | 3 | 1900ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.005 | #2 | 0 | 0 | 331ms | ✓ |
| radare2 | gcc -O2 | 0.006 | #2 | 0 | 0 | 306ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `power`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.076 | #1 | 1 | 2 | 2150ms | ✓ |
| fission | gcc -O2 | 0.081 | #1 | 2 | 5 | 1728ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.008 | #2 | 0 | 0 | 321ms | ✓ |
| radare2 | gcc -O2 | 0.008 | #2 | 0 | 0 | 325ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `process_code`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.068 | #1 | 4 | 3 | 1998ms | ✓ |
| fission | gcc -O2 | 0.331 | #1 | 0 | 1 | 1678ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.005 | #2 | 0 | 0 | 306ms | ✓ |
| radare2 | gcc -O2 | 0.006 | #2 | 0 | 0 | 311ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `reverse_in_place`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.106 | #1 | 2 | 2 | 2898ms | ✓ |
| fission | gcc -O2 | 0.131 | #1 | 2 | 3 | 2139ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.006 | #2 | 0 | 0 | 294ms | ✓ |
| radare2 | gcc -O2 | 0.006 | #2 | 0 | 0 | 309ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `saturating_add`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.061 | #1 | 2 | 3 | 2270ms | ✓ |
| fission | gcc -O2 | 0.294 | #1 | 1 | 2 | 1777ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.011 | #2 | 0 | 0 | 312ms | ✓ |
| radare2 | gcc -O2 | 0.012 | #2 | 0 | 0 | 364ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `signum`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.057 | #1 | 0 | 3 | 1554ms | ✓ |
| fission | gcc -O2 | 0.489 | #1 | 0 | 1 | 1508ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.004 | #2 | 0 | 0 | 298ms | ✓ |
| radare2 | gcc -O2 | 0.003 | #2 | 0 | 0 | 299ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `sum_array`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.105 | #1 | 1 | 2 | 1915ms | ✓ |
| fission | gcc -O2 | 0.357 | #1 | 0 | 3 | 1732ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.008 | #2 | 0 | 0 | 289ms | ✓ |
| radare2 | gcc -O2 | 0.008 | #2 | 0 | 0 | 307ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

---

## Overfitting Analysis

Functions where **all** decompilers scored below 0.3 are marked as objectively hard.
Functions where **only Fission** scored below 0.3 are marked as quality gaps.

**Objectively hard functions (14):** `count_bits`, `checksum`, `saturating_add`, `reverse_in_place`, `find_pair_value`, `accumulate_pairs`, `fibonacci`, `fibonacci_iter`, `bubble_sort`, `linear_search`, `binary_search`, `factorial`, `gcd`, `power`