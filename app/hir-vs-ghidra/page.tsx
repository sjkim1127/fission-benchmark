import { Suspense } from "react";
import { SiteChrome } from "@/components/SiteChrome";
import { UnavailableData } from "@/components/UnavailableData";
import { SkeletonSection } from "@/components/DashboardShared";
import { HirGhidraCompare } from "@/components/HirGhidraCompare";
import { getLatestBenchmarkOptional } from "@/lib/benchmark";
import styles from "../dashboard.module.css";

export const revalidate = 900;

export const metadata = {
  title: "HIR vs Ghidra · Readability comparison",
  description:
    "Fission's HIR printer next to Ghidra's own decompiled output, side by side — diagnostic only.",
};

async function CompareSection() {
  const data = await getLatestBenchmarkOptional();
  if (!data) {
    return <UnavailableData title="HIR vs Ghidra comparison unavailable" />;
  }

  const fissionRows = data.rows.filter((r) => r.decompiler === "fission");
  const ghidraRows = data.rows.filter((r) => r.decompiler === "ghidra");

  if (fissionRows.length === 0 || ghidraRows.length === 0) {
    return (
      <p className={styles.sectionLead}>
        This envelope doesn&apos;t have both fission and ghidra rows — re-run
        multi-decomp with both included.
      </p>
    );
  }

  return (
    <section className={styles.section}>
      <h2 className={styles.sectionTitle}>
        Fission HIR · Ghidra ·{" "}
        {new Set(fissionRows.map((r) => r.function_name)).size} functions
      </h2>
      <p className={styles.sectionLead}>
        Readability comparison only — never used for semantic ranking (that
        is Fission NIR vs. each tool&apos;s output, elsewhere on this
        dashboard). This is what a human reading each tool&apos;s output
        would actually see.
      </p>
      <HirGhidraCompare fissionRows={fissionRows} ghidraRows={ghidraRows} />
    </section>
  );
}

export default function HirVsGhidraPage() {
  return (
    <SiteChrome
      active="hir-ghidra"
      subtitle="HIR vs Ghidra — readability, side by side, not ranking"
    >
      <div className={styles.frame}>
        <div className={styles.frameTitle}>HIR vs Ghidra</div>
        <p className={styles.frameBody}>
          Fission&apos;s <strong>HIR</strong> (clone-only readability layer)
          next to Ghidra&apos;s own decompiled output for the same function.
          Semantic correctness is measured on Fission&apos;s NIR, not HIR —
          this page is purely a readability comparison.
        </p>
      </div>

      <Suspense fallback={<SkeletonSection rows={6} />}>
        <CompareSection />
      </Suspense>
    </SiteChrome>
  );
}
