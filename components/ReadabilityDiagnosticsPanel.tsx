import Link from "next/link";
import type { ReadabilityDiagStats } from "@/lib/benchmark";
import { meanFmt } from "@/lib/benchmark";
import tableStyles from "@/components/SummaryTable.module.css";
import styles from "@/app/dashboard.module.css";

const DECOMPILER_COLORS: Record<string, string> = {
  fission: "#6366f1",
  ghidra: "#10b981",
  angr: "#f59e0b",
  radare2: "#ec4899",
  boomerang: "#14b8a6",
  snowman: "#8b5cf6",
  revng: "#f97316",
  reko: "#06b6d4",
  retdec: "#64748b",
};

type Props = {
  stats: ReadabilityDiagStats[];
  /** Compact overview: fewer columns + CTA to /quality */
  compact?: boolean;
  showStudyNote?: boolean;
};

/**
 * Non-ranking readability / similarity diagnostics.
 * Sort order is fixed (fission, ghidra, then alpha) — never by proxy score.
 */
export function ReadabilityDiagnosticsPanel({
  stats,
  compact = false,
  showStudyNote = true,
}: Props) {
  if (stats.length === 0) {
    return (
      <p className={styles.sectionLead}>
        No readability diagnostics on this envelope yet. Re-run the multi-decomp
        benchmark after a runner that emits{" "}
        <code>readability_metrics</code> / <code>readability_proxy_score</code>.
      </p>
    );
  }

  return (
    <div>
      <div className={styles.frame} style={{ marginBottom: "1rem" }}>
        <div className={styles.frameTitle}>Policy · diagnostics only</div>
        <p className={styles.frameBody}>
          Source similarity, AST tree-edit proxies, and readability proxies
          (goto / temps / generic names / flag soup) are{" "}
          <strong>not ranking axes</strong>. Semantic pass rate on the
          original-binary oracle remains the only tool ranking signal. Table
          order is fixed (Fission, Ghidra, then alphabetical) — not sorted by
          proxy score.
          {showStudyNote ? (
            <>
              {" "}
              Human study materials:{" "}
              <code>benchmark/readability/</code> (Phase 3 before any composite).
            </>
          ) : null}
        </p>
      </div>

      <div className={tableStyles.wrap}>
        <table className={tableStyles.table}>
          <thead>
            <tr>
              <th>Decompiler</th>
              <th className={tableStyles.num}>Rows</th>
              <th className={tableStyles.num} title="Mean source string similarity (diagnostic)">
                Src sim
              </th>
              <th
                className={tableStyles.num}
                title="Mean Zhang-Shasha AST similarity (control-flow view when available)"
              >
                AST sim
              </th>
              <th
                className={tableStyles.num}
                title="Mean unvalidated readability proxy (0–1; not a ranking score)"
              >
                Proxy
              </th>
              {!compact ? (
                <>
                  <th className={tableStyles.num} title="Mean generic-naming normalized (higher = less generic)">
                    GNR↑
                  </th>
                  <th className={tableStyles.num}>Goto</th>
                  <th className={tableStyles.num}>Nest</th>
                  <th className={tableStyles.num}>Temp/LOC</th>
                  <th className={tableStyles.num}>Flag/LOC</th>
                </>
              ) : (
                <>
                  <th className={tableStyles.num}>Goto</th>
                  <th className={tableStyles.num}>Nest</th>
                </>
              )}
            </tr>
          </thead>
          <tbody>
            {stats.map((row) => {
              const color = DECOMPILER_COLORS[row.decompiler] ?? "#94a3b8";
              return (
                <tr
                  key={row.decompiler}
                  className={
                    row.decompiler === "fission" ? tableStyles.fissionRow : undefined
                  }
                >
                  <td>
                    <span
                      className={tableStyles.dot}
                      style={{ background: color }}
                    />
                    {row.decompiler}
                  </td>
                  <td className={tableStyles.num}>{row.rows || "—"}</td>
                  <td className={tableStyles.num}>
                    {meanFmt(row.meanSourceSimilarity)}
                  </td>
                  <td className={tableStyles.num}>
                    {meanFmt(row.meanAstSimilarity)}
                  </td>
                  <td className={tableStyles.num}>
                    {meanFmt(row.meanReadabilityProxy)}
                  </td>
                  {!compact ? (
                    <>
                      <td className={tableStyles.num}>
                        {meanFmt(row.meanGnrNormalized)}
                      </td>
                      <td className={tableStyles.num}>
                        {meanFmt(row.meanGotoCount, 2)}
                      </td>
                      <td className={tableStyles.num}>
                        {meanFmt(row.meanNestingDepth, 2)}
                      </td>
                      <td className={tableStyles.num}>
                        {meanFmt(row.meanTempLocRatio)}
                      </td>
                      <td className={tableStyles.num}>
                        {meanFmt(row.meanFlagSoupPerLoc)}
                      </td>
                    </>
                  ) : (
                    <>
                      <td className={tableStyles.num}>
                        {meanFmt(row.meanGotoCount, 2)}
                      </td>
                      <td className={tableStyles.num}>
                        {meanFmt(row.meanNestingDepth, 2)}
                      </td>
                    </>
                  )}
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>

      {compact ? (
        <p className={styles.sectionLead} style={{ marginTop: "0.75rem" }}>
          Full proxy families (GNR, temps, flag soup) and bare-compile pivots:{" "}
          <Link href="/quality">Quality EXT →</Link>
        </p>
      ) : null}
    </div>
  );
}
