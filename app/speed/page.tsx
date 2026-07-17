import { Suspense } from "react";
import { SiteChrome } from "@/components/SiteChrome";
import { ValidityBanner } from "@/components/ValidityBanner";
import { UnavailableData } from "@/components/UnavailableData";
import {
  MetaStrip,
  SkeletonMeta,
  SkeletonSection,
} from "@/components/DashboardShared";
import { getLatestBenchmarkOptional } from "@/lib/benchmark";
import {
  fissionByVariant,
  fissionSlowestFunctions,
  fissionVsGhidraPaired,
  pairSummary,
  speedByDecompiler,
} from "@/lib/speed";
import {
  DecompilerSpeedTable,
  PairedSpeedTable,
  SlowestFunctionsTable,
  VariantSpeedTable,
} from "@/components/SpeedPanel";
import styles from "../dashboard.module.css";

export const revalidate = 900;

export const metadata = {
  title: "Speed · Decompile latency",
  description:
    "Fission and multi-decompiler decompile wall times (time_ms) — non-ranking diagnostics.",
};

async function BannerSection() {
  const data = await getLatestBenchmarkOptional();
  if (!data) return null;
  return <ValidityBanner validity={data.validity} run={data.run} />;
}

function Tile({
  label,
  value,
  hint,
}: {
  label: string;
  value: string;
  hint?: string;
}) {
  return (
    <div className={styles.frame}>
      <div className={styles.frameTitle}>{label}</div>
      <p className={styles.frameBody} style={{ fontSize: "1.35rem", fontWeight: 700 }}>
        {value}
      </p>
      {hint ? (
        <p className={styles.sectionLead} style={{ marginTop: "0.35rem", marginBottom: 0 }}>
          {hint}
        </p>
      ) : null}
    </div>
  );
}

function fmtMs(v: number | null | undefined): string {
  if (v == null || Number.isNaN(v)) return "—";
  if (v >= 1000) return `${(v / 1000).toFixed(2)}s`;
  return `${Math.round(v)}ms`;
}

function fmtX(v: number | null | undefined): string {
  if (v == null || Number.isNaN(v)) return "—";
  return `${v.toFixed(2)}×`;
}

async function SpeedBody() {
  const data = await getLatestBenchmarkOptional();
  if (!data) {
    return (
      <section className={styles.section}>
        <h2 className={styles.sectionTitle}>Speed</h2>
        <UnavailableData title="Speed diagnostics unavailable" />
      </section>
    );
  }

  const byDec = speedByDecompiler(data);
  const fission = byDec.find((r) => r.decompiler === "fission");
  const ghidra = byDec.find((r) => r.decompiler === "ghidra");
  const pairs = fissionVsGhidraPaired(data);
  const pair = pairSummary(pairs);
  const slowest = fissionSlowestFunctions(data, 30);
  const variants = fissionByVariant(data);

  return (
    <>
      <section className={styles.section}>
        <h2 className={styles.sectionTitle}>Decompile speed</h2>
        <p className={styles.sectionLead}>
          Wall time from the decompiler adapter (<code>time_ms</code> on each
          row) — typically one binary batch decompile, amortized per function.
          Semantic / wine / oracle time is <strong>not</strong> included. This
          page is a <strong>non-ranking</strong> practicality diagnostic (same
          policy as Quality EXT).
        </p>
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fill, minmax(160px, 1fr))",
            gap: "0.75rem",
            marginBottom: "1.25rem",
          }}
        >
          <Tile
            label="Fission mean"
            value={fmtMs(fission?.mean)}
            hint={fission ? `n=${fission.timedRows} · p95 ${fmtMs(fission.p95)}` : undefined}
          />
          <Tile
            label="Fission p50"
            value={fmtMs(fission?.p50)}
            hint="Median decompile latency"
          />
          <Tile
            label="Ghidra mean"
            value={fmtMs(ghidra?.mean)}
            hint={ghidra ? `n=${ghidra.timedRows} · p95 ${fmtMs(ghidra.p95)}` : undefined}
          />
          <Tile
            label="Paired speedup"
            value={fmtX(pair.medianSpeedup)}
            hint={
              pair.n
                ? `median ghidra/fission · n=${pair.n} pairs · geo ${fmtX(pair.geometricMeanSpeedup)}`
                : "Need both tools on same cells"
            }
          />
          <Tile
            label="Fission faster"
            value={
              pair.fissionFasterShare != null
                ? `${(pair.fissionFasterShare * 100).toFixed(0)}%`
                : "—"
            }
            hint="Share of paired cells with fission_ms < ghidra_ms"
          />
        </div>
      </section>

      <section className={styles.section}>
        <h2 className={styles.sectionTitle}>By decompiler</h2>
        <div className={styles.frame}>
          <DecompilerSpeedTable rows={byDec} />
        </div>
      </section>

      <section className={styles.section}>
        <h2 className={styles.sectionTitle}>Fission ↔ Ghidra (paired)</h2>
        <div className={styles.frame}>
          <PairedSpeedTable pairs={pairs} limit={40} />
        </div>
      </section>

      <section className={styles.section}>
        <h2 className={styles.sectionTitle}>Slowest Fission functions</h2>
        <div className={styles.frame}>
          <SlowestFunctionsTable rows={slowest} />
        </div>
      </section>

      <section className={styles.section}>
        <h2 className={styles.sectionTitle}>Fission by compiler variant</h2>
        <div className={styles.frame}>
          <VariantSpeedTable rows={variants} />
        </div>
      </section>
    </>
  );
}

export default function SpeedPage() {
  return (
    <SiteChrome active="speed" subtitle="Decompile latency · non-ranking">
      <Suspense fallback={<div className={styles.bannerSkeleton} />}>
        <BannerSection />
      </Suspense>
      <Suspense fallback={<SkeletonMeta />}>
        <MetaStrip />
      </Suspense>
      <Suspense fallback={<SkeletonSection />}>
        <SpeedBody />
      </Suspense>
    </SiteChrome>
  );
}
