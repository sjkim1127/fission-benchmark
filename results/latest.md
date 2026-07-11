# Fission Benchmark Report

**Generated:** 2026-07-10 14:51 UTC
**Corpus:** `dev`
**Functions evaluated:** 6

---

## Summary — Correctness Score

> Readability metrics are recorded as unvalidated raw proxies. They are not combined into a final readability score until the human validation study is complete.

| Decompiler | Correctness | Similarity | Semantic Pass | Functions |
| ---|---|---|---|--- |
| **fission** | 0.779 | 0.192 | 86.0% | 24 |

---

## Per-Function Results

### `checksum`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O2 | 0.898 | 0.081 | 100.0% (5/5) | #1 | 0 | 3 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 1.00<br>art 0 | 720ms | ✅ |
| fission | gcc-m32 -O2 | 0.106 | 0.164 | 0.0% (0/5) | #1 | 0 | 3 | GNR 0.23<br>type 0.50<br>expr 0.68<br>cf 1.00<br>art 0 | 655ms | 🟠 runtime |
| fission | gcc-m32 -O0 | 0.102 | 0.122 | 0.0% (0/5) | #1 | 0 | 3 | GNR 0.42<br>type 0.50<br>expr 0.57<br>cf 1.00<br>art 0 | 649ms | 🔴 compile |
| fission | gcc -O0 | 0.083 | 0.108 | 0.0% (0/5) | #1 | 2 | 2 | GNR 1.00<br>type 0.00<br>expr 0.00<br>cf 0.00<br>art 0 | 790ms | 🔴 compile |

### `clamp`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc-m32 -O2 | 0.901 | 0.110 | 100.0% (6/6) ⚠️intrin | #1 | 0 | 2 | GNR 0.13<br>type 0.50<br>expr 0.74<br>cf 1.00<br>art 2 | 655ms | ✅ |
| fission | gcc-m32 -O0 | 0.880 | 0.097 | 100.0% (6/6) | #1 | 0 | 4 | GNR 0.59<br>type 0.50<br>expr 0.86<br>cf 1.00<br>art 0 | 649ms | ✅ |
| fission | gcc -O0 | 0.844 | 0.098 | 100.0% (6/6) | #1 | 4 | 2 | GNR 0.66<br>type 0.50<br>expr 0.80<br>cf 0.33<br>art 0 | 790ms | ✅ |
| fission | gcc -O2 | 0.809 | 0.423 | 83.3% (5/6) | #1 | 0 | 1 | GNR 0.64<br>type 0.50<br>expr 0.74<br>cf 1.00<br>art 0 | 720ms | 🟠 runtime |

### `classify_range`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc-m32 -O2 | 0.888 | 0.079 | 100.0% (5/5) | #1 | 0 | 4 | GNR 0.05<br>type 0.50<br>expr 0.59<br>cf 1.00<br>art 0 | 655ms | ✅ |
| fission | gcc -O0 | 0.837 | 0.073 | 100.0% (5/5) | #1 | 11 | 2 | GNR 0.38<br>type 0.50<br>expr 0.81<br>cf 0.35<br>art 0 | 790ms | ✅ |
| fission | gcc-m32 -O0 | 0.829 | 0.091 | 100.0% (5/5) | #1 | 5 | 3 | GNR 0.50<br>type 0.50<br>expr 0.86<br>cf 0.55<br>art 0 | 649ms | ✅ |
| fission | gcc -O2 | 0.734 | 0.137 | 80.0% (4/5) | #1 | 0 | 4 | GNR 0.04<br>type 0.50<br>expr 0.64<br>cf 1.00<br>art 0 | 720ms | 🟠 runtime |

### `count_bits`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc-m32 -O0 | 0.940 | 0.498 | 100.0% (6/6) | #1 | 0 | 3 | GNR 0.53<br>type 0.50<br>expr 0.85<br>cf 1.00<br>art 0 | 649ms | ✅ |
| fission | gcc -O2 | 0.916 | 0.260 | 100.0% (6/6) | #1 | 0 | 3 | GNR 0.33<br>type 0.50<br>expr 0.78<br>cf 1.00<br>art 0 | 720ms | ✅ |
| fission | gcc-m32 -O2 | 0.914 | 0.241 | 100.0% (6/6) | #1 | 0 | 3 | GNR 0.32<br>type 0.50<br>expr 0.86<br>cf 1.00<br>art 0 | 655ms | ✅ |
| fission | gcc -O0 | 0.891 | 0.192 | 100.0% (6/6) | #1 | 2 | 2 | GNR 0.61<br>type 0.50<br>expr 0.84<br>cf 0.33<br>art 0 | 790ms | ✅ |

### `saturating_add`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc -O2 | 0.886 | 0.160 | 100.0% (5/5) ⚠️intrin | #1 | 0 | 5 | GNR 0.31<br>type 0.50<br>expr 0.51<br>cf 1.00<br>art 3 | 720ms | ✅ |
| fission | gcc-m32 -O0 | 0.885 | 0.149 | 100.0% (5/5) | #1 | 0 | 6 | GNR 0.35<br>type 0.50<br>expr 0.73<br>cf 1.00<br>art 0 | 649ms | ✅ |
| fission | gcc-m32 -O2 | 0.883 | 0.126 | 100.0% (5/5) ⚠️intrin | #1 | 0 | 5 | GNR 0.26<br>type 0.50<br>expr 0.57<br>cf 1.00<br>art 3 | 655ms | ✅ |
| fission | gcc -O0 | 0.841 | 0.212 | 100.0% (5/5) | #1 | 6 | 2 | GNR 0.37<br>type 0.50<br>expr 0.72<br>cf 0.40<br>art 0 | 790ms | ✅ |

### `signum`
| Decompiler | Variant | Correctness | Similarity | Semantic | Correctness Rank | Gotos | Depth | Readability Proxies | Time | Status |
| ---|---|---|---|---|---|---|---|---|---|--- |
| fission | gcc-m32 -O0 | 0.925 | 0.554 | 100.0% (5/5) | #1 | 0 | 4 | GNR 0.38<br>type 0.50<br>expr 0.89<br>cf 1.00<br>art 0 | 649ms | ✅ |
| fission | gcc-m32 -O2 | 0.921 | 0.407 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.18<br>type 0.50<br>expr 0.85<br>cf 1.00<br>art 0 | 655ms | ✅ |
| fission | gcc -O2 | 0.902 | 0.120 | 100.0% (5/5) | #1 | 0 | 2 | GNR 0.06<br>type 0.50<br>expr 0.71<br>cf 1.00<br>art 0 | 720ms | ✅ |
| fission | gcc -O0 | 0.890 | 0.104 | 100.0% (5/5) | #1 | 0 | 3 | GNR 0.32<br>type 0.50<br>expr 0.77<br>cf 1.00<br>art 0 | 790ms | ✅ |

---

## Overfitting Analysis

Functions where **all** decompilers scored below 0.3 are marked as objectively hard.
Functions where **only Fission** scored below 0.3 are marked as quality gaps.

✅ No significant quality gaps detected.