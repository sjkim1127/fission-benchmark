import { Suspense } from "react";
import {
  getLatestBenchmark,
  groupByDecompiler,
  getFunctionNames,
  getCrossVariantRows,
  getCfgSecondary,
} from "@/lib/benchmark";
import { getParityTelemetry } from "@/lib/parity";
import { ValidityBanner } from "@/components/ValidityBanner";
import { SummaryTable } from "@/components/SummaryTable";
import { FunctionGrid } from "@/components/FunctionGrid";
import { CrossVariantTable } from "@/components/CrossVariantTable";
import { CfgSecondaryPanel } from "@/components/CfgSecondaryPanel";
import { ParityStageTable } from "@/components/ParityStageTable";
import styles from "./page.module.css";

// ISR: cache the rendered HTML output for 15 minutes.
// The raw JSON (~18-25 MB) is fetched server-side with cache:"no-store" and is
// NOT stored in the Next.js data cache. Only the rendered HTML is cached here.
export const revalidate = 900;

// Progressive streaming sections
async function MetaStrip() {
  const data = await getLatestBenchmark();
  const functionNames = getFunctionNames(data.rows);
  const stats = groupByDecompiler(data);
  const corpus = data.run?.corpus ?? "dev";
  const measuredAt = data.run?.finished_at
    ? new Date(data.run.finished_at).toLocaleString("en-US", {
        timeZone: "UTC",
        timeZoneName: "short",
      })
    : "not recorded";

  return (
    <div className={styles.heroMeta}>
      <span className={styles.metaItem}>
        <span className={styles.metaLabel}>Corpus</span>
        <code className={styles.metaValue}>{corpus}</code>
      </span>
      <span className={styles.metaItem}>
        <span className={styles.metaLabel}>Functions</span>
        <span className={styles.metaValue}>{functionNames.length}</span>
      </span>
      <span className={styles.metaItem}>
        <span className={styles.metaLabel}>Decompilers</span>
        <span className={styles.metaValue}>{stats.length}</span>
      </span>
      <span className={styles.metaItem}>
        <span className={styles.metaLabel}>Measured</span>
        <span className={styles.metaValue}>{measuredAt}</span>
      </span>
    </div>
  );
}

async function BannerSection() {
  const data = await getLatestBenchmark();
  return <ValidityBanner validity={data.validity} run={data.run} />;
}

async function SummarySection() {
  const data = await getLatestBenchmark();
  const stats = groupByDecompiler(data);
  return (
    <section className={styles.section}>
      <h2 className={styles.sectionTitle}>MVP Summary</h2>
      <p className={styles.sectionLead}>
        Semantic · Coverage · Fail taxonomy · Runtime (standard set)
      </p>
      <SummaryTable stats={stats} />
    </section>
  );
}

async function GridSection() {
  const data = await getLatestBenchmark();
  const functionNames = getFunctionNames(data.rows);
  return (
    <section className={styles.section}>
      <h2 className={styles.sectionTitle}>Per-Function Results</h2>
      {/* rows includes decompiled_code — passed as serialized RSC payload to the
          client component so the code modal works without a separate fetch */}
      <FunctionGrid functionNames={functionNames} rows={data.rows} />
    </section>
  );
}

async function CfgSection() {
  const data = await getLatestBenchmark();
  const cfg = getCfgSecondary(data);
  return (
    <section className={styles.section}>
      <h2 className={styles.sectionTitle}>Secondary · CFG match (envelope)</h2>
      <CfgSecondaryPanel status={cfg.status} byDecompiler={cfg.byDecompiler} />
    </section>
  );
}

async function ParitySection() {
  const telemetry = await getParityTelemetry();
  return (
    <section className={styles.section}>
      <h2 className={styles.sectionTitle}>Layered parity · Ghidra reference</h2>
      <p className={styles.sectionLead}>
        Assembly · p-code · CFG · function discovery (decode excluded until a
        real decode surface exists) — independent of decompiler-output quality
        scoring.
      </p>
      <ParityStageTable telemetry={telemetry} />
    </section>
  );
}

async function CrossVariantSection() {
  const data = await getLatestBenchmark();
  const rows = getCrossVariantRows(data);
  return (
    <section className={styles.section}>
      <h2 className={styles.sectionTitle}>Extension · Cross-compiler / opt</h2>
      <CrossVariantTable rows={rows} />
    </section>
  );
}

async function DiagnosticsNote() {
  return (
    <section className={styles.section}>
      <h2 className={styles.sectionTitle}>Diagnostics (non-ranking)</h2>
      <p className={styles.sectionLead}>
        Source similarity, AST structure similarity, and readability proxies remain
        on individual rows for triage. They do not affect correctness rank. Human
        readability scores require the study in{" "}
        <code>benchmark/readability/human_study.md</code>.
      </p>
    </section>
  );
}

function SkeletonMeta() {
  return (
    <div className={styles.heroMeta}>
      {Array.from({ length: 4 }).map((_, i) => (
        <span key={i} className={`${styles.metaItem} ${styles.skeleton}`}>
          <span className={styles.skeletonLine} style={{ width: 48 }} />
          <span className={styles.skeletonLine} style={{ width: 64 }} />
        </span>
      ))}
    </div>
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

export default function Home() {
  return (
    <div className={styles.page}>
      <header className={styles.header}>
        <div className={styles.headerInner}>
          <div className={styles.headerLeft}>
            <div className={styles.logo}>
              <span className={styles.logoIcon}>⚡</span>
              <span className={styles.logoText}>Fission</span>
              <span className={styles.logoBadge}>Benchmark</span>
            </div>
            <p className={styles.headerSub}>
              Standard set: semantic (original binary) · coverage · fail taxonomy ·
              runtime — Fission vs Ghidra, Boomerang, Radare2, angr, Snowman, rev.ng, Reko
            </p>
          </div>
          <div className={styles.headerLinks}>
            <a
              href="https://github.com/sjkim1127/fission-benchmark"
              target="_blank"
              rel="noopener noreferrer"
              className={styles.headerLink}
            >
              GitHub →
            </a>
          </div>
        </div>
      </header>

      <main className={styles.main}>
        {/* Each Suspense boundary streams independently.
            Browser receives HTML in order: meta → banner → summary → grid */}
        <Suspense fallback={<SkeletonMeta />}>
          <MetaStrip />
        </Suspense>

        <Suspense fallback={<div className={styles.bannerSkeleton} />}>
          <BannerSection />
        </Suspense>

        <Suspense fallback={<SkeletonSection rows={5} />}>
          <SummarySection />
        </Suspense>

        <Suspense fallback={<SkeletonSection rows={4} />}>
          <ParitySection />
        </Suspense>

        {/* Grid is largest — streams last while user reads the summary table */}
        <Suspense fallback={<SkeletonSection rows={8} />}>
          <GridSection />
        </Suspense>

        <Suspense fallback={<SkeletonSection rows={3} />}>
          <CfgSection />
        </Suspense>

        <Suspense fallback={<SkeletonSection rows={4} />}>
          <CrossVariantSection />
        </Suspense>

        <DiagnosticsNote />
      </main>

      <footer className={styles.footer}>
        <span>Fission Benchmark · Auto-updated on official runs · ISR 15 min</span>
        <a
          href="https://github.com/sjkim1127/fission-benchmark"
          target="_blank"
          rel="noopener noreferrer"
        >
          sjkim1127/fission-benchmark
        </a>
      </footer>
    </div>
  );
}
