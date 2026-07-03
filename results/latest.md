# Fission Benchmark Report

**Generated:** 2026-07-03 06:37 UTC
**Corpus:** `dev`
**Functions evaluated:** 10

---

## Summary — Correctness Score

> Readability metrics are recorded as unvalidated raw proxies. They are not combined into a final readability score until the human validation study is complete.

| Decompiler | Correctness | Similarity | Semantic Pass | Functions |
| ---|---|---|---|--- |
| **angr** | 0.787 | 0.415 | 80.8% | 10 |
| **fission** | 0.267 | 0.111 | 24.0% | 10 |
| **ghidra** | 0.234 | 0.422 | 12.5% | 10 |
| **radare2** | 0.133 | 0.400 | 0.0% | 10 |
| **reko** | 0.121 | 0.225 | 0.0% | 10 |
| **boomerang** | 0.119 | 0.192 | 0.0% | 9 |
| **snowman** | 0.101 | 0.159 | 0.0% | 10 |
| **revng** | 0.093 | 0.053 | 0.0% | 9 |

---

## Per-Function Results

### `checksum`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.957 | 0.567 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.33<br>type 0.50<br>expr 0.71<br>cf 1.00<br>art 0 | 435ms | ✅ |
| ghidra | gcc -O0 | 0.327 | 0.668 | 20.0% (1/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 4 | 4457ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.145 | 0.454 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 91ms | 🔴 compile |
| boomerang | gcc -O0 | 0.119 | 0.186 | 0.0% (0/5) | #4 | 0 | 1 | GNR 0.00<br>type 0.50<br>expr 1.00<br>cf 1.00<br>art 0 | 16ms | 🔴 compile |
| reko | gcc -O0 | 0.118 | 0.176 | 0.0% (0/5) | #5 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 464ms | 🔴 compile |
| snowman | gcc -O0 | 0.113 | 0.129 | 0.0% (0/5) | #6 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 587ms | 🔴 compile |
| revng | gcc -O0 | 0.094 | 0.044 | 0.0% (0/5) | #7 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 12175ms | 🔴 compile |
| fission | gcc -O0 | 0.082 | 0.103 | 0.0% (0/5) | #8 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 3339ms | 🔴 compile |

### `clamp`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.961 | 0.708 | 100.0% (6/6) | #1 | 0 | 2 | GNR 0.00<br>type 0.50<br>expr 0.93<br>cf 1.00<br>art 0 | 435ms | ✅ |
| fission | gcc -O0 | 0.675 | 0.414 | 66.7% (4/6) | #2 | 0 | 1 | GNR 0.87<br>type 0.50<br>expr 0.80<br>cf 1.00<br>art 0 | 3339ms | 🟠 runtime |
| reko | gcc -O0 | 0.141 | 0.407 | 0.0% (0/6) | #3 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 464ms | 🔴 compile |
| radare2 | gcc -O0 | 0.139 | 0.485 | 0.0% (0/6) | #4 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 91ms | 🔴 compile |
| ghidra | gcc -O0 | 0.132 | 0.421 | 0.0% (0/6) | #5 | 0 | 2 | GNR 0.75<br>type 0.50<br>expr 0.77<br>cf 1.00<br>art 9 | 4457ms | 🟠 runtime |
| boomerang | gcc -O0 | 0.124 | 0.239 | 0.0% (0/6) | #6 | 0 | 1 | GNR 0.00<br>type 0.50<br>expr 1.00<br>cf 1.00<br>art 0 | 16ms | 🔴 compile |
| revng | gcc -O0 | 0.104 | 0.038 | 0.0% (0/6) | #7 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 12175ms | 🔴 compile |
| snowman | gcc -O0 | 0.081 | 0.010 | 0.0% (0/6) | #8 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 587ms | 🔴 compile |

### `classify_range`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.918 | 0.182 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.00<br>type 0.50<br>expr 0.79<br>cf 1.00<br>art 0 | 435ms | ✅ |
| ghidra | gcc -O0 | 0.267 | 0.167 | 20.0% (1/5) | #2 | 0 | 3 | GNR 0.85<br>type 0.50<br>expr 0.80<br>cf 1.00<br>art 7 | 4457ms | 🟠 runtime |
| fission | gcc -O0 | 0.199 | 0.093 | 20.0% (1/5) | #3 | 9 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 3339ms | 🟠 runtime |
| boomerang | gcc -O0 | 0.119 | 0.186 | 0.0% (0/5) | #4 | 0 | 1 | GNR 0.00<br>type 0.50<br>expr 1.00<br>cf 1.00<br>art 0 | 16ms | 🔴 compile |
| radare2 | gcc -O0 | 0.104 | 0.144 | 0.0% (0/5) | #5 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 91ms | 🔴 compile |
| reko | gcc -O0 | 0.088 | 0.082 | 0.0% (0/5) | #6 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 464ms | 🔴 compile |
| revng | gcc -O0 | 0.084 | 0.042 | 0.0% (0/5) | #7 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 12175ms | 🔴 compile |
| snowman | gcc -O0 | 0.025 | 0.045 | 0.0% (0/5) | #8 | 7 | 3 | GNR 0.00<br>type 0.50<br>expr 0.84<br>cf 0.42<br>art 0 | 587ms | 🔴 compile |

### `count_bits`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.961 | 0.609 | 100.0% (6/6) | #1 | 0 | 2 | GNR 0.33<br>type 0.50<br>expr 0.86<br>cf 1.00<br>art 0 | 435ms | ✅ |
| fission | gcc -O0 | 0.352 | 0.135 | 33.3% (2/6) ⚠️intrin | #2 | 2 | 2 | GNR 0.31<br>type 0.50<br>expr 0.62<br>cf 0.33<br>art 6 | 3339ms | 🟠 runtime |
| ghidra | gcc -O0 | 0.150 | 0.688 | 0.0% (0/6) | #3 | 0 | 2 | GNR 0.14<br>type 0.50<br>expr 0.85<br>cf 1.00<br>art 2 | 4457ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.150 | 0.638 | 0.0% (0/6) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 91ms | 🔴 compile |
| snowman | gcc -O0 | 0.150 | 0.556 | 0.0% (0/6) | #3 | 0 | 2 | GNR 0.79<br>type 0.50<br>expr 0.78<br>cf 1.00<br>art 0 | 587ms | 🔴 compile |
| reko | gcc -O0 | 0.141 | 0.408 | 0.0% (0/6) | #6 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 464ms | 🔴 compile |
| boomerang | gcc -O0 | 0.128 | 0.279 | 0.0% (0/6) | #7 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 16ms | 🔴 compile |
| revng | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 12175ms | ❌ Decompiler output does not mat |

### `crc32`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.779 | 0.127 | 83.3% (5/6) | #1 | 0 | 3 | GNR 0.48<br>type 0.50<br>expr 0.68<br>cf 1.00<br>art 0 | 902ms | 🟠 runtime |
| ghidra | gcc -O0 | 0.134 | 0.343 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 4 | 10928ms | 🔴 compile |
| radare2 | gcc -O0 | 0.130 | 0.299 | 0.0% (0/6) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 242ms | 🔴 compile |
| boomerang | gcc -O0 | 0.111 | 0.105 | 0.0% (0/6) | #4 | 0 | 1 | GNR 0.00<br>type 0.50<br>expr 1.00<br>cf 1.00<br>art 0 | 203ms | 🔴 compile |
| reko | gcc -O0 | 0.110 | 0.102 | 0.0% (0/6) | #5 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 939ms | 🔴 compile |
| snowman | gcc -O0 | 0.108 | 0.082 | 0.0% (0/6) | #6 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 654ms | 🔴 compile |
| revng | gcc -O0 | 0.097 | 0.068 | 0.0% (0/6) | #7 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 19212ms | 🔴 compile |
| fission | gcc -O0 | 0.050 | 0.059 | 0.0% (0/6) | #8 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 28611ms | 🔴 compile |

### `rc4_crypt` ⚪ Universally hard
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O0 | 0.329 | 0.292 | 25.0% (1/4) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 17 | 10928ms | 🟠 runtime |
| angr | gcc -O0 | 0.309 | 0.092 | 25.0% (1/4) | #2 | 0 | 2 | GNR 0.53<br>type 0.50<br>expr 0.52<br>cf 1.00<br>art 0 | 902ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.142 | 0.424 | 0.0% (0/4) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 242ms | 🔴 compile |
| boomerang | gcc -O0 | 0.114 | 0.144 | 0.0% (0/4) | #4 | 0 | 1 | GNR 0.00<br>type 0.50<br>expr 1.00<br>cf 1.00<br>art 0 | 203ms | 🔴 compile |
| reko | gcc -O0 | 0.112 | 0.118 | 0.0% (0/4) | #5 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 939ms | 🔴 compile |
| snowman | gcc -O0 | 0.102 | 0.020 | 0.0% (0/4) | #6 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 654ms | 🔴 compile |
| revng | gcc -O0 | 0.096 | 0.061 | 0.0% (0/4) | #7 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 19212ms | 🔴 compile |
| fission | gcc -O0 | 0.073 | 0.009 | 0.0% (0/4) ⚠️intrin | #8 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 58 | 28611ms | 🔴 compile |

### `rc4_init` ⚪ Universally hard
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| radare2 | gcc -O0 | 0.150 | 0.501 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 242ms | 🔴 compile |
| ghidra | gcc -O0 | 0.136 | 0.362 | 0.0% (0/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 14 | 10928ms | 🟠 runtime |
| angr | gcc -O0 | 0.114 | 0.136 | 0.0% (0/5) | #3 | 0 | 2 | GNR 0.39<br>type 0.50<br>expr 0.62<br>cf 1.00<br>art 0 | 902ms | 🟠 runtime |
| reko | gcc -O0 | 0.113 | 0.129 | 0.0% (0/5) | #4 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 939ms | 🔴 compile |
| snowman | gcc -O0 | 0.103 | 0.026 | 0.0% (0/5) | #5 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 654ms | 🔴 compile |
| revng | gcc -O0 | 0.072 | 0.016 | 0.0% (0/5) | #6 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 19212ms | 🔴 compile |
| fission | gcc -O0 | 0.047 | 0.030 | 0.0% (0/5) ⚠️intrin | #7 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 34 | 28611ms | 🔴 compile |
| boomerang | gcc -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 203ms | ❌ Decompilation failed: Level |  |

### `saturating_add`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.977 | 0.769 | 100.0% (5/5) | #1 | 0 | 1 | GNR 0.36<br>type 0.50<br>expr 0.82<br>cf 1.00<br>art 0 | 435ms | ✅ |
| fission | gcc -O0 | 0.534 | 0.063 | 60.0% (3/5) ⚠️intrin | #2 | 3 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 8 | 3339ms | 🟠 runtime |
| reko | gcc -O0 | 0.119 | 0.187 | 0.0% (0/5) | #3 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 464ms | 🔴 compile |
| boomerang | gcc -O0 | 0.118 | 0.182 | 0.0% (0/5) | #4 | 0 | 1 | GNR 0.00<br>type 0.50<br>expr 1.00<br>cf 1.00<br>art 0 | 16ms | 🔴 compile |
| ghidra | gcc -O0 | 0.105 | 0.252 | 0.0% (0/5) | #5 | 0 | 3 | GNR 0.84<br>type 0.50<br>expr 0.76<br>cf 1.00<br>art 8 | 4457ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.103 | 0.227 | 0.0% (0/5) | #6 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 91ms | 🔴 compile |
| revng | gcc -O0 | 0.089 | 0.086 | 0.0% (0/5) | #7 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 12175ms | 🔴 compile |
| snowman | gcc -O0 | 0.084 | 0.035 | 0.0% (0/5) | #8 | 0 | 3 | GNR 0.00<br>type 0.50<br>expr 0.84<br>cf 1.00<br>art 0 | 587ms | 🔴 compile |

### `signum`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.950 | 0.503 | 100.0% (5/5) | #1 | 0 | 1 | GNR 0.00<br>type 0.50<br>expr 0.83<br>cf 1.00<br>art 0 | 435ms | ✅ |
| ghidra | gcc -O0 | 0.438 | 0.375 | 40.0% (2/5) | #2 | 0 | 3 | GNR 0.80<br>type 0.50<br>expr 0.85<br>cf 1.00<br>art 3 | 4457ms | 🟠 runtime |
| fission | gcc -O0 | 0.246 | 0.057 | 20.0% (1/5) | #3 | 0 | 3 | GNR 0.47<br>type 0.50<br>expr 0.82<br>cf 1.00<br>art 0 | 3339ms | 🟠 runtime |
| reko | gcc -O0 | 0.142 | 0.423 | 0.0% (0/5) | #4 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 464ms | 🔴 compile |
| radare2 | gcc -O0 | 0.134 | 0.541 | 0.0% (0/5) | #5 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 91ms | 🔴 compile |
| boomerang | gcc -O0 | 0.127 | 0.267 | 0.0% (0/5) | #6 | 0 | 1 | GNR 0.00<br>type 0.50<br>expr 1.00<br>cf 1.00<br>art 0 | 16ms | 🔴 compile |
| snowman | gcc -O0 | 0.109 | 0.291 | 0.0% (0/5) | #7 | 0 | 3 | GNR 0.00<br>type 0.50<br>expr 0.89<br>cf 1.00<br>art 0 | 587ms | 🔴 compile |
| revng | gcc -O0 | 0.106 | 0.059 | 0.0% (0/5) | #8 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 12175ms | 🔴 compile |

### `sum_array`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| angr | gcc -O0 | 0.946 | 0.455 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.29<br>type 0.50<br>expr 0.76<br>cf 1.00<br>art 0 | 1494ms | ✅ |
| fission | gcc -O0 | 0.407 | 0.145 | 40.0% (2/5) | #2 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 6482ms | 🟠 runtime |
| ghidra | gcc -O0 | 0.325 | 0.648 | 20.0% (1/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 4 | 29138ms | 🟠 runtime |
| snowman | gcc -O0 | 0.140 | 0.399 | 0.0% (0/5) | #4 | 0 | 2 | GNR 0.76<br>type 0.50<br>expr 0.77<br>cf 1.00<br>art 0 | 715ms | 🔴 compile |
| radare2 | gcc -O0 | 0.129 | 0.286 | 0.0% (0/5) | #5 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 449ms | 🔴 compile |
| reko | gcc -O0 | 0.122 | 0.224 | 0.0% (0/5) | #6 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 2794ms | 🔴 compile |
| boomerang | gcc -O0 | 0.114 | 0.138 | 0.0% (0/5) | #7 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 115ms | 🔴 compile |
| revng | gcc -O0 | 0.097 | 0.065 | 0.0% (0/5) | #8 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 33512ms | 🔴 compile |

---

## Overfitting Analysis

Functions where **all** decompilers scored below 0.3 are marked as objectively hard.
Functions where **only Fission** scored below 0.3 are marked as quality gaps.

**Objectively hard functions (1):** `rc4_init`
**Fission quality gaps (4):** `checksum`, `classify_range`, `rc4_crypt`, `crc32`