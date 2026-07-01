# Fission Benchmark Report

**Generated:** 2026-07-01 15:34 UTC  
**Corpus:** `dev`  
**Functions evaluated:** 21

---

## Summary — Average Source Similarity

| Decompiler | Avg Similarity | Functions |
| ---|---|--- |
| **fission** | 0.180 | 42 |
| **radare2** | 0.006 | 42 |

---

## Per-Function Results

### `accumulate_pairs`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.128 | #1 | 2 | 2 | 2462ms | ✓ |
| fission | gcc -O2 | 0.139 | #1 | 2 | 2 | 2101ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.009 | #2 | 0 | 0 | 304ms | ✓ |
| radare2 | gcc -O2 | 0.009 | #2 | 0 | 0 | 278ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `binary_search`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.051 | #1 | 6 | 2 | 4066ms | ✓ |
| fission | gcc -O2 | 0.056 | #1 | 6 | 2 | 2221ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.006 | #2 | 0 | 0 | 321ms | ✓ |
| radare2 | gcc -O2 | 0.009 | #2 | 0 | 0 | 287ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `bubble_sort`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.008 | #1 | 4 | 2 | 3318ms | ✓ |
| fission | gcc -O2 | 0.105 | #1 | 4 | 3 | 3069ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.006 | #2 | 0 | 0 | 307ms | ✓ |
| radare2 | gcc -O2 | 0.007 | #2 | 0 | 0 | 292ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `checksum`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.103 | #1 | 2 | 2 | 2277ms | ✓ |
| fission | gcc -O2 | 0.170 | #1 | 0 | 3 | 1673ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.012 | #2 | 0 | 0 | 296ms | ✓ |
| radare2 | gcc -O2 | 0.012 | #2 | 0 | 0 | 291ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `clamp`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.179 | #1 | 0 | 2 | 1614ms | ✓ |
| fission | gcc -O2 | 0.535 | #1 | 0 | 1 | 1481ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.005 | #2 | 0 | 0 | 289ms | ✓ |
| radare2 | gcc -O2 | 0.006 | #2 | 0 | 0 | 307ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `classify_range`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.093 | #1 | 9 | 2 | 2104ms | ✓ |
| fission | gcc -O2 | 0.513 | #1 | 0 | 3 | 1525ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.008 | #2 | 0 | 0 | 284ms | ✓ |
| radare2 | gcc -O2 | 0.009 | #2 | 0 | 0 | 280ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `count_bits`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.118 | #1 | 1 | 2 | 6074ms | ✓ |
| fission | gcc -O2 | 0.133 | #1 | 0 | 3 | 1769ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.009 | #2 | 0 | 0 | 292ms | ✓ |
| radare2 | gcc -O2 | 0.008 | #2 | 0 | 0 | 294ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `factorial`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.035 | #1 | 0 | 3 | 2056ms | ✓ |
| fission | gcc -O2 | 0.244 | #1 | 1 | 2 | 1688ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.004 | #2 | 0 | 0 | 292ms | ✓ |
| radare2 | gcc -O2 | 0.003 | #2 | 0 | 0 | 294ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `fibonacci`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.044 | #1 | 0 | 3 | 2193ms | ✓ |
| fission | gcc -O2 | 0.172 | #1 | 1 | 3 | 2378ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.004 | #2 | 0 | 0 | 301ms | ✓ |
| radare2 | gcc -O2 | 0.004 | #2 | 0 | 0 | 308ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `fibonacci_iter`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.173 | #1 | 4 | 2 | 2048ms | ✓ |
| fission | gcc -O2 | 0.245 | #1 | 0 | 2 | 1744ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.007 | #2 | 0 | 0 | 302ms | ✓ |
| radare2 | gcc -O2 | 0.008 | #2 | 0 | 0 | 288ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `find_pair_value`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.095 | #1 | 3 | 2 | 2009ms | ✓ |
| fission | gcc -O2 | 0.165 | #1 | 3 | 4 | 1682ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.005 | #2 | 0 | 0 | 280ms | ✓ |
| radare2 | gcc -O2 | 0.005 | #2 | 0 | 0 | 282ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `gcd`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.081 | #1 | 1 | 2 | 1918ms | ✓ |
| fission | gcc -O2 | 0.107 | #1 | 0 | 2 | 1955ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.004 | #2 | 0 | 0 | 315ms | ✓ |
| radare2 | gcc -O2 | 0.004 | #2 | 0 | 0 | 294ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `linear_search`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.124 | #1 | 3 | 2 | 2008ms | ✓ |
| fission | gcc -O2 | 0.154 | #1 | 3 | 4 | 1660ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.005 | #2 | 0 | 0 | 309ms | ✓ |
| radare2 | gcc -O2 | 0.005 | #2 | 0 | 0 | 301ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `max`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.365 | #1 | 0 | 1 | 1561ms | ✓ |
| fission | gcc -O2 | 0.579 | #1 | 0 | 1 | 1469ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.002 | #2 | 0 | 0 | 310ms | ✓ |
| radare2 | gcc -O2 | 0.002 | #2 | 0 | 0 | 299ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `pointer_stride_sum`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.135 | #1 | 1 | 2 | 1750ms | ✓ |
| fission | gcc -O2 | 0.319 | #1 | 0 | 3 | 1823ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.005 | #2 | 0 | 0 | 305ms | ✓ |
| radare2 | gcc -O2 | 0.006 | #2 | 0 | 0 | 298ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `power`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.076 | #1 | 1 | 2 | 2013ms | ✓ |
| fission | gcc -O2 | 0.081 | #1 | 2 | 5 | 1667ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.008 | #2 | 0 | 0 | 299ms | ✓ |
| radare2 | gcc -O2 | 0.008 | #2 | 0 | 0 | 298ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `process_code`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.068 | #1 | 4 | 3 | 1943ms | ✓ |
| fission | gcc -O2 | 0.331 | #1 | 0 | 1 | 1627ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.005 | #2 | 0 | 0 | 337ms | ✓ |
| radare2 | gcc -O2 | 0.006 | #2 | 0 | 0 | 318ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `reverse_in_place`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.111 | #1 | 2 | 2 | 2797ms | ✓ |
| fission | gcc -O2 | 0.151 | #1 | 2 | 2 | 1936ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.006 | #2 | 0 | 0 | 305ms | ✓ |
| radare2 | gcc -O2 | 0.006 | #2 | 0 | 0 | 299ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `saturating_add`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.061 | #1 | 2 | 3 | 2106ms | ✓ |
| fission | gcc -O2 | 0.294 | #1 | 1 | 2 | 1715ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.011 | #2 | 0 | 0 | 285ms | ✓ |
| radare2 | gcc -O2 | 0.012 | #2 | 0 | 0 | 279ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `signum`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.057 | #1 | 0 | 3 | 1509ms | ✓ |
| fission | gcc -O2 | 0.489 | #1 | 0 | 1 | 1454ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.004 | #2 | 0 | 0 | 284ms | ✓ |
| radare2 | gcc -O2 | 0.003 | #2 | 0 | 0 | 293ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

### `sum_array`
| Decompiler | Variant | Similarity | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.105 | #1 | 1 | 2 | 1855ms | ✓ |
| fission | gcc -O2 | 0.357 | #1 | 0 | 3 | 1661ms | ✓ |
| ghidra | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| ghidra | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| radare2 | gcc -O0 | 0.008 | #2 | 0 | 0 | 288ms | ✓ |
| radare2 | gcc -O2 | 0.008 | #2 | 0 | 0 | 286ms | ✓ |
| retdec | gcc -O0 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| retdec | gcc -O2 | 0.000 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |

---

## Overfitting Analysis

Functions where **all** decompilers scored below 0.3 are marked as objectively hard.
Functions where **only Fission** scored below 0.3 are marked as quality gaps.

**Objectively hard functions (14):** `count_bits`, `checksum`, `saturating_add`, `reverse_in_place`, `find_pair_value`, `accumulate_pairs`, `fibonacci`, `fibonacci_iter`, `bubble_sort`, `linear_search`, `binary_search`, `factorial`, `gcd`, `power`