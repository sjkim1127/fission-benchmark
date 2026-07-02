# Fission Benchmark Report

**Generated:** 2026-07-02 14:50 UTC
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
| **boomerang** | 0.150 | 0.192 | 0.0% | 9 |
| **radare2** | 0.150 | 0.400 | 0.0% | 10 |
| **reko** | 0.150 | 0.225 | 0.0% | 10 |
| **snowman** | 0.149 | 0.159 | 0.0% | 10 |
| **revng** | 0.147 | 0.053 | 0.0% | 9 |

---

## Per-Function Results

### `checksum`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.890 | 0.567 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.33<br>type 0.50<br>expr 0.71<br>cf 1.00<br>art 0 | 391ms | ✅ |
| ghidra | gcc -O0 | 0.317 | 0.668 | 20.0% (1/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 4 | 4608ms | 🟠 runtime |
| boomerang | gcc -O0 | 0.150 | 0.186 | 0.0% (0/5) | #3 | 0 | 1 | GNR 0.00<br>type 0.50<br>expr 1.00<br>cf 1.00<br>art 0 | 17ms | 🔴 compile |
| radare2 | gcc -O0 | 0.150 | 0.454 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 91ms | 🔴 compile |
| snowman | gcc -O0 | 0.150 | 0.129 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 534ms | 🔴 compile |
| revng | gcc -O0 | 0.150 | 0.044 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 11899ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.176 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 447ms | 🔴 compile |
| fission | gcc -O0 | 0.112 | 0.103 | 0.0% (0/5) | #8 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 3109ms | 🔴 compile |

### `clamp`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.929 | 0.708 | 100.0% (6/6) | #1 | 0 | 2 | GNR 0.00<br>type 0.50<br>expr 0.93<br>cf 1.00<br>art 0 | 391ms | ✅ |
| fission | gcc -O0 | 0.662 | 0.179 | 66.7% (4/6) | #2 | 0 | 2 | GNR 0.88<br>type 0.50<br>expr 0.81<br>cf 1.00<br>art 0 | 3109ms | 🟠 runtime |
| ghidra | gcc -O0 | 0.150 | 0.421 | 0.0% (0/6) | #3 | 0 | 2 | GNR 0.75<br>type 0.50<br>expr 0.77<br>cf 1.00<br>art 9 | 4608ms | 🟠 runtime |
| boomerang | gcc -O0 | 0.150 | 0.239 | 0.0% (0/6) | #3 | 0 | 1 | GNR 0.00<br>type 0.50<br>expr 1.00<br>cf 1.00<br>art 0 | 17ms | 🔴 compile |
| radare2 | gcc -O0 | 0.150 | 0.485 | 0.0% (0/6) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 91ms | 🔴 compile |
| revng | gcc -O0 | 0.150 | 0.038 | 0.0% (0/6) | #3 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 11899ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.407 | 0.0% (0/6) | #3 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 447ms | 🔴 compile |
| snowman | gcc -O0 | 0.141 | 0.010 | 0.0% (0/6) | #8 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 534ms | 🔴 compile |

### `classify_range`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.860 | 0.182 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.00<br>type 0.50<br>expr 0.79<br>cf 1.00<br>art 0 | 391ms | ✅ |
| ghidra | gcc -O0 | 0.395 | 0.167 | 20.0% (1/5) | #2 | 0 | 3 | GNR 0.85<br>type 0.50<br>expr 0.80<br>cf 1.00<br>art 7 | 4608ms | 🟠 runtime |
| fission | gcc -O0 | 0.169 | 0.093 | 20.0% (1/5) | #3 | 9 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 3109ms | 🟠 runtime |
| boomerang | gcc -O0 | 0.150 | 0.186 | 0.0% (0/5) | #4 | 0 | 1 | GNR 0.00<br>type 0.50<br>expr 1.00<br>cf 1.00<br>art 0 | 17ms | 🔴 compile |
| radare2 | gcc -O0 | 0.150 | 0.144 | 0.0% (0/5) | #4 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 91ms | 🔴 compile |
| snowman | gcc -O0 | 0.150 | 0.045 | 0.0% (0/5) | #4 | 7 | 3 | GNR 0.00<br>type 0.50<br>expr 0.84<br>cf 0.42<br>art 0 | 534ms | 🔴 compile |
| reko | gcc -O0 | 0.148 | 0.082 | 0.0% (0/5) | #7 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 447ms | 🔴 compile |
| revng | gcc -O0 | 0.144 | 0.042 | 0.0% (0/5) | #8 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 11899ms | 🔴 compile |

### `count_bits`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.903 | 0.609 | 100.0% (6/6) | #1 | 0 | 2 | GNR 0.33<br>type 0.50<br>expr 0.86<br>cf 1.00<br>art 0 | 391ms | ✅ |
| fission | gcc -O0 | 0.395 | 0.135 | 33.3% (2/6) ⚠️intrin | #2 | 2 | 2 | GNR 0.31<br>type 0.50<br>expr 0.62<br>cf 0.33<br>art 6 | 3109ms | 🟠 runtime |
| ghidra | gcc -O0 | 0.150 | 0.688 | 0.0% (0/6) | #3 | 0 | 2 | GNR 0.14<br>type 0.50<br>expr 0.85<br>cf 1.00<br>art 2 | 4608ms | 🟠 runtime |
| boomerang | gcc -O0 | 0.150 | 0.279 | 0.0% (0/6) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 17ms | 🔴 compile |
| radare2 | gcc -O0 | 0.150 | 0.638 | 0.0% (0/6) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 91ms | 🔴 compile |
| snowman | gcc -O0 | 0.150 | 0.556 | 0.0% (0/6) | #3 | 0 | 2 | GNR 0.79<br>type 0.50<br>expr 0.78<br>cf 1.00<br>art 0 | 534ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.408 | 0.0% (0/6) | #3 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 447ms | 🔴 compile |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 11899ms | ❌ Decompiler output does not mat |

### `crc32`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.747 | 0.127 | 83.3% (5/6) | #1 | 0 | 3 | GNR 0.48<br>type 0.50<br>expr 0.68<br>cf 1.00<br>art 0 | 935ms | 🟠 runtime |
| ghidra | gcc -O0 | 0.150 | 0.343 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 4 | 10166ms | 🔴 compile |
| boomerang | gcc -O0 | 0.150 | 0.105 | 0.0% (0/6) | #2 | 0 | 1 | GNR 0.00<br>type 0.50<br>expr 1.00<br>cf 1.00<br>art 0 | 202ms | 🔴 compile |
| radare2 | gcc -O0 | 0.150 | 0.299 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 219ms | 🔴 compile |
| snowman | gcc -O0 | 0.150 | 0.082 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 610ms | 🔴 compile |
| revng | gcc -O0 | 0.150 | 0.068 | 0.0% (0/6) | #2 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 18520ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.102 | 0.0% (0/6) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 866ms | 🔴 compile |
| fission | gcc -O0 | 0.080 | 0.058 | 0.0% (0/6) | #8 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 26017ms | 🔴 compile |

### `rc4_crypt`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.436 | 0.092 | 25.0% (1/4) | #1 | 0 | 2 | GNR 0.53<br>type 0.50<br>expr 0.52<br>cf 1.00<br>art 0 | 935ms | 🟠 runtime |
| ghidra | gcc -O0 | 0.284 | 0.292 | 25.0% (1/4) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 17 | 10166ms | 🟠 runtime |
| boomerang | gcc -O0 | 0.150 | 0.144 | 0.0% (0/4) | #3 | 0 | 1 | GNR 0.00<br>type 0.50<br>expr 1.00<br>cf 1.00<br>art 0 | 202ms | 🔴 compile |
| radare2 | gcc -O0 | 0.150 | 0.424 | 0.0% (0/4) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 219ms | 🔴 compile |
| snowman | gcc -O0 | 0.150 | 0.020 | 0.0% (0/4) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 610ms | 🔴 compile |
| revng | gcc -O0 | 0.150 | 0.061 | 0.0% (0/4) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 18520ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.118 | 0.0% (0/4) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 866ms | 🔴 compile |
| fission | gcc -O0 | 0.073 | 0.009 | 0.0% (0/4) ⚠️intrin | #8 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 58 | 26017ms | 🔴 compile |

### `rc4_init` ⚪ Universally hard
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O0 | 0.150 | 0.362 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 14 | 10166ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.150 | 0.501 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 219ms | 🔴 compile |
| angr | gcc -O0 | 0.150 | 0.136 | 0.0% (0/5) | #1 | 0 | 2 | GNR 0.39<br>type 0.50<br>expr 0.62<br>cf 1.00<br>art 0 | 935ms | 🟠 runtime |
| snowman | gcc -O0 | 0.150 | 0.026 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 610ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.129 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 866ms | 🔴 compile |
| revng | gcc -O0 | 0.132 | 0.016 | 0.0% (0/5) | #6 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 18520ms | 🔴 compile |
| fission | gcc -O0 | 0.047 | 0.031 | 0.0% (0/5) ⚠️intrin | #7 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 34 | 26017ms | 🔴 compile |
| boomerang | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 202ms | ❌ Decompilation failed: Level |  |

### `saturating_add`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.933 | 0.769 | 100.0% (5/5) | #1 | 0 | 1 | GNR 0.36<br>type 0.50<br>expr 0.82<br>cf 1.00<br>art 0 | 391ms | ✅ |
| fission | gcc -O0 | 0.364 | 0.063 | 60.0% (3/5) ⚠️intrin | #2 | 3 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 8 | 3109ms | 🟠 runtime |
| ghidra | gcc -O0 | 0.150 | 0.252 | 0.0% (0/5) | #3 | 0 | 3 | GNR 0.84<br>type 0.50<br>expr 0.76<br>cf 1.00<br>art 8 | 4608ms | 🟠 runtime |
| boomerang | gcc -O0 | 0.150 | 0.182 | 0.0% (0/5) | #3 | 0 | 1 | GNR 0.00<br>type 0.50<br>expr 1.00<br>cf 1.00<br>art 0 | 17ms | 🔴 compile |
| radare2 | gcc -O0 | 0.150 | 0.227 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 91ms | 🔴 compile |
| snowman | gcc -O0 | 0.150 | 0.035 | 0.0% (0/5) | #3 | 0 | 3 | GNR 0.00<br>type 0.50<br>expr 0.84<br>cf 1.00<br>art 0 | 534ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.187 | 0.0% (0/5) | #3 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 447ms | 🔴 compile |
| revng | gcc -O0 | 0.149 | 0.086 | 0.0% (0/5) | #8 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 11899ms | 🔴 compile |

### `signum`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.913 | 0.503 | 100.0% (5/5) | #1 | 0 | 1 | GNR 0.00<br>type 0.50<br>expr 0.83<br>cf 1.00<br>art 0 | 391ms | ✅ |
| ghidra | gcc -O0 | 0.535 | 0.375 | 40.0% (2/5) | #2 | 0 | 3 | GNR 0.80<br>type 0.50<br>expr 0.85<br>cf 1.00<br>art 3 | 4608ms | 🟠 runtime |
| fission | gcc -O0 | 0.409 | 0.057 | 20.0% (1/5) | #3 | 0 | 3 | GNR 0.47<br>type 0.50<br>expr 0.82<br>cf 1.00<br>art 0 | 3109ms | 🟠 runtime |
| boomerang | gcc -O0 | 0.150 | 0.267 | 0.0% (0/5) | #4 | 0 | 1 | GNR 0.00<br>type 0.50<br>expr 1.00<br>cf 1.00<br>art 0 | 17ms | 🔴 compile |
| radare2 | gcc -O0 | 0.150 | 0.541 | 0.0% (0/5) | #4 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 91ms | 🔴 compile |
| snowman | gcc -O0 | 0.150 | 0.291 | 0.0% (0/5) | #4 | 0 | 3 | GNR 0.00<br>type 0.50<br>expr 0.89<br>cf 1.00<br>art 0 | 534ms | 🔴 compile |
| revng | gcc -O0 | 0.150 | 0.059 | 0.0% (0/5) | #4 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 11899ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.423 | 0.0% (0/5) | #4 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 447ms | 🔴 compile |

### `sum_array`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.883 | 0.455 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.29<br>type 0.50<br>expr 0.76<br>cf 1.00<br>art 0 | 1354ms | ✅ |
| fission | gcc -O0 | 0.317 | 0.145 | 40.0% (2/5) | #2 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 7807ms | 🟠 runtime |
| ghidra | gcc -O0 | 0.315 | 0.648 | 20.0% (1/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 4 | 29739ms | 🟠 runtime |
| boomerang | gcc -O0 | 0.150 | 0.138 | 0.0% (0/5) | #4 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 122ms | 🔴 compile |
| radare2 | gcc -O0 | 0.150 | 0.286 | 0.0% (0/5) | #4 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 555ms | 🔴 compile |
| snowman | gcc -O0 | 0.150 | 0.399 | 0.0% (0/5) | #4 | 0 | 2 | GNR 0.76<br>type 0.50<br>expr 0.77<br>cf 1.00<br>art 0 | 663ms | 🔴 compile |
| revng | gcc -O0 | 0.150 | 0.065 | 0.0% (0/5) | #4 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 31242ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.224 | 0.0% (0/5) | #4 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 2709ms | 🔴 compile |

---

## Overfitting Analysis

Functions where **all** decompilers scored below 0.3 are marked as objectively hard.
Functions where **only Fission** scored below 0.3 are marked as quality gaps.

**Objectively hard functions (1):** `rc4_init`
**Fission quality gaps (4):** `checksum`, `classify_range`, `rc4_crypt`, `crc32`