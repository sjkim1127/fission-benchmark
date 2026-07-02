# Fission Benchmark Report

**Generated:** 2026-07-02 04:32 UTC
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
| reko | gcc -O0 | 0.141 | 0.204 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 522ms | 🔴 compile |
| reko | gcc -O2 | 0.125 | 0.124 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 517ms | 🔴 compile |
| radare2 | gcc -O2 | 0.121 | 0.153 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 93ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.120 | 0.102 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 533ms | 🔴 compile |
| angr | gcc -O0 | 0.119 | 0.097 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 230ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.119 | 0.097 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 225ms | 🔴 compile |
| angr | gcc -O2 | 0.119 | 0.097 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 234ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.119 | 0.097 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 246ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.113 | 0.116 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 82ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.112 | 0.060 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 539ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 20ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 19ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 482ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 496ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 587ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 155 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 524ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 220 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 509ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 505ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 947ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 896ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 919ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 895ms | ❌ usage: revng [-h] [--version]  |

### `binary_search`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.389 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 52ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.409 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 48ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.124 | 0.172 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 285ms | 🔴 compile |
| radare2 | gcc -O2 | 0.120 | 0.252 | 0.0% (0/6) | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 51ms | 🔴 compile |
| reko | gcc -O0 | 0.119 | 0.145 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 258ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.117 | 0.236 | 0.0% (0/6) | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 47ms | 🔴 compile |
| angr | gcc -O0 | 0.113 | 0.064 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 131ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.113 | 0.064 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 130ms | 🔴 compile |
| angr | gcc -O2 | 0.113 | 0.064 | 0.0% (0/6) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 124ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.113 | 0.064 | 0.0% (0/6) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 124ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.109 | 0.146 | 0.0% (0/6) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 270ms | 🔴 compile |
| reko | gcc -O2 | 0.097 | 0.084 | 0.0% (0/6) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 286ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.023 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.023 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 237ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 191ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% (0/6) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 483ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 669ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 639ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 499ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 955ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 853ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 976ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 751ms | ❌ usage: revng [-h] [--version]  |

### `bubble_sort`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc-m32 -O0 | 0.150 | 0.322 | 0.0% (0/5) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 48ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.135 | 0.172 | 0.0% (0/5) | #2 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 285ms | 🔴 compile |
| radare2 | gcc -O0 | 0.129 | 0.144 | 0.0% (0/5) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 52ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.127 | 0.186 | 0.0% (0/5) | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 47ms | 🔴 compile |
| reko | gcc -O2 | 0.120 | 0.102 | 0.0% (0/5) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 286ms | 🔴 compile |
| angr | gcc -O0 | 0.120 | 0.099 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 131ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.120 | 0.099 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 130ms | 🔴 compile |
| angr | gcc -O2 | 0.120 | 0.099 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 124ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.120 | 0.099 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 124ms | 🔴 compile |
| reko | gcc -O0 | 0.118 | 0.091 | 0.0% (0/5) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 258ms | 🔴 compile |
| radare2 | gcc -O2 | 0.118 | 0.141 | 0.0% (0/5) | #3 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 51ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.113 | 0.116 | 0.0% (0/5) | #3 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 270ms | 🔴 compile |
| boomerang | gcc -O0 | 0.079 | 0.037 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.079 | 0.037 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 237ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 191ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% (0/5) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 483ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% (0/5) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 639ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% (0/5) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 499ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 669ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 955ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 853ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 976ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 751ms | ❌ usage: revng [-h] [--version]  |

### `checksum`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.454 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 78ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.523 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 68ms | 🔴 compile |
| reko | gcc -O0 | 0.135 | 0.176 | 0.0% (0/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 454ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.130 | 0.151 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 453ms | 🔴 compile |
| angr | gcc -O0 | 0.117 | 0.087 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 224ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.117 | 0.087 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 190ms | 🔴 compile |
| angr | gcc -O2 | 0.117 | 0.087 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 209ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.117 | 0.087 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 186ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.117 | 0.086 | 0.0% (0/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 414ms | 🔴 compile |
| radare2 | gcc -O2 | 0.117 | 0.134 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 77ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.111 | 0.105 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 71ms | 🔴 compile |
| reko | gcc -O2 | 0.108 | 0.039 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 421ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 38ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 15ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.004 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 399ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 404ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 598ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 161 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 558ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 592ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 575ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 952ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 968ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 945ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1000ms | ❌ usage: revng [-h] [--version]  |

### `clamp`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.485 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 78ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.407 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 454ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.559 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 68ms | 🔴 compile |
| radare2 | gcc -O2 | 0.150 | 0.571 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 77ms | 🔴 compile |
| reko | gcc -O2 | 0.150 | 0.386 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 421ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.693 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 71ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.150 | 0.440 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 414ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.122 | 0.110 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 453ms | 🔴 compile |
| angr | gcc -O0 | 0.118 | 0.091 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 224ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.118 | 0.091 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 190ms | 🔴 compile |
| angr | gcc -O2 | 0.118 | 0.091 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 209ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.118 | 0.091 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 186ms | 🔴 compile |
| boomerang | gcc -O0 | 0.069 | 0.035 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 38ms | 🔴 compile |
| boomerang | gcc -O2 | 0.069 | 0.035 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 15ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 404ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 399ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 598ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% (0/6) | #5 | 161 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 558ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 592ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% (0/6) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 575ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 952ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 968ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 945ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1000ms | ❌ usage: revng [-h] [--version]  |

### `classify_range`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O2 | 0.150 | 0.489 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 77ms | 🔴 compile |
| reko | gcc -O2 | 0.150 | 0.362 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 421ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.477 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 71ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.150 | 0.353 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 414ms | 🔴 compile |
| angr | gcc -O0 | 0.126 | 0.131 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 224ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.126 | 0.131 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 190ms | 🔴 compile |
| angr | gcc -O2 | 0.126 | 0.131 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 209ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.126 | 0.131 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 186ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.119 | 0.146 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 68ms | 🔴 compile |
| radare2 | gcc -O0 | 0.119 | 0.144 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 78ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.119 | 0.194 | 0.0% (0/5) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 453ms | 🔴 compile |
| reko | gcc -O0 | 0.097 | 0.082 | 0.0% (0/5) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 454ms | 🔴 compile |
| boomerang | gcc -O0 | 0.079 | 0.033 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 38ms | 🔴 compile |
| boomerang | gcc -O2 | 0.079 | 0.033 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 15ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 404ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 399ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 598ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 161 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 558ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 592ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 575ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 952ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 968ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 945ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1000ms | ❌ usage: revng [-h] [--version]  |

### `count_bits`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.638 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 78ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.408 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 454ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.607 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 68ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.150 | 0.430 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 453ms | 🔴 compile |
| radare2 | gcc -O2 | 0.150 | 0.536 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 77ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.520 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 71ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.150 | 0.358 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 414ms | 🔴 compile |
| reko | gcc -O2 | 0.132 | 0.208 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 421ms | 🔴 compile |
| angr | gcc -O0 | 0.129 | 0.144 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 224ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.129 | 0.144 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 190ms | 🔴 compile |
| angr | gcc -O2 | 0.129 | 0.144 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 209ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.129 | 0.144 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 186ms | 🔴 compile |
| boomerang | gcc -O0 | 0.089 | 0.088 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 38ms | 🔴 compile |
| boomerang | gcc -O2 | 0.089 | 0.088 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 15ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 404ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 399ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 598ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 592ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 161 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 558ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 575ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 952ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 968ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 945ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1000ms | ❌ usage: revng [-h] [--version]  |

### `crc32`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.299 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 148ms | ⚪ no_test |
| radare2 | clang -O0 | 0.150 | 0.371 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 173ms | ⚪ no_test |
| radare2 | clang-m32 -O0 | 0.150 | 0.316 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 128ms | ⚪ no_test |
| radare2 | clang -O2 | 0.141 | 0.205 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 153ms | ⚪ no_test |
| radare2 | clang-m32 -O2 | 0.126 | 0.132 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 134ms | ⚪ no_test |
| radare2 | gcc-m32 -O0 | 0.126 | 0.129 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 150ms | ⚪ no_test |
| radare2 | gcc-m32 -O2 | 0.125 | 0.176 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 126ms | ⚪ no_test |
| reko | clang -O0 | 0.123 | 0.116 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 868ms | ⚪ no_test |
| reko | clang-m32 -O0 | 0.123 | 0.116 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 815ms | ⚪ no_test |
| radare2 | gcc -O2 | 0.122 | 0.162 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 151ms | ⚪ no_test |
| reko | gcc -O0 | 0.120 | 0.102 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 905ms | ⚪ no_test |
| angr | gcc -O0 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 360ms | ⚪ no_test |
| angr | gcc -O2 | 0.115 | 0.075 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 402ms | ⚪ no_test |
| angr | gcc-m32 -O0 | 0.115 | 0.075 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 366ms | ⚪ no_test |
| angr | gcc-m32 -O2 | 0.115 | 0.075 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 377ms | ⚪ no_test |
| angr | clang -O0 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 397ms | ⚪ no_test |
| angr | clang -O2 | 0.115 | 0.075 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 376ms | ⚪ no_test |
| angr | clang-m32 -O0 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 336ms | ⚪ no_test |
| angr | clang-m32 -O2 | 0.115 | 0.075 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 357ms | ⚪ no_test |
| reko | gcc-m32 -O2 | 0.114 | 0.071 | 0.0% | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 970ms | ⚪ no_test |
| reko | gcc-m32 -O0 | 0.114 | 0.069 | 0.0% | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 859ms | ⚪ no_test |
| reko | gcc -O2 | 0.108 | 0.042 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1144ms | ⚪ no_test |
| reko | clang-m32 -O2 | 0.107 | 0.035 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 922ms | ⚪ no_test |
| reko | clang -O2 | 0.105 | 0.026 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 964ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.076 | 0.022 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 33ms | ⚪ no_test |
| boomerang | gcc -O2 | 0.076 | 0.022 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 46ms | ⚪ no_test |
| boomerang | clang -O0 | 0.076 | 0.022 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 38ms | ⚪ no_test |
| boomerang | clang -O2 | 0.076 | 0.022 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 34ms | ⚪ no_test |
| snowman | clang-m32 -O2 | 0.000 | 0.002 | 0.0% | #4 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 456ms | ⚪ no_test |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 513ms | ⚪ no_test |
| boomerang | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 816ms | ⚪ no_test |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #5 | 153 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 479ms | ⚪ no_test |
| boomerang | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 800ms | ⚪ no_test |
| snowman | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 553ms | ⚪ no_test |
| snowman | clang -O0 | 0.000 | 0.001 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 605ms | ⚪ no_test |
| boomerang | clang-m32 -O0 | 0.000 | 0.002 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 815ms | ⚪ no_test |
| snowman | clang-m32 -O0 | 0.000 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 518ms | ⚪ no_test |
| boomerang | clang-m32 -O2 | 0.000 | 0.002 | 0.0% | #5 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 828ms | ⚪ no_test |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 221 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 634ms | ⚪ no_test |
| snowman | clang -O2 | 0.000 | 0.001 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 590ms | ⚪ no_test |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 938ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 892ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 983ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 989ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 942ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 985ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1015ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 952ms | ❌ usage: revng [-h] [--version]  |

### `factorial`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.469 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 52ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.437 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 258ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.120 | 0.151 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 48ms | 🔴 compile |
| angr | gcc -O0 | 0.119 | 0.095 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 131ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.119 | 0.095 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 130ms | 🔴 compile |
| angr | gcc -O2 | 0.119 | 0.095 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 124ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.119 | 0.095 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 124ms | 🔴 compile |
| radare2 | gcc -O2 | 0.118 | 0.189 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 51ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.107 | 0.136 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 47ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.098 | 0.041 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 285ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.098 | 0.088 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 270ms | 🔴 compile |
| reko | gcc -O2 | 0.086 | 0.028 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 286ms | 🔴 compile |
| boomerang | gcc -O0 | 0.072 | 0.048 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.072 | 0.048 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 237ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 191ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.000 | 0.0% (0/5) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 669ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 483ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.000 | 0.0% (0/5) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 639ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% (0/5) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 499ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 955ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 853ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 976ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 751ms | ❌ usage: revng [-h] [--version]  |

### `fibonacci`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.543 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 52ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.289 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 258ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.526 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 48ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.150 | 0.545 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 285ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.122 | 0.208 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 47ms | 🔴 compile |
| angr | gcc -O0 | 0.121 | 0.105 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 131ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.121 | 0.105 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 130ms | 🔴 compile |
| angr | gcc -O2 | 0.121 | 0.105 | 0.0% (0/6) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 124ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.121 | 0.105 | 0.0% (0/6) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 124ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.120 | 0.200 | 0.0% (0/6) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 270ms | 🔴 compile |
| radare2 | gcc -O2 | 0.115 | 0.176 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 51ms | 🔴 compile |
| reko | gcc -O2 | 0.106 | 0.132 | 0.0% (0/6) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 286ms | 🔴 compile |
| boomerang | gcc -O0 | 0.068 | 0.029 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.068 | 0.029 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 237ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 191ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 483ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 499ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.000 | 0.0% (0/6) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 669ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.000 | 0.0% (0/6) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 639ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 955ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 853ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 976ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 751ms | ❌ usage: revng [-h] [--version]  |

### `fibonacci_iter`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.688 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 52ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.412 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 48ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.150 | 0.302 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 285ms | 🔴 compile |
| reko | gcc -O0 | 0.140 | 0.252 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 258ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.138 | 0.241 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 47ms | 🔴 compile |
| radare2 | gcc -O2 | 0.138 | 0.238 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 51ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.134 | 0.219 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 270ms | 🔴 compile |
| reko | gcc -O2 | 0.122 | 0.161 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 286ms | 🔴 compile |
| angr | gcc -O0 | 0.115 | 0.073 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 131ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.115 | 0.073 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 130ms | 🔴 compile |
| angr | gcc -O2 | 0.115 | 0.073 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 124ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.115 | 0.073 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 124ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.027 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.027 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 237ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 191ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 483ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 499ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 669ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 639ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 955ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 853ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 976ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 751ms | ❌ usage: revng [-h] [--version]  |

### `find_pair_value`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc-m32 -O0 | 0.150 | 0.307 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 86ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.141 | 0.204 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 533ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.140 | 0.248 | 0.0% (0/5) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 82ms | 🔴 compile |
| reko | gcc -O0 | 0.138 | 0.190 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 522ms | 🔴 compile |
| radare2 | gcc -O0 | 0.134 | 0.172 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 95ms | 🔴 compile |
| angr | gcc -O0 | 0.128 | 0.139 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 230ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.128 | 0.139 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 225ms | 🔴 compile |
| angr | gcc -O2 | 0.128 | 0.139 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 234ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.128 | 0.139 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 246ms | 🔴 compile |
| reko | gcc -O2 | 0.126 | 0.131 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 517ms | 🔴 compile |
| radare2 | gcc -O2 | 0.125 | 0.174 | 0.0% (0/5) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 93ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.108 | 0.040 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 539ms | 🔴 compile |
| boomerang | gcc -O0 | 0.078 | 0.029 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 20ms | 🔴 compile |
| boomerang | gcc -O2 | 0.078 | 0.029 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 19ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 496ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 482ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 155 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 524ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 587ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 220 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 509ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 505ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 947ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 896ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 919ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 895ms | ❌ usage: revng [-h] [--version]  |

### `find_substring`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.384 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 193ms | ⚪ no_test |
| radare2 | gcc-m32 -O0 | 0.150 | 0.358 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 185ms | ⚪ no_test |
| radare2 | gcc-m32 -O2 | 0.150 | 0.352 | 0.0% | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 188ms | ⚪ no_test |
| radare2 | gcc -O2 | 0.126 | 0.228 | 0.0% | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 225ms | ⚪ no_test |
| radare2 | clang-m32 -O2 | 0.116 | 0.228 | 0.0% | #1 | 0 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 183ms | ⚪ no_test |
| reko | clang-m32 -O0 | 0.113 | 0.167 | 0.0% | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1295ms | ⚪ no_test |
| reko | gcc-m32 -O0 | 0.111 | 0.156 | 0.0% | #2 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1269ms | ⚪ no_test |
| angr | gcc -O0 | 0.111 | 0.054 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 569ms | ⚪ no_test |
| angr | gcc -O2 | 0.111 | 0.054 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 604ms | ⚪ no_test |
| angr | gcc-m32 -O0 | 0.111 | 0.054 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 522ms | ⚪ no_test |
| angr | gcc-m32 -O2 | 0.111 | 0.054 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 582ms | ⚪ no_test |
| angr | clang -O0 | 0.111 | 0.054 | 0.0% | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 543ms | ⚪ no_test |
| angr | clang -O2 | 0.111 | 0.054 | 0.0% | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 587ms | ⚪ no_test |
| angr | clang-m32 -O0 | 0.111 | 0.054 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 579ms | ⚪ no_test |
| angr | clang-m32 -O2 | 0.111 | 0.054 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 492ms | ⚪ no_test |
| reko | clang -O0 | 0.110 | 0.149 | 0.0% | #2 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1339ms | ⚪ no_test |
| reko | gcc -O0 | 0.102 | 0.111 | 0.0% | #3 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1247ms | ⚪ no_test |
| radare2 | clang -O0 | 0.100 | 0.099 | 0.0% | #3 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 211ms | ⚪ no_test |
| radare2 | clang-m32 -O0 | 0.097 | 0.086 | 0.0% | #3 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 173ms | ⚪ no_test |
| radare2 | clang -O2 | 0.087 | 0.086 | 0.0% | #2 | 0 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 239ms | ⚪ no_test |
| reko | clang-m32 -O2 | 0.085 | 0.146 | 0.0% | #3 | 1 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1301ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.081 | 0.045 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 51ms | ⚪ no_test |
| boomerang | gcc -O2 | 0.081 | 0.045 | 0.0% | #3 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 54ms | ⚪ no_test |
| boomerang | clang -O2 | 0.081 | 0.045 | 0.0% | #3 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 53ms | ⚪ no_test |
| reko | gcc-m32 -O2 | 0.075 | 0.116 | 0.0% | #3 | 2 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1276ms | ⚪ no_test |
| reko | clang -O2 | 0.072 | 0.080 | 0.0% | #4 | 1 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1250ms | ⚪ no_test |
| reko | gcc -O2 | 0.068 | 0.081 | 0.0% | #4 | 2 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1209ms | ⚪ no_test |
| boomerang | clang -O0 | 0.066 | 0.020 | 0.0% | #4 | 2 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 191ms | ⚪ no_test |
| boomerang | gcc-m32 -O2 | 0.001 | 0.006 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1191ms | ⚪ no_test |
| boomerang | clang-m32 -O0 | 0.001 | 0.006 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1147ms | ⚪ no_test |
| boomerang | gcc-m32 -O0 | 0.001 | 0.006 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1244ms | ⚪ no_test |
| boomerang | clang-m32 -O2 | 0.001 | 0.006 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1226ms | ⚪ no_test |
| snowman | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 470ms | ⚪ no_test |
| snowman | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% | #5 | 153 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 427ms | ⚪ no_test |
| snowman | clang-m32 -O0 | 0.001 | 0.003 | 0.0% | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 462ms | ⚪ no_test |
| snowman | gcc -O0 | 0.001 | 0.002 | 0.0% | #5 | 225 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 536ms | ⚪ no_test |
| snowman | clang -O0 | 0.001 | 0.002 | 0.0% | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 533ms | ⚪ no_test |
| snowman | clang-m32 -O2 | 0.001 | 0.002 | 0.0% | #5 | 156 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 470ms | ⚪ no_test |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 645ms | ⚪ no_test |
| snowman | clang -O2 | 0.000 | 0.002 | 0.0% | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 588ms | ⚪ no_test |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 896ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 954ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 984ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 973ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 970ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 924ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1000ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 949ms | ❌ usage: revng [-h] [--version]  |

### `gcd`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.302 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 52ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.369 | 0.0% (0/6) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 258ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.486 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 48ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.150 | 0.546 | 0.0% (0/6) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 285ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.149 | 0.294 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 47ms | 🔴 compile |
| radare2 | gcc -O2 | 0.148 | 0.242 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 51ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.140 | 0.200 | 0.0% (0/6) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 270ms | 🔴 compile |
| reko | gcc -O2 | 0.138 | 0.188 | 0.0% (0/6) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 286ms | 🔴 compile |
| angr | gcc -O0 | 0.130 | 0.149 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 131ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.130 | 0.149 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 130ms | 🔴 compile |
| angr | gcc -O2 | 0.130 | 0.149 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 124ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.130 | 0.149 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 124ms | 🔴 compile |
| boomerang | gcc -O0 | 0.088 | 0.082 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.088 | 0.082 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 237ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 191ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 483ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 499ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 669ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 639ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 955ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 853ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 976ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 751ms | ❌ usage: revng [-h] [--version]  |

### `linear_search`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.389 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 52ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.369 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 48ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.150 | 0.354 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 285ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.369 | 0.0% (0/6) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 47ms | 🔴 compile |
| reko | gcc -O0 | 0.140 | 0.249 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 258ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.139 | 0.247 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 270ms | 🔴 compile |
| radare2 | gcc -O2 | 0.139 | 0.296 | 0.0% (0/6) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 51ms | 🔴 compile |
| angr | gcc -O0 | 0.130 | 0.148 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 131ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.130 | 0.148 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 130ms | 🔴 compile |
| angr | gcc -O2 | 0.130 | 0.148 | 0.0% (0/6) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 124ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.130 | 0.148 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 124ms | 🔴 compile |
| reko | gcc -O2 | 0.111 | 0.104 | 0.0% (0/6) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 286ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.028 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.028 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 237ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.002 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 191ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 483ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 499ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 669ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 639ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 955ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 853ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 976ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 751ms | ❌ usage: revng [-h] [--version]  |

### `manipulate_bitfields`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O2 | 0.150 | 0.372 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 217ms | ⚪ no_test |
| radare2 | gcc-m32 -O2 | 0.150 | 0.367 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 199ms | ⚪ no_test |
| radare2 | clang -O2 | 0.150 | 0.384 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 240ms | ⚪ no_test |
| radare2 | clang-m32 -O2 | 0.150 | 0.378 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 222ms | ⚪ no_test |
| radare2 | gcc-m32 -O0 | 0.133 | 0.217 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 204ms | ⚪ no_test |
| radare2 | clang-m32 -O0 | 0.133 | 0.214 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 193ms | ⚪ no_test |
| reko | gcc -O2 | 0.130 | 0.149 | 0.0% | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1258ms | ⚪ no_test |
| radare2 | clang -O0 | 0.130 | 0.198 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 276ms | ⚪ no_test |
| reko | clang -O2 | 0.127 | 0.135 | 0.0% | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1375ms | ⚪ no_test |
| reko | gcc-m32 -O0 | 0.123 | 0.117 | 0.0% | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1316ms | ⚪ no_test |
| reko | clang -O0 | 0.123 | 0.116 | 0.0% | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1321ms | ⚪ no_test |
| reko | clang-m32 -O0 | 0.120 | 0.100 | 0.0% | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1363ms | ⚪ no_test |
| reko | gcc -O0 | 0.120 | 0.099 | 0.0% | #1 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1311ms | ⚪ no_test |
| reko | clang-m32 -O2 | 0.119 | 0.094 | 0.0% | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1262ms | ⚪ no_test |
| radare2 | gcc -O0 | 0.118 | 0.140 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 215ms | ⚪ no_test |
| angr | gcc -O0 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 550ms | ⚪ no_test |
| angr | gcc -O2 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 608ms | ⚪ no_test |
| angr | gcc-m32 -O0 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 595ms | ⚪ no_test |
| angr | gcc-m32 -O2 | 0.115 | 0.075 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 494ms | ⚪ no_test |
| angr | clang -O0 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 636ms | ⚪ no_test |
| angr | clang -O2 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 623ms | ⚪ no_test |
| angr | clang-m32 -O0 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 509ms | ⚪ no_test |
| angr | clang-m32 -O2 | 0.115 | 0.075 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 486ms | ⚪ no_test |
| reko | gcc-m32 -O2 | 0.114 | 0.068 | 0.0% | #3 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1384ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.071 | 0.047 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 48ms | ⚪ no_test |
| boomerang | gcc -O2 | 0.071 | 0.047 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 45ms | ⚪ no_test |
| boomerang | clang -O0 | 0.071 | 0.047 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 76ms | ⚪ no_test |
| boomerang | clang -O2 | 0.071 | 0.047 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 61ms | ⚪ no_test |
| boomerang | gcc-m32 -O0 | 0.001 | 0.004 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1198ms | ⚪ no_test |
| boomerang | gcc-m32 -O2 | 0.001 | 0.004 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1188ms | ⚪ no_test |
| boomerang | clang-m32 -O0 | 0.001 | 0.004 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1206ms | ⚪ no_test |
| boomerang | clang-m32 -O2 | 0.001 | 0.004 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1252ms | ⚪ no_test |
| snowman | clang-m32 -O0 | 0.001 | 0.003 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 437ms | ⚪ no_test |
| snowman | clang-m32 -O2 | 0.001 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 437ms | ⚪ no_test |
| snowman | gcc -O0 | 0.000 | 0.002 | 0.0% | #5 | 221 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 523ms | ⚪ no_test |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 618ms | ⚪ no_test |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #5 | 153 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 513ms | ⚪ no_test |
| snowman | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 590ms | ⚪ no_test |
| snowman | clang -O0 | 0.000 | 0.002 | 0.0% | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 548ms | ⚪ no_test |
| snowman | clang -O2 | 0.000 | 0.002 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 531ms | ⚪ no_test |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 993ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1011ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1003ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 983ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 950ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1057ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 912ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 953ms | ❌ usage: revng [-h] [--version]  |

### `matrix_multiply`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.559 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 215ms | ⚪ no_test |
| radare2 | clang -O0 | 0.150 | 0.679 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 276ms | ⚪ no_test |
| radare2 | clang-m32 -O0 | 0.150 | 0.517 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 193ms | ⚪ no_test |
| reko | gcc-m32 -O0 | 0.140 | 0.199 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1316ms | ⚪ no_test |
| reko | clang-m32 -O0 | 0.140 | 0.198 | 0.0% | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1363ms | ⚪ no_test |
| radare2 | gcc-m32 -O0 | 0.129 | 0.145 | 0.0% | #2 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 204ms | ⚪ no_test |
| radare2 | gcc -O2 | 0.123 | 0.165 | 0.0% | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 217ms | ⚪ no_test |
| radare2 | clang -O2 | 0.122 | 0.209 | 0.0% | #1 | 0 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 240ms | ⚪ no_test |
| reko | gcc -O0 | 0.119 | 0.096 | 0.0% | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1311ms | ⚪ no_test |
| reko | clang -O0 | 0.118 | 0.090 | 0.0% | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1321ms | ⚪ no_test |
| radare2 | gcc-m32 -O2 | 0.117 | 0.137 | 0.0% | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 199ms | ⚪ no_test |
| radare2 | clang-m32 -O2 | 0.114 | 0.169 | 0.0% | #1 | 0 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 222ms | ⚪ no_test |
| angr | gcc -O0 | 0.112 | 0.060 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 550ms | ⚪ no_test |
| angr | gcc -O2 | 0.112 | 0.060 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 608ms | ⚪ no_test |
| angr | gcc-m32 -O0 | 0.112 | 0.060 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 595ms | ⚪ no_test |
| angr | gcc-m32 -O2 | 0.112 | 0.060 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 494ms | ⚪ no_test |
| angr | clang -O0 | 0.112 | 0.060 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 636ms | ⚪ no_test |
| angr | clang -O2 | 0.112 | 0.060 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 623ms | ⚪ no_test |
| angr | clang-m32 -O0 | 0.112 | 0.060 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 509ms | ⚪ no_test |
| angr | clang-m32 -O2 | 0.112 | 0.060 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 486ms | ⚪ no_test |
| reko | gcc -O2 | 0.107 | 0.084 | 0.0% | #3 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1258ms | ⚪ no_test |
| reko | gcc-m32 -O2 | 0.097 | 0.034 | 0.0% | #3 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1384ms | ⚪ no_test |
| reko | clang -O2 | 0.096 | 0.081 | 0.0% | #3 | 0 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1375ms | ⚪ no_test |
| reko | clang-m32 -O2 | 0.096 | 0.081 | 0.0% | #3 | 0 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1262ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.084 | 0.060 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 48ms | ⚪ no_test |
| boomerang | gcc -O2 | 0.084 | 0.060 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 45ms | ⚪ no_test |
| boomerang | clang -O0 | 0.084 | 0.060 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 76ms | ⚪ no_test |
| boomerang | clang -O2 | 0.084 | 0.060 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 61ms | ⚪ no_test |
| boomerang | clang-m32 -O2 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1252ms | ⚪ no_test |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1198ms | ⚪ no_test |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1188ms | ⚪ no_test |
| boomerang | clang-m32 -O0 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1206ms | ⚪ no_test |
| snowman | clang-m32 -O0 | 0.001 | 0.003 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 437ms | ⚪ no_test |
| snowman | clang-m32 -O2 | 0.001 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 437ms | ⚪ no_test |
| snowman | gcc -O0 | 0.000 | 0.002 | 0.0% | #5 | 221 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 523ms | ⚪ no_test |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #5 | 153 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 513ms | ⚪ no_test |
| snowman | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 590ms | ⚪ no_test |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 618ms | ⚪ no_test |
| snowman | clang -O0 | 0.000 | 0.002 | 0.0% | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 548ms | ⚪ no_test |
| snowman | clang -O2 | 0.000 | 0.002 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 531ms | ⚪ no_test |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 993ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1011ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1003ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 983ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 950ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1057ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 912ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 953ms | ❌ usage: revng [-h] [--version]  |

### `max`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.415 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 52ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.315 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 258ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.389 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 48ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.150 | 0.395 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 285ms | 🔴 compile |
| radare2 | gcc -O2 | 0.150 | 0.630 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 51ms | 🔴 compile |
| reko | gcc -O2 | 0.150 | 0.315 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 286ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.391 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 47ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.150 | 0.398 | 0.0% (0/6) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 270ms | 🔴 compile |
| angr | gcc -O0 | 0.128 | 0.141 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 131ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.128 | 0.141 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 130ms | 🔴 compile |
| angr | gcc -O2 | 0.128 | 0.141 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 124ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.128 | 0.141 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 124ms | 🔴 compile |
| boomerang | gcc -O0 | 0.068 | 0.032 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.068 | 0.032 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 237ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 191ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.000 | 0.0% (0/6) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 669ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 483ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.000 | 0.0% (0/6) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 639ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 499ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 955ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 853ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 976ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 751ms | ❌ usage: revng [-h] [--version]  |

### `pointer_stride_sum`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O2 | 0.150 | 0.330 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 93ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.367 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 82ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.142 | 0.209 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 86ms | 🔴 compile |
| radare2 | gcc -O0 | 0.141 | 0.206 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 95ms | 🔴 compile |
| reko | gcc -O2 | 0.140 | 0.198 | 0.0% (0/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 517ms | 🔴 compile |
| angr | gcc -O0 | 0.123 | 0.115 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 230ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.123 | 0.115 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 225ms | 🔴 compile |
| angr | gcc -O2 | 0.123 | 0.115 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 234ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.123 | 0.115 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 246ms | 🔴 compile |
| reko | gcc -O0 | 0.122 | 0.108 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 522ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.120 | 0.102 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 533ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.109 | 0.097 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 539ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 20ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 19ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 496ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 482ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 587ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 155 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 524ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 220 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 509ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 505ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 947ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 896ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 919ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 895ms | ❌ usage: revng [-h] [--version]  |

### `power`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| reko | gcc-m32 -O0 | 0.138 | 0.188 | 0.0% (0/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 285ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.133 | 0.216 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 270ms | 🔴 compile |
| radare2 | gcc -O0 | 0.124 | 0.168 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 52ms | 🔴 compile |
| reko | gcc -O0 | 0.123 | 0.118 | 0.0% (0/6) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 258ms | 🔴 compile |
| reko | gcc -O2 | 0.116 | 0.129 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 286ms | 🔴 compile |
| angr | gcc -O0 | 0.116 | 0.078 | 0.0% (0/6) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 131ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.116 | 0.078 | 0.0% (0/6) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 130ms | 🔴 compile |
| angr | gcc -O2 | 0.116 | 0.078 | 0.0% (0/6) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 124ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.116 | 0.078 | 0.0% (0/6) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 124ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.112 | 0.111 | 0.0% (0/6) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 48ms | 🔴 compile |
| radare2 | gcc -O2 | 0.102 | 0.111 | 0.0% (0/6) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 51ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.099 | 0.093 | 0.0% (0/6) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 47ms | 🔴 compile |
| boomerang | gcc -O0 | 0.081 | 0.043 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.081 | 0.043 | 0.0% (0/6) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 237ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/6) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 191ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 669ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 483ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 639ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/6) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 499ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 955ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 853ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 976ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 751ms | ❌ usage: revng [-h] [--version]  |

### `process_code`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O2 | 0.148 | 0.288 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 51ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.146 | 0.282 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 47ms | 🔴 compile |
| angr | gcc -O0 | 0.123 | 0.114 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 131ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.123 | 0.114 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 130ms | 🔴 compile |
| angr | gcc -O2 | 0.123 | 0.114 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 124ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.123 | 0.114 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 124ms | 🔴 compile |
| reko | gcc -O0 | 0.116 | 0.078 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 258ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.115 | 0.075 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 285ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.112 | 0.160 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 270ms | 🔴 compile |
| reko | gcc -O2 | 0.096 | 0.079 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 286ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.094 | 0.121 | 0.0% (0/5) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 48ms | 🔴 compile |
| radare2 | gcc -O0 | 0.075 | 0.025 | 0.0% (0/5) | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 52ms | 🔴 compile |
| boomerang | gcc -O0 | 0.067 | 0.025 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10ms | 🔴 compile |
| boomerang | gcc -O2 | 0.067 | 0.025 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.004 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 191ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.004 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 237ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 483ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 223 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 639ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 499ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 669ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 955ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 853ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 976ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 751ms | ❌ usage: revng [-h] [--version]  |

### `rc4_crypt`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.424 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 148ms | ⚪ no_test |
| radare2 | gcc-m32 -O0 | 0.150 | 0.292 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 150ms | ⚪ no_test |
| radare2 | clang -O0 | 0.150 | 0.395 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 173ms | ⚪ no_test |
| radare2 | clang-m32 -O0 | 0.150 | 0.430 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 128ms | ⚪ no_test |
| radare2 | gcc -O2 | 0.143 | 0.267 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 151ms | ⚪ no_test |
| radare2 | clang -O2 | 0.133 | 0.263 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 153ms | ⚪ no_test |
| radare2 | clang-m32 -O2 | 0.131 | 0.257 | 0.0% | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 134ms | ⚪ no_test |
| radare2 | gcc-m32 -O2 | 0.130 | 0.200 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 126ms | ⚪ no_test |
| reko | gcc-m32 -O0 | 0.127 | 0.135 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 859ms | ⚪ no_test |
| reko | clang -O0 | 0.124 | 0.119 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 868ms | ⚪ no_test |
| reko | gcc -O0 | 0.124 | 0.118 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 905ms | ⚪ no_test |
| reko | clang-m32 -O0 | 0.121 | 0.106 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 815ms | ⚪ no_test |
| angr | gcc -O0 | 0.113 | 0.067 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 360ms | ⚪ no_test |
| angr | gcc -O2 | 0.113 | 0.067 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 402ms | ⚪ no_test |
| angr | gcc-m32 -O0 | 0.113 | 0.067 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 366ms | ⚪ no_test |
| angr | gcc-m32 -O2 | 0.113 | 0.067 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 377ms | ⚪ no_test |
| angr | clang -O0 | 0.113 | 0.067 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 397ms | ⚪ no_test |
| angr | clang -O2 | 0.113 | 0.067 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 376ms | ⚪ no_test |
| angr | clang-m32 -O0 | 0.113 | 0.067 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 336ms | ⚪ no_test |
| angr | clang-m32 -O2 | 0.113 | 0.067 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 357ms | ⚪ no_test |
| reko | gcc -O2 | 0.109 | 0.096 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1144ms | ⚪ no_test |
| reko | gcc-m32 -O2 | 0.104 | 0.068 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 970ms | ⚪ no_test |
| reko | clang-m32 -O2 | 0.101 | 0.055 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 922ms | ⚪ no_test |
| reko | clang -O2 | 0.100 | 0.049 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 964ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.079 | 0.034 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 33ms | ⚪ no_test |
| boomerang | gcc -O2 | 0.079 | 0.034 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 46ms | ⚪ no_test |
| boomerang | clang -O0 | 0.079 | 0.034 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 38ms | ⚪ no_test |
| boomerang | clang -O2 | 0.079 | 0.034 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 34ms | ⚪ no_test |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 816ms | ⚪ no_test |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 800ms | ⚪ no_test |
| boomerang | clang-m32 -O0 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 815ms | ⚪ no_test |
| boomerang | clang-m32 -O2 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 828ms | ⚪ no_test |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 513ms | ⚪ no_test |
| snowman | gcc -O0 | 0.000 | 0.002 | 0.0% | #5 | 221 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 634ms | ⚪ no_test |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 553ms | ⚪ no_test |
| snowman | clang -O0 | 0.000 | 0.002 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 605ms | ⚪ no_test |
| snowman | clang -O2 | 0.000 | 0.002 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 590ms | ⚪ no_test |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 153 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 479ms | ⚪ no_test |
| snowman | clang-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 518ms | ⚪ no_test |
| snowman | clang-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 456ms | ⚪ no_test |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 938ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 892ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 983ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 989ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 942ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 985ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1015ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 952ms | ❌ usage: revng [-h] [--version]  |

### `rc4_init`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.501 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 148ms | ⚪ no_test |
| radare2 | gcc-m32 -O0 | 0.150 | 0.301 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 150ms | ⚪ no_test |
| radare2 | clang -O0 | 0.150 | 0.291 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 173ms | ⚪ no_test |
| radare2 | clang-m32 -O0 | 0.150 | 0.350 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 128ms | ⚪ no_test |
| reko | clang -O0 | 0.136 | 0.178 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 868ms | ⚪ no_test |
| radare2 | gcc-m32 -O2 | 0.135 | 0.175 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 126ms | ⚪ no_test |
| reko | gcc-m32 -O0 | 0.127 | 0.137 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 859ms | ⚪ no_test |
| reko | gcc -O0 | 0.126 | 0.129 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 905ms | ⚪ no_test |
| radare2 | clang-m32 -O2 | 0.122 | 0.159 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 134ms | ⚪ no_test |
| reko | clang-m32 -O0 | 0.117 | 0.085 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 815ms | ⚪ no_test |
| reko | clang -O2 | 0.115 | 0.073 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 964ms | ⚪ no_test |
| reko | gcc-m32 -O2 | 0.114 | 0.070 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 970ms | ⚪ no_test |
| angr | gcc -O0 | 0.114 | 0.068 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 360ms | ⚪ no_test |
| angr | gcc -O2 | 0.114 | 0.068 | 0.0% | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 402ms | ⚪ no_test |
| angr | gcc-m32 -O0 | 0.114 | 0.068 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 366ms | ⚪ no_test |
| angr | gcc-m32 -O2 | 0.114 | 0.068 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 377ms | ⚪ no_test |
| angr | clang -O0 | 0.114 | 0.068 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 397ms | ⚪ no_test |
| angr | clang -O2 | 0.114 | 0.068 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 376ms | ⚪ no_test |
| angr | clang-m32 -O0 | 0.114 | 0.068 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 336ms | ⚪ no_test |
| angr | clang-m32 -O2 | 0.114 | 0.068 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 357ms | ⚪ no_test |
| reko | clang-m32 -O2 | 0.113 | 0.065 | 0.0% | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 922ms | ⚪ no_test |
| reko | gcc -O2 | 0.109 | 0.044 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1144ms | ⚪ no_test |
| radare2 | gcc -O2 | 0.105 | 0.025 | 0.0% | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 151ms | ⚪ no_test |
| radare2 | clang -O2 | 0.102 | 0.058 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 153ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.080 | 0.040 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 33ms | ⚪ no_test |
| boomerang | gcc -O2 | 0.080 | 0.040 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 46ms | ⚪ no_test |
| boomerang | clang -O0 | 0.080 | 0.040 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 38ms | ⚪ no_test |
| boomerang | clang -O2 | 0.080 | 0.040 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 34ms | ⚪ no_test |
| boomerang | gcc-m32 -O2 | 0.001 | 0.004 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 800ms | ⚪ no_test |
| boomerang | clang-m32 -O0 | 0.001 | 0.004 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 815ms | ⚪ no_test |
| boomerang | clang-m32 -O2 | 0.001 | 0.004 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 828ms | ⚪ no_test |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 816ms | ⚪ no_test |
| snowman | gcc -O2 | 0.000 | 0.002 | 0.0% | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 513ms | ⚪ no_test |
| snowman | clang-m32 -O2 | 0.000 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 456ms | ⚪ no_test |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 221 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 634ms | ⚪ no_test |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% | #5 | 153 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 479ms | ⚪ no_test |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 553ms | ⚪ no_test |
| snowman | clang -O0 | 0.000 | 0.002 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 605ms | ⚪ no_test |
| snowman | clang -O2 | 0.000 | 0.001 | 0.0% | #5 | 218 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 590ms | ⚪ no_test |
| snowman | clang-m32 -O0 | 0.000 | 0.002 | 0.0% | #5 | 150 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 518ms | ⚪ no_test |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 938ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 892ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 983ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 989ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 942ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 985ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1015ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 952ms | ❌ usage: revng [-h] [--version]  |

### `reverse_in_place`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc-m32 -O0 | 0.150 | 0.264 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 86ms | 🔴 compile |
| radare2 | gcc -O0 | 0.149 | 0.244 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 95ms | 🔴 compile |
| reko | gcc -O0 | 0.131 | 0.156 | 0.0% (0/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 522ms | 🔴 compile |
| radare2 | gcc -O2 | 0.123 | 0.164 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 93ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.117 | 0.133 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 82ms | 🔴 compile |
| angr | gcc -O0 | 0.116 | 0.081 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 230ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.116 | 0.081 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 225ms | 🔴 compile |
| angr | gcc -O2 | 0.116 | 0.081 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 234ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.116 | 0.081 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 246ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.113 | 0.067 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 533ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.104 | 0.069 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 539ms | 🔴 compile |
| reko | gcc -O2 | 0.103 | 0.064 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 517ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.028 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 20ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.028 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 19ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 496ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 482ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% (0/5) | #5 | 155 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 524ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 220 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 509ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 505ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 587ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 947ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 896ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 919ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 895ms | ❌ usage: revng [-h] [--version]  |

### `reverse_string`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc-m32 -O0 | 0.150 | 0.353 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 185ms | ⚪ no_test |
| radare2 | gcc-m32 -O2 | 0.148 | 0.291 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 188ms | ⚪ no_test |
| radare2 | gcc -O0 | 0.146 | 0.281 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 193ms | ⚪ no_test |
| reko | gcc -O2 | 0.142 | 0.261 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1209ms | ⚪ no_test |
| radare2 | clang-m32 -O2 | 0.140 | 0.248 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 183ms | ⚪ no_test |
| radare2 | clang-m32 -O0 | 0.135 | 0.225 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 173ms | ⚪ no_test |
| radare2 | clang -O0 | 0.133 | 0.215 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 211ms | ⚪ no_test |
| radare2 | clang -O2 | 0.132 | 0.209 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 239ms | ⚪ no_test |
| radare2 | gcc -O2 | 0.129 | 0.197 | 0.0% | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 225ms | ⚪ no_test |
| reko | clang -O0 | 0.117 | 0.138 | 0.0% | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1339ms | ⚪ no_test |
| reko | gcc-m32 -O0 | 0.117 | 0.133 | 0.0% | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1269ms | ⚪ no_test |
| angr | gcc -O0 | 0.117 | 0.083 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 569ms | ⚪ no_test |
| angr | gcc -O2 | 0.117 | 0.083 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 604ms | ⚪ no_test |
| angr | gcc-m32 -O0 | 0.117 | 0.083 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 522ms | ⚪ no_test |
| angr | gcc-m32 -O2 | 0.117 | 0.083 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 582ms | ⚪ no_test |
| angr | clang -O0 | 0.117 | 0.083 | 0.0% | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 543ms | ⚪ no_test |
| angr | clang -O2 | 0.117 | 0.083 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 587ms | ⚪ no_test |
| angr | clang-m32 -O0 | 0.117 | 0.083 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 579ms | ⚪ no_test |
| angr | clang-m32 -O2 | 0.117 | 0.083 | 0.0% | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 492ms | ⚪ no_test |
| reko | gcc -O0 | 0.116 | 0.132 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1247ms | ⚪ no_test |
| reko | clang-m32 -O0 | 0.116 | 0.129 | 0.0% | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1295ms | ⚪ no_test |
| reko | clang -O2 | 0.111 | 0.154 | 0.0% | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1250ms | ⚪ no_test |
| reko | clang-m32 -O2 | 0.106 | 0.128 | 0.0% | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1301ms | ⚪ no_test |
| reko | gcc-m32 -O2 | 0.103 | 0.113 | 0.0% | #3 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1276ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.079 | 0.036 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 51ms | ⚪ no_test |
| boomerang | gcc -O2 | 0.079 | 0.036 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 54ms | ⚪ no_test |
| boomerang | clang -O2 | 0.079 | 0.036 | 0.0% | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 53ms | ⚪ no_test |
| boomerang | clang -O0 | 0.057 | 0.023 | 0.0% | #4 | 2 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 191ms | ⚪ no_test |
| boomerang | gcc-m32 -O0 | 0.001 | 0.005 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1244ms | ⚪ no_test |
| boomerang | gcc-m32 -O2 | 0.001 | 0.005 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1191ms | ⚪ no_test |
| boomerang | clang-m32 -O0 | 0.001 | 0.005 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1147ms | ⚪ no_test |
| boomerang | clang-m32 -O2 | 0.001 | 0.005 | 0.0% | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 1226ms | ⚪ no_test |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #5 | 225 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 536ms | ⚪ no_test |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 645ms | ⚪ no_test |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 157 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 470ms | ⚪ no_test |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 153 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 427ms | ⚪ no_test |
| snowman | clang -O0 | 0.000 | 0.001 | 0.0% | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 533ms | ⚪ no_test |
| snowman | clang-m32 -O0 | 0.000 | 0.001 | 0.0% | #5 | 154 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 462ms | ⚪ no_test |
| snowman | clang -O2 | 0.000 | 0.001 | 0.0% | #5 | 224 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 588ms | ⚪ no_test |
| snowman | clang-m32 -O2 | 0.000 | 0.001 | 0.0% | #5 | 156 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 470ms | ⚪ no_test |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 896ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 954ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 984ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 973ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 970ms | ❌ usage: revng [-h] [--version]  |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 924ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1000ms | ❌ usage: revng [-h] [--version]  |
| fission | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | clang-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 949ms | ❌ usage: revng [-h] [--version]  |

### `saturating_add`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O2 | 0.150 | 0.599 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 77ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.586 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 71ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.142 | 0.211 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 414ms | 🔴 compile |
| reko | gcc -O0 | 0.137 | 0.187 | 0.0% (0/5) | #1 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 454ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.135 | 0.176 | 0.0% (0/5) | #1 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 453ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.126 | 0.228 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 68ms | 🔴 compile |
| radare2 | gcc -O0 | 0.126 | 0.227 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 78ms | 🔴 compile |
| angr | gcc -O0 | 0.117 | 0.085 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 224ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.117 | 0.085 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 190ms | 🔴 compile |
| angr | gcc -O2 | 0.117 | 0.085 | 0.0% (0/5) | #2 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 209ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.117 | 0.085 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 186ms | 🔴 compile |
| reko | gcc -O2 | 0.115 | 0.126 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 421ms | 🔴 compile |
| boomerang | gcc -O0 | 0.067 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 38ms | 🔴 compile |
| boomerang | gcc -O2 | 0.067 | 0.026 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 15ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.004 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 404ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.003 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 399ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 598ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 161 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 558ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 592ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 575ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 952ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 968ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 945ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1000ms | ❌ usage: revng [-h] [--version]  |

### `signum`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.541 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 78ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.423 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 454ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.573 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 68ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.150 | 0.408 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 453ms | 🔴 compile |
| radare2 | gcc -O2 | 0.150 | 0.497 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 77ms | 🔴 compile |
| reko | gcc -O2 | 0.150 | 0.484 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 421ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.150 | 0.563 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 71ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.150 | 0.532 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 414ms | 🔴 compile |
| angr | gcc -O0 | 0.126 | 0.127 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 224ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.126 | 0.127 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 190ms | 🔴 compile |
| angr | gcc -O2 | 0.126 | 0.127 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 209ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.126 | 0.127 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 186ms | 🔴 compile |
| boomerang | gcc -O0 | 0.069 | 0.037 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 38ms | 🔴 compile |
| boomerang | gcc -O2 | 0.069 | 0.037 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 15ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.001 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 404ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.001 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 399ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 598ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 161 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 558ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 219 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 592ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 575ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 952ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 968ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 945ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 1000ms | ❌ usage: revng [-h] [--version]  |

### `sum_array`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.286 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 95ms | 🔴 compile |
| radare2 | gcc-m32 -O0 | 0.150 | 0.431 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 86ms | 🔴 compile |
| reko | gcc -O0 | 0.145 | 0.224 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 522ms | 🔴 compile |
| reko | gcc-m32 -O0 | 0.125 | 0.123 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 533ms | 🔴 compile |
| angr | gcc -O0 | 0.124 | 0.120 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 230ms | 🔴 compile |
| angr | gcc-m32 -O0 | 0.124 | 0.120 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 225ms | 🔴 compile |
| angr | gcc -O2 | 0.124 | 0.120 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 234ms | 🔴 compile |
| angr | gcc-m32 -O2 | 0.124 | 0.120 | 0.0% (0/5) | #1 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 246ms | 🔴 compile |
| radare2 | gcc-m32 -O2 | 0.123 | 0.165 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 82ms | 🔴 compile |
| radare2 | gcc -O2 | 0.119 | 0.143 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 93ms | 🔴 compile |
| reko | gcc-m32 -O2 | 0.116 | 0.080 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 539ms | 🔴 compile |
| reko | gcc -O2 | 0.111 | 0.055 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 517ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.028 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 20ms | 🔴 compile |
| boomerang | gcc -O2 | 0.077 | 0.028 | 0.0% (0/5) | #4 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 19ms | 🔴 compile |
| boomerang | gcc-m32 -O0 | 0.000 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 496ms | 🔴 compile |
| boomerang | gcc-m32 -O2 | 0.000 | 0.002 | 0.0% (0/5) | #4 | 8 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 482ms | 🔴 compile |
| snowman | gcc-m32 -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 155 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 524ms | 🔴 compile |
| snowman | gcc -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 220 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 509ms | 🔴 compile |
| snowman | gcc-m32 -O2 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 151 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 505ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #5 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 587ms | 🔴 compile |
| fission | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 947ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 896ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 919ms | ❌ usage: revng [-h] [--version]  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| ghidra | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| revng | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 895ms | ❌ usage: revng [-h] [--version]  |

---

## Overfitting Analysis

Functions where **all** decompilers scored below 0.3 are marked as objectively hard.
Functions where **only Fission** scored below 0.3 are marked as quality gaps.

**Objectively hard functions (28):** `count_bits`, `clamp`, `signum`, `checksum`, `classify_range`, `saturating_add`, `rc4_init`, `rc4_crypt`, `crc32`, `sum_array`, `reverse_in_place`, `find_pair_value`, `accumulate_pairs`, `pointer_stride_sum`, `manipulate_bitfields`, `matrix_multiply`, `fibonacci`, `fibonacci_iter`, `max`, `bubble_sort`, `linear_search`, `binary_search`, `factorial`, `gcd`, `power`, `process_code`, `reverse_string`, `find_substring`