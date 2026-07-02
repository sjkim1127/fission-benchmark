# Fission Benchmark Report

**Generated:** 2026-07-02 03:29 UTC
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
| radare2 | gcc -O0 | 0.150 | 0.435 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 95ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.289 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 86ms | 🔴 compile |
| reko | gcc -O0 | 0.141 | 0.204 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 517ms | 🔴 compile |
| reko | gcc -O2 | 0.125 | 0.124 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 473ms | 🔴 compile |
| radare2 | gcc -O2 | 0.121 | 0.153 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 88ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.120 | 0.102 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 545ms | 🔴 compile |
| angr | gcc -O0 | 0.119 | 0.097 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 284ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.119 | 0.097 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 234ms | 🔴 compile |
| angr | gcc -O2 | 0.119 | 0.097 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 235ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.119 | 0.097 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 277ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.113 | 0.116 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 77ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.112 | 0.060 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 523ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 21ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 17ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 508ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 499ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 603ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 155 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 577ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 220 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 579ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 501ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 929ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 919ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 870ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 813ms | ❌ usage: revng [-h] [--version]  |

### `binary_search`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.389 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 58ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.409 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 47ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.124 | 0.172 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 263ms | 🔴 compile |
| radare2 | gcc -O2 | 0.120 | 0.252 | 0.0% (0/6) | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 50ms | 🔴 compile |
| reko | gcc -O0 | 0.119 | 0.145 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 271ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.117 | 0.236 | 0.0% (0/6) | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 43ms | 🔴 compile |
| angr | gcc -O0 | 0.113 | 0.064 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 119ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.113 | 0.064 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| angr | gcc -O2 | 0.113 | 0.064 | 0.0% (0/6) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 121ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.113 | 0.064 | 0.0% (0/6) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 120ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.109 | 0.146 | 0.0% (0/6) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 258ms | 🔴 compile |
| reko | gcc -O2 | 0.097 | 0.084 | 0.0% (0/6) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 251ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.023 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.023 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 234ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 231ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% (0/6) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 543ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 655ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 635ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 417ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 908ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 892ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 934ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 780ms | ❌ usage: revng [-h] [--version]  |

### `bubble_sort`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc-m32 -O0 | 0.150 | 0.322 | 0.0% (0/5) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 47ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.135 | 0.172 | 0.0% (0/5) | #2 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 263ms | 🔴 compile |
| radare2 | gcc -O0 | 0.129 | 0.144 | 0.0% (0/5) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 58ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.127 | 0.186 | 0.0% (0/5) | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 43ms | 🔴 compile |
| reko | gcc -O2 | 0.120 | 0.102 | 0.0% (0/5) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 251ms | 🔴 compile |
| angr | gcc -O0 | 0.120 | 0.099 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 119ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.120 | 0.099 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| angr | gcc -O2 | 0.120 | 0.099 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 121ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.120 | 0.099 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 120ms | 🔴 compile |
| reko | gcc -O0 | 0.118 | 0.091 | 0.0% (0/5) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 271ms | 🔴 compile |
| radare2 | gcc -O2 | 0.118 | 0.141 | 0.0% (0/5) | #3 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 50ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.113 | 0.116 | 0.0% (0/5) | #3 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 258ms | 🔴 compile |
| boomerang | gcc -O0 | 0.079 | 0.037 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.079 | 0.037 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 234ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 231ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% (0/5) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 543ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% (0/5) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 635ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% (0/5) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 417ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 655ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 908ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 892ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 934ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 780ms | ❌ usage: revng [-h] [--version]  |

### `checksum`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.454 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 74ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.523 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 66ms | 🔴 compile |
| reko | gcc -O0 | 0.135 | 0.176 | 0.0% (0/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 441ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.130 | 0.151 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 481ms | 🔴 compile |
| angr | gcc -O0 | 0.117 | 0.087 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 218ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.117 | 0.087 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 188ms | 🔴 compile |
| angr | gcc -O2 | 0.117 | 0.087 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 204ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.117 | 0.087 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 191ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.117 | 0.086 | 0.0% (0/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 425ms | 🔴 compile |
| radare2 | gcc -O2 | 0.117 | 0.134 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 74ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.111 | 0.105 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 69ms | 🔴 compile |
| reko | gcc -O2 | 0.108 | 0.039 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 414ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 38ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 16ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.004 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 373ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 385ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 609ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 161 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 498ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 543ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 560ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 907ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 901ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 858ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 876ms | ❌ usage: revng [-h] [--version]  |

### `clamp`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.485 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 74ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.407 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 441ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.559 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 66ms | 🔴 compile |
| radare2 | gcc -O2 | 0.150 | 0.571 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 74ms | 🔴 compile |
| reko | gcc -O2 | 0.150 | 0.386 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 414ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.693 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 69ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.150 | 0.440 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 425ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.122 | 0.110 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 481ms | 🔴 compile |
| angr | gcc -O0 | 0.118 | 0.091 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 218ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.118 | 0.091 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 188ms | 🔴 compile |
| angr | gcc -O2 | 0.118 | 0.091 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 204ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.118 | 0.091 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 191ms | 🔴 compile |
| boomerang | gcc -O0 | 0.069 | 0.035 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 38ms | 🔴 compile |
| boomerang | gcc -O2 | 0.069 | 0.035 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 16ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 385ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 373ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 609ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% (0/6) | #5 | 161 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 498ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 543ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% (0/6) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 560ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 907ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 901ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 858ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 876ms | ❌ usage: revng [-h] [--version]  |

### `classify_range`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O2 | 0.150 | 0.489 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 74ms | 🔴 compile |
| reko | gcc -O2 | 0.150 | 0.362 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 414ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.477 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 69ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.150 | 0.353 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 425ms | 🔴 compile |
| angr | gcc -O0 | 0.126 | 0.131 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 218ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.126 | 0.131 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 188ms | 🔴 compile |
| angr | gcc -O2 | 0.126 | 0.131 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 204ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.126 | 0.131 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 191ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.119 | 0.146 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 66ms | 🔴 compile |
| radare2 | gcc -O0 | 0.119 | 0.144 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 74ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.119 | 0.194 | 0.0% (0/5) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 481ms | 🔴 compile |
| reko | gcc -O0 | 0.097 | 0.082 | 0.0% (0/5) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 441ms | 🔴 compile |
| boomerang | gcc -O0 | 0.079 | 0.033 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 38ms | 🔴 compile |
| boomerang | gcc -O2 | 0.079 | 0.033 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 16ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 385ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 373ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 609ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 161 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 498ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 543ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 560ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 907ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 901ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 858ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 876ms | ❌ usage: revng [-h] [--version]  |

### `count_bits`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.638 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 74ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.408 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 441ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.607 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 66ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.150 | 0.430 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 481ms | 🔴 compile |
| radare2 | gcc -O2 | 0.150 | 0.536 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 74ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.520 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 69ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.150 | 0.358 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 425ms | 🔴 compile |
| reko | gcc -O2 | 0.132 | 0.208 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 414ms | 🔴 compile |
| angr | gcc -O0 | 0.129 | 0.144 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 218ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.129 | 0.144 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 188ms | 🔴 compile |
| angr | gcc -O2 | 0.129 | 0.144 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 204ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.129 | 0.144 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 191ms | 🔴 compile |
| boomerang | gcc -O0 | 0.089 | 0.088 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 38ms | 🔴 compile |
| boomerang | gcc -O2 | 0.089 | 0.088 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 16ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 385ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 373ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 609ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 543ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 161 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 498ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 560ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 907ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 901ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 858ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 876ms | ❌ usage: revng [-h] [--version]  |

### `crc32`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.299 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 144ms | ⚪ no_test |
| radare2 | clang -O0 | 0.150 | 0.371 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 150ms | ⚪ no_test |
| radare2 | clang-m32 -O0 | 0.150 | 0.316 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 124ms | ⚪ no_test |
| radare2 | clang -O2 | 0.141 | 0.205 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 152ms | ⚪ no_test |
| radare2 | clang-m32 -O2 | 0.126 | 0.132 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 133ms | ⚪ no_test |
| radare2 | gcc-m32 -O0 | 0.126 | 0.129 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 135ms | ⚪ no_test |
| radare2 | gcc-m32 -O2 | 0.125 | 0.176 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 147ms | ⚪ no_test |
| reko | clang -O0 | 0.123 | 0.116 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 799ms | ⚪ no_test |
| reko | clang-m32 -O0 | 0.123 | 0.116 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 890ms | ⚪ no_test |
| radare2 | gcc -O2 | 0.122 | 0.162 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 156ms | ⚪ no_test |
| reko | gcc -O0 | 0.120 | 0.102 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 840ms | ⚪ no_test |
| angr | gcc -O0 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 389ms | ⚪ no_test |
| angr | gcc -O2 | 0.115 | 0.075 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 405ms | ⚪ no_test |
| angr | gcc-m32 -O0 | 0.115 | 0.075 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 352ms | ⚪ no_test |
| angr | gcc-m32 -O2 | 0.115 | 0.075 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 372ms | ⚪ no_test |
| angr | clang -O0 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 484ms | ⚪ no_test |
| angr | clang -O2 | 0.115 | 0.075 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 361ms | ⚪ no_test |
| angr | clang-m32 -O0 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 358ms | ⚪ no_test |
| angr | clang-m32 -O2 | 0.115 | 0.075 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 353ms | ⚪ no_test |
| reko | gcc-m32 -O2 | 0.114 | 0.071 | 0.0% | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 871ms | ⚪ no_test |
| reko | gcc-m32 -O0 | 0.114 | 0.069 | 0.0% | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 880ms | ⚪ no_test |
| reko | gcc -O2 | 0.108 | 0.042 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1051ms | ⚪ no_test |
| reko | clang-m32 -O2 | 0.107 | 0.035 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 833ms | ⚪ no_test |
| reko | clang -O2 | 0.105 | 0.026 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 864ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.076 | 0.022 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 31ms | ⚪ no_test |
| boomerang | gcc -O2 | 0.076 | 0.022 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 32ms | ⚪ no_test |
| boomerang | clang -O0 | 0.076 | 0.022 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 33ms | ⚪ no_test |
| boomerang | clang -O2 | 0.076 | 0.022 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 38ms | ⚪ no_test |
| snowman | clang-m32 -O2 | 0.000 | 0.002 | 0.0% | #4 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 424ms | ⚪ no_test |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 465ms | ⚪ no_test |
| boomerang | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 798ms | ⚪ no_test |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #5 | 153 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 484ms | ⚪ no_test |
| boomerang | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 794ms | ⚪ no_test |
| snowman | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 550ms | ⚪ no_test |
| snowman | clang -O0 | 0.000 | 0.001 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 661ms | ⚪ no_test |
| boomerang | clang-m32 -O0 | 0.000 | 0.002 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 798ms | ⚪ no_test |
| snowman | clang-m32 -O0 | 0.000 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 484ms | ⚪ no_test |
| boomerang | clang-m32 -O2 | 0.000 | 0.002 | 0.0% | #5 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 805ms | ⚪ no_test |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 221 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 594ms | ⚪ no_test |
| snowman | clang -O2 | 0.000 | 0.001 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 567ms | ⚪ no_test |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 865ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 940ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 921ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 920ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 880ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 886ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 948ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 911ms | ❌ usage: revng [-h] [--version]  |

### `factorial`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.469 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 58ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.437 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 271ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.120 | 0.151 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 47ms | 🔴 compile |
| angr | gcc -O0 | 0.119 | 0.095 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 119ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.119 | 0.095 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| angr | gcc -O2 | 0.119 | 0.095 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 121ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.119 | 0.095 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 120ms | 🔴 compile |
| radare2 | gcc -O2 | 0.118 | 0.189 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 50ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.107 | 0.136 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 43ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.098 | 0.041 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 263ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.098 | 0.088 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 258ms | 🔴 compile |
| reko | gcc -O2 | 0.086 | 0.028 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 251ms | 🔴 compile |
| boomerang | gcc -O0 | 0.072 | 0.048 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.072 | 0.048 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 234ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 231ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.000 | 0.0% (0/5) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 655ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 543ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.000 | 0.0% (0/5) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 635ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% (0/5) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 417ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 908ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 892ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 934ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 780ms | ❌ usage: revng [-h] [--version]  |

### `fibonacci`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.543 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 58ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.289 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 271ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.526 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 47ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.150 | 0.545 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 263ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.122 | 0.208 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 43ms | 🔴 compile |
| angr | gcc -O0 | 0.121 | 0.105 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 119ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.121 | 0.105 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| angr | gcc -O2 | 0.121 | 0.105 | 0.0% (0/6) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 121ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.121 | 0.105 | 0.0% (0/6) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 120ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.120 | 0.200 | 0.0% (0/6) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 258ms | 🔴 compile |
| radare2 | gcc -O2 | 0.115 | 0.176 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 50ms | 🔴 compile |
| reko | gcc -O2 | 0.106 | 0.132 | 0.0% (0/6) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 251ms | 🔴 compile |
| boomerang | gcc -O0 | 0.068 | 0.029 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.068 | 0.029 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 234ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 231ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 543ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 417ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.000 | 0.0% (0/6) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 655ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.000 | 0.0% (0/6) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 635ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 908ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 892ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 934ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 780ms | ❌ usage: revng [-h] [--version]  |

### `fibonacci_iter`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.688 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 58ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.412 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 47ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.150 | 0.302 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 263ms | 🔴 compile |
| reko | gcc -O0 | 0.140 | 0.252 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 271ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.138 | 0.241 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 43ms | 🔴 compile |
| radare2 | gcc -O2 | 0.138 | 0.238 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 50ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.134 | 0.219 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 258ms | 🔴 compile |
| reko | gcc -O2 | 0.122 | 0.161 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 251ms | 🔴 compile |
| angr | gcc -O0 | 0.115 | 0.073 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 119ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.115 | 0.073 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| angr | gcc -O2 | 0.115 | 0.073 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 121ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.115 | 0.073 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 120ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.027 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.027 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 234ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 231ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 543ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 417ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 655ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 635ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 908ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 892ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 934ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 780ms | ❌ usage: revng [-h] [--version]  |

### `find_pair_value`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc-m32 -O0 | 0.150 | 0.307 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 86ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.141 | 0.204 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 545ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.140 | 0.248 | 0.0% (0/5) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 77ms | 🔴 compile |
| reko | gcc -O0 | 0.138 | 0.190 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 517ms | 🔴 compile |
| radare2 | gcc -O0 | 0.134 | 0.172 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 95ms | 🔴 compile |
| angr | gcc -O0 | 0.128 | 0.139 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 284ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.128 | 0.139 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 234ms | 🔴 compile |
| angr | gcc -O2 | 0.128 | 0.139 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 235ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.128 | 0.139 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 277ms | 🔴 compile |
| reko | gcc -O2 | 0.126 | 0.131 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 473ms | 🔴 compile |
| radare2 | gcc -O2 | 0.125 | 0.174 | 0.0% (0/5) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 88ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.108 | 0.040 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 523ms | 🔴 compile |
| boomerang | gcc -O0 | 0.078 | 0.029 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 21ms | 🔴 compile |
| boomerang | gcc -O2 | 0.078 | 0.029 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 17ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 499ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 508ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 155 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 577ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 603ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 220 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 579ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 501ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 929ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 919ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 870ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 813ms | ❌ usage: revng [-h] [--version]  |

### `find_substring`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.384 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 191ms | ⚪ no_test |
| radare2 | gcc-m32 -O0 | 0.150 | 0.358 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 183ms | ⚪ no_test |
| radare2 | gcc-m32 -O2 | 0.150 | 0.352 | 0.0% | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 181ms | ⚪ no_test |
| radare2 | gcc -O2 | 0.126 | 0.228 | 0.0% | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 215ms | ⚪ no_test |
| radare2 | clang-m32 -O2 | 0.116 | 0.228 | 0.0% | #1 | 0 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 203ms | ⚪ no_test |
| reko | clang-m32 -O0 | 0.113 | 0.167 | 0.0% | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1282ms | ⚪ no_test |
| reko | gcc-m32 -O0 | 0.111 | 0.156 | 0.0% | #2 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1220ms | ⚪ no_test |
| angr | gcc -O0 | 0.111 | 0.054 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 559ms | ⚪ no_test |
| angr | gcc -O2 | 0.111 | 0.054 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 568ms | ⚪ no_test |
| angr | gcc-m32 -O0 | 0.111 | 0.054 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 551ms | ⚪ no_test |
| angr | gcc-m32 -O2 | 0.111 | 0.054 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 544ms | ⚪ no_test |
| angr | clang -O0 | 0.111 | 0.054 | 0.0% | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 570ms | ⚪ no_test |
| angr | clang -O2 | 0.111 | 0.054 | 0.0% | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 576ms | ⚪ no_test |
| angr | clang-m32 -O0 | 0.111 | 0.054 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 483ms | ⚪ no_test |
| angr | clang-m32 -O2 | 0.111 | 0.054 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 473ms | ⚪ no_test |
| reko | clang -O0 | 0.110 | 0.149 | 0.0% | #2 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1220ms | ⚪ no_test |
| reko | gcc -O0 | 0.102 | 0.111 | 0.0% | #3 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1175ms | ⚪ no_test |
| radare2 | clang -O0 | 0.100 | 0.099 | 0.0% | #3 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 264ms | ⚪ no_test |
| radare2 | clang-m32 -O0 | 0.097 | 0.086 | 0.0% | #3 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 166ms | ⚪ no_test |
| radare2 | clang -O2 | 0.087 | 0.086 | 0.0% | #2 | 0 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 251ms | ⚪ no_test |
| reko | clang-m32 -O2 | 0.085 | 0.146 | 0.0% | #3 | 1 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1253ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.081 | 0.045 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 52ms | ⚪ no_test |
| boomerang | gcc -O2 | 0.081 | 0.045 | 0.0% | #3 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 52ms | ⚪ no_test |
| boomerang | clang -O2 | 0.081 | 0.045 | 0.0% | #3 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 56ms | ⚪ no_test |
| reko | gcc-m32 -O2 | 0.075 | 0.116 | 0.0% | #3 | 2 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1240ms | ⚪ no_test |
| reko | clang -O2 | 0.072 | 0.080 | 0.0% | #4 | 1 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1221ms | ⚪ no_test |
| reko | gcc -O2 | 0.068 | 0.081 | 0.0% | #4 | 2 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1282ms | ⚪ no_test |
| boomerang | clang -O0 | 0.066 | 0.020 | 0.0% | #4 | 2 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 191ms | ⚪ no_test |
| boomerang | gcc-m32 -O2 | 0.001 | 0.006 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1207ms | ⚪ no_test |
| boomerang | clang-m32 -O0 | 0.001 | 0.006 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1165ms | ⚪ no_test |
| boomerang | gcc-m32 -O0 | 0.001 | 0.006 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1190ms | ⚪ no_test |
| boomerang | clang-m32 -O2 | 0.001 | 0.006 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1219ms | ⚪ no_test |
| snowman | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 461ms | ⚪ no_test |
| snowman | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% | #5 | 153 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 435ms | ⚪ no_test |
| snowman | clang-m32 -O0 | 0.001 | 0.003 | 0.0% | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 454ms | ⚪ no_test |
| snowman | gcc -O0 | 0.001 | 0.002 | 0.0% | #5 | 225 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 528ms | ⚪ no_test |
| snowman | clang -O0 | 0.001 | 0.002 | 0.0% | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 538ms | ⚪ no_test |
| snowman | clang-m32 -O2 | 0.001 | 0.002 | 0.0% | #5 | 156 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 462ms | ⚪ no_test |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 616ms | ⚪ no_test |
| snowman | clang -O2 | 0.000 | 0.002 | 0.0% | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 569ms | ⚪ no_test |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 869ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 921ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 853ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 910ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 904ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 846ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 906ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 932ms | ❌ usage: revng [-h] [--version]  |

### `gcd`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.302 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 58ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.369 | 0.0% (0/6) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 271ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.486 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 47ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.150 | 0.546 | 0.0% (0/6) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 263ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.149 | 0.294 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 43ms | 🔴 compile |
| radare2 | gcc -O2 | 0.148 | 0.242 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 50ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.140 | 0.200 | 0.0% (0/6) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 258ms | 🔴 compile |
| reko | gcc -O2 | 0.138 | 0.188 | 0.0% (0/6) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 251ms | 🔴 compile |
| angr | gcc -O0 | 0.130 | 0.149 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 119ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.130 | 0.149 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| angr | gcc -O2 | 0.130 | 0.149 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 121ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.130 | 0.149 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 120ms | 🔴 compile |
| boomerang | gcc -O0 | 0.088 | 0.082 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.088 | 0.082 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 234ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 231ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 543ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 417ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 655ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 635ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 908ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 892ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 934ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 780ms | ❌ usage: revng [-h] [--version]  |

### `linear_search`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.389 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 58ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.369 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 47ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.150 | 0.354 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 263ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.369 | 0.0% (0/6) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 43ms | 🔴 compile |
| reko | gcc -O0 | 0.140 | 0.249 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 271ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.139 | 0.247 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 258ms | 🔴 compile |
| radare2 | gcc -O2 | 0.139 | 0.296 | 0.0% (0/6) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 50ms | 🔴 compile |
| angr | gcc -O0 | 0.130 | 0.148 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 119ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.130 | 0.148 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| angr | gcc -O2 | 0.130 | 0.148 | 0.0% (0/6) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 121ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.130 | 0.148 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 120ms | 🔴 compile |
| reko | gcc -O2 | 0.111 | 0.104 | 0.0% (0/6) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 251ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.028 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.028 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 234ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 231ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 543ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 417ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 655ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 635ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 908ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 892ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 934ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 780ms | ❌ usage: revng [-h] [--version]  |

### `manipulate_bitfields`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O2 | 0.150 | 0.372 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 220ms | ⚪ no_test |
| radare2 | gcc-m32 -O2 | 0.150 | 0.367 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 196ms | ⚪ no_test |
| radare2 | clang -O2 | 0.150 | 0.384 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 208ms | ⚪ no_test |
| radare2 | clang-m32 -O2 | 0.150 | 0.378 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 186ms | ⚪ no_test |
| radare2 | gcc-m32 -O0 | 0.133 | 0.217 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 182ms | ⚪ no_test |
| radare2 | clang-m32 -O0 | 0.133 | 0.214 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 190ms | ⚪ no_test |
| reko | gcc -O2 | 0.130 | 0.149 | 0.0% | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1256ms | ⚪ no_test |
| radare2 | clang -O0 | 0.130 | 0.198 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 184ms | ⚪ no_test |
| reko | clang -O2 | 0.127 | 0.135 | 0.0% | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1318ms | ⚪ no_test |
| reko | gcc-m32 -O0 | 0.123 | 0.117 | 0.0% | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1265ms | ⚪ no_test |
| reko | clang -O0 | 0.123 | 0.116 | 0.0% | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1289ms | ⚪ no_test |
| reko | clang-m32 -O0 | 0.120 | 0.100 | 0.0% | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1238ms | ⚪ no_test |
| reko | gcc -O0 | 0.120 | 0.099 | 0.0% | #1 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1355ms | ⚪ no_test |
| reko | clang-m32 -O2 | 0.119 | 0.094 | 0.0% | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1388ms | ⚪ no_test |
| radare2 | gcc -O0 | 0.118 | 0.140 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 206ms | ⚪ no_test |
| angr | gcc -O0 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 576ms | ⚪ no_test |
| angr | gcc -O2 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 597ms | ⚪ no_test |
| angr | gcc-m32 -O0 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 597ms | ⚪ no_test |
| angr | gcc-m32 -O2 | 0.115 | 0.075 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 513ms | ⚪ no_test |
| angr | clang -O0 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 629ms | ⚪ no_test |
| angr | clang -O2 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 589ms | ⚪ no_test |
| angr | clang-m32 -O0 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 505ms | ⚪ no_test |
| angr | clang-m32 -O2 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 505ms | ⚪ no_test |
| reko | gcc-m32 -O2 | 0.114 | 0.068 | 0.0% | #3 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1298ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.071 | 0.047 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 46ms | ⚪ no_test |
| boomerang | gcc -O2 | 0.071 | 0.047 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 47ms | ⚪ no_test |
| boomerang | clang -O0 | 0.071 | 0.047 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 55ms | ⚪ no_test |
| boomerang | clang -O2 | 0.071 | 0.047 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 64ms | ⚪ no_test |
| boomerang | gcc-m32 -O0 | 0.001 | 0.004 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1246ms | ⚪ no_test |
| boomerang | gcc-m32 -O2 | 0.001 | 0.004 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1248ms | ⚪ no_test |
| boomerang | clang-m32 -O0 | 0.001 | 0.004 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1193ms | ⚪ no_test |
| boomerang | clang-m32 -O2 | 0.001 | 0.004 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1191ms | ⚪ no_test |
| snowman | clang-m32 -O0 | 0.001 | 0.003 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 435ms | ⚪ no_test |
| snowman | clang-m32 -O2 | 0.001 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 467ms | ⚪ no_test |
| snowman | gcc -O0 | 0.000 | 0.002 | 0.0% | #5 | 221 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 519ms | ⚪ no_test |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 554ms | ⚪ no_test |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #5 | 153 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 498ms | ⚪ no_test |
| snowman | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 549ms | ⚪ no_test |
| snowman | clang -O0 | 0.000 | 0.002 | 0.0% | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 555ms | ⚪ no_test |
| snowman | clang -O2 | 0.000 | 0.002 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 545ms | ⚪ no_test |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 931ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 893ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 920ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 982ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 890ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 933ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 963ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 975ms | ❌ usage: revng [-h] [--version]  |

### `matrix_multiply`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.559 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 206ms | ⚪ no_test |
| radare2 | clang -O0 | 0.150 | 0.679 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 184ms | ⚪ no_test |
| radare2 | clang-m32 -O0 | 0.150 | 0.517 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 190ms | ⚪ no_test |
| reko | gcc-m32 -O0 | 0.140 | 0.199 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1265ms | ⚪ no_test |
| reko | clang-m32 -O0 | 0.140 | 0.198 | 0.0% | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1238ms | ⚪ no_test |
| radare2 | gcc-m32 -O0 | 0.129 | 0.145 | 0.0% | #2 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 182ms | ⚪ no_test |
| radare2 | gcc -O2 | 0.123 | 0.165 | 0.0% | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 220ms | ⚪ no_test |
| radare2 | clang -O2 | 0.122 | 0.209 | 0.0% | #1 | 0 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 208ms | ⚪ no_test |
| reko | gcc -O0 | 0.119 | 0.096 | 0.0% | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1355ms | ⚪ no_test |
| reko | clang -O0 | 0.118 | 0.090 | 0.0% | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1289ms | ⚪ no_test |
| radare2 | gcc-m32 -O2 | 0.117 | 0.137 | 0.0% | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 196ms | ⚪ no_test |
| radare2 | clang-m32 -O2 | 0.114 | 0.169 | 0.0% | #1 | 0 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 186ms | ⚪ no_test |
| angr | gcc -O0 | 0.112 | 0.060 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 576ms | ⚪ no_test |
| angr | gcc -O2 | 0.112 | 0.060 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 597ms | ⚪ no_test |
| angr | gcc-m32 -O0 | 0.112 | 0.060 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 597ms | ⚪ no_test |
| angr | gcc-m32 -O2 | 0.112 | 0.060 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 513ms | ⚪ no_test |
| angr | clang -O0 | 0.112 | 0.060 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 629ms | ⚪ no_test |
| angr | clang -O2 | 0.112 | 0.060 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 589ms | ⚪ no_test |
| angr | clang-m32 -O0 | 0.112 | 0.060 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 505ms | ⚪ no_test |
| angr | clang-m32 -O2 | 0.112 | 0.060 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 505ms | ⚪ no_test |
| reko | gcc -O2 | 0.107 | 0.084 | 0.0% | #3 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1256ms | ⚪ no_test |
| reko | gcc-m32 -O2 | 0.097 | 0.034 | 0.0% | #3 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1298ms | ⚪ no_test |
| reko | clang -O2 | 0.096 | 0.081 | 0.0% | #3 | 0 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1318ms | ⚪ no_test |
| reko | clang-m32 -O2 | 0.096 | 0.081 | 0.0% | #3 | 0 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1388ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.084 | 0.060 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 46ms | ⚪ no_test |
| boomerang | gcc -O2 | 0.084 | 0.060 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 47ms | ⚪ no_test |
| boomerang | clang -O0 | 0.084 | 0.060 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 55ms | ⚪ no_test |
| boomerang | clang -O2 | 0.084 | 0.060 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 64ms | ⚪ no_test |
| boomerang | clang-m32 -O2 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1191ms | ⚪ no_test |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1246ms | ⚪ no_test |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1248ms | ⚪ no_test |
| boomerang | clang-m32 -O0 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1193ms | ⚪ no_test |
| snowman | clang-m32 -O0 | 0.001 | 0.003 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 435ms | ⚪ no_test |
| snowman | clang-m32 -O2 | 0.001 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 467ms | ⚪ no_test |
| snowman | gcc -O0 | 0.000 | 0.002 | 0.0% | #5 | 221 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 519ms | ⚪ no_test |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #5 | 153 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 498ms | ⚪ no_test |
| snowman | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 549ms | ⚪ no_test |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 554ms | ⚪ no_test |
| snowman | clang -O0 | 0.000 | 0.002 | 0.0% | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 555ms | ⚪ no_test |
| snowman | clang -O2 | 0.000 | 0.002 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 545ms | ⚪ no_test |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 931ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 893ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 920ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 982ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 890ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 933ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 963ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 975ms | ❌ usage: revng [-h] [--version]  |

### `max`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.415 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 58ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.315 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 271ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.389 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 47ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.150 | 0.395 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 263ms | 🔴 compile |
| radare2 | gcc -O2 | 0.150 | 0.630 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 50ms | 🔴 compile |
| reko | gcc -O2 | 0.150 | 0.315 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 251ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.391 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 43ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.150 | 0.398 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 258ms | 🔴 compile |
| angr | gcc -O0 | 0.128 | 0.141 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 119ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.128 | 0.141 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| angr | gcc -O2 | 0.128 | 0.141 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 121ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.128 | 0.141 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 120ms | 🔴 compile |
| boomerang | gcc -O0 | 0.068 | 0.032 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.068 | 0.032 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 234ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 231ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.000 | 0.0% (0/6) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 655ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 543ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.000 | 0.0% (0/6) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 635ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 417ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 908ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 892ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 934ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 780ms | ❌ usage: revng [-h] [--version]  |

### `pointer_stride_sum`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O2 | 0.150 | 0.330 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 88ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.367 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 77ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.142 | 0.209 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 86ms | 🔴 compile |
| radare2 | gcc -O0 | 0.141 | 0.206 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 95ms | 🔴 compile |
| reko | gcc -O2 | 0.140 | 0.198 | 0.0% (0/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 473ms | 🔴 compile |
| angr | gcc -O0 | 0.123 | 0.115 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 284ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.123 | 0.115 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 234ms | 🔴 compile |
| angr | gcc -O2 | 0.123 | 0.115 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 235ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.123 | 0.115 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 277ms | 🔴 compile |
| reko | gcc -O0 | 0.122 | 0.108 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 517ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.120 | 0.102 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 545ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.109 | 0.097 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 523ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 21ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 17ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 499ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 508ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 603ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 155 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 577ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 220 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 579ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 501ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 929ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 919ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 870ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 813ms | ❌ usage: revng [-h] [--version]  |

### `power`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| reko | gcc-m32 -O0 | 0.138 | 0.188 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 263ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.133 | 0.216 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 258ms | 🔴 compile |
| radare2 | gcc -O0 | 0.124 | 0.168 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 58ms | 🔴 compile |
| reko | gcc -O0 | 0.123 | 0.118 | 0.0% (0/6) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 271ms | 🔴 compile |
| reko | gcc -O2 | 0.116 | 0.129 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 251ms | 🔴 compile |
| angr | gcc -O0 | 0.116 | 0.078 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 119ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.116 | 0.078 | 0.0% (0/6) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| angr | gcc -O2 | 0.116 | 0.078 | 0.0% (0/6) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 121ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.116 | 0.078 | 0.0% (0/6) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 120ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.112 | 0.111 | 0.0% (0/6) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 47ms | 🔴 compile |
| radare2 | gcc -O2 | 0.102 | 0.111 | 0.0% (0/6) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 50ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.099 | 0.093 | 0.0% (0/6) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 43ms | 🔴 compile |
| boomerang | gcc -O0 | 0.081 | 0.043 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.081 | 0.043 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 234ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 231ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 655ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 543ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 635ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 417ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 908ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 892ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 934ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 780ms | ❌ usage: revng [-h] [--version]  |

### `process_code`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O2 | 0.148 | 0.288 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 50ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.146 | 0.282 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 43ms | 🔴 compile |
| angr | gcc -O0 | 0.123 | 0.114 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 119ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.123 | 0.114 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| angr | gcc -O2 | 0.123 | 0.114 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 121ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.123 | 0.114 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 120ms | 🔴 compile |
| reko | gcc -O0 | 0.116 | 0.078 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 271ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.115 | 0.075 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 263ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.112 | 0.160 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 258ms | 🔴 compile |
| reko | gcc -O2 | 0.096 | 0.079 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 251ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.094 | 0.121 | 0.0% (0/5) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 47ms | 🔴 compile |
| radare2 | gcc -O0 | 0.075 | 0.025 | 0.0% (0/5) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 58ms | 🔴 compile |
| boomerang | gcc -O0 | 0.067 | 0.025 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.067 | 0.025 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.004 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 231ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.004 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 234ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 543ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 635ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 417ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 655ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 908ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 892ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 934ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 780ms | ❌ usage: revng [-h] [--version]  |

### `rc4_crypt`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.424 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 144ms | ⚪ no_test |
| radare2 | gcc-m32 -O0 | 0.150 | 0.292 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 135ms | ⚪ no_test |
| radare2 | clang -O0 | 0.150 | 0.395 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 150ms | ⚪ no_test |
| radare2 | clang-m32 -O0 | 0.150 | 0.430 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 124ms | ⚪ no_test |
| radare2 | gcc -O2 | 0.143 | 0.267 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 156ms | ⚪ no_test |
| radare2 | clang -O2 | 0.133 | 0.263 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 152ms | ⚪ no_test |
| radare2 | clang-m32 -O2 | 0.131 | 0.257 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 133ms | ⚪ no_test |
| radare2 | gcc-m32 -O2 | 0.130 | 0.200 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 147ms | ⚪ no_test |
| reko | gcc-m32 -O0 | 0.127 | 0.135 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 880ms | ⚪ no_test |
| reko | clang -O0 | 0.124 | 0.119 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 799ms | ⚪ no_test |
| reko | gcc -O0 | 0.124 | 0.118 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 840ms | ⚪ no_test |
| reko | clang-m32 -O0 | 0.121 | 0.106 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 890ms | ⚪ no_test |
| angr | gcc -O0 | 0.113 | 0.067 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 389ms | ⚪ no_test |
| angr | gcc -O2 | 0.113 | 0.067 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 405ms | ⚪ no_test |
| angr | gcc-m32 -O0 | 0.113 | 0.067 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 352ms | ⚪ no_test |
| angr | gcc-m32 -O2 | 0.113 | 0.067 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 372ms | ⚪ no_test |
| angr | clang -O0 | 0.113 | 0.067 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 484ms | ⚪ no_test |
| angr | clang -O2 | 0.113 | 0.067 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 361ms | ⚪ no_test |
| angr | clang-m32 -O0 | 0.113 | 0.067 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 358ms | ⚪ no_test |
| angr | clang-m32 -O2 | 0.113 | 0.067 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 353ms | ⚪ no_test |
| reko | gcc -O2 | 0.109 | 0.096 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1051ms | ⚪ no_test |
| reko | gcc-m32 -O2 | 0.104 | 0.068 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 871ms | ⚪ no_test |
| reko | clang-m32 -O2 | 0.101 | 0.055 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 833ms | ⚪ no_test |
| reko | clang -O2 | 0.100 | 0.049 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 864ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.079 | 0.034 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 31ms | ⚪ no_test |
| boomerang | gcc -O2 | 0.079 | 0.034 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 32ms | ⚪ no_test |
| boomerang | clang -O0 | 0.079 | 0.034 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 33ms | ⚪ no_test |
| boomerang | clang -O2 | 0.079 | 0.034 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 38ms | ⚪ no_test |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 798ms | ⚪ no_test |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 794ms | ⚪ no_test |
| boomerang | clang-m32 -O0 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 798ms | ⚪ no_test |
| boomerang | clang-m32 -O2 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 805ms | ⚪ no_test |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 465ms | ⚪ no_test |
| snowman | gcc -O0 | 0.000 | 0.002 | 0.0% | #5 | 221 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 594ms | ⚪ no_test |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 550ms | ⚪ no_test |
| snowman | clang -O0 | 0.000 | 0.002 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 661ms | ⚪ no_test |
| snowman | clang -O2 | 0.000 | 0.002 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 567ms | ⚪ no_test |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 153 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 484ms | ⚪ no_test |
| snowman | clang-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 484ms | ⚪ no_test |
| snowman | clang-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 424ms | ⚪ no_test |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 865ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 940ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 921ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 920ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 880ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 886ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 948ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 911ms | ❌ usage: revng [-h] [--version]  |

### `rc4_init`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.501 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 144ms | ⚪ no_test |
| radare2 | gcc-m32 -O0 | 0.150 | 0.301 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 135ms | ⚪ no_test |
| radare2 | clang -O0 | 0.150 | 0.291 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 150ms | ⚪ no_test |
| radare2 | clang-m32 -O0 | 0.150 | 0.350 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 124ms | ⚪ no_test |
| reko | clang -O0 | 0.136 | 0.178 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 799ms | ⚪ no_test |
| radare2 | gcc-m32 -O2 | 0.135 | 0.175 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 147ms | ⚪ no_test |
| reko | gcc-m32 -O0 | 0.127 | 0.137 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 880ms | ⚪ no_test |
| reko | gcc -O0 | 0.126 | 0.129 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 840ms | ⚪ no_test |
| radare2 | clang-m32 -O2 | 0.122 | 0.159 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 133ms | ⚪ no_test |
| reko | clang-m32 -O0 | 0.117 | 0.085 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 890ms | ⚪ no_test |
| reko | clang -O2 | 0.115 | 0.073 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 864ms | ⚪ no_test |
| reko | gcc-m32 -O2 | 0.114 | 0.070 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 871ms | ⚪ no_test |
| angr | gcc -O0 | 0.114 | 0.068 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 389ms | ⚪ no_test |
| angr | gcc -O2 | 0.114 | 0.068 | 0.0% | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 405ms | ⚪ no_test |
| angr | gcc-m32 -O0 | 0.114 | 0.068 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 352ms | ⚪ no_test |
| angr | gcc-m32 -O2 | 0.114 | 0.068 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 372ms | ⚪ no_test |
| angr | clang -O0 | 0.114 | 0.068 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 484ms | ⚪ no_test |
| angr | clang -O2 | 0.114 | 0.068 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 361ms | ⚪ no_test |
| angr | clang-m32 -O0 | 0.114 | 0.068 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 358ms | ⚪ no_test |
| angr | clang-m32 -O2 | 0.114 | 0.068 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 353ms | ⚪ no_test |
| reko | clang-m32 -O2 | 0.113 | 0.065 | 0.0% | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 833ms | ⚪ no_test |
| reko | gcc -O2 | 0.109 | 0.044 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1051ms | ⚪ no_test |
| radare2 | gcc -O2 | 0.105 | 0.025 | 0.0% | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 156ms | ⚪ no_test |
| radare2 | clang -O2 | 0.102 | 0.058 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 152ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.080 | 0.040 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 31ms | ⚪ no_test |
| boomerang | gcc -O2 | 0.080 | 0.040 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 32ms | ⚪ no_test |
| boomerang | clang -O0 | 0.080 | 0.040 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 33ms | ⚪ no_test |
| boomerang | clang -O2 | 0.080 | 0.040 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 38ms | ⚪ no_test |
| boomerang | gcc-m32 -O2 | 0.001 | 0.004 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 794ms | ⚪ no_test |
| boomerang | clang-m32 -O0 | 0.001 | 0.004 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 798ms | ⚪ no_test |
| boomerang | clang-m32 -O2 | 0.001 | 0.004 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 805ms | ⚪ no_test |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 798ms | ⚪ no_test |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 465ms | ⚪ no_test |
| snowman | clang-m32 -O2 | 0.000 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 424ms | ⚪ no_test |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 221 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 594ms | ⚪ no_test |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #5 | 153 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 484ms | ⚪ no_test |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 550ms | ⚪ no_test |
| snowman | clang -O0 | 0.000 | 0.002 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 661ms | ⚪ no_test |
| snowman | clang -O2 | 0.000 | 0.001 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 567ms | ⚪ no_test |
| snowman | clang-m32 -O0 | 0.000 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 484ms | ⚪ no_test |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 865ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 940ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 921ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 920ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 880ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 886ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 948ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 911ms | ❌ usage: revng [-h] [--version]  |

### `reverse_in_place`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc-m32 -O0 | 0.150 | 0.264 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 86ms | 🔴 compile |
| radare2 | gcc -O0 | 0.149 | 0.244 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 95ms | 🔴 compile |
| reko | gcc -O0 | 0.131 | 0.156 | 0.0% (0/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 517ms | 🔴 compile |
| radare2 | gcc -O2 | 0.123 | 0.164 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 88ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.117 | 0.133 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 77ms | 🔴 compile |
| angr | gcc -O0 | 0.116 | 0.081 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 284ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.116 | 0.081 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 234ms | 🔴 compile |
| angr | gcc -O2 | 0.116 | 0.081 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 235ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.116 | 0.081 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 277ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.113 | 0.067 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 545ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.104 | 0.069 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 523ms | 🔴 compile |
| reko | gcc -O2 | 0.103 | 0.064 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 473ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.028 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 21ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.028 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 17ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 499ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 508ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% (0/5) | #5 | 155 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 577ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 220 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 579ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 501ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 603ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 929ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 919ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 870ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 813ms | ❌ usage: revng [-h] [--version]  |

### `reverse_string`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc-m32 -O0 | 0.150 | 0.353 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 183ms | ⚪ no_test |
| radare2 | gcc-m32 -O2 | 0.148 | 0.291 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 181ms | ⚪ no_test |
| radare2 | gcc -O0 | 0.146 | 0.281 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 191ms | ⚪ no_test |
| reko | gcc -O2 | 0.142 | 0.261 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1282ms | ⚪ no_test |
| radare2 | clang-m32 -O2 | 0.140 | 0.248 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 203ms | ⚪ no_test |
| radare2 | clang-m32 -O0 | 0.135 | 0.225 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 166ms | ⚪ no_test |
| radare2 | clang -O0 | 0.133 | 0.215 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 264ms | ⚪ no_test |
| radare2 | clang -O2 | 0.132 | 0.209 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 251ms | ⚪ no_test |
| radare2 | gcc -O2 | 0.129 | 0.197 | 0.0% | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 215ms | ⚪ no_test |
| reko | clang -O0 | 0.117 | 0.138 | 0.0% | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1220ms | ⚪ no_test |
| reko | gcc-m32 -O0 | 0.117 | 0.133 | 0.0% | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1220ms | ⚪ no_test |
| angr | gcc -O0 | 0.117 | 0.083 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 559ms | ⚪ no_test |
| angr | gcc -O2 | 0.117 | 0.083 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 568ms | ⚪ no_test |
| angr | gcc-m32 -O0 | 0.117 | 0.083 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 551ms | ⚪ no_test |
| angr | gcc-m32 -O2 | 0.117 | 0.083 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 544ms | ⚪ no_test |
| angr | clang -O0 | 0.117 | 0.083 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 570ms | ⚪ no_test |
| angr | clang -O2 | 0.117 | 0.083 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 576ms | ⚪ no_test |
| angr | clang-m32 -O0 | 0.117 | 0.083 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 483ms | ⚪ no_test |
| angr | clang-m32 -O2 | 0.117 | 0.083 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 473ms | ⚪ no_test |
| reko | gcc -O0 | 0.116 | 0.132 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1175ms | ⚪ no_test |
| reko | clang-m32 -O0 | 0.116 | 0.129 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1282ms | ⚪ no_test |
| reko | clang -O2 | 0.111 | 0.154 | 0.0% | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1221ms | ⚪ no_test |
| reko | clang-m32 -O2 | 0.106 | 0.128 | 0.0% | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1253ms | ⚪ no_test |
| reko | gcc-m32 -O2 | 0.103 | 0.113 | 0.0% | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1240ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.079 | 0.036 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 52ms | ⚪ no_test |
| boomerang | gcc -O2 | 0.079 | 0.036 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 52ms | ⚪ no_test |
| boomerang | clang -O2 | 0.079 | 0.036 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 56ms | ⚪ no_test |
| boomerang | clang -O0 | 0.057 | 0.023 | 0.0% | #4 | 2 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 191ms | ⚪ no_test |
| boomerang | gcc-m32 -O0 | 0.001 | 0.005 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1190ms | ⚪ no_test |
| boomerang | gcc-m32 -O2 | 0.001 | 0.005 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1207ms | ⚪ no_test |
| boomerang | clang-m32 -O0 | 0.001 | 0.005 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1165ms | ⚪ no_test |
| boomerang | clang-m32 -O2 | 0.001 | 0.005 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1219ms | ⚪ no_test |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 225 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 528ms | ⚪ no_test |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 616ms | ⚪ no_test |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 461ms | ⚪ no_test |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 153 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 435ms | ⚪ no_test |
| snowman | clang -O0 | 0.000 | 0.001 | 0.0% | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 538ms | ⚪ no_test |
| snowman | clang-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 454ms | ⚪ no_test |
| snowman | clang -O2 | 0.000 | 0.001 | 0.0% | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 569ms | ⚪ no_test |
| snowman | clang-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 156 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 462ms | ⚪ no_test |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 869ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 921ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 853ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 910ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 904ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 846ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 906ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 932ms | ❌ usage: revng [-h] [--version]  |

### `saturating_add`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O2 | 0.150 | 0.599 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 74ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.586 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 69ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.142 | 0.211 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 425ms | 🔴 compile |
| reko | gcc -O0 | 0.137 | 0.187 | 0.0% (0/5) | #1 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 441ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.135 | 0.176 | 0.0% (0/5) | #1 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 481ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.126 | 0.228 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 66ms | 🔴 compile |
| radare2 | gcc -O0 | 0.126 | 0.227 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 74ms | 🔴 compile |
| angr | gcc -O0 | 0.117 | 0.085 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 218ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.117 | 0.085 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 188ms | 🔴 compile |
| angr | gcc -O2 | 0.117 | 0.085 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 204ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.117 | 0.085 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 191ms | 🔴 compile |
| reko | gcc -O2 | 0.115 | 0.126 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 414ms | 🔴 compile |
| boomerang | gcc -O0 | 0.067 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 38ms | 🔴 compile |
| boomerang | gcc -O2 | 0.067 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 16ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.004 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 385ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 373ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 609ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 161 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 498ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 543ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 560ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 907ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 901ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 858ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 876ms | ❌ usage: revng [-h] [--version]  |

### `signum`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.541 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 74ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.423 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 441ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.573 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 66ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.150 | 0.408 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 481ms | 🔴 compile |
| radare2 | gcc -O2 | 0.150 | 0.497 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 74ms | 🔴 compile |
| reko | gcc -O2 | 0.150 | 0.484 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 414ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.563 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 69ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.150 | 0.532 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 425ms | 🔴 compile |
| angr | gcc -O0 | 0.126 | 0.127 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 218ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.126 | 0.127 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 188ms | 🔴 compile |
| angr | gcc -O2 | 0.126 | 0.127 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 204ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.126 | 0.127 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 191ms | 🔴 compile |
| boomerang | gcc -O0 | 0.069 | 0.037 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 38ms | 🔴 compile |
| boomerang | gcc -O2 | 0.069 | 0.037 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 16ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 385ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 373ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 609ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 161 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 498ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 543ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 560ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 907ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 901ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 858ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 876ms | ❌ usage: revng [-h] [--version]  |

### `sum_array`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.286 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 95ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.431 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 86ms | 🔴 compile |
| reko | gcc -O0 | 0.145 | 0.224 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 517ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.125 | 0.123 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 545ms | 🔴 compile |
| angr | gcc -O0 | 0.124 | 0.120 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 284ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.124 | 0.120 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 234ms | 🔴 compile |
| angr | gcc -O2 | 0.124 | 0.120 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 235ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.124 | 0.120 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 277ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.123 | 0.165 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 77ms | 🔴 compile |
| radare2 | gcc -O2 | 0.119 | 0.143 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 88ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.116 | 0.080 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 523ms | 🔴 compile |
| reko | gcc -O2 | 0.111 | 0.055 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 473ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.028 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 21ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.028 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 17ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 499ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 508ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 155 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 577ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 220 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 579ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 501ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 603ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 929ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 919ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 870ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 813ms | ❌ usage: revng [-h] [--version]  |

---

## Overfitting Analysis

Functions where **all** decompilers scored below 0.3 are marked as objectively hard.
Functions where **only Fission** scored below 0.3 are marked as quality gaps.

**Objectively hard functions (28):** `count_bits`, `clamp`, `signum`, `checksum`, `classify_range`, `saturating_add`, `rc4_init`, `rc4_crypt`, `crc32`, `sum_array`, `reverse_in_place`, `find_pair_value`, `accumulate_pairs`, `pointer_stride_sum`, `manipulate_bitfields`, `matrix_multiply`, `fibonacci`, `fibonacci_iter`, `max`, `bubble_sort`, `linear_search`, `binary_search`, `factorial`, `gcd`, `power`, `process_code`, `reverse_string`, `find_substring`