import { Suspense } from "react";
import { SiteChrome } from "@/components/SiteChrome";
import { UnavailableData } from "@/components/UnavailableData";
import { SkeletonSection } from "@/components/DashboardShared";
import { ReleaseComparisonPanel } from "@/components/ReleaseComparisonPanel";
import { VersionTrendChart } from "@/components/VersionTrendChart";
import { getLatestBenchmarkOptional } from "@/lib/benchmark";
import { getReleaseComparison, getVersionTrend } from "@/lib/history";
import styles from "../dashboard.module.css";

export const revalidate = 900;

export const metadata = {
  title: "Releases · What changed",
  description:
    "Fission's own semantic pass rate across releases, and what changed since the last one.",
};

async function ComparisonSection() {
  const data = await getLatestBenchmarkOptional();
  if (!data) return <UnavailableData title="Release comparison unavailable" />;
  const comparison = await getReleaseComparison(data);
  if (!comparison) {
    return (
      <p className={styles.sectionLead}>
        No older archived release to compare against yet (this is either the
        first archived release, or the previous one has no multi-decomp
        snapshot — e.g. v0.1.5 shipped without one).
      </p>
    );
  }
  return <ReleaseComparisonPanel comparison={comparison} />;
}

async function TrendSection() {
  const points = await getVersionTrend();
  return <VersionTrendChart points={points} />;
}

export default function ReleasesPage() {
  return (
    <SiteChrome active="releases" subtitle="Release-over-release — Fission's own trend, not a re-ranking">
      <div className={styles.frame}>
        <div className={styles.frameTitle}>Releases</div>
        <p className={styles.frameBody}>
          Every archived <code>public/benchmark-history/&lt;version&gt;.json</code>{" "}
          is Fission&apos;s own measured envelope at that release, keyed by{" "}
          <code>toolchain.fission_version</code>. Other decompilers are shown
          for stability context only — this page never re-ranks tools.
        </p>
      </div>

      <section className={styles.section}>
        <h2 className={styles.sectionTitle}>Trend since the earliest archived release</h2>
        <p className={styles.sectionLead}>
          Semantic pass rate over time. Dot size shows the corpus size
          measured at that release — watch for it changing alongside the
          rate, since a bigger corpus is a harder bar to clear.
        </p>
        <Suspense fallback={<SkeletonSection rows={4} />}>
          <TrendSection />
        </Suspense>
      </section>

      <section className={styles.section}>
        <h2 className={styles.sectionTitle}>Latest release vs. previous</h2>
        <Suspense fallback={<SkeletonSection rows={5} />}>
          <ComparisonSection />
        </Suspense>
      </section>
    </SiteChrome>
  );
}
