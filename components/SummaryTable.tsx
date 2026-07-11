"use client";

import styles from "./SummaryTable.module.css";

interface DecompilerStat {
  decompiler: string;
  attempted: number;
  clean: number;
  error: number;
  avgCorrectness: number;
  avgSimilarity: number;
  semanticPassPct: number;
  avgTimeMs: number;
}

interface Props {
  stats: DecompilerStat[];
}

const DECOMPILER_COLORS: Record<string, string> = {
  fission: "#6366f1",
  ghidra: "#10b981",
  angr: "#f59e0b",
  radare2: "#ec4899",
  retdec: "#14b8a6",
  snowman: "#8b5cf6",
  revng: "#f97316",
  reko: "#06b6d4",
};

function ScoreBar({ value, color }: { value: number; color: string }) {
  return (
    <div className={styles.barWrap}>
      <div
        className={styles.bar}
        style={{ width: `${Math.min(value * 100, 100)}%`, background: color }}
      />
      <span className={styles.barLabel}>{value.toFixed(3)}</span>
    </div>
  );
}

export function SummaryTable({ stats }: Props) {
  return (
    <div className={styles.wrap}>
      <table className={styles.table}>
        <thead>
          <tr>
            <th>Decompiler</th>
            <th className={styles.num}>Attempted</th>
            <th className={styles.num}>Clean</th>
            <th className={styles.num}>Error</th>
            <th>Avg Correctness</th>
            <th>Avg Similarity</th>
            <th className={styles.num}>Semantic Pass</th>
            <th className={styles.num}>Avg Time</th>
          </tr>
        </thead>
        <tbody>
          {stats.map((s) => {
            const color = DECOMPILER_COLORS[s.decompiler] ?? "#94a3b8";
            const isFission = s.decompiler === "fission";
            return (
              <tr key={s.decompiler} className={isFission ? styles.fissionRow : undefined}>
                <td>
                  <span className={styles.dot} style={{ background: color }} />
                  <strong style={{ color: isFission ? color : "inherit" }}>
                    {s.decompiler}
                  </strong>
                </td>
                <td className={styles.num}>{s.attempted}</td>
                <td className={styles.num}>{s.clean}</td>
                <td className={`${styles.num} ${s.error > 0 ? styles.errorCell : ""}`}>{s.error || "—"}</td>
                <td><ScoreBar value={s.avgCorrectness} color={color} /></td>
                <td><ScoreBar value={s.avgSimilarity} color={color} /></td>
                <td className={styles.num}>{s.semanticPassPct.toFixed(1)}%</td>
                <td className={styles.num}>{s.avgTimeMs > 0 ? `${Math.round(s.avgTimeMs)}ms` : "—"}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}
