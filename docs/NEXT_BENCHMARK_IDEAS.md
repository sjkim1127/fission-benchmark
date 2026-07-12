# Next benchmark ideas (integrated workspace)

This repo is not “decompiler output vs source only.” It is a **multi-layer measurement
workspace**. Below are high-value next axes, ordered by leverage for Fission
engineering and scientific honesty.

## Near-term (fits existing infrastructure)

### 1. Calling-convention / ABI surface parity
- **What:** Recovered parameter locations (RCX/RDX/stack) and return register vs Ghidra.
- **Why:** Semantic oracle already compiles; many failures are ABI, not control flow.
- **How:** Extend adapter `/abi` export; compare normalized parameter lists.

### 2. Type recovery differential
- **What:** Struct/layout and primitive widths recovered at function boundaries.
- **Why:** Orthogonal to CFG; huge RE productivity impact.
- **How:** Ghidra DataType JSON vs Fission NIR type table; score field-level IoU.

### 3. Data-flow / def-use slice canaries
- **What:** For selected sinks (return, store), compare def-use chains.
- **Why:** Catches “looks like CFG match but wrong value” without full semantic tests.
- **How:** Small golden programs + required SSA edges in golden_repros.

### 4. Strip / no-symbol track (realworld extension)
- **What:** Same sources built with `strip`; measure function discovery + semantic drop.
- **Why:** Dev corpus currently has symbols; real RE does not.
- **How:** `corpus/realworld/` + compiler flags; report discovery Δ vs unstripped.

### 5. Optimization cliff matrix
- **What:** Per-function semantic/CFG match rate O0→O2→O3 as a heat-map.
- **Why:** Already have cross-variant data; productize as first-class extension panel.
- **How:** Pivot `summary.extensions.cross_variant` + parity telemetry by opt.

## Medium-term

### 6. Inter-procedural / call-graph parity
- **What:** Callee sets and call-site counts vs Ghidra/radare.
- **Why:** Whole-program tools (rev.ng) need a fair axis beyond single-function decomp.

### 7. Exception / SEH / unwind recovery (Windows PE)
- **What:** Personality routines, unwind codes, try/except regions.
- **Why:** Corpus is PE-heavy; few open benchmarks cover this.

### 8. Constant / string / switch recovery
- **What:** Recovered string xrefs and jump-table shapes.
- **Why:** Highly visible RE features; easy golden canaries.

### 9. Throughput & resource budget
- **What:** p50/p95 decompile and parity export times under fixed RAM.
- **Why:** Correctness without budgets is not a product metric.

### 10. Differential patch impact (CI for Fission PRs)
- **What:** Before/after semantic + parity deltas on a fixed canary set.
- **Why:** Prevents “fix one, break three” without full official runs.
- **How:** Graphite/PR workflow runs `golden_repros` + `run_parity --limit 20`.

## Longer-term / research

### 11. Human readability study (Phase 3)
- Already scaffolded under `benchmark/readability/`.
- Do not invent a composite readability score until correlations land.

### 12. Adversarial / obfuscation suite
- Control-flow flattening, MBA, virtualization — separate track, not default gate.

### 13. Multi-ISA track
- arm64/ELF once Windows PE path is publishable; keep oracle ABI matrix explicit.

### 14. Binary-diff assisted ground truth
- Use compiler IR or DWARF (when present) as intermediate truth for CFG/types,
  still validating against original PE for semantics.

## Design rules for any new axis

1. **Own a stage name** and JSONL under `results/<stage>/`.
2. Prefer **Ghidra (or stronger) reference** for structural layers; **original binary** for semantics.
3. Separate **infra failure** from **quality mismatch** (see `check_parity_smoke.py`).
4. Add **golden canaries** before expanding corpus breadth.
5. Dashboard shows **rates + denominators**, never a mystery composite.

## Suggested next implementation order

1. ~~Full-dev parity telemetry + conservative reliability gates~~ (in tree).
2. Grow `golden_repros` for every high-severity pcode/cfg residual gap.
3. Implement real adapter `/abi` exports (stage scaffold: `benchmark/abi_parity`).
4. Populate `corpus/realworld/` strip PE cases (stage scaffold: `benchmark/strip_track`).
5. PR-local differential canary workflow.
