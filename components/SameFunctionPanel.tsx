import styles from "./SummaryTable.module.css";
import type { SameFunctionSummary } from "@/lib/benchmark";
import { pct } from "@/lib/benchmark";

const COLORS: Record<string, string> = {
  fission: "#6366f1",
  ghidra: "#10b981",
  angr: "#f59e0b",
  radare2: "#ec4899",
  boomerang: "#14b8a6",
  snowman: "#8b5cf6",
  revng: "#f97316",
  reko: "#06b6d4",
};

export function SameFunctionPanel({
  summary,
  compact = false,
}: {
  summary: SameFunctionSummary | null;
  compact?: boolean;
}) {
  if (!summary || summary.byDecompiler.length === 0) {
    return (
      <p className={styles.hint}>
        Same-function matrix not present in this envelope. Rebuild with a runner
        that attaches <code>summary.mvp.same_function</code> (schema{" "}
        <code>same-function-matrix-v1</code>).
      </p>
    );
  }

  const tools = compact
    ? summary.byDecompiler.filter((t) =>
        ["fission", "ghidra"].includes(t.decompiler)
      )
    : summary.byDecompiler;

  return (
    <div className={styles.wrap}>
      <p className={styles.hint}>
        Request contract <strong>(binary, addr)</strong> — did the adapter return
        that function unit? Primary rate ={" "}
        <code>direct / (direct + boundary_*)</code>. Not a semantic ranking axis.
        {summary.addressAnchorRate != null
          ? ` Address anchor rate: ${pct(summary.addressAnchorRate)}.`
          : null}
      </p>
      <p className={styles.hint}>
        Cohorts — core: <strong>{pct(summary.coreRate)}</strong>
        {summary.coreLoose != null ? ` (loose ${pct(summary.coreLoose)})` : ""} ·
        multi: <strong>{pct(summary.multiRate)}</strong>
        {summary.multiLoose != null ? ` (loose ${pct(summary.multiLoose)})` : ""} ·
        all: <strong>{pct(summary.allRate)}</strong>
      </p>
      <table className={styles.table}>
        <thead>
          <tr>
            <th>Decompiler</th>
            <th>Cohort</th>
            <th className={styles.num}>same_fn_rate</th>
            <th className={styles.num}>loose_rate</th>
            <th>Status counts</th>
          </tr>
        </thead>
        <tbody>
          {tools.map((t) => {
            const color = COLORS[t.decompiler] ?? "#94a3b8";
            const status = Object.entries(t.byStatus)
              .filter(([, n]) => n > 0)
              .map(([k, n]) => `${k}:${n}`)
              .join(" · ");
            return (
              <tr
                key={t.decompiler}
                className={
                  t.decompiler === "fission" ? styles.fissionRow : undefined
                }
              >
                <td>
                  <span className={styles.dot} style={{ background: color }} />
                  <strong
                    style={{
                      color: t.decompiler === "fission" ? color : "inherit",
                    }}
                  >
                    {t.decompiler}
                  </strong>
                </td>
                <td className={styles.tax}>{t.cohort ?? "—"}</td>
                <td className={styles.num}>{pct(t.sameFunctionRate)}</td>
                <td className={styles.num}>{pct(t.sameFunctionLooseRate)}</td>
                <td className={styles.tax}>{status || "—"}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}
