<!-- run_id=146888c6-5724-4690-9082-9d9031d4f070 source_envelope_sha256=3140de13ca9b57ffcfb5780bda7b81fed577528dfe19d8e29986502060e848a0 -->
# Fission Benchmark Report

**Measured at:** 2026-07-17T21:03:56.011614Z
**Rendered at:** 2026-07-17 21:08 UTC
**Corpus:** `dev`
**Functions evaluated:** 36

---

## ✅ VALID RUN

> Fission 200/216 (92.6%), all-backend 415/432 (96.1%)

## MVP Summary — Standard set

> **Primary ranking axis:** semantic pass rate (original-binary oracle when available).
> **Also first-class:** coverage (attempted / adapter clean / boundary invalid / tested), fail taxonomy, runtime.
> **Secondary:** CFG match (attached when cfg_parity JSONL present).
> **Diagnostics only (non-ranking):** source similarity, AST similarity, readability proxies.
> Readability proxies are not a final score until the human validation study completes.

| Decompiler | Attempted | Adapter clean | Boundary invalid | Semantic tested | Semantic mean | Perfect | No wrapper | Fail taxonomy (top) | Mean time |
| ---|---|---|---|---|---|---|---|---|--- |
| **fission** | 216 | 200 | 2 | 200 | 58.7% | 94 | 0 | assertion_fail:53 · compile_error:31 · adapter_error:14 | 9848ms |
| **ghidra** | 216 | 215 | 1 | 215 | 77.3% | 164 | 0 | compile_error:22 · runtime_error:14 · assertion_fail:13 | 11137ms |

### Extension — Cross-compiler / opt

| Decompiler | Variant | Compiler | Opt | Tested | Semantic mean |
| ---|---|---|---|---|--- |
| fission | clang -O0 | clang | -O0 | 36 | 50.1% |
| fission | clang -O2 | clang | -O2 | 22 | 32.3% |
| fission | gcc -O0 | gcc | -O0 | 36 | 82.8% |
| fission | gcc -O2 | gcc | -O2 | 36 | 59.0% |
| fission | gcc-m32 -O0 | gcc-m32 | -O0 | 35 | 74.0% |
| fission | gcc-m32 -O2 | gcc-m32 | -O2 | 35 | 43.9% |
| ghidra | clang -O0 | clang | -O0 | 36 | 75.0% |
| ghidra | clang -O2 | clang | -O2 | 36 | 80.6% |
| ghidra | gcc -O0 | gcc | -O0 | 36 | 25.3% |
| ghidra | gcc -O2 | gcc | -O2 | 35 | 94.3% |
| ghidra | gcc-m32 -O0 | gcc-m32 | -O0 | 36 | 94.4% |
| ghidra | gcc-m32 -O2 | gcc-m32 | -O2 | 36 | 94.4% |

### Secondary — CFG match

| Decompiler | Match | Mismatch | Match rate |
| ---|---|---|--- |
| fission | 9 | 111 | 7.5% |

### Diagnostics note

> Source similarity is **not** listed in the MVP table. It remains on per-function rows for triage only.

---

## Per-Function Results

### `accumulate_pairs` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 1.000 | 0.083 | 100.0% (5/5) | #1 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 9561ms | ✅ |
| ghidra | gcc -O0 | 1.000 | 0.517 | 100.0% (5/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 5 | 11208ms | ✅ |
| fission | gcc -O2 | 1.000 | 0.122 | 100.0% (5/5) | #1 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9588ms | ✅ |
| ghidra | gcc -O2 | 1.000 | 0.120 | 100.0% (5/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 10763ms | ✅ |
| fission | gcc-m32 -O0 | 1.000 | 0.114 | 100.0% (5/5) | #1 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 4977ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.787 | 100.0% (5/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 5723ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.120 | 100.0% (5/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 8959ms | ✅ |
| ghidra | clang -O0 | 1.000 | 0.757 | 100.0% (5/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 9867ms | ✅ |
| fission | gcc-m32 -O2 | 0.000 | 0.166 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 8431ms | 🟡 timeout |
| fission | clang -O0 | 0.000 | 0.090 | 0.0% (0/5) | #2 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10111ms | 🔴 compile |
| ghidra | clang -O2 | 0.000 | 0.047 | 0.0% (0/5) | #1 | 2 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 16 | 10063ms | 🔴 compile |
| fission | clang -O2 | n/a | 0.000 | n/a | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: ReadTim |

### `add_ints` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 1.000 | 0.333 | 100.0% (5/5) | #1 | 0 | 1 | GNR 0.80<br>type 0.50<br>expr 0.83<br>cf 1.00<br>art 0 | 6576ms | ✅ |
| fission | gcc -O2 | 1.000 | 0.431 | 100.0% (5/5) | #1 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 6351ms | ✅ |
| ghidra | gcc -O2 | 1.000 | 0.739 | 100.0% (5/5) | #1 | 0 | 1 | GNR 0.80<br>type 0.50<br>expr 0.83<br>cf 1.00<br>art 0 | 6886ms | ✅ |
| fission | gcc-m32 -O0 | 1.000 | 0.604 | 100.0% (5/5) | #1 | 0 | 1 | GNR 0.80<br>type 0.50<br>expr 0.83<br>cf 1.00<br>art 0 | 5447ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.943 | 100.0% (5/5) | #1 | 0 | 1 | GNR 0.00<br>type 0.50<br>expr 0.93<br>cf 1.00<br>art 0 | 6902ms | ✅ |
| fission | gcc-m32 -O2 | 1.000 | 0.604 | 100.0% (5/5) | #1 | 0 | 1 | GNR 0.80<br>type 0.50<br>expr 0.83<br>cf 1.00<br>art 0 | 3392ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.943 | 100.0% (5/5) | #1 | 0 | 1 | GNR 0.00<br>type 0.50<br>expr 0.93<br>cf 1.00<br>art 0 | 7716ms | ✅ |
| ghidra | clang -O0 | 1.000 | 0.761 | 100.0% (5/5) | #1 | 0 | 1 | GNR 0.00<br>type 0.50<br>expr 0.93<br>cf 1.00<br>art 0 | 8724ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.989 | 100.0% (5/5) | #1 | 0 | 1 | GNR 0.00<br>type 0.50<br>expr 0.93<br>cf 1.00<br>art 0 | 7596ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.678 | 0.0% (0/5) | #2 | 0 | 1 | GNR 0.57<br>type 0.50<br>expr 0.86<br>cf 1.00<br>art 4 | 6857ms | 🟤 assert |
| fission | clang -O0 | 0.000 | 0.151 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 7000ms | 🔴 compile |
| fission | clang -O2 | n/a | 0.000 | n/a | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: ReadTim |

### `apply_binop` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 1.000 | 0.108 | 100.0% (6/6) | #1 | 2 | 2 | GNR 0.44<br>type 0.56<br>expr 0.66<br>cf 1.00<br>art 0 | 6576ms | ✅ |
| fission | gcc -O2 | 1.000 | 0.402 | 100.0% (6/6) | #1 | 0 | 2 | GNR 0.88<br>type 0.60<br>expr 0.68<br>cf 1.00<br>art 0 | 6351ms | ✅ |
| fission | gcc-m32 -O0 | 1.000 | 0.109 | 100.0% (6/6) | #1 | 0 | 3 | GNR 0.88<br>type 0.60<br>expr 0.74<br>cf 1.00<br>art 0 | 5447ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.658 | 100.0% (6/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 6902ms | ✅ |
| fission | gcc-m32 -O2 | 1.000 | 0.413 | 100.0% (6/6) | #1 | 0 | 2 | GNR 0.88<br>type 0.60<br>expr 0.68<br>cf 1.00<br>art 0 | 3392ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.615 | 100.0% (6/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 7716ms | ✅ |
| fission | clang -O0 | 1.000 | 0.113 | 100.0% (6/6) | #1 | 2 | 2 | GNR 0.88<br>type 0.57<br>expr 0.71<br>cf 1.00<br>art 0 | 7000ms | ✅ |
| ghidra | clang -O0 | 1.000 | 0.535 | 100.0% (6/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 8724ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.615 | 100.0% (6/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 7596ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.395 | 0.0% (0/6) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 7 | 6857ms | 🔴 compile |
| ghidra | gcc -O2 | 0.000 | 0.198 | 0.0% (0/6) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 6 | 6886ms | 🔴 compile |
| fission | clang -O2 | n/a | 0.000 | n/a | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: ReadTim |

### `bounded_checksum` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O2 | 1.000 | 0.098 | 100.0% (6/6) | #1 | 0 | 3 | GNR 0.62<br>type 0.50<br>expr 0.70<br>cf 1.00<br>art 0 | 6886ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.548 | 100.0% (6/6) | #1 | 0 | 2 | GNR 0.00<br>type 0.50<br>expr 0.80<br>cf 1.00<br>art 0 | 6902ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.286 | 100.0% (6/6) | #1 | 0 | 3 | GNR 0.22<br>type 0.50<br>expr 0.75<br>cf 1.00<br>art 0 | 7716ms | ✅ |
| fission | clang -O0 | 1.000 | 0.111 | 100.0% (6/6) | #1 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 7000ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.153 | 100.0% (6/6) | #1 | 0 | 4 | GNR 0.64<br>type 0.50<br>expr 0.47<br>cf 1.00<br>art 0 | 7596ms | ✅ |
| fission | gcc -O0 | 0.500 | 0.055 | 50.0% (3/6) | #1 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 6576ms | 🟤 assert |
| fission | gcc -O2 | 0.500 | 0.108 | 50.0% (3/6) | #2 | 1 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 6351ms | 🟤 assert |
| fission | gcc-m32 -O2 | 0.167 | 0.112 | 16.7% (1/6) | #2 | 2 | 2 | GNR 0.20<br>type 0.50<br>expr 0.67<br>cf 0.60<br>art 0 | 3392ms | 🟤 assert |
| ghidra | gcc -O0 | 0.000 | 0.421 | 0.0% (0/6) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 6 | 6857ms | 🟠 runtime |
| fission | gcc-m32 -O0 | 0.000 | 0.069 | 0.0% (0/6) ⚠️intrin | #2 | 0 | 3 | GNR 0.22<br>type 0.50<br>expr 0.45<br>cf 1.00<br>art 2 | 5447ms | 🔴 compile |
| ghidra | clang -O0 | 0.000 | 0.319 | 0.0% (0/6) | #2 | 0 | 2 | GNR 0.30<br>type 0.50<br>expr 0.74<br>cf 1.00<br>art 0 | 8724ms | 🔴 compile |
| fission | clang -O2 | n/a | 0.000 | n/a | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: ReadTim |

### `bounded_tlv_sum` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 1.000 | 0.092 | 100.0% (7/7) | #1 | 5 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 8586ms | ✅ |
| ghidra | gcc -O2 | 1.000 | 0.151 | 100.0% (7/7) | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 9494ms | ✅ |
| fission | gcc-m32 -O0 | 1.000 | 0.066 | 100.0% (7/7) | #1 | 5 | 2 | GNR 0.52<br>type 0.50<br>expr 0.48<br>cf 1.00<br>art 0 | 7312ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.363 | 100.0% (7/7) | #1 | 0 | 3 | GNR 0.22<br>type 0.50<br>expr 0.64<br>cf 1.00<br>art 0 | 8868ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.149 | 100.0% (7/7) | #1 | 0 | 5 | GNR 0.61<br>type 0.50<br>expr 0.56<br>cf 1.00<br>art 0 | 8968ms | ✅ |
| fission | clang -O0 | 1.000 | 0.084 | 100.0% (7/7) | #1 | 6 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9957ms | ✅ |
| ghidra | clang -O0 | 1.000 | 0.363 | 100.0% (7/7) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 8561ms | ✅ |
| fission | gcc -O2 | 0.429 | 0.044 | 42.9% (3/7) | #2 | 5 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 8157ms | 🟤 assert |
| ghidra | gcc -O0 | 0.000 | 0.334 | 0.0% (0/7) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 7 | 6521ms | 🟠 runtime |
| fission | gcc-m32 -O2 | 0.000 | 0.043 | 0.0% (0/7) | #2 | 5 | 3 | GNR 0.23<br>type 0.50<br>expr 0.50<br>cf 0.75<br>art 0 | 7586ms | 🔴 compile |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 16155ms | ❌ Decompiler returned whole-prog |
| ghidra | clang -O2 | 0.000 | 0.040 | 0.0% (0/7) | #1 | 2 | 7 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 16 | 8925ms | 🔴 compile |

### `bubble_sort` 🔴 Fission-only gap
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc-m32 -O0 | 1.000 | 0.152 | 100.0% (5/5) | #1 | 0 | 4 | GNR 0.12<br>type 0.50<br>expr 0.77<br>cf 1.00<br>art 0 | 8292ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.190 | 100.0% (5/5) | #1 | 0 | 5 | GNR 0.12<br>type 0.50<br>expr 0.72<br>cf 1.00<br>art 0 | 7541ms | ✅ |
| ghidra | clang -O0 | 1.000 | 0.361 | 100.0% (5/5) | #1 | 0 | 4 | GNR 0.57<br>type 0.50<br>expr 0.69<br>cf 1.00<br>art 0 | 9212ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.100 | 100.0% (5/5) | #1 | 0 | 7 | GNR 0.74<br>type 0.50<br>expr 0.52<br>cf 1.00<br>art 0 | 7615ms | ✅ |
| ghidra | gcc -O0 | 0.400 | 0.167 | 40.0% (2/5) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 15 | 8870ms | 🟤 assert |
| fission | gcc -O0 | 0.000 | 0.062 | 0.0% (0/5) | #2 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9593ms | 🟠 runtime |
| fission | gcc -O2 | 0.000 | 0.042 | 0.0% (0/5) | #1 | 4 | 3 | GNR 0.36<br>type 0.57<br>expr 0.50<br>cf 0.75<br>art 0 | 8452ms | 🔴 compile |
| ghidra | gcc -O2 | 0.000 | 0.131 | 0.0% (0/5) | #1 | 0 | 5 | GNR 0.26<br>type 0.42<br>expr 0.51<br>cf 1.00<br>art 2 | 8426ms | 🔴 compile |
| fission | gcc-m32 -O0 | 0.000 | 0.063 | 0.0% (0/5) | #2 | 4 | 2 | GNR 0.41<br>type 0.50<br>expr 0.40<br>cf 0.43<br>art 0 | 7828ms | 🟠 runtime |
| fission | gcc-m32 -O2 | 0.000 | 0.048 | 0.0% (0/5) | #2 | 4 | 3 | GNR 0.32<br>type 0.50<br>expr 0.63<br>cf 0.75<br>art 0 | 7952ms | 🟡 timeout |
| fission | clang -O0 | 0.000 | 0.042 | 0.0% (0/5) | #2 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9350ms | 🟠 runtime |
| fission | clang -O2 | 0.000 | 0.046 | 0.0% (0/5) | #2 | 14 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9424ms | 🟠 runtime |

### `checksum` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 1.000 | 0.121 | 100.0% (5/5) | #1 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 7363ms | ✅ |
| ghidra | gcc -O0 | 1.000 | 0.668 | 100.0% (5/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 4 | 12265ms | ✅ |
| fission | gcc -O2 | 1.000 | 0.187 | 100.0% (5/5) | #1 | 1 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 7052ms | ✅ |
| ghidra | gcc -O2 | 1.000 | 0.129 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.28<br>type 0.50<br>expr 0.78<br>cf 1.00<br>art 0 | 11998ms | ✅ |
| fission | gcc-m32 -O0 | 1.000 | 0.147 | 100.0% (5/5) | #1 | 2 | 2 | GNR 0.78<br>type 0.50<br>expr 0.69<br>cf 1.00<br>art 0 | 6485ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.819 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.00<br>type 0.50<br>expr 0.86<br>cf 1.00<br>art 0 | 10412ms | ✅ |
| fission | gcc-m32 -O2 | 1.000 | 0.114 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.24<br>type 0.50<br>expr 0.62<br>cf 1.00<br>art 0 | 4437ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.116 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.38<br>type 0.50<br>expr 0.64<br>cf 1.00<br>art 0 | 10298ms | ✅ |
| fission | clang -O0 | 1.000 | 0.105 | 100.0% (5/5) | #1 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 6712ms | ✅ |
| ghidra | clang -O0 | 1.000 | 0.732 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.00<br>type 0.50<br>expr 0.86<br>cf 1.00<br>art 0 | 8750ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.144 | 100.0% (5/5) | #1 | 0 | 4 | GNR 0.71<br>type 0.50<br>expr 0.49<br>cf 1.00<br>art 0 | 9138ms | ✅ |
| fission | clang -O2 | 0.000 | 0.033 | 0.0% (0/5) | #2 | 5 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 7644ms | 🔴 compile |

### `clamp` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 1.000 | 0.102 | 100.0% (6/6) | #1 | 4 | 2 | GNR 0.91<br>type 0.50<br>expr 0.63<br>cf 1.00<br>art 0 | 7363ms | ✅ |
| fission | gcc -O2 | 1.000 | 0.107 | 100.0% (6/6) ⚠️intrin | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 1 | 7052ms | ✅ |
| ghidra | gcc -O2 | 1.000 | 0.582 | 100.0% (6/6) | #1 | 0 | 2 | GNR 0.00<br>type 0.50<br>expr 0.91<br>cf 1.00<br>art 0 | 11998ms | ✅ |
| fission | gcc-m32 -O0 | 1.000 | 0.601 | 100.0% (6/6) | #1 | 0 | 2 | GNR 0.91<br>type 0.50<br>expr 0.63<br>cf 1.00<br>art 0 | 6485ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.590 | 100.0% (6/6) | #1 | 0 | 2 | GNR 0.00<br>type 0.50<br>expr 0.89<br>cf 1.00<br>art 0 | 10412ms | ✅ |
| fission | gcc-m32 -O2 | 1.000 | 0.187 | 100.0% (6/6) ⚠️intrin | #1 | 0 | 2 | GNR 0.30<br>type 0.50<br>expr 0.71<br>cf 1.00<br>art 1 | 4437ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.731 | 100.0% (6/6) | #1 | 0 | 2 | GNR 0.00<br>type 0.50<br>expr 0.91<br>cf 1.00<br>art 0 | 10298ms | ✅ |
| fission | clang -O0 | 1.000 | 0.100 | 100.0% (6/6) | #1 | 4 | 2 | GNR 0.91<br>type 0.50<br>expr 0.63<br>cf 1.00<br>art 0 | 6712ms | ✅ |
| ghidra | clang -O0 | 1.000 | 0.421 | 100.0% (6/6) | #1 | 0 | 2 | GNR 0.26<br>type 0.50<br>expr 0.85<br>cf 1.00<br>art 0 | 8750ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.731 | 100.0% (6/6) | #1 | 0 | 2 | GNR 0.00<br>type 0.50<br>expr 0.91<br>cf 1.00<br>art 0 | 9138ms | ✅ |
| fission | clang -O2 | 0.333 | 0.181 | 33.3% (2/6) | #2 | 0 | 1 | GNR 0.89<br>type 0.50<br>expr 0.68<br>cf 1.00<br>art 0 | 7644ms | 🟤 assert |
| ghidra | gcc -O0 | 0.000 | 0.421 | 0.0% (0/6) | #2 | 0 | 2 | GNR 0.75<br>type 0.50<br>expr 0.77<br>cf 1.00<br>art 9 | 12265ms | 🟤 assert |

### `count_bits` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 1.000 | 0.199 | 100.0% (6/6) | #1 | 2 | 2 | GNR 0.92<br>type 0.50<br>expr 0.81<br>cf 1.00<br>art 0 | 7363ms | ✅ |
| ghidra | gcc -O2 | 1.000 | 0.609 | 100.0% (6/6) | #1 | 0 | 2 | GNR 0.45<br>type 0.50<br>expr 0.82<br>cf 1.00<br>art 0 | 11998ms | ✅ |
| fission | gcc-m32 -O0 | 1.000 | 0.510 | 100.0% (6/6) | #1 | 0 | 3 | GNR 0.89<br>type 0.50<br>expr 0.82<br>cf 1.00<br>art 0 | 6485ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.755 | 100.0% (6/6) | #1 | 0 | 2 | GNR 0.00<br>type 0.50<br>expr 0.88<br>cf 1.00<br>art 0 | 10412ms | ✅ |
| fission | gcc-m32 -O2 | 1.000 | 0.421 | 100.0% (6/6) | #1 | 0 | 3 | GNR 0.50<br>type 0.50<br>expr 0.86<br>cf 1.00<br>art 0 | 4437ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.609 | 100.0% (6/6) | #1 | 0 | 2 | GNR 0.45<br>type 0.50<br>expr 0.82<br>cf 1.00<br>art 0 | 10298ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.581 | 100.0% (6/6) | #1 | 0 | 3 | GNR 0.53<br>type 0.50<br>expr 0.81<br>cf 1.00<br>art 0 | 9138ms | ✅ |
| fission | clang -O2 | 0.500 | 0.223 | 50.0% (3/6) | #2 | 1 | 3 | GNR 0.24<br>type 0.50<br>expr 0.78<br>cf 1.00<br>art 0 | 7644ms | 🟤 assert |
| ghidra | gcc -O0 | 0.167 | 0.688 | 16.7% (1/6) | #2 | 0 | 2 | GNR 0.14<br>type 0.50<br>expr 0.85<br>cf 1.00<br>art 2 | 12265ms | 🟤 assert |
| fission | gcc -O2 | 0.000 | 0.240 | 0.0% (0/6) | #2 | 1 | 3 | GNR 0.31<br>type 0.50<br>expr 0.79<br>cf 1.00<br>art 0 | 7052ms | 🟡 timeout |
| fission | clang -O0 | 0.000 | 0.146 | 0.0% (0/6) | #1 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 6712ms | 🔴 compile |
| ghidra | clang -O0 | 0.000 | 0.298 | 0.0% (0/6) | #1 | 0 | 2 | GNR 0.69<br>type 0.33<br>expr 0.78<br>cf 1.00<br>art 2 | 8750ms | 🟡 timeout |

### `crc32` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 1.000 | 0.071 | 100.0% (6/6) | #1 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 23524ms | ✅ |
| fission | gcc -O2 | 1.000 | 0.073 | 100.0% (6/6) | #1 | 1 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 21731ms | ✅ |
| ghidra | gcc -O2 | 1.000 | 0.293 | 100.0% (6/6) | #1 | 0 | 4 | GNR 0.50<br>type 0.50<br>expr 0.71<br>cf 1.00<br>art 0 | 13994ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.400 | 100.0% (6/6) | #1 | 0 | 3 | GNR 0.00<br>type 0.50<br>expr 0.80<br>cf 1.00<br>art 0 | 15661ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.305 | 100.0% (6/6) | #1 | 0 | 4 | GNR 0.50<br>type 0.50<br>expr 0.71<br>cf 1.00<br>art 0 | 15848ms | ✅ |
| fission | clang -O0 | 1.000 | 0.050 | 100.0% (6/6) | #1 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9806ms | ✅ |
| ghidra | clang -O0 | 1.000 | 0.474 | 100.0% (6/6) | #1 | 0 | 3 | GNR 0.00<br>type 0.50<br>expr 0.80<br>cf 1.00<br>art 0 | 17119ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.057 | 100.0% (6/6) | #1 | 0 | 3 | GNR 0.70<br>type 0.50<br>expr 0.50<br>cf 1.00<br>art 0 | 18789ms | ✅ |
| fission | clang -O2 | 0.333 | 0.086 | 33.3% (2/6) | #2 | 2 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 29124ms | 🟤 assert |
| fission | gcc-m32 -O0 | 0.167 | 0.075 | 16.7% (1/6) | #2 | 4 | 2 | GNR 0.51<br>type 0.50<br>expr 0.65<br>cf 1.00<br>art 0 | 12140ms | 🟤 assert |
| fission | gcc-m32 -O2 | 0.167 | 0.040 | 16.7% (1/6) | #2 | 1 | 4 | GNR 0.14<br>type 0.50<br>expr 0.60<br>cf 1.00<br>art 0 | 7601ms | 🟤 assert |
| ghidra | gcc -O0 | 0.000 | 0.343 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 4 | 15586ms | 🔴 compile |

### `dot_product_stride` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 1.000 | 0.069 | 100.0% (5/5) | #1 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 6576ms | ✅ |
| ghidra | gcc -O2 | 1.000 | 0.073 | 100.0% (5/5) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 6886ms | ✅ |
| fission | gcc-m32 -O0 | 1.000 | 0.092 | 100.0% (5/5) | #1 | 2 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 5447ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.566 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.12<br>type 0.50<br>expr 0.79<br>cf 1.00<br>art 0 | 6902ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.239 | 100.0% (5/5) | #1 | 0 | 4 | GNR 0.30<br>type 0.50<br>expr 0.68<br>cf 1.00<br>art 0 | 7716ms | ✅ |
| fission | clang -O0 | 1.000 | 0.113 | 100.0% (5/5) | #1 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 7000ms | ✅ |
| ghidra | clang -O0 | 1.000 | 0.494 | 100.0% (5/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 8724ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.474 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 4 | 6857ms | 🟠 runtime |
| fission | gcc -O2 | 0.000 | 0.075 | 0.0% (0/5) | #2 | 2 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 6351ms | 🟤 assert |
| fission | gcc-m32 -O2 | 0.000 | 0.090 | 0.0% (0/5) | #2 | 1 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 3392ms | 🔴 compile |
| ghidra | clang -O2 | 0.000 | 0.049 | 0.0% (0/5) | #1 | 1 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 13 | 7596ms | 🔴 compile |
| fission | clang -O2 | n/a | 0.000 | n/a | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: ReadTim |

### `factorial` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O2 | 1.000 | 0.212 | 100.0% (5/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 8426ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.579 | 100.0% (5/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 8292ms | ✅ |
| ghidra | clang -O0 | 1.000 | 0.504 | 100.0% (5/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 1 | 9212ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.290 | 100.0% (5/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 7615ms | ✅ |
| fission | gcc -O0 | 0.600 | 0.189 | 60.0% (3/5) | #1 | 2 | 2 | GNR 0.36<br>type 0.50<br>expr 0.78<br>cf 1.00<br>art 0 | 9593ms | 🟤 assert |
| ghidra | gcc -O0 | 0.400 | 0.335 | 40.0% (2/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 3 | 8870ms | 🟤 assert |
| fission | gcc -O2 | 0.400 | 0.179 | 40.0% (2/5) | #2 | 3 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 8452ms | 🟤 assert |
| fission | gcc-m32 -O0 | 0.400 | 0.146 | 40.0% (2/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 7828ms | 🟤 assert |
| fission | clang -O0 | 0.400 | 0.177 | 40.0% (2/5) | #2 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 9350ms | 🟤 assert |
| fission | clang -O2 | 0.400 | 0.080 | 40.0% (2/5) | #2 | 1 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 9424ms | 🟤 assert |
| fission | gcc-m32 -O2 | 0.000 | 0.033 | 0.0% (0/5) | #1 | 1 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 7952ms | 🟡 timeout |
| ghidra | gcc-m32 -O2 | 0.000 | 0.136 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 7541ms | 🔴 compile |

### `fibonacci` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O2 | 1.000 | 0.218 | 100.0% (6/6) | #1 | 0 | 3 | GNR 0.59<br>type 0.50<br>expr 0.68<br>cf 1.00<br>art 0 | 8426ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.598 | 100.0% (6/6) | #1 | 0 | 2 | GNR 0.35<br>type 0.50<br>expr 0.79<br>cf 1.00<br>art 0 | 8292ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.260 | 100.0% (6/6) | #1 | 0 | 3 | GNR 0.64<br>type 0.50<br>expr 0.73<br>cf 1.00<br>art 0 | 7541ms | ✅ |
| ghidra | clang -O0 | 1.000 | 0.484 | 100.0% (6/6) | #1 | 0 | 2 | GNR 0.45<br>type 0.40<br>expr 0.77<br>cf 1.00<br>art 1 | 9212ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.254 | 100.0% (6/6) | #1 | 0 | 3 | GNR 0.67<br>type 0.50<br>expr 0.75<br>cf 1.00<br>art 0 | 7615ms | ✅ |
| fission | gcc-m32 -O0 | 0.500 | 0.236 | 50.0% (3/6) | #2 | 0 | 3 | GNR 0.29<br>type 0.50<br>expr 0.80<br>cf 1.00<br>art 0 | 7828ms | 🟤 assert |
| fission | gcc-m32 -O2 | 0.500 | 0.086 | 50.0% (3/6) | #2 | 1 | 3 | GNR 0.24<br>type 0.50<br>expr 0.83<br>cf 0.75<br>art 0 | 7952ms | 🟤 assert |
| fission | gcc -O0 | 0.333 | 0.164 | 33.3% (2/6) | #1 | 2 | 2 | GNR 0.19<br>type 0.50<br>expr 0.75<br>cf 0.33<br>art 0 | 9593ms | 🟤 assert |
| fission | gcc -O2 | 0.333 | 0.160 | 33.3% (2/6) | #2 | 1 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 8452ms | 🟤 assert |
| fission | clang -O0 | 0.333 | 0.150 | 33.3% (2/6) | #2 | 2 | 2 | GNR 0.38<br>type 0.50<br>expr 0.87<br>cf 1.00<br>art 0 | 9350ms | 🟤 assert |
| ghidra | gcc -O0 | 0.167 | 0.321 | 16.7% (1/6) | #2 | 0 | 2 | GNR 0.53<br>type 0.50<br>expr 0.80<br>cf 1.00<br>art 4 | 8870ms | 🟤 assert |
| fission | clang -O2 | 0.167 | 0.177 | 16.7% (1/6) | #2 | 1 | 2 | GNR 0.10<br>type 0.50<br>expr 0.68<br>cf 0.67<br>art 0 | 9424ms | 🟤 assert |

### `find_pair_value` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 1.000 | 0.085 | 100.0% (5/5) | #1 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 9561ms | ✅ |
| ghidra | gcc -O2 | 1.000 | 0.212 | 100.0% (5/5) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 10763ms | ✅ |
| fission | gcc-m32 -O0 | 1.000 | 0.124 | 100.0% (5/5) | #1 | 2 | 2 | GNR 0.43<br>type 0.50<br>expr 0.52<br>cf 1.00<br>art 0 | 4977ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.695 | 100.0% (5/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 5723ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.212 | 100.0% (5/5) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 8959ms | ✅ |
| ghidra | clang -O0 | 1.000 | 0.472 | 100.0% (5/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 9867ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.442 | 100.0% (5/5) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 10063ms | ✅ |
| fission | gcc -O2 | 0.800 | 0.170 | 80.0% (4/5) | #2 | 4 | 2 | GNR 0.56<br>type 0.50<br>expr 0.82<br>cf 0.60<br>art 0 | 9588ms | 🟤 assert |
| fission | gcc-m32 -O2 | 0.800 | 0.168 | 80.0% (4/5) | #2 | 4 | 2 | GNR 0.44<br>type 0.50<br>expr 0.84<br>cf 0.60<br>art 0 | 8431ms | 🟤 assert |
| ghidra | gcc -O0 | 0.000 | 0.342 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 5 | 11208ms | 🟠 runtime |
| fission | clang -O0 | 0.000 | 0.083 | 0.0% (0/5) | #2 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10111ms | 🔴 compile |
| fission | clang -O2 | n/a | 0.000 | n/a | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: ReadTim |

### `find_substring` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O2 | 1.000 | 0.162 | 100.0% (6/6) | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 29360ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.401 | 100.0% (6/6) | #1 | 0 | 4 | GNR 0.16<br>type 0.50<br>expr 0.69<br>cf 1.00<br>art 0 | 28155ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.204 | 100.0% (6/6) | #1 | 0 | 5 | GNR 0.42<br>type 0.50<br>expr 0.64<br>cf 1.00<br>art 0 | 28725ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.223 | 100.0% (6/6) | #1 | 0 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 18330ms | ✅ |
| fission | gcc-m32 -O0 | 0.667 | 0.089 | 66.7% (4/6) | #2 | 5 | 2 | GNR 0.42<br>type 0.50<br>expr 0.56<br>cf 0.60<br>art 0 | 11293ms | 🟤 assert |
| fission | gcc -O0 | 0.500 | 0.082 | 50.0% (3/6) | #1 | 12 | 2 | GNR 0.80<br>type 0.50<br>expr 0.87<br>cf 0.67<br>art 0 | 27050ms | 🟤 assert |
| fission | gcc-m32 -O2 | 0.500 | 0.072 | 50.0% (3/6) | #2 | 6 | 2 | GNR 0.30<br>type 0.50<br>expr 0.65<br>cf 0.67<br>art 0 | 11680ms | 🟤 assert |
| ghidra | gcc -O0 | 0.167 | 0.281 | 16.7% (1/6) | #2 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 10 | 27516ms | 🟤 assert |
| fission | gcc -O2 | 0.000 | 0.126 | 0.0% (0/6) | #2 | 5 | 4 | GNR 0.43<br>type 0.50<br>expr 0.63<br>cf 0.64<br>art 0 | 11479ms | 🔴 compile |
| fission | clang -O0 | 0.000 | 0.066 | 0.0% (0/6) | #1 | 12 | 2 | GNR 0.83<br>type 0.50<br>expr 0.86<br>cf 0.67<br>art 0 | 13776ms | 🔴 compile |
| ghidra | clang -O0 | 0.000 | 0.142 | 0.0% (0/6) | #1 | 0 | 5 | GNR 0.43<br>type 0.50<br>expr 0.64<br>cf 1.00<br>art 0 | 24865ms | 🔴 compile |
| fission | clang -O2 | 0.000 | 0.063 | 0.0% (0/6) | #2 | 8 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 12719ms | 🔴 compile |

### `kv_lookup` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 1.000 | 0.061 | 100.0% (6/6) | #1 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 6576ms | ✅ |
| fission | gcc -O2 | 1.000 | 0.124 | 100.0% (6/6) | #1 | 4 | 2 | GNR 0.56<br>type 0.50<br>expr 0.82<br>cf 0.60<br>art 0 | 6351ms | ✅ |
| ghidra | gcc -O2 | 1.000 | 0.146 | 100.0% (6/6) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 6886ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.681 | 100.0% (6/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 6902ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.189 | 100.0% (6/6) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 7716ms | ✅ |
| ghidra | clang -O0 | 1.000 | 0.455 | 100.0% (6/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 8724ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.412 | 100.0% (6/6) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 7596ms | ✅ |
| fission | gcc-m32 -O2 | 0.833 | 0.096 | 83.3% (5/6) | #2 | 3 | 4 | GNR 0.45<br>type 0.50<br>expr 0.82<br>cf 0.62<br>art 0 | 3392ms | 🟤 assert |
| fission | gcc-m32 -O0 | 0.333 | 0.068 | 33.3% (2/6) | #2 | 1 | 3 | GNR 0.42<br>type 0.50<br>expr 0.51<br>cf 1.00<br>art 0 | 5447ms | 🟤 assert |
| ghidra | gcc -O0 | 0.000 | 0.316 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 5 | 6857ms | 🟠 runtime |
| fission | clang -O0 | 0.000 | 0.061 | 0.0% (0/6) | #2 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 7000ms | 🔴 compile |
| fission | clang -O2 | n/a | 0.000 | n/a | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: ReadTim |

### `linear_search` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O2 | 1.000 | 0.660 | 100.0% (6/6) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 8426ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.617 | 100.0% (6/6) | #1 | 0 | 3 | GNR 0.00<br>type 0.50<br>expr 0.89<br>cf 1.00<br>art 0 | 8292ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.688 | 100.0% (6/6) | #1 | 0 | 4 | GNR 0.47<br>type 0.50<br>expr 0.83<br>cf 1.00<br>art 0 | 7541ms | ✅ |
| fission | clang -O0 | 1.000 | 0.114 | 100.0% (6/6) | #1 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9350ms | ✅ |
| ghidra | clang -O0 | 1.000 | 0.401 | 100.0% (6/6) | #1 | 0 | 3 | GNR 0.00<br>type 0.50<br>expr 0.89<br>cf 1.00<br>art 0 | 9212ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.317 | 100.0% (6/6) | #1 | 0 | 4 | GNR 0.47<br>type 0.50<br>expr 0.76<br>cf 1.00<br>art 0 | 7615ms | ✅ |
| fission | gcc -O0 | 0.667 | 0.142 | 66.7% (4/6) | #1 | 4 | 2 | GNR 0.61<br>type 0.50<br>expr 0.81<br>cf 1.00<br>art 0 | 9593ms | 🟤 assert |
| fission | clang -O2 | 0.667 | 0.181 | 66.7% (4/6) | #2 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9424ms | 🟤 assert |
| fission | gcc -O2 | 0.333 | 0.220 | 33.3% (2/6) | #2 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 8452ms | 🟤 assert |
| fission | gcc-m32 -O0 | 0.333 | 0.205 | 33.3% (2/6) | #2 | 1 | 3 | GNR 0.48<br>type 0.50<br>expr 0.60<br>cf 1.00<br>art 0 | 7828ms | 🟤 assert |
| fission | gcc-m32 -O2 | 0.333 | 0.229 | 33.3% (2/6) | #2 | 4 | 2 | GNR 0.44<br>type 0.50<br>expr 0.84<br>cf 0.60<br>art 0 | 7952ms | 🟤 assert |
| ghidra | gcc -O0 | 0.000 | 0.371 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 4 | 8870ms | 🟠 runtime |

### `list_sum` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 1.000 | 0.057 | 100.0% (5/5) | #1 | 2 | 2 | GNR 0.67<br>type 0.50<br>expr 0.66<br>cf 1.00<br>art 0 | 6576ms | ✅ |
| fission | gcc -O2 | 1.000 | 0.089 | 100.0% (5/5) | #1 | 1 | 3 | GNR 0.33<br>type 0.50<br>expr 0.75<br>cf 1.00<br>art 0 | 6351ms | ✅ |
| ghidra | gcc -O2 | 1.000 | 0.453 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.91<br>type 0.50<br>expr 0.65<br>cf 1.00<br>art 0 | 6886ms | ✅ |
| fission | gcc-m32 -O0 | 1.000 | 0.247 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.67<br>type 0.50<br>expr 0.71<br>cf 1.00<br>art 0 | 5447ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.652 | 100.0% (5/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 6902ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.573 | 100.0% (5/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 7716ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.573 | 100.0% (5/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 1 | 7596ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.595 | 0.0% (0/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 2 | 6857ms | 🟠 runtime |
| fission | gcc-m32 -O2 | 0.000 | 0.455 | 0.0% (0/5) | #2 | 0 | 3 | GNR 0.33<br>type 0.50<br>expr 0.84<br>cf 1.00<br>art 0 | 3392ms | 🟡 timeout |
| fission | clang -O0 | 0.000 | 0.062 | 0.0% (0/5) | #1 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 7000ms | 🟠 runtime |
| ghidra | clang -O0 | 0.000 | 0.353 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 8724ms | 🔴 compile |
| fission | clang -O2 | n/a | 0.000 | n/a | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: ReadTim |

### `manipulate_bitfields` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O2 | 1.000 | 0.312 | 100.0% (5/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 20025ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.312 | 100.0% (5/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 24930ms | ✅ |
| fission | gcc -O2 | 0.800 | 0.097 | 80.0% (4/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 21511ms | 🟤 assert |
| fission | clang -O0 | 0.800 | 0.050 | 80.0% (4/5) ⚠️intrin | #1 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 1 | 16320ms | 🟤 assert |
| fission | clang -O2 | 0.800 | 0.083 | 80.0% (4/5) | #1 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 30147ms | 🟤 assert |
| fission | gcc-m32 -O2 | 0.200 | 0.069 | 20.0% (1/5) ⚠️intrin | #2 | 0 | 2 | GNR 0.14<br>type 0.50<br>expr 0.50<br>cf 1.00<br>art 1 | 13918ms | 🟤 assert |
| fission | gcc -O0 | 0.000 | 0.079 | 0.0% (0/5) ⚠️intrin | #1 | 0 | 1 | GNR 0.27<br>type 0.50<br>expr 0.47<br>cf 1.00<br>art 1 | 22238ms | 🔴 compile |
| ghidra | gcc -O0 | 0.000 | 0.119 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 14 | 19257ms | 🟠 runtime |
| fission | gcc-m32 -O0 | 0.000 | 0.049 | 0.0% (0/5) ⚠️intrin | #1 | 0 | 1 | GNR 0.28<br>type 0.50<br>expr 0.47<br>cf 1.00<br>art 1 | 18824ms | 🔴 compile |
| ghidra | gcc-m32 -O0 | 0.000 | 0.208 | 0.0% (0/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 24750ms | 🔴 compile |
| ghidra | clang -O0 | 0.000 | 0.205 | 0.0% (0/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 27492ms | 🔴 compile |
| ghidra | clang -O2 | 0.000 | 0.341 | 0.0% (0/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 24991ms | 🔴 compile |

### `matrix_multiply` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O2 | 1.000 | 0.206 | 100.0% (5/5) | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 20025ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.489 | 100.0% (5/5) | #1 | 0 | 4 | GNR 0.00<br>type 0.50<br>expr 0.77<br>cf 1.00<br>art 0 | 24750ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.163 | 100.0% (5/5) | #1 | 0 | 5 | GNR 0.38<br>type 0.50<br>expr 0.63<br>cf 1.00<br>art 0 | 24930ms | ✅ |
| ghidra | clang -O0 | 1.000 | 0.701 | 100.0% (5/5) | #1 | 0 | 4 | GNR 0.00<br>type 0.50<br>expr 0.77<br>cf 1.00<br>art 0 | 27492ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.197 | 100.0% (5/5) | #1 | 0 | 6 | GNR 0.46<br>type 0.50<br>expr 0.50<br>cf 1.00<br>art 0 | 24991ms | ✅ |
| fission | gcc -O0 | 0.200 | 0.057 | 20.0% (1/5) | #1 | 6 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 22238ms | 🟤 assert |
| ghidra | gcc -O0 | 0.000 | 0.387 | 0.0% (0/5) | #2 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 4 | 19257ms | 🟤 assert |
| fission | gcc -O2 | 0.000 | 0.018 | 0.0% (0/5) | #2 | 1 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 21511ms | 🔴 compile |
| fission | gcc-m32 -O0 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 18824ms | ❌ Decompiler error: rust_sleigh  |
| fission | gcc-m32 -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 13918ms | ❌ Decompiler error: rust_sleigh  |
| fission | clang -O0 | 0.000 | 0.050 | 0.0% (0/5) | #2 | 6 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 16320ms | 🟤 assert |
| fission | clang -O2 | 0.000 | 0.025 | 0.0% (0/5) | #2 | 9 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 30147ms | 🔴 compile |

### `mixed_width_accumulate` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O2 | 1.000 | 0.205 | 100.0% (6/6) | #1 | 0 | 4 | GNR 0.15<br>type 0.50<br>expr 0.75<br>cf 1.00<br>art 0 | 9494ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.629 | 100.0% (6/6) | #1 | 0 | 3 | GNR 0.30<br>type 0.50<br>expr 0.75<br>cf 1.00<br>art 0 | 8868ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.187 | 100.0% (6/6) | #1 | 0 | 4 | GNR 0.33<br>type 0.50<br>expr 0.74<br>cf 1.00<br>art 0 | 8968ms | ✅ |
| fission | gcc -O0 | 0.500 | 0.084 | 50.0% (3/6) | #1 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 8586ms | 🟤 assert |
| fission | gcc-m32 -O0 | 0.500 | 0.056 | 50.0% (3/6) | #2 | 0 | 4 | GNR 0.50<br>type 0.50<br>expr 0.53<br>cf 1.00<br>art 0 | 7312ms | 🟤 assert |
| fission | gcc-m32 -O2 | 0.333 | 0.068 | 33.3% (2/6) | #2 | 1 | 3 | GNR 0.30<br>type 0.50<br>expr 0.74<br>cf 1.00<br>art 0 | 7586ms | 🟤 assert |
| ghidra | gcc -O0 | 0.000 | 0.181 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 4 | 6521ms | 🟠 runtime |
| fission | gcc -O2 | 0.000 | 0.098 | 0.0% (0/6) | #2 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 8157ms | 🟠 runtime |
| fission | clang -O0 | 0.000 | 0.049 | 0.0% (0/6) ⚠️intrin | #1 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 3 | 9957ms | 🟡 timeout |
| ghidra | clang -O0 | 0.000 | 0.328 | 0.0% (0/6) | #1 | 0 | 3 | GNR 0.24<br>type 0.50<br>expr 0.73<br>cf 1.00<br>art 0 | 8561ms | 🔴 compile |
| fission | clang -O2 | 0.000 | 0.021 | 0.0% (0/6) | #1 | 5 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 16155ms | 🔴 compile |
| ghidra | clang -O2 | 0.000 | 0.044 | 0.0% (0/6) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 14 | 8925ms | 🔴 compile |

### `mul_ints` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 1.000 | 0.203 | 100.0% (5/5) | #1 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 6576ms | ✅ |
| fission | gcc -O2 | 1.000 | 0.424 | 100.0% (5/5) | #1 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 6351ms | ✅ |
| ghidra | gcc -O2 | 1.000 | 0.739 | 100.0% (5/5) | #1 | 0 | 1 | GNR 0.80<br>type 0.50<br>expr 0.83<br>cf 1.00<br>art 0 | 6886ms | ✅ |
| fission | gcc-m32 -O0 | 1.000 | 0.470 | 100.0% (5/5) | #1 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 5447ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.989 | 100.0% (5/5) | #1 | 0 | 1 | GNR 0.00<br>type 0.50<br>expr 0.93<br>cf 1.00<br>art 0 | 6902ms | ✅ |
| fission | gcc-m32 -O2 | 1.000 | 0.470 | 100.0% (5/5) | #1 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 3392ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.943 | 100.0% (5/5) | #1 | 0 | 1 | GNR 0.00<br>type 0.50<br>expr 0.93<br>cf 1.00<br>art 0 | 7716ms | ✅ |
| ghidra | clang -O0 | 1.000 | 0.761 | 100.0% (5/5) | #1 | 0 | 1 | GNR 0.00<br>type 0.50<br>expr 0.93<br>cf 1.00<br>art 0 | 8724ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.989 | 100.0% (5/5) | #1 | 0 | 1 | GNR 0.00<br>type 0.50<br>expr 0.93<br>cf 1.00<br>art 0 | 7596ms | ✅ |
| ghidra | gcc -O0 | 0.200 | 0.678 | 20.0% (1/5) | #2 | 0 | 1 | GNR 0.57<br>type 0.50<br>expr 0.86<br>cf 1.00<br>art 4 | 6857ms | 🟤 assert |
| fission | clang -O0 | 0.000 | 0.161 | 0.0% (0/5) | #2 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 7000ms | 🔴 compile |
| fission | clang -O2 | n/a | 0.000 | n/a | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: ReadTim |

### `overlap_move` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 1.000 | 0.046 | 100.0% (6/6) | #1 | 9 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 8586ms | ✅ |
| ghidra | gcc -O2 | 1.000 | 0.236 | 100.0% (6/6) | #1 | 0 | 4 | GNR 0.17<br>type 0.50<br>expr 0.73<br>cf 1.00<br>art 0 | 9494ms | ✅ |
| fission | gcc-m32 -O0 | 1.000 | 0.080 | 100.0% (6/6) | #1 | 6 | 2 | GNR 0.79<br>type 0.50<br>expr 0.59<br>cf 0.75<br>art 0 | 7312ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.528 | 100.0% (6/6) | #1 | 0 | 4 | GNR 0.00<br>type 0.50<br>expr 0.79<br>cf 1.00<br>art 0 | 8868ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.238 | 100.0% (6/6) | #1 | 0 | 4 | GNR 0.17<br>type 0.50<br>expr 0.73<br>cf 1.00<br>art 0 | 8968ms | ✅ |
| fission | clang -O0 | 1.000 | 0.033 | 100.0% (6/6) | #1 | 9 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9957ms | ✅ |
| ghidra | clang -O0 | 1.000 | 0.398 | 100.0% (6/6) | #1 | 0 | 4 | GNR 0.17<br>type 0.50<br>expr 0.76<br>cf 1.00<br>art 0 | 8561ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.048 | 100.0% (6/6) | #1 | 3 | 8 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 43 | 8925ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.269 | 0.0% (0/6) | #2 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 14 | 6521ms | 🟠 runtime |
| fission | gcc -O2 | 0.000 | 0.070 | 0.0% (0/6) | #2 | 3 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 8157ms | 🔴 compile |
| fission | gcc-m32 -O2 | 0.000 | 0.064 | 0.0% (0/6) | #2 | 3 | 3 | GNR 0.48<br>type 0.50<br>expr 0.43<br>cf 1.00<br>art 0 | 7586ms | 🔴 compile |
| fission | clang -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 16155ms | ❌ Decompiler returned whole-prog |

### `pointer_stride_sum` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 1.000 | 0.097 | 100.0% (5/5) | #1 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9561ms | ✅ |
| fission | gcc -O2 | 1.000 | 0.139 | 100.0% (5/5) | #1 | 1 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 9588ms | ✅ |
| ghidra | gcc -O2 | 1.000 | 0.609 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.29<br>type 0.50<br>expr 0.82<br>cf 1.00<br>art 0 | 10763ms | ✅ |
| fission | gcc-m32 -O0 | 1.000 | 0.347 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.64<br>type 0.50<br>expr 0.67<br>cf 1.00<br>art 0 | 4977ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.674 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.00<br>type 0.50<br>expr 0.86<br>cf 1.00<br>art 0 | 5723ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.648 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.29<br>type 0.50<br>expr 0.82<br>cf 1.00<br>art 0 | 8959ms | ✅ |
| fission | clang -O0 | 1.000 | 0.086 | 100.0% (5/5) | #1 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10111ms | ✅ |
| ghidra | clang -O0 | 1.000 | 0.489 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.00<br>type 0.50<br>expr 0.86<br>cf 1.00<br>art 0 | 9867ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.079 | 100.0% (5/5) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 10063ms | ✅ |
| fission | gcc-m32 -O2 | 0.200 | 0.240 | 20.0% (1/5) | #2 | 1 | 3 | GNR 0.32<br>type 0.50<br>expr 0.74<br>cf 1.00<br>art 0 | 8431ms | 🟤 assert |
| ghidra | gcc -O0 | 0.000 | 0.259 | 0.0% (0/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 5 | 11208ms | 🟠 runtime |
| fission | clang -O2 | n/a | 0.000 | n/a | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: ReadTim |

### `power` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 1.000 | 0.143 | 100.0% (6/6) | #1 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 9593ms | ✅ |
| fission | gcc -O2 | 1.000 | 0.225 | 100.0% (6/6) | #1 | 1 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 8452ms | ✅ |
| ghidra | gcc -O2 | 1.000 | 0.392 | 100.0% (6/6) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 8426ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.492 | 100.0% (6/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 8292ms | ✅ |
| fission | clang -O0 | 1.000 | 0.157 | 100.0% (6/6) | #1 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9350ms | ✅ |
| fission | clang -O2 | 1.000 | 0.218 | 100.0% (6/6) | #1 | 2 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 9424ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.264 | 100.0% (6/6) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 7615ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.374 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 4 | 8870ms | 🟤 assert |
| fission | gcc-m32 -O0 | 0.000 | 0.040 | 0.0% (0/6) | #2 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 7828ms | 🔴 compile |
| fission | gcc-m32 -O2 | 0.000 | 0.061 | 0.0% (0/6) | #1 | 1 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 7952ms | 🔴 compile |
| ghidra | gcc-m32 -O2 | 0.000 | 0.249 | 0.0% (0/6) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 7541ms | 🔴 compile |
| ghidra | clang -O0 | 0.000 | 0.215 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 1 | 9212ms | 🔴 compile |

### `process_code` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 1.000 | 0.090 | 100.0% (5/5) | #1 | 5 | 2 | GNR 0.90<br>type 0.50<br>expr 0.47<br>cf 1.00<br>art 0 | 9593ms | ✅ |
| fission | gcc -O2 | 1.000 | 0.130 | 100.0% (5/5) | #1 | 0 | 4 | GNR 0.83<br>type 0.50<br>expr 0.54<br>cf 1.00<br>art 0 | 8452ms | ✅ |
| ghidra | gcc -O2 | 1.000 | 0.286 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.50<br>type 0.50<br>expr 0.70<br>cf 1.00<br>art 0 | 8426ms | ✅ |
| fission | gcc-m32 -O0 | 1.000 | 0.106 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.89<br>type 0.50<br>expr 0.85<br>cf 1.00<br>art 0 | 7828ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.166 | 100.0% (5/5) | #1 | 0 | 4 | GNR 0.44<br>type 0.50<br>expr 0.80<br>cf 1.00<br>art 0 | 8292ms | ✅ |
| fission | gcc-m32 -O2 | 1.000 | 0.065 | 100.0% (5/5) | #1 | 0 | 5 | GNR 0.19<br>type 0.50<br>expr 0.69<br>cf 1.00<br>art 0 | 7952ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.286 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.50<br>type 0.50<br>expr 0.70<br>cf 1.00<br>art 0 | 7541ms | ✅ |
| ghidra | clang -O0 | 1.000 | 0.149 | 100.0% (5/5) | #1 | 0 | 4 | GNR 0.41<br>type 0.38<br>expr 0.80<br>cf 1.00<br>art 1 | 9212ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.309 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.50<br>type 0.50<br>expr 0.74<br>cf 1.00<br>art 0 | 7615ms | ✅ |
| fission | clang -O2 | 0.800 | 0.085 | 80.0% (4/5) | #2 | 4 | 2 | GNR 0.28<br>type 0.50<br>expr 0.73<br>cf 1.00<br>art 0 | 9424ms | 🟤 assert |
| ghidra | gcc -O0 | 0.200 | 0.157 | 20.0% (1/5) | #2 | 0 | 4 | GNR 0.88<br>type 0.50<br>expr 0.77<br>cf 1.00<br>art 8 | 8870ms | 🟤 assert |
| fission | clang -O0 | 0.000 | 0.099 | 0.0% (0/5) | #2 | 5 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 9350ms | 🔴 compile |

### `rc4_crypt` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 1.000 | 0.013 | 100.0% (5/5) | #1 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 23524ms | ✅ |
| fission | gcc -O2 | 1.000 | 0.028 | 100.0% (5/5) | #1 | 1 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 21731ms | ✅ |
| ghidra | gcc -O2 | 1.000 | 0.234 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.44<br>type 0.50<br>expr 0.62<br>cf 1.00<br>art 0 | 13994ms | ✅ |
| fission | gcc-m32 -O0 | 1.000 | 0.029 | 100.0% (5/5) | #1 | 2 | 2 | GNR 0.53<br>type 0.50<br>expr 0.38<br>cf 1.00<br>art 0 | 12140ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.440 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.10<br>type 0.50<br>expr 0.65<br>cf 1.00<br>art 0 | 15661ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.247 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.57<br>type 0.50<br>expr 0.60<br>cf 1.00<br>art 0 | 15848ms | ✅ |
| fission | clang -O0 | 1.000 | 0.044 | 100.0% (5/5) | #1 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9806ms | ✅ |
| ghidra | clang -O0 | 1.000 | 0.384 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.09<br>type 0.50<br>expr 0.62<br>cf 1.00<br>art 0 | 17119ms | ✅ |
| fission | clang -O2 | 1.000 | 0.062 | 100.0% (5/5) | #1 | 1 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 29124ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.162 | 100.0% (5/5) | #1 | 0 | 4 | GNR 0.75<br>type 0.50<br>expr 0.47<br>cf 1.00<br>art 0 | 18789ms | ✅ |
| fission | gcc-m32 -O2 | 0.200 | 0.053 | 20.0% (1/5) | #2 | 2 | 2 | GNR 0.40<br>type 0.50<br>expr 0.42<br>cf 0.50<br>art 0 | 7601ms | 🟤 assert |
| ghidra | gcc -O0 | 0.000 | 0.292 | 0.0% (0/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 17 | 15586ms | 🟠 runtime |

### `rc4_init` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 1.000 | 0.047 | 100.0% (5/5) | #1 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 23524ms | ✅ |
| fission | gcc-m32 -O0 | 1.000 | 0.033 | 100.0% (5/5) | #1 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 12140ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.544 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.11<br>type 0.50<br>expr 0.65<br>cf 1.00<br>art 0 | 15661ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.233 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.69<br>type 0.50<br>expr 0.61<br>cf 1.00<br>art 0 | 15848ms | ✅ |
| fission | clang -O0 | 1.000 | 0.051 | 100.0% (5/5) | #1 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9806ms | ✅ |
| ghidra | clang -O0 | 1.000 | 0.236 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.24<br>type 0.50<br>expr 0.63<br>cf 1.00<br>art 0 | 17119ms | ✅ |
| ghidra | gcc -O0 | 0.000 | 0.362 | 0.0% (0/5) | #2 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 14 | 15586ms | 🟠 runtime |
| fission | gcc -O2 | 0.000 | 0.017 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 21731ms | 🔴 compile |
| ghidra | gcc -O2 | 0.000 | 0.000 | 0.0% | — | 0 | 0 | — | 13994ms | ❌ Decompiler returned whole-prog |
| fission | gcc-m32 -O2 | 0.000 | 0.112 | 0.0% (0/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 7601ms | 🟠 runtime |
| fission | clang -O2 | 0.000 | 0.044 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 29124ms | 🔴 compile |
| ghidra | clang -O2 | 0.000 | 0.081 | 0.0% (0/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 33 | 18789ms | 🔴 compile |

### `reverse_in_place` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 1.000 | 0.051 | 100.0% (5/5) | #1 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9561ms | ✅ |
| ghidra | gcc -O0 | 1.000 | 0.323 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.60<br>type 0.50<br>expr 0.71<br>cf 1.00<br>art 11 | 11208ms | ✅ |
| ghidra | gcc -O2 | 1.000 | 0.221 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.10<br>type 0.50<br>expr 0.76<br>cf 1.00<br>art 0 | 10763ms | ✅ |
| fission | gcc-m32 -O0 | 1.000 | 0.074 | 100.0% (5/5) | #1 | 2 | 2 | GNR 0.38<br>type 0.50<br>expr 0.39<br>cf 0.50<br>art 0 | 4977ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.339 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.25<br>type 0.50<br>expr 0.77<br>cf 1.00<br>art 0 | 5723ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.221 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.10<br>type 0.50<br>expr 0.76<br>cf 1.00<br>art 0 | 8959ms | ✅ |
| fission | clang -O0 | 1.000 | 0.073 | 100.0% (5/5) | #1 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10111ms | ✅ |
| ghidra | clang -O0 | 1.000 | 0.325 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.26<br>type 0.50<br>expr 0.78<br>cf 1.00<br>art 0 | 9867ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.146 | 100.0% (5/5) | #1 | 0 | 4 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 10063ms | ✅ |
| fission | gcc -O2 | 0.000 | 0.121 | 0.0% (0/5) | #2 | 2 | 3 | GNR 0.32<br>type 0.50<br>expr 0.66<br>cf 0.75<br>art 0 | 9588ms | 🟠 runtime |
| fission | gcc-m32 -O2 | 0.000 | 0.126 | 0.0% (0/5) | #2 | 2 | 3 | GNR 0.29<br>type 0.50<br>expr 0.66<br>cf 0.75<br>art 0 | 8431ms | 🟠 runtime |
| fission | clang -O2 | n/a | 0.000 | n/a | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: ReadTim |

### `reverse_string` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 1.000 | 0.073 | 100.0% (5/5) | #1 | 3 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 27050ms | ✅ |
| ghidra | gcc -O0 | 1.000 | 0.251 | 100.0% (5/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 6 | 27516ms | ✅ |
| ghidra | gcc -O2 | 1.000 | 0.233 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.10<br>type 0.50<br>expr 0.75<br>cf 1.00<br>art 0 | 29360ms | ✅ |
| fission | gcc-m32 -O0 | 1.000 | 0.057 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.56<br>type 0.50<br>expr 0.55<br>cf 1.00<br>art 0 | 11293ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.353 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.16<br>type 0.50<br>expr 0.78<br>cf 1.00<br>art 0 | 28155ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.263 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.10<br>type 0.50<br>expr 0.77<br>cf 1.00<br>art 0 | 28725ms | ✅ |
| ghidra | clang -O0 | 1.000 | 0.256 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.14<br>type 0.50<br>expr 0.80<br>cf 1.00<br>art 0 | 24865ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.252 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.12<br>type 0.50<br>expr 0.77<br>cf 1.00<br>art 0 | 18330ms | ✅ |
| fission | gcc -O2 | 0.000 | 0.132 | 0.0% (0/5) | #2 | 2 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 11479ms | 🔴 compile |
| fission | gcc-m32 -O2 | 0.000 | 0.038 | 0.0% (0/5) | #2 | 3 | 2 | GNR 0.16<br>type 0.50<br>expr 0.64<br>cf 0.50<br>art 0 | 11680ms | 🔴 compile |
| fission | clang -O0 | 0.000 | 0.076 | 0.0% (0/5) | #2 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 13776ms | 🟠 runtime |
| fission | clang -O2 | 0.000 | 0.062 | 0.0% (0/5) | #2 | 2 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 12719ms | 🟠 runtime |

### `rolling_hash32` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 1.000 | 0.127 | 100.0% (6/6) | #1 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 8586ms | ✅ |
| ghidra | gcc -O0 | 1.000 | 0.414 | 100.0% (6/6) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 4 | 6521ms | ✅ |
| fission | gcc -O2 | 1.000 | 0.193 | 100.0% (6/6) | #1 | 1 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 8157ms | ✅ |
| ghidra | gcc -O2 | 1.000 | 0.303 | 100.0% (6/6) | #1 | 0 | 3 | GNR 0.38<br>type 0.50<br>expr 0.75<br>cf 1.00<br>art 0 | 9494ms | ✅ |
| fission | gcc-m32 -O0 | 1.000 | 0.123 | 100.0% (6/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 7312ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.783 | 100.0% (6/6) | #1 | 0 | 2 | GNR 0.00<br>type 0.50<br>expr 0.82<br>cf 1.00<br>art 0 | 8868ms | ✅ |
| fission | gcc-m32 -O2 | 1.000 | 0.181 | 100.0% (6/6) | #1 | 1 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 7586ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.303 | 100.0% (6/6) | #1 | 0 | 3 | GNR 0.38<br>type 0.50<br>expr 0.75<br>cf 1.00<br>art 0 | 8968ms | ✅ |
| ghidra | clang -O0 | 1.000 | 0.558 | 100.0% (6/6) | #1 | 0 | 2 | GNR 0.00<br>type 0.50<br>expr 0.82<br>cf 1.00<br>art 0 | 8561ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.340 | 100.0% (6/6) | #1 | 0 | 4 | GNR 0.64<br>type 0.50<br>expr 0.60<br>cf 1.00<br>art 0 | 8925ms | ✅ |
| fission | clang -O0 | 0.167 | 0.092 | 16.7% (1/6) | #2 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9957ms | 🟤 assert |
| fission | clang -O2 | 0.000 | 0.086 | 0.0% (0/6) | #2 | 3 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 16155ms | 🟠 runtime |

### `rotate_words` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| ghidra | gcc -O2 | 1.000 | 0.217 | 100.0% (6/6) | #1 | 0 | 3 | GNR 0.46<br>type 0.50<br>expr 0.66<br>cf 1.00<br>art 0 | 9494ms | ✅ |
| fission | gcc-m32 -O2 | 1.000 | 0.037 | 100.0% (6/6) | #1 | 1 | 3 | GNR 0.14<br>type 0.50<br>expr 0.63<br>cf 1.00<br>art 0 | 7586ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.213 | 100.0% (6/6) | #1 | 0 | 3 | GNR 0.44<br>type 0.50<br>expr 0.68<br>cf 1.00<br>art 0 | 8968ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.152 | 100.0% (6/6) | #1 | 0 | 4 | GNR 0.72<br>type 0.50<br>expr 0.47<br>cf 1.00<br>art 0 | 8925ms | ✅ |
| fission | gcc -O2 | 0.833 | 0.135 | 83.3% (5/6) | #2 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 8157ms | 🟤 assert |
| fission | gcc -O0 | 0.500 | 0.067 | 50.0% (3/6) | #1 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 8586ms | 🟤 assert |
| fission | clang -O2 | 0.500 | 0.068 | 50.0% (3/6) | #2 | 4 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 16155ms | 🟤 assert |
| fission | clang -O0 | 0.333 | 0.044 | 33.3% (2/6) | #1 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9957ms | 🟤 assert |
| ghidra | gcc -O0 | 0.000 | 0.337 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 5 | 6521ms | 🟠 runtime |
| fission | gcc-m32 -O0 | 0.000 | 0.066 | 0.0% (0/6) ⚠️intrin | #1 | 0 | 4 | GNR 0.29<br>type 0.50<br>expr 0.40<br>cf 1.00<br>art 3 | 7312ms | 🔴 compile |
| ghidra | gcc-m32 -O0 | 0.000 | 0.398 | 0.0% (0/6) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 8868ms | 🔴 compile |
| ghidra | clang -O0 | 0.000 | 0.344 | 0.0% (0/6) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 8561ms | 🔴 compile |

### `saturating_add` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 1.000 | 0.100 | 100.0% (5/5) | #1 | 6 | 2 | GNR 0.24<br>type 0.50<br>expr 0.67<br>cf 0.75<br>art 0 | 7363ms | ✅ |
| ghidra | gcc -O2 | 1.000 | 0.606 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.40<br>type 0.50<br>expr 0.81<br>cf 1.00<br>art 0 | 11998ms | ✅ |
| fission | gcc-m32 -O0 | 1.000 | 0.168 | 100.0% (5/5) | #1 | 0 | 6 | GNR 0.19<br>type 0.50<br>expr 0.62<br>cf 1.00<br>art 0 | 6485ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.246 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.47<br>type 0.50<br>expr 0.80<br>cf 1.00<br>art 0 | 10412ms | ✅ |
| fission | gcc-m32 -O2 | 1.000 | 0.121 | 100.0% (5/5) ⚠️intrin | #1 | 0 | 5 | GNR 0.24<br>type 0.50<br>expr 0.59<br>cf 1.00<br>art 3 | 4437ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.606 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.40<br>type 0.50<br>expr 0.81<br>cf 1.00<br>art 0 | 10298ms | ✅ |
| fission | clang -O0 | 1.000 | 0.106 | 100.0% (5/5) | #1 | 6 | 2 | GNR 0.28<br>type 0.50<br>expr 0.68<br>cf 0.75<br>art 0 | 6712ms | ✅ |
| ghidra | clang -O0 | 1.000 | 0.315 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.42<br>type 0.50<br>expr 0.81<br>cf 1.00<br>art 0 | 8750ms | ✅ |
| fission | gcc -O2 | 0.800 | 0.349 | 80.0% (4/5) | #2 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 7052ms | 🟤 assert |
| ghidra | gcc -O0 | 0.000 | 0.252 | 0.0% (0/5) | #2 | 0 | 3 | GNR 0.84<br>type 0.50<br>expr 0.76<br>cf 1.00<br>art 8 | 12265ms | 🟤 assert |
| fission | clang -O2 | 0.000 | 0.396 | 0.0% (0/5) | #1 | 0 | 1 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 7644ms | ❌ |
| ghidra | clang -O2 | 0.000 | 0.432 | 0.0% (0/5) | #1 | 0 | 1 | GNR 0.00<br>type 0.50<br>expr 0.93<br>cf 1.00<br>art 0 | 9138ms | ❌ |

### `signum` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 1.000 | 0.104 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.31<br>type 0.50<br>expr 0.80<br>cf 1.00<br>art 0 | 7363ms | ✅ |
| fission | gcc -O2 | 1.000 | 0.125 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.06<br>type 0.50<br>expr 0.69<br>cf 1.00<br>art 0 | 7052ms | ✅ |
| ghidra | gcc -O2 | 1.000 | 0.492 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.50<br>type 0.50<br>expr 0.77<br>cf 1.00<br>art 0 | 11998ms | ✅ |
| fission | gcc-m32 -O0 | 1.000 | 0.529 | 100.0% (5/5) | #1 | 0 | 4 | GNR 0.75<br>type 0.50<br>expr 0.75<br>cf 1.00<br>art 0 | 6485ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.611 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.56<br>type 0.50<br>expr 0.86<br>cf 1.00<br>art 0 | 10412ms | ✅ |
| fission | gcc-m32 -O2 | 1.000 | 0.419 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.25<br>type 0.50<br>expr 0.82<br>cf 1.00<br>art 0 | 4437ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.583 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.00<br>type 0.50<br>expr 0.84<br>cf 1.00<br>art 0 | 10298ms | ✅ |
| ghidra | clang -O0 | 1.000 | 0.523 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.50<br>type 0.38<br>expr 0.87<br>cf 1.00<br>art 1 | 8750ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.624 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.50<br>type 0.50<br>expr 0.86<br>cf 1.00<br>art 0 | 9138ms | ✅ |
| fission | clang -O2 | 0.600 | 0.121 | 60.0% (3/5) | #2 | 0 | 2 | GNR 0.13<br>type 0.50<br>expr 0.77<br>cf 1.00<br>art 0 | 7644ms | 🟤 assert |
| ghidra | gcc -O0 | 0.400 | 0.375 | 40.0% (2/5) | #2 | 0 | 3 | GNR 0.80<br>type 0.50<br>expr 0.85<br>cf 1.00<br>art 3 | 12265ms | 🟤 assert |
| fission | clang -O0 | 0.000 | 0.069 | 0.0% (0/5) | #2 | 4 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 6712ms | 🔴 compile |

### `state_machine_score` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 1.000 | 0.046 | 100.0% (7/7) | #1 | 19 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 8586ms | ✅ |
| ghidra | gcc -O0 | 1.000 | 0.107 | 100.0% (7/7) | #1 | 2 | 6 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 5 | 6521ms | ✅ |
| ghidra | gcc -O2 | 1.000 | 0.125 | 100.0% (7/7) | #1 | 0 | 5 | GNR 0.72<br>type 0.50<br>expr 0.61<br>cf 0.87<br>art 0 | 9494ms | ✅ |
| fission | gcc-m32 -O0 | 1.000 | 0.050 | 100.0% (7/7) | #1 | 19 | 2 | GNR 0.60<br>type 0.50<br>expr 0.57<br>cf 0.37<br>art 0 | 7312ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.117 | 100.0% (7/7) | #1 | 2 | 6 | GNR 0.16<br>type 0.50<br>expr 0.66<br>cf 0.52<br>art 0 | 8868ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.125 | 100.0% (7/7) | #1 | 0 | 5 | GNR 0.72<br>type 0.50<br>expr 0.61<br>cf 0.87<br>art 0 | 8968ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.237 | 100.0% (7/7) | #1 | 2 | 5 | GNR 0.74<br>type 0.50<br>expr 0.56<br>cf 0.48<br>art 0 | 8925ms | ✅ |
| fission | gcc-m32 -O2 | 0.143 | 0.085 | 14.3% (1/7) | #2 | 17 | 2 | GNR 0.12<br>type 0.50<br>expr 0.60<br>cf 0.39<br>art 0 | 7586ms | 🟤 assert |
| fission | gcc -O2 | 0.000 | 0.055 | 0.0% (0/7) | #2 | 17 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 8157ms | 🔴 compile |
| fission | clang -O0 | 0.000 | 0.030 | 0.0% (0/7) | #1 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 9957ms | 🟠 runtime |
| ghidra | clang -O0 | 0.000 | 0.146 | 0.0% (0/7) | #1 | 0 | 4 | GNR 0.11<br>type 0.50<br>expr 0.58<br>cf 0.67<br>art 0 | 8561ms | 🔴 compile |
| fission | clang -O2 | 0.000 | 0.072 | 0.0% (0/7) | #2 | 5 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 16155ms | 🟠 runtime |

### `sum_array` 🟢 Fission leads
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O0 | 1.000 | 0.105 | 100.0% (5/5) | #1 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 9561ms | ✅ |
| ghidra | gcc -O0 | 1.000 | 0.648 | 100.0% (5/5) | #1 | 0 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 4 | 11208ms | ✅ |
| fission | gcc -O2 | 1.000 | 0.087 | 100.0% (5/5) | #1 | 1 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 9588ms | ✅ |
| ghidra | gcc -O2 | 1.000 | 0.171 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.28<br>type 0.50<br>expr 0.83<br>cf 1.00<br>art 0 | 10763ms | ✅ |
| fission | gcc-m32 -O0 | 1.000 | 0.225 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.68<br>type 0.50<br>expr 0.57<br>cf 1.00<br>art 0 | 4977ms | ✅ |
| ghidra | gcc-m32 -O0 | 1.000 | 0.833 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.00<br>type 0.50<br>expr 0.88<br>cf 1.00<br>art 0 | 5723ms | ✅ |
| ghidra | gcc-m32 -O2 | 1.000 | 0.171 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.28<br>type 0.50<br>expr 0.83<br>cf 1.00<br>art 0 | 8959ms | ✅ |
| fission | clang -O0 | 1.000 | 0.095 | 100.0% (5/5) | #1 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 10111ms | ✅ |
| ghidra | clang -O0 | 1.000 | 0.733 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.00<br>type 0.50<br>expr 0.88<br>cf 1.00<br>art 0 | 9867ms | ✅ |
| ghidra | clang -O2 | 1.000 | 0.030 | 100.0% (5/5) | #1 | 0 | 5 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 10063ms | ✅ |
| fission | gcc-m32 -O2 | 0.000 | 0.135 | 0.0% (0/5) | #2 | 0 | 3 | GNR 0.25<br>type 0.50<br>expr 0.83<br>cf 1.00<br>art 0 | 8431ms | 🟡 timeout |
| fission | clang -O2 | n/a | 0.000 | n/a | — | 0 | 0 | — | 0ms | ❌ Batch decompile error: ReadTim |

---

## Overfitting Analysis

Functions where **all** decompilers scored below 0.3 are marked as objectively hard.
Functions where **only Fission** scored below 0.3 are marked as quality gaps.

**Fission quality gaps (1):** `bubble_sort`