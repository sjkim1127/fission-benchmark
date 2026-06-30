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
    "retdec":   "#10b981",
    "radare2":  "#ef4444",
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
        f"# Fission Benchmark Report",
        f"",
        f"**Generated:** {ts}  ",
        f"**Corpus:** `{corpus_split}`  ",
        f"**Functions evaluated:** {len(set(s.function_name for s in scores))}",
        f"",
        f"---",
        f"",
        f"## Summary — Average Source Similarity",
        f"",
    ]

    # Per-decompiler average
    by_decomp: dict[str, list[float]] = defaultdict(list)
    for s in scores:
        if s.error is None:
            by_decomp[s.decompiler].append(s.source_similarity)

    rows = []
    for d, sims in sorted(by_decomp.items(), key=lambda x: -sum(x[1]) / len(x[1])):
        avg = sum(sims) / len(sims)
        rows.append([f"**{d}**", f"{avg:.3f}", f"{len(sims)}"])
    lines.append(_md_table(["Decompiler", "Avg Similarity", "Functions"], rows))
    lines += ["", "---", "", "## Per-Function Results", ""]

    # Per function
    by_fn: dict[str, list[FunctionScore]] = defaultdict(list)
    for s in scores:
        by_fn[s.function_name].append(s)

    for fn_name, fn_scores in sorted(by_fn.items()):
        lines.append(f"### `{fn_name}`")
        rows = []
        for s in sorted(fn_scores, key=lambda x: x.decompiler):
            rank = f"#{s.consensus_rank}" if s.consensus_rank else "—"
            err = f"❌ {s.error[:40]}" if s.error else "✓"
            rows.append([
                s.decompiler, s.compiler_variant,
                f"{s.source_similarity:.3f}", rank,
                str(s.goto_count), str(s.nesting_depth),
                f"{s.time_ms}ms", err,
            ])
        lines.append(_md_table(
            ["Decompiler", "Variant", "Similarity", "Rank", "Gotos", "Depth", "Time", "Status"],
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
        all_low = all(s.source_similarity < 0.3 for s in valid)
        fission_scores = [s for s in valid if s.decompiler == "fission"]
        others_ok = any(s.source_similarity >= 0.3 for s in valid if s.decompiler != "fission")
        fission_low = fission_scores and all(s.source_similarity < 0.3 for s in fission_scores)

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
    for s in scores:
        if s.error is None:
            by_decomp[s.decompiler].append(s.source_similarity)

    bar_labels = list(by_decomp.keys())
    bar_data = [round(sum(v) / len(v), 4) if v else 0 for v in by_decomp.values()]
    bar_colors = [DECOMPILER_COLORS.get(d, "#888") for d in bar_labels]

    fn_names = sorted(set(s.function_name for s in scores))
    scatter_datasets = []
    for d in bar_labels:
        pts = []
        for i, fn in enumerate(fn_names):
            matches = [s for s in scores if s.decompiler == d and s.function_name == fn and not s.error]
            if matches:
                pts.append({"x": i, "y": round(sum(m.source_similarity for m in matches) / len(matches), 4)})
        scatter_datasets.append({
            "label": d,
            "data": pts,
            "backgroundColor": DECOMPILER_COLORS.get(d, "#888"),
        })

    scores_json = json.dumps([{
        "decompiler": s.decompiler,
        "function_name": s.function_name,
        "compiler_variant": s.compiler_variant,
        "source_similarity": s.source_similarity,
        "goto_count": s.goto_count,
        "consensus_rank": s.consensus_rank,
        "time_ms": s.time_ms,
        "error": s.error,
    } for s in scores], indent=2)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Fission Benchmark Dashboard</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4"></script>
<style>
  :root {{
    --bg: #0d1117; --surface: #161b22; --border: #30363d;
    --text: #e6edf3; --muted: #8b949e; --accent: #6366f1;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ background: var(--bg); color: var(--text); font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; padding: 2rem; }}
  h1 {{ font-size: 1.8rem; margin-bottom: 0.25rem; }}
  .meta {{ color: var(--muted); font-size: 0.85rem; margin-bottom: 2rem; }}
  .grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 2rem; }}
  .card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem; }}
  .card h2 {{ font-size: 1rem; color: var(--muted); margin-bottom: 1rem; text-transform: uppercase; letter-spacing: 0.05em; }}
  canvas {{ max-height: 280px; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 0.85rem; margin-top: 1rem; }}
  th {{ color: var(--muted); text-align: left; padding: 0.4rem 0.6rem; border-bottom: 1px solid var(--border); }}
  td {{ padding: 0.4rem 0.6rem; border-bottom: 1px solid var(--border); }}
  tr:hover td {{ background: rgba(255,255,255,0.03); }}
  .badge {{ display: inline-block; padding: 0.1rem 0.5rem; border-radius: 4px; font-size: 0.75rem; font-weight: 600; }}
  .gap {{ background: #7f1d1d; color: #fca5a5; }}
  .hard {{ background: #1c1917; color: #a8a29e; }}
  .ok {{ background: #14532d; color: #86efac; }}
  @media (max-width: 768px) {{ .grid {{ grid-template-columns: 1fr; }} }}
</style>
</head>
<body>
<h1>🔬 Fission Benchmark</h1>
<p class="meta">Generated: {ts} &nbsp;·&nbsp; Corpus: <strong>{corpus_split}</strong> &nbsp;·&nbsp; Functions: <strong>{len(fn_names)}</strong></p>

<div class="grid">
  <div class="card">
    <h2>Average Source Similarity</h2>
    <canvas id="barChart"></canvas>
  </div>
  <div class="card">
    <h2>Per-Function Similarity</h2>
    <canvas id="scatterChart"></canvas>
  </div>
</div>

<div class="card">
  <h2>Detailed Results</h2>
  <table id="resultsTable">
    <thead><tr><th>Function</th><th>Variant</th><th>Decompiler</th><th>Similarity</th><th>Rank</th><th>Gotos</th><th>Time</th><th>Status</th></tr></thead>
    <tbody></tbody>
  </table>
</div>

<script>
const SCORES = {scores_json};
const FN_NAMES = {json.dumps(fn_names)};

// Bar chart
new Chart(document.getElementById('barChart'), {{
  type: 'bar',
  data: {{
    labels: {json.dumps(bar_labels)},
    datasets: [{{ label: 'Avg Similarity', data: {json.dumps(bar_data)},
      backgroundColor: {json.dumps(bar_colors)}, borderRadius: 4 }}]
  }},
  options: {{ plugins: {{ legend: {{ display: false }} }},
    scales: {{ y: {{ min: 0, max: 1, grid: {{ color: '#30363d' }}, ticks: {{ color: '#8b949e' }} }},
               x: {{ grid: {{ display: false }}, ticks: {{ color: '#8b949e' }} }} }} }}
}});

// Scatter
new Chart(document.getElementById('scatterChart'), {{
  type: 'scatter',
  data: {{ datasets: {json.dumps(scatter_datasets)} }},
  options: {{
    scales: {{
      x: {{ ticks: {{ callback: v => FN_NAMES[v] || v, color: '#8b949e' }}, grid: {{ color: '#30363d' }} }},
      y: {{ min: 0, max: 1, grid: {{ color: '#30363d' }}, ticks: {{ color: '#8b949e' }} }}
    }}
  }}
}});

// Table
const tbody = document.querySelector('#resultsTable tbody');
SCORES.forEach(s => {{
  const tr = document.createElement('tr');
  const rankLabel = s.consensus_rank ? `#${{s.consensus_rank}}` : '—';
  const statusClass = s.error ? 'gap' : (s.source_similarity > 0.5 ? 'ok' : '');
  const statusText = s.error ? '❌' : '✓';
  tr.innerHTML = `<td>${{s.function_name}}</td><td>${{s.compiler_variant}}</td>
    <td>${{s.decompiler}}</td><td>${{s.source_similarity.toFixed(3)}}</td>
    <td>${{rankLabel}}</td><td>${{s.goto_count}}</td><td>${{s.time_ms}}ms</td>
    <td><span class="badge ${{statusClass}}">${{statusText}}</span></td>`;
  tbody.appendChild(tr);
}});
</script>
</body>
</html>"""


# ── Entry point ───────────────────────────────────────────────────────────────

def generate_report(scores: list[FunctionScore], corpus_split: str = "dev") -> None:
    RESULTS_DIR.mkdir(exist_ok=True)
    DOCS_DIR.mkdir(exist_ok=True)

    # Markdown
    md = generate_markdown(scores, corpus_split)
    (RESULTS_DIR / "latest.md").write_text(md)

    # HTML
    html = generate_html(scores, corpus_split)
    (DOCS_DIR / "index.html").write_text(html)
