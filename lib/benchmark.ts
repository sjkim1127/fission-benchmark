import {
  BenchmarkEnvelopeSchema,
  type BenchmarkEnvelope,
} from "./schemas";

const LATEST_URL =
  process.env.BENCHMARK_LATEST_URL ??
  "https://raw.githubusercontent.com/sjkim1127/fission-benchmark/main/results/latest.json";

export type MvpDecompilerStats = {
  decompiler: string;
  attempted: number;
  adapterClean: number;
  invalidBoundary: number;
  semanticTested: number;
  noWrapper: number;
  meanSemantic: number | null;
  perfectRows: number;
  meanTimeMs: number | null;
  taxonomy: Record<string, number>;
  oracleSubject: string | null;
};

export type CrossVariantRow = {
  decompiler: string;
  compiler_variant: string;
  compiler: string;
  opt: string;
  tested_rows: number;
  mean_pass_rate: number | null;
  perfect_rows: number;
};

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

function isAdapterFailure(row: BenchmarkEnvelope["rows"][number]): boolean {
  return Boolean(row.error) || row.fail_category === "adapter_error";
}

/** Prefer envelope.summary.mvp when present; otherwise aggregate from rows. */
export function groupByDecompiler(data: BenchmarkEnvelope): MvpDecompilerStats[] {
  const fromSummary = data.summary?.mvp?.by_decompiler as
    | Record<
        string,
        {
          semantic?: {
            mean_pass_rate?: number | null;
            perfect_rows?: number;
            tested_rows?: number;
            oracle_subject?: string | null;
          };
          coverage?: {
            attempted?: number;
            adapter_clean?: number;
            invalid_boundary?: number;
            semantic_tested?: number;
            no_wrapper?: number;
          };
          fail_taxonomy?: Record<string, number>;
          runtime?: { mean_ms?: number | null };
        }
      >
    | undefined;

  if (fromSummary && Object.keys(fromSummary).length > 0) {
    return Object.entries(fromSummary)
      .map(([decompiler, s]) => ({
        decompiler,
        attempted: s.coverage?.attempted ?? 0,
        adapterClean: s.coverage?.adapter_clean ?? 0,
        invalidBoundary: s.coverage?.invalid_boundary ?? 0,
        semanticTested: s.coverage?.semantic_tested ?? s.semantic?.tested_rows ?? 0,
        noWrapper: s.coverage?.no_wrapper ?? 0,
        meanSemantic:
          s.semantic?.mean_pass_rate === undefined || s.semantic?.mean_pass_rate === null
            ? null
            : Number(s.semantic.mean_pass_rate),
        perfectRows: s.semantic?.perfect_rows ?? 0,
        meanTimeMs:
          s.runtime?.mean_ms === undefined || s.runtime?.mean_ms === null
            ? null
            : Number(s.runtime.mean_ms),
        taxonomy: s.fail_taxonomy ?? {},
        oracleSubject: s.semantic?.oracle_subject ?? null,
      }))
      .sort((a, b) => {
        if (a.decompiler === "fission") return -1;
        if (b.decompiler === "fission") return 1;
        return (b.meanSemantic ?? -1) - (a.meanSemantic ?? -1);
      });
  }

  // Fallback for legacy envelopes without summary.
  const map = new Map<
    string,
    {
      attempted: number;
      adapterClean: number;
      invalidBoundary: number;
      semanticScores: number[];
      noWrapper: number;
      times: number[];
      taxonomy: Record<string, number>;
    }
  >();

  for (const row of data.rows) {
    const d = row.decompiler;
    if (!map.has(d)) {
      map.set(d, {
        attempted: 0,
        adapterClean: 0,
        invalidBoundary: 0,
        semanticScores: [],
        noWrapper: 0,
        times: [],
        taxonomy: {},
      });
    }
    const s = map.get(d)!;
    s.attempted++;
    const tax = row.fail_taxonomy || (isAdapterFailure(row) ? "adapter_error" : "other");
    s.taxonomy[tax] = (s.taxonomy[tax] ?? 0) + 1;
    if (tax === "boundary_mismatch" || tax === "whole_program_output") {
      s.invalidBoundary++;
    }
    if (!isAdapterFailure(row) && tax !== "boundary_mismatch" && tax !== "whole_program_output") {
      s.adapterClean++;
    }
    if (row.fail_category === "no_wrapper" || tax === "no_wrapper") {
      s.noWrapper++;
    } else if (
      row.semantic_score !== null &&
      row.semantic_score !== undefined &&
      !isAdapterFailure(row)
    ) {
      s.semanticScores.push(row.semantic_score);
    }
    if (row.time_ms > 0) s.times.push(row.time_ms);
  }

  return Array.from(map.entries())
    .map(([decompiler, s]) => ({
      decompiler,
      attempted: s.attempted,
      adapterClean: s.adapterClean,
      invalidBoundary: s.invalidBoundary,
      semanticTested: s.semanticScores.length,
      noWrapper: s.noWrapper,
      meanSemantic:
        s.semanticScores.length > 0
          ? s.semanticScores.reduce((a, b) => a + b, 0) / s.semanticScores.length
          : null,
      perfectRows: s.semanticScores.filter((v) => v >= 1).length,
      meanTimeMs:
        s.times.length > 0 ? s.times.reduce((a, b) => a + b, 0) / s.times.length : null,
      taxonomy: s.taxonomy,
      oracleSubject: null,
    }))
    .sort((a, b) => {
      if (a.decompiler === "fission") return -1;
      if (b.decompiler === "fission") return 1;
      return (b.meanSemantic ?? -1) - (a.meanSemantic ?? -1);
    });
}

/** @deprecated Use groupByDecompiler(envelope) — kept for call sites that only have rows. */
export function groupByDecompilerRows(rows: BenchmarkEnvelope["rows"]): MvpDecompilerStats[] {
  const stub = {
    schema_version: 2 as const,
    run: { official: false },
    toolchain: {},
    matrix: {
      expected_decompilers: [] as string[],
      expected_cells: [] as { decompiler: string; function_name: string; compiler_variant: string }[],
      expected_rows: 0,
      observed_rows: 0,
    },
    oracle: { mode: "example_cases" as const, valid: false },
    validity: { valid: false, publishable: false, reasons: [] as string[], publish_reasons: [] as string[] },
    rows,
  };
  return groupByDecompiler(stub as unknown as BenchmarkEnvelope);
}

export function getCrossVariantRows(data: BenchmarkEnvelope): CrossVariantRow[] {
  const raw = data.summary?.extensions?.cross_variant as
    | {
        by_decompiler_variant?: Record<
          string,
          Array<{
            compiler_variant: string;
            compiler: string;
            opt: string;
            tested_rows: number;
            mean_pass_rate: number | null;
            perfect_rows: number;
          }>
        >;
      }
    | undefined;
  if (!raw?.by_decompiler_variant) return [];
  const out: CrossVariantRow[] = [];
  for (const [decompiler, entries] of Object.entries(raw.by_decompiler_variant)) {
    for (const e of entries) {
      out.push({ decompiler, ...e });
    }
  }
  return out.sort((a, b) => {
    if (a.decompiler !== b.decompiler) {
      if (a.decompiler === "fission") return -1;
      if (b.decompiler === "fission") return 1;
      return a.decompiler.localeCompare(b.decompiler);
    }
    return a.compiler_variant.localeCompare(b.compiler_variant);
  });
}

export function getCfgSecondary(data: BenchmarkEnvelope): {
  status: string;
  byDecompiler: Record<string, { match?: number; mismatch?: number; match_rate?: number | null }>;
} {
  const cfg = data.summary?.secondary?.cfg as
    | {
        status?: string;
        by_decompiler?: Record<
          string,
          { match?: number; mismatch?: number; match_rate?: number | null }
        >;
      }
    | undefined;
  return {
    status: cfg?.status ?? "absent",
    byDecompiler: cfg?.by_decompiler ?? {},
  };
}

/** Get unique function names in the result */
export function getFunctionNames(rows: BenchmarkEnvelope["rows"]): string[] {
  return [...new Set(rows.map((r) => r.function_name))].sort();
}

/** Get rows for a specific function */
export function getRowsForFunction(rows: BenchmarkEnvelope["rows"], fn: string) {
  return rows.filter((r) => r.function_name === fn);
}
