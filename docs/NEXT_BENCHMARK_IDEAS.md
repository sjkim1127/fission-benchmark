# Next benchmark ideas (integrated workspace)

This repo is a **multi-layer measurement workspace**. Status below reflects
implementation as of the full extension pass (not only MVP semantic).

## Implemented (active)

| Track | Module / surface | Headline? |
|-------|------------------|-----------|
| Assembly / pcode / CFG / FD | `runner.run_parity` | Yes (strict dual metrics) |
| ABI | `abi_parity` + `/abi` | Extension |
| Type recovery (name-level) | `type_parity` + `/types` | Extension |
| Call-graph callees | `callgraph_parity` + `/callgraph` | Extension |
| String xrefs | `string_recovery` + `/strings` | Extension (Fission empty honest) |
| Data-flow sinks | `dataflow_parity` + `/dataflow` | Extension |
| SEH flags surface | `seh_parity` + `/seh` | Extension (flags-only) |
| Strip discovery + Δ | `strip_track` + `semantic_delta` | Extension |
| Opt cliff | `opt_cliff` from envelopes | Extension |
| Throughput p50/p95 | `throughput` | Extension |
| PR canary | `scripts/pr_canary.sh` | CI helper |
| Official publication | `publication_gate` | Release gate |
| Golden canaries | `golden_repros` | Meta locks |
| Readability proxies | `runner/readability.py` | Evidence only |
| Human study pack | `benchmark/readability/study_pack` | Scaffold for Phase 3 |

Unified extension runner:

```bash
python -m runner.run_extensions --corpus dev --limit 20
```

## Still deepening (not greenfield)

1. **Struct layout IoU** — type stage today is name/size tokens, not field-level.
2. **Full RUNTIME_FUNCTION / unwind** — SEH stage is flags + symbol counts.
3. **Fission string/xref product** — adapter returns empty until CLI emits xrefs.
4. **Third-party realworld corpus** — strip-from-dev is synthetic; external PE needs licenses/wrappers.
5. **Human readability Phase 3** — study pack exists; no composite until correlations.
6. **Multi-ISA (arm64/ELF)** — PE path first; oracle ABI matrix must expand explicitly.
7. **Obfuscation suite** — separate track (CFF/MBA), not default gate.
8. **Full 8-decompiler official** — publication proven on fission+ghidra core; expand profile.
9. **Golden growth** — add canaries for every high-severity residual gap.

## Design rules

1. Own a stage name and JSONL under `results/<stage>/`.
2. Ghidra (or stronger) for structural layers; **original binary** for semantics.
3. Separate infra failure from quality mismatch.
4. Golden canaries before corpus breadth.
5. Dashboard: rates + denominators, no mystery composite.
