# Fission Benchmark Report

> [!WARNING]
> **ARCHIVED LEGACY RESULT** — This file was originally measured before
> the provenance envelope was introduced.  Original run timing and toolchain
> version information are not available.  Official validity is **unverified**.

**Measured at:** unknown (legacy)
**Rendered at:** 2026-07-11 05:15 UTC
**Corpus:** `dev`
**Functions evaluated:** 21

---

## ⚠️ LEGACY / UNVERIFIED

> Fission 84/84 rows clean (100.0%), all-backend 501/588 (85.2%).
> Provenance incomplete — this result predates the envelope format.
> Do not use these numbers as an official comparison.

## Summary — Correctness Score

> Readability metrics are recorded as unvalidated raw proxies. They are not combined into a final readability score until the human validation study is complete.

| Decompiler | Attempted | Output Valid | Output Fail | Compile Fail | Runtime Fail | Timeout | No Wrapper | Avg Correctness | Avg Similarity | Semantic Pass |
| ---|---|---|---|---|---|---|---|---|---|--- |
| **ghidra** | 84 | 84 | 0 | — | — | — | — | 0.704 | 0.427 | 70.2% |
| **angr** | 84 | 81 | 3 | — | — | — | — | 0.623 | 0.399 | 60.5% |
| **fission** | 84 | 84 | 0 | — | — | — | — | 0.183 | 0.164 | 8.3% |
| **radare2** | 84 | 84 | 0 | — | — | — | — | 0.101 | 0.005 | 0.0% |
| **snowman** | 84 | 84 | 0 | — | — | — | — | 0.100 | 0.001 | 0.0% |
| **revng** | 84 | 84 | 0 | — | — | — | — | 0.100 | 0.001 | 0.0% |
| ~~retdec~~ ⛔ | 84 | 0 | 84 | — | — | — | — | — | — | — |

---

## Per-Function Results

### `accumulate_pairs`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc-m32 -O0 | 0.979 | 0.787 | 100.0% | #1 | 0 | 2 | — | 24185ms | ✅ |
| angr | gcc -O0 | 0.933 | 0.331 | 100.0% | #2 | 0 | 2 | — | 3713ms | ✅ |
| fission | gcc -O2 | 0.914 | 0.139 | 100.0% | #2 | 2 | 2 | — | 3661ms | ✅ |
| ghidra | gcc -O2 | 0.912 | 0.120 | 100.0% | #3 | 0 | 3 | — | 29833ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.912 | 0.120 | 100.0% | #3 | 0 | 3 | — | 30391ms | ✅ |
| ghidra | gcc -O0 | 0.150 | 0.517 | 0.0% | #1 | 0 | 2 | — | 32049ms | ✅ |
| angr | gcc-m32 -O0 | 0.132 | 0.320 | 0.0% | #2 | 0 | 2 | — | 2141ms | ✅ |
| fission | gcc-m32 -O2 | 0.116 | 0.162 | 0.0% | #1 | 0 | 3 | — | 5936ms | ✅ |
| angr | gcc -O2 | 0.116 | 0.160 | 0.0% | #1 | 0 | 2 | — | 1679ms | ✅ |
| fission | gcc -O0 | 0.113 | 0.128 | 0.0% | #3 | 2 | 2 | — | 7607ms | ✅ |
| angr | gcc-m32 -O2 | 0.112 | 0.121 | 0.0% | #2 | 0 | 2 | — | 3147ms | ✅ |
| fission | gcc-m32 -O0 | 0.109 | 0.091 | 0.0% | #3 | 1 | 2 | — | 3612ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.009 | 0.0% | #4 | 0 | 0 | — | 1646ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.009 | 0.0% | #4 | 0 | 0 | — | 426ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.101 | 0.005 | 0.0% | #4 | 0 | 0 | — | 381ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.101 | 0.005 | 0.0% | #4 | 0 | 0 | — | 1532ms | ✅ |
| snowman | gcc -O0 | 0.100 | 0.001 | 0.0% | #6 | 222 | 7 | — | 2420ms | ✅ |
| revng | gcc -O0 | 0.100 | 0.001 | 0.0% | #5 | 0 | 10 | — | 91908ms | ✅ |
| snowman | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #5 | 155 | 7 | — | 855ms | ✅ |
| revng | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #6 | 0 | 8 | — | 33616ms | ✅ |
| snowman | gcc -O2 | 0.100 | 0.001 | 0.0% | #5 | 220 | 7 | — | 764ms | ✅ |
| revng | gcc -O2 | 0.100 | 0.001 | 0.0% | #6 | 0 | 10 | — | 90322ms | ✅ |
| snowman | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #5 | 151 | 7 | — | 2678ms | ✅ |
| revng | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #6 | 0 | 8 | — | 42639ms | ✅ |
| retdec | gcc -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 152ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 174ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 30ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 89ms | ❌ No matching plugins found for  |

### `binary_search`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc-m32 -O0 | 0.944 | 0.438 | 100.0% | #1 | 0 | 3 | — | 26920ms | ✅ |
| angr | gcc -O0 | 0.933 | 0.335 | 100.0% | #1 | 0 | 2 | — | 3121ms | ✅ |
| ghidra | gcc -O2 | 0.924 | 0.239 | 100.0% | #1 | 0 | 5 | — | 22257ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.924 | 0.239 | 100.0% | #1 | 0 | 5 | — | 18849ms | ✅ |
| angr | gcc-m32 -O0 | 0.139 | 0.386 | 0.0% | #2 | 0 | 2 | — | 2221ms | ✅ |
| ghidra | gcc -O0 | 0.124 | 0.242 | 0.0% | #2 | 0 | 3 | — | 31369ms | ✅ |
| angr | gcc-m32 -O2 | 0.117 | 0.175 | 0.0% | #2 | 0 | 4 | — | 1841ms | ✅ |
| angr | gcc -O2 | 0.116 | 0.160 | 0.0% | #2 | 0 | 4 | — | 2368ms | ✅ |
| fission | gcc-m32 -O2 | 0.108 | 0.081 | 0.0% | #3 | 3 | 4 | — | 3395ms | ✅ |
| fission | gcc -O2 | 0.106 | 0.056 | 0.0% | #3 | 6 | 2 | — | 4301ms | ✅ |
| fission | gcc -O0 | 0.105 | 0.051 | 0.0% | #3 | 6 | 2 | — | 13286ms | ✅ |
| fission | gcc-m32 -O0 | 0.103 | 0.034 | 0.0% | #3 | 6 | 2 | — | 8947ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.009 | 0.0% | #4 | 0 | 0 | — | 896ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.006 | 0.0% | #4 | 0 | 0 | — | 459ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.101 | 0.005 | 0.0% | #4 | 0 | 0 | — | 925ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.100 | 0.004 | 0.0% | #4 | 0 | 0 | — | 805ms | ✅ |
| snowman | gcc-m32 -O0 | 0.100 | 0.002 | 0.0% | #6 | 157 | 7 | — | 867ms | ✅ |
| revng | gcc-m32 -O0 | 0.100 | 0.002 | 0.0% | #5 | 0 | 8 | — | 35530ms | ✅ |
| snowman | gcc -O0 | 0.100 | 0.001 | 0.0% | #6 | 224 | 7 | — | 975ms | ✅ |
| revng | gcc -O0 | 0.100 | 0.001 | 0.0% | #5 | 0 | 10 | — | 92376ms | ✅ |
| snowman | gcc -O2 | 0.100 | 0.001 | 0.0% | #5 | 223 | 7 | — | 979ms | ✅ |
| snowman | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #5 | 154 | 7 | — | 775ms | ✅ |
| revng | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #6 | 0 | 8 | — | 33285ms | ✅ |
| retdec | gcc -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 34ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 57ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 52ms | ❌ No matching plugins found for  |
| revng | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ✅ |
| retdec | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 43ms | ❌ No matching plugins found for  |

### `bubble_sort`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.929 | 0.295 | 100.0% | #1 | 0 | 4 | — | 2043ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.919 | 0.190 | 100.0% | #1 | 0 | 5 | — | 27443ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.915 | 0.152 | 100.0% | #2 | 0 | 4 | — | 18204ms | ✅ |
| angr | gcc-m32 -O0 | 0.126 | 0.257 | 0.0% | #1 | 0 | 4 | — | 1814ms | ✅ |
| ghidra | gcc -O0 | 0.117 | 0.167 | 0.0% | #2 | 0 | 4 | — | 23938ms | ✅ |
| ghidra | gcc -O2 | 0.113 | 0.131 | 0.0% | #1 | 0 | 5 | — | 30977ms | ✅ |
| angr | gcc -O2 | 0.111 | 0.107 | 0.0% | #2 | 0 | 4 | — | 2643ms | ✅ |
| fission | gcc -O2 | 0.111 | 0.105 | 0.0% | #3 | 4 | 3 | — | 8755ms | ✅ |
| angr | gcc-m32 -O2 | 0.107 | 0.069 | 0.0% | #2 | 0 | 5 | — | 2313ms | ✅ |
| fission | gcc-m32 -O0 | 0.105 | 0.048 | 0.0% | #3 | 4 | 3 | — | 3180ms | ✅ |
| fission | gcc-m32 -O2 | 0.104 | 0.038 | 0.0% | #3 | 2 | 4 | — | 5312ms | ✅ |
| fission | gcc -O0 | 0.101 | 0.008 | 0.0% | #3 | 4 | 2 | — | 5536ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.007 | 0.0% | #4 | 0 | 0 | — | 976ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.006 | 0.0% | #4 | 0 | 0 | — | 464ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.101 | 0.006 | 0.0% | #4 | 0 | 0 | — | 917ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.100 | 0.004 | 0.0% | #4 | 0 | 0 | — | 849ms | ✅ |
| snowman | gcc-m32 -O0 | 0.100 | 0.002 | 0.0% | #6 | 157 | 7 | — | 626ms | ✅ |
| revng | gcc-m32 -O0 | 0.100 | 0.002 | 0.0% | #5 | 0 | 8 | — | 24259ms | ✅ |
| snowman | gcc -O2 | 0.100 | 0.002 | 0.0% | #5 | 223 | 7 | — | 1184ms | ✅ |
| snowman | gcc-m32 -O2 | 0.100 | 0.002 | 0.0% | #5 | 154 | 7 | — | 786ms | ✅ |
| snowman | gcc -O0 | 0.100 | 0.001 | 0.0% | #6 | 224 | 7 | — | 971ms | ✅ |
| revng | gcc -O0 | 0.100 | 0.001 | 0.0% | #5 | 0 | 10 | — | 89696ms | ✅ |
| revng | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #6 | 0 | 8 | — | 46736ms | ✅ |
| retdec | gcc -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 108ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 172ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 90ms | ❌ No matching plugins found for  |
| revng | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ✅ |
| retdec | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 28ms | ❌ No matching plugins found for  |

### `checksum`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc-m32 -O0 | 0.982 | 0.819 | 100.0% | #1 | 0 | 2 | — | 26030ms | ✅ |
| angr | gcc -O0 | 0.957 | 0.567 | 100.0% | #2 | 0 | 2 | — | 1940ms | ✅ |
| fission | gcc -O2 | 0.917 | 0.170 | 100.0% | #1 | 0 | 3 | — | 3036ms | ✅ |
| ghidra | gcc -O2 | 0.913 | 0.129 | 100.0% | #2 | 0 | 3 | — | 26826ms | ✅ |
| angr | gcc -O2 | 0.912 | 0.125 | 100.0% | #3 | 0 | 2 | — | 1601ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.912 | 0.116 | 100.0% | #2 | 0 | 3 | — | 23620ms | ✅ |
| angr | gcc-m32 -O2 | 0.909 | 0.095 | 100.0% | #3 | 0 | 2 | — | 1927ms | ✅ |
| ghidra | gcc -O0 | 0.150 | 0.668 | 0.0% | #1 | 0 | 2 | — | 31281ms | ✅ |
| angr | gcc-m32 -O0 | 0.150 | 0.598 | 0.0% | #2 | 0 | 2 | — | 1792ms | ✅ |
| fission | gcc-m32 -O2 | 0.112 | 0.122 | 0.0% | #1 | 0 | 3 | — | 3489ms | ✅ |
| fission | gcc -O0 | 0.110 | 0.103 | 0.0% | #3 | 2 | 2 | — | 4071ms | ✅ |
| fission | gcc-m32 -O0 | 0.107 | 0.074 | 0.0% | #3 | 1 | 2 | — | 3384ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.012 | 0.0% | #4 | 0 | 0 | — | 445ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.012 | 0.0% | #4 | 0 | 0 | — | 469ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.101 | 0.011 | 0.0% | #4 | 0 | 0 | — | 721ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.101 | 0.010 | 0.0% | #4 | 0 | 0 | — | 683ms | ✅ |
| snowman | gcc -O0 | 0.100 | 0.001 | 0.0% | #5 | 227 | 7 | — | 858ms | ✅ |
| revng | gcc -O0 | 0.100 | 0.001 | 0.0% | #6 | 0 | 10 | — | 83931ms | ✅ |
| snowman | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #6 | 161 | 7 | — | 892ms | ✅ |
| revng | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #5 | 0 | 8 | — | 35326ms | ✅ |
| snowman | gcc -O2 | 0.100 | 0.001 | 0.0% | #5 | 219 | 7 | — | 946ms | ✅ |
| revng | gcc -O2 | 0.100 | 0.001 | 0.0% | #6 | 0 | 10 | — | 89794ms | ✅ |
| snowman | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #5 | 151 | 7 | — | 1151ms | ✅ |
| revng | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #6 | 0 | 8 | — | 38665ms | ✅ |
| retdec | gcc -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 30ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 45ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 29ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 48ms | ❌ No matching plugins found for  |

### `clamp` 🔴 Fission-only gap
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc-m32 -O2 | 0.973 | 0.731 | 100.0% | #1 | 0 | 2 | — | 33984ms | ✅ |
| angr | gcc -O0 | 0.971 | 0.708 | 100.0% | #1 | 0 | 2 | — | 3451ms | ✅ |
| angr | gcc-m32 -O0 | 0.971 | 0.705 | 100.0% | #1 | 0 | 2 | — | 3201ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.959 | 0.590 | 100.0% | #2 | 0 | 2 | — | 25389ms | ✅ |
| ghidra | gcc -O2 | 0.958 | 0.582 | 100.0% | #1 | 0 | 2 | — | 35117ms | ✅ |
| angr | gcc -O2 | 0.952 | 0.524 | 100.0% | #3 | 0 | 1 | — | 2102ms | ✅ |
| angr | gcc-m32 -O2 | 0.949 | 0.490 | 100.0% | #2 | 0 | 1 | — | 1777ms | ✅ |
| fission | gcc -O2 | 0.150 | 0.535 | 0.0% | #2 | 0 | 1 | — | 2735ms | ✅ |
| fission | gcc-m32 -O0 | 0.145 | 0.450 | 0.0% | #3 | 0 | 1 | — | 5501ms | ✅ |
| ghidra | gcc -O0 | 0.142 | 0.421 | 0.0% | #2 | 0 | 2 | — | 30443ms | ✅ |
| fission | gcc-m32 -O2 | 0.137 | 0.368 | 0.0% | #3 | 0 | 1 | — | 2866ms | ✅ |
| fission | gcc -O0 | 0.118 | 0.179 | 0.0% | #3 | 0 | 2 | — | 5596ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.006 | 0.0% | #4 | 0 | 0 | — | 404ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.005 | 0.0% | #4 | 0 | 0 | — | 1335ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.101 | 0.005 | 0.0% | #4 | 0 | 0 | — | 1455ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.101 | 0.005 | 0.0% | #4 | 0 | 0 | — | 645ms | ✅ |
| snowman | gcc -O0 | 0.100 | 0.001 | 0.0% | #5 | 227 | 7 | — | 1881ms | ✅ |
| revng | gcc -O0 | 0.100 | 0.001 | 0.0% | #6 | 0 | 10 | — | 91200ms | ✅ |
| revng | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #5 | 0 | 8 | — | 38453ms | ✅ |
| snowman | gcc -O2 | 0.100 | 0.001 | 0.0% | #5 | 219 | 7 | — | 746ms | ✅ |
| revng | gcc -O2 | 0.100 | 0.001 | 0.0% | #6 | 0 | 10 | — | 90944ms | ✅ |
| revng | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #5 | 0 | 8 | — | 41849ms | ✅ |
| retdec | gcc -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 87ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 83ms | ❌ No matching plugins found for  |
| snowman | gcc-m32 -O0 | 0.100 | 0.000 | 0.0% | #6 | 161 | 7 | — | 1665ms | ✅ |
| retdec | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 52ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 31ms | ❌ No matching plugins found for  |
| snowman | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | #6 | 151 | 7 | — | 585ms | ✅ |

### `classify_range`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O2 | 0.949 | 0.486 | 100.0% | #3 | 0 | 3 | — | 28483ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.949 | 0.486 | 100.0% | #1 | 0 | 3 | — | 27033ms | ✅ |
| angr | gcc -O0 | 0.918 | 0.182 | 100.0% | #1 | 0 | 2 | — | 1937ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.917 | 0.174 | 100.0% | #1 | 0 | 3 | — | 26649ms | ✅ |
| angr | gcc-m32 -O0 | 0.916 | 0.157 | 100.0% | #2 | 0 | 2 | — | 1705ms | ✅ |
| fission | gcc -O2 | 0.150 | 0.513 | 0.0% | #2 | 0 | 3 | — | 3173ms | ✅ |
| angr | gcc -O2 | 0.150 | 0.541 | 0.0% | #1 | 0 | 2 | — | 1680ms | ✅ |
| fission | gcc-m32 -O2 | 0.143 | 0.433 | 0.0% | #2 | 0 | 3 | — | 3031ms | ✅ |
| angr | gcc-m32 -O2 | 0.140 | 0.401 | 0.0% | #3 | 0 | 1 | — | 1547ms | ✅ |
| ghidra | gcc -O0 | 0.117 | 0.167 | 0.0% | #2 | 0 | 3 | — | 25063ms | ✅ |
| fission | gcc -O0 | 0.109 | 0.093 | 0.0% | #3 | 9 | 2 | — | 3932ms | ✅ |
| fission | gcc-m32 -O0 | 0.107 | 0.066 | 0.0% | #3 | 8 | 2 | — | 3328ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.009 | 0.0% | #4 | 0 | 0 | — | 419ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.008 | 0.0% | #4 | 0 | 0 | — | 611ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.100 | 0.003 | 0.0% | #4 | 0 | 0 | — | 514ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.100 | 0.003 | 0.0% | #4 | 0 | 0 | — | 618ms | ✅ |
| snowman | gcc -O0 | 0.100 | 0.001 | 0.0% | #5 | 227 | 7 | — | 894ms | ✅ |
| revng | gcc -O0 | 0.100 | 0.001 | 0.0% | #6 | 0 | 10 | — | 81972ms | ✅ |
| snowman | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #6 | 161 | 7 | — | 915ms | ✅ |
| revng | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #5 | 0 | 8 | — | 31570ms | ✅ |
| snowman | gcc -O2 | 0.100 | 0.001 | 0.0% | #6 | 219 | 7 | — | 887ms | ✅ |
| revng | gcc -O2 | 0.100 | 0.001 | 0.0% | #5 | 0 | 10 | — | 93220ms | ✅ |
| snowman | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #5 | 151 | 7 | — | 708ms | ✅ |
| revng | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #6 | 0 | 8 | — | 35155ms | ✅ |
| retdec | gcc -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 52ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 40ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 53ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 53ms | ❌ No matching plugins found for  |

### `count_bits`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc-m32 -O0 | 0.976 | 0.755 | 100.0% | #1 | 0 | 2 | — | 70267ms | ✅ |
| angr | gcc-m32 -O0 | 0.966 | 0.655 | 100.0% | #2 | 0 | 2 | — | 2383ms | ✅ |
| ghidra | gcc -O2 | 0.961 | 0.609 | 100.0% | #1 | 0 | 2 | — | 70175ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.961 | 0.609 | 100.0% | #1 | 0 | 2 | — | 70116ms | ✅ |
| fission | gcc -O2 | 0.910 | 0.104 | 100.0% | #2 | 1 | 3 | — | 40098ms | ✅ |
| ghidra | gcc -O0 | 0.150 | 0.688 | 0.0% | #1 | 0 | 2 | — | 70250ms | ✅ |
| fission | gcc -O0 | 0.114 | 0.135 | 0.0% | #2 | 2 | 2 | — | 39612ms | ✅ |
| fission | gcc-m32 -O2 | 0.112 | 0.123 | 0.0% | #2 | 0 | 3 | — | 39865ms | ✅ |
| fission | gcc-m32 -O0 | 0.110 | 0.102 | 0.0% | #3 | 1 | 2 | — | 39577ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.009 | 0.0% | #3 | 0 | 0 | — | 2561ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.008 | 0.0% | #3 | 0 | 0 | — | 2228ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.101 | 0.007 | 0.0% | #4 | 0 | 0 | — | 2658ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.101 | 0.006 | 0.0% | #3 | 0 | 0 | — | 2334ms | ✅ |
| snowman | gcc -O0 | 0.100 | 0.001 | 0.0% | #4 | 227 | 7 | — | 4047ms | ✅ |
| revng | gcc -O0 | 0.100 | 0.001 | 0.0% | #5 | 0 | 10 | — | 97666ms | ✅ |
| snowman | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #6 | 161 | 7 | — | 3820ms | ✅ |
| revng | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #5 | 0 | 8 | — | 54999ms | ✅ |
| snowman | gcc -O2 | 0.100 | 0.001 | 0.0% | #4 | 219 | 7 | — | 4152ms | ✅ |
| revng | gcc -O2 | 0.100 | 0.001 | 0.0% | #5 | 0 | 10 | — | 103102ms | ✅ |
| snowman | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #4 | 151 | 7 | — | 3645ms | ✅ |
| revng | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #5 | 0 | 8 | — | 60054ms | ✅ |
| retdec | gcc -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 222ms | ❌ No matching plugins found for  |
| angr | gcc -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Server error '500 Internal Ser |
| retdec | gcc-m32 -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 217ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 191ms | ❌ No matching plugins found for  |
| angr | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Server error '500 Internal Ser |
| retdec | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 207ms | ❌ No matching plugins found for  |
| angr | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Server error '500 Internal Ser |

### `factorial`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.970 | 0.702 | 100.0% | #1 | 0 | 1 | — | 3441ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.958 | 0.579 | 100.0% | #1 | 0 | 2 | — | 25963ms | ✅ |
| ghidra | gcc -O2 | 0.921 | 0.212 | 100.0% | #3 | 0 | 3 | — | 27174ms | ✅ |
| angr | gcc-m32 -O2 | 0.913 | 0.135 | 100.0% | #2 | 0 | 2 | — | 1690ms | ✅ |
| angr | gcc-m32 -O0 | 0.150 | 0.548 | 0.0% | #2 | 0 | 1 | — | 3214ms | ✅ |
| ghidra | gcc -O0 | 0.134 | 0.335 | 0.0% | #2 | 0 | 2 | — | 29181ms | ✅ |
| fission | gcc -O2 | 0.124 | 0.244 | 0.0% | #1 | 1 | 2 | — | 2912ms | ✅ |
| angr | gcc -O2 | 0.124 | 0.239 | 0.0% | #2 | 0 | 2 | — | 1692ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.114 | 0.136 | 0.0% | #1 | 0 | 3 | — | 22721ms | ✅ |
| fission | gcc-m32 -O0 | 0.105 | 0.050 | 0.0% | #3 | 0 | 3 | — | 7337ms | ✅ |
| fission | gcc -O0 | 0.103 | 0.033 | 0.0% | #3 | 2 | 2 | — | 6980ms | ✅ |
| fission | gcc-m32 -O2 | 0.102 | 0.022 | 0.0% | #3 | 1 | 2 | — | 5176ms | ✅ |
| radare2 | gcc -O0 | 0.100 | 0.004 | 0.0% | #4 | 0 | 0 | — | 1640ms | ✅ |
| radare2 | gcc -O2 | 0.100 | 0.003 | 0.0% | #4 | 0 | 0 | — | 441ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #4 | 0 | 0 | — | 1614ms | ✅ |
| snowman | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #5 | 157 | 7 | — | 2104ms | ✅ |
| revng | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #6 | 0 | 8 | — | 34736ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #4 | 0 | 0 | — | 737ms | ✅ |
| retdec | gcc -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 29ms | ❌ No matching plugins found for  |
| snowman | gcc -O0 | 0.100 | 0.000 | 0.0% | #5 | 224 | 7 | — | 1692ms | ✅ |
| revng | gcc -O0 | 0.100 | 0.000 | 0.0% | #6 | 0 | 10 | — | 97000ms | ✅ |
| retdec | gcc-m32 -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 55ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 37ms | ❌ No matching plugins found for  |
| snowman | gcc -O2 | 0.100 | 0.000 | 0.0% | #5 | 223 | 7 | — | 708ms | ✅ |
| revng | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ✅ |
| retdec | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 29ms | ❌ No matching plugins found for  |
| snowman | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | #5 | 154 | 7 | — | 894ms | ✅ |
| revng | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | #6 | 0 | 8 | — | 38813ms | ✅ |

### `fibonacci` 🔴 Fission-only gap
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc-m32 -O0 | 0.960 | 0.598 | 100.0% | #1 | 0 | 2 | — | 25362ms | ✅ |
| angr | gcc -O0 | 0.960 | 0.597 | 100.0% | #1 | 0 | 2 | — | 1806ms | ✅ |
| angr | gcc-m32 -O0 | 0.959 | 0.590 | 100.0% | #2 | 0 | 2 | — | 3174ms | ✅ |
| angr | gcc-m32 -O2 | 0.939 | 0.391 | 100.0% | #1 | 0 | 2 | — | 2364ms | ✅ |
| angr | gcc -O2 | 0.932 | 0.325 | 100.0% | #1 | 0 | 2 | — | 3566ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.926 | 0.260 | 100.0% | #2 | 0 | 3 | — | 24035ms | ✅ |
| ghidra | gcc -O2 | 0.922 | 0.218 | 100.0% | #2 | 0 | 3 | — | 29311ms | ✅ |
| fission | gcc-m32 -O0 | 0.148 | 0.477 | 0.0% | #3 | 0 | 3 | — | 5895ms | ✅ |
| ghidra | gcc -O0 | 0.132 | 0.321 | 0.0% | #2 | 0 | 2 | — | 27616ms | ✅ |
| fission | gcc -O2 | 0.117 | 0.172 | 0.0% | #3 | 1 | 3 | — | 7133ms | ✅ |
| fission | gcc-m32 -O2 | 0.109 | 0.088 | 0.0% | #3 | 0 | 3 | — | 3872ms | ✅ |
| fission | gcc -O0 | 0.104 | 0.044 | 0.0% | #3 | 0 | 3 | — | 4267ms | ✅ |
| radare2 | gcc -O0 | 0.100 | 0.004 | 0.0% | #4 | 0 | 0 | — | 862ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.100 | 0.004 | 0.0% | #4 | 0 | 0 | — | 1514ms | ✅ |
| radare2 | gcc -O2 | 0.100 | 0.004 | 0.0% | #4 | 0 | 0 | — | 1784ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.100 | 0.004 | 0.0% | #4 | 0 | 0 | — | 802ms | ✅ |
| snowman | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #5 | 157 | 7 | — | 2025ms | ✅ |
| revng | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #6 | 0 | 8 | — | 31039ms | ✅ |
| snowman | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #5 | 154 | 7 | — | 868ms | ✅ |
| retdec | gcc -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 49ms | ❌ No matching plugins found for  |
| snowman | gcc -O0 | 0.100 | 0.000 | 0.0% | #5 | 224 | 7 | — | 884ms | ✅ |
| revng | gcc -O0 | 0.100 | 0.000 | 0.0% | #6 | 0 | 10 | — | 91497ms | ✅ |
| retdec | gcc-m32 -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 95ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 101ms | ❌ No matching plugins found for  |
| snowman | gcc -O2 | 0.100 | 0.000 | 0.0% | #5 | 223 | 7 | — | 1769ms | ✅ |
| revng | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ✅ |
| retdec | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 29ms | ❌ No matching plugins found for  |
| revng | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | #6 | 0 | 8 | — | 37755ms | ✅ |

### `fibonacci_iter`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc-m32 -O0 | 0.972 | 0.718 | 100.0% | #1 | 0 | 3 | — | 24971ms | ✅ |
| angr | gcc -O0 | 0.971 | 0.711 | 100.0% | #1 | 0 | 2 | — | 1724ms | ✅ |
| angr | gcc-m32 -O0 | 0.971 | 0.709 | 100.0% | #2 | 0 | 2 | — | 1523ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.924 | 0.243 | 100.0% | #2 | 0 | 3 | — | 18862ms | ✅ |
| ghidra | gcc -O2 | 0.924 | 0.241 | 100.0% | #3 | 0 | 3 | — | 25763ms | ✅ |
| ghidra | gcc -O0 | 0.148 | 0.480 | 0.0% | #2 | 0 | 3 | — | 27831ms | ✅ |
| angr | gcc-m32 -O2 | 0.126 | 0.262 | 0.0% | #1 | 0 | 2 | — | 1588ms | ✅ |
| angr | gcc -O2 | 0.125 | 0.248 | 0.0% | #1 | 0 | 2 | — | 1891ms | ✅ |
| fission | gcc -O2 | 0.124 | 0.245 | 0.0% | #2 | 0 | 2 | — | 3430ms | ✅ |
| fission | gcc-m32 -O2 | 0.122 | 0.217 | 0.0% | #3 | 0 | 3 | — | 2887ms | ✅ |
| fission | gcc -O0 | 0.118 | 0.176 | 0.0% | #3 | 4 | 2 | — | 4074ms | ✅ |
| fission | gcc-m32 -O0 | 0.116 | 0.156 | 0.0% | #3 | 2 | 2 | — | 2884ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.008 | 0.0% | #4 | 0 | 0 | — | 772ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.007 | 0.0% | #4 | 0 | 0 | — | 583ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.100 | 0.004 | 0.0% | #4 | 0 | 0 | — | 377ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.100 | 0.003 | 0.0% | #4 | 0 | 0 | — | 729ms | ✅ |
| snowman | gcc -O0 | 0.100 | 0.001 | 0.0% | #5 | 224 | 7 | — | 824ms | ✅ |
| revng | gcc -O0 | 0.100 | 0.001 | 0.0% | #6 | 0 | 10 | — | 81451ms | ✅ |
| snowman | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #5 | 157 | 7 | — | 720ms | ✅ |
| revng | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #6 | 0 | 8 | — | 31245ms | ✅ |
| snowman | gcc -O2 | 0.100 | 0.001 | 0.0% | #5 | 223 | 7 | — | 1026ms | ✅ |
| snowman | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #5 | 154 | 7 | — | 761ms | ✅ |
| revng | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #6 | 0 | 8 | — | 30803ms | ✅ |
| retdec | gcc -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 52ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 47ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 72ms | ❌ No matching plugins found for  |
| revng | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ✅ |
| retdec | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 30ms | ❌ No matching plugins found for  |

### `find_pair_value`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc-m32 -O0 | 0.970 | 0.695 | 100.0% | #1 | 0 | 3 | — | 26116ms | ✅ |
| angr | gcc -O0 | 0.929 | 0.289 | 100.0% | #2 | 0 | 2 | — | 2217ms | ✅ |
| angr | gcc -O2 | 0.921 | 0.215 | 100.0% | #1 | 0 | 2 | — | 2149ms | ✅ |
| ghidra | gcc -O2 | 0.921 | 0.212 | 100.0% | #2 | 0 | 4 | — | 27001ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.921 | 0.212 | 100.0% | #1 | 0 | 4 | — | 28163ms | ✅ |
| fission | gcc -O2 | 0.916 | 0.165 | 100.0% | #3 | 3 | 4 | — | 3613ms | ✅ |
| angr | gcc-m32 -O2 | 0.916 | 0.165 | 100.0% | #2 | 0 | 2 | — | 3406ms | ✅ |
| ghidra | gcc -O0 | 0.134 | 0.342 | 0.0% | #1 | 0 | 3 | — | 29546ms | ✅ |
| angr | gcc-m32 -O0 | 0.128 | 0.277 | 0.0% | #2 | 0 | 2 | — | 1907ms | ✅ |
| fission | gcc-m32 -O0 | 0.110 | 0.099 | 0.0% | #3 | 3 | 2 | — | 3370ms | ✅ |
| fission | gcc-m32 -O2 | 0.110 | 0.099 | 0.0% | #3 | 3 | 4 | — | 6372ms | ✅ |
| fission | gcc -O0 | 0.110 | 0.097 | 0.0% | #3 | 4 | 2 | — | 3741ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.005 | 0.0% | #4 | 0 | 0 | — | 716ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.101 | 0.005 | 0.0% | #4 | 0 | 0 | — | 821ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.005 | 0.0% | #4 | 0 | 0 | — | 1006ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.100 | 0.004 | 0.0% | #4 | 0 | 0 | — | 1548ms | ✅ |
| snowman | gcc -O0 | 0.100 | 0.001 | 0.0% | #6 | 222 | 7 | — | 915ms | ✅ |
| revng | gcc -O0 | 0.100 | 0.001 | 0.0% | #5 | 0 | 10 | — | 90716ms | ✅ |
| snowman | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #5 | 155 | 7 | — | 876ms | ✅ |
| revng | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #6 | 0 | 8 | — | 34552ms | ✅ |
| snowman | gcc -O2 | 0.100 | 0.001 | 0.0% | #5 | 220 | 7 | — | 886ms | ✅ |
| revng | gcc -O2 | 0.100 | 0.001 | 0.0% | #6 | 0 | 10 | — | 93623ms | ✅ |
| snowman | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #5 | 151 | 7 | — | 1964ms | ✅ |
| revng | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #6 | 0 | 8 | — | 41784ms | ✅ |
| retdec | gcc -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 74ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 59ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 29ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 129ms | ❌ No matching plugins found for  |

### `gcd`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O2 | 0.978 | 0.778 | 100.0% | #1 | 0 | 2 | — | 29476ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.975 | 0.749 | 100.0% | #1 | 0 | 2 | — | 21017ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.951 | 0.514 | 100.0% | #1 | 0 | 3 | — | 26943ms | ✅ |
| angr | gcc-m32 -O0 | 0.949 | 0.488 | 100.0% | #2 | 0 | 2 | — | 1699ms | ✅ |
| angr | gcc -O0 | 0.947 | 0.467 | 100.0% | #2 | 0 | 2 | — | 1911ms | ✅ |
| angr | gcc-m32 -O2 | 0.939 | 0.388 | 100.0% | #2 | 0 | 2 | — | 2875ms | ✅ |
| fission | gcc -O0 | 0.908 | 0.077 | 100.0% | #3 | 2 | 2 | — | 3581ms | ✅ |
| ghidra | gcc -O0 | 0.150 | 0.596 | 0.0% | #1 | 0 | 2 | — | 23524ms | ✅ |
| angr | gcc -O2 | 0.147 | 0.467 | 0.0% | #2 | 0 | 3 | — | 3381ms | ✅ |
| fission | gcc-m32 -O2 | 0.115 | 0.153 | 0.0% | #3 | 0 | 3 | — | 5432ms | ✅ |
| fission | gcc -O2 | 0.113 | 0.129 | 0.0% | #3 | 2 | 2 | — | 6287ms | ✅ |
| fission | gcc-m32 -O0 | 0.107 | 0.068 | 0.0% | #3 | 1 | 2 | — | 3419ms | ✅ |
| radare2 | gcc -O0 | 0.100 | 0.004 | 0.0% | #4 | 0 | 0 | — | 660ms | ✅ |
| radare2 | gcc -O2 | 0.100 | 0.004 | 0.0% | #4 | 0 | 0 | — | 1379ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.100 | 0.003 | 0.0% | #4 | 0 | 0 | — | 944ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.100 | 0.002 | 0.0% | #4 | 0 | 0 | — | 776ms | ✅ |
| snowman | gcc -O0 | 0.100 | 0.001 | 0.0% | #5 | 224 | 7 | — | 1125ms | ✅ |
| revng | gcc -O0 | 0.100 | 0.001 | 0.0% | #6 | 0 | 10 | — | 90899ms | ✅ |
| snowman | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #6 | 157 | 7 | — | 778ms | ✅ |
| revng | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #5 | 0 | 8 | — | 28035ms | ✅ |
| snowman | gcc -O2 | 0.100 | 0.001 | 0.0% | #5 | 223 | 7 | — | 1962ms | ✅ |
| snowman | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #5 | 154 | 7 | — | 2417ms | ✅ |
| revng | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #6 | 0 | 8 | — | 43392ms | ✅ |
| retdec | gcc -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 121ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 83ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 46ms | ❌ No matching plugins found for  |
| revng | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ✅ |
| retdec | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 77ms | ❌ No matching plugins found for  |

### `linear_search`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.971 | 0.707 | 100.0% | #1 | 0 | 2 | — | 1843ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.969 | 0.688 | 100.0% | #1 | 0 | 4 | — | 22977ms | ✅ |
| ghidra | gcc -O2 | 0.966 | 0.660 | 100.0% | #1 | 0 | 4 | — | 28041ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.962 | 0.617 | 100.0% | #2 | 0 | 3 | — | 20461ms | ✅ |
| angr | gcc-m32 -O0 | 0.150 | 0.714 | 0.0% | #1 | 0 | 2 | — | 2158ms | ✅ |
| angr | gcc-m32 -O2 | 0.150 | 0.497 | 0.0% | #2 | 0 | 2 | — | 1735ms | ✅ |
| ghidra | gcc -O0 | 0.137 | 0.371 | 0.0% | #2 | 0 | 3 | — | 25281ms | ✅ |
| angr | gcc -O2 | 0.120 | 0.200 | 0.0% | #2 | 0 | 2 | — | 2118ms | ✅ |
| fission | gcc -O2 | 0.115 | 0.154 | 0.0% | #3 | 3 | 4 | — | 3394ms | ✅ |
| fission | gcc -O0 | 0.114 | 0.135 | 0.0% | #3 | 4 | 2 | — | 3627ms | ✅ |
| fission | gcc-m32 -O0 | 0.111 | 0.114 | 0.0% | #3 | 3 | 2 | — | 3471ms | ✅ |
| fission | gcc-m32 -O2 | 0.108 | 0.080 | 0.0% | #3 | 3 | 4 | — | 3310ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.005 | 0.0% | #4 | 0 | 0 | — | 554ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.005 | 0.0% | #4 | 0 | 0 | — | 847ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.100 | 0.002 | 0.0% | #4 | 0 | 0 | — | 488ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.100 | 0.002 | 0.0% | #4 | 0 | 0 | — | 699ms | ✅ |
| snowman | gcc -O0 | 0.100 | 0.001 | 0.0% | #5 | 224 | 7 | — | 1013ms | ✅ |
| revng | gcc -O0 | 0.100 | 0.001 | 0.0% | #6 | 0 | 10 | — | 84946ms | ✅ |
| snowman | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #5 | 157 | 7 | — | 1097ms | ✅ |
| revng | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #6 | 0 | 8 | — | 27806ms | ✅ |
| snowman | gcc -O2 | 0.100 | 0.001 | 0.0% | #5 | 223 | 7 | — | 972ms | ✅ |
| snowman | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #5 | 154 | 7 | — | 801ms | ✅ |
| revng | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #6 | 0 | 8 | — | 36135ms | ✅ |
| retdec | gcc -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 52ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 37ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 62ms | ❌ No matching plugins found for  |
| revng | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ✅ |
| retdec | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 41ms | ❌ No matching plugins found for  |

### `max` 🔴 Fission-only gap
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.975 | 0.752 | 100.0% | #1 | 0 | 1 | — | 1558ms | ✅ |
| angr | gcc -O2 | 0.975 | 0.752 | 100.0% | #1 | 0 | 1 | — | 1844ms | ✅ |
| angr | gcc-m32 -O0 | 0.967 | 0.673 | 100.0% | #1 | 0 | 1 | — | 1568ms | ✅ |
| angr | gcc-m32 -O2 | 0.967 | 0.667 | 100.0% | #1 | 0 | 1 | — | 1679ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.966 | 0.660 | 100.0% | #2 | 0 | 2 | — | 21776ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.965 | 0.654 | 100.0% | #2 | 0 | 2 | — | 22905ms | ✅ |
| ghidra | gcc -O2 | 0.965 | 0.654 | 100.0% | #2 | 0 | 2 | — | 21627ms | ✅ |
| fission | gcc -O2 | 0.150 | 0.579 | 0.0% | #3 | 0 | 1 | — | 2719ms | ✅ |
| ghidra | gcc -O0 | 0.143 | 0.431 | 0.0% | #2 | 0 | 2 | — | 25688ms | ✅ |
| fission | gcc-m32 -O0 | 0.142 | 0.419 | 0.0% | #3 | 0 | 1 | — | 2935ms | ✅ |
| fission | gcc-m32 -O2 | 0.142 | 0.419 | 0.0% | #3 | 0 | 1 | — | 2841ms | ✅ |
| fission | gcc -O0 | 0.137 | 0.365 | 0.0% | #3 | 0 | 1 | — | 3022ms | ✅ |
| radare2 | gcc -O0 | 0.100 | 0.002 | 0.0% | #4 | 0 | 0 | — | 824ms | ✅ |
| radare2 | gcc -O2 | 0.100 | 0.002 | 0.0% | #4 | 0 | 0 | — | 443ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #4 | 0 | 0 | — | 564ms | ✅ |
| snowman | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #5 | 157 | 7 | — | 890ms | ✅ |
| revng | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #6 | 0 | 8 | — | 26042ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #4 | 0 | 0 | — | 706ms | ✅ |
| snowman | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #5 | 154 | 7 | — | 1024ms | ✅ |
| retdec | gcc -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 29ms | ❌ No matching plugins found for  |
| snowman | gcc -O0 | 0.100 | 0.000 | 0.0% | #5 | 224 | 7 | — | 994ms | ✅ |
| revng | gcc -O0 | 0.100 | 0.000 | 0.0% | #6 | 0 | 10 | — | 74879ms | ✅ |
| retdec | gcc-m32 -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 32ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 29ms | ❌ No matching plugins found for  |
| snowman | gcc -O2 | 0.100 | 0.000 | 0.0% | #5 | 223 | 7 | — | 979ms | ✅ |
| revng | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ✅ |
| retdec | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 78ms | ❌ No matching plugins found for  |
| revng | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | #6 | 0 | 8 | — | 40224ms | ✅ |

### `pointer_stride_sum`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc-m32 -O0 | 0.967 | 0.674 | 100.0% | #1 | 0 | 2 | — | 23690ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.965 | 0.648 | 100.0% | #1 | 0 | 2 | — | 26031ms | ✅ |
| ghidra | gcc -O2 | 0.961 | 0.609 | 100.0% | #1 | 0 | 2 | — | 26539ms | ✅ |
| angr | gcc-m32 -O0 | 0.951 | 0.511 | 100.0% | #2 | 0 | 2 | — | 2309ms | ✅ |
| angr | gcc -O2 | 0.932 | 0.325 | 100.0% | #2 | 0 | 3 | — | 1527ms | ✅ |
| fission | gcc -O2 | 0.932 | 0.319 | 100.0% | #3 | 0 | 3 | — | 3327ms | ✅ |
| angr | gcc -O0 | 0.925 | 0.253 | 100.0% | #2 | 0 | 2 | — | 3392ms | ✅ |
| angr | gcc-m32 -O2 | 0.919 | 0.195 | 100.0% | #3 | 0 | 2 | — | 1615ms | ✅ |
| ghidra | gcc -O0 | 0.126 | 0.259 | 0.0% | #1 | 0 | 2 | — | 35390ms | ✅ |
| fission | gcc-m32 -O2 | 0.123 | 0.226 | 0.0% | #2 | 0 | 3 | — | 2965ms | ✅ |
| fission | gcc-m32 -O0 | 0.117 | 0.166 | 0.0% | #3 | 1 | 2 | — | 3833ms | ✅ |
| fission | gcc -O0 | 0.110 | 0.097 | 0.0% | #3 | 2 | 2 | — | 6134ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.006 | 0.0% | #4 | 0 | 0 | — | 448ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.005 | 0.0% | #4 | 0 | 0 | — | 1630ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.101 | 0.004 | 0.0% | #4 | 0 | 0 | — | 681ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.101 | 0.005 | 0.0% | #4 | 0 | 0 | — | 385ms | ✅ |
| snowman | gcc -O0 | 0.100 | 0.001 | 0.0% | #5 | 222 | 7 | — | 2519ms | ✅ |
| revng | gcc -O0 | 0.100 | 0.001 | 0.0% | #6 | 0 | 10 | — | 92627ms | ✅ |
| snowman | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #5 | 155 | 7 | — | 943ms | ✅ |
| revng | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #6 | 0 | 8 | — | 31980ms | ✅ |
| snowman | gcc -O2 | 0.100 | 0.001 | 0.0% | #5 | 220 | 7 | — | 757ms | ✅ |
| revng | gcc -O2 | 0.100 | 0.001 | 0.0% | #6 | 0 | 10 | — | 85844ms | ✅ |
| snowman | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #5 | 151 | 7 | — | 810ms | ✅ |
| revng | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #6 | 0 | 8 | — | 34551ms | ✅ |
| retdec | gcc -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 115ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 34ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 70ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 55ms | ❌ No matching plugins found for  |

### `power` ⚪ Universally low (harness)
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O2 | 0.939 | 0.392 | 100.0% | #1 | 0 | 4 | — | 27111ms | ✅ |
| angr | gcc -O0 | 0.928 | 0.283 | 100.0% | #2 | 0 | 2 | — | 1851ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.149 | 0.492 | 0.0% | #1 | 0 | 3 | — | 25249ms | ✅ |
| ghidra | gcc -O0 | 0.137 | 0.374 | 0.0% | #1 | 0 | 3 | — | 26264ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.125 | 0.249 | 0.0% | #1 | 0 | 4 | — | 25052ms | ✅ |
| angr | gcc -O2 | 0.119 | 0.195 | 0.0% | #2 | 0 | 2 | — | 1728ms | ✅ |
| angr | gcc-m32 -O0 | 0.118 | 0.176 | 0.0% | #2 | 0 | 3 | — | 2148ms | ✅ |
| angr | gcc-m32 -O2 | 0.109 | 0.088 | 0.0% | #2 | 0 | 3 | — | 2218ms | ✅ |
| fission | gcc -O2 | 0.108 | 0.081 | 0.0% | #3 | 2 | 5 | — | 3243ms | ✅ |
| fission | gcc -O0 | 0.108 | 0.077 | 0.0% | #3 | 2 | 2 | — | 3753ms | ✅ |
| fission | gcc-m32 -O0 | 0.104 | 0.039 | 0.0% | #3 | 1 | 2 | — | 3808ms | ✅ |
| fission | gcc-m32 -O2 | 0.103 | 0.035 | 0.0% | #3 | 1 | 5 | — | 4613ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.008 | 0.0% | #4 | 0 | 0 | — | 727ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.008 | 0.0% | #4 | 0 | 0 | — | 902ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.100 | 0.004 | 0.0% | #4 | 0 | 0 | — | 867ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.100 | 0.004 | 0.0% | #4 | 0 | 0 | — | 551ms | ✅ |
| revng | gcc-m32 -O0 | 0.100 | 0.002 | 0.0% | #5 | 0 | 8 | — | 32534ms | ✅ |
| snowman | gcc -O0 | 0.100 | 0.001 | 0.0% | #6 | 224 | 7 | — | 808ms | ✅ |
| revng | gcc -O0 | 0.100 | 0.001 | 0.0% | #5 | 0 | 10 | — | 96054ms | ✅ |
| snowman | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #6 | 157 | 7 | — | 743ms | ✅ |
| snowman | gcc -O2 | 0.100 | 0.001 | 0.0% | #5 | 223 | 7 | — | 782ms | ✅ |
| snowman | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #5 | 154 | 7 | — | 785ms | ✅ |
| revng | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #6 | 0 | 8 | — | 40632ms | ✅ |
| retdec | gcc -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 50ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 51ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 35ms | ❌ No matching plugins found for  |
| revng | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ✅ |
| retdec | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 48ms | ❌ No matching plugins found for  |

### `process_code`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.966 | 0.661 | 100.0% | #1 | 0 | 1 | — | 1907ms | ✅ |
| angr | gcc-m32 -O0 | 0.966 | 0.660 | 100.0% | #1 | 0 | 1 | — | 2002ms | ✅ |
| ghidra | gcc -O2 | 0.929 | 0.286 | 100.0% | #2 | 0 | 2 | — | 25690ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.929 | 0.286 | 100.0% | #1 | 0 | 2 | — | 23046ms | ✅ |
| angr | gcc-m32 -O2 | 0.926 | 0.260 | 100.0% | #2 | 0 | 3 | — | 1547ms | ✅ |
| angr | gcc -O2 | 0.925 | 0.247 | 100.0% | #3 | 0 | 3 | — | 1726ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.917 | 0.166 | 100.0% | #2 | 0 | 4 | — | 22761ms | ✅ |
| fission | gcc -O2 | 0.133 | 0.331 | 0.0% | #1 | 0 | 1 | — | 3245ms | ✅ |
| ghidra | gcc -O0 | 0.116 | 0.157 | 0.0% | #2 | 0 | 4 | — | 25314ms | ✅ |
| fission | gcc-m32 -O2 | 0.110 | 0.099 | 0.0% | #3 | 0 | 5 | — | 3459ms | ✅ |
| fission | gcc-m32 -O0 | 0.105 | 0.054 | 0.0% | #3 | 3 | 5 | — | 3600ms | ✅ |
| fission | gcc -O0 | 0.105 | 0.049 | 0.0% | #3 | 4 | 3 | — | 3685ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.006 | 0.0% | #4 | 0 | 0 | — | 577ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.005 | 0.0% | #4 | 0 | 0 | — | 770ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.101 | 0.005 | 0.0% | #4 | 0 | 0 | — | 680ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.100 | 0.004 | 0.0% | #4 | 0 | 0 | — | 501ms | ✅ |
| snowman | gcc -O0 | 0.100 | 0.001 | 0.0% | #5 | 224 | 7 | — | 981ms | ✅ |
| revng | gcc -O0 | 0.100 | 0.001 | 0.0% | #6 | 0 | 10 | — | 86814ms | ✅ |
| snowman | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #6 | 157 | 7 | — | 787ms | ✅ |
| revng | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #5 | 0 | 8 | — | 27695ms | ✅ |
| snowman | gcc -O2 | 0.100 | 0.001 | 0.0% | #5 | 223 | 7 | — | 766ms | ✅ |
| snowman | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #5 | 154 | 7 | — | 827ms | ✅ |
| revng | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #6 | 0 | 8 | — | 36736ms | ✅ |
| retdec | gcc -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 82ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 52ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 33ms | ❌ No matching plugins found for  |
| revng | gcc -O2 | 0.100 | 0.000 | 0.0% | #6 | 0 | 10 | — | 112958ms | ✅ |
| retdec | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 65ms | ❌ No matching plugins found for  |

### `reverse_in_place`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc-m32 -O0 | 0.934 | 0.339 | 100.0% | #1 | 0 | 2 | — | 26005ms | ✅ |
| ghidra | gcc -O2 | 0.922 | 0.221 | 100.0% | #1 | 0 | 3 | — | 30062ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.922 | 0.221 | 100.0% | #1 | 0 | 3 | — | 25146ms | ✅ |
| ghidra | gcc -O0 | 0.132 | 0.323 | 0.0% | #1 | 0 | 2 | — | 27952ms | ✅ |
| angr | gcc -O0 | 0.127 | 0.273 | 0.0% | #2 | 0 | 2 | — | 1822ms | ✅ |
| angr | gcc-m32 -O0 | 0.122 | 0.222 | 0.0% | #2 | 0 | 2 | — | 2017ms | ✅ |
| angr | gcc -O2 | 0.116 | 0.164 | 0.0% | #2 | 0 | 3 | — | 1935ms | ✅ |
| fission | gcc -O2 | 0.113 | 0.131 | 0.0% | #3 | 2 | 3 | — | 3591ms | ✅ |
| fission | gcc-m32 -O2 | 0.112 | 0.121 | 0.0% | #2 | 2 | 2 | — | 3537ms | ✅ |
| fission | gcc -O0 | 0.111 | 0.106 | 0.0% | #3 | 2 | 2 | — | 5013ms | ✅ |
| angr | gcc-m32 -O2 | 0.110 | 0.099 | 0.0% | #3 | 0 | 3 | — | 2171ms | ✅ |
| fission | gcc-m32 -O0 | 0.105 | 0.051 | 0.0% | #3 | 1 | 2 | — | 3809ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.006 | 0.0% | #4 | 0 | 0 | — | 579ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.101 | 0.006 | 0.0% | #4 | 0 | 0 | — | 913ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.006 | 0.0% | #4 | 0 | 0 | — | 631ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.101 | 0.005 | 0.0% | #4 | 0 | 0 | — | 481ms | ✅ |
| revng | gcc -O0 | 0.100 | 0.002 | 0.0% | #5 | 0 | 10 | — | 88450ms | ✅ |
| snowman | gcc-m32 -O0 | 0.100 | 0.002 | 0.0% | #5 | 155 | 7 | — | 1134ms | ✅ |
| snowman | gcc -O0 | 0.100 | 0.001 | 0.0% | #6 | 222 | 7 | — | 869ms | ✅ |
| revng | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #6 | 0 | 8 | — | 33893ms | ✅ |
| snowman | gcc -O2 | 0.100 | 0.001 | 0.0% | #5 | 220 | 7 | — | 855ms | ✅ |
| revng | gcc -O2 | 0.100 | 0.001 | 0.0% | #6 | 0 | 10 | — | 91955ms | ✅ |
| snowman | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #5 | 151 | 7 | — | 831ms | ✅ |
| revng | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #6 | 0 | 8 | — | 38100ms | ✅ |
| retdec | gcc -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 50ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 44ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 73ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 28ms | ❌ No matching plugins found for  |

### `saturating_add`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.977 | 0.769 | 100.0% | #1 | 0 | 1 | — | 2133ms | ✅ |
| angr | gcc-m32 -O0 | 0.977 | 0.766 | 100.0% | #1 | 0 | 1 | — | 1611ms | ✅ |
| angr | gcc-m32 -O2 | 0.964 | 0.639 | 100.0% | #1 | 0 | 2 | — | 3098ms | ✅ |
| ghidra | gcc -O2 | 0.961 | 0.606 | 100.0% | #1 | 0 | 2 | — | 29947ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.961 | 0.606 | 100.0% | #2 | 0 | 2 | — | 26901ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.925 | 0.246 | 100.0% | #2 | 0 | 3 | — | 27432ms | ✅ |
| angr | gcc -O2 | 0.131 | 0.311 | 0.0% | #2 | 0 | 2 | — | 1666ms | ✅ |
| fission | gcc -O2 | 0.129 | 0.290 | 0.0% | #3 | 1 | 2 | — | 3151ms | ✅ |
| ghidra | gcc -O0 | 0.125 | 0.252 | 0.0% | #2 | 0 | 3 | — | 30426ms | ✅ |
| fission | gcc-m32 -O2 | 0.112 | 0.124 | 0.0% | #3 | 1 | 2 | — | 5796ms | ✅ |
| fission | gcc -O0 | 0.106 | 0.063 | 0.0% | #3 | 3 | 2 | — | 4270ms | ✅ |
| fission | gcc-m32 -O0 | 0.105 | 0.048 | 0.0% | #3 | 2 | 3 | — | 3699ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.012 | 0.0% | #4 | 0 | 0 | — | 517ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.011 | 0.0% | #4 | 0 | 0 | — | 416ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.101 | 0.006 | 0.0% | #4 | 0 | 0 | — | 567ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.101 | 0.006 | 0.0% | #4 | 0 | 0 | — | 1665ms | ✅ |
| snowman | gcc -O0 | 0.100 | 0.001 | 0.0% | #5 | 227 | 7 | — | 751ms | ✅ |
| revng | gcc -O0 | 0.100 | 0.001 | 0.0% | #6 | 0 | 10 | — | 86308ms | ✅ |
| snowman | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #6 | 161 | 7 | — | 794ms | ✅ |
| revng | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #5 | 0 | 8 | — | 31488ms | ✅ |
| snowman | gcc -O2 | 0.100 | 0.001 | 0.0% | #6 | 219 | 7 | — | 809ms | ✅ |
| revng | gcc -O2 | 0.100 | 0.001 | 0.0% | #5 | 0 | 10 | — | 100256ms | ✅ |
| snowman | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #5 | 151 | 7 | — | 2684ms | ✅ |
| revng | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #6 | 0 | 8 | — | 40056ms | ✅ |
| retdec | gcc -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 52ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 29ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 54ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 51ms | ❌ No matching plugins found for  |

### `signum`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc-m32 -O0 | 0.961 | 0.611 | 100.0% | #1 | 0 | 3 | — | 19524ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.958 | 0.583 | 100.0% | #2 | 0 | 2 | — | 29593ms | ✅ |
| angr | gcc -O0 | 0.950 | 0.503 | 100.0% | #1 | 0 | 1 | — | 1901ms | ✅ |
| ghidra | gcc -O2 | 0.949 | 0.492 | 100.0% | #2 | 0 | 2 | — | 26895ms | ✅ |
| angr | gcc-m32 -O0 | 0.949 | 0.488 | 100.0% | #2 | 0 | 1 | — | 1477ms | ✅ |
| angr | gcc -O2 | 0.150 | 0.675 | 0.0% | #1 | 0 | 1 | — | 1504ms | ✅ |
| angr | gcc-m32 -O2 | 0.150 | 0.595 | 0.0% | #1 | 0 | 1 | — | 1738ms | ✅ |
| fission | gcc -O2 | 0.149 | 0.489 | 0.0% | #3 | 0 | 1 | — | 2913ms | ✅ |
| ghidra | gcc -O0 | 0.138 | 0.375 | 0.0% | #2 | 0 | 3 | — | 32573ms | ✅ |
| fission | gcc-m32 -O0 | 0.132 | 0.321 | 0.0% | #3 | 0 | 3 | — | 2892ms | ✅ |
| fission | gcc-m32 -O2 | 0.109 | 0.094 | 0.0% | #3 | 0 | 3 | — | 2999ms | ✅ |
| fission | gcc -O0 | 0.106 | 0.057 | 0.0% | #3 | 0 | 3 | — | 3165ms | ✅ |
| radare2 | gcc -O0 | 0.100 | 0.004 | 0.0% | #4 | 0 | 0 | — | 709ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.100 | 0.004 | 0.0% | #4 | 0 | 0 | — | 432ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.100 | 0.003 | 0.0% | #4 | 0 | 0 | — | 706ms | ✅ |
| radare2 | gcc -O2 | 0.100 | 0.003 | 0.0% | #4 | 0 | 0 | — | 617ms | ✅ |
| snowman | gcc -O0 | 0.100 | 0.001 | 0.0% | #5 | 227 | 7 | — | 833ms | ✅ |
| snowman | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #5 | 161 | 7 | — | 739ms | ✅ |
| snowman | gcc -O2 | 0.100 | 0.001 | 0.0% | #5 | 219 | 7 | — | 901ms | ✅ |
| retdec | gcc -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 70ms | ❌ No matching plugins found for  |
| revng | gcc -O0 | 0.100 | 0.000 | 0.0% | #6 | 0 | 10 | — | 88199ms | ✅ |
| retdec | gcc-m32 -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 34ms | ❌ No matching plugins found for  |
| revng | gcc-m32 -O0 | 0.100 | 0.000 | 0.0% | #6 | 0 | 8 | — | 27923ms | ✅ |
| retdec | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 32ms | ❌ No matching plugins found for  |
| revng | gcc -O2 | 0.100 | 0.000 | 0.0% | #6 | 0 | 10 | — | 92542ms | ✅ |
| retdec | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 39ms | ❌ No matching plugins found for  |
| snowman | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | #5 | 151 | 7 | — | 727ms | ✅ |
| revng | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | #6 | 0 | 8 | — | 44691ms | ✅ |

### `sum_array`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc-m32 -O0 | 0.983 | 0.833 | 100.0% | #1 | 0 | 2 | — | 23892ms | ✅ |
| angr | gcc -O0 | 0.946 | 0.455 | 100.0% | #2 | 0 | 2 | — | 3237ms | ✅ |
| fission | gcc -O2 | 0.936 | 0.357 | 100.0% | #1 | 0 | 3 | — | 3315ms | ✅ |
| ghidra | gcc -O2 | 0.917 | 0.171 | 100.0% | #3 | 0 | 3 | — | 28388ms | ✅ |
| angr | gcc -O2 | 0.917 | 0.171 | 100.0% | #2 | 0 | 2 | — | 1693ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.917 | 0.171 | 100.0% | #1 | 0 | 3 | — | 26984ms | ✅ |
| angr | gcc-m32 -O2 | 0.912 | 0.122 | 100.0% | #3 | 0 | 2 | — | 2639ms | ✅ |
| ghidra | gcc -O0 | 0.150 | 0.648 | 0.0% | #1 | 0 | 2 | — | 31213ms | ✅ |
| angr | gcc-m32 -O0 | 0.150 | 0.543 | 0.0% | #2 | 0 | 2 | — | 1905ms | ✅ |
| fission | gcc -O0 | 0.115 | 0.145 | 0.0% | #3 | 2 | 2 | — | 5830ms | ✅ |
| fission | gcc-m32 -O2 | 0.112 | 0.124 | 0.0% | #2 | 0 | 3 | — | 3803ms | ✅ |
| fission | gcc-m32 -O0 | 0.112 | 0.120 | 0.0% | #3 | 1 | 2 | — | 3064ms | ✅ |
| radare2 | gcc -O0 | 0.101 | 0.008 | 0.0% | #4 | 0 | 0 | — | 1750ms | ✅ |
| radare2 | gcc -O2 | 0.101 | 0.008 | 0.0% | #4 | 0 | 0 | — | 882ms | ✅ |
| radare2 | gcc-m32 -O0 | 0.101 | 0.005 | 0.0% | #4 | 0 | 0 | — | 645ms | ✅ |
| radare2 | gcc-m32 -O2 | 0.101 | 0.005 | 0.0% | #4 | 0 | 0 | — | 417ms | ✅ |
| snowman | gcc -O0 | 0.100 | 0.001 | 0.0% | #6 | 222 | 7 | — | 1437ms | ✅ |
| revng | gcc -O0 | 0.100 | 0.001 | 0.0% | #5 | 0 | 10 | — | 91966ms | ✅ |
| snowman | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #5 | 155 | 7 | — | 819ms | ✅ |
| revng | gcc-m32 -O0 | 0.100 | 0.001 | 0.0% | #6 | 0 | 8 | — | 31174ms | ✅ |
| snowman | gcc -O2 | 0.100 | 0.001 | 0.0% | #5 | 220 | 7 | — | 765ms | ✅ |
| revng | gcc -O2 | 0.100 | 0.001 | 0.0% | #6 | 0 | 10 | — | 94613ms | ✅ |
| snowman | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #5 | 151 | 7 | — | 821ms | ✅ |
| revng | gcc-m32 -O2 | 0.100 | 0.001 | 0.0% | #6 | 0 | 8 | — | 42955ms | ✅ |
| retdec | gcc -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 54ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O0 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 48ms | ❌ No matching plugins found for  |
| retdec | gcc -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 56ms | ❌ No matching plugins found for  |
| retdec | gcc-m32 -O2 | 0.100 | 0.000 | 0.0% | — | 0 | 0 | — | 79ms | ❌ No matching plugins found for  |

---

## Overfitting Analysis

Functions where **all** decompilers scored below 0.3 are marked as objectively hard.
Functions where **only Fission** scored below 0.3 are marked as quality gaps.

**Fission quality gaps (14):** `clamp`, `signum`, `classify_range`, `saturating_add`, `reverse_in_place`, `fibonacci`, `fibonacci_iter`, `max`, `bubble_sort`, `linear_search`, `binary_search`, `factorial`, `power`, `process_code`