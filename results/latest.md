# Fission Benchmark Report

**Generated:** 2026-07-01 18:52 UTC  
**Corpus:** `dev`  
**Functions evaluated:** 21

---

## Summary — Average Source Similarity

| Decompiler | Avg Similarity | Semantic Pass | Functions |
| ---|---|---|--- |
| **ghidra** | 0.427 | 70.2% | 84 |
| **angr** | 0.401 | 59.5% | 84 |
| **fission** | 0.163 | 8.3% | 84 |
| **boomerang** | 0.019 | 0.0% | 84 |
| **radare2** | 0.005 | 0.0% | 84 |
| **snowman** | 0.001 | 0.0% | 84 |
| **revng** | 0.001 | 0.0% | 64 |

---

## Per-Function Results

### `accumulate_pairs`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.331 | 1 | #2 | 0 | 2 | 414ms | ✓ |
| angr | gcc-m32 -O0 | 0.320 | 0 | #2 | 0 | 2 | 342ms | ✓ |
| angr | gcc -O2 | 0.160 | 0 | #1 | 0 | 2 | 338ms | ✓ |
| angr | gcc-m32 -O2 | 0.121 | 0 | #2 | 0 | 2 | 377ms | ✓ |
| boomerang | gcc -O0 | 0.026 | 0 | #4 | 2 | 2 | 17ms | ✓ |
| boomerang | gcc-m32 -O0 | 0.002 | 0 | #5 | 8 | 8 | 484ms | ✓ |
| boomerang | gcc -O2 | 0.026 | 0 | #4 | 2 | 2 | 20ms | ✓ |
| boomerang | gcc-m32 -O2 | 0.002 | 0 | #5 | 8 | 8 | 478ms | ✓ |
| fission | gcc -O0 | 0.128 | 0 | #3 | 2 | 2 | 1693ms | ✓ |
| fission | gcc-m32 -O0 | 0.091 | 0 | #3 | 1 | 2 | 1319ms | ✓ |
| fission | gcc -O2 | 0.139 | 1 | #2 | 2 | 2 | 1444ms | ✓ |
| fission | gcc-m32 -O2 | 0.162 | 0 | #1 | 0 | 3 | 1140ms | ✓ |
| ghidra | gcc -O0 | 0.517 | 0 | #1 | 0 | 2 | 4243ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.787 | 1 | #1 | 0 | 2 | 3388ms | ✓ |
| ghidra | gcc -O2 | 0.120 | 1 | #3 | 0 | 3 | 4165ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.120 | 1 | #3 | 0 | 3 | 3966ms | ✓ |
| radare2 | gcc -O0 | 0.009 | 0 | #5 | 0 | 0 | 87ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.005 | 0 | #4 | 0 | 0 | 74ms | ✓ |
| radare2 | gcc -O2 | 0.009 | 0 | #5 | 0 | 0 | 90ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.005 | 0 | #4 | 0 | 0 | 75ms | ✓ |
| revng | gcc -O0 | 0.001 | 0 | #6 | 0 | 10 | 42627ms | ✓ |
| revng | gcc-m32 -O0 | 0.001 | 0 | #7 | 0 | 8 | 15272ms | ✓ |
| revng | gcc -O2 | 0.001 | 0 | #7 | 0 | 10 | 45806ms | ✓ |
| revng | gcc-m32 -O2 | 0.001 | 0 | #7 | 0 | 8 | 17967ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #7 | 222 | 7 | 553ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #6 | 155 | 7 | 457ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #6 | 220 | 7 | 498ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #6 | 151 | 7 | 527ms | ✓ |

### `binary_search`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.335 | 1 | #1 | 0 | 2 | 351ms | ✓ |
| angr | gcc-m32 -O0 | 0.386 | 0 | #2 | 0 | 2 | 308ms | ✓ |
| angr | gcc -O2 | 0.160 | 0 | #2 | 0 | 4 | 317ms | ✓ |
| angr | gcc-m32 -O2 | 0.175 | 0 | #2 | 0 | 4 | 319ms | ✓ |
| boomerang | gcc -O0 | 0.023 | 0 | #4 | 2 | 2 | 6ms | ✓ |
| boomerang | gcc-m32 -O0 | 0.003 | 0 | #5 | 8 | 8 | 247ms | ✓ |
| boomerang | gcc -O2 | 0.023 | 0 | #4 | 2 | 2 | 9ms | ✓ |
| boomerang | gcc-m32 -O2 | 0.003 | 0 | #5 | 8 | 8 | 242ms | ✓ |
| fission | gcc -O0 | 0.062 | 0 | #3 | 6 | 2 | 1493ms | ✓ |
| fission | gcc-m32 -O0 | 0.045 | 0 | #3 | 6 | 2 | 1033ms | ✓ |
| fission | gcc -O2 | 0.056 | 0 | #3 | 6 | 2 | 1214ms | ✓ |
| fission | gcc-m32 -O2 | 0.081 | 0 | #3 | 3 | 4 | 895ms | ✓ |
| ghidra | gcc -O0 | 0.242 | 0 | #2 | 0 | 3 | 2058ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.438 | 1 | #1 | 0 | 3 | 1737ms | ✓ |
| ghidra | gcc -O2 | 0.239 | 1 | #1 | 0 | 5 | 2089ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.239 | 1 | #1 | 0 | 5 | 1783ms | ✓ |
| radare2 | gcc -O0 | 0.006 | 0 | #5 | 0 | 0 | 49ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.005 | 0 | #4 | 0 | 0 | 44ms | ✓ |
| radare2 | gcc -O2 | 0.009 | 0 | #5 | 0 | 0 | 49ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.004 | 0 | #4 | 0 | 0 | 43ms | ✓ |
| revng | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 0ms | ❌ Batch decompile error:  |
| revng | gcc-m32 -O0 | 0.002 | 0 | #6 | 0 | 8 | 15026ms | ✓ |
| revng | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 0ms | ❌ Batch decompile error:  |
| revng | gcc-m32 -O2 | 0.001 | 0 | #7 | 0 | 8 | 13506ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #6 | 224 | 7 | 593ms | ✓ |
| snowman | gcc-m32 -O0 | 0.002 | 0 | #7 | 157 | 7 | 471ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #6 | 223 | 7 | 534ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #6 | 154 | 7 | 505ms | ✓ |

### `bubble_sort`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.295 | 1 | #1 | 0 | 4 | 351ms | ✓ |
| angr | gcc-m32 -O0 | 0.257 | 0 | #1 | 0 | 4 | 308ms | ✓ |
| angr | gcc -O2 | 0.107 | 0 | #2 | 0 | 4 | 317ms | ✓ |
| angr | gcc-m32 -O2 | 0.069 | 0 | #2 | 0 | 5 | 319ms | ✓ |
| boomerang | gcc -O0 | 0.037 | 0 | #3 | 2 | 2 | 6ms | ✓ |
| boomerang | gcc-m32 -O0 | 0.003 | 0 | #5 | 8 | 8 | 247ms | ✓ |
| boomerang | gcc -O2 | 0.037 | 0 | #4 | 2 | 2 | 9ms | ✓ |
| boomerang | gcc-m32 -O2 | 0.003 | 0 | #5 | 8 | 8 | 242ms | ✓ |
| fission | gcc -O0 | 0.008 | 0 | #4 | 4 | 2 | 1493ms | ✓ |
| fission | gcc-m32 -O0 | 0.048 | 0 | #3 | 4 | 3 | 1033ms | ✓ |
| fission | gcc -O2 | 0.105 | 0 | #3 | 4 | 3 | 1214ms | ✓ |
| fission | gcc-m32 -O2 | 0.038 | 0 | #3 | 2 | 4 | 895ms | ✓ |
| ghidra | gcc -O0 | 0.167 | 0 | #2 | 0 | 4 | 2058ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.152 | 1 | #2 | 0 | 4 | 1737ms | ✓ |
| ghidra | gcc -O2 | 0.131 | 0 | #1 | 0 | 5 | 2089ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.190 | 1 | #1 | 0 | 5 | 1783ms | ✓ |
| radare2 | gcc -O0 | 0.006 | 0 | #5 | 0 | 0 | 49ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.004 | 0 | #4 | 0 | 0 | 44ms | ✓ |
| radare2 | gcc -O2 | 0.007 | 0 | #5 | 0 | 0 | 49ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.006 | 0 | #4 | 0 | 0 | 43ms | ✓ |
| revng | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 0ms | ❌ Batch decompile error:  |
| revng | gcc-m32 -O0 | 0.002 | 0 | #6 | 0 | 8 | 15026ms | ✓ |
| revng | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 0ms | ❌ Batch decompile error:  |
| revng | gcc-m32 -O2 | 0.001 | 0 | #7 | 0 | 8 | 13506ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #6 | 224 | 7 | 593ms | ✓ |
| snowman | gcc-m32 -O0 | 0.002 | 0 | #7 | 157 | 7 | 471ms | ✓ |
| snowman | gcc -O2 | 0.002 | 0 | #6 | 223 | 7 | 534ms | ✓ |
| snowman | gcc-m32 -O2 | 0.002 | 0 | #6 | 154 | 7 | 505ms | ✓ |

### `checksum`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.567 | 1 | #2 | 0 | 2 | 399ms | ✓ |
| angr | gcc-m32 -O0 | 0.598 | 0 | #2 | 0 | 2 | 328ms | ✓ |
| angr | gcc -O2 | 0.125 | 1 | #2 | 0 | 2 | 333ms | ✓ |
| angr | gcc-m32 -O2 | 0.095 | 1 | #3 | 0 | 2 | 304ms | ✓ |
| boomerang | gcc -O0 | 0.026 | 0 | #4 | 2 | 2 | 45ms | ✓ |
| boomerang | gcc-m32 -O0 | 0.003 | 0 | #5 | 8 | 8 | 399ms | ✓ |
| boomerang | gcc -O2 | 0.026 | 0 | #4 | 2 | 2 | 15ms | ✓ |
| boomerang | gcc-m32 -O2 | 0.004 | 0 | #5 | 8 | 8 | 395ms | ✓ |
| fission | gcc -O0 | 0.103 | 0 | #3 | 2 | 2 | 5077ms | ✓ |
| fission | gcc-m32 -O0 | 0.132 | 0 | #3 | 2 | 2 | 3294ms | ✓ |
| fission | gcc -O2 | 0.125 | 1 | #3 | 1 | 3 | 1399ms | ✓ |
| fission | gcc-m32 -O2 | 0.122 | 0 | #1 | 0 | 3 | 1037ms | ✓ |
| ghidra | gcc -O0 | 0.668 | 0 | #1 | 0 | 2 | 5578ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.819 | 1 | #1 | 0 | 2 | 3874ms | ✓ |
| ghidra | gcc -O2 | 0.129 | 1 | #1 | 0 | 3 | 3833ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.116 | 1 | #2 | 0 | 3 | 2692ms | ✓ |
| radare2 | gcc -O0 | 0.012 | 0 | #5 | 0 | 0 | 106ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.011 | 0 | #4 | 0 | 0 | 75ms | ✓ |
| radare2 | gcc -O2 | 0.012 | 0 | #5 | 0 | 0 | 91ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.010 | 0 | #4 | 0 | 0 | 61ms | ✓ |
| revng | gcc -O0 | 0.001 | 0 | #7 | 0 | 10 | 42220ms | ✓ |
| revng | gcc-m32 -O0 | 0.001 | 0 | #6 | 0 | 8 | 15082ms | ✓ |
| revng | gcc -O2 | 0.001 | 0 | #7 | 0 | 10 | 45560ms | ✓ |
| revng | gcc-m32 -O2 | 0.001 | 0 | #7 | 0 | 8 | 16853ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #6 | 227 | 7 | 473ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #7 | 161 | 7 | 496ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #6 | 219 | 7 | 520ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #6 | 151 | 7 | 488ms | ✓ |

### `clamp`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.708 | 1 | #1 | 0 | 2 | 399ms | ✓ |
| angr | gcc-m32 -O0 | 0.705 | 1 | #1 | 0 | 2 | 328ms | ✓ |
| angr | gcc -O2 | 0.524 | 1 | #3 | 0 | 1 | 333ms | ✓ |
| angr | gcc-m32 -O2 | 0.490 | 1 | #2 | 0 | 1 | 304ms | ✓ |
| boomerang | gcc -O0 | 0.035 | 0 | #4 | 2 | 2 | 45ms | ✓ |
| boomerang | gcc-m32 -O0 | 0.003 | 0 | #5 | 8 | 8 | 399ms | ✓ |
| boomerang | gcc -O2 | 0.035 | 0 | #4 | 2 | 2 | 15ms | ✓ |
| boomerang | gcc-m32 -O2 | 0.003 | 0 | #5 | 8 | 8 | 395ms | ✓ |
| fission | gcc -O0 | 0.414 | 0 | #3 | 0 | 1 | 5077ms | ✓ |
| fission | gcc-m32 -O0 | 0.450 | 0 | #3 | 0 | 1 | 3294ms | ✓ |
| fission | gcc -O2 | 0.535 | 0 | #2 | 0 | 1 | 1399ms | ✓ |
| fission | gcc-m32 -O2 | 0.368 | 0 | #3 | 0 | 1 | 1037ms | ✓ |
| ghidra | gcc -O0 | 0.421 | 0 | #2 | 0 | 2 | 5578ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.590 | 1 | #2 | 0 | 2 | 3874ms | ✓ |
| ghidra | gcc -O2 | 0.582 | 1 | #1 | 0 | 2 | 3833ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.731 | 1 | #1 | 0 | 2 | 2692ms | ✓ |
| radare2 | gcc -O0 | 0.005 | 0 | #5 | 0 | 0 | 106ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.005 | 0 | #4 | 0 | 0 | 75ms | ✓ |
| radare2 | gcc -O2 | 0.006 | 0 | #5 | 0 | 0 | 91ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.005 | 0 | #4 | 0 | 0 | 61ms | ✓ |
| revng | gcc -O0 | 0.001 | 0 | #7 | 0 | 10 | 42220ms | ✓ |
| revng | gcc-m32 -O0 | 0.001 | 0 | #6 | 0 | 8 | 15082ms | ✓ |
| revng | gcc -O2 | 0.001 | 0 | #7 | 0 | 10 | 45560ms | ✓ |
| revng | gcc-m32 -O2 | 0.001 | 0 | #6 | 0 | 8 | 16853ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #6 | 227 | 7 | 473ms | ✓ |
| snowman | gcc-m32 -O0 | 0.000 | 0 | #7 | 161 | 7 | 496ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #6 | 219 | 7 | 520ms | ✓ |
| snowman | gcc-m32 -O2 | 0.000 | 0 | #7 | 151 | 7 | 488ms | ✓ |

### `classify_range`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.182 | 1 | #1 | 0 | 2 | 399ms | ✓ |
| angr | gcc-m32 -O0 | 0.157 | 1 | #2 | 0 | 2 | 328ms | ✓ |
| angr | gcc -O2 | 0.541 | 0 | #1 | 0 | 2 | 333ms | ✓ |
| angr | gcc-m32 -O2 | 0.401 | 0 | #3 | 0 | 1 | 304ms | ✓ |
| boomerang | gcc -O0 | 0.033 | 0 | #4 | 2 | 2 | 45ms | ✓ |
| boomerang | gcc-m32 -O0 | 0.003 | 0 | #5 | 8 | 8 | 399ms | ✓ |
| boomerang | gcc -O2 | 0.033 | 0 | #4 | 2 | 2 | 15ms | ✓ |
| boomerang | gcc-m32 -O2 | 0.003 | 0 | #5 | 8 | 8 | 395ms | ✓ |
| fission | gcc -O0 | 0.093 | 0 | #3 | 9 | 2 | 5077ms | ✓ |
| fission | gcc-m32 -O0 | 0.060 | 0 | #3 | 8 | 2 | 3294ms | ✓ |
| fission | gcc -O2 | 0.513 | 0 | #2 | 0 | 3 | 1399ms | ✓ |
| fission | gcc-m32 -O2 | 0.433 | 0 | #2 | 0 | 3 | 1037ms | ✓ |
| ghidra | gcc -O0 | 0.167 | 0 | #2 | 0 | 3 | 5578ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.174 | 1 | #1 | 0 | 3 | 3874ms | ✓ |
| ghidra | gcc -O2 | 0.486 | 1 | #3 | 0 | 3 | 3833ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.486 | 1 | #1 | 0 | 3 | 2692ms | ✓ |
| radare2 | gcc -O0 | 0.008 | 0 | #5 | 0 | 0 | 106ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.003 | 0 | #4 | 0 | 0 | 75ms | ✓ |
| radare2 | gcc -O2 | 0.009 | 0 | #5 | 0 | 0 | 91ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.003 | 0 | #4 | 0 | 0 | 61ms | ✓ |
| revng | gcc -O0 | 0.001 | 0 | #7 | 0 | 10 | 42220ms | ✓ |
| revng | gcc-m32 -O0 | 0.001 | 0 | #6 | 0 | 8 | 15082ms | ✓ |
| revng | gcc -O2 | 0.001 | 0 | #6 | 0 | 10 | 45560ms | ✓ |
| revng | gcc-m32 -O2 | 0.001 | 0 | #7 | 0 | 8 | 16853ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #6 | 227 | 7 | 473ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #7 | 161 | 7 | 496ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #7 | 219 | 7 | 520ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #6 | 151 | 7 | 488ms | ✓ |

### `count_bits`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.609 | 1 | #2 | 0 | 2 | 399ms | ✓ |
| angr | gcc-m32 -O0 | 0.655 | 1 | #2 | 0 | 2 | 328ms | ✓ |
| angr | gcc -O2 | 0.494 | 0 | #2 | 0 | 3 | 333ms | ✓ |
| angr | gcc-m32 -O2 | 0.261 | 0 | #2 | 0 | 2 | 304ms | ✓ |
| boomerang | gcc -O0 | 0.088 | 0 | #4 | 2 | 2 | 45ms | ✓ |
| boomerang | gcc-m32 -O0 | 0.002 | 0 | #5 | 8 | 8 | 399ms | ✓ |
| boomerang | gcc -O2 | 0.088 | 0 | #4 | 2 | 2 | 15ms | ✓ |
| boomerang | gcc-m32 -O2 | 0.002 | 0 | #5 | 8 | 8 | 395ms | ✓ |
| fission | gcc -O0 | 0.135 | 0 | #3 | 2 | 2 | 5077ms | ✓ |
| fission | gcc-m32 -O0 | 0.102 | 0 | #3 | 1 | 2 | 3294ms | ✓ |
| fission | gcc -O2 | 0.104 | 1 | #3 | 1 | 3 | 1399ms | ✓ |
| fission | gcc-m32 -O2 | 0.123 | 0 | #3 | 0 | 3 | 1037ms | ✓ |
| ghidra | gcc -O0 | 0.688 | 0 | #1 | 0 | 2 | 5578ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.755 | 1 | #1 | 0 | 2 | 3874ms | ✓ |
| ghidra | gcc -O2 | 0.609 | 1 | #1 | 0 | 2 | 3833ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.609 | 1 | #1 | 0 | 2 | 2692ms | ✓ |
| radare2 | gcc -O0 | 0.009 | 0 | #5 | 0 | 0 | 106ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.007 | 0 | #4 | 0 | 0 | 75ms | ✓ |
| radare2 | gcc -O2 | 0.008 | 0 | #5 | 0 | 0 | 91ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.006 | 0 | #4 | 0 | 0 | 61ms | ✓ |
| revng | gcc -O0 | 0.001 | 0 | #7 | 0 | 10 | 42220ms | ✓ |
| revng | gcc-m32 -O0 | 0.001 | 0 | #6 | 0 | 8 | 15082ms | ✓ |
| revng | gcc -O2 | 0.001 | 0 | #7 | 0 | 10 | 45560ms | ✓ |
| revng | gcc-m32 -O2 | 0.001 | 0 | #7 | 0 | 8 | 16853ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #6 | 227 | 7 | 473ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #7 | 161 | 7 | 496ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #6 | 219 | 7 | 520ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #6 | 151 | 7 | 488ms | ✓ |

### `factorial`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.702 | 1 | #1 | 0 | 1 | 351ms | ✓ |
| angr | gcc-m32 -O0 | 0.548 | 0 | #2 | 0 | 1 | 308ms | ✓ |
| angr | gcc -O2 | 0.239 | 0 | #1 | 0 | 2 | 317ms | ✓ |
| angr | gcc-m32 -O2 | 0.135 | 1 | #2 | 0 | 2 | 319ms | ✓ |
| boomerang | gcc -O0 | 0.048 | 0 | #3 | 2 | 2 | 6ms | ✓ |
| boomerang | gcc-m32 -O0 | 0.002 | 0 | #4 | 8 | 8 | 247ms | ✓ |
| boomerang | gcc -O2 | 0.048 | 0 | #4 | 2 | 2 | 9ms | ✓ |
| boomerang | gcc-m32 -O2 | 0.002 | 0 | #4 | 8 | 8 | 242ms | ✓ |
| fission | gcc -O0 | 0.033 | 0 | #4 | 2 | 2 | 1493ms | ✓ |
| fission | gcc-m32 -O0 | 0.050 | 0 | #3 | 0 | 3 | 1033ms | ✓ |
| fission | gcc -O2 | 0.183 | 0 | #3 | 3 | 2 | 1214ms | ✓ |
| fission | gcc-m32 -O2 | 0.021 | 0 | #3 | 1 | 3 | 895ms | ✓ |
| ghidra | gcc -O0 | 0.335 | 0 | #2 | 0 | 2 | 2058ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.579 | 1 | #1 | 0 | 2 | 1737ms | ✓ |
| ghidra | gcc -O2 | 0.212 | 1 | #2 | 0 | 3 | 2089ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.136 | 0 | #1 | 0 | 3 | 1783ms | ✓ |
| radare2 | gcc -O0 | 0.004 | 0 | #5 | 0 | 0 | 49ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.001 | 0 | #5 | 0 | 0 | 44ms | ✓ |
| radare2 | gcc -O2 | 0.003 | 0 | #5 | 0 | 0 | 49ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.001 | 0 | #5 | 0 | 0 | 43ms | ✓ |
| revng | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 0ms | ❌ Batch decompile error:  |
| revng | gcc-m32 -O0 | 0.001 | 0 | #7 | 0 | 8 | 15026ms | ✓ |
| revng | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 0ms | ❌ Batch decompile error:  |
| revng | gcc-m32 -O2 | 0.000 | 0 | #7 | 0 | 8 | 13506ms | ✓ |
| snowman | gcc -O0 | 0.000 | 0 | #6 | 224 | 7 | 593ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #6 | 157 | 7 | 471ms | ✓ |
| snowman | gcc -O2 | 0.000 | 0 | #6 | 223 | 7 | 534ms | ✓ |
| snowman | gcc-m32 -O2 | 0.000 | 0 | #6 | 154 | 7 | 505ms | ✓ |

### `fibonacci`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.597 | 1 | #1 | 0 | 2 | 351ms | ✓ |
| angr | gcc-m32 -O0 | 0.590 | 1 | #2 | 0 | 2 | 308ms | ✓ |
| angr | gcc -O2 | 0.325 | 1 | #1 | 0 | 2 | 317ms | ✓ |
| angr | gcc-m32 -O2 | 0.391 | 1 | #1 | 0 | 2 | 319ms | ✓ |
| boomerang | gcc -O0 | 0.029 | 0 | #4 | 2 | 2 | 6ms | ✓ |
| boomerang | gcc-m32 -O0 | 0.002 | 0 | #5 | 8 | 8 | 247ms | ✓ |
| boomerang | gcc -O2 | 0.029 | 0 | #4 | 2 | 2 | 9ms | ✓ |
| boomerang | gcc-m32 -O2 | 0.002 | 0 | #5 | 8 | 8 | 242ms | ✓ |
| fission | gcc -O0 | 0.038 | 0 | #3 | 2 | 2 | 1493ms | ✓ |
| fission | gcc-m32 -O0 | 0.477 | 0 | #3 | 0 | 3 | 1033ms | ✓ |
| fission | gcc -O2 | 0.172 | 0 | #3 | 1 | 3 | 1214ms | ✓ |
| fission | gcc-m32 -O2 | 0.088 | 0 | #3 | 0 | 3 | 895ms | ✓ |
| ghidra | gcc -O0 | 0.321 | 0 | #2 | 0 | 2 | 2058ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.598 | 1 | #1 | 0 | 2 | 1737ms | ✓ |
| ghidra | gcc -O2 | 0.218 | 1 | #2 | 0 | 3 | 2089ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.260 | 1 | #2 | 0 | 3 | 1783ms | ✓ |
| radare2 | gcc -O0 | 0.004 | 0 | #5 | 0 | 0 | 49ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.004 | 0 | #4 | 0 | 0 | 44ms | ✓ |
| radare2 | gcc -O2 | 0.004 | 0 | #5 | 0 | 0 | 49ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.004 | 0 | #4 | 0 | 0 | 43ms | ✓ |
| revng | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 0ms | ❌ Batch decompile error:  |
| revng | gcc-m32 -O0 | 0.001 | 0 | #7 | 0 | 8 | 15026ms | ✓ |
| revng | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 0ms | ❌ Batch decompile error:  |
| revng | gcc-m32 -O2 | 0.000 | 0 | #7 | 0 | 8 | 13506ms | ✓ |
| snowman | gcc -O0 | 0.000 | 0 | #6 | 224 | 7 | 593ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #6 | 157 | 7 | 471ms | ✓ |
| snowman | gcc -O2 | 0.000 | 0 | #6 | 223 | 7 | 534ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #6 | 154 | 7 | 505ms | ✓ |

### `fibonacci_iter`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.711 | 1 | #1 | 0 | 2 | 351ms | ✓ |
| angr | gcc-m32 -O0 | 0.709 | 1 | #2 | 0 | 2 | 308ms | ✓ |
| angr | gcc -O2 | 0.248 | 0 | #2 | 0 | 2 | 317ms | ✓ |
| angr | gcc-m32 -O2 | 0.262 | 0 | #1 | 0 | 2 | 319ms | ✓ |
| boomerang | gcc -O0 | 0.027 | 0 | #4 | 2 | 2 | 6ms | ✓ |
| boomerang | gcc-m32 -O0 | 0.003 | 0 | #5 | 8 | 8 | 247ms | ✓ |
| boomerang | gcc -O2 | 0.027 | 0 | #4 | 2 | 2 | 9ms | ✓ |
| boomerang | gcc-m32 -O2 | 0.003 | 0 | #5 | 8 | 8 | 242ms | ✓ |
| fission | gcc -O0 | 0.176 | 0 | #3 | 4 | 2 | 1493ms | ✓ |
| fission | gcc-m32 -O0 | 0.156 | 0 | #3 | 2 | 2 | 1033ms | ✓ |
| fission | gcc -O2 | 0.278 | 0 | #1 | 1 | 3 | 1214ms | ✓ |
| fission | gcc-m32 -O2 | 0.217 | 0 | #3 | 0 | 3 | 895ms | ✓ |
| ghidra | gcc -O0 | 0.480 | 0 | #2 | 0 | 3 | 2058ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.718 | 1 | #1 | 0 | 3 | 1737ms | ✓ |
| ghidra | gcc -O2 | 0.241 | 1 | #3 | 0 | 3 | 2089ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.243 | 1 | #2 | 0 | 3 | 1783ms | ✓ |
| radare2 | gcc -O0 | 0.007 | 0 | #5 | 0 | 0 | 49ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.004 | 0 | #4 | 0 | 0 | 44ms | ✓ |
| radare2 | gcc -O2 | 0.008 | 0 | #5 | 0 | 0 | 49ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.003 | 0 | #4 | 0 | 0 | 43ms | ✓ |
| revng | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 0ms | ❌ Batch decompile error:  |
| revng | gcc-m32 -O0 | 0.001 | 0 | #7 | 0 | 8 | 15026ms | ✓ |
| revng | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 0ms | ❌ Batch decompile error:  |
| revng | gcc-m32 -O2 | 0.001 | 0 | #7 | 0 | 8 | 13506ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #6 | 224 | 7 | 593ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #6 | 157 | 7 | 471ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #6 | 223 | 7 | 534ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #6 | 154 | 7 | 505ms | ✓ |

### `find_pair_value`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.289 | 1 | #2 | 0 | 2 | 414ms | ✓ |
| angr | gcc-m32 -O0 | 0.277 | 0 | #2 | 0 | 2 | 342ms | ✓ |
| angr | gcc -O2 | 0.215 | 1 | #1 | 0 | 2 | 338ms | ✓ |
| angr | gcc-m32 -O2 | 0.165 | 1 | #2 | 0 | 2 | 377ms | ✓ |
| boomerang | gcc -O0 | 0.029 | 0 | #4 | 2 | 2 | 17ms | ✓ |
| boomerang | gcc-m32 -O0 | 0.003 | 0 | #5 | 8 | 8 | 484ms | ✓ |
| boomerang | gcc -O2 | 0.029 | 0 | #4 | 2 | 2 | 20ms | ✓ |
| boomerang | gcc-m32 -O2 | 0.003 | 0 | #5 | 8 | 8 | 478ms | ✓ |
| fission | gcc -O0 | 0.097 | 0 | #3 | 4 | 2 | 1693ms | ✓ |
| fission | gcc-m32 -O0 | 0.099 | 0 | #3 | 3 | 2 | 1319ms | ✓ |
| fission | gcc -O2 | 0.168 | 1 | #3 | 4 | 2 | 1444ms | ✓ |
| fission | gcc-m32 -O2 | 0.099 | 0 | #3 | 3 | 4 | 1140ms | ✓ |
| ghidra | gcc -O0 | 0.342 | 0 | #1 | 0 | 3 | 4243ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.695 | 1 | #1 | 0 | 3 | 3388ms | ✓ |
| ghidra | gcc -O2 | 0.212 | 1 | #2 | 0 | 4 | 4165ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.212 | 1 | #1 | 0 | 4 | 3966ms | ✓ |
| radare2 | gcc -O0 | 0.005 | 0 | #5 | 0 | 0 | 87ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.005 | 0 | #4 | 0 | 0 | 74ms | ✓ |
| radare2 | gcc -O2 | 0.005 | 0 | #5 | 0 | 0 | 90ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.004 | 0 | #4 | 0 | 0 | 75ms | ✓ |
| revng | gcc -O0 | 0.001 | 0 | #6 | 0 | 10 | 42627ms | ✓ |
| revng | gcc-m32 -O0 | 0.001 | 0 | #7 | 0 | 8 | 15272ms | ✓ |
| revng | gcc -O2 | 0.001 | 0 | #7 | 0 | 10 | 45806ms | ✓ |
| revng | gcc-m32 -O2 | 0.001 | 0 | #7 | 0 | 8 | 17967ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #7 | 222 | 7 | 553ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #6 | 155 | 7 | 457ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #6 | 220 | 7 | 498ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #6 | 151 | 7 | 527ms | ✓ |

### `gcd`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.467 | 1 | #2 | 0 | 2 | 351ms | ✓ |
| angr | gcc-m32 -O0 | 0.488 | 1 | #2 | 0 | 2 | 308ms | ✓ |
| angr | gcc -O2 | 0.467 | 0 | #2 | 0 | 3 | 317ms | ✓ |
| angr | gcc-m32 -O2 | 0.388 | 1 | #2 | 0 | 2 | 319ms | ✓ |
| boomerang | gcc -O0 | 0.082 | 0 | #3 | 2 | 2 | 6ms | ✓ |
| boomerang | gcc-m32 -O0 | 0.002 | 0 | #5 | 8 | 8 | 247ms | ✓ |
| boomerang | gcc -O2 | 0.082 | 0 | #4 | 2 | 2 | 9ms | ✓ |
| boomerang | gcc-m32 -O2 | 0.002 | 0 | #5 | 8 | 8 | 242ms | ✓ |
| fission | gcc -O0 | 0.077 | 1 | #4 | 2 | 2 | 1493ms | ✓ |
| fission | gcc-m32 -O0 | 0.068 | 0 | #3 | 1 | 2 | 1033ms | ✓ |
| fission | gcc -O2 | 0.129 | 0 | #3 | 2 | 2 | 1214ms | ✓ |
| fission | gcc-m32 -O2 | 0.153 | 0 | #3 | 0 | 3 | 895ms | ✓ |
| ghidra | gcc -O0 | 0.596 | 0 | #1 | 0 | 2 | 2058ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.749 | 1 | #1 | 0 | 2 | 1737ms | ✓ |
| ghidra | gcc -O2 | 0.778 | 1 | #1 | 0 | 2 | 2089ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.514 | 1 | #1 | 0 | 3 | 1783ms | ✓ |
| radare2 | gcc -O0 | 0.004 | 0 | #5 | 0 | 0 | 49ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.003 | 0 | #4 | 0 | 0 | 44ms | ✓ |
| radare2 | gcc -O2 | 0.004 | 0 | #5 | 0 | 0 | 49ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.002 | 0 | #4 | 0 | 0 | 43ms | ✓ |
| revng | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 0ms | ❌ Batch decompile error:  |
| revng | gcc-m32 -O0 | 0.001 | 0 | #6 | 0 | 8 | 15026ms | ✓ |
| revng | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 0ms | ❌ Batch decompile error:  |
| revng | gcc-m32 -O2 | 0.001 | 0 | #7 | 0 | 8 | 13506ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #6 | 224 | 7 | 593ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #7 | 157 | 7 | 471ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #6 | 223 | 7 | 534ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #6 | 154 | 7 | 505ms | ✓ |

### `linear_search`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.707 | 1 | #1 | 0 | 2 | 351ms | ✓ |
| angr | gcc-m32 -O0 | 0.714 | 0 | #1 | 0 | 2 | 308ms | ✓ |
| angr | gcc -O2 | 0.200 | 0 | #2 | 0 | 2 | 317ms | ✓ |
| angr | gcc-m32 -O2 | 0.497 | 0 | #2 | 0 | 2 | 319ms | ✓ |
| boomerang | gcc -O0 | 0.028 | 0 | #4 | 2 | 2 | 6ms | ✓ |
| boomerang | gcc-m32 -O0 | 0.002 | 0 | #4 | 8 | 8 | 247ms | ✓ |
| boomerang | gcc -O2 | 0.028 | 0 | #4 | 2 | 2 | 9ms | ✓ |
| boomerang | gcc-m32 -O2 | 0.002 | 0 | #4 | 8 | 8 | 242ms | ✓ |
| fission | gcc -O0 | 0.135 | 0 | #3 | 4 | 2 | 1493ms | ✓ |
| fission | gcc-m32 -O0 | 0.114 | 0 | #3 | 3 | 2 | 1033ms | ✓ |
| fission | gcc -O2 | 0.196 | 0 | #3 | 4 | 2 | 1214ms | ✓ |
| fission | gcc-m32 -O2 | 0.080 | 0 | #3 | 3 | 4 | 895ms | ✓ |
| ghidra | gcc -O0 | 0.371 | 0 | #2 | 0 | 3 | 2058ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.617 | 1 | #2 | 0 | 3 | 1737ms | ✓ |
| ghidra | gcc -O2 | 0.660 | 1 | #1 | 0 | 4 | 2089ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.688 | 1 | #1 | 0 | 4 | 1783ms | ✓ |
| radare2 | gcc -O0 | 0.005 | 0 | #5 | 0 | 0 | 49ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.002 | 0 | #5 | 0 | 0 | 44ms | ✓ |
| radare2 | gcc -O2 | 0.005 | 0 | #5 | 0 | 0 | 49ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.002 | 0 | #5 | 0 | 0 | 43ms | ✓ |
| revng | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 0ms | ❌ Batch decompile error:  |
| revng | gcc-m32 -O0 | 0.001 | 0 | #7 | 0 | 8 | 15026ms | ✓ |
| revng | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 0ms | ❌ Batch decompile error:  |
| revng | gcc-m32 -O2 | 0.001 | 0 | #7 | 0 | 8 | 13506ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #6 | 224 | 7 | 593ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #6 | 157 | 7 | 471ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #6 | 223 | 7 | 534ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #6 | 154 | 7 | 505ms | ✓ |

### `max`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.752 | 1 | #1 | 0 | 1 | 351ms | ✓ |
| angr | gcc-m32 -O0 | 0.673 | 1 | #1 | 0 | 1 | 308ms | ✓ |
| angr | gcc -O2 | 0.752 | 1 | #1 | 0 | 1 | 317ms | ✓ |
| angr | gcc-m32 -O2 | 0.667 | 1 | #1 | 0 | 1 | 319ms | ✓ |
| boomerang | gcc -O0 | 0.032 | 0 | #4 | 2 | 2 | 6ms | ✓ |
| boomerang | gcc-m32 -O0 | 0.001 | 0 | #5 | 8 | 8 | 247ms | ✓ |
| boomerang | gcc -O2 | 0.032 | 0 | #4 | 2 | 2 | 9ms | ✓ |
| boomerang | gcc-m32 -O2 | 0.001 | 0 | #5 | 8 | 8 | 242ms | ✓ |
| fission | gcc -O0 | 0.365 | 0 | #3 | 0 | 1 | 1493ms | ✓ |
| fission | gcc-m32 -O0 | 0.419 | 0 | #3 | 0 | 1 | 1033ms | ✓ |
| fission | gcc -O2 | 0.579 | 0 | #3 | 0 | 1 | 1214ms | ✓ |
| fission | gcc-m32 -O2 | 0.419 | 0 | #3 | 0 | 1 | 895ms | ✓ |
| ghidra | gcc -O0 | 0.431 | 0 | #2 | 0 | 2 | 2058ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.654 | 1 | #2 | 0 | 2 | 1737ms | ✓ |
| ghidra | gcc -O2 | 0.654 | 1 | #2 | 0 | 2 | 2089ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.660 | 1 | #2 | 0 | 2 | 1783ms | ✓ |
| radare2 | gcc -O0 | 0.002 | 0 | #5 | 0 | 0 | 49ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.001 | 0 | #4 | 0 | 0 | 44ms | ✓ |
| radare2 | gcc -O2 | 0.002 | 0 | #5 | 0 | 0 | 49ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.001 | 0 | #4 | 0 | 0 | 43ms | ✓ |
| revng | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 0ms | ❌ Batch decompile error:  |
| revng | gcc-m32 -O0 | 0.001 | 0 | #7 | 0 | 8 | 15026ms | ✓ |
| revng | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 0ms | ❌ Batch decompile error:  |
| revng | gcc-m32 -O2 | 0.000 | 0 | #7 | 0 | 8 | 13506ms | ✓ |
| snowman | gcc -O0 | 0.000 | 0 | #6 | 224 | 7 | 593ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #6 | 157 | 7 | 471ms | ✓ |
| snowman | gcc -O2 | 0.000 | 0 | #6 | 223 | 7 | 534ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #6 | 154 | 7 | 505ms | ✓ |

### `pointer_stride_sum`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.253 | 1 | #2 | 0 | 2 | 414ms | ✓ |
| angr | gcc-m32 -O0 | 0.511 | 1 | #2 | 0 | 2 | 342ms | ✓ |
| angr | gcc -O2 | 0.325 | 1 | #2 | 0 | 3 | 338ms | ✓ |
| angr | gcc-m32 -O2 | 0.195 | 1 | #3 | 0 | 2 | 377ms | ✓ |
| boomerang | gcc -O0 | 0.026 | 0 | #4 | 2 | 2 | 17ms | ✓ |
| boomerang | gcc-m32 -O0 | 0.002 | 0 | #5 | 8 | 8 | 484ms | ✓ |
| boomerang | gcc -O2 | 0.026 | 0 | #4 | 2 | 2 | 20ms | ✓ |
| boomerang | gcc-m32 -O2 | 0.002 | 0 | #5 | 8 | 8 | 478ms | ✓ |
| fission | gcc -O0 | 0.097 | 0 | #3 | 2 | 2 | 1693ms | ✓ |
| fission | gcc-m32 -O0 | 0.166 | 0 | #3 | 1 | 2 | 1319ms | ✓ |
| fission | gcc -O2 | 0.142 | 1 | #3 | 1 | 3 | 1444ms | ✓ |
| fission | gcc-m32 -O2 | 0.226 | 0 | #2 | 0 | 3 | 1140ms | ✓ |
| ghidra | gcc -O0 | 0.259 | 0 | #1 | 0 | 2 | 4243ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.674 | 1 | #1 | 0 | 2 | 3388ms | ✓ |
| ghidra | gcc -O2 | 0.609 | 1 | #1 | 0 | 2 | 4165ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.648 | 1 | #1 | 0 | 2 | 3966ms | ✓ |
| radare2 | gcc -O0 | 0.005 | 0 | #5 | 0 | 0 | 87ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.004 | 0 | #4 | 0 | 0 | 74ms | ✓ |
| radare2 | gcc -O2 | 0.006 | 0 | #5 | 0 | 0 | 90ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.005 | 0 | #4 | 0 | 0 | 75ms | ✓ |
| revng | gcc -O0 | 0.001 | 0 | #7 | 0 | 10 | 42627ms | ✓ |
| revng | gcc-m32 -O0 | 0.001 | 0 | #7 | 0 | 8 | 15272ms | ✓ |
| revng | gcc -O2 | 0.001 | 0 | #7 | 0 | 10 | 45806ms | ✓ |
| revng | gcc-m32 -O2 | 0.001 | 0 | #7 | 0 | 8 | 17967ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #6 | 222 | 7 | 553ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #6 | 155 | 7 | 457ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #6 | 220 | 7 | 498ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #6 | 151 | 7 | 527ms | ✓ |

### `power`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.283 | 1 | #2 | 0 | 2 | 351ms | ✓ |
| angr | gcc-m32 -O0 | 0.176 | 0 | #2 | 0 | 3 | 308ms | ✓ |
| angr | gcc -O2 | 0.195 | 0 | #2 | 0 | 2 | 317ms | ✓ |
| angr | gcc-m32 -O2 | 0.088 | 0 | #2 | 0 | 3 | 319ms | ✓ |
| boomerang | gcc -O0 | 0.043 | 0 | #4 | 2 | 2 | 6ms | ✓ |
| boomerang | gcc-m32 -O0 | 0.003 | 0 | #5 | 8 | 8 | 247ms | ✓ |
| boomerang | gcc -O2 | 0.043 | 0 | #4 | 2 | 2 | 9ms | ✓ |
| boomerang | gcc-m32 -O2 | 0.003 | 0 | #5 | 8 | 8 | 242ms | ✓ |
| fission | gcc -O0 | 0.077 | 0 | #3 | 2 | 2 | 1493ms | ✓ |
| fission | gcc-m32 -O0 | 0.039 | 0 | #3 | 1 | 2 | 1033ms | ✓ |
| fission | gcc -O2 | 0.081 | 0 | #3 | 2 | 5 | 1214ms | ✓ |
| fission | gcc-m32 -O2 | 0.035 | 0 | #3 | 1 | 5 | 895ms | ✓ |
| ghidra | gcc -O0 | 0.374 | 0 | #1 | 0 | 3 | 2058ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.492 | 0 | #1 | 0 | 3 | 1737ms | ✓ |
| ghidra | gcc -O2 | 0.392 | 1 | #1 | 0 | 4 | 2089ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.249 | 0 | #1 | 0 | 4 | 1783ms | ✓ |
| radare2 | gcc -O0 | 0.008 | 0 | #5 | 0 | 0 | 49ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.004 | 0 | #4 | 0 | 0 | 44ms | ✓ |
| radare2 | gcc -O2 | 0.008 | 0 | #5 | 0 | 0 | 49ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.004 | 0 | #4 | 0 | 0 | 43ms | ✓ |
| revng | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 0ms | ❌ Batch decompile error:  |
| revng | gcc-m32 -O0 | 0.002 | 0 | #6 | 0 | 8 | 15026ms | ✓ |
| revng | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 0ms | ❌ Batch decompile error:  |
| revng | gcc-m32 -O2 | 0.001 | 0 | #7 | 0 | 8 | 13506ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #6 | 224 | 7 | 593ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #7 | 157 | 7 | 471ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #6 | 223 | 7 | 534ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #6 | 154 | 7 | 505ms | ✓ |

### `process_code`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.661 | 1 | #1 | 0 | 1 | 351ms | ✓ |
| angr | gcc-m32 -O0 | 0.660 | 1 | #1 | 0 | 1 | 308ms | ✓ |
| angr | gcc -O2 | 0.247 | 1 | #3 | 0 | 3 | 317ms | ✓ |
| angr | gcc-m32 -O2 | 0.260 | 1 | #2 | 0 | 3 | 319ms | ✓ |
| boomerang | gcc -O0 | 0.025 | 0 | #4 | 2 | 2 | 6ms | ✓ |
| boomerang | gcc-m32 -O0 | 0.004 | 0 | #5 | 8 | 8 | 247ms | ✓ |
| boomerang | gcc -O2 | 0.025 | 0 | #4 | 2 | 2 | 9ms | ✓ |
| boomerang | gcc-m32 -O2 | 0.004 | 0 | #4 | 8 | 8 | 242ms | ✓ |
| fission | gcc -O0 | 0.047 | 0 | #3 | 8 | 2 | 1493ms | ✓ |
| fission | gcc-m32 -O0 | 0.062 | 0 | #3 | 3 | 5 | 1033ms | ✓ |
| fission | gcc -O2 | 0.331 | 0 | #1 | 0 | 1 | 1214ms | ✓ |
| fission | gcc-m32 -O2 | 0.090 | 0 | #3 | 0 | 5 | 895ms | ✓ |
| ghidra | gcc -O0 | 0.157 | 0 | #2 | 0 | 4 | 2058ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.166 | 1 | #2 | 0 | 4 | 1737ms | ✓ |
| ghidra | gcc -O2 | 0.286 | 1 | #2 | 0 | 2 | 2089ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.286 | 1 | #1 | 0 | 2 | 1783ms | ✓ |
| radare2 | gcc -O0 | 0.005 | 0 | #5 | 0 | 0 | 49ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.005 | 0 | #4 | 0 | 0 | 44ms | ✓ |
| radare2 | gcc -O2 | 0.006 | 0 | #5 | 0 | 0 | 49ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.004 | 0 | #5 | 0 | 0 | 43ms | ✓ |
| revng | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 0ms | ❌ Batch decompile error:  |
| revng | gcc-m32 -O0 | 0.001 | 0 | #6 | 0 | 8 | 15026ms | ✓ |
| revng | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 0ms | ❌ Batch decompile error:  |
| revng | gcc-m32 -O2 | 0.001 | 0 | #7 | 0 | 8 | 13506ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #6 | 224 | 7 | 593ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #7 | 157 | 7 | 471ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #6 | 223 | 7 | 534ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #6 | 154 | 7 | 505ms | ✓ |

### `reverse_in_place`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.273 | 0 | #2 | 0 | 2 | 414ms | ✓ |
| angr | gcc-m32 -O0 | 0.222 | 0 | #2 | 0 | 2 | 342ms | ✓ |
| angr | gcc -O2 | 0.164 | 0 | #2 | 0 | 3 | 338ms | ✓ |
| angr | gcc-m32 -O2 | 0.099 | 0 | #3 | 0 | 3 | 377ms | ✓ |
| boomerang | gcc -O0 | 0.028 | 0 | #4 | 2 | 2 | 17ms | ✓ |
| boomerang | gcc-m32 -O0 | 0.003 | 0 | #5 | 8 | 8 | 484ms | ✓ |
| boomerang | gcc -O2 | 0.028 | 0 | #4 | 2 | 2 | 20ms | ✓ |
| boomerang | gcc-m32 -O2 | 0.003 | 0 | #5 | 8 | 8 | 478ms | ✓ |
| fission | gcc -O0 | 0.111 | 0 | #3 | 2 | 2 | 1693ms | ✓ |
| fission | gcc-m32 -O0 | 0.051 | 0 | #3 | 1 | 2 | 1319ms | ✓ |
| fission | gcc -O2 | 0.131 | 0 | #3 | 2 | 3 | 1444ms | ✓ |
| fission | gcc-m32 -O2 | 0.121 | 0 | #2 | 2 | 2 | 1140ms | ✓ |
| ghidra | gcc -O0 | 0.323 | 0 | #1 | 0 | 2 | 4243ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.339 | 1 | #1 | 0 | 2 | 3388ms | ✓ |
| ghidra | gcc -O2 | 0.221 | 1 | #1 | 0 | 3 | 4165ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.221 | 1 | #1 | 0 | 3 | 3966ms | ✓ |
| radare2 | gcc -O0 | 0.006 | 0 | #5 | 0 | 0 | 87ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.006 | 0 | #4 | 0 | 0 | 74ms | ✓ |
| radare2 | gcc -O2 | 0.006 | 0 | #5 | 0 | 0 | 90ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.005 | 0 | #4 | 0 | 0 | 75ms | ✓ |
| revng | gcc -O0 | 0.002 | 0 | #6 | 0 | 10 | 42627ms | ✓ |
| revng | gcc-m32 -O0 | 0.001 | 0 | #7 | 0 | 8 | 15272ms | ✓ |
| revng | gcc -O2 | 0.001 | 0 | #7 | 0 | 10 | 45806ms | ✓ |
| revng | gcc-m32 -O2 | 0.001 | 0 | #7 | 0 | 8 | 17967ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #7 | 222 | 7 | 553ms | ✓ |
| snowman | gcc-m32 -O0 | 0.002 | 0 | #6 | 155 | 7 | 457ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #6 | 220 | 7 | 498ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #6 | 151 | 7 | 527ms | ✓ |

### `saturating_add`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.769 | 1 | #1 | 0 | 1 | 399ms | ✓ |
| angr | gcc-m32 -O0 | 0.766 | 1 | #1 | 0 | 1 | 328ms | ✓ |
| angr | gcc -O2 | 0.311 | 0 | #2 | 0 | 2 | 333ms | ✓ |
| angr | gcc-m32 -O2 | 0.639 | 1 | #1 | 0 | 2 | 304ms | ✓ |
| boomerang | gcc -O0 | 0.026 | 0 | #4 | 2 | 2 | 45ms | ✓ |
| boomerang | gcc-m32 -O0 | 0.004 | 0 | #5 | 8 | 8 | 399ms | ✓ |
| boomerang | gcc -O2 | 0.026 | 0 | #4 | 2 | 2 | 15ms | ✓ |
| boomerang | gcc-m32 -O2 | 0.003 | 0 | #5 | 8 | 8 | 395ms | ✓ |
| fission | gcc -O0 | 0.063 | 0 | #3 | 3 | 2 | 5077ms | ✓ |
| fission | gcc-m32 -O0 | 0.048 | 0 | #3 | 2 | 3 | 3294ms | ✓ |
| fission | gcc -O2 | 0.279 | 0 | #3 | 2 | 2 | 1399ms | ✓ |
| fission | gcc-m32 -O2 | 0.124 | 0 | #3 | 1 | 2 | 1037ms | ✓ |
| ghidra | gcc -O0 | 0.252 | 0 | #2 | 0 | 3 | 5578ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.246 | 1 | #2 | 0 | 3 | 3874ms | ✓ |
| ghidra | gcc -O2 | 0.606 | 1 | #1 | 0 | 2 | 3833ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.606 | 1 | #2 | 0 | 2 | 2692ms | ✓ |
| radare2 | gcc -O0 | 0.011 | 0 | #5 | 0 | 0 | 106ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.006 | 0 | #4 | 0 | 0 | 75ms | ✓ |
| radare2 | gcc -O2 | 0.012 | 0 | #5 | 0 | 0 | 91ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.006 | 0 | #4 | 0 | 0 | 61ms | ✓ |
| revng | gcc -O0 | 0.001 | 0 | #7 | 0 | 10 | 42220ms | ✓ |
| revng | gcc-m32 -O0 | 0.001 | 0 | #6 | 0 | 8 | 15082ms | ✓ |
| revng | gcc -O2 | 0.001 | 0 | #6 | 0 | 10 | 45560ms | ✓ |
| revng | gcc-m32 -O2 | 0.001 | 0 | #7 | 0 | 8 | 16853ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #6 | 227 | 7 | 473ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #7 | 161 | 7 | 496ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #7 | 219 | 7 | 520ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #6 | 151 | 7 | 488ms | ✓ |

### `signum`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.503 | 1 | #1 | 0 | 1 | 399ms | ✓ |
| angr | gcc-m32 -O0 | 0.488 | 1 | #2 | 0 | 1 | 328ms | ✓ |
| angr | gcc -O2 | 0.675 | 0 | #1 | 0 | 1 | 333ms | ✓ |
| angr | gcc-m32 -O2 | 0.595 | 0 | #1 | 0 | 1 | 304ms | ✓ |
| boomerang | gcc -O0 | 0.037 | 0 | #4 | 2 | 2 | 45ms | ✓ |
| boomerang | gcc-m32 -O0 | 0.002 | 0 | #5 | 8 | 8 | 399ms | ✓ |
| boomerang | gcc -O2 | 0.037 | 0 | #4 | 2 | 2 | 15ms | ✓ |
| boomerang | gcc-m32 -O2 | 0.002 | 0 | #5 | 8 | 8 | 395ms | ✓ |
| fission | gcc -O0 | 0.149 | 0 | #3 | 2 | 2 | 5077ms | ✓ |
| fission | gcc-m32 -O0 | 0.321 | 0 | #3 | 0 | 3 | 3294ms | ✓ |
| fission | gcc -O2 | 0.489 | 0 | #3 | 0 | 1 | 1399ms | ✓ |
| fission | gcc-m32 -O2 | 0.094 | 0 | #3 | 0 | 3 | 1037ms | ✓ |
| ghidra | gcc -O0 | 0.375 | 0 | #2 | 0 | 3 | 5578ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.611 | 1 | #1 | 0 | 3 | 3874ms | ✓ |
| ghidra | gcc -O2 | 0.492 | 1 | #2 | 0 | 2 | 3833ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.583 | 1 | #2 | 0 | 2 | 2692ms | ✓ |
| radare2 | gcc -O0 | 0.004 | 0 | #5 | 0 | 0 | 106ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.003 | 0 | #4 | 0 | 0 | 75ms | ✓ |
| radare2 | gcc -O2 | 0.003 | 0 | #5 | 0 | 0 | 91ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.004 | 0 | #4 | 0 | 0 | 61ms | ✓ |
| revng | gcc -O0 | 0.000 | 0 | #7 | 0 | 10 | 42220ms | ✓ |
| revng | gcc-m32 -O0 | 0.000 | 0 | #7 | 0 | 8 | 15082ms | ✓ |
| revng | gcc -O2 | 0.000 | 0 | #7 | 0 | 10 | 45560ms | ✓ |
| revng | gcc-m32 -O2 | 0.000 | 0 | #7 | 0 | 8 | 16853ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #6 | 227 | 7 | 473ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #6 | 161 | 7 | 496ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #6 | 219 | 7 | 520ms | ✓ |
| snowman | gcc-m32 -O2 | 0.000 | 0 | #6 | 151 | 7 | 488ms | ✓ |

### `sum_array`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.455 | 1 | #2 | 0 | 2 | 414ms | ✓ |
| angr | gcc-m32 -O0 | 0.543 | 0 | #2 | 0 | 2 | 342ms | ✓ |
| angr | gcc -O2 | 0.171 | 1 | #1 | 0 | 2 | 338ms | ✓ |
| angr | gcc-m32 -O2 | 0.122 | 1 | #3 | 0 | 2 | 377ms | ✓ |
| boomerang | gcc -O0 | 0.028 | 0 | #4 | 2 | 2 | 17ms | ✓ |
| boomerang | gcc-m32 -O0 | 0.002 | 0 | #5 | 8 | 8 | 484ms | ✓ |
| boomerang | gcc -O2 | 0.028 | 0 | #4 | 2 | 2 | 20ms | ✓ |
| boomerang | gcc-m32 -O2 | 0.002 | 0 | #5 | 8 | 8 | 478ms | ✓ |
| fission | gcc -O0 | 0.145 | 0 | #3 | 2 | 2 | 1693ms | ✓ |
| fission | gcc-m32 -O0 | 0.120 | 0 | #3 | 1 | 2 | 1319ms | ✓ |
| fission | gcc -O2 | 0.085 | 1 | #3 | 1 | 3 | 1444ms | ✓ |
| fission | gcc-m32 -O2 | 0.124 | 0 | #2 | 0 | 3 | 1140ms | ✓ |
| ghidra | gcc -O0 | 0.648 | 0 | #1 | 0 | 2 | 4243ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.833 | 1 | #1 | 0 | 2 | 3388ms | ✓ |
| ghidra | gcc -O2 | 0.171 | 1 | #2 | 0 | 3 | 4165ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.171 | 1 | #1 | 0 | 3 | 3966ms | ✓ |
| radare2 | gcc -O0 | 0.008 | 0 | #5 | 0 | 0 | 87ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.005 | 0 | #4 | 0 | 0 | 74ms | ✓ |
| radare2 | gcc -O2 | 0.008 | 0 | #5 | 0 | 0 | 90ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.005 | 0 | #4 | 0 | 0 | 75ms | ✓ |
| revng | gcc -O0 | 0.001 | 0 | #6 | 0 | 10 | 42627ms | ✓ |
| revng | gcc-m32 -O0 | 0.001 | 0 | #7 | 0 | 8 | 15272ms | ✓ |
| revng | gcc -O2 | 0.001 | 0 | #7 | 0 | 10 | 45806ms | ✓ |
| revng | gcc-m32 -O2 | 0.001 | 0 | #7 | 0 | 8 | 17967ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #7 | 222 | 7 | 553ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #6 | 155 | 7 | 457ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #6 | 220 | 7 | 498ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #6 | 151 | 7 | 527ms | ✓ |

---

## Overfitting Analysis

Functions where **all** decompilers scored below 0.3 are marked as objectively hard.
Functions where **only Fission** scored below 0.3 are marked as quality gaps.

**Objectively hard functions (1):** `bubble_sort`
**Fission quality gaps (14):** `count_bits`, `checksum`, `saturating_add`, `sum_array`, `reverse_in_place`, `find_pair_value`, `accumulate_pairs`, `pointer_stride_sum`, `fibonacci_iter`, `linear_search`, `binary_search`, `factorial`, `gcd`, `power`