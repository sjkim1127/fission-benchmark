import type { ReleaseComparison, MetricDelta, FunctionMovement } from "@/lib/history";
import { pct } from "@/lib/benchmark";
import styles from "./ReleaseComparisonPanel.module.css";

interface Props {
  comparison: ReleaseComparison;
}

function DeltaBadge({ value, digits = 1 }: { value: number | null; digits?: number }) {
  if (value === null || Number.isNaN(value)) {
    return <span className={styles.deltaFlat}>—</span>;
  }
  if (Math.abs(value) < 0.0005) {
    return <span className={styles.deltaFlat}>±0.0%</span>;
  }
  const up = value > 0;
  const pctValue = `${up ? "+" : ""}${(value * 100).toFixed(digits)}%`;
  return (
    <span className={up ? styles.deltaUp : styles.deltaDown}>
      {up ? "▲" : "▼"} {pctValue}
    </span>
  );
}

function IntDeltaBadge({ value }: { value: number | null }) {
  if (value === null || value === 0) return <span className={styles.deltaFlat}>±0</span>;
  const up = value > 0;
  return (
    <span className={up ? styles.deltaUp : styles.deltaDown}>
      {up ? "▲" : "▼"} {up ? "+" : ""}
      {value}
    </span>
  );
}

function DeltaRow({ delta }: { delta: MetricDelta }) {
  const isFission = delta.decompiler === "fission";
  return (
    <tr className={isFission ? styles.fissionRow : undefined}>
      <td>
        <code>{delta.decompiler}</code>
        {isFission && <span className={styles.youAreHere}>this project</span>}
      </td>
      <td className={styles.num}>{pct(delta.previousMeanSemantic)}</td>
      <td className={styles.num}>{pct(delta.currentMeanSemantic)}</td>
      <td className={styles.num}>
        <DeltaBadge value={delta.meanSemanticDelta} />
      </td>
      <td className={styles.num}>{delta.previousPerfectRows}</td>
      <td className={styles.num}>{delta.currentPerfectRows}</td>
      <td className={styles.num}>
        <IntDeltaBadge value={delta.perfectRowsDelta} />
      </td>
      <td className={styles.num}>{delta.rowsCompared}</td>
    </tr>
  );
}

function MovementList({
  title,
  items,
  tone,
}: {
  title: string;
  items: FunctionMovement[];
  tone: "good" | "bad";
}) {
  if (items.length === 0) {
    return (
      <div className={styles.movementEmpty}>
        {tone === "good" ? "No newly-passing functions this release." : "No regressions found. ✅"}
      </div>
    );
  }
  const shown = items.slice(0, 15);
  const remaining = items.length - shown.length;
  return (
    <div>
      <div className={tone === "good" ? styles.movementTitleGood : styles.movementTitleBad}>
        {title} ({items.length})
      </div>
      <ul className={styles.movementList}>
        {shown.map((m) => (
          <li key={`${m.functionName}-${m.compilerVariant}`}>
            <code>{m.functionName}</code>{" "}
            <span className={styles.variant}>{m.compilerVariant}</span>
          </li>
        ))}
      </ul>
      {remaining > 0 && <div className={styles.movementMore}>+{remaining} more</div>}
    </div>
  );
}

export function ReleaseComparisonPanel({ comparison }: Props) {
  const fission = comparison.deltas.find((d) => d.decompiler === "fission");
  const others = comparison.deltas.filter((d) => d.decompiler !== "fission");

  return (
    <div className={styles.wrap}>
      <div className={styles.header}>
        <div className={styles.headerTitle}>
          What changed: <code>{comparison.previousVersion}</code> →{" "}
          <code>{comparison.currentVersion}</code>
        </div>
        <p className={styles.headerLead}>
          Same corpus subset, same oracle, two Fission releases — every number
          below is computed only over the (function, compiler variant) pairs
          measured in <em>both</em> runs, so a bigger or smaller corpus in
          either release can&apos;t skew the comparison. Fission&apos;s own
          numbers are what matter here — other tools are shown as a stability
          reference, not a re-ranking.
        </p>
      </div>

      {fission && (
        <div className={styles.headline}>
          <div className={styles.headlineStat}>
            <div className={styles.headlineLabel}>Semantic pass rate</div>
            <div className={styles.headlineValue}>
              {pct(fission.previousMeanSemantic)} → {pct(fission.currentMeanSemantic)}
            </div>
            <DeltaBadge value={fission.meanSemanticDelta} digits={1} />
          </div>
          <div className={styles.headlineStat}>
            <div className={styles.headlineLabel}>Perfect rows</div>
            <div className={styles.headlineValue}>
              {fission.previousPerfectRows} → {fission.currentPerfectRows}
            </div>
            <IntDeltaBadge value={fission.perfectRowsDelta} />
          </div>
          <div className={styles.headlineStat}>
            <div className={styles.headlineLabel}>Functions compared</div>
            <div className={styles.headlineValue}>{fission.rowsCompared}</div>
            <span className={styles.deltaFlat}>same (function, variant) pairs</span>
          </div>
        </div>
      )}

      {fission && fission.rowsCompared < 30 && (
        <p className={styles.smallSampleNote}>
          ⚠️ Only {fission.rowsCompared} functions overlap between these two
          releases&apos; measured corpora — one flipped result can move the
          percentage a lot. Treat this delta as a signal to look at the
          function list below, not a precise measurement.
        </p>
      )}

      <div className={styles.wrapTable}>
        <table className={styles.table}>
          <thead>
            <tr>
              <th>Decompiler</th>
              <th className={styles.num}>{comparison.previousVersion} semantic</th>
              <th className={styles.num}>{comparison.currentVersion} semantic</th>
              <th className={styles.num}>Δ</th>
              <th className={styles.num}>{comparison.previousVersion} perfect</th>
              <th className={styles.num}>{comparison.currentVersion} perfect</th>
              <th className={styles.num}>Δ</th>
              <th className={styles.num}>Rows compared</th>
            </tr>
          </thead>
          <tbody>
            {fission && <DeltaRow delta={fission} />}
            {others.map((d) => (
              <DeltaRow key={d.decompiler} delta={d} />
            ))}
          </tbody>
        </table>
      </div>

      <div className={styles.movementGrid}>
        <MovementList
          title="Newly passing"
          items={comparison.fissionNewlyPassing}
          tone="good"
        />
        <MovementList
          title="Newly failing"
          items={comparison.fissionNewlyFailing}
          tone="bad"
        />
      </div>
    </div>
  );
}
