"""
Report generation: JSON → Markdown → HTML (GitHub Pages dashboard).
"""
from __future__ import annotations

import json
import time
from collections import defaultdict
from pathlib import Path

from scoring import FunctionScore

RESULTS_DIR = Path(__file__).parent.parent / "results"
DOCS_DIR = Path(__file__).parent.parent / "docs"

DECOMPILER_COLORS = {
    "fission":  "#6366f1",
    "ghidra":   "#f59e0b",

    "boomerang": "#10b981",
    "radare2":  "#ef4444",
    "angr":     "#06b6d4",
    "snowman":  "#8b5cf6",
    "revng":    "#ec4899",
}


# ── Markdown ──────────────────────────────────────────────────────────────────

def _md_table(headers: list[str], rows: list[list[str]]) -> str:
    sep = "|".join(["---"] * len(headers))
    head = "| " + " | ".join(headers) + " |"
    lines = [head, f"| {sep} |"]
    for row in rows:
        lines.append("| " + " | ".join(str(c) for c in row) + " |")
    return "\n".join(lines)


def generate_markdown(scores: list[FunctionScore], corpus_split: str) -> str:
    ts = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())
    lines = [
        "# Fission Benchmark Report",
        "",
        f"**Generated:** {ts}  ",
        f"**Corpus:** `{corpus_split}`  ",
        f"**Functions evaluated:** {len(set(s.function_name for s in scores))}",
        "",
        "---",
        "",
        "## Summary — Average Source Similarity",
        "",
    ]

    # Per-decompiler average (ranked by composite_score)
    by_decomp_comp: dict[str, list[float]] = defaultdict(list)
    by_decomp_sim: dict[str, list[float]] = defaultdict(list)
    by_decomp_sem: dict[str, list[float]] = defaultdict(list)
    for s in scores:
        if s.error is None:
            by_decomp_comp[s.decompiler].append(getattr(s, "composite_score", 0.0))
            by_decomp_sim[s.decompiler].append(s.source_similarity)
            by_decomp_sem[s.decompiler].append(s.semantic_score)

    rows = []
    all_decomps = sorted(by_decomp_comp.keys(), key=lambda d: -(sum(by_decomp_comp[d]) / len(by_decomp_comp[d])))
    for d in all_decomps:
        comps = by_decomp_comp[d]
        sims = by_decomp_sim[d]
        sems = by_decomp_sem[d]
        avg_comp = sum(comps) / len(comps)
        avg_sim = sum(sims) / len(sims)
        avg_sem = sum(sems) / len(sems) if sems else 0.0
        rows.append([f"**{d}**", f"{avg_comp:.3f}", f"{avg_sim:.3f}", f"{avg_sem * 100:.1f}%", f"{len(comps)}"])
    lines.append(_md_table(["Decompiler", "Composite ⭐", "Similarity", "Semantic Pass", "Functions"], rows))
    lines += ["", "---", "", "## Per-Function Results", ""]

    # Per function
    by_fn: dict[str, list[FunctionScore]] = defaultdict(list)
    for s in scores:
        by_fn[s.function_name].append(s)

    for fn_name, fn_scores in sorted(by_fn.items()):
        lines.append(f"### `{fn_name}`")
        # Consensus badge for this function
        badge = ""
        fission_scores_fn = [s for s in fn_scores if s.decompiler == "fission" and s.error is None]
        other_scores_fn = [s for s in fn_scores if s.decompiler != "fission" and s.error is None]
        if fission_scores_fn and other_scores_fn:
            fn_comp = fission_scores_fn[0].composite_score if hasattr(fission_scores_fn[0], "composite_score") else 0.0
            others_avg = sum(getattr(s, "composite_score", 0.0) for s in other_scores_fn) / len(other_scores_fn)
            if fission_scores_fn[0].consensus_rank == 1:
                badge = " 🟢 Fission leads"
            elif fn_comp < 0.20 and others_avg > 0.40:
                badge = " 🔴 Fission-only gap"
            elif fn_comp < 0.20 and others_avg < 0.20:
                badge = " ⚪ Universally hard"
        lines[-1] = lines[-1] + badge

        rows = []
        for s in sorted(fn_scores, key=lambda x: -(getattr(x, "composite_score", 0.0))):
            rank = f"#{s.consensus_rank}" if s.consensus_rank else "—"
            fail_cat = getattr(s, "fail_category", "") or ""
            cat_icons = {
                "compile_error": "🔴 compile",
                "runtime_error": "🟠 runtime",
                "timeout": "🟡 timeout",
                "assertion_fail": "🟤 assert",
                "no_wrapper": "⚪ no_test",
                "": "✅" if not s.error else "❌",
            }
            status_icon = cat_icons.get(fail_cat, "❌")
            if s.error:
                status_icon = f"❌ {s.error[:30]}"
            sem_str = f"{s.semantic_score:.1%}"
            if hasattr(s, "cases_passed") and getattr(s, "cases_total", 0) > 0:
                sem_str = f"{s.semantic_score:.1%} ({s.cases_passed}/{s.cases_total})"
            intrin_flag = " ⚠️intrin" if getattr(s, "uses_intrinsics", False) else ""
            rows.append([
                s.decompiler, s.compiler_variant,
                f"{getattr(s, 'composite_score', 0.0):.3f}",
                f"{s.source_similarity:.3f}",
                sem_str + intrin_flag, rank,
                str(s.goto_count), str(s.nesting_depth),
                f"{s.time_ms}ms", status_icon,
            ])
        lines.append(_md_table(
            ["Decompiler", "Variant", "Composite ⭐", "Similarity", "Semantic", "Rank", "Gotos", "Depth", "Time", "Status"],
            rows,
        ))
        lines.append("")

    # Overfitting alert
    lines += [
        "---",
        "",
        "## Overfitting Analysis",
        "",
        "Functions where **all** decompilers scored below 0.3 are marked as objectively hard.",
        "Functions where **only Fission** scored below 0.3 are marked as quality gaps.",
        "",
    ]

    hard, gaps = [], []
    for fn_name, fn_scores in by_fn.items():
        valid = [s for s in fn_scores if s.error is None]
        if not valid:
            continue
        all_low = all(getattr(s, "composite_score", s.source_similarity) < 0.20 for s in valid)
        fission_scores = [s for s in valid if s.decompiler == "fission"]
        others_ok = any(getattr(s, "composite_score", s.source_similarity) >= 0.20 for s in valid if s.decompiler != "fission")
        fission_low = fission_scores and all(getattr(s, "composite_score", s.source_similarity) < 0.20 for s in fission_scores)

        if all_low:
            hard.append(fn_name)
        elif fission_low and others_ok:
            gaps.append(fn_name)

    if hard:
        lines.append(f"**Objectively hard functions ({len(hard)}):** " + ", ".join(f"`{f}`" for f in hard))
    if gaps:
        lines.append(f"**Fission quality gaps ({len(gaps)}):** " + ", ".join(f"`{f}`" for f in gaps))
    if not hard and not gaps:
        lines.append("✅ No significant quality gaps detected.")

    return "\n".join(lines)


# ── HTML (GitHub Pages) ───────────────────────────────────────────────────────


def generate_html(scores: list[FunctionScore], corpus_split: str) -> str:
    ts = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())

    by_decomp: dict[str, list[float]] = defaultdict(list)
    by_decomp_sem: dict[str, list[float]] = defaultdict(list)
    for s in scores:
        if s.error is None:
            by_decomp[s.decompiler].append(s.source_similarity)
            by_decomp_sem[s.decompiler].append(s.semantic_score)



    fn_names = sorted(set(s.function_name for s in scores))
    
    # We will serialize scores and color dict to JSON to inject directly into script
    scores_json = json.dumps([{
        "decompiler": s.decompiler,
        "function_name": s.function_name,
        "compiler_variant": s.compiler_variant,
        "source_similarity": s.source_similarity,
        "semantic_score": s.semantic_score,
        "semantic_error": s.semantic_error,
        "fail_category": getattr(s, "fail_category", "") or "",
        "cases_passed": getattr(s, "cases_passed", 0),
        "cases_total": getattr(s, "cases_total", 0),
        "composite_score": getattr(s, "composite_score", 0.0),
        "structural_penalty": getattr(s, "structural_penalty", 0.0),
        "uses_intrinsics": getattr(s, "uses_intrinsics", False),
        "goto_count": s.goto_count,
        "nesting_depth": s.nesting_depth,
        "consensus_rank": s.consensus_rank,
        "time_ms": s.time_ms,
        "error": s.error,
    } for s in scores], indent=2)

    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Fission Benchmark Dashboard</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/chart.js@4"></script>
<style>
  :root {
    --bg: #090d16;
    --surface: #111827;
    --surface-hover: #1f2937;
    --border: #374151;
    --text: #f3f4f6;
    --muted: #9ca3af;
    --accent-indigo: #6366f1;
    --accent-cyan: #06b6d4;
    --success: #10b981;
    --warning: #f59e0b;
    --error: #ef4444;
  }
  
  * { box-sizing: border-box; margin: 0; padding: 0; }
  
  body {
    background: radial-gradient(circle at top, #1e293b, #0f172a);
    color: var(--text);
    font-family: 'Inter', -apple-system, sans-serif;
    padding: 2rem;
    min-height: 100vh;
  }
  
  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
    border-bottom: 1px solid var(--border);
    padding-bottom: 1.5rem;
  }
  
  .brand h1 {
    font-size: 2.2rem;
    font-weight: 700;
    letter-spacing: -0.025em;
    background: linear-gradient(to right, #6366f1, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }
  
  .brand p {
    color: var(--muted);
    font-size: 0.95rem;
    margin-top: 0.25rem;
  }
  
  .meta-badges {
    display: flex;
    gap: 0.75rem;
  }
  
  .meta-badge {
    background: rgba(55, 65, 81, 0.4);
    border: 1px solid var(--border);
    padding: 0.5rem 1rem;
    border-radius: 9999px;
    font-size: 0.85rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: #e5e7eb;
  }
  
  .meta-badge strong {
    color: var(--accent-cyan);
  }

  .kpi-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 1rem;
    margin-bottom: 2rem;
  }
  
  .kpi-card {
    background: rgba(17, 24, 39, 0.6);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.25rem;
    backdrop-filter: blur(12px);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  }
  
  .kpi-card:hover {
    transform: translateY(-2px);
    border-color: var(--accent-indigo);
    box-shadow: 0 10px 25px -5px rgba(99, 102, 241, 0.15);
  }
  
  .kpi-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.75rem;
  }
  
  .kpi-title {
    font-size: 0.875rem;
    font-weight: 600;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  
  .kpi-color-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
  }
  
  .kpi-value {
    font-size: 1.8rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
  }
  
  .kpi-bar-bg {
    background: #1f2937;
    height: 6px;
    border-radius: 9999px;
    margin-bottom: 0.75rem;
    overflow: hidden;
  }
  
  .kpi-bar-fill {
    height: 100%;
    border-radius: 9999px;
  }
  
  .kpi-stats {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.5rem;
    font-size: 0.75rem;
    color: var(--muted);
  }
  
  .kpi-stat-item strong {
    color: var(--text);
  }

  .charts-grid {
    display: grid;
    grid-template-columns: 1fr 1.2fr;
    gap: 1.5rem;
    margin-bottom: 2rem;
  }
  
  @media (max-width: 1024px) {
    .charts-grid { grid-template-columns: 1fr; }
  }
  
  .card {
    background: rgba(17, 24, 39, 0.6);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.5rem;
    backdrop-filter: blur(12px);
  }
  
  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.25rem;
  }
  
  .card h2 {
    font-size: 1.1rem;
    font-weight: 600;
    color: #f3f4f6;
  }
  
  .card-actions select {
    background: #1f2937;
    border: 1px solid var(--border);
    color: var(--text);
    padding: 0.4rem 0.8rem;
    border-radius: 6px;
    font-size: 0.85rem;
    outline: none;
    cursor: pointer;
  }
  
  .chart-container {
    position: relative;
    height: 280px;
    width: 100%;
  }

  .table-controls {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    margin-bottom: 1rem;
    align-items: center;
  }
  
  .search-wrapper {
    flex-grow: 1;
    position: relative;
    min-width: 200px;
  }
  
  .search-wrapper input {
    width: 100%;
    background: #1f2937;
    border: 1px solid var(--border);
    color: var(--text);
    padding: 0.5rem 1rem;
    border-radius: 8px;
    font-size: 0.875rem;
    outline: none;
    transition: all 0.2s;
  }
  
  .search-wrapper input:focus {
    border-color: var(--accent-indigo);
    box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2);
  }
  
  .filter-select {
    background: #1f2937;
    border: 1px solid var(--border);
    color: var(--text);
    padding: 0.5rem 1rem;
    border-radius: 8px;
    font-size: 0.875rem;
    outline: none;
    cursor: pointer;
  }
  
  .filter-select:focus {
    border-color: var(--accent-indigo);
  }

  .table-container {
    overflow-x: auto;
    border-radius: 8px;
    border: 1px solid var(--border);
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.875rem;
    text-align: left;
  }
  
  th {
    background: #1f2937;
    color: #e5e7eb;
    font-weight: 600;
    padding: 0.75rem 1rem;
    border-bottom: 1px solid var(--border);
    cursor: pointer;
    user-select: none;
  }
  
  th:hover {
    background: #374151;
  }
  
  th.sorted-asc::after { content: " ▲"; font-size: 0.75rem; }
  th.sorted-desc::after { content: " ▼"; font-size: 0.75rem; }
  
  td {
    padding: 0.75rem 1rem;
    border-bottom: 1px solid var(--border);
    color: #d1d5db;
    vertical-align: middle;
  }
  
  tr:last-child td { border-bottom: none; }
  
  tr:hover td {
    background: rgba(255, 255, 255, 0.02);
  }
  
  tr.highlighted-row td {
    background: rgba(99, 102, 241, 0.05);
    border-left: 3px solid var(--accent-indigo);
  }
  
  tr.highlighted-row:hover td {
    background: rgba(99, 102, 241, 0.08);
  }
  
  .sim-cell {
    display: flex;
    align-items: center;
    gap: 0.75rem;
  }
  
  .sim-badge {
    padding: 0.25rem 0.5rem;
    border-radius: 6px;
    font-size: 0.75rem;
    font-weight: 700;
    min-width: 45px;
    text-align: center;
  }
  
  .sim-badge.excellent { background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); }
  .sim-badge.good { background: rgba(59, 130, 246, 0.15); color: #60a5fa; border: 1px solid rgba(59, 130, 246, 0.3); }
  .sim-badge.weak { background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.3); }
  .sim-badge.poor { background: rgba(239, 68, 68, 0.15); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.3); }
  
  .sim-bar-bg {
    background: #1f2937;
    height: 6px;
    border-radius: 9999px;
    width: 80px;
    overflow: hidden;
  }
  .sim-bar-fill { height: 100%; border-radius: 9999px; }
  .sim-bar-fill.excellent { background: #10b981; }
  .sim-bar-fill.good { background: #3b82f6; }
  .sim-bar-fill.weak { background: #f59e0b; }
  .sim-bar-fill.poor { background: #ef4444; }

  .badge {
    display: inline-flex;
    align-items: center;
    gap: 0.25rem;
    padding: 0.25rem 0.5rem;
    border-radius: 6px;
    font-size: 0.75rem;
    font-weight: 600;
  }
  
  .badge.success { background: rgba(16, 185, 129, 0.1); color: #10b981; border: 1px solid rgba(16, 185, 129, 0.2); }
  .badge.error { background: rgba(239, 68, 68, 0.1); color: #ef4444; border: 1px solid rgba(239, 68, 68, 0.2); }
  
  .rank-badge {
    font-size: 0.75rem;
    font-weight: 700;
    padding: 0.2rem 0.4rem;
    border-radius: 4px;
    display: inline-block;
  }
  .rank-gold { background: rgba(245, 158, 11, 0.2); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.4); }
  .rank-silver { background: rgba(156, 163, 175, 0.2); color: #e5e7eb; border: 1px solid rgba(156, 163, 175, 0.4); }
  .rank-bronze { background: rgba(180, 83, 9, 0.2); color: #f97316; border: 1px solid rgba(180, 83, 9, 0.4); }
  .rank-other { color: var(--muted); }

  .pagination-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 1rem;
    font-size: 0.875rem;
    color: var(--muted);
  }
  
  .pagination-buttons {
    display: flex;
    gap: 0.5rem;
  }
  
  .pagination-btn {
    background: #1f2937;
    border: 1px solid var(--border);
    color: var(--text);
    padding: 0.4rem 0.8rem;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s;
  }
  
  .pagination-btn:hover:not(:disabled) {
    background: #374151;
    border-color: var(--accent-indigo);
  }
  
  .pagination-btn:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
</style>
</head>
<body>

<header>
  <div class="brand">
    <h1>🔬 Fission Benchmark</h1>
    <p>Cross-Decompiler Semantic Parity & Similarity Dashboard</p>
  </div>
  <div class="meta-badges">
    <div class="meta-badge">Corpus: <strong id="corpusName">__CORPUS_SPLIT__</strong></div>
    <div class="meta-badge">Functions: <strong id="funcCount">__FUNCTIONS_COUNT__</strong></div>
    <div class="meta-badge">Updated: <strong id="genTime">__TS__</strong></div>
  </div>
</header>

<!-- KPI Cards -->
<div class="kpi-grid" id="kpiContainer"></div>

<!-- Charts Section -->
<div class="charts-grid">
  <div class="card">
    <div class="card-header">
      <h2>Average Source Similarity</h2>
    </div>
    <div class="chart-container">
      <canvas id="barChart"></canvas>
    </div>
  </div>
  
  <div class="card">
    <div class="card-header">
      <h2>Per-Function Comparison</h2>
      <div class="card-actions">
        <select id="functionChartSelector"></select>
      </div>
    </div>
    <div class="chart-container">
      <canvas id="perFuncChart"></canvas>
    </div>
  </div>
</div>

<!-- Detailed Table Section -->
<div class="card">
  <div class="card-header">
    <h2>Detailed Decompilation Results</h2>
  </div>
  
  <div class="table-controls">
    <div class="search-wrapper">
      <input type="text" id="searchInput" placeholder="Search functions, compilers, or decompilers...">
    </div>
    <select id="decompilerFilter" class="filter-select">
      <option value="all">All Decompilers</option>
    </select>
    <select id="variantFilter" class="filter-select">
      <option value="all">All Variants</option>
    </select>
    <select id="gapFilter" class="filter-select">
      <option value="all">All Results</option>
      <option value="fission-gap">Fission Quality Gaps</option>
      <option value="hard">Objectively Hard</option>
      <option value="gotos">Fission with Gotos</option>
    </select>
  </div>
  
  <div class="table-container">
    <table id="resultsTable">
      <thead>
        <tr>
          <th data-key="function_name">Function</th>
          <th data-key="compiler_variant">Variant</th>
          <th data-key="decompiler">Decompiler</th>
          <th data-key="source_similarity">Similarity</th>
          <th data-key="semantic_score">Semantic</th>
          <th data-key="consensus_rank">Rank</th>
          <th data-key="goto_count">Gotos</th>
          <th data-key="time_ms">Time</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody></tbody>
    </table>
  </div>
  
  <div class="pagination-container">
    <span id="pageInfo"></span>
    <div class="pagination-buttons">
      <button id="prevBtn" class="pagination-btn">Prev</button>
      <button id="nextBtn" class="pagination-btn">Next</button>
    </div>
  </div>
</div>

<script>
const SCORES = __SCORES_JSON__;
const DECOMPILER_COLORS = __DECOMPILER_COLORS__;

// Helper to group scores
const scoresByGroup = {};
SCORES.forEach(s => {
  const key = s.function_name + '|' + s.compiler_variant;
  if (!scoresByGroup[key]) scoresByGroup[key] = [];
  scoresByGroup[key].push(s);
});

// Setup metadata and filters
const fnNames = [...new Set(SCORES.map(s => s.function_name))].sort();
const variants = [...new Set(SCORES.map(s => s.compiler_variant))].sort();
const decompilers = [...new Set(SCORES.map(s => s.decompiler))].sort();

// Populate function selector for chart
const fnChartSel = document.getElementById('functionChartSelector');
fnNames.forEach(fn => {
  const opt = document.createElement('option');
  opt.value = fn;
  opt.textContent = fn;
  fnChartSel.appendChild(opt);
});
if (fnNames.length > 0) fnChartSel.value = fnNames[0];

// Populate filters
const decompFilter = document.getElementById('decompilerFilter');
decompilers.forEach(d => {
  const opt = document.createElement('option');
  opt.value = d;
  opt.textContent = d;
  decompFilter.appendChild(opt);
});

const variantFilter = document.getElementById('variantFilter');
variants.forEach(v => {
  const opt = document.createElement('option');
  opt.value = v;
  opt.textContent = v;
  variantFilter.appendChild(opt);
});

// Calculate statistics per decompiler
const stats = {};
decompilers.forEach(d => {
  const decScores = SCORES.filter(s => s.decompiler === d);
  const validScores = decScores.filter(s => s.error === null);
  const avgSim = validScores.length ? validScores.reduce((sum, s) => sum + s.source_similarity, 0) / validScores.length : 0;
  const avgSem = validScores.length ? validScores.reduce((sum, s) => sum + (s.semantic_score || 0), 0) / validScores.length : 0;
  const successCount = decScores.filter(s => s.error === null).length;
  const successRate = decScores.length ? (successCount / decScores.length) * 100 : 0;
  const totalGotos = decScores.reduce((sum, s) => sum + (s.goto_count || 0), 0);
  const avgTime = decScores.length ? decScores.reduce((sum, s) => sum + s.time_ms, 0) / decScores.length : 0;
  
  stats[d] = { avgSim, avgSem, successRate, totalGotos, avgTime };
});

// Render KPI Cards
const kpiContainer = document.getElementById('kpiContainer');
decompilers.forEach(d => {
  const s = stats[d];
  const color = DECOMPILER_COLORS[d] || '#888';
  
  const card = document.createElement('div');
  card.className = 'kpi-card';
  card.innerHTML = `
    <div class="kpi-header">
      <span class="kpi-title">${d}</span>
      <span class="kpi-color-dot" style="background-color: ${color}"></span>
    </div>
    <div class="kpi-value">${(s.avgSim * 100).toFixed(1)}% <span style="font-size: 0.85rem; color: var(--muted); font-weight: normal;">(Sem: ${(s.avgSem * 100).toFixed(0)}%)</span></div>
    <div class="kpi-bar-bg">
      <div class="kpi-bar-fill" style="width: ${s.avgSim * 100}%; background-color: ${color}"></div>
    </div>
    <div class="kpi-stats">
      <div class="kpi-stat-item">Success: <strong>${s.successRate.toFixed(0)}%</strong></div>
      <div class="kpi-stat-item">Gotos: <strong>${s.totalGotos}</strong></div>
      <div class="kpi-stat-item" style="grid-column: span 2; margin-top: 4px;">Avg Time: <strong>${s.avgTime.toFixed(0)}ms</strong></div>
    </div>
  `;
  kpiContainer.appendChild(card);
});

// Setup global Bar Chart
const globalBarCtx = document.getElementById('barChart').getContext('2d');
const sortedDecompilers = [...decompilers].sort((a, b) => stats[b].avgSim - stats[a].avgSim);
new Chart(globalBarCtx, {
  type: 'bar',
  data: {
    labels: sortedDecompilers,
    datasets: [{
      label: 'Avg Similarity',
      data: sortedDecompilers.map(d => stats[d].avgSim),
      backgroundColor: sortedDecompilers.map(d => DECOMPILER_COLORS[d] || '#888'),
      borderRadius: 6
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: { legend: { display: false } },
    scales: {
      y: { min: 0, max: 1, grid: { color: '#374151' }, ticks: { color: '#9ca3af' } },
      x: { grid: { display: false }, ticks: { color: '#9ca3af' } }
    }
  }
});

// Setup interactive Per-Function Chart
let perFuncChart = null;
function updatePerFuncChart(funcName) {
  const funcScores = SCORES.filter(s => s.function_name === funcName);
  const datasets = decompilers.map(d => {
    const dScores = funcScores.filter(s => s.decompiler === d);
    return {
      label: d,
      data: variants.map(v => {
        const match = dScores.find(s => s.compiler_variant === v);
        return match && !match.error ? match.source_similarity : 0;
      }),
      backgroundColor: DECOMPILER_COLORS[d] || '#888',
      borderRadius: 4
    };
  });
  
  if (perFuncChart) perFuncChart.destroy();
  
  const ctx = document.getElementById('perFuncChart').getContext('2d');
  perFuncChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: variants,
      datasets: datasets
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: { legend: { position: 'top', labels: { color: '#9ca3af' } } },
      scales: {
        y: { min: 0, max: 1, grid: { color: '#374151' }, ticks: { color: '#9ca3af' } },
        x: { grid: { display: false }, ticks: { color: '#9ca3af' } }
      }
    }
  });
}

fnChartSel.addEventListener('change', (e) => updatePerFuncChart(e.target.value));
if (fnNames.length > 0) updatePerFuncChart(fnNames[0]);

// Table Pagination, Search and Sort Logic
let currentFiltered = [...SCORES];
let currentPage = 1;
const rowsPerPage = 25;
let currentSort = { key: 'function_name', asc: true };

function getSimilarityClass(val, hasError) {
  if (hasError) return 'poor';
  if (val >= 0.8) return 'excellent';
  if (val >= 0.5) return 'good';
  if (val >= 0.2) return 'weak';
  return 'poor';
}

function getRankBadge(rank) {
  if (rank === 1) return '<span class="rank-badge rank-gold">#1</span>';
  if (rank === 2) return '<span class="rank-badge rank-silver">#2</span>';
  if (rank === 3) return '<span class="rank-badge rank-bronze">#3</span>';
  if (rank) return `<span class="rank-badge rank-other">#${rank}</span>`;
  return '<span class="rank-badge rank-other">—</span>';
}

function renderTable() {
  const tbody = document.querySelector('#resultsTable tbody');
  tbody.innerHTML = '';
  
  // Sort scores
  const k = currentSort.key;
  const isAsc = currentSort.asc ? 1 : -1;
  currentFiltered.sort((a, b) => {
    let valA = a[k];
    let valB = b[k];
    if (valA === null || valA === undefined) valA = '';
    if (valB === null || valB === undefined) valB = '';
    
    if (typeof valA === 'string') {
      return valA.localeCompare(valB) * isAsc;
    }
    return (valA < valB ? -1 : valA > valB ? 1 : 0) * isAsc;
  });
  
  const totalRows = currentFiltered.length;
  const totalPages = Math.ceil(totalRows / rowsPerPage) || 1;
  if (currentPage > totalPages) currentPage = totalPages;
  
  const startIdx = (currentPage - 1) * rowsPerPage;
  const endIdx = Math.min(startIdx + rowsPerPage, totalRows);
  const pageRows = currentFiltered.slice(startIdx, endIdx);
  
  pageRows.forEach(s => {
    const tr = document.createElement('tr');
    if (s.decompiler === 'fission') {
      tr.className = 'highlighted-row';
    }
    
    const rankLabel = getRankBadge(s.consensus_rank);
    const compScore = (s.composite_score || 0);
    const simClass = getSimilarityClass(compScore, s.error);
    const statusClass = s.error ? 'error' : 'success';
    const statusText = s.error ? '❌ Error' : '✓ Success';
    const failCatLabels = {'compile_error':'🔴','runtime_error':'🟠','timeout':'🟡','assertion_fail':'🟤','no_wrapper':'⚪','':''};
    const failCat = s.fail_category || '';
    const failIcon = failCatLabels[failCat] !== undefined ? failCatLabels[failCat] : '🟤';
    const semPct = s.cases_total > 0
      ? `${(s.semantic_score*100).toFixed(0)}% (${s.cases_passed}/${s.cases_total})`
      : (s.semantic_score >= 1.0 ? 'Pass' : 'Fail');
    const intrinFlag = s.uses_intrinsics ? ' ⚠️' : '';
    const errTxt = (s.semantic_error||'').replace(/\\/g,'\\\\').replace(/`/g,'\\`').replace(/\$/g,'\\$');
    const semHtml = s.error
      ? '<span class="badge error">N/A</span>'
      : (s.semantic_score >= 1.0
          ? `<span class="badge success">${semPct}${intrinFlag}</span>`
          : `<span class="badge error" title="${failCat}" style="cursor:pointer;" onclick="openModal('${s.decompiler}','${s.function_name}','${s.compiler_variant}','${errTxt}')">${failIcon} ${semPct}${intrinFlag}</span>`);
    
    tr.innerHTML = `
      <td><strong>${s.function_name}</strong></td>
      <td>${s.compiler_variant}</td>
      <td>
        <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background-color:${DECOMPILER_COLORS[s.decompiler] || '#888'}; margin-right:6px;"></span>
        ${s.decompiler}
      </td>
      <td>
        <div class="sim-cell">
          <span class="sim-badge ${simClass}">${compScore.toFixed(3)}</span>
          <div class="sim-bar-bg">
            <div class="sim-bar-fill ${simClass}" style="width: ${compScore * 100}%"></div>
          </div>
        </div>
        <small style="color:#9ca3af;font-size:0.75em;">sim:${s.source_similarity.toFixed(3)}</small>
      </td>
      <td>${semHtml}</td>
      <td>${rankLabel}</td>
      <td>${s.goto_count}</td>
      <td>${s.time_ms}ms</td>
      <td><span class="badge ${statusClass}">${statusText}</span></td>
    `;
    tbody.appendChild(tr);
  });
  
  document.getElementById('pageInfo').textContent = `Showing ${totalRows ? startIdx + 1 : 0} - ${endIdx} of ${totalRows} results`;
  document.getElementById('prevBtn').disabled = currentPage === 1;
  document.getElementById('nextBtn').disabled = currentPage === totalPages;
}

function filterScores() {
  const query = document.getElementById('searchInput').value.toLowerCase();
  const decomp = document.getElementById('decompilerFilter').value;
  const variant = document.getElementById('variantFilter').value;
  const gapType = document.getElementById('gapFilter').value;
  
  currentFiltered = SCORES.filter(s => {
    const matchesQuery = s.function_name.toLowerCase().includes(query) || 
                       s.compiler_variant.toLowerCase().includes(query) ||
                       s.decompiler.toLowerCase().includes(query);
    const matchesDecomp = decomp === 'all' || s.decompiler === decomp;
    const matchesVariant = variant === 'all' || s.compiler_variant === variant;
    
    let matchesGap = true;
    if (gapType === 'fission-gap') {
      const key = s.function_name + '|' + s.compiler_variant;
      const group = scoresByGroup[key] || [];
      const fissionScore = group.find(x => x.decompiler === 'fission');
      const othersOk = group.some(x => x.decompiler !== 'fission' && x.source_similarity >= 0.3);
      matchesGap = fissionScore && fissionScore.source_similarity < 0.3 && othersOk;
    } else if (gapType === 'hard') {
      const key = s.function_name + '|' + s.compiler_variant;
      const group = scoresByGroup[key] || [];
      matchesGap = group.every(x => x.source_similarity < 0.3);
    } else if (gapType === 'gotos') {
      matchesGap = s.decompiler === 'fission' && s.goto_count > 0;
    }
    
    return matchesQuery && matchesDecomp && matchesVariant && matchesGap;
  });
  
  currentPage = 1;
  renderTable();
}

// Event Listeners for Filters
document.getElementById('searchInput').addEventListener('input', filterScores);
document.getElementById('decompilerFilter').addEventListener('change', filterScores);
document.getElementById('variantFilter').addEventListener('change', filterScores);
document.getElementById('gapFilter').addEventListener('change', filterScores);

// Pagination Buttons
document.getElementById('prevBtn').addEventListener('click', () => {
  if (currentPage > 1) {
    currentPage--;
    renderTable();
  }
});
document.getElementById('nextBtn').addEventListener('click', () => {
  const totalPages = Math.ceil(currentFiltered.length / rowsPerPage);
  if (currentPage < totalPages) {
    currentPage++;
    renderTable();
  }
});

// Sorting columns
document.querySelectorAll('#resultsTable th').forEach(th => {
  th.addEventListener('click', () => {
    const key = th.dataset.key;
    if (!key) return;
    
    if (currentSort.key === key) {
      currentSort.asc = !currentSort.asc;
    } else {
      currentSort.key = key;
      currentSort.asc = true;
    }
    
    document.querySelectorAll('#resultsTable th').forEach(h => {
      h.classList.remove('sorted-asc', 'sorted-desc');
    });
    
    th.classList.add(currentSort.asc ? 'sorted-asc' : 'sorted-desc');
    renderTable();
  });
});

// Initial Render

// Modal logic
function openModal(decompiler, funcName, variant, errorMsg) {
  document.getElementById('modalTitle').textContent = `Verification Error: ${decompiler} - ${funcName} (${variant})`;
  document.getElementById('modalErrorContent').textContent = errorMsg || 'No error details recorded.';
  document.getElementById('errorModal').style.display = 'flex';
}
function closeModal() {
  document.getElementById('errorModal').style.display = 'none';
}
window.addEventListener('click', (e) => {
  const modal = document.getElementById('errorModal');
  if (e.target === modal) closeModal();
});

renderTable();
</script>

<!-- Modal overlay -->
<div id="errorModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.7); z-index: 1000; justify-content: center; align-items: center;">
  <div style="background: var(--surface); border: 1px solid var(--border); border-radius: 12px; width: 80%; max-width: 800px; max-height: 80%; display: flex; flex-direction: column; overflow: hidden; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.5);">
    <div style="padding: 1.25rem; border-bottom: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; background: #1f2937;">
      <h3 style="font-weight: 600;" id="modalTitle">Verification Error Details</h3>
      <button onclick="closeModal()" style="background: none; border: none; color: var(--muted); font-size: 1.5rem; cursor: pointer; line-height: 1;">&times;</button>
    </div>
    <div style="padding: 1.5rem; overflow-y: auto; flex-grow: 1;">
      <pre style="background: #090d16; border: 1px solid var(--border); padding: 1rem; border-radius: 8px; font-family: monospace; font-size: 0.85rem; color: #ef4444; white-space: pre-wrap;" id="modalErrorContent"></pre>
    </div>
  </div>
</div>
</body>
</html>
"""

    # Inject variables into HTML
    html = html_template.replace("__TS__", ts)
    html = html.replace("__CORPUS_SPLIT__", corpus_split)
    html = html.replace("__FUNCTIONS_COUNT__", str(len(fn_names)))
    html = html.replace("__SCORES_JSON__", scores_json)
    html = html.replace("__DECOMPILER_COLORS__", json.dumps(DECOMPILER_COLORS))

    return html


def generate_report(scores: list[FunctionScore], corpus_split: str = "dev") -> None:
    RESULTS_DIR.mkdir(exist_ok=True)
    DOCS_DIR.mkdir(exist_ok=True)

    # Markdown
    md = generate_markdown(scores, corpus_split)
    (RESULTS_DIR / "latest.md").write_text(md)

    # HTML
    html = generate_html(scores, corpus_split)
    (DOCS_DIR / "index.html").write_text(html)
