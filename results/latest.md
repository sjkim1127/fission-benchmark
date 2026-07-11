# Fission Benchmark Report

**Generated:** 2026-07-11 01:42 UTC
**Corpus:** `dev`
**Functions evaluated:** 21

---

## ✅ VALID RUN — 84/84 Fission rows succeeded

## Summary — Correctness Score

> Readability metrics are recorded as unvalidated raw proxies. They are not combined into a final readability score until the human validation study is complete.

| Decompiler | Attempted | Valid | Adapter Fail | Compile Fail | Avg Correctness | Avg Similarity | Semantic Pass |
| ---|---|---|---|---|---|---|--- |
| **ghidra** | 84 | 84 | 0 | 0 | 0.694 | 0.427 | 70.2% |
| **angr** | 84 | 81 | 3 | 0 | 0.620 | 0.399 | 60.5% |
| **fission** | 84 | 84 | 0 | 0 | 0.154 | 0.164 | 8.3% |
| **radare2** | 84 | 84 | 0 | 0 | 0.101 | 0.005 | 0.0% |
| **revng** | 84 | 75 | 0 | 0 | 0.070 | 0.001 | 0.0% |
| **snowman** | 84 | 84 | 0 | 0 | 0.000 | 0.001 | 0.0% |
| ~~retdec~~ ⛔ | 84 | 0 | 84 | 0 | — | — | — |

---

## Per-Function Results

### `accumulate_pairs`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc-m32 -O0 | 0.979 | 0.787 | 100.0% | #1 | 0 | 2 | — | 24185ms | ✅ |
| angr | gcc -O0 | 0.933 | 0.331 | 100.0% | #1 | 0 | 2 | — | 3713ms | ✅ |
| ghidra | gcc -O2 | 0.902 | 0.120 | 100.0% | #1 | 0 | 3 | — | 29833ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.902 | 0.120 | 100.0% | #1 | 0 | 3 | — | 30391ms | ✅ |
| fission | gcc -O2 | 0.886 | 0.139 | 100.0% | #2 | 2 | 2 | — | 3661ms | ✅ |
| ghidra | gcc -O0 | 0.150 | 0.517 | 0.0% | #2 | 0 | 2 | — | 32049ms | ✅ |
| angr | gcc-m32 -O0 | 0.132 | 0.320 | 0.0% | #2 | 0 | 2 | — | 2141ms | ✅ |
| angr | gcc -O2 | 0.116 | 0.160 | 0.0% | #3 | 0 | 2 | — | 1679ms | ✅ |
| angr | gcc-m32 -O2 | 0.112 | 0.121 | 0.0% | #2 | 0 | 2 | — | 3147ms | ✅ |
| fission | gcc-m32 -O2 | 0.106 | 0.162 | 0.0% | #3 | 0 | 3 | — | 5936ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.009 | 0.0% | #3 | 0 | 0 | — | 1646ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.009 | 0.0% | #4 | 0 | 0 | — | 426ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.101 | 0.005 | 0.0% | #3 | 0 | 0 | — | 381ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.101 | 0.005 | 0.0% | #4 | 0 | 0 | — | 1532ms | ✅ |
| fission | gcc-m32 -O0 | 0.095 | 0.091 | 0.0% | #4 | 1 | 2 | — | 3612ms | ✅ |
| fission | gcc -O0 | 0.085 | 0.128 | 0.0% | #4 | 2 | 2 | — | 7607ms | ✅ |
| revng | gcc -O0 | 0.070 | 0.001 | 0.0% | #5 | 0 | 10 | — | 91908ms | ✅ |
| revng | gcc-m32 -O0 | 0.070 | 0.001 | 0.0% | #5 | 0 | 8 | — | 33616ms | ✅ |
| revng | gcc -O2 | 0.070 | 0.001 | 0.0% | #5 | 0 | 10 | — | 90322ms | ✅ |
| revng | gcc-m32 -O2 | 0.070 | 0.001 | 0.0% | #5 | 0 | 8 | — | 42639ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 222 | 7 | — | 2420ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 155 | 7 | — | 855ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #6 | 220 | 7 | — | 764ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 151 | 7 | — | 2678ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 152ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 174ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 30ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 89ms | ❌ No matching plugins found for  |

### `binary_search`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc-m32 -O0 | 0.934 | 0.438 | 100.0% | #1 | 0 | 3 | — | 26920ms | ✅ |
| angr | gcc -O0 | 0.933 | 0.335 | 100.0% | #1 | 0 | 2 | — | 3121ms | ✅ |
| ghidra | gcc -O2 | 0.894 | 0.239 | 100.0% | #1 | 0 | 5 | — | 22257ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.894 | 0.239 | 100.0% | #1 | 0 | 5 | — | 18849ms | ✅ |
| angr | gcc-m32 -O0 | 0.139 | 0.386 | 0.0% | #2 | 0 | 2 | — | 2221ms | ✅ |
| ghidra | gcc -O0 | 0.114 | 0.242 | 0.0% | #2 | 0 | 3 | — | 31369ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.009 | 0.0% | #2 | 0 | 0 | — | 896ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.006 | 0.0% | #3 | 0 | 0 | — | 459ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.101 | 0.005 | 0.0% | #3 | 0 | 0 | — | 925ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.100 | 0.004 | 0.0% | #2 | 0 | 0 | — | 805ms | ✅ |
| angr | gcc-m32 -O2 | 0.098 | 0.175 | 0.0% | #3 | 0 | 4 | — | 1841ms | ✅ |
| angr | gcc -O2 | 0.096 | 0.160 | 0.0% | #3 | 0 | 4 | — | 2368ms | ✅ |
| revng | gcc-m32 -O0 | 0.070 | 0.002 | 0.0% | #4 | 0 | 8 | — | 35530ms | ✅ |
| revng | gcc -O0 | 0.070 | 0.001 | 0.0% | #4 | 0 | 10 | — | 92376ms | ✅ |
| revng | gcc-m32 -O2 | 0.070 | 0.001 | 0.0% | #4 | 0 | 8 | — | 33285ms | ✅ |
| fission | gcc-m32 -O2 | 0.046 | 0.081 | 0.0% | #5 | 3 | 4 | — | 3395ms | ✅ |
| fission | gcc -O2 | 0.036 | 0.056 | 0.0% | #4 | 6 | 2 | — | 4301ms | ✅ |
| fission | gcc -O0 | 0.035 | 0.051 | 0.0% | #5 | 6 | 2 | — | 13286ms | ✅ |
| fission | gcc-m32 -O0 | 0.033 | 0.034 | 0.0% | #5 | 6 | 2 | — | 8947ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #6 | 157 | 7 | — | 867ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 224 | 7 | — | 975ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #5 | 223 | 7 | — | 979ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 154 | 7 | — | 775ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 34ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 57ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 52ms | ❌ No matching plugins found for  |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 43ms | ❌ No matching plugins found for  |

### `bubble_sort`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.929 | 0.295 | 100.0% | #1 | 0 | 4 | — | 2043ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.915 | 0.152 | 100.0% | #1 | 0 | 4 | — | 18204ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.909 | 0.190 | 100.0% | #1 | 0 | 5 | — | 27443ms | ✅ |
| angr | gcc-m32 -O0 | 0.126 | 0.257 | 0.0% | #2 | 0 | 4 | — | 1814ms | ✅ |
| ghidra | gcc -O0 | 0.117 | 0.167 | 0.0% | #2 | 0 | 4 | — | 23938ms | ✅ |
| angr | gcc -O2 | 0.111 | 0.107 | 0.0% | #1 | 0 | 4 | — | 2643ms | ✅ |
| ghidra | gcc -O2 | 0.103 | 0.131 | 0.0% | #2 | 0 | 5 | — | 30977ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.007 | 0.0% | #3 | 0 | 0 | — | 976ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.006 | 0.0% | #3 | 0 | 0 | — | 464ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.101 | 0.006 | 0.0% | #2 | 0 | 0 | — | 917ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.100 | 0.004 | 0.0% | #3 | 0 | 0 | — | 849ms | ✅ |
| angr | gcc-m32 -O2 | 0.097 | 0.069 | 0.0% | #3 | 0 | 5 | — | 2313ms | ✅ |
| fission | gcc-m32 -O2 | 0.076 | 0.038 | 0.0% | #4 | 2 | 4 | — | 5312ms | ✅ |
| revng | gcc-m32 -O0 | 0.070 | 0.002 | 0.0% | #4 | 0 | 8 | — | 24259ms | ✅ |
| revng | gcc -O0 | 0.070 | 0.001 | 0.0% | #4 | 0 | 10 | — | 89696ms | ✅ |
| revng | gcc-m32 -O2 | 0.070 | 0.001 | 0.0% | #5 | 0 | 8 | — | 46736ms | ✅ |
| fission | gcc -O2 | 0.054 | 0.105 | 0.0% | #4 | 4 | 3 | — | 8755ms | ✅ |
| fission | gcc-m32 -O0 | 0.049 | 0.048 | 0.0% | #5 | 4 | 3 | — | 3180ms | ✅ |
| fission | gcc -O0 | 0.045 | 0.008 | 0.0% | #5 | 4 | 2 | — | 5536ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #6 | 157 | 7 | — | 626ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% | #5 | 223 | 7 | — | 1184ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% | #6 | 154 | 7 | — | 786ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 224 | 7 | — | 971ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 108ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 172ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 90ms | ❌ No matching plugins found for  |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 28ms | ❌ No matching plugins found for  |

### `checksum`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc-m32 -O0 | 0.982 | 0.819 | 100.0% | #1 | 0 | 2 | — | 26030ms | ✅ |
| angr | gcc -O0 | 0.957 | 0.567 | 100.0% | #1 | 0 | 2 | — | 1940ms | ✅ |
| angr | gcc -O2 | 0.912 | 0.125 | 100.0% | #1 | 0 | 2 | — | 1601ms | ✅ |
| angr | gcc-m32 -O2 | 0.909 | 0.095 | 100.0% | #1 | 0 | 2 | — | 1927ms | ✅ |
| fission | gcc -O2 | 0.907 | 0.170 | 100.0% | #2 | 0 | 3 | — | 3036ms | ✅ |
| ghidra | gcc -O2 | 0.903 | 0.129 | 100.0% | #3 | 0 | 3 | — | 26826ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.902 | 0.116 | 100.0% | #2 | 0 | 3 | — | 23620ms | ✅ |
| ghidra | gcc -O0 | 0.150 | 0.668 | 0.0% | #2 | 0 | 2 | — | 31281ms | ✅ |
| angr | gcc-m32 -O0 | 0.150 | 0.598 | 0.0% | #2 | 0 | 2 | — | 1792ms | ✅ |
| fission | gcc-m32 -O2 | 0.102 | 0.122 | 0.0% | #3 | 0 | 3 | — | 3489ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.012 | 0.0% | #3 | 0 | 0 | — | 445ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.012 | 0.0% | #4 | 0 | 0 | — | 469ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.101 | 0.011 | 0.0% | #3 | 0 | 0 | — | 721ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.101 | 0.010 | 0.0% | #4 | 0 | 0 | — | 683ms | ✅ |
| fission | gcc-m32 -O0 | 0.093 | 0.074 | 0.0% | #4 | 1 | 2 | — | 3384ms | ✅ |
| fission | gcc -O0 | 0.082 | 0.103 | 0.0% | #4 | 2 | 2 | — | 4071ms | ✅ |
| revng | gcc -O0 | 0.070 | 0.001 | 0.0% | #5 | 0 | 10 | — | 83931ms | ✅ |
| revng | gcc-m32 -O0 | 0.070 | 0.001 | 0.0% | #5 | 0 | 8 | — | 35326ms | ✅ |
| revng | gcc -O2 | 0.070 | 0.001 | 0.0% | #5 | 0 | 10 | — | 89794ms | ✅ |
| revng | gcc-m32 -O2 | 0.070 | 0.001 | 0.0% | #5 | 0 | 8 | — | 38665ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 227 | 7 | — | 858ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 161 | 7 | — | 892ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #6 | 219 | 7 | — | 946ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 151 | 7 | — | 1151ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 30ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 45ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 29ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 48ms | ❌ No matching plugins found for  |

### `clamp`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc-m32 -O2 | 0.963 | 0.731 | 100.0% | #1 | 0 | 2 | — | 33984ms | ✅ |
| angr | gcc -O0 | 0.961 | 0.708 | 100.0% | #1 | 0 | 2 | — | 3451ms | ✅ |
| angr | gcc-m32 -O0 | 0.961 | 0.705 | 100.0% | #1 | 0 | 2 | — | 3201ms | ✅ |
| angr | gcc -O2 | 0.952 | 0.524 | 100.0% | #1 | 0 | 1 | — | 2102ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.949 | 0.590 | 100.0% | #2 | 0 | 2 | — | 25389ms | ✅ |
| angr | gcc-m32 -O2 | 0.949 | 0.490 | 100.0% | #2 | 0 | 1 | — | 1777ms | ✅ |
| ghidra | gcc -O2 | 0.948 | 0.582 | 100.0% | #2 | 0 | 2 | — | 35117ms | ✅ |
| fission | gcc -O2 | 0.150 | 0.535 | 0.0% | #3 | 0 | 1 | — | 2735ms | ✅ |
| fission | gcc-m32 -O0 | 0.145 | 0.450 | 0.0% | #3 | 0 | 1 | — | 5501ms | ✅ |
| fission | gcc-m32 -O2 | 0.137 | 0.368 | 0.0% | #3 | 0 | 1 | — | 2866ms | ✅ |
| ghidra | gcc -O0 | 0.132 | 0.421 | 0.0% | #2 | 0 | 2 | — | 30443ms | ✅ |
| fission | gcc -O0 | 0.108 | 0.179 | 0.0% | #3 | 0 | 2 | — | 5596ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.006 | 0.0% | #4 | 0 | 0 | — | 404ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.005 | 0.0% | #4 | 0 | 0 | — | 1335ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.101 | 0.005 | 0.0% | #4 | 0 | 0 | — | 1455ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.101 | 0.005 | 0.0% | #4 | 0 | 0 | — | 645ms | ✅ |
| revng | gcc -O0 | 0.070 | 0.001 | 0.0% | #5 | 0 | 10 | — | 91200ms | ✅ |
| revng | gcc-m32 -O0 | 0.070 | 0.001 | 0.0% | #5 | 0 | 8 | — | 38453ms | ✅ |
| revng | gcc -O2 | 0.070 | 0.001 | 0.0% | #5 | 0 | 10 | — | 90944ms | ✅ |
| revng | gcc-m32 -O2 | 0.070 | 0.001 | 0.0% | #5 | 0 | 8 | — | 41849ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 227 | 7 | — | 1881ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #6 | 219 | 7 | — | 746ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 87ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 83ms | ❌ No matching plugins found for  |
| snowman | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | #6 | 161 | 7 | — | 1665ms | ✅ |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 52ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 31ms | ❌ No matching plugins found for  |
| snowman | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | #6 | 151 | 7 | — | 585ms | ✅ |

### `classify_range`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O2 | 0.939 | 0.486 | 100.0% | #1 | 0 | 3 | — | 28483ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.939 | 0.486 | 100.0% | #1 | 0 | 3 | — | 27033ms | ✅ |
| angr | gcc -O0 | 0.918 | 0.182 | 100.0% | #1 | 0 | 2 | — | 1937ms | ✅ |
| angr | gcc-m32 -O0 | 0.916 | 0.157 | 100.0% | #1 | 0 | 2 | — | 1705ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.907 | 0.174 | 100.0% | #2 | 0 | 3 | — | 26649ms | ✅ |
| angr | gcc -O2 | 0.150 | 0.541 | 0.0% | #2 | 0 | 2 | — | 1680ms | ✅ |
| fission | gcc -O2 | 0.141 | 0.513 | 0.0% | #3 | 0 | 3 | — | 3173ms | ✅ |
| angr | gcc-m32 -O2 | 0.140 | 0.401 | 0.0% | #2 | 0 | 1 | — | 1547ms | ✅ |
| fission | gcc-m32 -O2 | 0.133 | 0.433 | 0.0% | #3 | 0 | 3 | — | 3031ms | ✅ |
| ghidra | gcc -O0 | 0.107 | 0.167 | 0.0% | #2 | 0 | 3 | — | 25063ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.009 | 0.0% | #4 | 0 | 0 | — | 419ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.008 | 0.0% | #3 | 0 | 0 | — | 611ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.100 | 0.003 | 0.0% | #3 | 0 | 0 | — | 514ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.100 | 0.003 | 0.0% | #4 | 0 | 0 | — | 618ms | ✅ |
| revng | gcc -O0 | 0.070 | 0.001 | 0.0% | #4 | 0 | 10 | — | 81972ms | ✅ |
| revng | gcc-m32 -O0 | 0.070 | 0.001 | 0.0% | #4 | 0 | 8 | — | 31570ms | ✅ |
| revng | gcc -O2 | 0.070 | 0.001 | 0.0% | #5 | 0 | 10 | — | 93220ms | ✅ |
| revng | gcc-m32 -O2 | 0.070 | 0.001 | 0.0% | #5 | 0 | 8 | — | 35155ms | ✅ |
| fission | gcc -O0 | 0.039 | 0.093 | 0.0% | #5 | 9 | 2 | — | 3932ms | ✅ |
| fission | gcc-m32 -O0 | 0.037 | 0.066 | 0.0% | #5 | 8 | 2 | — | 3328ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 227 | 7 | — | 894ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 161 | 7 | — | 915ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #6 | 219 | 7 | — | 887ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 151 | 7 | — | 708ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 52ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 40ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 53ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 53ms | ❌ No matching plugins found for  |

### `count_bits`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc-m32 -O0 | 0.976 | 0.755 | 100.0% | #1 | 0 | 2 | — | 70267ms | ✅ |
| angr | gcc-m32 -O0 | 0.966 | 0.655 | 100.0% | #2 | 0 | 2 | — | 2383ms | ✅ |
| ghidra | gcc -O2 | 0.961 | 0.609 | 100.0% | #1 | 0 | 2 | — | 70175ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.961 | 0.609 | 100.0% | #1 | 0 | 2 | — | 70116ms | ✅ |
| fission | gcc -O2 | 0.886 | 0.104 | 100.0% | #2 | 1 | 3 | — | 40098ms | ✅ |
| ghidra | gcc -O0 | 0.150 | 0.688 | 0.0% | #1 | 0 | 2 | — | 70250ms | ✅ |
| fission | gcc-m32 -O2 | 0.102 | 0.123 | 0.0% | #2 | 0 | 3 | — | 39865ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.009 | 0.0% | #2 | 0 | 0 | — | 2561ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.008 | 0.0% | #3 | 0 | 0 | — | 2228ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.101 | 0.007 | 0.0% | #3 | 0 | 0 | — | 2658ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.101 | 0.006 | 0.0% | #3 | 0 | 0 | — | 2334ms | ✅ |
| fission | gcc-m32 -O0 | 0.096 | 0.102 | 0.0% | #4 | 1 | 2 | — | 39577ms | ✅ |
| fission | gcc -O0 | 0.086 | 0.135 | 0.0% | #3 | 2 | 2 | — | 39612ms | ✅ |
| revng | gcc -O0 | 0.070 | 0.001 | 0.0% | #4 | 0 | 10 | — | 97666ms | ✅ |
| revng | gcc-m32 -O0 | 0.070 | 0.001 | 0.0% | #5 | 0 | 8 | — | 54999ms | ✅ |
| revng | gcc -O2 | 0.070 | 0.001 | 0.0% | #4 | 0 | 10 | — | 103102ms | ✅ |
| revng | gcc-m32 -O2 | 0.070 | 0.001 | 0.0% | #4 | 0 | 8 | — | 60054ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 227 | 7 | — | 4047ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 161 | 7 | — | 3820ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #5 | 219 | 7 | — | 4152ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 151 | 7 | — | 3645ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 222ms | ❌ No matching plugins found for  |
| angr | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Server error '500 Internal Ser |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 217ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 191ms | ❌ No matching plugins found for  |
| angr | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Server error '500 Internal Ser |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 207ms | ❌ No matching plugins found for  |
| angr | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Server error '500 Internal Ser |

### `factorial`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.970 | 0.702 | 100.0% | #1 | 0 | 1 | — | 3441ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.948 | 0.579 | 100.0% | #1 | 0 | 2 | — | 25963ms | ✅ |
| angr | gcc-m32 -O2 | 0.903 | 0.135 | 100.0% | #1 | 0 | 2 | — | 1690ms | ✅ |
| ghidra | gcc -O2 | 0.901 | 0.212 | 100.0% | #1 | 0 | 3 | — | 27174ms | ✅ |
| angr | gcc-m32 -O0 | 0.150 | 0.548 | 0.0% | #2 | 0 | 1 | — | 3214ms | ✅ |
| ghidra | gcc -O0 | 0.123 | 0.335 | 0.0% | #2 | 0 | 2 | — | 29181ms | ✅ |
| angr | gcc -O2 | 0.114 | 0.239 | 0.0% | #2 | 0 | 2 | — | 1692ms | ✅ |
| radare2 | gcc -O0 | 0.100 | 0.004 | 0.0% | #3 | 0 | 0 | — | 1640ms | ✅ |
| fission | gcc -O2 | 0.100 | 0.244 | 0.0% | #3 | 1 | 2 | — | 2912ms | ✅ |
| radare2 | gcc -O2 | 0.100 | 0.003 | 0.0% | #4 | 0 | 0 | — | 441ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #3 | 0 | 0 | — | 1614ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #2 | 0 | 0 | — | 737ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.094 | 0.136 | 0.0% | #3 | 0 | 3 | — | 22721ms | ✅ |
| fission | gcc-m32 -O0 | 0.085 | 0.050 | 0.0% | #4 | 0 | 3 | — | 7337ms | ✅ |
| fission | gcc-m32 -O2 | 0.078 | 0.022 | 0.0% | #4 | 1 | 2 | — | 5176ms | ✅ |
| revng | gcc -O0 | 0.070 | 0.000 | 0.0% | #4 | 0 | 10 | — | 97000ms | ✅ |
| revng | gcc-m32 -O0 | 0.070 | 0.001 | 0.0% | #5 | 0 | 8 | — | 34736ms | ✅ |
| revng | gcc-m32 -O2 | 0.070 | 0.000 | 0.0% | #5 | 0 | 8 | — | 38813ms | ✅ |
| fission | gcc -O0 | 0.065 | 0.033 | 0.0% | #5 | 2 | 2 | — | 6980ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 157 | 7 | — | 2104ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 29ms | ❌ No matching plugins found for  |
| snowman | gcc -O0 | 0.000 | 0.000 | 0.0% | #6 | 224 | 7 | — | 1692ms | ✅ |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 55ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 37ms | ❌ No matching plugins found for  |
| snowman | gcc -O2 | 0.000 | 0.000 | 0.0% | #5 | 223 | 7 | — | 708ms | ✅ |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 29ms | ❌ No matching plugins found for  |
| snowman | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | #6 | 154 | 7 | — | 894ms | ✅ |

### `fibonacci`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc-m32 -O0 | 0.950 | 0.598 | 100.0% | #1 | 0 | 2 | — | 25362ms | ✅ |
| angr | gcc -O0 | 0.950 | 0.597 | 100.0% | #1 | 0 | 2 | — | 1806ms | ✅ |
| angr | gcc-m32 -O0 | 0.949 | 0.590 | 100.0% | #2 | 0 | 2 | — | 3174ms | ✅ |
| angr | gcc-m32 -O2 | 0.929 | 0.391 | 100.0% | #1 | 0 | 2 | — | 2364ms | ✅ |
| angr | gcc -O2 | 0.922 | 0.325 | 100.0% | #1 | 0 | 2 | — | 3566ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.906 | 0.260 | 100.0% | #2 | 0 | 3 | — | 24035ms | ✅ |
| ghidra | gcc -O2 | 0.902 | 0.218 | 100.0% | #2 | 0 | 3 | — | 29311ms | ✅ |
| fission | gcc-m32 -O0 | 0.128 | 0.477 | 0.0% | #3 | 0 | 3 | — | 5895ms | ✅ |
| ghidra | gcc -O0 | 0.122 | 0.321 | 0.0% | #2 | 0 | 2 | — | 27616ms | ✅ |
| radare2 | gcc -O0 | 0.100 | 0.004 | 0.0% | #3 | 0 | 0 | — | 862ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.100 | 0.004 | 0.0% | #4 | 0 | 0 | — | 1514ms | ✅ |
| radare2 | gcc -O2 | 0.100 | 0.004 | 0.0% | #3 | 0 | 0 | — | 1784ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.100 | 0.004 | 0.0% | #3 | 0 | 0 | — | 802ms | ✅ |
| fission | gcc-m32 -O2 | 0.089 | 0.088 | 0.0% | #4 | 0 | 3 | — | 3872ms | ✅ |
| fission | gcc -O0 | 0.084 | 0.044 | 0.0% | #4 | 0 | 3 | — | 4267ms | ✅ |
| fission | gcc -O2 | 0.083 | 0.172 | 0.0% | #4 | 1 | 3 | — | 7133ms | ✅ |
| revng | gcc-m32 -O0 | 0.070 | 0.001 | 0.0% | #5 | 0 | 8 | — | 31039ms | ✅ |
| revng | gcc -O0 | 0.070 | 0.000 | 0.0% | #5 | 0 | 10 | — | 91497ms | ✅ |
| revng | gcc-m32 -O2 | 0.070 | 0.000 | 0.0% | #5 | 0 | 8 | — | 37755ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 157 | 7 | — | 2025ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 154 | 7 | — | 868ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 49ms | ❌ No matching plugins found for  |
| snowman | gcc -O0 | 0.000 | 0.000 | 0.0% | #6 | 224 | 7 | — | 884ms | ✅ |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 95ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 101ms | ❌ No matching plugins found for  |
| snowman | gcc -O2 | 0.000 | 0.000 | 0.0% | #5 | 223 | 7 | — | 1769ms | ✅ |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 29ms | ❌ No matching plugins found for  |

### `fibonacci_iter`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.971 | 0.711 | 100.0% | #1 | 0 | 2 | — | 1724ms | ✅ |
| angr | gcc-m32 -O0 | 0.971 | 0.709 | 100.0% | #1 | 0 | 2 | — | 1523ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.962 | 0.718 | 100.0% | #2 | 0 | 3 | — | 24971ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.914 | 0.243 | 100.0% | #1 | 0 | 3 | — | 18862ms | ✅ |
| ghidra | gcc -O2 | 0.914 | 0.241 | 100.0% | #1 | 0 | 3 | — | 25763ms | ✅ |
| ghidra | gcc -O0 | 0.138 | 0.480 | 0.0% | #2 | 0 | 3 | — | 27831ms | ✅ |
| angr | gcc-m32 -O2 | 0.126 | 0.262 | 0.0% | #2 | 0 | 2 | — | 1588ms | ✅ |
| angr | gcc -O2 | 0.125 | 0.248 | 0.0% | #2 | 0 | 2 | — | 1891ms | ✅ |
| fission | gcc -O2 | 0.124 | 0.245 | 0.0% | #3 | 0 | 2 | — | 3430ms | ✅ |
| fission | gcc-m32 -O2 | 0.112 | 0.217 | 0.0% | #3 | 0 | 3 | — | 2887ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.008 | 0.0% | #4 | 0 | 0 | — | 772ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.007 | 0.0% | #3 | 0 | 0 | — | 583ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.100 | 0.004 | 0.0% | #3 | 0 | 0 | — | 377ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.100 | 0.003 | 0.0% | #4 | 0 | 0 | — | 729ms | ✅ |
| fission | gcc-m32 -O0 | 0.088 | 0.156 | 0.0% | #4 | 2 | 2 | — | 2884ms | ✅ |
| revng | gcc -O0 | 0.070 | 0.001 | 0.0% | #4 | 0 | 10 | — | 81451ms | ✅ |
| revng | gcc-m32 -O0 | 0.070 | 0.001 | 0.0% | #5 | 0 | 8 | — | 31245ms | ✅ |
| revng | gcc-m32 -O2 | 0.070 | 0.001 | 0.0% | #5 | 0 | 8 | — | 30803ms | ✅ |
| fission | gcc -O0 | 0.062 | 0.176 | 0.0% | #5 | 4 | 2 | — | 4074ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 224 | 7 | — | 824ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 157 | 7 | — | 720ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #5 | 223 | 7 | — | 1026ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 154 | 7 | — | 761ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 52ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 47ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 72ms | ❌ No matching plugins found for  |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 30ms | ❌ No matching plugins found for  |

### `find_pair_value`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc-m32 -O0 | 0.970 | 0.695 | 100.0% | #1 | 0 | 3 | — | 26116ms | ✅ |
| angr | gcc -O0 | 0.929 | 0.289 | 100.0% | #1 | 0 | 2 | — | 2217ms | ✅ |
| angr | gcc -O2 | 0.921 | 0.215 | 100.0% | #1 | 0 | 2 | — | 2149ms | ✅ |
| angr | gcc-m32 -O2 | 0.916 | 0.165 | 100.0% | #1 | 0 | 2 | — | 3406ms | ✅ |
| ghidra | gcc -O2 | 0.911 | 0.212 | 100.0% | #2 | 0 | 4 | — | 27001ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.911 | 0.212 | 100.0% | #2 | 0 | 4 | — | 28163ms | ✅ |
| fission | gcc -O2 | 0.865 | 0.165 | 100.0% | #3 | 3 | 4 | — | 3613ms | ✅ |
| ghidra | gcc -O0 | 0.134 | 0.342 | 0.0% | #2 | 0 | 3 | — | 29546ms | ✅ |
| angr | gcc-m32 -O0 | 0.128 | 0.277 | 0.0% | #2 | 0 | 2 | — | 1907ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.005 | 0.0% | #3 | 0 | 0 | — | 716ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.101 | 0.005 | 0.0% | #3 | 0 | 0 | — | 821ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.005 | 0.0% | #4 | 0 | 0 | — | 1006ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.100 | 0.004 | 0.0% | #3 | 0 | 0 | — | 1548ms | ✅ |
| revng | gcc -O0 | 0.070 | 0.001 | 0.0% | #4 | 0 | 10 | — | 90716ms | ✅ |
| revng | gcc-m32 -O0 | 0.070 | 0.001 | 0.0% | #4 | 0 | 8 | — | 34552ms | ✅ |
| revng | gcc -O2 | 0.070 | 0.001 | 0.0% | #5 | 0 | 10 | — | 93623ms | ✅ |
| revng | gcc-m32 -O2 | 0.070 | 0.001 | 0.0% | #4 | 0 | 8 | — | 41784ms | ✅ |
| fission | gcc-m32 -O0 | 0.068 | 0.099 | 0.0% | #5 | 3 | 2 | — | 3370ms | ✅ |
| fission | gcc-m32 -O2 | 0.058 | 0.099 | 0.0% | #5 | 3 | 4 | — | 6372ms | ✅ |
| fission | gcc -O0 | 0.054 | 0.097 | 0.0% | #5 | 4 | 2 | — | 3741ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 222 | 7 | — | 915ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 155 | 7 | — | 876ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #6 | 220 | 7 | — | 886ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 151 | 7 | — | 1964ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 74ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 59ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 29ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 129ms | ❌ No matching plugins found for  |

### `gcd`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O2 | 0.978 | 0.778 | 100.0% | #1 | 0 | 2 | — | 29476ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.975 | 0.749 | 100.0% | #1 | 0 | 2 | — | 21017ms | ✅ |
| angr | gcc-m32 -O0 | 0.949 | 0.488 | 100.0% | #2 | 0 | 2 | — | 1699ms | ✅ |
| angr | gcc -O0 | 0.947 | 0.467 | 100.0% | #1 | 0 | 2 | — | 1911ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.941 | 0.514 | 100.0% | #1 | 0 | 3 | — | 26943ms | ✅ |
| angr | gcc-m32 -O2 | 0.939 | 0.388 | 100.0% | #2 | 0 | 2 | — | 2875ms | ✅ |
| fission | gcc -O0 | 0.880 | 0.077 | 100.0% | #2 | 2 | 2 | — | 3581ms | ✅ |
| ghidra | gcc -O0 | 0.150 | 0.596 | 0.0% | #3 | 0 | 2 | — | 23524ms | ✅ |
| angr | gcc -O2 | 0.137 | 0.467 | 0.0% | #2 | 0 | 3 | — | 3381ms | ✅ |
| fission | gcc-m32 -O2 | 0.105 | 0.153 | 0.0% | #3 | 0 | 3 | — | 5432ms | ✅ |
| radare2 | gcc -O0 | 0.100 | 0.004 | 0.0% | #4 | 0 | 0 | — | 660ms | ✅ |
| radare2 | gcc -O2 | 0.100 | 0.004 | 0.0% | #3 | 0 | 0 | — | 1379ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.100 | 0.003 | 0.0% | #3 | 0 | 0 | — | 944ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.100 | 0.002 | 0.0% | #4 | 0 | 0 | — | 776ms | ✅ |
| fission | gcc-m32 -O0 | 0.093 | 0.068 | 0.0% | #4 | 1 | 2 | — | 3419ms | ✅ |
| fission | gcc -O2 | 0.085 | 0.129 | 0.0% | #4 | 2 | 2 | — | 6287ms | ✅ |
| revng | gcc -O0 | 0.070 | 0.001 | 0.0% | #5 | 0 | 10 | — | 90899ms | ✅ |
| revng | gcc-m32 -O0 | 0.070 | 0.001 | 0.0% | #5 | 0 | 8 | — | 28035ms | ✅ |
| revng | gcc-m32 -O2 | 0.070 | 0.001 | 0.0% | #5 | 0 | 8 | — | 43392ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 224 | 7 | — | 1125ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 157 | 7 | — | 778ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #5 | 223 | 7 | — | 1962ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 154 | 7 | — | 2417ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 121ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 83ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 46ms | ❌ No matching plugins found for  |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 77ms | ❌ No matching plugins found for  |

### `linear_search`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.971 | 0.707 | 100.0% | #1 | 0 | 2 | — | 1843ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.952 | 0.617 | 100.0% | #1 | 0 | 3 | — | 20461ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.949 | 0.688 | 100.0% | #1 | 0 | 4 | — | 22977ms | ✅ |
| ghidra | gcc -O2 | 0.946 | 0.660 | 100.0% | #1 | 0 | 4 | — | 28041ms | ✅ |
| angr | gcc-m32 -O0 | 0.150 | 0.714 | 0.0% | #2 | 0 | 2 | — | 2158ms | ✅ |
| angr | gcc-m32 -O2 | 0.150 | 0.497 | 0.0% | #2 | 0 | 2 | — | 1735ms | ✅ |
| ghidra | gcc -O0 | 0.127 | 0.371 | 0.0% | #2 | 0 | 3 | — | 25281ms | ✅ |
| angr | gcc -O2 | 0.120 | 0.200 | 0.0% | #2 | 0 | 2 | — | 2118ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.005 | 0.0% | #3 | 0 | 0 | — | 554ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.005 | 0.0% | #3 | 0 | 0 | — | 847ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.100 | 0.002 | 0.0% | #3 | 0 | 0 | — | 488ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.100 | 0.002 | 0.0% | #3 | 0 | 0 | — | 699ms | ✅ |
| revng | gcc -O0 | 0.070 | 0.001 | 0.0% | #4 | 0 | 10 | — | 84946ms | ✅ |
| revng | gcc-m32 -O0 | 0.070 | 0.001 | 0.0% | #4 | 0 | 8 | — | 27806ms | ✅ |
| revng | gcc-m32 -O2 | 0.070 | 0.001 | 0.0% | #4 | 0 | 8 | — | 36135ms | ✅ |
| fission | gcc-m32 -O0 | 0.069 | 0.114 | 0.0% | #5 | 3 | 2 | — | 3471ms | ✅ |
| fission | gcc -O0 | 0.058 | 0.135 | 0.0% | #5 | 4 | 2 | — | 3627ms | ✅ |
| fission | gcc -O2 | 0.053 | 0.154 | 0.0% | #4 | 3 | 4 | — | 3394ms | ✅ |
| fission | gcc-m32 -O2 | 0.046 | 0.080 | 0.0% | #5 | 3 | 4 | — | 3310ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 224 | 7 | — | 1013ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 157 | 7 | — | 1097ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #5 | 223 | 7 | — | 972ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 154 | 7 | — | 801ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 52ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 37ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 62ms | ❌ No matching plugins found for  |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 41ms | ❌ No matching plugins found for  |

### `max`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.975 | 0.752 | 100.0% | #1 | 0 | 1 | — | 1558ms | ✅ |
| angr | gcc -O2 | 0.975 | 0.752 | 100.0% | #1 | 0 | 1 | — | 1844ms | ✅ |
| angr | gcc-m32 -O0 | 0.967 | 0.673 | 100.0% | #1 | 0 | 1 | — | 1568ms | ✅ |
| angr | gcc-m32 -O2 | 0.967 | 0.667 | 100.0% | #1 | 0 | 1 | — | 1679ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.956 | 0.660 | 100.0% | #2 | 0 | 2 | — | 21776ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.955 | 0.654 | 100.0% | #2 | 0 | 2 | — | 22905ms | ✅ |
| ghidra | gcc -O2 | 0.955 | 0.654 | 100.0% | #2 | 0 | 2 | — | 21627ms | ✅ |
| fission | gcc -O2 | 0.150 | 0.579 | 0.0% | #3 | 0 | 1 | — | 2719ms | ✅ |
| fission | gcc-m32 -O0 | 0.142 | 0.419 | 0.0% | #3 | 0 | 1 | — | 2935ms | ✅ |
| fission | gcc-m32 -O2 | 0.142 | 0.419 | 0.0% | #3 | 0 | 1 | — | 2841ms | ✅ |
| fission | gcc -O0 | 0.137 | 0.365 | 0.0% | #2 | 0 | 1 | — | 3022ms | ✅ |
| ghidra | gcc -O0 | 0.133 | 0.431 | 0.0% | #3 | 0 | 2 | — | 25688ms | ✅ |
| radare2 | gcc -O0 | 0.100 | 0.002 | 0.0% | #4 | 0 | 0 | — | 824ms | ✅ |
| radare2 | gcc -O2 | 0.100 | 0.002 | 0.0% | #4 | 0 | 0 | — | 443ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #4 | 0 | 0 | — | 564ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #4 | 0 | 0 | — | 706ms | ✅ |
| revng | gcc-m32 -O0 | 0.070 | 0.001 | 0.0% | #5 | 0 | 8 | — | 26042ms | ✅ |
| revng | gcc -O0 | 0.070 | 0.000 | 0.0% | #5 | 0 | 10 | — | 74879ms | ✅ |
| revng | gcc-m32 -O2 | 0.070 | 0.000 | 0.0% | #5 | 0 | 8 | — | 40224ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 157 | 7 | — | 890ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 154 | 7 | — | 1024ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 29ms | ❌ No matching plugins found for  |
| snowman | gcc -O0 | 0.000 | 0.000 | 0.0% | #6 | 224 | 7 | — | 994ms | ✅ |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 32ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 29ms | ❌ No matching plugins found for  |
| snowman | gcc -O2 | 0.000 | 0.000 | 0.0% | #5 | 223 | 7 | — | 979ms | ✅ |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 78ms | ❌ No matching plugins found for  |

### `pointer_stride_sum`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc-m32 -O0 | 0.967 | 0.674 | 100.0% | #1 | 0 | 2 | — | 23690ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.965 | 0.648 | 100.0% | #1 | 0 | 2 | — | 26031ms | ✅ |
| ghidra | gcc -O2 | 0.961 | 0.609 | 100.0% | #1 | 0 | 2 | — | 26539ms | ✅ |
| angr | gcc-m32 -O0 | 0.951 | 0.511 | 100.0% | #2 | 0 | 2 | — | 2309ms | ✅ |
| angr | gcc -O0 | 0.925 | 0.253 | 100.0% | #1 | 0 | 2 | — | 3392ms | ✅ |
| angr | gcc -O2 | 0.922 | 0.325 | 100.0% | #2 | 0 | 3 | — | 1527ms | ✅ |
| fission | gcc -O2 | 0.922 | 0.319 | 100.0% | #3 | 0 | 3 | — | 3327ms | ✅ |
| angr | gcc-m32 -O2 | 0.919 | 0.195 | 100.0% | #2 | 0 | 2 | — | 1615ms | ✅ |
| ghidra | gcc -O0 | 0.126 | 0.259 | 0.0% | #2 | 0 | 2 | — | 35390ms | ✅ |
| fission | gcc-m32 -O2 | 0.113 | 0.226 | 0.0% | #3 | 0 | 3 | — | 2965ms | ✅ |
| fission | gcc-m32 -O0 | 0.103 | 0.166 | 0.0% | #3 | 1 | 2 | — | 3833ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.006 | 0.0% | #4 | 0 | 0 | — | 448ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.005 | 0.0% | #3 | 0 | 0 | — | 1630ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.101 | 0.004 | 0.0% | #4 | 0 | 0 | — | 681ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.101 | 0.005 | 0.0% | #4 | 0 | 0 | — | 385ms | ✅ |
| fission | gcc -O0 | 0.082 | 0.097 | 0.0% | #4 | 2 | 2 | — | 6134ms | ✅ |
| revng | gcc -O0 | 0.070 | 0.001 | 0.0% | #5 | 0 | 10 | — | 92627ms | ✅ |
| revng | gcc-m32 -O0 | 0.070 | 0.001 | 0.0% | #5 | 0 | 8 | — | 31980ms | ✅ |
| revng | gcc -O2 | 0.070 | 0.001 | 0.0% | #5 | 0 | 10 | — | 85844ms | ✅ |
| revng | gcc-m32 -O2 | 0.070 | 0.001 | 0.0% | #5 | 0 | 8 | — | 34551ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 222 | 7 | — | 2519ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 155 | 7 | — | 943ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #6 | 220 | 7 | — | 757ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 151 | 7 | — | 810ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 115ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 34ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 70ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 55ms | ❌ No matching plugins found for  |

### `power` ⚪ Universally low (harness)
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.928 | 0.283 | 100.0% | #1 | 0 | 2 | — | 1851ms | ✅ |
| ghidra | gcc -O2 | 0.919 | 0.392 | 100.0% | #1 | 0 | 4 | — | 27111ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.139 | 0.492 | 0.0% | #1 | 0 | 3 | — | 25249ms | ✅ |
| ghidra | gcc -O0 | 0.127 | 0.374 | 0.0% | #2 | 0 | 3 | — | 26264ms | ✅ |
| angr | gcc -O2 | 0.119 | 0.195 | 0.0% | #2 | 0 | 2 | — | 1728ms | ✅ |
| angr | gcc-m32 -O0 | 0.108 | 0.176 | 0.0% | #2 | 0 | 3 | — | 2148ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.105 | 0.249 | 0.0% | #1 | 0 | 4 | — | 25052ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.008 | 0.0% | #3 | 0 | 0 | — | 727ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.008 | 0.0% | #3 | 0 | 0 | — | 902ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.100 | 0.004 | 0.0% | #3 | 0 | 0 | — | 867ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.100 | 0.004 | 0.0% | #2 | 0 | 0 | — | 551ms | ✅ |
| angr | gcc-m32 -O2 | 0.099 | 0.088 | 0.0% | #3 | 0 | 3 | — | 2218ms | ✅ |
| fission | gcc-m32 -O0 | 0.090 | 0.039 | 0.0% | #4 | 1 | 2 | — | 3808ms | ✅ |
| fission | gcc -O0 | 0.080 | 0.077 | 0.0% | #4 | 2 | 2 | — | 3753ms | ✅ |
| revng | gcc -O0 | 0.070 | 0.001 | 0.0% | #5 | 0 | 10 | — | 96054ms | ✅ |
| revng | gcc-m32 -O0 | 0.070 | 0.002 | 0.0% | #5 | 0 | 8 | — | 32534ms | ✅ |
| revng | gcc-m32 -O2 | 0.070 | 0.001 | 0.0% | #4 | 0 | 8 | — | 40632ms | ✅ |
| fission | gcc-m32 -O2 | 0.059 | 0.035 | 0.0% | #5 | 1 | 5 | — | 4613ms | ✅ |
| fission | gcc -O2 | 0.050 | 0.081 | 0.0% | #4 | 2 | 5 | — | 3243ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 224 | 7 | — | 808ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 157 | 7 | — | 743ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #5 | 223 | 7 | — | 782ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 154 | 7 | — | 785ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 50ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 51ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 35ms | ❌ No matching plugins found for  |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 48ms | ❌ No matching plugins found for  |

### `process_code`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.966 | 0.661 | 100.0% | #1 | 0 | 1 | — | 1907ms | ✅ |
| angr | gcc-m32 -O0 | 0.966 | 0.660 | 100.0% | #1 | 0 | 1 | — | 2002ms | ✅ |
| ghidra | gcc -O2 | 0.919 | 0.286 | 100.0% | #1 | 0 | 2 | — | 25690ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.919 | 0.286 | 100.0% | #1 | 0 | 2 | — | 23046ms | ✅ |
| angr | gcc-m32 -O2 | 0.906 | 0.260 | 100.0% | #2 | 0 | 3 | — | 1547ms | ✅ |
| angr | gcc -O2 | 0.905 | 0.247 | 100.0% | #2 | 0 | 3 | — | 1726ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.887 | 0.166 | 100.0% | #2 | 0 | 4 | — | 22761ms | ✅ |
| fission | gcc -O2 | 0.133 | 0.331 | 0.0% | #3 | 0 | 1 | — | 3245ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.006 | 0.0% | #4 | 0 | 0 | — | 577ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.005 | 0.0% | #2 | 0 | 0 | — | 770ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.101 | 0.005 | 0.0% | #3 | 0 | 0 | — | 680ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.100 | 0.004 | 0.0% | #3 | 0 | 0 | — | 501ms | ✅ |
| ghidra | gcc -O0 | 0.086 | 0.157 | 0.0% | #3 | 0 | 4 | — | 25314ms | ✅ |
| fission | gcc-m32 -O2 | 0.080 | 0.099 | 0.0% | #4 | 0 | 5 | — | 3459ms | ✅ |
| revng | gcc -O0 | 0.070 | 0.001 | 0.0% | #4 | 0 | 10 | — | 86814ms | ✅ |
| revng | gcc-m32 -O0 | 0.070 | 0.001 | 0.0% | #4 | 0 | 8 | — | 27695ms | ✅ |
| revng | gcc-m32 -O2 | 0.070 | 0.001 | 0.0% | #5 | 0 | 8 | — | 36736ms | ✅ |
| revng | gcc -O2 | 0.070 | 0.000 | 0.0% | #5 | 0 | 10 | — | 112958ms | ✅ |
| fission | gcc-m32 -O0 | 0.033 | 0.054 | 0.0% | #5 | 3 | 5 | — | 3600ms | ✅ |
| fission | gcc -O0 | 0.029 | 0.049 | 0.0% | #5 | 4 | 3 | — | 3685ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 224 | 7 | — | 981ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 157 | 7 | — | 787ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #6 | 223 | 7 | — | 766ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 154 | 7 | — | 827ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 82ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 52ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 33ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 65ms | ❌ No matching plugins found for  |

### `reverse_in_place`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc-m32 -O0 | 0.934 | 0.339 | 100.0% | #1 | 0 | 2 | — | 26005ms | ✅ |
| ghidra | gcc -O2 | 0.912 | 0.221 | 100.0% | #1 | 0 | 3 | — | 30062ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.912 | 0.221 | 100.0% | #1 | 0 | 3 | — | 25146ms | ✅ |
| ghidra | gcc -O0 | 0.132 | 0.323 | 0.0% | #1 | 0 | 2 | — | 27952ms | ✅ |
| angr | gcc -O0 | 0.127 | 0.273 | 0.0% | #2 | 0 | 2 | — | 1822ms | ✅ |
| angr | gcc-m32 -O0 | 0.122 | 0.222 | 0.0% | #2 | 0 | 2 | — | 2017ms | ✅ |
| angr | gcc -O2 | 0.106 | 0.164 | 0.0% | #2 | 0 | 3 | — | 1935ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.006 | 0.0% | #3 | 0 | 0 | — | 579ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.101 | 0.006 | 0.0% | #3 | 0 | 0 | — | 913ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.006 | 0.0% | #3 | 0 | 0 | — | 631ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.101 | 0.005 | 0.0% | #2 | 0 | 0 | — | 481ms | ✅ |
| angr | gcc-m32 -O2 | 0.100 | 0.099 | 0.0% | #3 | 0 | 3 | — | 2171ms | ✅ |
| fission | gcc-m32 -O0 | 0.091 | 0.051 | 0.0% | #4 | 1 | 2 | — | 3809ms | ✅ |
| fission | gcc-m32 -O2 | 0.084 | 0.121 | 0.0% | #4 | 2 | 2 | — | 3537ms | ✅ |
| fission | gcc -O0 | 0.083 | 0.106 | 0.0% | #4 | 2 | 2 | — | 5013ms | ✅ |
| fission | gcc -O2 | 0.075 | 0.131 | 0.0% | #4 | 2 | 3 | — | 3591ms | ✅ |
| revng | gcc -O0 | 0.070 | 0.002 | 0.0% | #5 | 0 | 10 | — | 88450ms | ✅ |
| revng | gcc-m32 -O0 | 0.070 | 0.001 | 0.0% | #5 | 0 | 8 | — | 33893ms | ✅ |
| revng | gcc -O2 | 0.070 | 0.001 | 0.0% | #5 | 0 | 10 | — | 91955ms | ✅ |
| revng | gcc-m32 -O2 | 0.070 | 0.001 | 0.0% | #5 | 0 | 8 | — | 38100ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #6 | 155 | 7 | — | 1134ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 222 | 7 | — | 869ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #6 | 220 | 7 | — | 855ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 151 | 7 | — | 831ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 50ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 44ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 73ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 28ms | ❌ No matching plugins found for  |

### `saturating_add`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.977 | 0.769 | 100.0% | #1 | 0 | 1 | — | 2133ms | ✅ |
| angr | gcc-m32 -O0 | 0.977 | 0.766 | 100.0% | #1 | 0 | 1 | — | 1611ms | ✅ |
| angr | gcc-m32 -O2 | 0.954 | 0.639 | 100.0% | #1 | 0 | 2 | — | 3098ms | ✅ |
| ghidra | gcc -O2 | 0.951 | 0.606 | 100.0% | #1 | 0 | 2 | — | 29947ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.951 | 0.606 | 100.0% | #2 | 0 | 2 | — | 26901ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.905 | 0.246 | 100.0% | #2 | 0 | 3 | — | 27432ms | ✅ |
| angr | gcc -O2 | 0.121 | 0.311 | 0.0% | #2 | 0 | 2 | — | 1666ms | ✅ |
| ghidra | gcc -O0 | 0.105 | 0.252 | 0.0% | #2 | 0 | 3 | — | 30426ms | ✅ |
| fission | gcc -O2 | 0.105 | 0.290 | 0.0% | #3 | 1 | 2 | — | 3151ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.012 | 0.0% | #4 | 0 | 0 | — | 517ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.011 | 0.0% | #3 | 0 | 0 | — | 416ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.101 | 0.006 | 0.0% | #3 | 0 | 0 | — | 567ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.101 | 0.006 | 0.0% | #3 | 0 | 0 | — | 1665ms | ✅ |
| fission | gcc-m32 -O2 | 0.088 | 0.124 | 0.0% | #4 | 1 | 2 | — | 5796ms | ✅ |
| revng | gcc -O0 | 0.070 | 0.001 | 0.0% | #4 | 0 | 10 | — | 86308ms | ✅ |
| revng | gcc-m32 -O0 | 0.070 | 0.001 | 0.0% | #4 | 0 | 8 | — | 31488ms | ✅ |
| revng | gcc -O2 | 0.070 | 0.001 | 0.0% | #5 | 0 | 10 | — | 100256ms | ✅ |
| revng | gcc-m32 -O2 | 0.070 | 0.001 | 0.0% | #5 | 0 | 8 | — | 40056ms | ✅ |
| fission | gcc-m32 -O0 | 0.057 | 0.048 | 0.0% | #5 | 2 | 3 | — | 3699ms | ✅ |
| fission | gcc -O0 | 0.054 | 0.063 | 0.0% | #5 | 3 | 2 | — | 4270ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 227 | 7 | — | 751ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 161 | 7 | — | 794ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #6 | 219 | 7 | — | 809ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 151 | 7 | — | 2684ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 52ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 29ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 54ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 51ms | ❌ No matching plugins found for  |

### `signum`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.950 | 0.503 | 100.0% | #1 | 0 | 1 | — | 1901ms | ✅ |
| angr | gcc-m32 -O0 | 0.949 | 0.488 | 100.0% | #1 | 0 | 1 | — | 1477ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.948 | 0.583 | 100.0% | #1 | 0 | 2 | — | 29593ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.941 | 0.611 | 100.0% | #2 | 0 | 3 | — | 19524ms | ✅ |
| ghidra | gcc -O2 | 0.939 | 0.492 | 100.0% | #1 | 0 | 2 | — | 26895ms | ✅ |
| angr | gcc -O2 | 0.150 | 0.675 | 0.0% | #2 | 0 | 1 | — | 1504ms | ✅ |
| angr | gcc-m32 -O2 | 0.150 | 0.595 | 0.0% | #2 | 0 | 1 | — | 1738ms | ✅ |
| fission | gcc -O2 | 0.149 | 0.489 | 0.0% | #3 | 0 | 1 | — | 2913ms | ✅ |
| ghidra | gcc -O0 | 0.117 | 0.375 | 0.0% | #2 | 0 | 3 | — | 32573ms | ✅ |
| fission | gcc-m32 -O0 | 0.112 | 0.321 | 0.0% | #3 | 0 | 3 | — | 2892ms | ✅ |
| radare2 | gcc -O0 | 0.100 | 0.004 | 0.0% | #3 | 0 | 0 | — | 709ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.100 | 0.004 | 0.0% | #3 | 0 | 0 | — | 432ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.100 | 0.003 | 0.0% | #4 | 0 | 0 | — | 706ms | ✅ |
| radare2 | gcc -O2 | 0.100 | 0.003 | 0.0% | #4 | 0 | 0 | — | 617ms | ✅ |
| fission | gcc-m32 -O2 | 0.089 | 0.094 | 0.0% | #4 | 0 | 3 | — | 2999ms | ✅ |
| fission | gcc -O0 | 0.086 | 0.057 | 0.0% | #4 | 0 | 3 | — | 3165ms | ✅ |
| revng | gcc -O0 | 0.070 | 0.000 | 0.0% | #5 | 0 | 10 | — | 88199ms | ✅ |
| revng | gcc-m32 -O0 | 0.070 | 0.000 | 0.0% | #5 | 0 | 8 | — | 27923ms | ✅ |
| revng | gcc -O2 | 0.070 | 0.000 | 0.0% | #5 | 0 | 10 | — | 92542ms | ✅ |
| revng | gcc-m32 -O2 | 0.070 | 0.000 | 0.0% | #5 | 0 | 8 | — | 44691ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 227 | 7 | — | 833ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 161 | 7 | — | 739ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #6 | 219 | 7 | — | 901ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 70ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 34ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 32ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 39ms | ❌ No matching plugins found for  |
| snowman | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | #6 | 151 | 7 | — | 727ms | ✅ |

### `sum_array`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc-m32 -O0 | 0.983 | 0.833 | 100.0% | #1 | 0 | 2 | — | 23892ms | ✅ |
| angr | gcc -O0 | 0.946 | 0.455 | 100.0% | #1 | 0 | 2 | — | 3237ms | ✅ |
| fission | gcc -O2 | 0.926 | 0.357 | 100.0% | #1 | 0 | 3 | — | 3315ms | ✅ |
| angr | gcc -O2 | 0.917 | 0.171 | 100.0% | #2 | 0 | 2 | — | 1693ms | ✅ |
| angr | gcc-m32 -O2 | 0.912 | 0.122 | 100.0% | #1 | 0 | 2 | — | 2639ms | ✅ |
| ghidra | gcc -O2 | 0.907 | 0.171 | 100.0% | #3 | 0 | 3 | — | 28388ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.907 | 0.171 | 100.0% | #2 | 0 | 3 | — | 26984ms | ✅ |
| ghidra | gcc -O0 | 0.150 | 0.648 | 0.0% | #2 | 0 | 2 | — | 31213ms | ✅ |
| angr | gcc-m32 -O0 | 0.150 | 0.543 | 0.0% | #2 | 0 | 2 | — | 1905ms | ✅ |
| fission | gcc-m32 -O2 | 0.102 | 0.124 | 0.0% | #3 | 0 | 3 | — | 3803ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.008 | 0.0% | #3 | 0 | 0 | — | 1750ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.008 | 0.0% | #4 | 0 | 0 | — | 882ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.101 | 0.005 | 0.0% | #3 | 0 | 0 | — | 645ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.101 | 0.005 | 0.0% | #4 | 0 | 0 | — | 417ms | ✅ |
| fission | gcc-m32 -O0 | 0.098 | 0.120 | 0.0% | #4 | 1 | 2 | — | 3064ms | ✅ |
| fission | gcc -O0 | 0.086 | 0.145 | 0.0% | #4 | 2 | 2 | — | 5830ms | ✅ |
| revng | gcc -O0 | 0.070 | 0.001 | 0.0% | #5 | 0 | 10 | — | 91966ms | ✅ |
| revng | gcc-m32 -O0 | 0.070 | 0.001 | 0.0% | #5 | 0 | 8 | — | 31174ms | ✅ |
| revng | gcc -O2 | 0.070 | 0.001 | 0.0% | #5 | 0 | 10 | — | 94613ms | ✅ |
| revng | gcc-m32 -O2 | 0.070 | 0.001 | 0.0% | #5 | 0 | 8 | — | 42955ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 222 | 7 | — | 1437ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 155 | 7 | — | 819ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #6 | 220 | 7 | — | 765ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 151 | 7 | — | 821ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 54ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 48ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 56ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 79ms | ❌ No matching plugins found for  |

---

## Overfitting Analysis

Functions where **all** decompilers scored below 0.3 are marked as objectively hard.
Functions where **only Fission** scored below 0.3 are marked as quality gaps.

**Fission quality gaps (14):** `clamp`, `signum`, `classify_range`, `saturating_add`, `reverse_in_place`, `fibonacci`, `fibonacci_iter`, `max`, `bubble_sort`, `linear_search`, `binary_search`, `factorial`, `power`, `process_code`