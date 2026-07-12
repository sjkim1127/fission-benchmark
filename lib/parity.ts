export type ParityStageDetail = {
  total: number;
  match: number;
  mismatch: number;
  error_or_other: number;
  match_rate: number | null;
  mismatch_rate: number | null;
  match_rate_attempted?: number | null;
  usable_coverage?: number | null;
  skipped?: number;
  fetch_error?: number;
  by_status: Record<string, number>;
  by_mismatch_kind: Record<string, number>;
};

export type ParityReliability = {
  usable_coverage?: number | null;
  match_rate_comparable?: number | null;
  match_rate_attempted?: number | null;
  fetch_error_rate?: number | null;
  skipped_rate?: number | null;
};

export type ParityPublishable = {
  stages?: Record<string, ParityStageDetail>;
  total_rows?: number;
  match?: number;
  mismatch?: number;
  match_rate_comparable?: number | null;
  usable_coverage?: number | null;
};

export type ParityTelemetry = {
  schema?: string;
  total_rows: number;
  by_stage: Record<string, number>;
  by_status: Record<string, number>;
  by_mismatch_kind: Record<string, number>;
  by_variant?: Record<string, number>;
  by_pair?: Record<string, number>;
  stages?: Record<string, ParityStageDetail>;
  sources?: string[];
  reliability?: ParityReliability;
  canonicalize_mode?: string;
  non_publishable_stages?: string[];
  publishable?: ParityPublishable;
};

const LOCAL_URL =
  process.env.PARITY_TELEMETRY_URL ?? "/parity-telemetry.json";

const REMOTE_FALLBACK =
  process.env.PARITY_TELEMETRY_REMOTE_URL ??
  "https://raw.githubusercontent.com/sjkim1127/fission-benchmark/main/results/telemetry/latest.json";

export async function getParityTelemetry(): Promise<ParityTelemetry | null> {
  for (const url of [LOCAL_URL, REMOTE_FALLBACK]) {
    try {
      const res = await fetch(url, { cache: "no-store" });
      if (!res.ok) continue;
      const data = (await res.json()) as ParityTelemetry;
      if (typeof data.total_rows === "number") return data;
    } catch {
      // try next source
    }
  }
  return null;
}
