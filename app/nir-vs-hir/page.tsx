import { Suspense } from "react";
import Link from "next/link";
import { SiteChrome } from "@/components/SiteChrome";
import { UnavailableData } from "@/components/UnavailableData";
import {
  MetaStrip,
  SkeletonMeta,
  SkeletonSection,
} from "@/components/DashboardShared";
import { NirHirCompare } from "@/components/NirHirCompare";
import { getLatestBenchmarkOptional } from "@/lib/benchmark";
import { loadFunctionSources } from "@/lib/source";
import styles from "../dashboard.module.css";

export const revalidate = 900;

export const metadata = {
  title: "NIR vs HIR · Source comparison",
  description:
    "Side-by-side original source, Fission NIR, and Fission HIR — diagnostic only.",
};

async function CompareSection() {
  const data = await getLatestBenchmarkOptional();
  if (!data) {
    return <UnavailableData title="NIR vs HIR comparison unavailable" />;
  }

  const corpus =
    typeof data.run?.corpus === "string" && data.run.corpus
      ? data.run.corpus
      : "dev";
  const sources = await loadFunctionSources(corpus);
  // Prefer holdout overlay for names that only appear there when corpus is mixed.
  if (corpus === "dev") {
    const holdout = await loadFunctionSources("holdout");
    for (const [k, v] of Object.entries(holdout)) {
      if (!sources[k]) sources[k] = v;
    }
  }

  const fissionRows = data.rows.filter((r) => r.decompiler === "fission");
  if (fissionRows.length === 0) {
    return (
      <p className={styles.sectionLead}>
        No Fission rows in this envelope. Re-run multi-decomp with fission
        included.
      </p>
    );
  }

  return (
    <section className={styles.section}>
      <h2 className={styles.sectionTitle}>
        Source · NIR · HIR · {new Set(fissionRows.map((r) => r.function_name)).size}{" "}
        functions
      </h2>
      <p className={styles.sectionLead}>
        Fission dual printers only. Semantic correctness is measured on NIR;
        HIR is the human-oriented surface. Original C is loaded from the corpus
        tree checked into this repo.
      </p>
      <NirHirCompare fissionRows={fissionRows} sources={sources} />
    </section>
  );
}

export default function NirVsHirPage() {
  return (
    <SiteChrome
      active="nir-hir"
      subtitle="Source · NIR · HIR — dual-layer diagnostic, not ranking"
    >
      <div className={styles.frame}>
        <div className={styles.frameTitle}>Fission NIR vs HIR</div>
        <p className={styles.frameBody}>
          Compare original corpus source with Fission{" "}
          <strong>NIR</strong> (semantic) and <strong>HIR</strong> (readability)
          for the same function and compiler variant. Multi-tool code browse
          remains on <Link href="/functions">Functions</Link>; semantic means on{" "}
          <Link href="/">Overview</Link>.
        </p>
      </div>

      <Suspense fallback={<SkeletonMeta />}>
        <MetaStrip />
      </Suspense>

      <Suspense fallback={<SkeletonSection rows={8} />}>
        <CompareSection />
      </Suspense>
    </SiteChrome>
  );
}
