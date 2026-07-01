# Fission Benchmark Report

<<<<<<< Updated upstream
**Generated:** 2026-07-01 18:06 UTC  
=======
**Generated:** 2026-07-01 18:18 UTC  
>>>>>>> Stashed changes
**Corpus:** `dev`  
**Functions evaluated:** 3

---

## Summary — Average Source Similarity

| Decompiler | Avg Similarity | Semantic Pass | Functions |
| ---|---|---|--- |
<<<<<<< Updated upstream
| **ghidra** | 0.587 | 75.0% | 12 |
| **fission** | 0.248 | 8.3% | 12 |
=======
| **ghidra** | 0.427 | 70.2% | 84 |
| **angr** | 0.399 | 60.5% | 81 |
| **fission** | 0.164 | 8.3% | 84 |
| **radare2** | 0.005 | 0.0% | 84 |
| **snowman** | 0.001 | 0.0% | 84 |
| **revng** | 0.001 | 0.0% | 75 |
>>>>>>> Stashed changes

---

## Per-Function Results

<<<<<<< Updated upstream
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
=======
### `accumulate_pairs`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.331 | 1 | #2 | 0 | 2 | 3713ms | ✓ |
| angr | gcc-m32 -O0 | 0.320 | 0 | #2 | 0 | 2 | 2141ms | ✓ |
| angr | gcc -O2 | 0.160 | 0 | #1 | 0 | 2 | 1679ms | ✓ |
| angr | gcc-m32 -O2 | 0.121 | 0 | #2 | 0 | 2 | 3147ms | ✓ |
| fission | gcc -O0 | 0.128 | 0 | #3 | 2 | 2 | 7607ms | ✓ |
| fission | gcc-m32 -O0 | 0.091 | 0 | #3 | 1 | 2 | 3612ms | ✓ |
| fission | gcc -O2 | 0.139 | 1 | #2 | 2 | 2 | 3661ms | ✓ |
| fission | gcc-m32 -O2 | 0.162 | 0 | #1 | 0 | 3 | 5936ms | ✓ |
| ghidra | gcc -O0 | 0.517 | 0 | #1 | 0 | 2 | 32049ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.787 | 1 | #1 | 0 | 2 | 24185ms | ✓ |
| ghidra | gcc -O2 | 0.120 | 1 | #3 | 0 | 3 | 29833ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.120 | 1 | #3 | 0 | 3 | 30391ms | ✓ |
| radare2 | gcc -O0 | 0.009 | 0 | #4 | 0 | 0 | 1646ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.005 | 0 | #4 | 0 | 0 | 381ms | ✓ |
| radare2 | gcc -O2 | 0.009 | 0 | #4 | 0 | 0 | 426ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.005 | 0 | #4 | 0 | 0 | 1532ms | ✓ |
| retdec | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 152ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O0 | 0.000 | 0 | — | 0 | 0 | 174ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 30ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O2 | 0.000 | 0 | — | 0 | 0 | 89ms | ❌ No matching plugins found for 'GCC'
No m |
| revng | gcc -O0 | 0.001 | 0 | #5 | 0 | 10 | 91908ms | ✓ |
| revng | gcc-m32 -O0 | 0.001 | 0 | #6 | 0 | 8 | 33616ms | ✓ |
| revng | gcc -O2 | 0.001 | 0 | #6 | 0 | 10 | 90322ms | ✓ |
| revng | gcc-m32 -O2 | 0.001 | 0 | #6 | 0 | 8 | 42639ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #6 | 222 | 7 | 2420ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #5 | 155 | 7 | 855ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #5 | 220 | 7 | 764ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #5 | 151 | 7 | 2678ms | ✓ |

### `binary_search`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.335 | 1 | #1 | 0 | 2 | 3121ms | ✓ |
| angr | gcc-m32 -O0 | 0.386 | 0 | #2 | 0 | 2 | 2221ms | ✓ |
| angr | gcc -O2 | 0.160 | 0 | #2 | 0 | 4 | 2368ms | ✓ |
| angr | gcc-m32 -O2 | 0.175 | 0 | #2 | 0 | 4 | 1841ms | ✓ |
| fission | gcc -O0 | 0.051 | 0 | #3 | 6 | 2 | 13286ms | ✓ |
| fission | gcc-m32 -O0 | 0.034 | 0 | #3 | 6 | 2 | 8947ms | ✓ |
| fission | gcc -O2 | 0.056 | 0 | #3 | 6 | 2 | 4301ms | ✓ |
| fission | gcc-m32 -O2 | 0.081 | 0 | #3 | 3 | 4 | 3395ms | ✓ |
| ghidra | gcc -O0 | 0.242 | 0 | #2 | 0 | 3 | 31369ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.438 | 1 | #1 | 0 | 3 | 26920ms | ✓ |
| ghidra | gcc -O2 | 0.239 | 1 | #1 | 0 | 5 | 22257ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.239 | 1 | #1 | 0 | 5 | 18849ms | ✓ |
| radare2 | gcc -O0 | 0.006 | 0 | #4 | 0 | 0 | 459ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.005 | 0 | #4 | 0 | 0 | 925ms | ✓ |
| radare2 | gcc -O2 | 0.009 | 0 | #4 | 0 | 0 | 896ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.004 | 0 | #4 | 0 | 0 | 805ms | ✓ |
| retdec | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 34ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O0 | 0.000 | 0 | — | 0 | 0 | 57ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 52ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O2 | 0.000 | 0 | — | 0 | 0 | 43ms | ❌ No matching plugins found for 'GCC'
No m |
| revng | gcc -O0 | 0.001 | 0 | #5 | 0 | 10 | 92376ms | ✓ |
| revng | gcc-m32 -O0 | 0.002 | 0 | #5 | 0 | 8 | 35530ms | ✓ |
| revng | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 0ms | ✓ |
| revng | gcc-m32 -O2 | 0.001 | 0 | #6 | 0 | 8 | 33285ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #6 | 224 | 7 | 975ms | ✓ |
| snowman | gcc-m32 -O0 | 0.002 | 0 | #6 | 157 | 7 | 867ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #5 | 223 | 7 | 979ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #5 | 154 | 7 | 775ms | ✓ |

### `bubble_sort`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.295 | 1 | #1 | 0 | 4 | 2043ms | ✓ |
| angr | gcc-m32 -O0 | 0.257 | 0 | #1 | 0 | 4 | 1814ms | ✓ |
| angr | gcc -O2 | 0.107 | 0 | #2 | 0 | 4 | 2643ms | ✓ |
| angr | gcc-m32 -O2 | 0.069 | 0 | #2 | 0 | 5 | 2313ms | ✓ |
| fission | gcc -O0 | 0.008 | 0 | #3 | 4 | 2 | 5536ms | ✓ |
| fission | gcc-m32 -O0 | 0.048 | 0 | #3 | 4 | 3 | 3180ms | ✓ |
| fission | gcc -O2 | 0.105 | 0 | #3 | 4 | 3 | 8755ms | ✓ |
| fission | gcc-m32 -O2 | 0.038 | 0 | #3 | 2 | 4 | 5312ms | ✓ |
| ghidra | gcc -O0 | 0.167 | 0 | #2 | 0 | 4 | 23938ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.152 | 1 | #2 | 0 | 4 | 18204ms | ✓ |
| ghidra | gcc -O2 | 0.131 | 0 | #1 | 0 | 5 | 30977ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.190 | 1 | #1 | 0 | 5 | 27443ms | ✓ |
| radare2 | gcc -O0 | 0.006 | 0 | #4 | 0 | 0 | 464ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.004 | 0 | #4 | 0 | 0 | 849ms | ✓ |
| radare2 | gcc -O2 | 0.007 | 0 | #4 | 0 | 0 | 976ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.006 | 0 | #4 | 0 | 0 | 917ms | ✓ |
| retdec | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 108ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O0 | 0.000 | 0 | — | 0 | 0 | 172ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 90ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O2 | 0.000 | 0 | — | 0 | 0 | 28ms | ❌ No matching plugins found for 'GCC'
No m |
| revng | gcc -O0 | 0.001 | 0 | #5 | 0 | 10 | 89696ms | ✓ |
| revng | gcc-m32 -O0 | 0.002 | 0 | #5 | 0 | 8 | 24259ms | ✓ |
| revng | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 0ms | ✓ |
| revng | gcc-m32 -O2 | 0.001 | 0 | #6 | 0 | 8 | 46736ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #6 | 224 | 7 | 971ms | ✓ |
| snowman | gcc-m32 -O0 | 0.002 | 0 | #6 | 157 | 7 | 626ms | ✓ |
| snowman | gcc -O2 | 0.002 | 0 | #5 | 223 | 7 | 1184ms | ✓ |
| snowman | gcc-m32 -O2 | 0.002 | 0 | #5 | 154 | 7 | 786ms | ✓ |

### `checksum`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.567 | 1 | #2 | 0 | 2 | 1940ms | ✓ |
| angr | gcc-m32 -O0 | 0.598 | 0 | #2 | 0 | 2 | 1792ms | ✓ |
| angr | gcc -O2 | 0.125 | 1 | #3 | 0 | 2 | 1601ms | ✓ |
| angr | gcc-m32 -O2 | 0.095 | 1 | #3 | 0 | 2 | 1927ms | ✓ |
| fission | gcc -O0 | 0.103 | 0 | #3 | 2 | 2 | 4071ms | ✓ |
| fission | gcc-m32 -O0 | 0.074 | 0 | #3 | 1 | 2 | 3384ms | ✓ |
| fission | gcc -O2 | 0.170 | 1 | #1 | 0 | 3 | 3036ms | ✓ |
| fission | gcc-m32 -O2 | 0.122 | 0 | #1 | 0 | 3 | 3489ms | ✓ |
| ghidra | gcc -O0 | 0.668 | 0 | #1 | 0 | 2 | 31281ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.819 | 1 | #1 | 0 | 2 | 26030ms | ✓ |
| ghidra | gcc -O2 | 0.129 | 1 | #2 | 0 | 3 | 26826ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.116 | 1 | #2 | 0 | 3 | 23620ms | ✓ |
| radare2 | gcc -O0 | 0.012 | 0 | #4 | 0 | 0 | 445ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.011 | 0 | #4 | 0 | 0 | 721ms | ✓ |
| radare2 | gcc -O2 | 0.012 | 0 | #4 | 0 | 0 | 469ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.010 | 0 | #4 | 0 | 0 | 683ms | ✓ |
| retdec | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 30ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O0 | 0.000 | 0 | — | 0 | 0 | 45ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 29ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O2 | 0.000 | 0 | — | 0 | 0 | 48ms | ❌ No matching plugins found for 'GCC'
No m |
| revng | gcc -O0 | 0.001 | 0 | #6 | 0 | 10 | 83931ms | ✓ |
| revng | gcc-m32 -O0 | 0.001 | 0 | #5 | 0 | 8 | 35326ms | ✓ |
| revng | gcc -O2 | 0.001 | 0 | #6 | 0 | 10 | 89794ms | ✓ |
| revng | gcc-m32 -O2 | 0.001 | 0 | #6 | 0 | 8 | 38665ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #5 | 227 | 7 | 858ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #6 | 161 | 7 | 892ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #5 | 219 | 7 | 946ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #5 | 151 | 7 | 1151ms | ✓ |

### `clamp`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.708 | 1 | #1 | 0 | 2 | 3451ms | ✓ |
| angr | gcc-m32 -O0 | 0.705 | 1 | #1 | 0 | 2 | 3201ms | ✓ |
| angr | gcc -O2 | 0.524 | 1 | #3 | 0 | 1 | 2102ms | ✓ |
| angr | gcc-m32 -O2 | 0.490 | 1 | #2 | 0 | 1 | 1777ms | ✓ |
| fission | gcc -O0 | 0.179 | 0 | #3 | 0 | 2 | 5596ms | ✓ |
| fission | gcc-m32 -O0 | 0.450 | 0 | #3 | 0 | 1 | 5501ms | ✓ |
| fission | gcc -O2 | 0.535 | 0 | #2 | 0 | 1 | 2735ms | ✓ |
| fission | gcc-m32 -O2 | 0.368 | 0 | #3 | 0 | 1 | 2866ms | ✓ |
| ghidra | gcc -O0 | 0.421 | 0 | #2 | 0 | 2 | 30443ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.590 | 1 | #2 | 0 | 2 | 25389ms | ✓ |
| ghidra | gcc -O2 | 0.582 | 1 | #1 | 0 | 2 | 35117ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.731 | 1 | #1 | 0 | 2 | 33984ms | ✓ |
| radare2 | gcc -O0 | 0.005 | 0 | #4 | 0 | 0 | 1335ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.005 | 0 | #4 | 0 | 0 | 1455ms | ✓ |
| radare2 | gcc -O2 | 0.006 | 0 | #4 | 0 | 0 | 404ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.005 | 0 | #4 | 0 | 0 | 645ms | ✓ |
| retdec | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 87ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O0 | 0.000 | 0 | — | 0 | 0 | 83ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 52ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O2 | 0.000 | 0 | — | 0 | 0 | 31ms | ❌ No matching plugins found for 'GCC'
No m |
| revng | gcc -O0 | 0.001 | 0 | #6 | 0 | 10 | 91200ms | ✓ |
| revng | gcc-m32 -O0 | 0.001 | 0 | #5 | 0 | 8 | 38453ms | ✓ |
| revng | gcc -O2 | 0.001 | 0 | #6 | 0 | 10 | 90944ms | ✓ |
| revng | gcc-m32 -O2 | 0.001 | 0 | #5 | 0 | 8 | 41849ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #5 | 227 | 7 | 1881ms | ✓ |
| snowman | gcc-m32 -O0 | 0.000 | 0 | #6 | 161 | 7 | 1665ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #5 | 219 | 7 | 746ms | ✓ |
| snowman | gcc-m32 -O2 | 0.000 | 0 | #6 | 151 | 7 | 585ms | ✓ |

### `classify_range`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.182 | 1 | #1 | 0 | 2 | 1937ms | ✓ |
| angr | gcc-m32 -O0 | 0.157 | 1 | #2 | 0 | 2 | 1705ms | ✓ |
| angr | gcc -O2 | 0.541 | 0 | #1 | 0 | 2 | 1680ms | ✓ |
| angr | gcc-m32 -O2 | 0.401 | 0 | #3 | 0 | 1 | 1547ms | ✓ |
| fission | gcc -O0 | 0.093 | 0 | #3 | 9 | 2 | 3932ms | ✓ |
| fission | gcc-m32 -O0 | 0.066 | 0 | #3 | 8 | 2 | 3328ms | ✓ |
| fission | gcc -O2 | 0.513 | 0 | #2 | 0 | 3 | 3173ms | ✓ |
| fission | gcc-m32 -O2 | 0.433 | 0 | #2 | 0 | 3 | 3031ms | ✓ |
| ghidra | gcc -O0 | 0.167 | 0 | #2 | 0 | 3 | 25063ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.174 | 1 | #1 | 0 | 3 | 26649ms | ✓ |
| ghidra | gcc -O2 | 0.486 | 1 | #3 | 0 | 3 | 28483ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.486 | 1 | #1 | 0 | 3 | 27033ms | ✓ |
| radare2 | gcc -O0 | 0.008 | 0 | #4 | 0 | 0 | 611ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.003 | 0 | #4 | 0 | 0 | 514ms | ✓ |
| radare2 | gcc -O2 | 0.009 | 0 | #4 | 0 | 0 | 419ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.003 | 0 | #4 | 0 | 0 | 618ms | ✓ |
| retdec | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 52ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O0 | 0.000 | 0 | — | 0 | 0 | 40ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 53ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O2 | 0.000 | 0 | — | 0 | 0 | 53ms | ❌ No matching plugins found for 'GCC'
No m |
| revng | gcc -O0 | 0.001 | 0 | #6 | 0 | 10 | 81972ms | ✓ |
| revng | gcc-m32 -O0 | 0.001 | 0 | #5 | 0 | 8 | 31570ms | ✓ |
| revng | gcc -O2 | 0.001 | 0 | #5 | 0 | 10 | 93220ms | ✓ |
| revng | gcc-m32 -O2 | 0.001 | 0 | #6 | 0 | 8 | 35155ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #5 | 227 | 7 | 894ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #6 | 161 | 7 | 915ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #6 | 219 | 7 | 887ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #5 | 151 | 7 | 708ms | ✓ |
>>>>>>> Stashed changes

### `count_bits`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
<<<<<<< Updated upstream
| fission | gcc -O0 | 0.118 | 0 | #2 | 1 | 2 | 5556ms | ✓ |
| fission | gcc-m32 -O0 | 0.102 | 0 | #2 | 1 | 2 | 5159ms | ✓ |
| fission | gcc -O2 | 0.133 | 1 | #2 | 0 | 3 | 5286ms | ✓ |
| fission | gcc-m32 -O2 | 0.123 | 0 | #2 | 0 | 3 | 5088ms | ✓ |
| ghidra | gcc -O0 | 0.688 | 0 | #1 | 0 | 2 | 15574ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.755 | 1 | #1 | 0 | 2 | 13873ms | ✓ |
| ghidra | gcc -O2 | 0.609 | 1 | #1 | 0 | 2 | 15684ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.609 | 1 | #1 | 0 | 2 | 13268ms | ✓ |
=======
| angr | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| angr | gcc-m32 -O0 | 0.655 | 1 | #2 | 0 | 2 | 2383ms | ✓ |
| angr | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| angr | gcc-m32 -O2 | 0.000 | 0 | — | 0 | 0 | 0ms | ❌ Server error '500 Internal Server Error' |
| fission | gcc -O0 | 0.135 | 0 | #2 | 2 | 2 | 39612ms | ✓ |
| fission | gcc-m32 -O0 | 0.102 | 0 | #3 | 1 | 2 | 39577ms | ✓ |
| fission | gcc -O2 | 0.104 | 1 | #2 | 1 | 3 | 40098ms | ✓ |
| fission | gcc-m32 -O2 | 0.123 | 0 | #2 | 0 | 3 | 39865ms | ✓ |
| ghidra | gcc -O0 | 0.688 | 0 | #1 | 0 | 2 | 70250ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.755 | 1 | #1 | 0 | 2 | 70267ms | ✓ |
| ghidra | gcc -O2 | 0.609 | 1 | #1 | 0 | 2 | 70175ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.609 | 1 | #1 | 0 | 2 | 70116ms | ✓ |
| radare2 | gcc -O0 | 0.009 | 0 | #3 | 0 | 0 | 2561ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.007 | 0 | #4 | 0 | 0 | 2658ms | ✓ |
| radare2 | gcc -O2 | 0.008 | 0 | #3 | 0 | 0 | 2228ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.006 | 0 | #3 | 0 | 0 | 2334ms | ✓ |
| retdec | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 222ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O0 | 0.000 | 0 | — | 0 | 0 | 217ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 191ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O2 | 0.000 | 0 | — | 0 | 0 | 207ms | ❌ No matching plugins found for 'GCC'
No m |
| revng | gcc -O0 | 0.001 | 0 | #5 | 0 | 10 | 97666ms | ✓ |
| revng | gcc-m32 -O0 | 0.001 | 0 | #5 | 0 | 8 | 54999ms | ✓ |
| revng | gcc -O2 | 0.001 | 0 | #5 | 0 | 10 | 103102ms | ✓ |
| revng | gcc-m32 -O2 | 0.001 | 0 | #5 | 0 | 8 | 60054ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #4 | 227 | 7 | 4047ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #6 | 161 | 7 | 3820ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #4 | 219 | 7 | 4152ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #4 | 151 | 7 | 3645ms | ✓ |

### `factorial`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.702 | 1 | #1 | 0 | 1 | 3441ms | ✓ |
| angr | gcc-m32 -O0 | 0.548 | 0 | #2 | 0 | 1 | 3214ms | ✓ |
| angr | gcc -O2 | 0.239 | 0 | #2 | 0 | 2 | 1692ms | ✓ |
| angr | gcc-m32 -O2 | 0.135 | 1 | #2 | 0 | 2 | 1690ms | ✓ |
| fission | gcc -O0 | 0.033 | 0 | #3 | 2 | 2 | 6980ms | ✓ |
| fission | gcc-m32 -O0 | 0.050 | 0 | #3 | 0 | 3 | 7337ms | ✓ |
| fission | gcc -O2 | 0.244 | 0 | #1 | 1 | 2 | 2912ms | ✓ |
| fission | gcc-m32 -O2 | 0.022 | 0 | #3 | 1 | 2 | 5176ms | ✓ |
| ghidra | gcc -O0 | 0.335 | 0 | #2 | 0 | 2 | 29181ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.579 | 1 | #1 | 0 | 2 | 25963ms | ✓ |
| ghidra | gcc -O2 | 0.212 | 1 | #3 | 0 | 3 | 27174ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.136 | 0 | #1 | 0 | 3 | 22721ms | ✓ |
| radare2 | gcc -O0 | 0.004 | 0 | #4 | 0 | 0 | 1640ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.001 | 0 | #4 | 0 | 0 | 1614ms | ✓ |
| radare2 | gcc -O2 | 0.003 | 0 | #4 | 0 | 0 | 441ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.001 | 0 | #4 | 0 | 0 | 737ms | ✓ |
| retdec | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 29ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O0 | 0.000 | 0 | — | 0 | 0 | 55ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 37ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O2 | 0.000 | 0 | — | 0 | 0 | 29ms | ❌ No matching plugins found for 'GCC'
No m |
| revng | gcc -O0 | 0.000 | 0 | #6 | 0 | 10 | 97000ms | ✓ |
| revng | gcc-m32 -O0 | 0.001 | 0 | #6 | 0 | 8 | 34736ms | ✓ |
| revng | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 0ms | ✓ |
| revng | gcc-m32 -O2 | 0.000 | 0 | #6 | 0 | 8 | 38813ms | ✓ |
| snowman | gcc -O0 | 0.000 | 0 | #5 | 224 | 7 | 1692ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #5 | 157 | 7 | 2104ms | ✓ |
| snowman | gcc -O2 | 0.000 | 0 | #5 | 223 | 7 | 708ms | ✓ |
| snowman | gcc-m32 -O2 | 0.000 | 0 | #5 | 154 | 7 | 894ms | ✓ |

### `fibonacci`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.597 | 1 | #1 | 0 | 2 | 1806ms | ✓ |
| angr | gcc-m32 -O0 | 0.590 | 1 | #2 | 0 | 2 | 3174ms | ✓ |
| angr | gcc -O2 | 0.325 | 1 | #1 | 0 | 2 | 3566ms | ✓ |
| angr | gcc-m32 -O2 | 0.391 | 1 | #1 | 0 | 2 | 2364ms | ✓ |
| fission | gcc -O0 | 0.044 | 0 | #3 | 0 | 3 | 4267ms | ✓ |
| fission | gcc-m32 -O0 | 0.477 | 0 | #3 | 0 | 3 | 5895ms | ✓ |
| fission | gcc -O2 | 0.172 | 0 | #3 | 1 | 3 | 7133ms | ✓ |
| fission | gcc-m32 -O2 | 0.088 | 0 | #3 | 0 | 3 | 3872ms | ✓ |
| ghidra | gcc -O0 | 0.321 | 0 | #2 | 0 | 2 | 27616ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.598 | 1 | #1 | 0 | 2 | 25362ms | ✓ |
| ghidra | gcc -O2 | 0.218 | 1 | #2 | 0 | 3 | 29311ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.260 | 1 | #2 | 0 | 3 | 24035ms | ✓ |
| radare2 | gcc -O0 | 0.004 | 0 | #4 | 0 | 0 | 862ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.004 | 0 | #4 | 0 | 0 | 1514ms | ✓ |
| radare2 | gcc -O2 | 0.004 | 0 | #4 | 0 | 0 | 1784ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.004 | 0 | #4 | 0 | 0 | 802ms | ✓ |
| retdec | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 49ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O0 | 0.000 | 0 | — | 0 | 0 | 95ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 101ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O2 | 0.000 | 0 | — | 0 | 0 | 29ms | ❌ No matching plugins found for 'GCC'
No m |
| revng | gcc -O0 | 0.000 | 0 | #6 | 0 | 10 | 91497ms | ✓ |
| revng | gcc-m32 -O0 | 0.001 | 0 | #6 | 0 | 8 | 31039ms | ✓ |
| revng | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 0ms | ✓ |
| revng | gcc-m32 -O2 | 0.000 | 0 | #6 | 0 | 8 | 37755ms | ✓ |
| snowman | gcc -O0 | 0.000 | 0 | #5 | 224 | 7 | 884ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #5 | 157 | 7 | 2025ms | ✓ |
| snowman | gcc -O2 | 0.000 | 0 | #5 | 223 | 7 | 1769ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #5 | 154 | 7 | 868ms | ✓ |

### `fibonacci_iter`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.711 | 1 | #1 | 0 | 2 | 1724ms | ✓ |
| angr | gcc-m32 -O0 | 0.709 | 1 | #2 | 0 | 2 | 1523ms | ✓ |
| angr | gcc -O2 | 0.248 | 0 | #1 | 0 | 2 | 1891ms | ✓ |
| angr | gcc-m32 -O2 | 0.262 | 0 | #1 | 0 | 2 | 1588ms | ✓ |
| fission | gcc -O0 | 0.176 | 0 | #3 | 4 | 2 | 4074ms | ✓ |
| fission | gcc-m32 -O0 | 0.156 | 0 | #3 | 2 | 2 | 2884ms | ✓ |
| fission | gcc -O2 | 0.245 | 0 | #2 | 0 | 2 | 3430ms | ✓ |
| fission | gcc-m32 -O2 | 0.217 | 0 | #3 | 0 | 3 | 2887ms | ✓ |
| ghidra | gcc -O0 | 0.480 | 0 | #2 | 0 | 3 | 27831ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.718 | 1 | #1 | 0 | 3 | 24971ms | ✓ |
| ghidra | gcc -O2 | 0.241 | 1 | #3 | 0 | 3 | 25763ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.243 | 1 | #2 | 0 | 3 | 18862ms | ✓ |
| radare2 | gcc -O0 | 0.007 | 0 | #4 | 0 | 0 | 583ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.004 | 0 | #4 | 0 | 0 | 377ms | ✓ |
| radare2 | gcc -O2 | 0.008 | 0 | #4 | 0 | 0 | 772ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.003 | 0 | #4 | 0 | 0 | 729ms | ✓ |
| retdec | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 52ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O0 | 0.000 | 0 | — | 0 | 0 | 47ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 72ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O2 | 0.000 | 0 | — | 0 | 0 | 30ms | ❌ No matching plugins found for 'GCC'
No m |
| revng | gcc -O0 | 0.001 | 0 | #6 | 0 | 10 | 81451ms | ✓ |
| revng | gcc-m32 -O0 | 0.001 | 0 | #6 | 0 | 8 | 31245ms | ✓ |
| revng | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 0ms | ✓ |
| revng | gcc-m32 -O2 | 0.001 | 0 | #6 | 0 | 8 | 30803ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #5 | 224 | 7 | 824ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #5 | 157 | 7 | 720ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #5 | 223 | 7 | 1026ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #5 | 154 | 7 | 761ms | ✓ |

### `find_pair_value`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.289 | 1 | #2 | 0 | 2 | 2217ms | ✓ |
| angr | gcc-m32 -O0 | 0.277 | 0 | #2 | 0 | 2 | 1907ms | ✓ |
| angr | gcc -O2 | 0.215 | 1 | #1 | 0 | 2 | 2149ms | ✓ |
| angr | gcc-m32 -O2 | 0.165 | 1 | #2 | 0 | 2 | 3406ms | ✓ |
| fission | gcc -O0 | 0.097 | 0 | #3 | 4 | 2 | 3741ms | ✓ |
| fission | gcc-m32 -O0 | 0.099 | 0 | #3 | 3 | 2 | 3370ms | ✓ |
| fission | gcc -O2 | 0.165 | 1 | #3 | 3 | 4 | 3613ms | ✓ |
| fission | gcc-m32 -O2 | 0.099 | 0 | #3 | 3 | 4 | 6372ms | ✓ |
| ghidra | gcc -O0 | 0.342 | 0 | #1 | 0 | 3 | 29546ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.695 | 1 | #1 | 0 | 3 | 26116ms | ✓ |
| ghidra | gcc -O2 | 0.212 | 1 | #2 | 0 | 4 | 27001ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.212 | 1 | #1 | 0 | 4 | 28163ms | ✓ |
| radare2 | gcc -O0 | 0.005 | 0 | #4 | 0 | 0 | 716ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.005 | 0 | #4 | 0 | 0 | 821ms | ✓ |
| radare2 | gcc -O2 | 0.005 | 0 | #4 | 0 | 0 | 1006ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.004 | 0 | #4 | 0 | 0 | 1548ms | ✓ |
| retdec | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 74ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O0 | 0.000 | 0 | — | 0 | 0 | 59ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 29ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O2 | 0.000 | 0 | — | 0 | 0 | 129ms | ❌ No matching plugins found for 'GCC'
No m |
| revng | gcc -O0 | 0.001 | 0 | #5 | 0 | 10 | 90716ms | ✓ |
| revng | gcc-m32 -O0 | 0.001 | 0 | #6 | 0 | 8 | 34552ms | ✓ |
| revng | gcc -O2 | 0.001 | 0 | #6 | 0 | 10 | 93623ms | ✓ |
| revng | gcc-m32 -O2 | 0.001 | 0 | #6 | 0 | 8 | 41784ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #6 | 222 | 7 | 915ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #5 | 155 | 7 | 876ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #5 | 220 | 7 | 886ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #5 | 151 | 7 | 1964ms | ✓ |

### `gcd`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.467 | 1 | #2 | 0 | 2 | 1911ms | ✓ |
| angr | gcc-m32 -O0 | 0.488 | 1 | #2 | 0 | 2 | 1699ms | ✓ |
| angr | gcc -O2 | 0.467 | 0 | #2 | 0 | 3 | 3381ms | ✓ |
| angr | gcc-m32 -O2 | 0.388 | 1 | #2 | 0 | 2 | 2875ms | ✓ |
| fission | gcc -O0 | 0.077 | 1 | #3 | 2 | 2 | 3581ms | ✓ |
| fission | gcc-m32 -O0 | 0.068 | 0 | #3 | 1 | 2 | 3419ms | ✓ |
| fission | gcc -O2 | 0.129 | 0 | #3 | 2 | 2 | 6287ms | ✓ |
| fission | gcc-m32 -O2 | 0.153 | 0 | #3 | 0 | 3 | 5432ms | ✓ |
| ghidra | gcc -O0 | 0.596 | 0 | #1 | 0 | 2 | 23524ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.749 | 1 | #1 | 0 | 2 | 21017ms | ✓ |
| ghidra | gcc -O2 | 0.778 | 1 | #1 | 0 | 2 | 29476ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.514 | 1 | #1 | 0 | 3 | 26943ms | ✓ |
| radare2 | gcc -O0 | 0.004 | 0 | #4 | 0 | 0 | 660ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.003 | 0 | #4 | 0 | 0 | 944ms | ✓ |
| radare2 | gcc -O2 | 0.004 | 0 | #4 | 0 | 0 | 1379ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.002 | 0 | #4 | 0 | 0 | 776ms | ✓ |
| retdec | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 121ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O0 | 0.000 | 0 | — | 0 | 0 | 83ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 46ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O2 | 0.000 | 0 | — | 0 | 0 | 77ms | ❌ No matching plugins found for 'GCC'
No m |
| revng | gcc -O0 | 0.001 | 0 | #6 | 0 | 10 | 90899ms | ✓ |
| revng | gcc-m32 -O0 | 0.001 | 0 | #5 | 0 | 8 | 28035ms | ✓ |
| revng | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 0ms | ✓ |
| revng | gcc-m32 -O2 | 0.001 | 0 | #6 | 0 | 8 | 43392ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #5 | 224 | 7 | 1125ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #6 | 157 | 7 | 778ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #5 | 223 | 7 | 1962ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #5 | 154 | 7 | 2417ms | ✓ |

### `linear_search`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.707 | 1 | #1 | 0 | 2 | 1843ms | ✓ |
| angr | gcc-m32 -O0 | 0.714 | 0 | #1 | 0 | 2 | 2158ms | ✓ |
| angr | gcc -O2 | 0.200 | 0 | #2 | 0 | 2 | 2118ms | ✓ |
| angr | gcc-m32 -O2 | 0.497 | 0 | #2 | 0 | 2 | 1735ms | ✓ |
| fission | gcc -O0 | 0.135 | 0 | #3 | 4 | 2 | 3627ms | ✓ |
| fission | gcc-m32 -O0 | 0.114 | 0 | #3 | 3 | 2 | 3471ms | ✓ |
| fission | gcc -O2 | 0.154 | 0 | #3 | 3 | 4 | 3394ms | ✓ |
| fission | gcc-m32 -O2 | 0.080 | 0 | #3 | 3 | 4 | 3310ms | ✓ |
| ghidra | gcc -O0 | 0.371 | 0 | #2 | 0 | 3 | 25281ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.617 | 1 | #2 | 0 | 3 | 20461ms | ✓ |
| ghidra | gcc -O2 | 0.660 | 1 | #1 | 0 | 4 | 28041ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.688 | 1 | #1 | 0 | 4 | 22977ms | ✓ |
| radare2 | gcc -O0 | 0.005 | 0 | #4 | 0 | 0 | 554ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.002 | 0 | #4 | 0 | 0 | 488ms | ✓ |
| radare2 | gcc -O2 | 0.005 | 0 | #4 | 0 | 0 | 847ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.002 | 0 | #4 | 0 | 0 | 699ms | ✓ |
| retdec | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 52ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O0 | 0.000 | 0 | — | 0 | 0 | 37ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 62ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O2 | 0.000 | 0 | — | 0 | 0 | 41ms | ❌ No matching plugins found for 'GCC'
No m |
| revng | gcc -O0 | 0.001 | 0 | #6 | 0 | 10 | 84946ms | ✓ |
| revng | gcc-m32 -O0 | 0.001 | 0 | #6 | 0 | 8 | 27806ms | ✓ |
| revng | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 0ms | ✓ |
| revng | gcc-m32 -O2 | 0.001 | 0 | #6 | 0 | 8 | 36135ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #5 | 224 | 7 | 1013ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #5 | 157 | 7 | 1097ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #5 | 223 | 7 | 972ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #5 | 154 | 7 | 801ms | ✓ |

### `max`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.752 | 1 | #1 | 0 | 1 | 1558ms | ✓ |
| angr | gcc-m32 -O0 | 0.673 | 1 | #1 | 0 | 1 | 1568ms | ✓ |
| angr | gcc -O2 | 0.752 | 1 | #1 | 0 | 1 | 1844ms | ✓ |
| angr | gcc-m32 -O2 | 0.667 | 1 | #1 | 0 | 1 | 1679ms | ✓ |
| fission | gcc -O0 | 0.365 | 0 | #3 | 0 | 1 | 3022ms | ✓ |
| fission | gcc-m32 -O0 | 0.419 | 0 | #3 | 0 | 1 | 2935ms | ✓ |
| fission | gcc -O2 | 0.579 | 0 | #3 | 0 | 1 | 2719ms | ✓ |
| fission | gcc-m32 -O2 | 0.419 | 0 | #3 | 0 | 1 | 2841ms | ✓ |
| ghidra | gcc -O0 | 0.431 | 0 | #2 | 0 | 2 | 25688ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.654 | 1 | #2 | 0 | 2 | 22905ms | ✓ |
| ghidra | gcc -O2 | 0.654 | 1 | #2 | 0 | 2 | 21627ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.660 | 1 | #2 | 0 | 2 | 21776ms | ✓ |
| radare2 | gcc -O0 | 0.002 | 0 | #4 | 0 | 0 | 824ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.001 | 0 | #4 | 0 | 0 | 564ms | ✓ |
| radare2 | gcc -O2 | 0.002 | 0 | #4 | 0 | 0 | 443ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.001 | 0 | #4 | 0 | 0 | 706ms | ✓ |
| retdec | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 29ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O0 | 0.000 | 0 | — | 0 | 0 | 32ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 29ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O2 | 0.000 | 0 | — | 0 | 0 | 78ms | ❌ No matching plugins found for 'GCC'
No m |
| revng | gcc -O0 | 0.000 | 0 | #6 | 0 | 10 | 74879ms | ✓ |
| revng | gcc-m32 -O0 | 0.001 | 0 | #6 | 0 | 8 | 26042ms | ✓ |
| revng | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 0ms | ✓ |
| revng | gcc-m32 -O2 | 0.000 | 0 | #6 | 0 | 8 | 40224ms | ✓ |
| snowman | gcc -O0 | 0.000 | 0 | #5 | 224 | 7 | 994ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #5 | 157 | 7 | 890ms | ✓ |
| snowman | gcc -O2 | 0.000 | 0 | #5 | 223 | 7 | 979ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #5 | 154 | 7 | 1024ms | ✓ |

### `pointer_stride_sum`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.253 | 1 | #2 | 0 | 2 | 3392ms | ✓ |
| angr | gcc-m32 -O0 | 0.511 | 1 | #2 | 0 | 2 | 2309ms | ✓ |
| angr | gcc -O2 | 0.325 | 1 | #2 | 0 | 3 | 1527ms | ✓ |
| angr | gcc-m32 -O2 | 0.195 | 1 | #3 | 0 | 2 | 1615ms | ✓ |
| fission | gcc -O0 | 0.097 | 0 | #3 | 2 | 2 | 6134ms | ✓ |
| fission | gcc-m32 -O0 | 0.166 | 0 | #3 | 1 | 2 | 3833ms | ✓ |
| fission | gcc -O2 | 0.319 | 1 | #3 | 0 | 3 | 3327ms | ✓ |
| fission | gcc-m32 -O2 | 0.226 | 0 | #2 | 0 | 3 | 2965ms | ✓ |
| ghidra | gcc -O0 | 0.259 | 0 | #1 | 0 | 2 | 35390ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.674 | 1 | #1 | 0 | 2 | 23690ms | ✓ |
| ghidra | gcc -O2 | 0.609 | 1 | #1 | 0 | 2 | 26539ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.648 | 1 | #1 | 0 | 2 | 26031ms | ✓ |
| radare2 | gcc -O0 | 0.005 | 0 | #4 | 0 | 0 | 1630ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.004 | 0 | #4 | 0 | 0 | 681ms | ✓ |
| radare2 | gcc -O2 | 0.006 | 0 | #4 | 0 | 0 | 448ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.005 | 0 | #4 | 0 | 0 | 385ms | ✓ |
| retdec | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 115ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O0 | 0.000 | 0 | — | 0 | 0 | 34ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 70ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O2 | 0.000 | 0 | — | 0 | 0 | 55ms | ❌ No matching plugins found for 'GCC'
No m |
| revng | gcc -O0 | 0.001 | 0 | #6 | 0 | 10 | 92627ms | ✓ |
| revng | gcc-m32 -O0 | 0.001 | 0 | #6 | 0 | 8 | 31980ms | ✓ |
| revng | gcc -O2 | 0.001 | 0 | #6 | 0 | 10 | 85844ms | ✓ |
| revng | gcc-m32 -O2 | 0.001 | 0 | #6 | 0 | 8 | 34551ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #5 | 222 | 7 | 2519ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #5 | 155 | 7 | 943ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #5 | 220 | 7 | 757ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #5 | 151 | 7 | 810ms | ✓ |

### `power`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.283 | 1 | #2 | 0 | 2 | 1851ms | ✓ |
| angr | gcc-m32 -O0 | 0.176 | 0 | #2 | 0 | 3 | 2148ms | ✓ |
| angr | gcc -O2 | 0.195 | 0 | #2 | 0 | 2 | 1728ms | ✓ |
| angr | gcc-m32 -O2 | 0.088 | 0 | #2 | 0 | 3 | 2218ms | ✓ |
| fission | gcc -O0 | 0.077 | 0 | #3 | 2 | 2 | 3753ms | ✓ |
| fission | gcc-m32 -O0 | 0.039 | 0 | #3 | 1 | 2 | 3808ms | ✓ |
| fission | gcc -O2 | 0.081 | 0 | #3 | 2 | 5 | 3243ms | ✓ |
| fission | gcc-m32 -O2 | 0.035 | 0 | #3 | 1 | 5 | 4613ms | ✓ |
| ghidra | gcc -O0 | 0.374 | 0 | #1 | 0 | 3 | 26264ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.492 | 0 | #1 | 0 | 3 | 25249ms | ✓ |
| ghidra | gcc -O2 | 0.392 | 1 | #1 | 0 | 4 | 27111ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.249 | 0 | #1 | 0 | 4 | 25052ms | ✓ |
| radare2 | gcc -O0 | 0.008 | 0 | #4 | 0 | 0 | 727ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.004 | 0 | #4 | 0 | 0 | 867ms | ✓ |
| radare2 | gcc -O2 | 0.008 | 0 | #4 | 0 | 0 | 902ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.004 | 0 | #4 | 0 | 0 | 551ms | ✓ |
| retdec | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 50ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O0 | 0.000 | 0 | — | 0 | 0 | 51ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 35ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O2 | 0.000 | 0 | — | 0 | 0 | 48ms | ❌ No matching plugins found for 'GCC'
No m |
| revng | gcc -O0 | 0.001 | 0 | #5 | 0 | 10 | 96054ms | ✓ |
| revng | gcc-m32 -O0 | 0.002 | 0 | #5 | 0 | 8 | 32534ms | ✓ |
| revng | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 0ms | ✓ |
| revng | gcc-m32 -O2 | 0.001 | 0 | #6 | 0 | 8 | 40632ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #6 | 224 | 7 | 808ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #6 | 157 | 7 | 743ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #5 | 223 | 7 | 782ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #5 | 154 | 7 | 785ms | ✓ |

### `process_code`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.661 | 1 | #1 | 0 | 1 | 1907ms | ✓ |
| angr | gcc-m32 -O0 | 0.660 | 1 | #1 | 0 | 1 | 2002ms | ✓ |
| angr | gcc -O2 | 0.247 | 1 | #3 | 0 | 3 | 1726ms | ✓ |
| angr | gcc-m32 -O2 | 0.260 | 1 | #2 | 0 | 3 | 1547ms | ✓ |
| fission | gcc -O0 | 0.049 | 0 | #3 | 4 | 3 | 3685ms | ✓ |
| fission | gcc-m32 -O0 | 0.054 | 0 | #3 | 3 | 5 | 3600ms | ✓ |
| fission | gcc -O2 | 0.331 | 0 | #1 | 0 | 1 | 3245ms | ✓ |
| fission | gcc-m32 -O2 | 0.099 | 0 | #3 | 0 | 5 | 3459ms | ✓ |
| ghidra | gcc -O0 | 0.157 | 0 | #2 | 0 | 4 | 25314ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.166 | 1 | #2 | 0 | 4 | 22761ms | ✓ |
| ghidra | gcc -O2 | 0.286 | 1 | #2 | 0 | 2 | 25690ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.286 | 1 | #1 | 0 | 2 | 23046ms | ✓ |
| radare2 | gcc -O0 | 0.005 | 0 | #4 | 0 | 0 | 770ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.005 | 0 | #4 | 0 | 0 | 680ms | ✓ |
| radare2 | gcc -O2 | 0.006 | 0 | #4 | 0 | 0 | 577ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.004 | 0 | #4 | 0 | 0 | 501ms | ✓ |
| retdec | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 82ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O0 | 0.000 | 0 | — | 0 | 0 | 52ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 33ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O2 | 0.000 | 0 | — | 0 | 0 | 65ms | ❌ No matching plugins found for 'GCC'
No m |
| revng | gcc -O0 | 0.001 | 0 | #6 | 0 | 10 | 86814ms | ✓ |
| revng | gcc-m32 -O0 | 0.001 | 0 | #5 | 0 | 8 | 27695ms | ✓ |
| revng | gcc -O2 | 0.000 | 0 | #6 | 0 | 10 | 112958ms | ✓ |
| revng | gcc-m32 -O2 | 0.001 | 0 | #6 | 0 | 8 | 36736ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #5 | 224 | 7 | 981ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #6 | 157 | 7 | 787ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #5 | 223 | 7 | 766ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #5 | 154 | 7 | 827ms | ✓ |

### `reverse_in_place`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.273 | 0 | #2 | 0 | 2 | 1822ms | ✓ |
| angr | gcc-m32 -O0 | 0.222 | 0 | #2 | 0 | 2 | 2017ms | ✓ |
| angr | gcc -O2 | 0.164 | 0 | #2 | 0 | 3 | 1935ms | ✓ |
| angr | gcc-m32 -O2 | 0.099 | 0 | #3 | 0 | 3 | 2171ms | ✓ |
| fission | gcc -O0 | 0.106 | 0 | #3 | 2 | 2 | 5013ms | ✓ |
| fission | gcc-m32 -O0 | 0.051 | 0 | #3 | 1 | 2 | 3809ms | ✓ |
| fission | gcc -O2 | 0.131 | 0 | #3 | 2 | 3 | 3591ms | ✓ |
| fission | gcc-m32 -O2 | 0.121 | 0 | #2 | 2 | 2 | 3537ms | ✓ |
| ghidra | gcc -O0 | 0.323 | 0 | #1 | 0 | 2 | 27952ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.339 | 1 | #1 | 0 | 2 | 26005ms | ✓ |
| ghidra | gcc -O2 | 0.221 | 1 | #1 | 0 | 3 | 30062ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.221 | 1 | #1 | 0 | 3 | 25146ms | ✓ |
| radare2 | gcc -O0 | 0.006 | 0 | #4 | 0 | 0 | 579ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.006 | 0 | #4 | 0 | 0 | 913ms | ✓ |
| radare2 | gcc -O2 | 0.006 | 0 | #4 | 0 | 0 | 631ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.005 | 0 | #4 | 0 | 0 | 481ms | ✓ |
| retdec | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 50ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O0 | 0.000 | 0 | — | 0 | 0 | 44ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 73ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O2 | 0.000 | 0 | — | 0 | 0 | 28ms | ❌ No matching plugins found for 'GCC'
No m |
| revng | gcc -O0 | 0.002 | 0 | #5 | 0 | 10 | 88450ms | ✓ |
| revng | gcc-m32 -O0 | 0.001 | 0 | #6 | 0 | 8 | 33893ms | ✓ |
| revng | gcc -O2 | 0.001 | 0 | #6 | 0 | 10 | 91955ms | ✓ |
| revng | gcc-m32 -O2 | 0.001 | 0 | #6 | 0 | 8 | 38100ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #6 | 222 | 7 | 869ms | ✓ |
| snowman | gcc-m32 -O0 | 0.002 | 0 | #5 | 155 | 7 | 1134ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #5 | 220 | 7 | 855ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #5 | 151 | 7 | 831ms | ✓ |

### `saturating_add`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.769 | 1 | #1 | 0 | 1 | 2133ms | ✓ |
| angr | gcc-m32 -O0 | 0.766 | 1 | #1 | 0 | 1 | 1611ms | ✓ |
| angr | gcc -O2 | 0.311 | 0 | #2 | 0 | 2 | 1666ms | ✓ |
| angr | gcc-m32 -O2 | 0.639 | 1 | #1 | 0 | 2 | 3098ms | ✓ |
| fission | gcc -O0 | 0.063 | 0 | #3 | 3 | 2 | 4270ms | ✓ |
| fission | gcc-m32 -O0 | 0.048 | 0 | #3 | 2 | 3 | 3699ms | ✓ |
| fission | gcc -O2 | 0.290 | 0 | #3 | 1 | 2 | 3151ms | ✓ |
| fission | gcc-m32 -O2 | 0.124 | 0 | #3 | 1 | 2 | 5796ms | ✓ |
| ghidra | gcc -O0 | 0.252 | 0 | #2 | 0 | 3 | 30426ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.246 | 1 | #2 | 0 | 3 | 27432ms | ✓ |
| ghidra | gcc -O2 | 0.606 | 1 | #1 | 0 | 2 | 29947ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.606 | 1 | #2 | 0 | 2 | 26901ms | ✓ |
| radare2 | gcc -O0 | 0.011 | 0 | #4 | 0 | 0 | 416ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.006 | 0 | #4 | 0 | 0 | 567ms | ✓ |
| radare2 | gcc -O2 | 0.012 | 0 | #4 | 0 | 0 | 517ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.006 | 0 | #4 | 0 | 0 | 1665ms | ✓ |
| retdec | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 52ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O0 | 0.000 | 0 | — | 0 | 0 | 29ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 54ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O2 | 0.000 | 0 | — | 0 | 0 | 51ms | ❌ No matching plugins found for 'GCC'
No m |
| revng | gcc -O0 | 0.001 | 0 | #6 | 0 | 10 | 86308ms | ✓ |
| revng | gcc-m32 -O0 | 0.001 | 0 | #5 | 0 | 8 | 31488ms | ✓ |
| revng | gcc -O2 | 0.001 | 0 | #5 | 0 | 10 | 100256ms | ✓ |
| revng | gcc-m32 -O2 | 0.001 | 0 | #6 | 0 | 8 | 40056ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #5 | 227 | 7 | 751ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #6 | 161 | 7 | 794ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #6 | 219 | 7 | 809ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #5 | 151 | 7 | 2684ms | ✓ |
>>>>>>> Stashed changes

### `signum`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
<<<<<<< Updated upstream
| fission | gcc -O0 | 0.057 | 0 | #2 | 0 | 3 | 5556ms | ✓ |
| fission | gcc-m32 -O0 | 0.321 | 0 | #2 | 0 | 3 | 5159ms | ✓ |
| fission | gcc -O2 | 0.489 | 0 | #2 | 0 | 1 | 5286ms | ✓ |
| fission | gcc-m32 -O2 | 0.094 | 0 | #2 | 0 | 3 | 5088ms | ✓ |
| ghidra | gcc -O0 | 0.375 | 0 | #1 | 0 | 3 | 15574ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.611 | 1 | #1 | 0 | 3 | 13873ms | ✓ |
| ghidra | gcc -O2 | 0.492 | 1 | #1 | 0 | 2 | 15684ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.583 | 1 | #1 | 0 | 2 | 13268ms | ✓ |
=======
| angr | gcc -O0 | 0.503 | 1 | #1 | 0 | 1 | 1901ms | ✓ |
| angr | gcc-m32 -O0 | 0.488 | 1 | #2 | 0 | 1 | 1477ms | ✓ |
| angr | gcc -O2 | 0.675 | 0 | #1 | 0 | 1 | 1504ms | ✓ |
| angr | gcc-m32 -O2 | 0.595 | 0 | #1 | 0 | 1 | 1738ms | ✓ |
| fission | gcc -O0 | 0.057 | 0 | #3 | 0 | 3 | 3165ms | ✓ |
| fission | gcc-m32 -O0 | 0.321 | 0 | #3 | 0 | 3 | 2892ms | ✓ |
| fission | gcc -O2 | 0.489 | 0 | #3 | 0 | 1 | 2913ms | ✓ |
| fission | gcc-m32 -O2 | 0.094 | 0 | #3 | 0 | 3 | 2999ms | ✓ |
| ghidra | gcc -O0 | 0.375 | 0 | #2 | 0 | 3 | 32573ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.611 | 1 | #1 | 0 | 3 | 19524ms | ✓ |
| ghidra | gcc -O2 | 0.492 | 1 | #2 | 0 | 2 | 26895ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.583 | 1 | #2 | 0 | 2 | 29593ms | ✓ |
| radare2 | gcc -O0 | 0.004 | 0 | #4 | 0 | 0 | 709ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.003 | 0 | #4 | 0 | 0 | 706ms | ✓ |
| radare2 | gcc -O2 | 0.003 | 0 | #4 | 0 | 0 | 617ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.004 | 0 | #4 | 0 | 0 | 432ms | ✓ |
| retdec | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 70ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O0 | 0.000 | 0 | — | 0 | 0 | 34ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 32ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O2 | 0.000 | 0 | — | 0 | 0 | 39ms | ❌ No matching plugins found for 'GCC'
No m |
| revng | gcc -O0 | 0.000 | 0 | #6 | 0 | 10 | 88199ms | ✓ |
| revng | gcc-m32 -O0 | 0.000 | 0 | #6 | 0 | 8 | 27923ms | ✓ |
| revng | gcc -O2 | 0.000 | 0 | #6 | 0 | 10 | 92542ms | ✓ |
| revng | gcc-m32 -O2 | 0.000 | 0 | #6 | 0 | 8 | 44691ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #5 | 227 | 7 | 833ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #5 | 161 | 7 | 739ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #5 | 219 | 7 | 901ms | ✓ |
| snowman | gcc-m32 -O2 | 0.000 | 0 | #5 | 151 | 7 | 727ms | ✓ |

### `sum_array`
| Decompiler | Variant | Similarity | Semantic | Rank | Gotos | Depth | Time | Status |
| ---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.455 | 1 | #2 | 0 | 2 | 3237ms | ✓ |
| angr | gcc-m32 -O0 | 0.543 | 0 | #2 | 0 | 2 | 1905ms | ✓ |
| angr | gcc -O2 | 0.171 | 1 | #2 | 0 | 2 | 1693ms | ✓ |
| angr | gcc-m32 -O2 | 0.122 | 1 | #3 | 0 | 2 | 2639ms | ✓ |
| fission | gcc -O0 | 0.145 | 0 | #3 | 2 | 2 | 5830ms | ✓ |
| fission | gcc-m32 -O0 | 0.120 | 0 | #3 | 1 | 2 | 3064ms | ✓ |
| fission | gcc -O2 | 0.357 | 1 | #1 | 0 | 3 | 3315ms | ✓ |
| fission | gcc-m32 -O2 | 0.124 | 0 | #2 | 0 | 3 | 3803ms | ✓ |
| ghidra | gcc -O0 | 0.648 | 0 | #1 | 0 | 2 | 31213ms | ✓ |
| ghidra | gcc-m32 -O0 | 0.833 | 1 | #1 | 0 | 2 | 23892ms | ✓ |
| ghidra | gcc -O2 | 0.171 | 1 | #3 | 0 | 3 | 28388ms | ✓ |
| ghidra | gcc-m32 -O2 | 0.171 | 1 | #1 | 0 | 3 | 26984ms | ✓ |
| radare2 | gcc -O0 | 0.008 | 0 | #4 | 0 | 0 | 1750ms | ✓ |
| radare2 | gcc-m32 -O0 | 0.005 | 0 | #4 | 0 | 0 | 645ms | ✓ |
| radare2 | gcc -O2 | 0.008 | 0 | #4 | 0 | 0 | 882ms | ✓ |
| radare2 | gcc-m32 -O2 | 0.005 | 0 | #4 | 0 | 0 | 417ms | ✓ |
| retdec | gcc -O0 | 0.000 | 0 | — | 0 | 0 | 54ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O0 | 0.000 | 0 | — | 0 | 0 | 48ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc -O2 | 0.000 | 0 | — | 0 | 0 | 56ms | ❌ No matching plugins found for 'GCC'
No m |
| retdec | gcc-m32 -O2 | 0.000 | 0 | — | 0 | 0 | 79ms | ❌ No matching plugins found for 'GCC'
No m |
| revng | gcc -O0 | 0.001 | 0 | #5 | 0 | 10 | 91966ms | ✓ |
| revng | gcc-m32 -O0 | 0.001 | 0 | #6 | 0 | 8 | 31174ms | ✓ |
| revng | gcc -O2 | 0.001 | 0 | #6 | 0 | 10 | 94613ms | ✓ |
| revng | gcc-m32 -O2 | 0.001 | 0 | #6 | 0 | 8 | 42955ms | ✓ |
| snowman | gcc -O0 | 0.001 | 0 | #6 | 222 | 7 | 1437ms | ✓ |
| snowman | gcc-m32 -O0 | 0.001 | 0 | #5 | 155 | 7 | 819ms | ✓ |
| snowman | gcc -O2 | 0.001 | 0 | #5 | 220 | 7 | 765ms | ✓ |
| snowman | gcc-m32 -O2 | 0.001 | 0 | #5 | 151 | 7 | 821ms | ✓ |
>>>>>>> Stashed changes

---

## Overfitting Analysis

Functions where **all** decompilers scored below 0.3 are marked as objectively hard.
Functions where **only Fission** scored below 0.3 are marked as quality gaps.

<<<<<<< Updated upstream
**Fission quality gaps (1):** `count_bits`
=======
**Objectively hard functions (1):** `bubble_sort`
**Fission quality gaps (12):** `count_bits`, `checksum`, `saturating_add`, `reverse_in_place`, `find_pair_value`, `accumulate_pairs`, `fibonacci_iter`, `linear_search`, `binary_search`, `factorial`, `gcd`, `power`
>>>>>>> Stashed changes
