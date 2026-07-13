import { Suspense } from "react";
import Link from "next/link";
import {
  getLatestBenchmark,
  groupByDecompiler,
  getFunctionNames,
  getCrossVariantRows,
  getSameFunctionSummary,
} from "@/lib/benchmark";
import { SiteChrome } from "@/components/SiteChrome";
import { ValidityBanner } from "@/components/ValidityBanner";
import { SummaryTable } from "@/components/SummaryTable";
import { FunctionGrid } from "@/components/FunctionGrid";
import { CrossVariantTable } from "@/components/CrossVariantTable";
import { SameFunctionPanel } from "@/components/SameFunctionPanel";
import styles from "./dashboard.module.css";

// ISR: cache the rendered HTML output for 15 minutes.
export const revalidate = 900;

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
      <h2 className={styles.sectionTitle}>MVP · Semantic ranking</h2>
      <p className={styles.sectionLead}>
        Only <strong>semantic pass rate</strong> ranks tools. Coverage and fail
        taxonomy keep denominators honest. Multi-decompiler fairness surface —
        not IR kinship with Ghidra.
      </p>
      <SummaryTable stats={stats} />
    </section>
  );
}

async function SameFunctionSection() {
  const data = await getLatestBenchmark();
  const sameFn = getSameFunctionSummary(data);
  return (
    <section className={styles.section}>
      <h2 className={styles.sectionTitle}>MVP-0 · Same-function matrix</h2>
      <p className={styles.sectionLead}>
        Did each adapter decompile the <strong>requested</strong>{" "}
        <code>(binary, addr)</code>? Infra honesty — separate from oracle
        correctness.
      </p>
      <SameFunctionPanel summary={sameFn} />
    </section>
  );
}

async function GridSection() {
  const data = await getLatestBenchmark();
  const functionNames = getFunctionNames(data.rows);
  return (
    <section className={styles.section}>
      <h2 className={styles.sectionTitle}>Per-function results</h2>
      <p className={styles.sectionLead}>
        Side-by-side decompiler outputs for each corpus function (click a cell
        for code).
      </p>
      <FunctionGrid functionNames={functionNames} rows={data.rows} />
    </section>
  );
}

async function CrossVariantSection() {
  const data = await getLatestBenchmark();
  const rows = getCrossVariantRows(data);
  return (
    <section className={styles.section}>
      <h2 className={styles.sectionTitle}>Extension · Cross-compiler / opt</h2>
      <p className={styles.sectionLead}>
        Semantic means pivoted by compiler variant (gcc / gcc-m32 × opt).
      </p>
      <CrossVariantTable rows={rows} />
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
    <SiteChrome
      active="multi"
      subtitle="Multi-decompiler quality — semantic oracle, coverage, same-function honesty"
    >
      <div className={styles.frame}>
        <div className={styles.frameTitle}>Multi-decompiler quality</div>
        <p className={styles.frameBody}>
          Compare <strong>Fission</strong> against open decompilers on the same
          corpus under an <strong>original_binary</strong> oracle. Ranking axis
          is semantic pass rate only. Layered p-code / assembly / CFG agreement
          with Ghidra lives on a separate page — Fission shares a p-code-class
          IR, so that comparison is structural kinship, not a multi-tool score.
        </p>
      </div>

      <div className={styles.cardGrid}>
        <Link href="/fission-vs-ghidra" className={styles.card}>
          <div className={styles.cardKicker}>Shared IR</div>
          <div className={styles.cardTitle}>Fission ↔ Ghidra parity</div>
          <p className={styles.cardBody}>
            Assembly, p-code dual metrics, CFG, and function discovery vs Ghidra
            as reference — not a ranking table.
          </p>
          <div className={styles.cardCta}>Open layered parity →</div>
        </Link>
        <div className={styles.card} style={{ cursor: "default" }}>
          <div className={styles.cardKicker}>This page</div>
          <div className={styles.cardTitle}>Semantic multi-matrix</div>
          <p className={styles.cardBody}>
            MVP semantic · coverage · taxonomy · same-function · per-function
            grid · cross-compiler pivots.
          </p>
        </div>
      </div>

      <Suspense fallback={<SkeletonMeta />}>
        <MetaStrip />
      </Suspense>

      <Suspense fallback={<div className={styles.bannerSkeleton} />}>
        <BannerSection />
      </Suspense>

      <Suspense fallback={<SkeletonSection rows={5} />}>
        <SummarySection />
      </Suspense>

      <Suspense fallback={<SkeletonSection rows={3} />}>
        <SameFunctionSection />
      </Suspense>

      <Suspense fallback={<SkeletonSection rows={8} />}>
        <GridSection />
      </Suspense>

      <Suspense fallback={<SkeletonSection rows={4} />}>
        <CrossVariantSection />
      </Suspense>

      <section className={styles.section}>
        <h2 className={styles.sectionTitle}>Diagnostics (non-ranking)</h2>
        <p className={styles.sectionLead}>
          Source similarity, AST proxies, and readability scores stay on row
          detail for triage. They never rank tools. Human readability requires
          the study pack in <code>benchmark/readability/</code>.
        </p>
      </section>
    </SiteChrome>
  );
}
