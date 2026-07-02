# Fission Benchmark Report

**Generated:** 2026-07-02 13:32 UTC
**Corpus:** `dev`
**Functions evaluated:** 10

---

## Summary — Correctness Score

> Readability metrics are recorded as unvalidated raw proxies. They are not combined into a final readability score until the human validation study is complete.

| Decompiler | Correctness | Similarity | Semantic Pass | Functions |
| ---|---|---|---|--- |
| **angr** | 0.764 | 0.415 | 80.8% | 10 |
| **fission** | 0.263 | 0.087 | 24.0% | 10 |
| **ghidra** | 0.260 | 0.422 | 12.5% | 10 |
| **radare2** | 0.150 | 0.400 | 0.0% | 10 |
| **reko** | 0.150 | 0.225 | 0.0% | 10 |
| **snowman** | 0.149 | 0.159 | 0.0% | 10 |
| **revng** | 0.147 | 0.053 | 0.0% | 9 |

---

## Per-Function Results

### `checksum`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.890 | 0.567 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.33<br>type 0.50<br>expr 0.71<br>cf 1.00<br>art 0 | 425ms | ✅ |
| ghidra | gcc -O0 | 0.317 | 0.668 | 20.0% (1/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 4 | 5261ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.150 | 0.454 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 83ms | 🔴 compile |
| snowman | gcc -O0 | 0.150 | 0.129 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 557ms | 🔴 compile |
| revng | gcc -O0 | 0.150 | 0.044 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 9846ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.176 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 485ms | 🔴 compile |
| fission | gcc -O0 | 0.112 | 0.103 | 0.0% (0/5) | #7 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 3334ms | 🔴 compile |
| boomerang | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 10ms | ❌ Function at address 0x1400015b |

### `clamp`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.929 | 0.708 | 100.0% (6/6) | #1 | 0 | 2 | GNR 0.00<br>type 0.50<br>expr 0.93<br>cf 1.00<br>art 0 | 425ms | ✅ |
| fission | gcc -O0 | 0.662 | 0.179 | 66.7% (4/6) | #2 | 0 | 2 | GNR 0.88<br>type 0.50<br>expr 0.81<br>cf 1.00<br>art 0 | 3334ms | 🟠 runtime |
| ghidra | gcc -O0 | 0.150 | 0.421 | 0.0% (0/6) | #3 | 0 | 2 | GNR 0.75<br>type 0.50<br>expr 0.77<br>cf 1.00<br>art 9 | 5261ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.150 | 0.485 | 0.0% (0/6) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 83ms | 🔴 compile |
| revng | gcc -O0 | 0.150 | 0.038 | 0.0% (0/6) | #3 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 9846ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.407 | 0.0% (0/6) | #3 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 485ms | 🔴 compile |
| snowman | gcc -O0 | 0.141 | 0.010 | 0.0% (0/6) | #7 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 557ms | 🔴 compile |
| boomerang | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 10ms | ❌ Function at address 0x14000155 |

### `classify_range`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.860 | 0.182 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.00<br>type 0.50<br>expr 0.79<br>cf 1.00<br>art 0 | 425ms | ✅ |
| ghidra | gcc -O0 | 0.395 | 0.167 | 20.0% (1/5) | #2 | 0 | 3 | GNR 0.85<br>type 0.50<br>expr 0.80<br>cf 1.00<br>art 7 | 5261ms | 🟠 runtime |
| fission | gcc -O0 | 0.169 | 0.093 | 20.0% (1/5) | #3 | 9 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 3334ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.150 | 0.144 | 0.0% (0/5) | #4 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 83ms | 🔴 compile |
| snowman | gcc -O0 | 0.150 | 0.045 | 0.0% (0/5) | #4 | 7 | 3 | GNR 0.00<br>type 0.50<br>expr 0.84<br>cf 0.42<br>art 0 | 557ms | 🔴 compile |
| reko | gcc -O0 | 0.148 | 0.082 | 0.0% (0/5) | #6 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 485ms | 🔴 compile |
| revng | gcc -O0 | 0.144 | 0.042 | 0.0% (0/5) | #7 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 9846ms | 🔴 compile |
| boomerang | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 10ms | ❌ Function at address 0x14000160 |

### `count_bits`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.903 | 0.609 | 100.0% (6/6) | #1 | 0 | 2 | GNR 0.33<br>type 0.50<br>expr 0.86<br>cf 1.00<br>art 0 | 425ms | ✅ |
| fission | gcc -O0 | 0.395 | 0.135 | 33.3% (2/6) ⚠️intrin | #2 | 2 | 2 | GNR 0.31<br>type 0.50<br>expr 0.62<br>cf 0.33<br>art 6 | 3334ms | 🟠 runtime |
| ghidra | gcc -O0 | 0.150 | 0.688 | 0.0% (0/6) | #3 | 0 | 2 | GNR 0.14<br>type 0.50<br>expr 0.85<br>cf 1.00<br>art 2 | 5261ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.150 | 0.638 | 0.0% (0/6) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 83ms | 🔴 compile |
| snowman | gcc -O0 | 0.150 | 0.556 | 0.0% (0/6) | #3 | 0 | 2 | GNR 0.79<br>type 0.50<br>expr 0.78<br>cf 1.00<br>art 0 | 557ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.408 | 0.0% (0/6) | #3 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 485ms | 🔴 compile |
| boomerang | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 10ms | ❌ Function at address 0x14000153 |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 9846ms | ❌ Decompiler output does not mat |

### `crc32`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.747 | 0.127 | 83.3% (5/6) | #1 | 0 | 3 | GNR 0.48<br>type 0.50<br>expr 0.68<br>cf 1.00<br>art 0 | 927ms | 🟠 runtime |
| ghidra | gcc -O0 | 0.150 | 0.343 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 4 | 9429ms | 🔴 compile |
| radare2 | gcc -O0 | 0.150 | 0.299 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 170ms | 🔴 compile |
| snowman | gcc -O0 | 0.150 | 0.082 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 634ms | 🔴 compile |
| revng | gcc -O0 | 0.150 | 0.068 | 0.0% (0/6) | #2 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 16132ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.102 | 0.0% (0/6) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 933ms | 🔴 compile |
| fission | gcc -O0 | 0.080 | 0.059 | 0.0% (0/6) | #7 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 26659ms | 🔴 compile |
| boomerang | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 21ms | ❌ Function at address 0x14000174 |

### `rc4_crypt`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.436 | 0.092 | 25.0% (1/4) | #1 | 0 | 2 | GNR 0.53<br>type 0.50<br>expr 0.52<br>cf 1.00<br>art 0 | 927ms | 🟠 runtime |
| ghidra | gcc -O0 | 0.284 | 0.292 | 25.0% (1/4) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 17 | 9429ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.150 | 0.424 | 0.0% (0/4) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 170ms | 🔴 compile |
| snowman | gcc -O0 | 0.150 | 0.020 | 0.0% (0/4) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 634ms | 🔴 compile |
| revng | gcc -O0 | 0.150 | 0.061 | 0.0% (0/4) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 16132ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.118 | 0.0% (0/4) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 933ms | 🔴 compile |
| fission | gcc -O0 | 0.073 | 0.009 | 0.0% (0/4) ⚠️intrin | #7 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 58 | 26659ms | 🔴 compile |
| boomerang | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 21ms | ❌ Function at address 0x14000162 |

### `rc4_init` ⚪ Universally hard
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O0 | 0.150 | 0.362 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 14 | 9429ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.150 | 0.501 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 170ms | 🔴 compile |
| angr | gcc -O0 | 0.150 | 0.136 | 0.0% (0/5) | #1 | 0 | 2 | GNR 0.39<br>type 0.50<br>expr 0.62<br>cf 1.00<br>art 0 | 927ms | 🟠 runtime |
| snowman | gcc -O0 | 0.150 | 0.026 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 634ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.129 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 933ms | 🔴 compile |
| revng | gcc -O0 | 0.132 | 0.016 | 0.0% (0/5) | #6 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 16132ms | 🔴 compile |
| fission | gcc -O0 | 0.047 | 0.031 | 0.0% (0/5) ⚠️intrin | #7 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 34 | 26659ms | 🔴 compile |
| boomerang | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 21ms | ❌ Function at address 0x14000153 |

### `saturating_add`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.933 | 0.769 | 100.0% (5/5) | #1 | 0 | 1 | GNR 0.36<br>type 0.50<br>expr 0.82<br>cf 1.00<br>art 0 | 425ms | ✅ |
| fission | gcc -O0 | 0.364 | 0.063 | 60.0% (3/5) ⚠️intrin | #2 | 3 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 8 | 3334ms | 🟠 runtime |
| ghidra | gcc -O0 | 0.150 | 0.252 | 0.0% (0/5) | #3 | 0 | 3 | GNR 0.84<br>type 0.50<br>expr 0.76<br>cf 1.00<br>art 8 | 5261ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.150 | 0.227 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 83ms | 🔴 compile |
| snowman | gcc -O0 | 0.150 | 0.035 | 0.0% (0/5) | #3 | 0 | 3 | GNR 0.00<br>type 0.50<br>expr 0.84<br>cf 1.00<br>art 0 | 557ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.187 | 0.0% (0/5) | #3 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 485ms | 🔴 compile |
| revng | gcc -O0 | 0.149 | 0.086 | 0.0% (0/5) | #7 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 9846ms | 🔴 compile |
| boomerang | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 10ms | ❌ Function at address 0x14000166 |

### `signum`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.913 | 0.503 | 100.0% (5/5) | #1 | 0 | 1 | GNR 0.00<br>type 0.50<br>expr 0.83<br>cf 1.00<br>art 0 | 425ms | ✅ |
| ghidra | gcc -O0 | 0.535 | 0.375 | 40.0% (2/5) | #2 | 0 | 3 | GNR 0.80<br>type 0.50<br>expr 0.85<br>cf 1.00<br>art 3 | 5261ms | 🟠 runtime |
| fission | gcc -O0 | 0.409 | 0.057 | 20.0% (1/5) | #3 | 0 | 3 | GNR 0.47<br>type 0.50<br>expr 0.82<br>cf 1.00<br>art 0 | 3334ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.150 | 0.541 | 0.0% (0/5) | #4 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 83ms | 🔴 compile |
| snowman | gcc -O0 | 0.150 | 0.291 | 0.0% (0/5) | #4 | 0 | 3 | GNR 0.00<br>type 0.50<br>expr 0.89<br>cf 1.00<br>art 0 | 557ms | 🔴 compile |
| revng | gcc -O0 | 0.150 | 0.059 | 0.0% (0/5) | #4 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 9846ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.423 | 0.0% (0/5) | #4 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 485ms | 🔴 compile |
| boomerang | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 10ms | ❌ Function at address 0x14000158 |

### `sum_array`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.883 | 0.455 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.29<br>type 0.50<br>expr 0.76<br>cf 1.00<br>art 0 | 1837ms | ✅ |
| fission | gcc -O0 | 0.317 | 0.145 | 40.0% (2/5) | #2 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10266ms | 🟠 runtime |
| ghidra | gcc -O0 | 0.315 | 0.648 | 20.0% (1/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 4 | 30459ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.150 | 0.286 | 0.0% (0/5) | #4 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 543ms | 🔴 compile |
| snowman | gcc -O0 | 0.150 | 0.399 | 0.0% (0/5) | #4 | 0 | 2 | GNR 0.76<br>type 0.50<br>expr 0.77<br>cf 1.00<br>art 0 | 801ms | 🔴 compile |
| revng | gcc -O0 | 0.150 | 0.065 | 0.0% (0/5) | #4 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 34668ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.224 | 0.0% (0/5) | #4 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 2496ms | 🔴 compile |
| boomerang | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 105ms | ❌ Function at address 0x14000153 |

---

## Overfitting Analysis

Functions where **all** decompilers scored below 0.3 are marked as objectively hard.
Functions where **only Fission** scored below 0.3 are marked as quality gaps.

**Objectively hard functions (1):** `rc4_init`
**Fission quality gaps (4):** `checksum`, `classify_range`, `rc4_crypt`, `crc32`