import { Suspense } from "react";
import Link from "next/link";
import {
  getLatestBenchmarkOptional,
  getSameFunctionSummary,
} from "@/lib/benchmark";
import { SiteChrome } from "@/components/SiteChrome";
import { SameFunctionPanel } from "@/components/SameFunctionPanel";
import { UnavailableData } from "@/components/UnavailableData";
import {
  MetaStrip,
  SkeletonMeta,
  SkeletonSection,
} from "@/components/DashboardShared";
import styles from "../dashboard.module.css";

export const revalidate = 900;

export const metadata = {
  title: "Same-function matrix",
  description:
    "MVP-0 same-function honesty: direct_function / (direct + boundary_*) for each decompiler.",
};

async function MatrixSection() {
  const data = await getLatestBenchmarkOptional({ requirePublishable: true });
  if (!data) {
    return <UnavailableData title="Same-function matrix unavailable" />;
  }
  const sameFn = getSameFunctionSummary(data);
  return (
    <section className={styles.section}>
      <h2 className={styles.sectionTitle}>By decompiler</h2>
      <SameFunctionPanel summary={sameFn} />
    </section>
  );
}

export default function SameFunctionPage() {
  return (
    <SiteChrome
      active="same-function"
      subtitle="MVP-0 — request (binary, addr); not semantic ranking"
    >
      <div className={styles.frame}>
        <div className={styles.frameTitle}>Same-function matrix</div>
        <p className={styles.frameBody}>
          Each result row is one decompile request for a single entry{" "}
          <strong>(binary, addr)</strong>. Primary rate ={" "}
          <code>direct_function / (direct + boundary_*)</code> where boundary_*
          includes mismatch, whole-program, and no_output. This is{" "}
          <strong>infra honesty</strong>, not oracle correctness.
        </p>
        <p className={styles.frameNote}>
          Distinct from function discovery (inventory) and from Fission↔Ghidra
          IR parity.
        </p>
      </div>

      <p className={styles.sectionLead}>
        <Link href="/">← Overview</Link>
        {" · "}
        <Link href="/functions">Per-function code →</Link>
      </p>

      <Suspense fallback={<SkeletonMeta />}>
        <MetaStrip />
      </Suspense>

      <Suspense fallback={<SkeletonSection rows={5} />}>
        <MatrixSection />
      </Suspense>
    </SiteChrome>
  );
}
