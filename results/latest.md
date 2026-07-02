# Fission Benchmark Report

**Generated:** 2026-07-02 07:11 UTC
**Corpus:** `dev`
**Functions evaluated:** 10

---

## Summary — Correctness Score

> Readability metrics are recorded as unvalidated raw proxies. They are not combined into a final readability score until the human validation study is complete.

| Decompiler | Correctness | Similarity | Semantic Pass | Functions |
| ---|---|---|---|--- |
| **ghidra** | 0.229 | 0.422 | 10.5% | 10 |
| **fission** | 0.210 | 0.082 | 18.3% | 10 |
| **radare2** | 0.144 | 0.400 | 0.0% | 10 |
| **reko** | 0.133 | 0.225 | 0.0% | 10 |
| **revng** | 0.098 | 0.053 | 0.0% | 9 |

---

## Per-Function Results

### `checksum` ⚪ Universally hard
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O0 | 0.374 | 0.668 | 20.0% (1/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 4 | 6072ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.150 | 0.454 | 0.0% (0/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 109ms | 🔴 compile |
| reko | gcc -O0 | 0.135 | 0.176 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 592ms | 🔴 compile |
| revng | gcc -O0 | 0.099 | 0.044 | 0.0% (0/5) | #4 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 5905ms | 🔴 compile |
| fission | gcc -O0 | 0.093 | 0.103 | 0.0% (0/5) | #5 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 2272ms | 🔴 compile |
| boomerang | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 41ms | ❌ Function at address 0x1400015b |
| angr | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| snowman | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 437ms | ❌ Snowman returned whole-program |

### `clamp` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.593 | 0.179 | 66.7% (4/6) | #1 | 0 | 2 | GNR 0.88<br>type 0.50<br>expr 0.81<br>cf 1.00<br>art 0 | 2272ms | 🟠 runtime |
| ghidra | gcc -O0 | 0.150 | 0.421 | 0.0% (0/6) | #2 | 0 | 2 | GNR 0.75<br>type 0.50<br>expr 0.77<br>cf 1.00<br>art 9 | 6072ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.150 | 0.485 | 0.0% (0/6) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 109ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.407 | 0.0% (0/6) | #4 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 592ms | 🔴 compile |
| revng | gcc -O0 | 0.107 | 0.038 | 0.0% (0/6) | #5 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 5905ms | 🔴 compile |
| boomerang | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 41ms | ❌ Function at address 0x14000155 |
| angr | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| snowman | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 437ms | ❌ Snowman returned whole-program |

### `classify_range` ⚪ Universally hard
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O0 | 0.263 | 0.167 | 20.0% (1/5) | #1 | 0 | 3 | GNR 0.85<br>type 0.50<br>expr 0.80<br>cf 1.00<br>art 7 | 6072ms | 🟠 runtime |
| fission | gcc -O0 | 0.189 | 0.093 | 20.0% (1/5) | #2 | 9 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 2272ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.119 | 0.144 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 109ms | 🔴 compile |
| reko | gcc -O0 | 0.097 | 0.082 | 0.0% (0/5) | #4 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 592ms | 🔴 compile |
| revng | gcc -O0 | 0.088 | 0.042 | 0.0% (0/5) | #5 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 5905ms | 🔴 compile |
| boomerang | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 41ms | ❌ Function at address 0x14000160 |
| angr | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| snowman | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 437ms | ❌ Snowman returned whole-program |

### `count_bits` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.226 | 0.118 | 16.7% (1/6) ⚠️intrin | #1 | 1 | 2 | GNR 0.31<br>type 0.50<br>expr 0.62<br>cf 0.50<br>art 6 | 2272ms | 🟠 runtime |
| ghidra | gcc -O0 | 0.150 | 0.688 | 0.0% (0/6) | #2 | 0 | 2 | GNR 0.14<br>type 0.50<br>expr 0.85<br>cf 1.00<br>art 2 | 6072ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.150 | 0.638 | 0.0% (0/6) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 109ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.408 | 0.0% (0/6) | #4 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 592ms | 🔴 compile |
| boomerang | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 41ms | ❌ Function at address 0x14000153 |
| angr | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| snowman | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 437ms | ❌ Snowman returned whole-program |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 5905ms | ❌ Decompiler output does not mat |

### `crc32` ⚪ Universally hard
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O0 | 0.150 | 0.343 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 4 | 11928ms | 🔴 compile |
| radare2 | gcc -O0 | 0.150 | 0.299 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 221ms | 🔴 compile |
| reko | gcc -O0 | 0.120 | 0.102 | 0.0% (0/6) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1109ms | 🔴 compile |
| revng | gcc -O0 | 0.104 | 0.068 | 0.0% (0/6) | #4 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 11181ms | 🔴 compile |
| fission | gcc -O0 | 0.056 | 0.060 | 0.0% (0/6) | #5 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10055ms | 🔴 compile |
| boomerang | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 84ms | ❌ Function at address 0x14000174 |
| angr | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 299ms | ❌ No decompiler output for targe |
| snowman | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 531ms | ❌ Snowman returned whole-program |

### `rc4_crypt` ⚪ Universally hard
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O0 | 0.333 | 0.292 | 25.0% (1/4) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 17 | 11928ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.150 | 0.424 | 0.0% (0/4) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 221ms | 🔴 compile |
| reko | gcc -O0 | 0.124 | 0.118 | 0.0% (0/4) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1109ms | 🔴 compile |
| revng | gcc -O0 | 0.102 | 0.061 | 0.0% (0/4) | #4 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 11181ms | 🔴 compile |
| fission | gcc -O0 | 0.074 | 0.009 | 0.0% (0/4) ⚠️intrin | #5 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 58 | 10055ms | 🔴 compile |
| boomerang | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 84ms | ❌ Function at address 0x14000162 |
| angr | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 299ms | ❌ No decompiler output for targe |
| snowman | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 531ms | ❌ Snowman returned whole-program |

### `rc4_init` ⚪ Universally hard
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O0 | 0.150 | 0.362 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 14 | 11928ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.150 | 0.501 | 0.0% (0/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 221ms | 🔴 compile |
| reko | gcc -O0 | 0.126 | 0.129 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1109ms | 🔴 compile |
| revng | gcc -O0 | 0.073 | 0.016 | 0.0% (0/5) | #4 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 11181ms | 🔴 compile |
| fission | gcc -O0 | 0.050 | 0.030 | 0.0% (0/5) ⚠️intrin | #5 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 34 | 10055ms | 🔴 compile |
| boomerang | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 84ms | ❌ Function at address 0x14000153 |
| angr | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 299ms | ❌ No decompiler output for targe |
| snowman | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 531ms | ❌ Snowman returned whole-program |

### `saturating_add` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.484 | 0.061 | 60.0% (3/5) ⚠️intrin | #1 | 2 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 8 | 2272ms | 🟠 runtime |
| reko | gcc -O0 | 0.137 | 0.187 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 592ms | 🔴 compile |
| ghidra | gcc -O0 | 0.131 | 0.252 | 0.0% (0/5) | #3 | 0 | 3 | GNR 0.84<br>type 0.50<br>expr 0.76<br>cf 1.00<br>art 8 | 6072ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.126 | 0.227 | 0.0% (0/5) | #4 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 109ms | 🔴 compile |
| revng | gcc -O0 | 0.097 | 0.086 | 0.0% (0/5) | #5 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 5905ms | 🔴 compile |
| boomerang | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 41ms | ❌ Function at address 0x14000166 |
| angr | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| snowman | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 437ms | ❌ Snowman returned whole-program |

### `signum`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O0 | 0.435 | 0.375 | 40.0% (2/5) | #1 | 0 | 3 | GNR 0.80<br>type 0.50<br>expr 0.85<br>cf 1.00<br>art 3 | 6072ms | 🟠 runtime |
| fission | gcc -O0 | 0.231 | 0.057 | 20.0% (1/5) | #2 | 0 | 3 | GNR 0.47<br>type 0.50<br>expr 0.82<br>cf 1.00<br>art 0 | 2272ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.150 | 0.541 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 109ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.423 | 0.0% (0/5) | #4 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 592ms | 🔴 compile |
| revng | gcc -O0 | 0.112 | 0.059 | 0.0% (0/5) | #5 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 5905ms | 🔴 compile |
| boomerang | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 41ms | ❌ Function at address 0x14000158 |
| angr | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: HTTP st |
| snowman | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 437ms | ❌ Snowman returned whole-program |

### `sum_array` ⚪ Universally hard
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O0 | 0.150 | 0.648 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 4 | 34775ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.150 | 0.286 | 0.0% (0/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 202ms | 🔴 compile |
| reko | gcc -O0 | 0.145 | 0.224 | 0.0% (0/5) | #3 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 4690ms | 🔴 compile |
| fission | gcc -O0 | 0.107 | 0.105 | 0.0% (0/5) | #4 | 1 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 6677ms | 🔴 compile |
| revng | gcc -O0 | 0.103 | 0.065 | 0.0% (0/5) | #5 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 30856ms | 🔴 compile |
| boomerang | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 224ms | ❌ Function at address 0x14000153 |
| angr | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 457ms | ❌ No decompiler output for targe |
| snowman | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 403ms | ❌ Snowman returned whole-program |

---

## Overfitting Analysis

Functions where **all** decompilers scored below 0.3 are marked as objectively hard.
Functions where **only Fission** scored below 0.3 are marked as quality gaps.

**Objectively hard functions (3):** `rc4_init`, `crc32`, `sum_array`
**Fission quality gaps (3):** `checksum`, `classify_range`, `rc4_crypt`