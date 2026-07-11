# Fission Benchmark Report

> [!WARNING]
> **ARCHIVED LEGACY RESULT** — This file was originally measured before
> the provenance envelope was introduced.  Original run timing and toolchain
> version information are not available.  Official validity is **unverified**.

**Measured at:** unknown (legacy)
**Rendered at:** 2026-07-11 02:03 UTC
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
| **fission** | 84 | 84 | 0 | — | — | — | — | 0.000 | 0.164 | 8.3% |
| **ghidra** | 84 | 84 | 0 | — | — | — | — | 0.000 | 0.427 | 70.2% |
| ~~retdec~~ ⛔ | 84 | 0 | 84 | — | — | — | — | — | — | — |
| **radare2** | 84 | 84 | 0 | — | — | — | — | 0.000 | 0.005 | 0.0% |
| **angr** | 84 | 81 | 3 | — | — | — | — | 0.000 | 0.399 | 60.5% |
| **snowman** | 84 | 84 | 0 | — | — | — | — | 0.000 | 0.001 | 0.0% |
| **revng** | 84 | 84 | 0 | — | — | — | — | 0.000 | 0.001 | 0.0% |

---

## Per-Function Results

### `accumulate_pairs` ⚪ Universally low (harness)
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.000 | 0.128 | 0.0% | #3 | 2 | 2 | — | 7607ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.517 | 0.0% | #1 | 0 | 2 | — | 32049ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 152ms | ❌ No matching plugins found for  |
| radare2 | gcc -O0 | 0.000 | 0.009 | 0.0% | #4 | 0 | 0 | — | 1646ms | ✅ |
| angr | gcc -O0 | 0.000 | 0.331 | 100.0% | #2 | 0 | 2 | — | 3713ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 222 | 7 | — | 2420ms | ✅ |
| revng | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 0 | 10 | — | 91908ms | ✅ |
| fission | gcc-m32 -O0 | 0.000 | 0.091 | 0.0% | #3 | 1 | 2 | — | 3612ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.000 | 0.787 | 100.0% | #1 | 0 | 2 | — | 24185ms | ✅ |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 174ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O0 | 0.000 | 0.005 | 0.0% | #4 | 0 | 0 | — | 381ms | ✅ |
| angr | gcc-m32 -O0 | 0.000 | 0.320 | 0.0% | #2 | 0 | 2 | — | 2141ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 155 | 7 | — | 855ms | ✅ |
| revng | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 0 | 8 | — | 33616ms | ✅ |
| fission | gcc -O2 | 0.000 | 0.139 | 100.0% | #2 | 2 | 2 | — | 3661ms | ✅ |
| ghidra | gcc -O2 | 0.000 | 0.120 | 100.0% | #3 | 0 | 3 | — | 29833ms | ✅ |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 30ms | ❌ No matching plugins found for  |
| radare2 | gcc -O2 | 0.000 | 0.009 | 0.0% | #4 | 0 | 0 | — | 426ms | ✅ |
| angr | gcc -O2 | 0.000 | 0.160 | 0.0% | #1 | 0 | 2 | — | 1679ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #5 | 220 | 7 | — | 764ms | ✅ |
| revng | gcc -O2 | 0.000 | 0.001 | 0.0% | #6 | 0 | 10 | — | 90322ms | ✅ |
| fission | gcc-m32 -O2 | 0.000 | 0.162 | 0.0% | #1 | 0 | 3 | — | 5936ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.000 | 0.120 | 100.0% | #3 | 0 | 3 | — | 30391ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 89ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O2 | 0.000 | 0.005 | 0.0% | #4 | 0 | 0 | — | 1532ms | ✅ |
| angr | gcc-m32 -O2 | 0.000 | 0.121 | 0.0% | #2 | 0 | 2 | — | 3147ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 151 | 7 | — | 2678ms | ✅ |
| revng | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 0 | 8 | — | 42639ms | ✅ |

### `binary_search` ⚪ Universally low (harness)
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.000 | 0.051 | 0.0% | #3 | 6 | 2 | — | 13286ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.242 | 0.0% | #2 | 0 | 3 | — | 31369ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 34ms | ❌ No matching plugins found for  |
| radare2 | gcc -O0 | 0.000 | 0.006 | 0.0% | #4 | 0 | 0 | — | 459ms | ✅ |
| angr | gcc -O0 | 0.000 | 0.335 | 100.0% | #1 | 0 | 2 | — | 3121ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 224 | 7 | — | 975ms | ✅ |
| revng | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 0 | 10 | — | 92376ms | ✅ |
| fission | gcc-m32 -O0 | 0.000 | 0.034 | 0.0% | #3 | 6 | 2 | — | 8947ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.000 | 0.438 | 100.0% | #1 | 0 | 3 | — | 26920ms | ✅ |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 57ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O0 | 0.000 | 0.005 | 0.0% | #4 | 0 | 0 | — | 925ms | ✅ |
| angr | gcc-m32 -O0 | 0.000 | 0.386 | 0.0% | #2 | 0 | 2 | — | 2221ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #6 | 157 | 7 | — | 867ms | ✅ |
| revng | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #5 | 0 | 8 | — | 35530ms | ✅ |
| fission | gcc -O2 | 0.000 | 0.056 | 0.0% | #3 | 6 | 2 | — | 4301ms | ✅ |
| ghidra | gcc -O2 | 0.000 | 0.239 | 100.0% | #1 | 0 | 5 | — | 22257ms | ✅ |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 52ms | ❌ No matching plugins found for  |
| radare2 | gcc -O2 | 0.000 | 0.009 | 0.0% | #4 | 0 | 0 | — | 896ms | ✅ |
| angr | gcc -O2 | 0.000 | 0.160 | 0.0% | #2 | 0 | 4 | — | 2368ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #5 | 223 | 7 | — | 979ms | ✅ |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ✅ |
| fission | gcc-m32 -O2 | 0.000 | 0.081 | 0.0% | #3 | 3 | 4 | — | 3395ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.000 | 0.239 | 100.0% | #1 | 0 | 5 | — | 18849ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 43ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O2 | 0.000 | 0.004 | 0.0% | #4 | 0 | 0 | — | 805ms | ✅ |
| angr | gcc-m32 -O2 | 0.000 | 0.175 | 0.0% | #2 | 0 | 4 | — | 1841ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 154 | 7 | — | 775ms | ✅ |
| revng | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 0 | 8 | — | 33285ms | ✅ |

### `bubble_sort` ⚪ Universally low (harness)
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.000 | 0.008 | 0.0% | #3 | 4 | 2 | — | 5536ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.167 | 0.0% | #2 | 0 | 4 | — | 23938ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 108ms | ❌ No matching plugins found for  |
| radare2 | gcc -O0 | 0.000 | 0.006 | 0.0% | #4 | 0 | 0 | — | 464ms | ✅ |
| angr | gcc -O0 | 0.000 | 0.295 | 100.0% | #1 | 0 | 4 | — | 2043ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 224 | 7 | — | 971ms | ✅ |
| revng | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 0 | 10 | — | 89696ms | ✅ |
| fission | gcc-m32 -O0 | 0.000 | 0.048 | 0.0% | #3 | 4 | 3 | — | 3180ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.000 | 0.152 | 100.0% | #2 | 0 | 4 | — | 18204ms | ✅ |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 172ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O0 | 0.000 | 0.004 | 0.0% | #4 | 0 | 0 | — | 849ms | ✅ |
| angr | gcc-m32 -O0 | 0.000 | 0.257 | 0.0% | #1 | 0 | 4 | — | 1814ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #6 | 157 | 7 | — | 626ms | ✅ |
| revng | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #5 | 0 | 8 | — | 24259ms | ✅ |
| fission | gcc -O2 | 0.000 | 0.105 | 0.0% | #3 | 4 | 3 | — | 8755ms | ✅ |
| ghidra | gcc -O2 | 0.000 | 0.131 | 0.0% | #1 | 0 | 5 | — | 30977ms | ✅ |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 90ms | ❌ No matching plugins found for  |
| radare2 | gcc -O2 | 0.000 | 0.007 | 0.0% | #4 | 0 | 0 | — | 976ms | ✅ |
| angr | gcc -O2 | 0.000 | 0.107 | 0.0% | #2 | 0 | 4 | — | 2643ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% | #5 | 223 | 7 | — | 1184ms | ✅ |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ✅ |
| fission | gcc-m32 -O2 | 0.000 | 0.038 | 0.0% | #3 | 2 | 4 | — | 5312ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.000 | 0.190 | 100.0% | #1 | 0 | 5 | — | 27443ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 28ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O2 | 0.000 | 0.006 | 0.0% | #4 | 0 | 0 | — | 917ms | ✅ |
| angr | gcc-m32 -O2 | 0.000 | 0.069 | 0.0% | #2 | 0 | 5 | — | 2313ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% | #5 | 154 | 7 | — | 786ms | ✅ |
| revng | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 0 | 8 | — | 46736ms | ✅ |

### `checksum` ⚪ Universally low (harness)
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.000 | 0.103 | 0.0% | #3 | 2 | 2 | — | 4071ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.668 | 0.0% | #1 | 0 | 2 | — | 31281ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 30ms | ❌ No matching plugins found for  |
| radare2 | gcc -O0 | 0.000 | 0.012 | 0.0% | #4 | 0 | 0 | — | 445ms | ✅ |
| angr | gcc -O0 | 0.000 | 0.567 | 100.0% | #2 | 0 | 2 | — | 1940ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 227 | 7 | — | 858ms | ✅ |
| revng | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 0 | 10 | — | 83931ms | ✅ |
| fission | gcc-m32 -O0 | 0.000 | 0.074 | 0.0% | #3 | 1 | 2 | — | 3384ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.000 | 0.819 | 100.0% | #1 | 0 | 2 | — | 26030ms | ✅ |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 45ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O0 | 0.000 | 0.011 | 0.0% | #4 | 0 | 0 | — | 721ms | ✅ |
| angr | gcc-m32 -O0 | 0.000 | 0.598 | 0.0% | #2 | 0 | 2 | — | 1792ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 161 | 7 | — | 892ms | ✅ |
| revng | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 0 | 8 | — | 35326ms | ✅ |
| fission | gcc -O2 | 0.000 | 0.170 | 100.0% | #1 | 0 | 3 | — | 3036ms | ✅ |
| ghidra | gcc -O2 | 0.000 | 0.129 | 100.0% | #2 | 0 | 3 | — | 26826ms | ✅ |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 29ms | ❌ No matching plugins found for  |
| radare2 | gcc -O2 | 0.000 | 0.012 | 0.0% | #4 | 0 | 0 | — | 469ms | ✅ |
| angr | gcc -O2 | 0.000 | 0.125 | 100.0% | #3 | 0 | 2 | — | 1601ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #5 | 219 | 7 | — | 946ms | ✅ |
| revng | gcc -O2 | 0.000 | 0.001 | 0.0% | #6 | 0 | 10 | — | 89794ms | ✅ |
| fission | gcc-m32 -O2 | 0.000 | 0.122 | 0.0% | #1 | 0 | 3 | — | 3489ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.000 | 0.116 | 100.0% | #2 | 0 | 3 | — | 23620ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 48ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O2 | 0.000 | 0.010 | 0.0% | #4 | 0 | 0 | — | 683ms | ✅ |
| angr | gcc-m32 -O2 | 0.000 | 0.095 | 100.0% | #3 | 0 | 2 | — | 1927ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 151 | 7 | — | 1151ms | ✅ |
| revng | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 0 | 8 | — | 38665ms | ✅ |

### `clamp` ⚪ Universally low (harness)
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.000 | 0.179 | 0.0% | #3 | 0 | 2 | — | 5596ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.421 | 0.0% | #2 | 0 | 2 | — | 30443ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 87ms | ❌ No matching plugins found for  |
| radare2 | gcc -O0 | 0.000 | 0.005 | 0.0% | #4 | 0 | 0 | — | 1335ms | ✅ |
| angr | gcc -O0 | 0.000 | 0.708 | 100.0% | #1 | 0 | 2 | — | 3451ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 227 | 7 | — | 1881ms | ✅ |
| revng | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 0 | 10 | — | 91200ms | ✅ |
| fission | gcc-m32 -O0 | 0.000 | 0.450 | 0.0% | #3 | 0 | 1 | — | 5501ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.000 | 0.590 | 100.0% | #2 | 0 | 2 | — | 25389ms | ✅ |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 83ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O0 | 0.000 | 0.005 | 0.0% | #4 | 0 | 0 | — | 1455ms | ✅ |
| angr | gcc-m32 -O0 | 0.000 | 0.705 | 100.0% | #1 | 0 | 2 | — | 3201ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | #6 | 161 | 7 | — | 1665ms | ✅ |
| revng | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 0 | 8 | — | 38453ms | ✅ |
| fission | gcc -O2 | 0.000 | 0.535 | 0.0% | #2 | 0 | 1 | — | 2735ms | ✅ |
| ghidra | gcc -O2 | 0.000 | 0.582 | 100.0% | #1 | 0 | 2 | — | 35117ms | ✅ |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 52ms | ❌ No matching plugins found for  |
| radare2 | gcc -O2 | 0.000 | 0.006 | 0.0% | #4 | 0 | 0 | — | 404ms | ✅ |
| angr | gcc -O2 | 0.000 | 0.524 | 100.0% | #3 | 0 | 1 | — | 2102ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #5 | 219 | 7 | — | 746ms | ✅ |
| revng | gcc -O2 | 0.000 | 0.001 | 0.0% | #6 | 0 | 10 | — | 90944ms | ✅ |
| fission | gcc-m32 -O2 | 0.000 | 0.368 | 0.0% | #3 | 0 | 1 | — | 2866ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.000 | 0.731 | 100.0% | #1 | 0 | 2 | — | 33984ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 31ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O2 | 0.000 | 0.005 | 0.0% | #4 | 0 | 0 | — | 645ms | ✅ |
| angr | gcc-m32 -O2 | 0.000 | 0.490 | 100.0% | #2 | 0 | 1 | — | 1777ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | #6 | 151 | 7 | — | 585ms | ✅ |
| revng | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 0 | 8 | — | 41849ms | ✅ |

### `classify_range` ⚪ Universally low (harness)
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.000 | 0.093 | 0.0% | #3 | 9 | 2 | — | 3932ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.167 | 0.0% | #2 | 0 | 3 | — | 25063ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 52ms | ❌ No matching plugins found for  |
| radare2 | gcc -O0 | 0.000 | 0.008 | 0.0% | #4 | 0 | 0 | — | 611ms | ✅ |
| angr | gcc -O0 | 0.000 | 0.182 | 100.0% | #1 | 0 | 2 | — | 1937ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 227 | 7 | — | 894ms | ✅ |
| revng | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 0 | 10 | — | 81972ms | ✅ |
| fission | gcc-m32 -O0 | 0.000 | 0.066 | 0.0% | #3 | 8 | 2 | — | 3328ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.000 | 0.174 | 100.0% | #1 | 0 | 3 | — | 26649ms | ✅ |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 40ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O0 | 0.000 | 0.003 | 0.0% | #4 | 0 | 0 | — | 514ms | ✅ |
| angr | gcc-m32 -O0 | 0.000 | 0.157 | 100.0% | #2 | 0 | 2 | — | 1705ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 161 | 7 | — | 915ms | ✅ |
| revng | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 0 | 8 | — | 31570ms | ✅ |
| fission | gcc -O2 | 0.000 | 0.513 | 0.0% | #2 | 0 | 3 | — | 3173ms | ✅ |
| ghidra | gcc -O2 | 0.000 | 0.486 | 100.0% | #3 | 0 | 3 | — | 28483ms | ✅ |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 53ms | ❌ No matching plugins found for  |
| radare2 | gcc -O2 | 0.000 | 0.009 | 0.0% | #4 | 0 | 0 | — | 419ms | ✅ |
| angr | gcc -O2 | 0.000 | 0.541 | 0.0% | #1 | 0 | 2 | — | 1680ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #6 | 219 | 7 | — | 887ms | ✅ |
| revng | gcc -O2 | 0.000 | 0.001 | 0.0% | #5 | 0 | 10 | — | 93220ms | ✅ |
| fission | gcc-m32 -O2 | 0.000 | 0.433 | 0.0% | #2 | 0 | 3 | — | 3031ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.000 | 0.486 | 100.0% | #1 | 0 | 3 | — | 27033ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 53ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O2 | 0.000 | 0.003 | 0.0% | #4 | 0 | 0 | — | 618ms | ✅ |
| angr | gcc-m32 -O2 | 0.000 | 0.401 | 0.0% | #3 | 0 | 1 | — | 1547ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 151 | 7 | — | 708ms | ✅ |
| revng | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 0 | 8 | — | 35155ms | ✅ |

### `count_bits` ⚪ Universally low (harness)
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.000 | 0.135 | 0.0% | #2 | 2 | 2 | — | 39612ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.688 | 0.0% | #1 | 0 | 2 | — | 70250ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 222ms | ❌ No matching plugins found for  |
| radare2 | gcc -O0 | 0.000 | 0.009 | 0.0% | #3 | 0 | 0 | — | 2561ms | ✅ |
| angr | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Server error '500 Internal Ser |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #4 | 227 | 7 | — | 4047ms | ✅ |
| revng | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 0 | 10 | — | 97666ms | ✅ |
| fission | gcc-m32 -O0 | 0.000 | 0.102 | 0.0% | #3 | 1 | 2 | — | 39577ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.000 | 0.755 | 100.0% | #1 | 0 | 2 | — | 70267ms | ✅ |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 217ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O0 | 0.000 | 0.007 | 0.0% | #4 | 0 | 0 | — | 2658ms | ✅ |
| angr | gcc-m32 -O0 | 0.000 | 0.655 | 100.0% | #2 | 0 | 2 | — | 2383ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 161 | 7 | — | 3820ms | ✅ |
| revng | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 0 | 8 | — | 54999ms | ✅ |
| fission | gcc -O2 | 0.000 | 0.104 | 100.0% | #2 | 1 | 3 | — | 40098ms | ✅ |
| ghidra | gcc -O2 | 0.000 | 0.609 | 100.0% | #1 | 0 | 2 | — | 70175ms | ✅ |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 191ms | ❌ No matching plugins found for  |
| radare2 | gcc -O2 | 0.000 | 0.008 | 0.0% | #3 | 0 | 0 | — | 2228ms | ✅ |
| angr | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Server error '500 Internal Ser |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #4 | 219 | 7 | — | 4152ms | ✅ |
| revng | gcc -O2 | 0.000 | 0.001 | 0.0% | #5 | 0 | 10 | — | 103102ms | ✅ |
| fission | gcc-m32 -O2 | 0.000 | 0.123 | 0.0% | #2 | 0 | 3 | — | 39865ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.000 | 0.609 | 100.0% | #1 | 0 | 2 | — | 70116ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 207ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O2 | 0.000 | 0.006 | 0.0% | #3 | 0 | 0 | — | 2334ms | ✅ |
| angr | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Server error '500 Internal Ser |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #4 | 151 | 7 | — | 3645ms | ✅ |
| revng | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 0 | 8 | — | 60054ms | ✅ |

### `factorial` ⚪ Universally low (harness)
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.000 | 0.033 | 0.0% | #3 | 2 | 2 | — | 6980ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.335 | 0.0% | #2 | 0 | 2 | — | 29181ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 29ms | ❌ No matching plugins found for  |
| radare2 | gcc -O0 | 0.000 | 0.004 | 0.0% | #4 | 0 | 0 | — | 1640ms | ✅ |
| angr | gcc -O0 | 0.000 | 0.702 | 100.0% | #1 | 0 | 1 | — | 3441ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.000 | 0.0% | #5 | 224 | 7 | — | 1692ms | ✅ |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | #6 | 0 | 10 | — | 97000ms | ✅ |
| fission | gcc-m32 -O0 | 0.000 | 0.050 | 0.0% | #3 | 0 | 3 | — | 7337ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.000 | 0.579 | 100.0% | #1 | 0 | 2 | — | 25963ms | ✅ |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 55ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #4 | 0 | 0 | — | 1614ms | ✅ |
| angr | gcc-m32 -O0 | 0.000 | 0.548 | 0.0% | #2 | 0 | 1 | — | 3214ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 157 | 7 | — | 2104ms | ✅ |
| revng | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 0 | 8 | — | 34736ms | ✅ |
| fission | gcc -O2 | 0.000 | 0.244 | 0.0% | #1 | 1 | 2 | — | 2912ms | ✅ |
| ghidra | gcc -O2 | 0.000 | 0.212 | 100.0% | #3 | 0 | 3 | — | 27174ms | ✅ |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 37ms | ❌ No matching plugins found for  |
| radare2 | gcc -O2 | 0.000 | 0.003 | 0.0% | #4 | 0 | 0 | — | 441ms | ✅ |
| angr | gcc -O2 | 0.000 | 0.239 | 0.0% | #2 | 0 | 2 | — | 1692ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.000 | 0.0% | #5 | 223 | 7 | — | 708ms | ✅ |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ✅ |
| fission | gcc-m32 -O2 | 0.000 | 0.022 | 0.0% | #3 | 1 | 2 | — | 5176ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.000 | 0.136 | 0.0% | #1 | 0 | 3 | — | 22721ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 29ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #4 | 0 | 0 | — | 737ms | ✅ |
| angr | gcc-m32 -O2 | 0.000 | 0.135 | 100.0% | #2 | 0 | 2 | — | 1690ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | #5 | 154 | 7 | — | 894ms | ✅ |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | #6 | 0 | 8 | — | 38813ms | ✅ |

### `fibonacci` ⚪ Universally low (harness)
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.000 | 0.044 | 0.0% | #3 | 0 | 3 | — | 4267ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.321 | 0.0% | #2 | 0 | 2 | — | 27616ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 49ms | ❌ No matching plugins found for  |
| radare2 | gcc -O0 | 0.000 | 0.004 | 0.0% | #4 | 0 | 0 | — | 862ms | ✅ |
| angr | gcc -O0 | 0.000 | 0.597 | 100.0% | #1 | 0 | 2 | — | 1806ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.000 | 0.0% | #5 | 224 | 7 | — | 884ms | ✅ |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | #6 | 0 | 10 | — | 91497ms | ✅ |
| fission | gcc-m32 -O0 | 0.000 | 0.477 | 0.0% | #3 | 0 | 3 | — | 5895ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.000 | 0.598 | 100.0% | #1 | 0 | 2 | — | 25362ms | ✅ |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 95ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O0 | 0.000 | 0.004 | 0.0% | #4 | 0 | 0 | — | 1514ms | ✅ |
| angr | gcc-m32 -O0 | 0.000 | 0.590 | 100.0% | #2 | 0 | 2 | — | 3174ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 157 | 7 | — | 2025ms | ✅ |
| revng | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 0 | 8 | — | 31039ms | ✅ |
| fission | gcc -O2 | 0.000 | 0.172 | 0.0% | #3 | 1 | 3 | — | 7133ms | ✅ |
| ghidra | gcc -O2 | 0.000 | 0.218 | 100.0% | #2 | 0 | 3 | — | 29311ms | ✅ |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 101ms | ❌ No matching plugins found for  |
| radare2 | gcc -O2 | 0.000 | 0.004 | 0.0% | #4 | 0 | 0 | — | 1784ms | ✅ |
| angr | gcc -O2 | 0.000 | 0.325 | 100.0% | #1 | 0 | 2 | — | 3566ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.000 | 0.0% | #5 | 223 | 7 | — | 1769ms | ✅ |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ✅ |
| fission | gcc-m32 -O2 | 0.000 | 0.088 | 0.0% | #3 | 0 | 3 | — | 3872ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.000 | 0.260 | 100.0% | #2 | 0 | 3 | — | 24035ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 29ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O2 | 0.000 | 0.004 | 0.0% | #4 | 0 | 0 | — | 802ms | ✅ |
| angr | gcc-m32 -O2 | 0.000 | 0.391 | 100.0% | #1 | 0 | 2 | — | 2364ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 154 | 7 | — | 868ms | ✅ |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | #6 | 0 | 8 | — | 37755ms | ✅ |

### `fibonacci_iter` ⚪ Universally low (harness)
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.000 | 0.176 | 0.0% | #3 | 4 | 2 | — | 4074ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.480 | 0.0% | #2 | 0 | 3 | — | 27831ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 52ms | ❌ No matching plugins found for  |
| radare2 | gcc -O0 | 0.000 | 0.007 | 0.0% | #4 | 0 | 0 | — | 583ms | ✅ |
| angr | gcc -O0 | 0.000 | 0.711 | 100.0% | #1 | 0 | 2 | — | 1724ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 224 | 7 | — | 824ms | ✅ |
| revng | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 0 | 10 | — | 81451ms | ✅ |
| fission | gcc-m32 -O0 | 0.000 | 0.156 | 0.0% | #3 | 2 | 2 | — | 2884ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.000 | 0.718 | 100.0% | #1 | 0 | 3 | — | 24971ms | ✅ |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 47ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O0 | 0.000 | 0.004 | 0.0% | #4 | 0 | 0 | — | 377ms | ✅ |
| angr | gcc-m32 -O0 | 0.000 | 0.709 | 100.0% | #2 | 0 | 2 | — | 1523ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 157 | 7 | — | 720ms | ✅ |
| revng | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 0 | 8 | — | 31245ms | ✅ |
| fission | gcc -O2 | 0.000 | 0.245 | 0.0% | #2 | 0 | 2 | — | 3430ms | ✅ |
| ghidra | gcc -O2 | 0.000 | 0.241 | 100.0% | #3 | 0 | 3 | — | 25763ms | ✅ |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 72ms | ❌ No matching plugins found for  |
| radare2 | gcc -O2 | 0.000 | 0.008 | 0.0% | #4 | 0 | 0 | — | 772ms | ✅ |
| angr | gcc -O2 | 0.000 | 0.248 | 0.0% | #1 | 0 | 2 | — | 1891ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #5 | 223 | 7 | — | 1026ms | ✅ |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ✅ |
| fission | gcc-m32 -O2 | 0.000 | 0.217 | 0.0% | #3 | 0 | 3 | — | 2887ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.000 | 0.243 | 100.0% | #2 | 0 | 3 | — | 18862ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 30ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O2 | 0.000 | 0.003 | 0.0% | #4 | 0 | 0 | — | 729ms | ✅ |
| angr | gcc-m32 -O2 | 0.000 | 0.262 | 0.0% | #1 | 0 | 2 | — | 1588ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 154 | 7 | — | 761ms | ✅ |
| revng | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 0 | 8 | — | 30803ms | ✅ |

### `find_pair_value` ⚪ Universally low (harness)
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.000 | 0.097 | 0.0% | #3 | 4 | 2 | — | 3741ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.342 | 0.0% | #1 | 0 | 3 | — | 29546ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 74ms | ❌ No matching plugins found for  |
| radare2 | gcc -O0 | 0.000 | 0.005 | 0.0% | #4 | 0 | 0 | — | 716ms | ✅ |
| angr | gcc -O0 | 0.000 | 0.289 | 100.0% | #2 | 0 | 2 | — | 2217ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 222 | 7 | — | 915ms | ✅ |
| revng | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 0 | 10 | — | 90716ms | ✅ |
| fission | gcc-m32 -O0 | 0.000 | 0.099 | 0.0% | #3 | 3 | 2 | — | 3370ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.000 | 0.695 | 100.0% | #1 | 0 | 3 | — | 26116ms | ✅ |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 59ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O0 | 0.000 | 0.005 | 0.0% | #4 | 0 | 0 | — | 821ms | ✅ |
| angr | gcc-m32 -O0 | 0.000 | 0.277 | 0.0% | #2 | 0 | 2 | — | 1907ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 155 | 7 | — | 876ms | ✅ |
| revng | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 0 | 8 | — | 34552ms | ✅ |
| fission | gcc -O2 | 0.000 | 0.165 | 100.0% | #3 | 3 | 4 | — | 3613ms | ✅ |
| ghidra | gcc -O2 | 0.000 | 0.212 | 100.0% | #2 | 0 | 4 | — | 27001ms | ✅ |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 29ms | ❌ No matching plugins found for  |
| radare2 | gcc -O2 | 0.000 | 0.005 | 0.0% | #4 | 0 | 0 | — | 1006ms | ✅ |
| angr | gcc -O2 | 0.000 | 0.215 | 100.0% | #1 | 0 | 2 | — | 2149ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #5 | 220 | 7 | — | 886ms | ✅ |
| revng | gcc -O2 | 0.000 | 0.001 | 0.0% | #6 | 0 | 10 | — | 93623ms | ✅ |
| fission | gcc-m32 -O2 | 0.000 | 0.099 | 0.0% | #3 | 3 | 4 | — | 6372ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.000 | 0.212 | 100.0% | #1 | 0 | 4 | — | 28163ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 129ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O2 | 0.000 | 0.004 | 0.0% | #4 | 0 | 0 | — | 1548ms | ✅ |
| angr | gcc-m32 -O2 | 0.000 | 0.165 | 100.0% | #2 | 0 | 2 | — | 3406ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 151 | 7 | — | 1964ms | ✅ |
| revng | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 0 | 8 | — | 41784ms | ✅ |

### `gcd` ⚪ Universally low (harness)
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.000 | 0.077 | 100.0% | #3 | 2 | 2 | — | 3581ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.596 | 0.0% | #1 | 0 | 2 | — | 23524ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 121ms | ❌ No matching plugins found for  |
| radare2 | gcc -O0 | 0.000 | 0.004 | 0.0% | #4 | 0 | 0 | — | 660ms | ✅ |
| angr | gcc -O0 | 0.000 | 0.467 | 100.0% | #2 | 0 | 2 | — | 1911ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 224 | 7 | — | 1125ms | ✅ |
| revng | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 0 | 10 | — | 90899ms | ✅ |
| fission | gcc-m32 -O0 | 0.000 | 0.068 | 0.0% | #3 | 1 | 2 | — | 3419ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.000 | 0.749 | 100.0% | #1 | 0 | 2 | — | 21017ms | ✅ |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 83ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O0 | 0.000 | 0.003 | 0.0% | #4 | 0 | 0 | — | 944ms | ✅ |
| angr | gcc-m32 -O0 | 0.000 | 0.488 | 100.0% | #2 | 0 | 2 | — | 1699ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 157 | 7 | — | 778ms | ✅ |
| revng | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 0 | 8 | — | 28035ms | ✅ |
| fission | gcc -O2 | 0.000 | 0.129 | 0.0% | #3 | 2 | 2 | — | 6287ms | ✅ |
| ghidra | gcc -O2 | 0.000 | 0.778 | 100.0% | #1 | 0 | 2 | — | 29476ms | ✅ |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 46ms | ❌ No matching plugins found for  |
| radare2 | gcc -O2 | 0.000 | 0.004 | 0.0% | #4 | 0 | 0 | — | 1379ms | ✅ |
| angr | gcc -O2 | 0.000 | 0.467 | 0.0% | #2 | 0 | 3 | — | 3381ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #5 | 223 | 7 | — | 1962ms | ✅ |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ✅ |
| fission | gcc-m32 -O2 | 0.000 | 0.153 | 0.0% | #3 | 0 | 3 | — | 5432ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.000 | 0.514 | 100.0% | #1 | 0 | 3 | — | 26943ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 77ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% | #4 | 0 | 0 | — | 776ms | ✅ |
| angr | gcc-m32 -O2 | 0.000 | 0.388 | 100.0% | #2 | 0 | 2 | — | 2875ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 154 | 7 | — | 2417ms | ✅ |
| revng | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 0 | 8 | — | 43392ms | ✅ |

### `linear_search` ⚪ Universally low (harness)
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.000 | 0.135 | 0.0% | #3 | 4 | 2 | — | 3627ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.371 | 0.0% | #2 | 0 | 3 | — | 25281ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 52ms | ❌ No matching plugins found for  |
| radare2 | gcc -O0 | 0.000 | 0.005 | 0.0% | #4 | 0 | 0 | — | 554ms | ✅ |
| angr | gcc -O0 | 0.000 | 0.707 | 100.0% | #1 | 0 | 2 | — | 1843ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 224 | 7 | — | 1013ms | ✅ |
| revng | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 0 | 10 | — | 84946ms | ✅ |
| fission | gcc-m32 -O0 | 0.000 | 0.114 | 0.0% | #3 | 3 | 2 | — | 3471ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.000 | 0.617 | 100.0% | #2 | 0 | 3 | — | 20461ms | ✅ |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 37ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #4 | 0 | 0 | — | 488ms | ✅ |
| angr | gcc-m32 -O0 | 0.000 | 0.714 | 0.0% | #1 | 0 | 2 | — | 2158ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 157 | 7 | — | 1097ms | ✅ |
| revng | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 0 | 8 | — | 27806ms | ✅ |
| fission | gcc -O2 | 0.000 | 0.154 | 0.0% | #3 | 3 | 4 | — | 3394ms | ✅ |
| ghidra | gcc -O2 | 0.000 | 0.660 | 100.0% | #1 | 0 | 4 | — | 28041ms | ✅ |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 62ms | ❌ No matching plugins found for  |
| radare2 | gcc -O2 | 0.000 | 0.005 | 0.0% | #4 | 0 | 0 | — | 847ms | ✅ |
| angr | gcc -O2 | 0.000 | 0.200 | 0.0% | #2 | 0 | 2 | — | 2118ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #5 | 223 | 7 | — | 972ms | ✅ |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ✅ |
| fission | gcc-m32 -O2 | 0.000 | 0.080 | 0.0% | #3 | 3 | 4 | — | 3310ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.000 | 0.688 | 100.0% | #1 | 0 | 4 | — | 22977ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 41ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% | #4 | 0 | 0 | — | 699ms | ✅ |
| angr | gcc-m32 -O2 | 0.000 | 0.497 | 0.0% | #2 | 0 | 2 | — | 1735ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 154 | 7 | — | 801ms | ✅ |
| revng | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 0 | 8 | — | 36135ms | ✅ |

### `max` ⚪ Universally low (harness)
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.000 | 0.365 | 0.0% | #3 | 0 | 1 | — | 3022ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.431 | 0.0% | #2 | 0 | 2 | — | 25688ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 29ms | ❌ No matching plugins found for  |
| radare2 | gcc -O0 | 0.000 | 0.002 | 0.0% | #4 | 0 | 0 | — | 824ms | ✅ |
| angr | gcc -O0 | 0.000 | 0.752 | 100.0% | #1 | 0 | 1 | — | 1558ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.000 | 0.0% | #5 | 224 | 7 | — | 994ms | ✅ |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | #6 | 0 | 10 | — | 74879ms | ✅ |
| fission | gcc-m32 -O0 | 0.000 | 0.419 | 0.0% | #3 | 0 | 1 | — | 2935ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.000 | 0.654 | 100.0% | #2 | 0 | 2 | — | 22905ms | ✅ |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 32ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #4 | 0 | 0 | — | 564ms | ✅ |
| angr | gcc-m32 -O0 | 0.000 | 0.673 | 100.0% | #1 | 0 | 1 | — | 1568ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 157 | 7 | — | 890ms | ✅ |
| revng | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 0 | 8 | — | 26042ms | ✅ |
| fission | gcc -O2 | 0.000 | 0.579 | 0.0% | #3 | 0 | 1 | — | 2719ms | ✅ |
| ghidra | gcc -O2 | 0.000 | 0.654 | 100.0% | #2 | 0 | 2 | — | 21627ms | ✅ |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 29ms | ❌ No matching plugins found for  |
| radare2 | gcc -O2 | 0.000 | 0.002 | 0.0% | #4 | 0 | 0 | — | 443ms | ✅ |
| angr | gcc -O2 | 0.000 | 0.752 | 100.0% | #1 | 0 | 1 | — | 1844ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.000 | 0.0% | #5 | 223 | 7 | — | 979ms | ✅ |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ✅ |
| fission | gcc-m32 -O2 | 0.000 | 0.419 | 0.0% | #3 | 0 | 1 | — | 2841ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.000 | 0.660 | 100.0% | #2 | 0 | 2 | — | 21776ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 78ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #4 | 0 | 0 | — | 706ms | ✅ |
| angr | gcc-m32 -O2 | 0.000 | 0.667 | 100.0% | #1 | 0 | 1 | — | 1679ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 154 | 7 | — | 1024ms | ✅ |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | #6 | 0 | 8 | — | 40224ms | ✅ |

### `pointer_stride_sum` ⚪ Universally low (harness)
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.000 | 0.097 | 0.0% | #3 | 2 | 2 | — | 6134ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.259 | 0.0% | #1 | 0 | 2 | — | 35390ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 115ms | ❌ No matching plugins found for  |
| radare2 | gcc -O0 | 0.000 | 0.005 | 0.0% | #4 | 0 | 0 | — | 1630ms | ✅ |
| angr | gcc -O0 | 0.000 | 0.253 | 100.0% | #2 | 0 | 2 | — | 3392ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 222 | 7 | — | 2519ms | ✅ |
| revng | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 0 | 10 | — | 92627ms | ✅ |
| fission | gcc-m32 -O0 | 0.000 | 0.166 | 0.0% | #3 | 1 | 2 | — | 3833ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.000 | 0.674 | 100.0% | #1 | 0 | 2 | — | 23690ms | ✅ |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 34ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O0 | 0.000 | 0.004 | 0.0% | #4 | 0 | 0 | — | 681ms | ✅ |
| angr | gcc-m32 -O0 | 0.000 | 0.511 | 100.0% | #2 | 0 | 2 | — | 2309ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 155 | 7 | — | 943ms | ✅ |
| revng | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 0 | 8 | — | 31980ms | ✅ |
| fission | gcc -O2 | 0.000 | 0.319 | 100.0% | #3 | 0 | 3 | — | 3327ms | ✅ |
| ghidra | gcc -O2 | 0.000 | 0.609 | 100.0% | #1 | 0 | 2 | — | 26539ms | ✅ |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 70ms | ❌ No matching plugins found for  |
| radare2 | gcc -O2 | 0.000 | 0.006 | 0.0% | #4 | 0 | 0 | — | 448ms | ✅ |
| angr | gcc -O2 | 0.000 | 0.325 | 100.0% | #2 | 0 | 3 | — | 1527ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #5 | 220 | 7 | — | 757ms | ✅ |
| revng | gcc -O2 | 0.000 | 0.001 | 0.0% | #6 | 0 | 10 | — | 85844ms | ✅ |
| fission | gcc-m32 -O2 | 0.000 | 0.226 | 0.0% | #2 | 0 | 3 | — | 2965ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.000 | 0.648 | 100.0% | #1 | 0 | 2 | — | 26031ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 55ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O2 | 0.000 | 0.005 | 0.0% | #4 | 0 | 0 | — | 385ms | ✅ |
| angr | gcc-m32 -O2 | 0.000 | 0.195 | 100.0% | #3 | 0 | 2 | — | 1615ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 151 | 7 | — | 810ms | ✅ |
| revng | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 0 | 8 | — | 34551ms | ✅ |

### `power` ⚪ Universally low (harness)
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.000 | 0.077 | 0.0% | #3 | 2 | 2 | — | 3753ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.374 | 0.0% | #1 | 0 | 3 | — | 26264ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 50ms | ❌ No matching plugins found for  |
| radare2 | gcc -O0 | 0.000 | 0.008 | 0.0% | #4 | 0 | 0 | — | 727ms | ✅ |
| angr | gcc -O0 | 0.000 | 0.283 | 100.0% | #2 | 0 | 2 | — | 1851ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 224 | 7 | — | 808ms | ✅ |
| revng | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 0 | 10 | — | 96054ms | ✅ |
| fission | gcc-m32 -O0 | 0.000 | 0.039 | 0.0% | #3 | 1 | 2 | — | 3808ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.000 | 0.492 | 0.0% | #1 | 0 | 3 | — | 25249ms | ✅ |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 51ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O0 | 0.000 | 0.004 | 0.0% | #4 | 0 | 0 | — | 867ms | ✅ |
| angr | gcc-m32 -O0 | 0.000 | 0.176 | 0.0% | #2 | 0 | 3 | — | 2148ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 157 | 7 | — | 743ms | ✅ |
| revng | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #5 | 0 | 8 | — | 32534ms | ✅ |
| fission | gcc -O2 | 0.000 | 0.081 | 0.0% | #3 | 2 | 5 | — | 3243ms | ✅ |
| ghidra | gcc -O2 | 0.000 | 0.392 | 100.0% | #1 | 0 | 4 | — | 27111ms | ✅ |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 35ms | ❌ No matching plugins found for  |
| radare2 | gcc -O2 | 0.000 | 0.008 | 0.0% | #4 | 0 | 0 | — | 902ms | ✅ |
| angr | gcc -O2 | 0.000 | 0.195 | 0.0% | #2 | 0 | 2 | — | 1728ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #5 | 223 | 7 | — | 782ms | ✅ |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ✅ |
| fission | gcc-m32 -O2 | 0.000 | 0.035 | 0.0% | #3 | 1 | 5 | — | 4613ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.000 | 0.249 | 0.0% | #1 | 0 | 4 | — | 25052ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 48ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O2 | 0.000 | 0.004 | 0.0% | #4 | 0 | 0 | — | 551ms | ✅ |
| angr | gcc-m32 -O2 | 0.000 | 0.088 | 0.0% | #2 | 0 | 3 | — | 2218ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 154 | 7 | — | 785ms | ✅ |
| revng | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 0 | 8 | — | 40632ms | ✅ |

### `process_code` ⚪ Universally low (harness)
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.000 | 0.049 | 0.0% | #3 | 4 | 3 | — | 3685ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.157 | 0.0% | #2 | 0 | 4 | — | 25314ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 82ms | ❌ No matching plugins found for  |
| radare2 | gcc -O0 | 0.000 | 0.005 | 0.0% | #4 | 0 | 0 | — | 770ms | ✅ |
| angr | gcc -O0 | 0.000 | 0.661 | 100.0% | #1 | 0 | 1 | — | 1907ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 224 | 7 | — | 981ms | ✅ |
| revng | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 0 | 10 | — | 86814ms | ✅ |
| fission | gcc-m32 -O0 | 0.000 | 0.054 | 0.0% | #3 | 3 | 5 | — | 3600ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.000 | 0.166 | 100.0% | #2 | 0 | 4 | — | 22761ms | ✅ |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 52ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O0 | 0.000 | 0.005 | 0.0% | #4 | 0 | 0 | — | 680ms | ✅ |
| angr | gcc-m32 -O0 | 0.000 | 0.660 | 100.0% | #1 | 0 | 1 | — | 2002ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 157 | 7 | — | 787ms | ✅ |
| revng | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 0 | 8 | — | 27695ms | ✅ |
| fission | gcc -O2 | 0.000 | 0.331 | 0.0% | #1 | 0 | 1 | — | 3245ms | ✅ |
| ghidra | gcc -O2 | 0.000 | 0.286 | 100.0% | #2 | 0 | 2 | — | 25690ms | ✅ |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 33ms | ❌ No matching plugins found for  |
| radare2 | gcc -O2 | 0.000 | 0.006 | 0.0% | #4 | 0 | 0 | — | 577ms | ✅ |
| angr | gcc -O2 | 0.000 | 0.247 | 100.0% | #3 | 0 | 3 | — | 1726ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #5 | 223 | 7 | — | 766ms | ✅ |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | #6 | 0 | 10 | — | 112958ms | ✅ |
| fission | gcc-m32 -O2 | 0.000 | 0.099 | 0.0% | #3 | 0 | 5 | — | 3459ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.000 | 0.286 | 100.0% | #1 | 0 | 2 | — | 23046ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 65ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O2 | 0.000 | 0.004 | 0.0% | #4 | 0 | 0 | — | 501ms | ✅ |
| angr | gcc-m32 -O2 | 0.000 | 0.260 | 100.0% | #2 | 0 | 3 | — | 1547ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 154 | 7 | — | 827ms | ✅ |
| revng | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 0 | 8 | — | 36736ms | ✅ |

### `reverse_in_place` ⚪ Universally low (harness)
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.000 | 0.106 | 0.0% | #3 | 2 | 2 | — | 5013ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.323 | 0.0% | #1 | 0 | 2 | — | 27952ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 50ms | ❌ No matching plugins found for  |
| radare2 | gcc -O0 | 0.000 | 0.006 | 0.0% | #4 | 0 | 0 | — | 579ms | ✅ |
| angr | gcc -O0 | 0.000 | 0.273 | 0.0% | #2 | 0 | 2 | — | 1822ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 222 | 7 | — | 869ms | ✅ |
| revng | gcc -O0 | 0.000 | 0.002 | 0.0% | #5 | 0 | 10 | — | 88450ms | ✅ |
| fission | gcc-m32 -O0 | 0.000 | 0.051 | 0.0% | #3 | 1 | 2 | — | 3809ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.000 | 0.339 | 100.0% | #1 | 0 | 2 | — | 26005ms | ✅ |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 44ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O0 | 0.000 | 0.006 | 0.0% | #4 | 0 | 0 | — | 913ms | ✅ |
| angr | gcc-m32 -O0 | 0.000 | 0.222 | 0.0% | #2 | 0 | 2 | — | 2017ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #5 | 155 | 7 | — | 1134ms | ✅ |
| revng | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 0 | 8 | — | 33893ms | ✅ |
| fission | gcc -O2 | 0.000 | 0.131 | 0.0% | #3 | 2 | 3 | — | 3591ms | ✅ |
| ghidra | gcc -O2 | 0.000 | 0.221 | 100.0% | #1 | 0 | 3 | — | 30062ms | ✅ |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 73ms | ❌ No matching plugins found for  |
| radare2 | gcc -O2 | 0.000 | 0.006 | 0.0% | #4 | 0 | 0 | — | 631ms | ✅ |
| angr | gcc -O2 | 0.000 | 0.164 | 0.0% | #2 | 0 | 3 | — | 1935ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #5 | 220 | 7 | — | 855ms | ✅ |
| revng | gcc -O2 | 0.000 | 0.001 | 0.0% | #6 | 0 | 10 | — | 91955ms | ✅ |
| fission | gcc-m32 -O2 | 0.000 | 0.121 | 0.0% | #2 | 2 | 2 | — | 3537ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.000 | 0.221 | 100.0% | #1 | 0 | 3 | — | 25146ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 28ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O2 | 0.000 | 0.005 | 0.0% | #4 | 0 | 0 | — | 481ms | ✅ |
| angr | gcc-m32 -O2 | 0.000 | 0.099 | 0.0% | #3 | 0 | 3 | — | 2171ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 151 | 7 | — | 831ms | ✅ |
| revng | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 0 | 8 | — | 38100ms | ✅ |

### `saturating_add` ⚪ Universally low (harness)
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.000 | 0.063 | 0.0% | #3 | 3 | 2 | — | 4270ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.252 | 0.0% | #2 | 0 | 3 | — | 30426ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 52ms | ❌ No matching plugins found for  |
| radare2 | gcc -O0 | 0.000 | 0.011 | 0.0% | #4 | 0 | 0 | — | 416ms | ✅ |
| angr | gcc -O0 | 0.000 | 0.769 | 100.0% | #1 | 0 | 1 | — | 2133ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 227 | 7 | — | 751ms | ✅ |
| revng | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 0 | 10 | — | 86308ms | ✅ |
| fission | gcc-m32 -O0 | 0.000 | 0.048 | 0.0% | #3 | 2 | 3 | — | 3699ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.000 | 0.246 | 100.0% | #2 | 0 | 3 | — | 27432ms | ✅ |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 29ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O0 | 0.000 | 0.006 | 0.0% | #4 | 0 | 0 | — | 567ms | ✅ |
| angr | gcc-m32 -O0 | 0.000 | 0.766 | 100.0% | #1 | 0 | 1 | — | 1611ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 161 | 7 | — | 794ms | ✅ |
| revng | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 0 | 8 | — | 31488ms | ✅ |
| fission | gcc -O2 | 0.000 | 0.290 | 0.0% | #3 | 1 | 2 | — | 3151ms | ✅ |
| ghidra | gcc -O2 | 0.000 | 0.606 | 100.0% | #1 | 0 | 2 | — | 29947ms | ✅ |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 54ms | ❌ No matching plugins found for  |
| radare2 | gcc -O2 | 0.000 | 0.012 | 0.0% | #4 | 0 | 0 | — | 517ms | ✅ |
| angr | gcc -O2 | 0.000 | 0.311 | 0.0% | #2 | 0 | 2 | — | 1666ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #6 | 219 | 7 | — | 809ms | ✅ |
| revng | gcc -O2 | 0.000 | 0.001 | 0.0% | #5 | 0 | 10 | — | 100256ms | ✅ |
| fission | gcc-m32 -O2 | 0.000 | 0.124 | 0.0% | #3 | 1 | 2 | — | 5796ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.000 | 0.606 | 100.0% | #2 | 0 | 2 | — | 26901ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 51ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O2 | 0.000 | 0.006 | 0.0% | #4 | 0 | 0 | — | 1665ms | ✅ |
| angr | gcc-m32 -O2 | 0.000 | 0.639 | 100.0% | #1 | 0 | 2 | — | 3098ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 151 | 7 | — | 2684ms | ✅ |
| revng | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 0 | 8 | — | 40056ms | ✅ |

### `signum` ⚪ Universally low (harness)
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.000 | 0.057 | 0.0% | #3 | 0 | 3 | — | 3165ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.375 | 0.0% | #2 | 0 | 3 | — | 32573ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 70ms | ❌ No matching plugins found for  |
| radare2 | gcc -O0 | 0.000 | 0.004 | 0.0% | #4 | 0 | 0 | — | 709ms | ✅ |
| angr | gcc -O0 | 0.000 | 0.503 | 100.0% | #1 | 0 | 1 | — | 1901ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 227 | 7 | — | 833ms | ✅ |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | #6 | 0 | 10 | — | 88199ms | ✅ |
| fission | gcc-m32 -O0 | 0.000 | 0.321 | 0.0% | #3 | 0 | 3 | — | 2892ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.000 | 0.611 | 100.0% | #1 | 0 | 3 | — | 19524ms | ✅ |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 34ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O0 | 0.000 | 0.003 | 0.0% | #4 | 0 | 0 | — | 706ms | ✅ |
| angr | gcc-m32 -O0 | 0.000 | 0.488 | 100.0% | #2 | 0 | 1 | — | 1477ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 161 | 7 | — | 739ms | ✅ |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | #6 | 0 | 8 | — | 27923ms | ✅ |
| fission | gcc -O2 | 0.000 | 0.489 | 0.0% | #3 | 0 | 1 | — | 2913ms | ✅ |
| ghidra | gcc -O2 | 0.000 | 0.492 | 100.0% | #2 | 0 | 2 | — | 26895ms | ✅ |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 32ms | ❌ No matching plugins found for  |
| radare2 | gcc -O2 | 0.000 | 0.003 | 0.0% | #4 | 0 | 0 | — | 617ms | ✅ |
| angr | gcc -O2 | 0.000 | 0.675 | 0.0% | #1 | 0 | 1 | — | 1504ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #5 | 219 | 7 | — | 901ms | ✅ |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | #6 | 0 | 10 | — | 92542ms | ✅ |
| fission | gcc-m32 -O2 | 0.000 | 0.094 | 0.0% | #3 | 0 | 3 | — | 2999ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.000 | 0.583 | 100.0% | #2 | 0 | 2 | — | 29593ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 39ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O2 | 0.000 | 0.004 | 0.0% | #4 | 0 | 0 | — | 432ms | ✅ |
| angr | gcc-m32 -O2 | 0.000 | 0.595 | 0.0% | #1 | 0 | 1 | — | 1738ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | #5 | 151 | 7 | — | 727ms | ✅ |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | #6 | 0 | 8 | — | 44691ms | ✅ |

### `sum_array` ⚪ Universally low (harness)
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.000 | 0.145 | 0.0% | #3 | 2 | 2 | — | 5830ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.648 | 0.0% | #1 | 0 | 2 | — | 31213ms | ✅ |
| retdec | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 54ms | ❌ No matching plugins found for  |
| radare2 | gcc -O0 | 0.000 | 0.008 | 0.0% | #4 | 0 | 0 | — | 1750ms | ✅ |
| angr | gcc -O0 | 0.000 | 0.455 | 100.0% | #2 | 0 | 2 | — | 3237ms | ✅ |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #6 | 222 | 7 | — | 1437ms | ✅ |
| revng | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 0 | 10 | — | 91966ms | ✅ |
| fission | gcc-m32 -O0 | 0.000 | 0.120 | 0.0% | #3 | 1 | 2 | — | 3064ms | ✅ |
| ghidra | gcc-m32 -O0 | 0.000 | 0.833 | 100.0% | #1 | 0 | 2 | — | 23892ms | ✅ |
| retdec | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 48ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O0 | 0.000 | 0.005 | 0.0% | #4 | 0 | 0 | — | 645ms | ✅ |
| angr | gcc-m32 -O0 | 0.000 | 0.543 | 0.0% | #2 | 0 | 2 | — | 1905ms | ✅ |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 155 | 7 | — | 819ms | ✅ |
| revng | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #6 | 0 | 8 | — | 31174ms | ✅ |
| fission | gcc -O2 | 0.000 | 0.357 | 100.0% | #1 | 0 | 3 | — | 3315ms | ✅ |
| ghidra | gcc -O2 | 0.000 | 0.171 | 100.0% | #3 | 0 | 3 | — | 28388ms | ✅ |
| retdec | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 56ms | ❌ No matching plugins found for  |
| radare2 | gcc -O2 | 0.000 | 0.008 | 0.0% | #4 | 0 | 0 | — | 882ms | ✅ |
| angr | gcc -O2 | 0.000 | 0.171 | 100.0% | #2 | 0 | 2 | — | 1693ms | ✅ |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #5 | 220 | 7 | — | 765ms | ✅ |
| revng | gcc -O2 | 0.000 | 0.001 | 0.0% | #6 | 0 | 10 | — | 94613ms | ✅ |
| fission | gcc-m32 -O2 | 0.000 | 0.124 | 0.0% | #2 | 0 | 3 | — | 3803ms | ✅ |
| ghidra | gcc-m32 -O2 | 0.000 | 0.171 | 100.0% | #1 | 0 | 3 | — | 26984ms | ✅ |
| retdec | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 79ms | ❌ No matching plugins found for  |
| radare2 | gcc-m32 -O2 | 0.000 | 0.005 | 0.0% | #4 | 0 | 0 | — | 417ms | ✅ |
| angr | gcc-m32 -O2 | 0.000 | 0.122 | 100.0% | #3 | 0 | 2 | — | 2639ms | ✅ |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 151 | 7 | — | 821ms | ✅ |
| revng | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #6 | 0 | 8 | — | 42955ms | ✅ |

---

## Overfitting Analysis

Functions where **all** decompilers scored below 0.3 are marked as objectively hard.
Functions where **only Fission** scored below 0.3 are marked as quality gaps.

**Objectively hard functions (21):** `count_bits`, `clamp`, `signum`, `checksum`, `classify_range`, `saturating_add`, `sum_array`, `reverse_in_place`, `find_pair_value`, `accumulate_pairs`, `pointer_stride_sum`, `fibonacci`, `fibonacci_iter`, `max`, `bubble_sort`, `linear_search`, `binary_search`, `factorial`, `gcd`, `power`, `process_code`