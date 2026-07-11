import { BenchmarkEnvelopeSchema, type BenchmarkEnvelope } from "./schemas";

const LATEST_URL =
  process.env.BENCHMARK_LATEST_URL ??
  "https://raw.githubusercontent.com/sjkim1127/fission-benchmark/main/results/latest.json";

export async function getLatestBenchmark(): Promise<BenchmarkEnvelope> {
  // Intentionally NOT using Next.js data cache (next.tags) here because the raw
  // JSON is ~18-25 MB and exceeds the 2 MB per-entry cache limit.
  // ISR is instead applied at the route segment level via `export const revalidate`
  // in page.tsx. The rendered HTML output is what gets cached, not the source data.
  const res = await fetch(LATEST_URL, { cache: "no-store" });

  if (!res.ok) {
    throw new Error(`Failed to load benchmark data: ${res.status} ${res.statusText}`);
  }

  const raw: unknown = await res.json();
  const envelope = BenchmarkEnvelopeSchema.parse(raw);
  if (envelope.validity?.publishable !== true) {
    throw new Error("Latest benchmark artifact is not a publishable official run");
  }
  return envelope;
}

/** Group rows by decompiler for summary statistics */
export function groupByDecompiler(rows: BenchmarkEnvelope["rows"]) {
  const map = new Map<string, {
    attempted: number;
    clean: number;
    error: number;
    totalCorrectness: number;
    correctnessTested: number;
    totalSimilarity: number;
    semanticPass: number;
    semanticTested: number;
    totalTime: number;
  }>();

  for (const row of rows) {
    const d = row.decompiler;
    if (!map.has(d)) {
      map.set(d, { attempted: 0, clean: 0, error: 0, totalCorrectness: 0, correctnessTested: 0, totalSimilarity: 0, semanticPass: 0, semanticTested: 0, totalTime: 0 });
    }
    const s = map.get(d)!;
    s.attempted++;
    if (row.error) {
      s.error++;
    } else {
      s.clean++;
      if (row.correctness_score !== null && row.correctness_score !== undefined) {
        s.totalCorrectness += row.correctness_score;
        s.correctnessTested++;
      }
      s.totalSimilarity += row.source_similarity;
      if (row.semantic_score !== null && row.semantic_score !== undefined) {
        s.semanticTested++;
        if (row.semantic_score >= 1.0) s.semanticPass++;
      }
      s.totalTime += row.time_ms;
    }
  }

  return Array.from(map.entries()).map(([decompiler, s]) => ({
    decompiler,
    attempted: s.attempted,
    clean: s.clean,
    error: s.error,
    avgCorrectness: s.correctnessTested > 0 ? s.totalCorrectness / s.correctnessTested : null,
    avgSimilarity: s.clean > 0 ? s.totalSimilarity / s.clean : 0,
    semanticPassPct: s.semanticTested > 0 ? (s.semanticPass / s.semanticTested) * 100 : null,
    avgTimeMs: s.clean > 0 ? s.totalTime / s.clean : 0,
  })).sort((a, b) => {
    // Fission first, then sort by correctness desc
    if (a.decompiler === "fission") return -1;
    if (b.decompiler === "fission") return 1;
    return (b.avgCorrectness ?? -1) - (a.avgCorrectness ?? -1);
  });
}

/** Get unique function names in the result */
export function getFunctionNames(rows: BenchmarkEnvelope["rows"]): string[] {
  return [...new Set(rows.map((r) => r.function_name))].sort();
}

/** Get rows for a specific function */
export function getRowsForFunction(rows: BenchmarkEnvelope["rows"], fn: string) {
  return rows.filter((r) => r.function_name === fn);
}
