import styles from "./SummaryTable.module.css";
import type {
  DecompilerSpeedRow,
  FunctionSpeedRow,
  PairedSpeedRow,
  PivotSpeedRow,
} from "@/lib/speed";

const COLORS: Record<string, string> = {
  fission: "#6366f1",
  ghidra: "#10b981",
  angr: "#f59e0b",
  radare2: "#ec4899",
  boomerang: "#14b8a6",
  snowman: "#8b5cf6",
  revng: "#f97316",
  reko: "#06b6d4",
  retdec: "#a78bfa",
};

function fmtMs(v: number | null | undefined): string {
  if (v == null || Number.isNaN(v)) return "—";
  if (v >= 1000) return `${(v / 1000).toFixed(2)}s`;
  return `${Math.round(v)}ms`;
}

function fmtX(v: number | null | undefined): string {
  if (v == null || Number.isNaN(v)) return "—";
  return `${v.toFixed(2)}×`;
}

export function DecompilerSpeedTable({ rows }: { rows: DecompilerSpeedRow[] }) {
  return (
    <div className={styles.wrap}>
      <p className={styles.hint}>
        Adapter <strong>decompile</strong> wall time per row (<code>time_ms</code>
        ). Excludes semantic/oracle. Not a ranking axis.
      </p>
      <table className={styles.table}>
        <thead>
          <tr>
            <th>Decompiler</th>
            <th className={styles.num}>Timed</th>
            <th className={styles.num}>Missing</th>
            <th className={styles.num}>Mean</th>
            <th className={styles.num}>p50</th>
            <th className={styles.num}>p95</th>
            <th className={styles.num}>Min</th>
            <th className={styles.num}>Max</th>
            <th className={styles.num}>Sum</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((r) => {
            const color = COLORS[r.decompiler] ?? "#94a3b8";
            const isFission = r.decompiler === "fission";
            return (
              <tr
                key={r.decompiler}
                className={isFission ? styles.fissionRow : undefined}
              >
                <td>
                  <span className={styles.dot} style={{ background: color }} />
                  <strong style={{ color: isFission ? color : "inherit" }}>
                    {r.decompiler}
                  </strong>
                </td>
                <td className={styles.num}>{r.timedRows}</td>
                <td className={styles.num}>{r.zeroOrMissing}</td>
                <td className={styles.num}>{fmtMs(r.mean)}</td>
                <td className={styles.num}>{fmtMs(r.p50)}</td>
                <td className={styles.num}>{fmtMs(r.p95)}</td>
                <td className={styles.num}>{fmtMs(r.min)}</td>
                <td className={styles.num}>{fmtMs(r.max)}</td>
                <td className={styles.num}>{fmtMs(r.sum)}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}

export function PairedSpeedTable({
  pairs,
  limit = 40,
}: {
  pairs: PairedSpeedRow[];
  limit?: number;
}) {
  const slice = pairs.slice(0, limit);
  if (slice.length === 0) {
    return (
      <p className={styles.hint}>
        No paired fission+ghidra cells with both <code>time_ms</code> &gt; 0.
      </p>
    );
  }
  return (
    <div className={styles.wrap}>
      <p className={styles.hint}>
        Same function × variant. <strong>Speedup</strong> = ghidra_ms /
        fission_ms (&gt;1 ⇒ Fission faster). Sorted by slowest Fission first.
        Showing top {slice.length} of {pairs.length}.
      </p>
      <table className={styles.table}>
        <thead>
          <tr>
            <th>Function</th>
            <th>Variant</th>
            <th className={styles.num}>Fission</th>
            <th className={styles.num}>Ghidra</th>
            <th className={styles.num}>Speedup</th>
          </tr>
        </thead>
        <tbody>
          {slice.map((p) => (
            <tr key={`${p.function_name}|${p.compiler_variant}`}>
              <td>
                <code>{p.function_name}</code>
              </td>
              <td>{p.compiler_variant}</td>
              <td className={styles.num}>{fmtMs(p.fission_ms)}</td>
              <td className={styles.num}>{fmtMs(p.ghidra_ms)}</td>
              <td className={styles.num}>{fmtX(p.speedup)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export function SlowestFunctionsTable({ rows }: { rows: FunctionSpeedRow[] }) {
  if (rows.length === 0) {
    return <p className={styles.hint}>No timed Fission rows.</p>;
  }
  return (
    <div className={styles.wrap}>
      <p className={styles.hint}>
        Fission-only, aggregated across variants (mean / p95 / max).
      </p>
      <table className={styles.table}>
        <thead>
          <tr>
            <th>Function</th>
            <th className={styles.num}>n</th>
            <th className={styles.num}>Mean</th>
            <th className={styles.num}>p95</th>
            <th className={styles.num}>Max</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((r) => (
            <tr key={r.function_name}>
              <td>
                <code>{r.function_name}</code>
              </td>
              <td className={styles.num}>{r.n}</td>
              <td className={styles.num}>{fmtMs(r.mean_ms)}</td>
              <td className={styles.num}>{fmtMs(r.p95_ms)}</td>
              <td className={styles.num}>{fmtMs(r.max_ms)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export function VariantSpeedTable({ rows }: { rows: PivotSpeedRow[] }) {
  if (rows.length === 0) {
    return <p className={styles.hint}>No Fission variant timing.</p>;
  }
  return (
    <div className={styles.wrap}>
      <p className={styles.hint}>Fission mean / p50 by compiler_variant.</p>
      <table className={styles.table}>
        <thead>
          <tr>
            <th>Variant</th>
            <th className={styles.num}>n</th>
            <th className={styles.num}>Mean</th>
            <th className={styles.num}>p50</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((r) => (
            <tr key={r.key}>
              <td>{r.key}</td>
              <td className={styles.num}>{r.n}</td>
              <td className={styles.num}>{fmtMs(r.mean_ms)}</td>
              <td className={styles.num}>{fmtMs(r.p50_ms)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
