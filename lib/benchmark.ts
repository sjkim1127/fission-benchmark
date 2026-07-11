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
  return BenchmarkEnvelopeSchema.parse(raw);
}

/** Group rows by decompiler for summary statistics */
export function groupByDecompiler(rows: BenchmarkEnvelope["rows"]) {
  const map = new Map<string, {
    attempted: number;
    clean: number;
    error: number;
    totalCorrectness: number;
    totalSimilarity: number;
    semanticPass: number;
    totalTime: number;
  }>();

  for (const row of rows) {
    const d = row.decompiler;
    if (!map.has(d)) {
      map.set(d, { attempted: 0, clean: 0, error: 0, totalCorrectness: 0, totalSimilarity: 0, semanticPass: 0, totalTime: 0 });
    }
    const s = map.get(d)!;
    s.attempted++;
    if (row.error) {
      s.error++;
    } else {
      s.clean++;
      s.totalCorrectness += row.correctness_score ?? 0;
      s.totalSimilarity += row.source_similarity;
      if ((row.semantic_score ?? 0) >= 1.0) s.semanticPass++;
      s.totalTime += row.time_ms;
    }
  }

  return Array.from(map.entries()).map(([decompiler, s]) => ({
    decompiler,
    attempted: s.attempted,
    clean: s.clean,
    error: s.error,
    avgCorrectness: s.clean > 0 ? s.totalCorrectness / s.clean : 0,
    avgSimilarity: s.clean > 0 ? s.totalSimilarity / s.clean : 0,
    semanticPassPct: s.clean > 0 ? (s.semanticPass / s.clean) * 100 : 0,
    avgTimeMs: s.clean > 0 ? s.totalTime / s.clean : 0,
  })).sort((a, b) => {
    // Fission first, then sort by correctness desc
    if (a.decompiler === "fission") return -1;
    if (b.decompiler === "fission") return 1;
    return b.avgCorrectness - a.avgCorrectness;
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
