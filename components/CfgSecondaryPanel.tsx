"use client";

import styles from "./SummaryTable.module.css";

interface Props {
  status: string;
  byDecompiler: Record<
    string,
    { match?: number; mismatch?: number; match_rate?: number | null; total?: number }
  >;
}

/** Optional secondary: CFG parity (not correctness). */
export function CfgSecondaryPanel({ status, byDecompiler }: Props) {
  if (status !== "present" || Object.keys(byDecompiler).length === 0) {
    return (
      <p className={styles.hint}>
        CFG match secondary is <strong>absent</strong> for this artifact. Run{" "}
        <code>benchmark/cfg_parity</code> / <code>runner/run_parity.py</code> and
        re-render the envelope to attach match rates.
      </p>
    );
  }

  return (
    <div className={styles.wrap}>
      <p className={styles.hint}>
        Secondary — basic-block/edge parity vs reference. Does not affect
        semantic ranking.
      </p>
      <table className={styles.table}>
        <thead>
          <tr>
            <th>Decompiler</th>
            <th className={styles.num}>Match</th>
            <th className={styles.num}>Mismatch</th>
            <th className={styles.num}>Match rate</th>
          </tr>
        </thead>
        <tbody>
          {Object.entries(byDecompiler).map(([name, s]) => (
            <tr key={name}>
              <td>
                <strong>{name}</strong>
              </td>
              <td className={styles.num}>{s.match ?? 0}</td>
              <td className={styles.num}>{s.mismatch ?? 0}</td>
              <td className={styles.num}>
                {s.match_rate == null ? "—" : `${(s.match_rate * 100).toFixed(1)}%`}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
