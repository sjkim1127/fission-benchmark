import { Suspense } from "react";
import Link from "next/link";
import {
  getLatestBenchmarkOptional,
  groupByDecompiler,
  filterCorePairStats,
  getSameFunctionSummary,
  pct,
} from "@/lib/benchmark";
import { getParityTelemetry } from "@/lib/parity";
import { SiteChrome } from "@/components/SiteChrome";
import { CorePairPanel } from "@/components/CorePairPanel";
import { DualMetricsTiles } from "@/components/DualMetricsTiles";
import { ParityStageTable } from "@/components/ParityStageTable";
import { SameFunctionPanel } from "@/components/SameFunctionPanel";
import styles from "../dashboard.module.css";

export const revalidate = 900;

export const metadata = {
  title: "Fission ↔ Ghidra · Layered parity",
  description:
    "Shared p-code-class IR comparison: assembly, p-code dual metrics, CFG, and function discovery with Ghidra as reference — not multi-decompiler ranking.",
};

async function DualSection() {
  const telemetry = await getParityTelemetry();
  return (
    <section className={styles.section}>
      <h2 className={styles.sectionTitle}>Dual metrics at a glance</h2>
      <p className={styles.sectionLead}>
        Prefer dual rates for triage. Strict set / full equality is intentionally
        hard (CRT, space IDs, inventory heuristics).
      </p>
      <DualMetricsTiles telemetry={telemetry} />
    </section>
  );
}

async function StageTableSection() {
  const telemetry = await getParityTelemetry();
  return (
    <section className={styles.section}>
      <h2 className={styles.sectionTitle}>Layer stack · full telemetry</h2>
      <p className={styles.sectionLead}>
        Primary publishable stages: assembly · p-code · CFG · function discovery.
        Decode / extension tracks are listed but not headline quality.
      </p>
      <ParityStageTable telemetry={telemetry} />
    </section>
  );
}

async function CoreSemanticSection() {
  const data = await getLatestBenchmarkOptional({ requirePublishable: false });
  if (!data) {
    return (
      <section className={styles.section}>
        <h2 className={styles.sectionTitle}>Core pair · semantic side-by-side</h2>
        <p className={styles.sectionLead}>
          Official multi-decomp envelope not available — parity tiles above still
          stand alone. Publish an official run to populate semantic cards.
        </p>
      </section>
    );
  }
  const stats = filterCorePairStats(groupByDecompiler(data));
  const sameFn = getSameFunctionSummary(data);
  const corpus = data.run?.corpus ?? "?";
  return (
    <>
      <section className={styles.section}>
        <h2 className={styles.sectionTitle}>Core pair · semantic side-by-side</h2>
        <p className={styles.sectionLead}>
          From the multi-decomp envelope (<code>{corpus}</code>), filtered to
          Fission + Ghidra only. Useful context —{" "}
          <strong>not</strong> the ranking surface for other tools (see{" "}
          <Link href="/">Multi-decompiler</Link>).
        </p>
        <CorePairPanel stats={stats} />
      </section>
      <section className={styles.section}>
        <h2 className={styles.sectionTitle}>Core · same-function rates</h2>
        <p className={styles.sectionLead}>
          Boundary contract on the core pair (expected ~1.0 after address anchors).
          {sameFn?.coreRate != null
            ? ` Core cohort rate: ${pct(sameFn.coreRate)}.`
            : ""}
        </p>
        <SameFunctionPanel summary={sameFn} compact />
      </section>
    </>
  );
}

function SkeletonSection({ rows = 4 }: { rows?: number }) {
  return (
    <section className={styles.section}>
      <div className={`${styles.skeletonLine} ${styles.sectionTitleSkeleton}`} />
      {Array.from({ length: rows }).map((_, i) => (
        <div key={i} className={`${styles.skeletonLine} ${styles.skeletonRow}`} />
      ))}
    </section>
  );
}

export default function FissionVsGhidraPage() {
  return (
    <SiteChrome
      active="parity"
      subtitle="Shared p-code-class IR · Ghidra is reference · Fission is candidate"
    >
      <div className={`${styles.frame} ${styles.frameParity}`}>
        <div className={styles.frameTitle}>Fission ↔ Ghidra layered parity</div>
        <p className={styles.frameBody}>
          Fission and Ghidra share a <strong>p-code-class intermediate
          representation</strong>. This page measures structural agreement —
          assembly bytes, p-code ops (strict/loose dual), CFG topology, and
          function inventories — with <strong>Ghidra as reference</strong> and{" "}
          <strong>Fission as candidate</strong>.
        </p>
        <p className={styles.frameNote}>
          Match rates here are not multi-decompiler quality rankings. Oracle
          semantic pass rate lives on the Multi-decompiler page.
        </p>
      </div>

      <div className={styles.cardGrid}>
        <Link href="/" className={styles.card}>
          <div className={styles.cardKicker}>Ranking surface</div>
          <div className={styles.cardTitle}>Multi-decompiler quality →</div>
          <p className={styles.cardBody}>
            Semantic oracle, coverage, same-function matrix, and full tool grid.
          </p>
        </Link>
        <div className={styles.card} style={{ cursor: "default" }}>
          <div className={styles.cardKicker}>Reference contract</div>
          <div className={styles.cardTitle}>Ghidra inventory &amp; IR</div>
          <p className={styles.cardBody}>
            Unified runner: <code>python -m runner.run_parity</code> with
            decompilers fission,ghidra.
          </p>
        </div>
      </div>

      <Suspense fallback={<SkeletonSection rows={3} />}>
        <DualSection />
      </Suspense>

      <Suspense fallback={<SkeletonSection rows={6} />}>
        <StageTableSection />
      </Suspense>

      <Suspense fallback={<SkeletonSection rows={4} />}>
        <CoreSemanticSection />
      </Suspense>

      <section className={styles.section}>
        <h2 className={styles.sectionTitle}>Reproduce</h2>
        <div className={styles.repro}>
          <pre>{`export FISSION_HOST_PORT=8007
python -m runner.run_parity --corpus dev --limit 20 --decompilers fission,ghidra
python -m benchmark.telemetry.aggregate
# → public/parity-telemetry.json

python -m benchmark.function_discovery.run --limit 10
python scripts/check_reliability.py public/parity-telemetry.json`}</pre>
        </div>
      </section>
    </SiteChrome>
  );
}
