import { Suspense } from "react";
import Link from "next/link";
import {
  getLatestBenchmarkOptional,
  getFunctionNames,
} from "@/lib/benchmark";
import { SiteChrome } from "@/components/SiteChrome";
import { FunctionGrid } from "@/components/FunctionGrid";
import { UnavailableData } from "@/components/UnavailableData";
import {
  MetaStrip,
  SkeletonMeta,
  SkeletonSection,
} from "@/components/DashboardShared";
import styles from "../dashboard.module.css";

export const revalidate = 900;

export const metadata = {
  title: "Per-function results",
  description:
    "Side-by-side decompiled code for each corpus function across decompilers.",
};

async function GridSection() {
  const data = await getLatestBenchmarkOptional();
  if (!data) {
    return <UnavailableData title="Per-function grid unavailable" />;
  }
  const functionNames = getFunctionNames(data.rows);
  return (
    <section className={styles.section}>
      <h2 className={styles.sectionTitle}>
        Grid · {functionNames.length} functions
      </h2>
      <p className={styles.sectionLead}>
        Click a cell for decompiled source. Large payload — isolated from the
        overview for faster hub loads.
      </p>
      <FunctionGrid functionNames={functionNames} rows={data.rows} />
    </section>
  );
}

export default function FunctionsPage() {
  return (
    <SiteChrome
      active="functions"
      subtitle="Per-function decompiler outputs — browse, not ranking"
    >
      <div className={styles.frame}>
        <div className={styles.frameTitle}>Per-function results</div>
        <p className={styles.frameBody}>
          Browse every corpus function across adapters. Use{" "}
          <Link href="/">Overview</Link> for semantic means and{" "}
          <Link href="/same-function">Same-function</Link> for boundary rates.
        </p>
      </div>

      <Suspense fallback={<SkeletonMeta />}>
        <MetaStrip />
      </Suspense>

      <Suspense fallback={<SkeletonSection rows={10} />}>
        <GridSection />
      </Suspense>
    </SiteChrome>
  );
}
