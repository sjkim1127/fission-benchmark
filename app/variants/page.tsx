import { Suspense } from "react";
import Link from "next/link";
import {
  getLatestBenchmarkOptional,
  getCrossVariantRows,
} from "@/lib/benchmark";
import { SiteChrome } from "@/components/SiteChrome";
import { CrossVariantTable } from "@/components/CrossVariantTable";
import { UnavailableData } from "@/components/UnavailableData";
import {
  MetaStrip,
  SkeletonMeta,
  SkeletonSection,
} from "@/components/DashboardShared";
import styles from "../dashboard.module.css";

export const revalidate = 900;

export const metadata = {
  title: "Compiler × opt variants",
  description:
    "Semantic pass rates pivoted by compiler variant (gcc / gcc-m32 × optimization).",
};

async function VariantsSection() {
  const data = await getLatestBenchmarkOptional();
  if (!data) {
    return <UnavailableData title="Variant table unavailable" />;
  }
  const rows = getCrossVariantRows(data);
  return (
    <section className={styles.section}>
      <h2 className={styles.sectionTitle}>Cross-variant semantic means</h2>
      <p className={styles.sectionLead}>
        Extension pivot — how each decompiler behaves under compiler and opt
        changes. Ranking still uses overall semantic on Overview.
      </p>
      {rows.length === 0 ? (
        <p className={styles.sectionLead}>
          No cross-variant block in this envelope.
        </p>
      ) : (
        <CrossVariantTable rows={rows} />
      )}
    </section>
  );
}

export default function VariantsPage() {
  return (
    <SiteChrome
      active="variants"
      subtitle="Extension — semantic by compiler × optimization"
    >
      <div className={styles.frame}>
        <div className={styles.frameTitle}>Compiler × opt variants</div>
        <p className={styles.frameBody}>
          Break down semantic pass rates by <code>compiler_variant</code> (e.g.{" "}
          <code>gcc -O0</code>, <code>gcc-m32 -O2</code>). Useful for opt cliffs
          and ISA width (m32) triage.
        </p>
      </div>

      <p className={styles.sectionLead}>
        <Link href="/">← Overview</Link>
        {" · "}
        <Link href="/functions">Per-function →</Link>
      </p>

      <Suspense fallback={<SkeletonMeta />}>
        <MetaStrip />
      </Suspense>

      <Suspense fallback={<SkeletonSection rows={6} />}>
        <VariantsSection />
      </Suspense>
    </SiteChrome>
  );
}
