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
  const envelope = await getLatestBenchmarkOptional({ requirePublishable: true });
  if (!envelope) {
    throw new Error("Failed to load a publishable official benchmark envelope");
  }
  return envelope;
}

/**
 * Load envelope without throwing. Parity page can still render telemetry when
 * the multi-decomp artifact is missing or not yet publishable.
 */
export async function getLatestBenchmarkOptional(options?: {
  requirePublishable?: boolean;
}): Promise<BenchmarkEnvelope | null> {
  // Intentionally NOT using Next.js data cache (next.tags) here because the raw
  // JSON is ~18-25 MB and exceeds the 2 MB per-entry cache limit.
  // ISR is instead applied at the route segment level via `export const revalidate`.
  try {
    const res = await fetch(LATEST_URL, { cache: "no-store" });
    if (!res.ok) return null;
    const raw: unknown = await res.json();
    const envelope = BenchmarkEnvelopeSchema.parse(raw);
    if (options?.requirePublishable !== false) {
      if (envelope.validity?.publishable !== true) return null;
    }
    return envelope;
  } catch {
    return null;
  }
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

export const CORE_DECOMPILERS = ["fission", "ghidra"] as const;

export type SameFunctionToolStats = {
  decompiler: string;
  cohort: string | null;
  sameFunctionRate: number | null;
  sameFunctionLooseRate: number | null;
  byStatus: Record<string, number>;
};

export type SameFunctionSummary = {
  schema: string | null;
  coreRate: number | null;
  multiRate: number | null;
  allRate: number | null;
  coreLoose: number | null;
  multiLoose: number | null;
  byDecompiler: SameFunctionToolStats[];
  addressAnchorRate: number | null;
};

/** MVP-0 same-function matrix from envelope.summary (if present). */
export function getSameFunctionSummary(
  data: BenchmarkEnvelope
): SameFunctionSummary | null {
  const raw = (data.summary?.mvp as { same_function?: Record<string, unknown> } | undefined)
    ?.same_function;
  if (!raw || typeof raw !== "object") return null;

  const cohorts = (raw.cohorts || {}) as Record<
    string,
    {
      same_function_rate?: number | null;
      same_function_loose_rate?: number | null;
    }
  >;
  const by = (raw.by_decompiler || {}) as Record<
    string,
    {
      cohort?: string;
      same_function_rate?: number | null;
      same_function_loose_rate?: number | null;
      by_status?: Record<string, number>;
    }
  >;
  const totals = (raw.totals || {}) as {
    address_anchor_rate?: number | null;
  };

  const byDecompiler: SameFunctionToolStats[] = Object.entries(by)
    .map(([decompiler, s]) => ({
      decompiler,
      cohort: s.cohort ?? null,
      sameFunctionRate:
        s.same_function_rate === undefined || s.same_function_rate === null
          ? null
          : Number(s.same_function_rate),
      sameFunctionLooseRate:
        s.same_function_loose_rate === undefined || s.same_function_loose_rate === null
          ? null
          : Number(s.same_function_loose_rate),
      byStatus: s.by_status ?? {},
    }))
    .sort((a, b) => {
      if (a.decompiler === "fission") return -1;
      if (b.decompiler === "fission") return 1;
      if (a.decompiler === "ghidra") return -1;
      if (b.decompiler === "ghidra") return 1;
      return a.decompiler.localeCompare(b.decompiler);
    });

  return {
    schema: typeof raw.schema === "string" ? raw.schema : null,
    coreRate: cohorts.core?.same_function_rate ?? null,
    multiRate: cohorts.multi?.same_function_rate ?? null,
    allRate: cohorts.all?.same_function_rate ?? null,
    coreLoose: cohorts.core?.same_function_loose_rate ?? null,
    multiLoose: cohorts.multi?.same_function_loose_rate ?? null,
    byDecompiler,
    addressAnchorRate: totals.address_anchor_rate ?? null,
  };
}

/** Filter MVP stats / rows to the Fission + Ghidra core pair. */
export function filterCorePairStats(
  stats: MvpDecompilerStats[]
): MvpDecompilerStats[] {
  const set = new Set<string>(CORE_DECOMPILERS);
  return stats.filter((s) => set.has(s.decompiler));
}

export function filterCorePairRows(
  rows: BenchmarkEnvelope["rows"]
): BenchmarkEnvelope["rows"] {
  const set = new Set<string>(CORE_DECOMPILERS);
  return rows.filter((r) => set.has(r.decompiler));
}

export function pct(rate: number | null | undefined, digits = 1): string {
  if (rate === null || rate === undefined || Number.isNaN(rate)) return "—";
  return `${(rate * 100).toFixed(digits)}%`;
}
