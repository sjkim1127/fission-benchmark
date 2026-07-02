# Fission Benchmark Report

**Generated:** 2026-07-02 04:14 UTC
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
| radare2 | gcc -O0 | 0.150 | 0.435 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 99ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.289 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 89ms | 🔴 compile |
| reko | gcc -O0 | 0.141 | 0.204 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 543ms | 🔴 compile |
| reko | gcc -O2 | 0.125 | 0.124 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 493ms | 🔴 compile |
| radare2 | gcc -O2 | 0.121 | 0.153 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 105ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.120 | 0.102 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 525ms | 🔴 compile |
| angr | gcc -O0 | 0.119 | 0.097 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 262ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.119 | 0.097 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 248ms | 🔴 compile |
| angr | gcc -O2 | 0.119 | 0.097 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 223ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.119 | 0.097 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 262ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.113 | 0.116 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 88ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.112 | 0.060 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 504ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 21ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 21ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 474ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 474ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 658ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 155 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 637ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 220 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 589ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 595ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1015ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1044ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1000ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1052ms | ❌ usage: revng [-h] [--version]  |

### `binary_search`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.389 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 55ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.409 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 54ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.124 | 0.172 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 312ms | 🔴 compile |
| radare2 | gcc -O2 | 0.120 | 0.252 | 0.0% (0/6) | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 65ms | 🔴 compile |
| reko | gcc -O0 | 0.119 | 0.145 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 279ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.117 | 0.236 | 0.0% (0/6) | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 51ms | 🔴 compile |
| angr | gcc -O0 | 0.113 | 0.064 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 127ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.113 | 0.064 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 135ms | 🔴 compile |
| angr | gcc -O2 | 0.113 | 0.064 | 0.0% (0/6) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.113 | 0.064 | 0.0% (0/6) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.109 | 0.146 | 0.0% (0/6) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 265ms | 🔴 compile |
| reko | gcc -O2 | 0.097 | 0.084 | 0.0% (0/6) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 281ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.023 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.023 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 240ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 220ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% (0/6) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 630ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 720ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 699ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 571ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1000ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1104ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1077ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 907ms | ❌ usage: revng [-h] [--version]  |

### `bubble_sort`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc-m32 -O0 | 0.150 | 0.322 | 0.0% (0/5) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 54ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.135 | 0.172 | 0.0% (0/5) | #2 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 312ms | 🔴 compile |
| radare2 | gcc -O0 | 0.129 | 0.144 | 0.0% (0/5) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 55ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.127 | 0.186 | 0.0% (0/5) | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 51ms | 🔴 compile |
| reko | gcc -O2 | 0.120 | 0.102 | 0.0% (0/5) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 281ms | 🔴 compile |
| angr | gcc -O0 | 0.120 | 0.099 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 127ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.120 | 0.099 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 135ms | 🔴 compile |
| angr | gcc -O2 | 0.120 | 0.099 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.120 | 0.099 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| reko | gcc -O0 | 0.118 | 0.091 | 0.0% (0/5) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 279ms | 🔴 compile |
| radare2 | gcc -O2 | 0.118 | 0.141 | 0.0% (0/5) | #3 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 65ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.113 | 0.116 | 0.0% (0/5) | #3 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 265ms | 🔴 compile |
| boomerang | gcc -O0 | 0.079 | 0.037 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.079 | 0.037 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 240ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 220ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% (0/5) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 630ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% (0/5) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 699ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% (0/5) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 571ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 720ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1000ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1104ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1077ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 907ms | ❌ usage: revng [-h] [--version]  |

### `checksum`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.454 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 109ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.523 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 73ms | 🔴 compile |
| reko | gcc -O0 | 0.135 | 0.176 | 0.0% (0/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 505ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.130 | 0.151 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 463ms | 🔴 compile |
| angr | gcc -O0 | 0.117 | 0.087 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 215ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.117 | 0.087 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 183ms | 🔴 compile |
| angr | gcc -O2 | 0.117 | 0.087 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 208ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.117 | 0.087 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 170ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.117 | 0.086 | 0.0% (0/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 413ms | 🔴 compile |
| radare2 | gcc -O2 | 0.117 | 0.134 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 85ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.111 | 0.105 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 73ms | 🔴 compile |
| reko | gcc -O2 | 0.108 | 0.039 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 414ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 80ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 16ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.004 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 369ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 375ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 653ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 161 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 594ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 628ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 581ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1084ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1038ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1004ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 872ms | ❌ usage: revng [-h] [--version]  |

### `clamp`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.485 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 109ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.407 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 505ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.559 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 73ms | 🔴 compile |
| radare2 | gcc -O2 | 0.150 | 0.571 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 85ms | 🔴 compile |
| reko | gcc -O2 | 0.150 | 0.386 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 414ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.693 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 73ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.150 | 0.440 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 413ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.122 | 0.110 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 463ms | 🔴 compile |
| angr | gcc -O0 | 0.118 | 0.091 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 215ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.118 | 0.091 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 183ms | 🔴 compile |
| angr | gcc -O2 | 0.118 | 0.091 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 208ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.118 | 0.091 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 170ms | 🔴 compile |
| boomerang | gcc -O0 | 0.069 | 0.035 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 80ms | 🔴 compile |
| boomerang | gcc -O2 | 0.069 | 0.035 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 16ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 375ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 369ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 653ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% (0/6) | #5 | 161 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 594ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 628ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% (0/6) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 581ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1084ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1038ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1004ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 872ms | ❌ usage: revng [-h] [--version]  |

### `classify_range`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O2 | 0.150 | 0.489 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 85ms | 🔴 compile |
| reko | gcc -O2 | 0.150 | 0.362 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 414ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.477 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 73ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.150 | 0.353 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 413ms | 🔴 compile |
| angr | gcc -O0 | 0.126 | 0.131 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 215ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.126 | 0.131 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 183ms | 🔴 compile |
| angr | gcc -O2 | 0.126 | 0.131 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 208ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.126 | 0.131 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 170ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.119 | 0.146 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 73ms | 🔴 compile |
| radare2 | gcc -O0 | 0.119 | 0.144 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 109ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.119 | 0.194 | 0.0% (0/5) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 463ms | 🔴 compile |
| reko | gcc -O0 | 0.097 | 0.082 | 0.0% (0/5) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 505ms | 🔴 compile |
| boomerang | gcc -O0 | 0.079 | 0.033 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 80ms | 🔴 compile |
| boomerang | gcc -O2 | 0.079 | 0.033 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 16ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 375ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 369ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 653ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 161 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 594ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 628ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 581ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1084ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1038ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1004ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 872ms | ❌ usage: revng [-h] [--version]  |

### `count_bits`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.638 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 109ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.408 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 505ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.607 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 73ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.150 | 0.430 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 463ms | 🔴 compile |
| radare2 | gcc -O2 | 0.150 | 0.536 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 85ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.520 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 73ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.150 | 0.358 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 413ms | 🔴 compile |
| reko | gcc -O2 | 0.132 | 0.208 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 414ms | 🔴 compile |
| angr | gcc -O0 | 0.129 | 0.144 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 215ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.129 | 0.144 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 183ms | 🔴 compile |
| angr | gcc -O2 | 0.129 | 0.144 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 208ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.129 | 0.144 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 170ms | 🔴 compile |
| boomerang | gcc -O0 | 0.089 | 0.088 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 80ms | 🔴 compile |
| boomerang | gcc -O2 | 0.089 | 0.088 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 16ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 375ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 369ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 653ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 628ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 161 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 594ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 581ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1084ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1038ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1004ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 872ms | ❌ usage: revng [-h] [--version]  |

### `crc32`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.299 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 176ms | ⚪ no_test |
| radare2 | clang -O0 | 0.150 | 0.371 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 170ms | ⚪ no_test |
| radare2 | clang-m32 -O0 | 0.150 | 0.316 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 133ms | ⚪ no_test |
| radare2 | clang -O2 | 0.141 | 0.205 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 163ms | ⚪ no_test |
| radare2 | clang-m32 -O2 | 0.126 | 0.132 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 175ms | ⚪ no_test |
| radare2 | gcc-m32 -O0 | 0.126 | 0.129 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 193ms | ⚪ no_test |
| radare2 | gcc-m32 -O2 | 0.125 | 0.176 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 141ms | ⚪ no_test |
| reko | clang -O0 | 0.123 | 0.116 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 917ms | ⚪ no_test |
| reko | clang-m32 -O0 | 0.123 | 0.116 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 911ms | ⚪ no_test |
| radare2 | gcc -O2 | 0.122 | 0.162 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 151ms | ⚪ no_test |
| reko | gcc -O0 | 0.120 | 0.102 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 937ms | ⚪ no_test |
| angr | gcc -O0 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 388ms | ⚪ no_test |
| angr | gcc -O2 | 0.115 | 0.075 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 421ms | ⚪ no_test |
| angr | gcc-m32 -O0 | 0.115 | 0.075 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 369ms | ⚪ no_test |
| angr | gcc-m32 -O2 | 0.115 | 0.075 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 350ms | ⚪ no_test |
| angr | clang -O0 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 458ms | ⚪ no_test |
| angr | clang -O2 | 0.115 | 0.075 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 375ms | ⚪ no_test |
| angr | clang-m32 -O0 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 343ms | ⚪ no_test |
| angr | clang-m32 -O2 | 0.115 | 0.075 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 330ms | ⚪ no_test |
| reko | gcc-m32 -O2 | 0.114 | 0.071 | 0.0% | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 911ms | ⚪ no_test |
| reko | gcc-m32 -O0 | 0.114 | 0.069 | 0.0% | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 842ms | ⚪ no_test |
| reko | gcc -O2 | 0.108 | 0.042 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1100ms | ⚪ no_test |
| reko | clang-m32 -O2 | 0.107 | 0.035 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 937ms | ⚪ no_test |
| reko | clang -O2 | 0.105 | 0.026 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 846ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.076 | 0.022 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 39ms | ⚪ no_test |
| boomerang | gcc -O2 | 0.076 | 0.022 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 32ms | ⚪ no_test |
| boomerang | clang -O0 | 0.076 | 0.022 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 38ms | ⚪ no_test |
| boomerang | clang -O2 | 0.076 | 0.022 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 35ms | ⚪ no_test |
| snowman | clang-m32 -O2 | 0.000 | 0.002 | 0.0% | #4 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 499ms | ⚪ no_test |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 541ms | ⚪ no_test |
| boomerang | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 755ms | ⚪ no_test |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #5 | 153 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 549ms | ⚪ no_test |
| boomerang | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 875ms | ⚪ no_test |
| snowman | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 624ms | ⚪ no_test |
| snowman | clang -O0 | 0.000 | 0.001 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 693ms | ⚪ no_test |
| boomerang | clang-m32 -O0 | 0.000 | 0.002 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 803ms | ⚪ no_test |
| snowman | clang-m32 -O0 | 0.000 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 574ms | ⚪ no_test |
| boomerang | clang-m32 -O2 | 0.000 | 0.002 | 0.0% | #5 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 780ms | ⚪ no_test |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 221 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 699ms | ⚪ no_test |
| snowman | clang -O2 | 0.000 | 0.001 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 633ms | ⚪ no_test |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1188ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1032ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1131ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1048ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1115ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1021ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1009ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1074ms | ❌ usage: revng [-h] [--version]  |

### `factorial`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.469 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 55ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.437 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 279ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.120 | 0.151 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 54ms | 🔴 compile |
| angr | gcc -O0 | 0.119 | 0.095 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 127ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.119 | 0.095 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 135ms | 🔴 compile |
| angr | gcc -O2 | 0.119 | 0.095 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.119 | 0.095 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| radare2 | gcc -O2 | 0.118 | 0.189 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 65ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.107 | 0.136 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 51ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.098 | 0.041 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 312ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.098 | 0.088 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 265ms | 🔴 compile |
| reko | gcc -O2 | 0.086 | 0.028 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 281ms | 🔴 compile |
| boomerang | gcc -O0 | 0.072 | 0.048 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.072 | 0.048 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 240ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 220ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.000 | 0.0% (0/5) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 720ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 630ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.000 | 0.0% (0/5) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 699ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% (0/5) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 571ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1000ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1104ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1077ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 907ms | ❌ usage: revng [-h] [--version]  |

### `fibonacci`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.543 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 55ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.289 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 279ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.526 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 54ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.150 | 0.545 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 312ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.122 | 0.208 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 51ms | 🔴 compile |
| angr | gcc -O0 | 0.121 | 0.105 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 127ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.121 | 0.105 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 135ms | 🔴 compile |
| angr | gcc -O2 | 0.121 | 0.105 | 0.0% (0/6) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.121 | 0.105 | 0.0% (0/6) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.120 | 0.200 | 0.0% (0/6) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 265ms | 🔴 compile |
| radare2 | gcc -O2 | 0.115 | 0.176 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 65ms | 🔴 compile |
| reko | gcc -O2 | 0.106 | 0.132 | 0.0% (0/6) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 281ms | 🔴 compile |
| boomerang | gcc -O0 | 0.068 | 0.029 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.068 | 0.029 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 240ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 220ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 630ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 571ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.000 | 0.0% (0/6) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 720ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.000 | 0.0% (0/6) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 699ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1000ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1104ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1077ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 907ms | ❌ usage: revng [-h] [--version]  |

### `fibonacci_iter`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.688 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 55ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.412 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 54ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.150 | 0.302 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 312ms | 🔴 compile |
| reko | gcc -O0 | 0.140 | 0.252 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 279ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.138 | 0.241 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 51ms | 🔴 compile |
| radare2 | gcc -O2 | 0.138 | 0.238 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 65ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.134 | 0.219 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 265ms | 🔴 compile |
| reko | gcc -O2 | 0.122 | 0.161 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 281ms | 🔴 compile |
| angr | gcc -O0 | 0.115 | 0.073 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 127ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.115 | 0.073 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 135ms | 🔴 compile |
| angr | gcc -O2 | 0.115 | 0.073 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.115 | 0.073 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.027 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.027 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 240ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 220ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 630ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 571ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 720ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 699ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1000ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1104ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1077ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 907ms | ❌ usage: revng [-h] [--version]  |

### `find_pair_value`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc-m32 -O0 | 0.150 | 0.307 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 89ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.141 | 0.204 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 525ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.140 | 0.248 | 0.0% (0/5) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 88ms | 🔴 compile |
| reko | gcc -O0 | 0.138 | 0.190 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 543ms | 🔴 compile |
| radare2 | gcc -O0 | 0.134 | 0.172 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 99ms | 🔴 compile |
| angr | gcc -O0 | 0.128 | 0.139 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 262ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.128 | 0.139 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 248ms | 🔴 compile |
| angr | gcc -O2 | 0.128 | 0.139 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 223ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.128 | 0.139 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 262ms | 🔴 compile |
| reko | gcc -O2 | 0.126 | 0.131 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 493ms | 🔴 compile |
| radare2 | gcc -O2 | 0.125 | 0.174 | 0.0% (0/5) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 105ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.108 | 0.040 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 504ms | 🔴 compile |
| boomerang | gcc -O0 | 0.078 | 0.029 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 21ms | 🔴 compile |
| boomerang | gcc -O2 | 0.078 | 0.029 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 21ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 474ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 474ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 155 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 637ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 658ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 220 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 589ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 595ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1015ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1044ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1000ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1052ms | ❌ usage: revng [-h] [--version]  |

### `find_substring`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.384 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 211ms | ⚪ no_test |
| radare2 | gcc-m32 -O0 | 0.150 | 0.358 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 233ms | ⚪ no_test |
| radare2 | gcc-m32 -O2 | 0.150 | 0.352 | 0.0% | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 194ms | ⚪ no_test |
| radare2 | gcc -O2 | 0.126 | 0.228 | 0.0% | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 241ms | ⚪ no_test |
| radare2 | clang-m32 -O2 | 0.116 | 0.228 | 0.0% | #1 | 0 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 205ms | ⚪ no_test |
| reko | clang-m32 -O0 | 0.113 | 0.167 | 0.0% | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1406ms | ⚪ no_test |
| reko | gcc-m32 -O0 | 0.111 | 0.156 | 0.0% | #2 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1309ms | ⚪ no_test |
| angr | gcc -O0 | 0.111 | 0.054 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 541ms | ⚪ no_test |
| angr | gcc -O2 | 0.111 | 0.054 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 591ms | ⚪ no_test |
| angr | gcc-m32 -O0 | 0.111 | 0.054 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 514ms | ⚪ no_test |
| angr | gcc-m32 -O2 | 0.111 | 0.054 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 600ms | ⚪ no_test |
| angr | clang -O0 | 0.111 | 0.054 | 0.0% | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 556ms | ⚪ no_test |
| angr | clang -O2 | 0.111 | 0.054 | 0.0% | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 590ms | ⚪ no_test |
| angr | clang-m32 -O0 | 0.111 | 0.054 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 578ms | ⚪ no_test |
| angr | clang-m32 -O2 | 0.111 | 0.054 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 523ms | ⚪ no_test |
| reko | clang -O0 | 0.110 | 0.149 | 0.0% | #2 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1304ms | ⚪ no_test |
| reko | gcc -O0 | 0.102 | 0.111 | 0.0% | #3 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1243ms | ⚪ no_test |
| radare2 | clang -O0 | 0.100 | 0.099 | 0.0% | #3 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 232ms | ⚪ no_test |
| radare2 | clang-m32 -O0 | 0.097 | 0.086 | 0.0% | #3 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 202ms | ⚪ no_test |
| radare2 | clang -O2 | 0.087 | 0.086 | 0.0% | #2 | 0 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 246ms | ⚪ no_test |
| reko | clang-m32 -O2 | 0.085 | 0.146 | 0.0% | #3 | 1 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1247ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.081 | 0.045 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 49ms | ⚪ no_test |
| boomerang | gcc -O2 | 0.081 | 0.045 | 0.0% | #3 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 52ms | ⚪ no_test |
| boomerang | clang -O2 | 0.081 | 0.045 | 0.0% | #3 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 56ms | ⚪ no_test |
| reko | gcc-m32 -O2 | 0.075 | 0.116 | 0.0% | #3 | 2 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1329ms | ⚪ no_test |
| reko | clang -O2 | 0.072 | 0.080 | 0.0% | #4 | 1 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1293ms | ⚪ no_test |
| reko | gcc -O2 | 0.068 | 0.081 | 0.0% | #4 | 2 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1341ms | ⚪ no_test |
| boomerang | clang -O0 | 0.066 | 0.020 | 0.0% | #4 | 2 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 173ms | ⚪ no_test |
| boomerang | gcc-m32 -O2 | 0.001 | 0.006 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1160ms | ⚪ no_test |
| boomerang | clang-m32 -O0 | 0.001 | 0.006 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1196ms | ⚪ no_test |
| boomerang | gcc-m32 -O0 | 0.001 | 0.006 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1245ms | ⚪ no_test |
| boomerang | clang-m32 -O2 | 0.001 | 0.006 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1216ms | ⚪ no_test |
| snowman | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 495ms | ⚪ no_test |
| snowman | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% | #5 | 153 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 494ms | ⚪ no_test |
| snowman | clang-m32 -O0 | 0.001 | 0.003 | 0.0% | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 490ms | ⚪ no_test |
| snowman | gcc -O0 | 0.001 | 0.002 | 0.0% | #5 | 225 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 588ms | ⚪ no_test |
| snowman | clang -O0 | 0.001 | 0.002 | 0.0% | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 572ms | ⚪ no_test |
| snowman | clang-m32 -O2 | 0.001 | 0.002 | 0.0% | #5 | 156 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 563ms | ⚪ no_test |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 722ms | ⚪ no_test |
| snowman | clang -O2 | 0.000 | 0.002 | 0.0% | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 626ms | ⚪ no_test |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1061ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1111ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1095ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1078ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1087ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1043ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1120ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1051ms | ❌ usage: revng [-h] [--version]  |

### `gcd`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.302 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 55ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.369 | 0.0% (0/6) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 279ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.486 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 54ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.150 | 0.546 | 0.0% (0/6) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 312ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.149 | 0.294 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 51ms | 🔴 compile |
| radare2 | gcc -O2 | 0.148 | 0.242 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 65ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.140 | 0.200 | 0.0% (0/6) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 265ms | 🔴 compile |
| reko | gcc -O2 | 0.138 | 0.188 | 0.0% (0/6) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 281ms | 🔴 compile |
| angr | gcc -O0 | 0.130 | 0.149 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 127ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.130 | 0.149 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 135ms | 🔴 compile |
| angr | gcc -O2 | 0.130 | 0.149 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.130 | 0.149 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| boomerang | gcc -O0 | 0.088 | 0.082 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.088 | 0.082 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 240ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 220ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 630ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 571ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 720ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 699ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1000ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1104ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1077ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 907ms | ❌ usage: revng [-h] [--version]  |

### `linear_search`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.389 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 55ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.369 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 54ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.150 | 0.354 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 312ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.369 | 0.0% (0/6) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 51ms | 🔴 compile |
| reko | gcc -O0 | 0.140 | 0.249 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 279ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.139 | 0.247 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 265ms | 🔴 compile |
| radare2 | gcc -O2 | 0.139 | 0.296 | 0.0% (0/6) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 65ms | 🔴 compile |
| angr | gcc -O0 | 0.130 | 0.148 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 127ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.130 | 0.148 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 135ms | 🔴 compile |
| angr | gcc -O2 | 0.130 | 0.148 | 0.0% (0/6) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.130 | 0.148 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| reko | gcc -O2 | 0.111 | 0.104 | 0.0% (0/6) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 281ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.028 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.028 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 240ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 220ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 630ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 571ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 720ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 699ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1000ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1104ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1077ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 907ms | ❌ usage: revng [-h] [--version]  |

### `manipulate_bitfields`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O2 | 0.150 | 0.372 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 226ms | ⚪ no_test |
| radare2 | gcc-m32 -O2 | 0.150 | 0.367 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 261ms | ⚪ no_test |
| radare2 | clang -O2 | 0.150 | 0.384 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 228ms | ⚪ no_test |
| radare2 | clang-m32 -O2 | 0.150 | 0.378 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 202ms | ⚪ no_test |
| radare2 | gcc-m32 -O0 | 0.133 | 0.217 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 195ms | ⚪ no_test |
| radare2 | clang-m32 -O0 | 0.133 | 0.214 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 244ms | ⚪ no_test |
| reko | gcc -O2 | 0.130 | 0.149 | 0.0% | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1295ms | ⚪ no_test |
| radare2 | clang -O0 | 0.130 | 0.198 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 263ms | ⚪ no_test |
| reko | clang -O2 | 0.127 | 0.135 | 0.0% | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1272ms | ⚪ no_test |
| reko | gcc-m32 -O0 | 0.123 | 0.117 | 0.0% | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1358ms | ⚪ no_test |
| reko | clang -O0 | 0.123 | 0.116 | 0.0% | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1357ms | ⚪ no_test |
| reko | clang-m32 -O0 | 0.120 | 0.100 | 0.0% | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1297ms | ⚪ no_test |
| reko | gcc -O0 | 0.120 | 0.099 | 0.0% | #1 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1344ms | ⚪ no_test |
| reko | clang-m32 -O2 | 0.119 | 0.094 | 0.0% | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1271ms | ⚪ no_test |
| radare2 | gcc -O0 | 0.118 | 0.140 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 224ms | ⚪ no_test |
| angr | gcc -O0 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 583ms | ⚪ no_test |
| angr | gcc -O2 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 534ms | ⚪ no_test |
| angr | gcc-m32 -O0 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 606ms | ⚪ no_test |
| angr | gcc-m32 -O2 | 0.115 | 0.075 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 531ms | ⚪ no_test |
| angr | clang -O0 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 561ms | ⚪ no_test |
| angr | clang -O2 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 631ms | ⚪ no_test |
| angr | clang-m32 -O0 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 460ms | ⚪ no_test |
| angr | clang-m32 -O2 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 511ms | ⚪ no_test |
| reko | gcc-m32 -O2 | 0.114 | 0.068 | 0.0% | #3 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1307ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.071 | 0.047 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 49ms | ⚪ no_test |
| boomerang | gcc -O2 | 0.071 | 0.047 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 50ms | ⚪ no_test |
| boomerang | clang -O0 | 0.071 | 0.047 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 55ms | ⚪ no_test |
| boomerang | clang -O2 | 0.071 | 0.047 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 52ms | ⚪ no_test |
| boomerang | gcc-m32 -O0 | 0.001 | 0.004 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1170ms | ⚪ no_test |
| boomerang | gcc-m32 -O2 | 0.001 | 0.004 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1256ms | ⚪ no_test |
| boomerang | clang-m32 -O0 | 0.001 | 0.004 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1153ms | ⚪ no_test |
| boomerang | clang-m32 -O2 | 0.001 | 0.004 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1207ms | ⚪ no_test |
| snowman | clang-m32 -O0 | 0.001 | 0.003 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 486ms | ⚪ no_test |
| snowman | clang-m32 -O2 | 0.001 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 503ms | ⚪ no_test |
| snowman | gcc -O0 | 0.000 | 0.002 | 0.0% | #5 | 221 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 600ms | ⚪ no_test |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 590ms | ⚪ no_test |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #5 | 153 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 587ms | ⚪ no_test |
| snowman | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 602ms | ⚪ no_test |
| snowman | clang -O0 | 0.000 | 0.002 | 0.0% | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 595ms | ⚪ no_test |
| snowman | clang -O2 | 0.000 | 0.002 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 570ms | ⚪ no_test |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1198ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1029ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1022ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1036ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 997ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1011ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1030ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1163ms | ❌ usage: revng [-h] [--version]  |

### `matrix_multiply`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.559 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 224ms | ⚪ no_test |
| radare2 | clang -O0 | 0.150 | 0.679 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 263ms | ⚪ no_test |
| radare2 | clang-m32 -O0 | 0.150 | 0.517 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 244ms | ⚪ no_test |
| reko | gcc-m32 -O0 | 0.140 | 0.199 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1358ms | ⚪ no_test |
| reko | clang-m32 -O0 | 0.140 | 0.198 | 0.0% | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1297ms | ⚪ no_test |
| radare2 | gcc-m32 -O0 | 0.129 | 0.145 | 0.0% | #2 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 195ms | ⚪ no_test |
| radare2 | gcc -O2 | 0.123 | 0.165 | 0.0% | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 226ms | ⚪ no_test |
| radare2 | clang -O2 | 0.122 | 0.209 | 0.0% | #1 | 0 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 228ms | ⚪ no_test |
| reko | gcc -O0 | 0.119 | 0.096 | 0.0% | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1344ms | ⚪ no_test |
| reko | clang -O0 | 0.118 | 0.090 | 0.0% | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1357ms | ⚪ no_test |
| radare2 | gcc-m32 -O2 | 0.117 | 0.137 | 0.0% | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 261ms | ⚪ no_test |
| radare2 | clang-m32 -O2 | 0.114 | 0.169 | 0.0% | #1 | 0 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 202ms | ⚪ no_test |
| angr | gcc -O0 | 0.112 | 0.060 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 583ms | ⚪ no_test |
| angr | gcc -O2 | 0.112 | 0.060 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 534ms | ⚪ no_test |
| angr | gcc-m32 -O0 | 0.112 | 0.060 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 606ms | ⚪ no_test |
| angr | gcc-m32 -O2 | 0.112 | 0.060 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 531ms | ⚪ no_test |
| angr | clang -O0 | 0.112 | 0.060 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 561ms | ⚪ no_test |
| angr | clang -O2 | 0.112 | 0.060 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 631ms | ⚪ no_test |
| angr | clang-m32 -O0 | 0.112 | 0.060 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 460ms | ⚪ no_test |
| angr | clang-m32 -O2 | 0.112 | 0.060 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 511ms | ⚪ no_test |
| reko | gcc -O2 | 0.107 | 0.084 | 0.0% | #3 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1295ms | ⚪ no_test |
| reko | gcc-m32 -O2 | 0.097 | 0.034 | 0.0% | #3 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1307ms | ⚪ no_test |
| reko | clang -O2 | 0.096 | 0.081 | 0.0% | #3 | 0 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1272ms | ⚪ no_test |
| reko | clang-m32 -O2 | 0.096 | 0.081 | 0.0% | #3 | 0 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1271ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.084 | 0.060 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 49ms | ⚪ no_test |
| boomerang | gcc -O2 | 0.084 | 0.060 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 50ms | ⚪ no_test |
| boomerang | clang -O0 | 0.084 | 0.060 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 55ms | ⚪ no_test |
| boomerang | clang -O2 | 0.084 | 0.060 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 52ms | ⚪ no_test |
| boomerang | clang-m32 -O2 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1207ms | ⚪ no_test |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1170ms | ⚪ no_test |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1256ms | ⚪ no_test |
| boomerang | clang-m32 -O0 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1153ms | ⚪ no_test |
| snowman | clang-m32 -O0 | 0.001 | 0.003 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 486ms | ⚪ no_test |
| snowman | clang-m32 -O2 | 0.001 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 503ms | ⚪ no_test |
| snowman | gcc -O0 | 0.000 | 0.002 | 0.0% | #5 | 221 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 600ms | ⚪ no_test |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #5 | 153 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 587ms | ⚪ no_test |
| snowman | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 602ms | ⚪ no_test |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 590ms | ⚪ no_test |
| snowman | clang -O0 | 0.000 | 0.002 | 0.0% | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 595ms | ⚪ no_test |
| snowman | clang -O2 | 0.000 | 0.002 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 570ms | ⚪ no_test |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1198ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1029ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1022ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1036ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 997ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1011ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1030ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1163ms | ❌ usage: revng [-h] [--version]  |

### `max`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.415 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 55ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.315 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 279ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.389 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 54ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.150 | 0.395 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 312ms | 🔴 compile |
| radare2 | gcc -O2 | 0.150 | 0.630 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 65ms | 🔴 compile |
| reko | gcc -O2 | 0.150 | 0.315 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 281ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.391 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 51ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.150 | 0.398 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 265ms | 🔴 compile |
| angr | gcc -O0 | 0.128 | 0.141 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 127ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.128 | 0.141 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 135ms | 🔴 compile |
| angr | gcc -O2 | 0.128 | 0.141 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.128 | 0.141 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| boomerang | gcc -O0 | 0.068 | 0.032 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.068 | 0.032 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 240ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 220ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.000 | 0.0% (0/6) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 720ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 630ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.000 | 0.0% (0/6) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 699ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 571ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1000ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1104ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1077ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 907ms | ❌ usage: revng [-h] [--version]  |

### `pointer_stride_sum`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O2 | 0.150 | 0.330 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 105ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.367 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 88ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.142 | 0.209 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 89ms | 🔴 compile |
| radare2 | gcc -O0 | 0.141 | 0.206 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 99ms | 🔴 compile |
| reko | gcc -O2 | 0.140 | 0.198 | 0.0% (0/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 493ms | 🔴 compile |
| angr | gcc -O0 | 0.123 | 0.115 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 262ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.123 | 0.115 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 248ms | 🔴 compile |
| angr | gcc -O2 | 0.123 | 0.115 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 223ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.123 | 0.115 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 262ms | 🔴 compile |
| reko | gcc -O0 | 0.122 | 0.108 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 543ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.120 | 0.102 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 525ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.109 | 0.097 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 504ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 21ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 21ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 474ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 474ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 658ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 155 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 637ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 220 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 589ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 595ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1015ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1044ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1000ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1052ms | ❌ usage: revng [-h] [--version]  |

### `power`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| reko | gcc-m32 -O0 | 0.138 | 0.188 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 312ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.133 | 0.216 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 265ms | 🔴 compile |
| radare2 | gcc -O0 | 0.124 | 0.168 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 55ms | 🔴 compile |
| reko | gcc -O0 | 0.123 | 0.118 | 0.0% (0/6) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 279ms | 🔴 compile |
| reko | gcc -O2 | 0.116 | 0.129 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 281ms | 🔴 compile |
| angr | gcc -O0 | 0.116 | 0.078 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 127ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.116 | 0.078 | 0.0% (0/6) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 135ms | 🔴 compile |
| angr | gcc -O2 | 0.116 | 0.078 | 0.0% (0/6) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.116 | 0.078 | 0.0% (0/6) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.112 | 0.111 | 0.0% (0/6) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 54ms | 🔴 compile |
| radare2 | gcc -O2 | 0.102 | 0.111 | 0.0% (0/6) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 65ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.099 | 0.093 | 0.0% (0/6) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 51ms | 🔴 compile |
| boomerang | gcc -O0 | 0.081 | 0.043 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.081 | 0.043 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 240ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 220ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 720ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 630ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 699ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 571ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1000ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1104ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1077ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 907ms | ❌ usage: revng [-h] [--version]  |

### `process_code`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O2 | 0.148 | 0.288 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 65ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.146 | 0.282 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 51ms | 🔴 compile |
| angr | gcc -O0 | 0.123 | 0.114 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 127ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.123 | 0.114 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 135ms | 🔴 compile |
| angr | gcc -O2 | 0.123 | 0.114 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.123 | 0.114 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 132ms | 🔴 compile |
| reko | gcc -O0 | 0.116 | 0.078 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 279ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.115 | 0.075 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 312ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.112 | 0.160 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 265ms | 🔴 compile |
| reko | gcc -O2 | 0.096 | 0.079 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 281ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.094 | 0.121 | 0.0% (0/5) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 54ms | 🔴 compile |
| radare2 | gcc -O0 | 0.075 | 0.025 | 0.0% (0/5) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 55ms | 🔴 compile |
| boomerang | gcc -O0 | 0.067 | 0.025 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.067 | 0.025 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.004 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 220ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.004 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 240ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 630ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 699ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 571ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 720ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1000ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1104ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1077ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 907ms | ❌ usage: revng [-h] [--version]  |

### `rc4_crypt`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.424 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 176ms | ⚪ no_test |
| radare2 | gcc-m32 -O0 | 0.150 | 0.292 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 193ms | ⚪ no_test |
| radare2 | clang -O0 | 0.150 | 0.395 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 170ms | ⚪ no_test |
| radare2 | clang-m32 -O0 | 0.150 | 0.430 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 133ms | ⚪ no_test |
| radare2 | gcc -O2 | 0.143 | 0.267 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 151ms | ⚪ no_test |
| radare2 | clang -O2 | 0.133 | 0.263 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 163ms | ⚪ no_test |
| radare2 | clang-m32 -O2 | 0.131 | 0.257 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 175ms | ⚪ no_test |
| radare2 | gcc-m32 -O2 | 0.130 | 0.200 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 141ms | ⚪ no_test |
| reko | gcc-m32 -O0 | 0.127 | 0.135 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 842ms | ⚪ no_test |
| reko | clang -O0 | 0.124 | 0.119 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 917ms | ⚪ no_test |
| reko | gcc -O0 | 0.124 | 0.118 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 937ms | ⚪ no_test |
| reko | clang-m32 -O0 | 0.121 | 0.106 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 911ms | ⚪ no_test |
| angr | gcc -O0 | 0.113 | 0.067 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 388ms | ⚪ no_test |
| angr | gcc -O2 | 0.113 | 0.067 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 421ms | ⚪ no_test |
| angr | gcc-m32 -O0 | 0.113 | 0.067 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 369ms | ⚪ no_test |
| angr | gcc-m32 -O2 | 0.113 | 0.067 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 350ms | ⚪ no_test |
| angr | clang -O0 | 0.113 | 0.067 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 458ms | ⚪ no_test |
| angr | clang -O2 | 0.113 | 0.067 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 375ms | ⚪ no_test |
| angr | clang-m32 -O0 | 0.113 | 0.067 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 343ms | ⚪ no_test |
| angr | clang-m32 -O2 | 0.113 | 0.067 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 330ms | ⚪ no_test |
| reko | gcc -O2 | 0.109 | 0.096 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1100ms | ⚪ no_test |
| reko | gcc-m32 -O2 | 0.104 | 0.068 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 911ms | ⚪ no_test |
| reko | clang-m32 -O2 | 0.101 | 0.055 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 937ms | ⚪ no_test |
| reko | clang -O2 | 0.100 | 0.049 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 846ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.079 | 0.034 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 39ms | ⚪ no_test |
| boomerang | gcc -O2 | 0.079 | 0.034 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 32ms | ⚪ no_test |
| boomerang | clang -O0 | 0.079 | 0.034 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 38ms | ⚪ no_test |
| boomerang | clang -O2 | 0.079 | 0.034 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 35ms | ⚪ no_test |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 755ms | ⚪ no_test |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 875ms | ⚪ no_test |
| boomerang | clang-m32 -O0 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 803ms | ⚪ no_test |
| boomerang | clang-m32 -O2 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 780ms | ⚪ no_test |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 541ms | ⚪ no_test |
| snowman | gcc -O0 | 0.000 | 0.002 | 0.0% | #5 | 221 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 699ms | ⚪ no_test |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 624ms | ⚪ no_test |
| snowman | clang -O0 | 0.000 | 0.002 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 693ms | ⚪ no_test |
| snowman | clang -O2 | 0.000 | 0.002 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 633ms | ⚪ no_test |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 153 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 549ms | ⚪ no_test |
| snowman | clang-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 574ms | ⚪ no_test |
| snowman | clang-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 499ms | ⚪ no_test |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1188ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1032ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1131ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1048ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1115ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1021ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1009ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1074ms | ❌ usage: revng [-h] [--version]  |

### `rc4_init`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.501 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 176ms | ⚪ no_test |
| radare2 | gcc-m32 -O0 | 0.150 | 0.301 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 193ms | ⚪ no_test |
| radare2 | clang -O0 | 0.150 | 0.291 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 170ms | ⚪ no_test |
| radare2 | clang-m32 -O0 | 0.150 | 0.350 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 133ms | ⚪ no_test |
| reko | clang -O0 | 0.136 | 0.178 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 917ms | ⚪ no_test |
| radare2 | gcc-m32 -O2 | 0.135 | 0.175 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 141ms | ⚪ no_test |
| reko | gcc-m32 -O0 | 0.127 | 0.137 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 842ms | ⚪ no_test |
| reko | gcc -O0 | 0.126 | 0.129 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 937ms | ⚪ no_test |
| radare2 | clang-m32 -O2 | 0.122 | 0.159 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 175ms | ⚪ no_test |
| reko | clang-m32 -O0 | 0.117 | 0.085 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 911ms | ⚪ no_test |
| reko | clang -O2 | 0.115 | 0.073 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 846ms | ⚪ no_test |
| reko | gcc-m32 -O2 | 0.114 | 0.070 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 911ms | ⚪ no_test |
| angr | gcc -O0 | 0.114 | 0.068 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 388ms | ⚪ no_test |
| angr | gcc -O2 | 0.114 | 0.068 | 0.0% | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 421ms | ⚪ no_test |
| angr | gcc-m32 -O0 | 0.114 | 0.068 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 369ms | ⚪ no_test |
| angr | gcc-m32 -O2 | 0.114 | 0.068 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 350ms | ⚪ no_test |
| angr | clang -O0 | 0.114 | 0.068 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 458ms | ⚪ no_test |
| angr | clang -O2 | 0.114 | 0.068 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 375ms | ⚪ no_test |
| angr | clang-m32 -O0 | 0.114 | 0.068 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 343ms | ⚪ no_test |
| angr | clang-m32 -O2 | 0.114 | 0.068 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 330ms | ⚪ no_test |
| reko | clang-m32 -O2 | 0.113 | 0.065 | 0.0% | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 937ms | ⚪ no_test |
| reko | gcc -O2 | 0.109 | 0.044 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1100ms | ⚪ no_test |
| radare2 | gcc -O2 | 0.105 | 0.025 | 0.0% | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 151ms | ⚪ no_test |
| radare2 | clang -O2 | 0.102 | 0.058 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 163ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.080 | 0.040 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 39ms | ⚪ no_test |
| boomerang | gcc -O2 | 0.080 | 0.040 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 32ms | ⚪ no_test |
| boomerang | clang -O0 | 0.080 | 0.040 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 38ms | ⚪ no_test |
| boomerang | clang -O2 | 0.080 | 0.040 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 35ms | ⚪ no_test |
| boomerang | gcc-m32 -O2 | 0.001 | 0.004 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 875ms | ⚪ no_test |
| boomerang | clang-m32 -O0 | 0.001 | 0.004 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 803ms | ⚪ no_test |
| boomerang | clang-m32 -O2 | 0.001 | 0.004 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 780ms | ⚪ no_test |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 755ms | ⚪ no_test |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 541ms | ⚪ no_test |
| snowman | clang-m32 -O2 | 0.000 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 499ms | ⚪ no_test |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 221 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 699ms | ⚪ no_test |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #5 | 153 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 549ms | ⚪ no_test |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 624ms | ⚪ no_test |
| snowman | clang -O0 | 0.000 | 0.002 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 693ms | ⚪ no_test |
| snowman | clang -O2 | 0.000 | 0.001 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 633ms | ⚪ no_test |
| snowman | clang-m32 -O0 | 0.000 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 574ms | ⚪ no_test |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1188ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1032ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1131ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1048ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1115ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1021ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1009ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1074ms | ❌ usage: revng [-h] [--version]  |

### `reverse_in_place`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc-m32 -O0 | 0.150 | 0.264 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 89ms | 🔴 compile |
| radare2 | gcc -O0 | 0.149 | 0.244 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 99ms | 🔴 compile |
| reko | gcc -O0 | 0.131 | 0.156 | 0.0% (0/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 543ms | 🔴 compile |
| radare2 | gcc -O2 | 0.123 | 0.164 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 105ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.117 | 0.133 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 88ms | 🔴 compile |
| angr | gcc -O0 | 0.116 | 0.081 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 262ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.116 | 0.081 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 248ms | 🔴 compile |
| angr | gcc -O2 | 0.116 | 0.081 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 223ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.116 | 0.081 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 262ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.113 | 0.067 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 525ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.104 | 0.069 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 504ms | 🔴 compile |
| reko | gcc -O2 | 0.103 | 0.064 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 493ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.028 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 21ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.028 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 21ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 474ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 474ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% (0/5) | #5 | 155 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 637ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 220 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 589ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 595ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 658ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1015ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1044ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1000ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1052ms | ❌ usage: revng [-h] [--version]  |

### `reverse_string`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc-m32 -O0 | 0.150 | 0.353 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 233ms | ⚪ no_test |
| radare2 | gcc-m32 -O2 | 0.148 | 0.291 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 194ms | ⚪ no_test |
| radare2 | gcc -O0 | 0.146 | 0.281 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 211ms | ⚪ no_test |
| reko | gcc -O2 | 0.142 | 0.261 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1341ms | ⚪ no_test |
| radare2 | clang-m32 -O2 | 0.140 | 0.248 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 205ms | ⚪ no_test |
| radare2 | clang-m32 -O0 | 0.135 | 0.225 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 202ms | ⚪ no_test |
| radare2 | clang -O0 | 0.133 | 0.215 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 232ms | ⚪ no_test |
| radare2 | clang -O2 | 0.132 | 0.209 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 246ms | ⚪ no_test |
| radare2 | gcc -O2 | 0.129 | 0.197 | 0.0% | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 241ms | ⚪ no_test |
| reko | clang -O0 | 0.117 | 0.138 | 0.0% | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1304ms | ⚪ no_test |
| reko | gcc-m32 -O0 | 0.117 | 0.133 | 0.0% | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1309ms | ⚪ no_test |
| angr | gcc -O0 | 0.117 | 0.083 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 541ms | ⚪ no_test |
| angr | gcc -O2 | 0.117 | 0.083 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 591ms | ⚪ no_test |
| angr | gcc-m32 -O0 | 0.117 | 0.083 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 514ms | ⚪ no_test |
| angr | gcc-m32 -O2 | 0.117 | 0.083 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 600ms | ⚪ no_test |
| angr | clang -O0 | 0.117 | 0.083 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 556ms | ⚪ no_test |
| angr | clang -O2 | 0.117 | 0.083 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 590ms | ⚪ no_test |
| angr | clang-m32 -O0 | 0.117 | 0.083 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 578ms | ⚪ no_test |
| angr | clang-m32 -O2 | 0.117 | 0.083 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 523ms | ⚪ no_test |
| reko | gcc -O0 | 0.116 | 0.132 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1243ms | ⚪ no_test |
| reko | clang-m32 -O0 | 0.116 | 0.129 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1406ms | ⚪ no_test |
| reko | clang -O2 | 0.111 | 0.154 | 0.0% | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1293ms | ⚪ no_test |
| reko | clang-m32 -O2 | 0.106 | 0.128 | 0.0% | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1247ms | ⚪ no_test |
| reko | gcc-m32 -O2 | 0.103 | 0.113 | 0.0% | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1329ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.079 | 0.036 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 49ms | ⚪ no_test |
| boomerang | gcc -O2 | 0.079 | 0.036 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 52ms | ⚪ no_test |
| boomerang | clang -O2 | 0.079 | 0.036 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 56ms | ⚪ no_test |
| boomerang | clang -O0 | 0.057 | 0.023 | 0.0% | #4 | 2 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 173ms | ⚪ no_test |
| boomerang | gcc-m32 -O0 | 0.001 | 0.005 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1245ms | ⚪ no_test |
| boomerang | gcc-m32 -O2 | 0.001 | 0.005 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1160ms | ⚪ no_test |
| boomerang | clang-m32 -O0 | 0.001 | 0.005 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1196ms | ⚪ no_test |
| boomerang | clang-m32 -O2 | 0.001 | 0.005 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1216ms | ⚪ no_test |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 225 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 588ms | ⚪ no_test |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 722ms | ⚪ no_test |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 495ms | ⚪ no_test |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 153 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 494ms | ⚪ no_test |
| snowman | clang -O0 | 0.000 | 0.001 | 0.0% | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 572ms | ⚪ no_test |
| snowman | clang-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 490ms | ⚪ no_test |
| snowman | clang -O2 | 0.000 | 0.001 | 0.0% | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 626ms | ⚪ no_test |
| snowman | clang-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 156 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 563ms | ⚪ no_test |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1061ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1111ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1095ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1078ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1087ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1043ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1120ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1051ms | ❌ usage: revng [-h] [--version]  |

### `saturating_add`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O2 | 0.150 | 0.599 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 85ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.586 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 73ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.142 | 0.211 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 413ms | 🔴 compile |
| reko | gcc -O0 | 0.137 | 0.187 | 0.0% (0/5) | #1 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 505ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.135 | 0.176 | 0.0% (0/5) | #1 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 463ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.126 | 0.228 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 73ms | 🔴 compile |
| radare2 | gcc -O0 | 0.126 | 0.227 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 109ms | 🔴 compile |
| angr | gcc -O0 | 0.117 | 0.085 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 215ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.117 | 0.085 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 183ms | 🔴 compile |
| angr | gcc -O2 | 0.117 | 0.085 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 208ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.117 | 0.085 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 170ms | 🔴 compile |
| reko | gcc -O2 | 0.115 | 0.126 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 414ms | 🔴 compile |
| boomerang | gcc -O0 | 0.067 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 80ms | 🔴 compile |
| boomerang | gcc -O2 | 0.067 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 16ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.004 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 375ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 369ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 653ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 161 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 594ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 628ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 581ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1084ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1038ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1004ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 872ms | ❌ usage: revng [-h] [--version]  |

### `signum`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.541 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 109ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.423 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 505ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.573 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 73ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.150 | 0.408 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 463ms | 🔴 compile |
| radare2 | gcc -O2 | 0.150 | 0.497 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 85ms | 🔴 compile |
| reko | gcc -O2 | 0.150 | 0.484 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 414ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.563 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 73ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.150 | 0.532 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 413ms | 🔴 compile |
| angr | gcc -O0 | 0.126 | 0.127 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 215ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.126 | 0.127 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 183ms | 🔴 compile |
| angr | gcc -O2 | 0.126 | 0.127 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 208ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.126 | 0.127 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 170ms | 🔴 compile |
| boomerang | gcc -O0 | 0.069 | 0.037 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 80ms | 🔴 compile |
| boomerang | gcc -O2 | 0.069 | 0.037 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 16ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 375ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 369ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 653ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 161 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 594ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 628ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 581ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1084ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1038ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1004ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 872ms | ❌ usage: revng [-h] [--version]  |

### `sum_array`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.286 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 99ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.431 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 89ms | 🔴 compile |
| reko | gcc -O0 | 0.145 | 0.224 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 543ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.125 | 0.123 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 525ms | 🔴 compile |
| angr | gcc -O0 | 0.124 | 0.120 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 262ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.124 | 0.120 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 248ms | 🔴 compile |
| angr | gcc -O2 | 0.124 | 0.120 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 223ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.124 | 0.120 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 262ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.123 | 0.165 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 88ms | 🔴 compile |
| radare2 | gcc -O2 | 0.119 | 0.143 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 105ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.116 | 0.080 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 504ms | 🔴 compile |
| reko | gcc -O2 | 0.111 | 0.055 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 493ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.028 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 21ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.028 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 21ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 474ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 474ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 155 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 637ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 220 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 589ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 595ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 658ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1015ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1044ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1000ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1052ms | ❌ usage: revng [-h] [--version]  |

---

## Overfitting Analysis

Functions where **all** decompilers scored below 0.3 are marked as objectively hard.
Functions where **only Fission** scored below 0.3 are marked as quality gaps.

**Objectively hard functions (28):** `count_bits`, `clamp`, `signum`, `checksum`, `classify_range`, `saturating_add`, `rc4_init`, `rc4_crypt`, `crc32`, `sum_array`, `reverse_in_place`, `find_pair_value`, `accumulate_pairs`, `pointer_stride_sum`, `manipulate_bitfields`, `matrix_multiply`, `fibonacci`, `fibonacci_iter`, `max`, `bubble_sort`, `linear_search`, `binary_search`, `factorial`, `gcd`, `power`, `process_code`, `reverse_string`, `find_substring`