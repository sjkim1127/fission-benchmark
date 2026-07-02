# Fission Benchmark Report

**Generated:** 2026-07-02 03:01 UTC
**Corpus:** `dev`
**Functions evaluated:** 28

---

## Summary — Correctness-Oriented Composite

> Readability metrics are recorded as unvalidated raw proxies. They are not combined into a final readability score until the human validation study is complete.

| Decompiler | Composite ⭐ | Similarity | Semantic Pass | Functions |
| ---|---|---|---|--- |
| **radare2** | 0.136 | 0.303 | 0.0% | 140 |
| **reko** | 0.123 | 0.169 | 0.0% | 140 |
| **angr** | 0.119 | 0.093 | 0.0% | 140 |
| **boomerang** | 0.039 | 0.020 | 0.0% | 140 |
| **snowman** | 0.000 | 0.001 | 0.0% | 140 |

---

## Per-Function Results

### `accumulate_pairs`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.435 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 73ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.289 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 63ms | 🔴 compile |
| reko | gcc -O0 | 0.141 | 0.204 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 372ms | 🔴 compile |
| reko | gcc -O2 | 0.125 | 0.124 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 365ms | 🔴 compile |
| radare2 | gcc -O2 | 0.121 | 0.153 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 73ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.120 | 0.102 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 378ms | 🔴 compile |
| angr | gcc -O0 | 0.119 | 0.097 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 198ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.119 | 0.097 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 157ms | 🔴 compile |
| angr | gcc -O2 | 0.119 | 0.097 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 173ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.119 | 0.097 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 182ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.113 | 0.116 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 56ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.112 | 0.060 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 446ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 14ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 15ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 322ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 333ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 469ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 155 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 415ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 220 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 430ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 427ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 723ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 748ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 725ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 713ms | ❌ usage: revng [-h] [--version]  |

### `binary_search`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.389 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 43ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.409 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 35ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.124 | 0.172 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 170ms | 🔴 compile |
| radare2 | gcc -O2 | 0.120 | 0.252 | 0.0% (0/6) | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 39ms | 🔴 compile |
| reko | gcc -O0 | 0.119 | 0.145 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 197ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.117 | 0.236 | 0.0% (0/6) | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 39ms | 🔴 compile |
| angr | gcc -O0 | 0.113 | 0.064 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 87ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.113 | 0.064 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 94ms | 🔴 compile |
| angr | gcc -O2 | 0.113 | 0.064 | 0.0% (0/6) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 92ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.113 | 0.064 | 0.0% (0/6) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 100ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.109 | 0.146 | 0.0% (0/6) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 202ms | 🔴 compile |
| reko | gcc -O2 | 0.097 | 0.084 | 0.0% (0/6) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 239ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.023 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 8ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.023 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 7ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 152ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 169ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% (0/6) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 280ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 505ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 524ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 351ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 732ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 533ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 784ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 578ms | ❌ usage: revng [-h] [--version]  |

### `bubble_sort`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc-m32 -O0 | 0.150 | 0.322 | 0.0% (0/5) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 35ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.135 | 0.172 | 0.0% (0/5) | #2 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 170ms | 🔴 compile |
| radare2 | gcc -O0 | 0.129 | 0.144 | 0.0% (0/5) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 43ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.127 | 0.186 | 0.0% (0/5) | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 39ms | 🔴 compile |
| reko | gcc -O2 | 0.120 | 0.102 | 0.0% (0/5) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 239ms | 🔴 compile |
| angr | gcc -O0 | 0.120 | 0.099 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 87ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.120 | 0.099 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 94ms | 🔴 compile |
| angr | gcc -O2 | 0.120 | 0.099 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 92ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.120 | 0.099 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 100ms | 🔴 compile |
| reko | gcc -O0 | 0.118 | 0.091 | 0.0% (0/5) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 197ms | 🔴 compile |
| radare2 | gcc -O2 | 0.118 | 0.141 | 0.0% (0/5) | #3 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 39ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.113 | 0.116 | 0.0% (0/5) | #3 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 202ms | 🔴 compile |
| boomerang | gcc -O0 | 0.079 | 0.037 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 8ms | 🔴 compile |
| boomerang | gcc -O2 | 0.079 | 0.037 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 7ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 152ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 169ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% (0/5) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 280ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% (0/5) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 524ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% (0/5) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 351ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 505ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 732ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 533ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 784ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 578ms | ❌ usage: revng [-h] [--version]  |

### `checksum`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.454 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 54ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.523 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 49ms | 🔴 compile |
| reko | gcc -O0 | 0.135 | 0.176 | 0.0% (0/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 379ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.130 | 0.151 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 337ms | 🔴 compile |
| angr | gcc -O0 | 0.117 | 0.087 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 148ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.117 | 0.087 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 116ms | 🔴 compile |
| angr | gcc -O2 | 0.117 | 0.087 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 161ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.117 | 0.087 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 131ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.117 | 0.086 | 0.0% (0/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 384ms | 🔴 compile |
| radare2 | gcc -O2 | 0.117 | 0.134 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 66ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.111 | 0.105 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 52ms | 🔴 compile |
| reko | gcc -O2 | 0.108 | 0.039 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 339ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 15ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 13ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.004 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 267ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 233ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 457ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 161 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 429ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 489ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 489ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 722ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 678ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 764ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 753ms | ❌ usage: revng [-h] [--version]  |

### `clamp`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.485 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 54ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.407 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 379ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.559 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 49ms | 🔴 compile |
| radare2 | gcc -O2 | 0.150 | 0.571 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 66ms | 🔴 compile |
| reko | gcc -O2 | 0.150 | 0.386 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 339ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.693 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 52ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.150 | 0.440 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 384ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.122 | 0.110 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 337ms | 🔴 compile |
| angr | gcc -O0 | 0.118 | 0.091 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 148ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.118 | 0.091 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 116ms | 🔴 compile |
| angr | gcc -O2 | 0.118 | 0.091 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 161ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.118 | 0.091 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 131ms | 🔴 compile |
| boomerang | gcc -O0 | 0.069 | 0.035 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 15ms | 🔴 compile |
| boomerang | gcc -O2 | 0.069 | 0.035 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 13ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 233ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 267ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 457ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% (0/6) | #5 | 161 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 429ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 489ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% (0/6) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 489ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 722ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 678ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 764ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 753ms | ❌ usage: revng [-h] [--version]  |

### `classify_range`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O2 | 0.150 | 0.489 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 66ms | 🔴 compile |
| reko | gcc -O2 | 0.150 | 0.362 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 339ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.477 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 52ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.150 | 0.353 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 384ms | 🔴 compile |
| angr | gcc -O0 | 0.126 | 0.131 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 148ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.126 | 0.131 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 116ms | 🔴 compile |
| angr | gcc -O2 | 0.126 | 0.131 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 161ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.126 | 0.131 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 131ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.119 | 0.146 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 49ms | 🔴 compile |
| radare2 | gcc -O0 | 0.119 | 0.144 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 54ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.119 | 0.194 | 0.0% (0/5) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 337ms | 🔴 compile |
| reko | gcc -O0 | 0.097 | 0.082 | 0.0% (0/5) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 379ms | 🔴 compile |
| boomerang | gcc -O0 | 0.079 | 0.033 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 15ms | 🔴 compile |
| boomerang | gcc -O2 | 0.079 | 0.033 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 13ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 233ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 267ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 457ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 161 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 429ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 489ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 489ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 722ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 678ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 764ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 753ms | ❌ usage: revng [-h] [--version]  |

### `count_bits`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.638 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 54ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.408 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 379ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.607 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 49ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.150 | 0.430 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 337ms | 🔴 compile |
| radare2 | gcc -O2 | 0.150 | 0.536 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 66ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.520 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 52ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.150 | 0.358 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 384ms | 🔴 compile |
| reko | gcc -O2 | 0.132 | 0.208 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 339ms | 🔴 compile |
| angr | gcc -O0 | 0.129 | 0.144 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 148ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.129 | 0.144 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 116ms | 🔴 compile |
| angr | gcc -O2 | 0.129 | 0.144 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 161ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.129 | 0.144 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 131ms | 🔴 compile |
| boomerang | gcc -O0 | 0.089 | 0.088 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 15ms | 🔴 compile |
| boomerang | gcc -O2 | 0.089 | 0.088 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 13ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 233ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 267ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 457ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 489ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 161 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 429ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 489ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 722ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 678ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 764ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 753ms | ❌ usage: revng [-h] [--version]  |

### `crc32`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.299 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 106ms | ⚪ no_test |
| radare2 | clang -O0 | 0.150 | 0.371 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 119ms | ⚪ no_test |
| radare2 | clang-m32 -O0 | 0.150 | 0.316 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 102ms | ⚪ no_test |
| radare2 | clang -O2 | 0.141 | 0.205 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 123ms | ⚪ no_test |
| radare2 | clang-m32 -O2 | 0.126 | 0.132 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 109ms | ⚪ no_test |
| radare2 | gcc-m32 -O0 | 0.126 | 0.129 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 95ms | ⚪ no_test |
| radare2 | gcc-m32 -O2 | 0.125 | 0.176 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 104ms | ⚪ no_test |
| reko | clang -O0 | 0.123 | 0.116 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 584ms | ⚪ no_test |
| reko | clang-m32 -O0 | 0.123 | 0.116 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 643ms | ⚪ no_test |
| radare2 | gcc -O2 | 0.122 | 0.162 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 118ms | ⚪ no_test |
| reko | gcc -O0 | 0.120 | 0.102 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 634ms | ⚪ no_test |
| angr | gcc -O0 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 257ms | ⚪ no_test |
| angr | gcc -O2 | 0.115 | 0.075 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 328ms | ⚪ no_test |
| angr | gcc-m32 -O0 | 0.115 | 0.075 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 267ms | ⚪ no_test |
| angr | gcc-m32 -O2 | 0.115 | 0.075 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 271ms | ⚪ no_test |
| angr | clang -O0 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 341ms | ⚪ no_test |
| angr | clang -O2 | 0.115 | 0.075 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 273ms | ⚪ no_test |
| angr | clang-m32 -O0 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 240ms | ⚪ no_test |
| angr | clang-m32 -O2 | 0.115 | 0.075 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 265ms | ⚪ no_test |
| reko | gcc-m32 -O2 | 0.114 | 0.071 | 0.0% | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 695ms | ⚪ no_test |
| reko | gcc-m32 -O0 | 0.114 | 0.069 | 0.0% | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 667ms | ⚪ no_test |
| reko | gcc -O2 | 0.108 | 0.042 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 923ms | ⚪ no_test |
| reko | clang-m32 -O2 | 0.107 | 0.035 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 709ms | ⚪ no_test |
| reko | clang -O2 | 0.105 | 0.026 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 674ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.076 | 0.022 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 25ms | ⚪ no_test |
| boomerang | gcc -O2 | 0.076 | 0.022 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 25ms | ⚪ no_test |
| boomerang | clang -O0 | 0.076 | 0.022 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 25ms | ⚪ no_test |
| boomerang | clang -O2 | 0.076 | 0.022 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 28ms | ⚪ no_test |
| snowman | clang-m32 -O2 | 0.000 | 0.002 | 0.0% | #4 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 361ms | ⚪ no_test |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 386ms | ⚪ no_test |
| boomerang | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 572ms | ⚪ no_test |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #5 | 153 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 387ms | ⚪ no_test |
| boomerang | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 593ms | ⚪ no_test |
| snowman | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 461ms | ⚪ no_test |
| snowman | clang -O0 | 0.000 | 0.001 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 464ms | ⚪ no_test |
| boomerang | clang-m32 -O0 | 0.000 | 0.002 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 580ms | ⚪ no_test |
| snowman | clang-m32 -O0 | 0.000 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 392ms | ⚪ no_test |
| boomerang | clang-m32 -O2 | 0.000 | 0.002 | 0.0% | #5 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 585ms | ⚪ no_test |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 221 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 494ms | ⚪ no_test |
| snowman | clang -O2 | 0.000 | 0.001 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 483ms | ⚪ no_test |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 710ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 746ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 720ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 736ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 692ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 733ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 774ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 810ms | ❌ usage: revng [-h] [--version]  |

### `factorial`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.469 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 43ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.437 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 197ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.120 | 0.151 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 35ms | 🔴 compile |
| angr | gcc -O0 | 0.119 | 0.095 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 87ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.119 | 0.095 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 94ms | 🔴 compile |
| angr | gcc -O2 | 0.119 | 0.095 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 92ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.119 | 0.095 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 100ms | 🔴 compile |
| radare2 | gcc -O2 | 0.118 | 0.189 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 39ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.107 | 0.136 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 39ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.098 | 0.041 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 170ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.098 | 0.088 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 202ms | 🔴 compile |
| reko | gcc -O2 | 0.086 | 0.028 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 239ms | 🔴 compile |
| boomerang | gcc -O0 | 0.072 | 0.048 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 8ms | 🔴 compile |
| boomerang | gcc -O2 | 0.072 | 0.048 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 7ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 152ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 169ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.000 | 0.0% (0/5) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 505ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 280ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.000 | 0.0% (0/5) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 524ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% (0/5) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 351ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 732ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 533ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 784ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 578ms | ❌ usage: revng [-h] [--version]  |

### `fibonacci`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.543 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 43ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.289 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 197ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.526 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 35ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.150 | 0.545 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 170ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.122 | 0.208 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 39ms | 🔴 compile |
| angr | gcc -O0 | 0.121 | 0.105 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 87ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.121 | 0.105 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 94ms | 🔴 compile |
| angr | gcc -O2 | 0.121 | 0.105 | 0.0% (0/6) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 92ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.121 | 0.105 | 0.0% (0/6) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 100ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.120 | 0.200 | 0.0% (0/6) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 202ms | 🔴 compile |
| radare2 | gcc -O2 | 0.115 | 0.176 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 39ms | 🔴 compile |
| reko | gcc -O2 | 0.106 | 0.132 | 0.0% (0/6) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 239ms | 🔴 compile |
| boomerang | gcc -O0 | 0.068 | 0.029 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 8ms | 🔴 compile |
| boomerang | gcc -O2 | 0.068 | 0.029 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 7ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 152ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 169ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 280ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 351ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.000 | 0.0% (0/6) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 505ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.000 | 0.0% (0/6) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 524ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 732ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 533ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 784ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 578ms | ❌ usage: revng [-h] [--version]  |

### `fibonacci_iter`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.688 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 43ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.412 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 35ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.150 | 0.302 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 170ms | 🔴 compile |
| reko | gcc -O0 | 0.140 | 0.252 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 197ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.138 | 0.241 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 39ms | 🔴 compile |
| radare2 | gcc -O2 | 0.138 | 0.238 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 39ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.134 | 0.219 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 202ms | 🔴 compile |
| reko | gcc -O2 | 0.122 | 0.161 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 239ms | 🔴 compile |
| angr | gcc -O0 | 0.115 | 0.073 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 87ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.115 | 0.073 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 94ms | 🔴 compile |
| angr | gcc -O2 | 0.115 | 0.073 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 92ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.115 | 0.073 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 100ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.027 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 8ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.027 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 7ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 152ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 169ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 280ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 351ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 505ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 524ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 732ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 533ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 784ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 578ms | ❌ usage: revng [-h] [--version]  |

### `find_pair_value`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc-m32 -O0 | 0.150 | 0.307 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 63ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.141 | 0.204 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 378ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.140 | 0.248 | 0.0% (0/5) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 56ms | 🔴 compile |
| reko | gcc -O0 | 0.138 | 0.190 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 372ms | 🔴 compile |
| radare2 | gcc -O0 | 0.134 | 0.172 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 73ms | 🔴 compile |
| angr | gcc -O0 | 0.128 | 0.139 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 198ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.128 | 0.139 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 157ms | 🔴 compile |
| angr | gcc -O2 | 0.128 | 0.139 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 173ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.128 | 0.139 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 182ms | 🔴 compile |
| reko | gcc -O2 | 0.126 | 0.131 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 365ms | 🔴 compile |
| radare2 | gcc -O2 | 0.125 | 0.174 | 0.0% (0/5) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 73ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.108 | 0.040 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 446ms | 🔴 compile |
| boomerang | gcc -O0 | 0.078 | 0.029 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 14ms | 🔴 compile |
| boomerang | gcc -O2 | 0.078 | 0.029 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 15ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 333ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 322ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 155 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 415ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 469ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 220 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 430ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 427ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 723ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 748ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 725ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 713ms | ❌ usage: revng [-h] [--version]  |

### `find_substring`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.384 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 157ms | ⚪ no_test |
| radare2 | gcc-m32 -O0 | 0.150 | 0.358 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 182ms | ⚪ no_test |
| radare2 | gcc-m32 -O2 | 0.150 | 0.352 | 0.0% | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 152ms | ⚪ no_test |
| radare2 | gcc -O2 | 0.126 | 0.228 | 0.0% | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 157ms | ⚪ no_test |
| radare2 | clang-m32 -O2 | 0.116 | 0.228 | 0.0% | #1 | 0 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 148ms | ⚪ no_test |
| reko | clang-m32 -O0 | 0.113 | 0.167 | 0.0% | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 923ms | ⚪ no_test |
| reko | gcc-m32 -O0 | 0.111 | 0.156 | 0.0% | #2 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 956ms | ⚪ no_test |
| angr | gcc -O0 | 0.111 | 0.054 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 409ms | ⚪ no_test |
| angr | gcc -O2 | 0.111 | 0.054 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 411ms | ⚪ no_test |
| angr | gcc-m32 -O0 | 0.111 | 0.054 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 470ms | ⚪ no_test |
| angr | gcc-m32 -O2 | 0.111 | 0.054 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 379ms | ⚪ no_test |
| angr | clang -O0 | 0.111 | 0.054 | 0.0% | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 391ms | ⚪ no_test |
| angr | clang -O2 | 0.111 | 0.054 | 0.0% | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 390ms | ⚪ no_test |
| angr | clang-m32 -O0 | 0.111 | 0.054 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 406ms | ⚪ no_test |
| angr | clang-m32 -O2 | 0.111 | 0.054 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 334ms | ⚪ no_test |
| reko | clang -O0 | 0.110 | 0.149 | 0.0% | #2 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1028ms | ⚪ no_test |
| reko | gcc -O0 | 0.102 | 0.111 | 0.0% | #3 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 885ms | ⚪ no_test |
| radare2 | clang -O0 | 0.100 | 0.099 | 0.0% | #3 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 149ms | ⚪ no_test |
| radare2 | clang-m32 -O0 | 0.097 | 0.086 | 0.0% | #3 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 137ms | ⚪ no_test |
| radare2 | clang -O2 | 0.087 | 0.086 | 0.0% | #2 | 0 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 162ms | ⚪ no_test |
| reko | clang-m32 -O2 | 0.085 | 0.146 | 0.0% | #3 | 1 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 931ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.081 | 0.045 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 37ms | ⚪ no_test |
| boomerang | gcc -O2 | 0.081 | 0.045 | 0.0% | #3 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 41ms | ⚪ no_test |
| boomerang | clang -O2 | 0.081 | 0.045 | 0.0% | #3 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 42ms | ⚪ no_test |
| reko | gcc-m32 -O2 | 0.075 | 0.116 | 0.0% | #3 | 2 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 918ms | ⚪ no_test |
| reko | clang -O2 | 0.072 | 0.080 | 0.0% | #4 | 1 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 907ms | ⚪ no_test |
| reko | gcc -O2 | 0.068 | 0.081 | 0.0% | #4 | 2 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 923ms | ⚪ no_test |
| boomerang | clang -O0 | 0.066 | 0.020 | 0.0% | #4 | 2 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 131ms | ⚪ no_test |
| boomerang | gcc-m32 -O2 | 0.001 | 0.006 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 860ms | ⚪ no_test |
| boomerang | clang-m32 -O0 | 0.001 | 0.006 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 842ms | ⚪ no_test |
| boomerang | gcc-m32 -O0 | 0.001 | 0.006 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 850ms | ⚪ no_test |
| boomerang | clang-m32 -O2 | 0.001 | 0.006 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 854ms | ⚪ no_test |
| snowman | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 336ms | ⚪ no_test |
| snowman | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% | #5 | 153 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 343ms | ⚪ no_test |
| snowman | clang-m32 -O0 | 0.001 | 0.003 | 0.0% | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 353ms | ⚪ no_test |
| snowman | gcc -O0 | 0.001 | 0.002 | 0.0% | #5 | 225 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 438ms | ⚪ no_test |
| snowman | clang -O0 | 0.001 | 0.002 | 0.0% | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 424ms | ⚪ no_test |
| snowman | clang-m32 -O2 | 0.001 | 0.002 | 0.0% | #5 | 156 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 390ms | ⚪ no_test |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 488ms | ⚪ no_test |
| snowman | clang -O2 | 0.000 | 0.002 | 0.0% | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 408ms | ⚪ no_test |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 701ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 703ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 828ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 734ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 759ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 648ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 749ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 724ms | ❌ usage: revng [-h] [--version]  |

### `gcd`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.302 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 43ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.369 | 0.0% (0/6) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 197ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.486 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 35ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.150 | 0.546 | 0.0% (0/6) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 170ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.149 | 0.294 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 39ms | 🔴 compile |
| radare2 | gcc -O2 | 0.148 | 0.242 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 39ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.140 | 0.200 | 0.0% (0/6) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 202ms | 🔴 compile |
| reko | gcc -O2 | 0.138 | 0.188 | 0.0% (0/6) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 239ms | 🔴 compile |
| angr | gcc -O0 | 0.130 | 0.149 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 87ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.130 | 0.149 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 94ms | 🔴 compile |
| angr | gcc -O2 | 0.130 | 0.149 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 92ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.130 | 0.149 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 100ms | 🔴 compile |
| boomerang | gcc -O0 | 0.088 | 0.082 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 8ms | 🔴 compile |
| boomerang | gcc -O2 | 0.088 | 0.082 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 7ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 152ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 169ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 280ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 351ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 505ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 524ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 732ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 533ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 784ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 578ms | ❌ usage: revng [-h] [--version]  |

### `linear_search`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.389 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 43ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.369 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 35ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.150 | 0.354 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 170ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.369 | 0.0% (0/6) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 39ms | 🔴 compile |
| reko | gcc -O0 | 0.140 | 0.249 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 197ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.139 | 0.247 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 202ms | 🔴 compile |
| radare2 | gcc -O2 | 0.139 | 0.296 | 0.0% (0/6) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 39ms | 🔴 compile |
| angr | gcc -O0 | 0.130 | 0.148 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 87ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.130 | 0.148 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 94ms | 🔴 compile |
| angr | gcc -O2 | 0.130 | 0.148 | 0.0% (0/6) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 92ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.130 | 0.148 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 100ms | 🔴 compile |
| reko | gcc -O2 | 0.111 | 0.104 | 0.0% (0/6) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 239ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.028 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 8ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.028 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 7ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 152ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 169ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 280ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 351ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 505ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 524ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 732ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 533ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 784ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 578ms | ❌ usage: revng [-h] [--version]  |

### `manipulate_bitfields`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O2 | 0.150 | 0.372 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 213ms | ⚪ no_test |
| radare2 | gcc-m32 -O2 | 0.150 | 0.367 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 179ms | ⚪ no_test |
| radare2 | clang -O2 | 0.150 | 0.384 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 160ms | ⚪ no_test |
| radare2 | clang-m32 -O2 | 0.150 | 0.378 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 144ms | ⚪ no_test |
| radare2 | gcc-m32 -O0 | 0.133 | 0.217 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 149ms | ⚪ no_test |
| radare2 | clang-m32 -O0 | 0.133 | 0.214 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 133ms | ⚪ no_test |
| reko | gcc -O2 | 0.130 | 0.149 | 0.0% | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1035ms | ⚪ no_test |
| radare2 | clang -O0 | 0.130 | 0.198 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 174ms | ⚪ no_test |
| reko | clang -O2 | 0.127 | 0.135 | 0.0% | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 976ms | ⚪ no_test |
| reko | gcc-m32 -O0 | 0.123 | 0.117 | 0.0% | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 945ms | ⚪ no_test |
| reko | clang -O0 | 0.123 | 0.116 | 0.0% | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 914ms | ⚪ no_test |
| reko | clang-m32 -O0 | 0.120 | 0.100 | 0.0% | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1033ms | ⚪ no_test |
| reko | gcc -O0 | 0.120 | 0.099 | 0.0% | #1 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 956ms | ⚪ no_test |
| reko | clang-m32 -O2 | 0.119 | 0.094 | 0.0% | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1308ms | ⚪ no_test |
| radare2 | gcc -O0 | 0.118 | 0.140 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 160ms | ⚪ no_test |
| angr | gcc -O0 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 410ms | ⚪ no_test |
| angr | gcc -O2 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 411ms | ⚪ no_test |
| angr | gcc-m32 -O0 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 449ms | ⚪ no_test |
| angr | gcc-m32 -O2 | 0.115 | 0.075 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 429ms | ⚪ no_test |
| angr | clang -O0 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 419ms | ⚪ no_test |
| angr | clang -O2 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 454ms | ⚪ no_test |
| angr | clang-m32 -O0 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 384ms | ⚪ no_test |
| angr | clang-m32 -O2 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 364ms | ⚪ no_test |
| reko | gcc-m32 -O2 | 0.114 | 0.068 | 0.0% | #3 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 947ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.071 | 0.047 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 37ms | ⚪ no_test |
| boomerang | gcc -O2 | 0.071 | 0.047 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 42ms | ⚪ no_test |
| boomerang | clang -O0 | 0.071 | 0.047 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 40ms | ⚪ no_test |
| boomerang | clang -O2 | 0.071 | 0.047 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 39ms | ⚪ no_test |
| boomerang | gcc-m32 -O0 | 0.001 | 0.004 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 879ms | ⚪ no_test |
| boomerang | gcc-m32 -O2 | 0.001 | 0.004 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 875ms | ⚪ no_test |
| boomerang | clang-m32 -O0 | 0.001 | 0.004 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 895ms | ⚪ no_test |
| boomerang | clang-m32 -O2 | 0.001 | 0.004 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 841ms | ⚪ no_test |
| snowman | clang-m32 -O0 | 0.001 | 0.003 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 325ms | ⚪ no_test |
| snowman | clang-m32 -O2 | 0.001 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 340ms | ⚪ no_test |
| snowman | gcc -O0 | 0.000 | 0.002 | 0.0% | #5 | 221 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 405ms | ⚪ no_test |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 439ms | ⚪ no_test |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #5 | 153 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 391ms | ⚪ no_test |
| snowman | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 458ms | ⚪ no_test |
| snowman | clang -O0 | 0.000 | 0.002 | 0.0% | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 401ms | ⚪ no_test |
| snowman | clang -O2 | 0.000 | 0.002 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 403ms | ⚪ no_test |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 737ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 803ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 756ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 736ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 719ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 705ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 763ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 814ms | ❌ usage: revng [-h] [--version]  |

### `matrix_multiply`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.559 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 160ms | ⚪ no_test |
| radare2 | clang -O0 | 0.150 | 0.679 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 174ms | ⚪ no_test |
| radare2 | clang-m32 -O0 | 0.150 | 0.517 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 133ms | ⚪ no_test |
| reko | gcc-m32 -O0 | 0.140 | 0.199 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 945ms | ⚪ no_test |
| reko | clang-m32 -O0 | 0.140 | 0.198 | 0.0% | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1033ms | ⚪ no_test |
| radare2 | gcc-m32 -O0 | 0.129 | 0.145 | 0.0% | #2 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 149ms | ⚪ no_test |
| radare2 | gcc -O2 | 0.123 | 0.165 | 0.0% | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 213ms | ⚪ no_test |
| radare2 | clang -O2 | 0.122 | 0.209 | 0.0% | #1 | 0 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 160ms | ⚪ no_test |
| reko | gcc -O0 | 0.119 | 0.096 | 0.0% | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 956ms | ⚪ no_test |
| reko | clang -O0 | 0.118 | 0.090 | 0.0% | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 914ms | ⚪ no_test |
| radare2 | gcc-m32 -O2 | 0.117 | 0.137 | 0.0% | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 179ms | ⚪ no_test |
| radare2 | clang-m32 -O2 | 0.114 | 0.169 | 0.0% | #1 | 0 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 144ms | ⚪ no_test |
| angr | gcc -O0 | 0.112 | 0.060 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 410ms | ⚪ no_test |
| angr | gcc -O2 | 0.112 | 0.060 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 411ms | ⚪ no_test |
| angr | gcc-m32 -O0 | 0.112 | 0.060 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 449ms | ⚪ no_test |
| angr | gcc-m32 -O2 | 0.112 | 0.060 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 429ms | ⚪ no_test |
| angr | clang -O0 | 0.112 | 0.060 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 419ms | ⚪ no_test |
| angr | clang -O2 | 0.112 | 0.060 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 454ms | ⚪ no_test |
| angr | clang-m32 -O0 | 0.112 | 0.060 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 384ms | ⚪ no_test |
| angr | clang-m32 -O2 | 0.112 | 0.060 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 364ms | ⚪ no_test |
| reko | gcc -O2 | 0.107 | 0.084 | 0.0% | #3 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1035ms | ⚪ no_test |
| reko | gcc-m32 -O2 | 0.097 | 0.034 | 0.0% | #3 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 947ms | ⚪ no_test |
| reko | clang -O2 | 0.096 | 0.081 | 0.0% | #3 | 0 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 976ms | ⚪ no_test |
| reko | clang-m32 -O2 | 0.096 | 0.081 | 0.0% | #3 | 0 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1308ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.084 | 0.060 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 37ms | ⚪ no_test |
| boomerang | gcc -O2 | 0.084 | 0.060 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 42ms | ⚪ no_test |
| boomerang | clang -O0 | 0.084 | 0.060 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 40ms | ⚪ no_test |
| boomerang | clang -O2 | 0.084 | 0.060 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 39ms | ⚪ no_test |
| boomerang | clang-m32 -O2 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 841ms | ⚪ no_test |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 879ms | ⚪ no_test |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 875ms | ⚪ no_test |
| boomerang | clang-m32 -O0 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 895ms | ⚪ no_test |
| snowman | clang-m32 -O0 | 0.001 | 0.003 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 325ms | ⚪ no_test |
| snowman | clang-m32 -O2 | 0.001 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 340ms | ⚪ no_test |
| snowman | gcc -O0 | 0.000 | 0.002 | 0.0% | #5 | 221 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 405ms | ⚪ no_test |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #5 | 153 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 391ms | ⚪ no_test |
| snowman | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 458ms | ⚪ no_test |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 439ms | ⚪ no_test |
| snowman | clang -O0 | 0.000 | 0.002 | 0.0% | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 401ms | ⚪ no_test |
| snowman | clang -O2 | 0.000 | 0.002 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 403ms | ⚪ no_test |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 737ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 803ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 756ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 736ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 719ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 705ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 763ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 814ms | ❌ usage: revng [-h] [--version]  |

### `max`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.415 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 43ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.315 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 197ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.389 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 35ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.150 | 0.395 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 170ms | 🔴 compile |
| radare2 | gcc -O2 | 0.150 | 0.630 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 39ms | 🔴 compile |
| reko | gcc -O2 | 0.150 | 0.315 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 239ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.391 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 39ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.150 | 0.398 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 202ms | 🔴 compile |
| angr | gcc -O0 | 0.128 | 0.141 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 87ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.128 | 0.141 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 94ms | 🔴 compile |
| angr | gcc -O2 | 0.128 | 0.141 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 92ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.128 | 0.141 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 100ms | 🔴 compile |
| boomerang | gcc -O0 | 0.068 | 0.032 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 8ms | 🔴 compile |
| boomerang | gcc -O2 | 0.068 | 0.032 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 7ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 152ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 169ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.000 | 0.0% (0/6) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 505ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 280ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.000 | 0.0% (0/6) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 524ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 351ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 732ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 533ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 784ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 578ms | ❌ usage: revng [-h] [--version]  |

### `pointer_stride_sum`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O2 | 0.150 | 0.330 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 73ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.367 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 56ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.142 | 0.209 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 63ms | 🔴 compile |
| radare2 | gcc -O0 | 0.141 | 0.206 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 73ms | 🔴 compile |
| reko | gcc -O2 | 0.140 | 0.198 | 0.0% (0/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 365ms | 🔴 compile |
| angr | gcc -O0 | 0.123 | 0.115 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 198ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.123 | 0.115 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 157ms | 🔴 compile |
| angr | gcc -O2 | 0.123 | 0.115 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 173ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.123 | 0.115 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 182ms | 🔴 compile |
| reko | gcc -O0 | 0.122 | 0.108 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 372ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.120 | 0.102 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 378ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.109 | 0.097 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 446ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 14ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 15ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 333ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 322ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 469ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 155 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 415ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 220 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 430ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 427ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 723ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 748ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 725ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 713ms | ❌ usage: revng [-h] [--version]  |

### `power`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| reko | gcc-m32 -O0 | 0.138 | 0.188 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 170ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.133 | 0.216 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 202ms | 🔴 compile |
| radare2 | gcc -O0 | 0.124 | 0.168 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 43ms | 🔴 compile |
| reko | gcc -O0 | 0.123 | 0.118 | 0.0% (0/6) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 197ms | 🔴 compile |
| reko | gcc -O2 | 0.116 | 0.129 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 239ms | 🔴 compile |
| angr | gcc -O0 | 0.116 | 0.078 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 87ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.116 | 0.078 | 0.0% (0/6) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 94ms | 🔴 compile |
| angr | gcc -O2 | 0.116 | 0.078 | 0.0% (0/6) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 92ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.116 | 0.078 | 0.0% (0/6) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 100ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.112 | 0.111 | 0.0% (0/6) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 35ms | 🔴 compile |
| radare2 | gcc -O2 | 0.102 | 0.111 | 0.0% (0/6) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 39ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.099 | 0.093 | 0.0% (0/6) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 39ms | 🔴 compile |
| boomerang | gcc -O0 | 0.081 | 0.043 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 8ms | 🔴 compile |
| boomerang | gcc -O2 | 0.081 | 0.043 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 7ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 152ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 169ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 505ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 280ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 524ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 351ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 732ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 533ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 784ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 578ms | ❌ usage: revng [-h] [--version]  |

### `process_code`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O2 | 0.148 | 0.288 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 39ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.146 | 0.282 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 39ms | 🔴 compile |
| angr | gcc -O0 | 0.123 | 0.114 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 87ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.123 | 0.114 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 94ms | 🔴 compile |
| angr | gcc -O2 | 0.123 | 0.114 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 92ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.123 | 0.114 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 100ms | 🔴 compile |
| reko | gcc -O0 | 0.116 | 0.078 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 197ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.115 | 0.075 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 170ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.112 | 0.160 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 202ms | 🔴 compile |
| reko | gcc -O2 | 0.096 | 0.079 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 239ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.094 | 0.121 | 0.0% (0/5) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 35ms | 🔴 compile |
| radare2 | gcc -O0 | 0.075 | 0.025 | 0.0% (0/5) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 43ms | 🔴 compile |
| boomerang | gcc -O0 | 0.067 | 0.025 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 8ms | 🔴 compile |
| boomerang | gcc -O2 | 0.067 | 0.025 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 7ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.004 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 169ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.004 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 152ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 280ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 524ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 351ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 505ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 732ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 533ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 784ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 578ms | ❌ usage: revng [-h] [--version]  |

### `rc4_crypt`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.424 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 106ms | ⚪ no_test |
| radare2 | gcc-m32 -O0 | 0.150 | 0.292 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 95ms | ⚪ no_test |
| radare2 | clang -O0 | 0.150 | 0.395 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 119ms | ⚪ no_test |
| radare2 | clang-m32 -O0 | 0.150 | 0.430 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 102ms | ⚪ no_test |
| radare2 | gcc -O2 | 0.143 | 0.267 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 118ms | ⚪ no_test |
| radare2 | clang -O2 | 0.133 | 0.263 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 123ms | ⚪ no_test |
| radare2 | clang-m32 -O2 | 0.131 | 0.257 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 109ms | ⚪ no_test |
| radare2 | gcc-m32 -O2 | 0.130 | 0.200 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 104ms | ⚪ no_test |
| reko | gcc-m32 -O0 | 0.127 | 0.135 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 667ms | ⚪ no_test |
| reko | clang -O0 | 0.124 | 0.119 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 584ms | ⚪ no_test |
| reko | gcc -O0 | 0.124 | 0.118 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 634ms | ⚪ no_test |
| reko | clang-m32 -O0 | 0.121 | 0.106 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 643ms | ⚪ no_test |
| angr | gcc -O0 | 0.113 | 0.067 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 257ms | ⚪ no_test |
| angr | gcc -O2 | 0.113 | 0.067 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 328ms | ⚪ no_test |
| angr | gcc-m32 -O0 | 0.113 | 0.067 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 267ms | ⚪ no_test |
| angr | gcc-m32 -O2 | 0.113 | 0.067 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 271ms | ⚪ no_test |
| angr | clang -O0 | 0.113 | 0.067 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 341ms | ⚪ no_test |
| angr | clang -O2 | 0.113 | 0.067 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 273ms | ⚪ no_test |
| angr | clang-m32 -O0 | 0.113 | 0.067 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 240ms | ⚪ no_test |
| angr | clang-m32 -O2 | 0.113 | 0.067 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 265ms | ⚪ no_test |
| reko | gcc -O2 | 0.109 | 0.096 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 923ms | ⚪ no_test |
| reko | gcc-m32 -O2 | 0.104 | 0.068 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 695ms | ⚪ no_test |
| reko | clang-m32 -O2 | 0.101 | 0.055 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 709ms | ⚪ no_test |
| reko | clang -O2 | 0.100 | 0.049 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 674ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.079 | 0.034 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 25ms | ⚪ no_test |
| boomerang | gcc -O2 | 0.079 | 0.034 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 25ms | ⚪ no_test |
| boomerang | clang -O0 | 0.079 | 0.034 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 25ms | ⚪ no_test |
| boomerang | clang -O2 | 0.079 | 0.034 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 28ms | ⚪ no_test |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 572ms | ⚪ no_test |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 593ms | ⚪ no_test |
| boomerang | clang-m32 -O0 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 580ms | ⚪ no_test |
| boomerang | clang-m32 -O2 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 585ms | ⚪ no_test |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 386ms | ⚪ no_test |
| snowman | gcc -O0 | 0.000 | 0.002 | 0.0% | #5 | 221 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 494ms | ⚪ no_test |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 461ms | ⚪ no_test |
| snowman | clang -O0 | 0.000 | 0.002 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 464ms | ⚪ no_test |
| snowman | clang -O2 | 0.000 | 0.002 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 483ms | ⚪ no_test |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 153 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 387ms | ⚪ no_test |
| snowman | clang-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 392ms | ⚪ no_test |
| snowman | clang-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 361ms | ⚪ no_test |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 710ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 746ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 720ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 736ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 692ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 733ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 774ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 810ms | ❌ usage: revng [-h] [--version]  |

### `rc4_init`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.501 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 106ms | ⚪ no_test |
| radare2 | gcc-m32 -O0 | 0.150 | 0.301 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 95ms | ⚪ no_test |
| radare2 | clang -O0 | 0.150 | 0.291 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 119ms | ⚪ no_test |
| radare2 | clang-m32 -O0 | 0.150 | 0.350 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 102ms | ⚪ no_test |
| reko | clang -O0 | 0.136 | 0.178 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 584ms | ⚪ no_test |
| radare2 | gcc-m32 -O2 | 0.135 | 0.175 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 104ms | ⚪ no_test |
| reko | gcc-m32 -O0 | 0.127 | 0.137 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 667ms | ⚪ no_test |
| reko | gcc -O0 | 0.126 | 0.129 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 634ms | ⚪ no_test |
| radare2 | clang-m32 -O2 | 0.122 | 0.159 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 109ms | ⚪ no_test |
| reko | clang-m32 -O0 | 0.117 | 0.085 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 643ms | ⚪ no_test |
| reko | clang -O2 | 0.115 | 0.073 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 674ms | ⚪ no_test |
| reko | gcc-m32 -O2 | 0.114 | 0.070 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 695ms | ⚪ no_test |
| angr | gcc -O0 | 0.114 | 0.068 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 257ms | ⚪ no_test |
| angr | gcc -O2 | 0.114 | 0.068 | 0.0% | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 328ms | ⚪ no_test |
| angr | gcc-m32 -O0 | 0.114 | 0.068 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 267ms | ⚪ no_test |
| angr | gcc-m32 -O2 | 0.114 | 0.068 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 271ms | ⚪ no_test |
| angr | clang -O0 | 0.114 | 0.068 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 341ms | ⚪ no_test |
| angr | clang -O2 | 0.114 | 0.068 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 273ms | ⚪ no_test |
| angr | clang-m32 -O0 | 0.114 | 0.068 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 240ms | ⚪ no_test |
| angr | clang-m32 -O2 | 0.114 | 0.068 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 265ms | ⚪ no_test |
| reko | clang-m32 -O2 | 0.113 | 0.065 | 0.0% | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 709ms | ⚪ no_test |
| reko | gcc -O2 | 0.109 | 0.044 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 923ms | ⚪ no_test |
| radare2 | gcc -O2 | 0.105 | 0.025 | 0.0% | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 118ms | ⚪ no_test |
| radare2 | clang -O2 | 0.102 | 0.058 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 123ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.080 | 0.040 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 25ms | ⚪ no_test |
| boomerang | gcc -O2 | 0.080 | 0.040 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 25ms | ⚪ no_test |
| boomerang | clang -O0 | 0.080 | 0.040 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 25ms | ⚪ no_test |
| boomerang | clang -O2 | 0.080 | 0.040 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 28ms | ⚪ no_test |
| boomerang | gcc-m32 -O2 | 0.001 | 0.004 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 593ms | ⚪ no_test |
| boomerang | clang-m32 -O0 | 0.001 | 0.004 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 580ms | ⚪ no_test |
| boomerang | clang-m32 -O2 | 0.001 | 0.004 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 585ms | ⚪ no_test |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 572ms | ⚪ no_test |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 386ms | ⚪ no_test |
| snowman | clang-m32 -O2 | 0.000 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 361ms | ⚪ no_test |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 221 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 494ms | ⚪ no_test |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #5 | 153 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 387ms | ⚪ no_test |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 461ms | ⚪ no_test |
| snowman | clang -O0 | 0.000 | 0.002 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 464ms | ⚪ no_test |
| snowman | clang -O2 | 0.000 | 0.001 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 483ms | ⚪ no_test |
| snowman | clang-m32 -O0 | 0.000 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 392ms | ⚪ no_test |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 710ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 746ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 720ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 736ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 692ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 733ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 774ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 810ms | ❌ usage: revng [-h] [--version]  |

### `reverse_in_place`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc-m32 -O0 | 0.150 | 0.264 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 63ms | 🔴 compile |
| radare2 | gcc -O0 | 0.149 | 0.244 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 73ms | 🔴 compile |
| reko | gcc -O0 | 0.131 | 0.156 | 0.0% (0/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 372ms | 🔴 compile |
| radare2 | gcc -O2 | 0.123 | 0.164 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 73ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.117 | 0.133 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 56ms | 🔴 compile |
| angr | gcc -O0 | 0.116 | 0.081 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 198ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.116 | 0.081 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 157ms | 🔴 compile |
| angr | gcc -O2 | 0.116 | 0.081 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 173ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.116 | 0.081 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 182ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.113 | 0.067 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 378ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.104 | 0.069 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 446ms | 🔴 compile |
| reko | gcc -O2 | 0.103 | 0.064 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 365ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.028 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 14ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.028 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 15ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 333ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 322ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% (0/5) | #5 | 155 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 415ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 220 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 430ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 427ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 469ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 723ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 748ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 725ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 713ms | ❌ usage: revng [-h] [--version]  |

### `reverse_string`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc-m32 -O0 | 0.150 | 0.353 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 182ms | ⚪ no_test |
| radare2 | gcc-m32 -O2 | 0.148 | 0.291 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 152ms | ⚪ no_test |
| radare2 | gcc -O0 | 0.146 | 0.281 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 157ms | ⚪ no_test |
| reko | gcc -O2 | 0.142 | 0.261 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 923ms | ⚪ no_test |
| radare2 | clang-m32 -O2 | 0.140 | 0.248 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 148ms | ⚪ no_test |
| radare2 | clang-m32 -O0 | 0.135 | 0.225 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 137ms | ⚪ no_test |
| radare2 | clang -O0 | 0.133 | 0.215 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 149ms | ⚪ no_test |
| radare2 | clang -O2 | 0.132 | 0.209 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 162ms | ⚪ no_test |
| radare2 | gcc -O2 | 0.129 | 0.197 | 0.0% | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 157ms | ⚪ no_test |
| reko | clang -O0 | 0.117 | 0.138 | 0.0% | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1028ms | ⚪ no_test |
| reko | gcc-m32 -O0 | 0.117 | 0.133 | 0.0% | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 956ms | ⚪ no_test |
| angr | gcc -O0 | 0.117 | 0.083 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 409ms | ⚪ no_test |
| angr | gcc -O2 | 0.117 | 0.083 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 411ms | ⚪ no_test |
| angr | gcc-m32 -O0 | 0.117 | 0.083 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 470ms | ⚪ no_test |
| angr | gcc-m32 -O2 | 0.117 | 0.083 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 379ms | ⚪ no_test |
| angr | clang -O0 | 0.117 | 0.083 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 391ms | ⚪ no_test |
| angr | clang -O2 | 0.117 | 0.083 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 390ms | ⚪ no_test |
| angr | clang-m32 -O0 | 0.117 | 0.083 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 406ms | ⚪ no_test |
| angr | clang-m32 -O2 | 0.117 | 0.083 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 334ms | ⚪ no_test |
| reko | gcc -O0 | 0.116 | 0.132 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 885ms | ⚪ no_test |
| reko | clang-m32 -O0 | 0.116 | 0.129 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 923ms | ⚪ no_test |
| reko | clang -O2 | 0.111 | 0.154 | 0.0% | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 907ms | ⚪ no_test |
| reko | clang-m32 -O2 | 0.106 | 0.128 | 0.0% | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 931ms | ⚪ no_test |
| reko | gcc-m32 -O2 | 0.103 | 0.113 | 0.0% | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 918ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.079 | 0.036 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 37ms | ⚪ no_test |
| boomerang | gcc -O2 | 0.079 | 0.036 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 41ms | ⚪ no_test |
| boomerang | clang -O2 | 0.079 | 0.036 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 42ms | ⚪ no_test |
| boomerang | clang -O0 | 0.057 | 0.023 | 0.0% | #4 | 2 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 131ms | ⚪ no_test |
| boomerang | gcc-m32 -O0 | 0.001 | 0.005 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 850ms | ⚪ no_test |
| boomerang | gcc-m32 -O2 | 0.001 | 0.005 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 860ms | ⚪ no_test |
| boomerang | clang-m32 -O0 | 0.001 | 0.005 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 842ms | ⚪ no_test |
| boomerang | clang-m32 -O2 | 0.001 | 0.005 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 854ms | ⚪ no_test |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 225 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 438ms | ⚪ no_test |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 488ms | ⚪ no_test |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 336ms | ⚪ no_test |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 153 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 343ms | ⚪ no_test |
| snowman | clang -O0 | 0.000 | 0.001 | 0.0% | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 424ms | ⚪ no_test |
| snowman | clang-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 353ms | ⚪ no_test |
| snowman | clang -O2 | 0.000 | 0.001 | 0.0% | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 408ms | ⚪ no_test |
| snowman | clang-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 156 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 390ms | ⚪ no_test |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 701ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 703ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 828ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 734ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 759ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 648ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 749ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 724ms | ❌ usage: revng [-h] [--version]  |

### `saturating_add`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O2 | 0.150 | 0.599 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 66ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.586 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 52ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.142 | 0.211 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 384ms | 🔴 compile |
| reko | gcc -O0 | 0.137 | 0.187 | 0.0% (0/5) | #1 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 379ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.135 | 0.176 | 0.0% (0/5) | #1 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 337ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.126 | 0.228 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 49ms | 🔴 compile |
| radare2 | gcc -O0 | 0.126 | 0.227 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 54ms | 🔴 compile |
| angr | gcc -O0 | 0.117 | 0.085 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 148ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.117 | 0.085 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 116ms | 🔴 compile |
| angr | gcc -O2 | 0.117 | 0.085 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 161ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.117 | 0.085 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 131ms | 🔴 compile |
| reko | gcc -O2 | 0.115 | 0.126 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 339ms | 🔴 compile |
| boomerang | gcc -O0 | 0.067 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 15ms | 🔴 compile |
| boomerang | gcc -O2 | 0.067 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 13ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.004 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 233ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 267ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 457ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 161 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 429ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 489ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 489ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 722ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 678ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 764ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 753ms | ❌ usage: revng [-h] [--version]  |

### `signum`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.541 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 54ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.423 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 379ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.573 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 49ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.150 | 0.408 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 337ms | 🔴 compile |
| radare2 | gcc -O2 | 0.150 | 0.497 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 66ms | 🔴 compile |
| reko | gcc -O2 | 0.150 | 0.484 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 339ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.563 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 52ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.150 | 0.532 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 384ms | 🔴 compile |
| angr | gcc -O0 | 0.126 | 0.127 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 148ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.126 | 0.127 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 116ms | 🔴 compile |
| angr | gcc -O2 | 0.126 | 0.127 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 161ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.126 | 0.127 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 131ms | 🔴 compile |
| boomerang | gcc -O0 | 0.069 | 0.037 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 15ms | 🔴 compile |
| boomerang | gcc -O2 | 0.069 | 0.037 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 13ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 233ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 267ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 457ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 161 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 429ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 489ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 489ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 722ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 678ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 764ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 753ms | ❌ usage: revng [-h] [--version]  |

### `sum_array`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.286 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 73ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.431 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 63ms | 🔴 compile |
| reko | gcc -O0 | 0.145 | 0.224 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 372ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.125 | 0.123 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 378ms | 🔴 compile |
| angr | gcc -O0 | 0.124 | 0.120 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 198ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.124 | 0.120 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 157ms | 🔴 compile |
| angr | gcc -O2 | 0.124 | 0.120 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 173ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.124 | 0.120 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 182ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.123 | 0.165 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 56ms | 🔴 compile |
| radare2 | gcc -O2 | 0.119 | 0.143 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 73ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.116 | 0.080 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 446ms | 🔴 compile |
| reko | gcc -O2 | 0.111 | 0.055 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 365ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.028 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 14ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.028 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 15ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 333ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 322ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 155 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 415ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 220 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 430ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 427ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 469ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 723ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 748ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 725ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 713ms | ❌ usage: revng [-h] [--version]  |

---

## Overfitting Analysis

Functions where **all** decompilers scored below 0.3 are marked as objectively hard.
Functions where **only Fission** scored below 0.3 are marked as quality gaps.

**Objectively hard functions (28):** `count_bits`, `clamp`, `signum`, `checksum`, `classify_range`, `saturating_add`, `rc4_init`, `rc4_crypt`, `crc32`, `sum_array`, `reverse_in_place`, `find_pair_value`, `accumulate_pairs`, `pointer_stride_sum`, `manipulate_bitfields`, `matrix_multiply`, `fibonacci`, `fibonacci_iter`, `max`, `bubble_sort`, `linear_search`, `binary_search`, `factorial`, `gcd`, `power`, `process_code`, `reverse_string`, `find_substring`