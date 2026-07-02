# Fission Benchmark Report

**Generated:** 2026-07-02 05:49 UTC
**Corpus:** `dev`
**Functions evaluated:** 10

---

## Summary — Correctness-Oriented Composite

> Readability metrics are recorded as unvalidated raw proxies. They are not combined into a final readability score until the human validation study is complete.

| Decompiler | Composite ⭐ | Similarity | Semantic Pass | Functions |
| ---|---|---|---|--- |
| **fission** | 0.254 | 0.111 | 24.0% | 10 |
| **ghidra** | 0.232 | 0.422 | 10.0% | 10 |
| **radare2** | 0.144 | 0.400 | 0.0% | 10 |
| **reko** | 0.133 | 0.225 | 0.0% | 10 |
| **angr** | 0.120 | 0.100 | 0.0% | 10 |
| **revng** | 0.101 | 0.062 | 0.0% | 10 |
| **boomerang** | 0.076 | 0.037 | 0.0% | 10 |
| **snowman** | 0.000 | 0.001 | 0.0% | 10 |

---

## Per-Function Results

### `checksum` ⚪ Universally hard
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O0 | 0.374 | 0.668 | 20.0% (1/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 4 | 5735ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.150 | 0.454 | 0.0% (0/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 105ms | 🔴 compile |
| reko | gcc -O0 | 0.135 | 0.176 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 404ms | 🔴 compile |
| angr | gcc -O0 | 0.117 | 0.087 | 0.0% (0/5) | #4 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 202ms | 🔴 compile |
| revng | gcc -O0 | 0.099 | 0.044 | 0.0% (0/5) | #5 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 7339ms | 🔴 compile |
| fission | gcc -O0 | 0.093 | 0.103 | 0.0% (0/5) | #6 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 4341ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.026 | 0.0% (0/5) | #7 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 36ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #8 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 621ms | 🔴 compile |

### `clamp` 🟢 Fission leads
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.650 | 0.414 | 66.7% (4/6) | #1 | 0 | 1 | GNR 0.87<br>type 0.50<br>expr 0.80<br>cf 1.00<br>art 0 | 4341ms | 🟠 runtime |
| ghidra | gcc -O0 | 0.150 | 0.421 | 0.0% (0/6) | #2 | 0 | 2 | GNR 0.75<br>type 0.50<br>expr 0.77<br>cf 1.00<br>art 9 | 5735ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.150 | 0.485 | 0.0% (0/6) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 105ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.407 | 0.0% (0/6) | #4 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 404ms | 🔴 compile |
| angr | gcc -O0 | 0.118 | 0.091 | 0.0% (0/6) | #5 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 202ms | 🔴 compile |
| revng | gcc -O0 | 0.107 | 0.038 | 0.0% (0/6) | #6 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 7339ms | 🔴 compile |
| boomerang | gcc -O0 | 0.069 | 0.035 | 0.0% (0/6) | #7 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 36ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #8 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 621ms | 🔴 compile |

### `classify_range` ⚪ Universally hard
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O0 | 0.263 | 0.167 | 20.0% (1/5) | #1 | 0 | 3 | GNR 0.85<br>type 0.50<br>expr 0.80<br>cf 1.00<br>art 7 | 5735ms | 🟠 runtime |
| fission | gcc -O0 | 0.189 | 0.093 | 20.0% (1/5) | #2 | 9 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 4341ms | 🟠 runtime |
| angr | gcc -O0 | 0.126 | 0.131 | 0.0% (0/5) | #3 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 202ms | 🔴 compile |
| radare2 | gcc -O0 | 0.119 | 0.144 | 0.0% (0/5) | #4 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 105ms | 🔴 compile |
| reko | gcc -O0 | 0.097 | 0.082 | 0.0% (0/5) | #5 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 404ms | 🔴 compile |
| revng | gcc -O0 | 0.088 | 0.042 | 0.0% (0/5) | #6 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 7339ms | 🔴 compile |
| boomerang | gcc -O0 | 0.079 | 0.033 | 0.0% (0/5) | #7 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 36ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #8 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 621ms | 🔴 compile |

### `count_bits` 🟢 Fission leads
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.332 | 0.135 | 33.3% (2/6) | #1 | 2 | 2 | GNR 0.31<br>type 0.50<br>expr 0.62<br>cf 0.33<br>art 6 | 4341ms | 🟠 runtime |
| ghidra | gcc -O0 | 0.150 | 0.688 | 0.0% (0/6) | #2 | 0 | 2 | GNR 0.14<br>type 0.50<br>expr 0.85<br>cf 1.00<br>art 2 | 5735ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.150 | 0.638 | 0.0% (0/6) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 105ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.408 | 0.0% (0/6) | #4 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 404ms | 🔴 compile |
| angr | gcc -O0 | 0.129 | 0.144 | 0.0% (0/6) | #5 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 202ms | 🔴 compile |
| revng | gcc -O0 | 0.128 | 0.141 | 0.0% (0/6) | #6 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 7339ms | 🔴 compile |
| boomerang | gcc -O0 | 0.089 | 0.088 | 0.0% (0/6) | #7 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 36ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/6) | #8 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 621ms | 🔴 compile |

### `crc32` ⚪ Universally hard
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O0 | 0.150 | 0.343 | 0.0% | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 4 | 9867ms | ⚪ no_test |
| radare2 | gcc -O0 | 0.150 | 0.299 | 0.0% | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 153ms | ⚪ no_test |
| reko | gcc -O0 | 0.120 | 0.102 | 0.0% | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 976ms | ⚪ no_test |
| angr | gcc -O0 | 0.115 | 0.075 | 0.0% | #4 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 373ms | ⚪ no_test |
| revng | gcc -O0 | 0.104 | 0.068 | 0.0% | #5 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 17793ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.076 | 0.022 | 0.0% | #6 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 54ms | ⚪ no_test |
| fission | gcc -O0 | 0.056 | 0.058 | 0.0% | #7 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 20416ms | ⚪ no_test |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #8 | 221 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 676ms | ⚪ no_test |

### `rc4_crypt` ⚪ Universally hard
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O0 | 0.150 | 0.292 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 17 | 9867ms | ⚪ no_test |
| radare2 | gcc -O0 | 0.150 | 0.424 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 153ms | ⚪ no_test |
| reko | gcc -O0 | 0.124 | 0.118 | 0.0% | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 976ms | ⚪ no_test |
| angr | gcc -O0 | 0.113 | 0.067 | 0.0% | #4 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 373ms | ⚪ no_test |
| revng | gcc -O0 | 0.102 | 0.061 | 0.0% | #5 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 17793ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.079 | 0.034 | 0.0% | #6 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 54ms | ⚪ no_test |
| fission | gcc -O0 | 0.074 | 0.009 | 0.0% | #7 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 58 | 20416ms | ⚪ no_test |
| snowman | gcc -O0 | 0.000 | 0.002 | 0.0% | #8 | 221 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 676ms | ⚪ no_test |

### `rc4_init` ⚪ Universally hard
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O0 | 0.150 | 0.362 | 0.0% | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 14 | 9867ms | ⚪ no_test |
| radare2 | gcc -O0 | 0.150 | 0.501 | 0.0% | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 153ms | ⚪ no_test |
| reko | gcc -O0 | 0.126 | 0.129 | 0.0% | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 976ms | ⚪ no_test |
| angr | gcc -O0 | 0.114 | 0.068 | 0.0% | #4 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 373ms | ⚪ no_test |
| boomerang | gcc -O0 | 0.080 | 0.040 | 0.0% | #5 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 54ms | ⚪ no_test |
| revng | gcc -O0 | 0.073 | 0.016 | 0.0% | #6 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 17793ms | ⚪ no_test |
| fission | gcc -O0 | 0.050 | 0.030 | 0.0% | #7 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 34 | 20416ms | ⚪ no_test |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% | #8 | 221 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 676ms | ⚪ no_test |

### `saturating_add` 🟢 Fission leads
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.481 | 0.063 | 60.0% (3/5) | #1 | 3 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 8 | 4341ms | 🟠 runtime |
| reko | gcc -O0 | 0.137 | 0.187 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 404ms | 🔴 compile |
| ghidra | gcc -O0 | 0.131 | 0.252 | 0.0% (0/5) | #3 | 0 | 3 | GNR 0.84<br>type 0.50<br>expr 0.76<br>cf 1.00<br>art 8 | 5735ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.126 | 0.227 | 0.0% (0/5) | #4 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 105ms | 🔴 compile |
| angr | gcc -O0 | 0.117 | 0.085 | 0.0% (0/5) | #5 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 202ms | 🔴 compile |
| revng | gcc -O0 | 0.097 | 0.086 | 0.0% (0/5) | #6 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 7339ms | 🔴 compile |
| boomerang | gcc -O0 | 0.067 | 0.026 | 0.0% (0/5) | #7 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 36ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #8 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 621ms | 🔴 compile |

### `signum`
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O0 | 0.435 | 0.375 | 40.0% (2/5) | #1 | 0 | 3 | GNR 0.80<br>type 0.50<br>expr 0.85<br>cf 1.00<br>art 3 | 5735ms | 🟠 runtime |
| fission | gcc -O0 | 0.231 | 0.057 | 20.0% (1/5) | #2 | 0 | 3 | GNR 0.47<br>type 0.50<br>expr 0.82<br>cf 1.00<br>art 0 | 4341ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.150 | 0.541 | 0.0% (0/5) | #3 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 105ms | 🔴 compile |
| reko | gcc -O0 | 0.150 | 0.423 | 0.0% (0/5) | #4 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 404ms | 🔴 compile |
| angr | gcc -O0 | 0.126 | 0.127 | 0.0% (0/5) | #5 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 202ms | 🔴 compile |
| revng | gcc -O0 | 0.112 | 0.059 | 0.0% (0/5) | #6 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 7339ms | 🔴 compile |
| boomerang | gcc -O0 | 0.069 | 0.037 | 0.0% (0/5) | #7 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 36ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #8 | 227 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 621ms | 🔴 compile |

### `sum_array` 🟢 Fission leads
| Decompiler | Variant | Composite ⭐ | Similarity | Semantic | Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 0.381 | 0.145 | 40.0% (2/5) | #1 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 6217ms | 🟠 runtime |
| ghidra | gcc -O0 | 0.370 | 0.648 | 20.0% (1/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 4 | 33984ms | 🟠 runtime |
| radare2 | gcc -O0 | 0.150 | 0.286 | 0.0% (0/5) | #3 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 663ms | 🔴 compile |
| reko | gcc -O0 | 0.145 | 0.224 | 0.0% (0/5) | #4 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 2653ms | 🔴 compile |
| angr | gcc -O0 | 0.124 | 0.120 | 0.0% (0/5) | #5 | 0 | 0 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 1717ms | 🔴 compile |
| revng | gcc -O0 | 0.103 | 0.065 | 0.0% (0/5) | #6 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 37943ms | 🔴 compile |
| boomerang | gcc -O0 | 0.077 | 0.028 | 0.0% (0/5) | #7 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 101ms | 🔴 compile |
| snowman | gcc -O0 | 0.000 | 0.001 | 0.0% (0/5) | #8 | 222 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 628ms | 🔴 compile |

---

## Overfitting Analysis

Functions where **all** decompilers scored below 0.3 are marked as objectively hard.
Functions where **only Fission** scored below 0.3 are marked as quality gaps.

**Objectively hard functions (3):** `rc4_init`, `rc4_crypt`, `crc32`
**Fission quality gaps (2):** `checksum`, `classify_range`