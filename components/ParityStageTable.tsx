"use client";

import styles from "./SummaryTable.module.css";
import type { ParityTelemetry } from "@/lib/parity";

interface Props {
  telemetry: ParityTelemetry | null;
}

const STAGE_LABELS: Record<string, string> = {
  assembly_parity: "Assembly",
  decode_parity: "Decode",
  pcode_parity: "P-code",
  cfg_parity: "CFG",
  function_discovery: "Functions",
  ir_invariants: "IR invariants",
  golden_repros: "Golden repros",
};

/**
 * Non-headline stages: stub, weak structural, or meta canaries.
 * Primary quality = assembly / pcode / cfg / function inventory.
 */
const EXCLUDED_PRIMARY = new Set([
  "decode_parity", // retired stub
  "ir_invariants",
  "golden_repros",
  "abi_parity", // scaffold pending /abi
  "strip_discovery", // scaffold pending realworld strip corpus
]);

function pct(rate: number | null | undefined): string {
  if (rate === null || rate === undefined) return "—";
  return `${(rate * 100).toFixed(1)}%`;
}

export function ParityStageTable({ telemetry }: Props) {
  if (!telemetry || !telemetry.stages || Object.keys(telemetry.stages).length === 0) {
    return (
      <p className={styles.hint}>
        No parity telemetry yet. Run{" "}
        <code>python -m runner.run_parity --corpus dev</code> then{" "}
        <code>python -m benchmark.telemetry.aggregate</code>.
      </p>
    );
  }

  const allStages = Object.entries(telemetry.stages);
  const primary = allStages.filter(([stage]) => !EXCLUDED_PRIMARY.has(stage));
  const excluded = allStages.filter(([stage]) => EXCLUDED_PRIMARY.has(stage));
  const mode = telemetry.canonicalize_mode ?? "loose";
  const pub = telemetry.publishable;
  const critique = telemetry.reliability_critique;
  const pcodeDual =
    pub?.pcode_dual ||
    telemetry.stages?.pcode_parity?.dual ||
    null;

  return (
    <div className={styles.wrap}>
      <p className={styles.hint}>
        Layered parity vs reference (typically <strong>Ghidra</strong>).{" "}
        <strong>Headline quality</strong> = assembly + p-code + CFG + function
        inventory (Ghidra vs candidate).
        Match rate is among comparable rows; coverage shows infra health.
        Mode: <code>{mode}</code>
        {mode === "strict"
          ? " (conservative / no leniency)"
          : " (local triage only — not for CI)"}
        .
      </p>
      {pub && (
        <p className={styles.hint}>
          Headline rollup: match_rate=
          {pct(pub.match_rate_comparable)} · coverage=
          {pct(pub.usable_coverage)} · rows={pub.total_rows}
          {pub.definition ? ` · ${pub.definition}` : ""}
        </p>
      )}
      {pcodeDual && (
        <p className={styles.hint}>
          P-code dual rates (do not read strict 0% alone): opcode=
          {pct(pcodeDual.opcode_sequence_match_rate ?? null)} · loose_full=
          {pct(pcodeDual.loose_full_match_rate ?? null)} · strict_full=
          {pct(pcodeDual.strict_full_match_rate ?? null)}
        </p>
      )}
      {telemetry.stages?.function_discovery?.dual && (
        <p className={styles.hint}>
          Function inventory dual: set match_rate=
          {pct(telemetry.stages.function_discovery.match_rate)} · mean
          presence_recall=
          {pct(
            telemetry.stages.function_discovery.dual.mean_presence_recall ?? null
          )}{" "}
          · mean manifest_recall=
          {pct(
            telemetry.stages.function_discovery.dual.mean_manifest_recall ?? null
          )}{" "}
          (exact set equality is strict; Fission often finds fewer CRT/helpers)
        </p>
      )}
      {critique?.warnings && critique.warnings.length > 0 && (
        <p className={styles.hint}>
          Reliability notes: {critique.warnings.slice(0, 3).join(" · ")}
        </p>
      )}
      <table className={styles.table}>
        <thead>
          <tr>
            <th>Stage</th>
            <th className={styles.num}>Total</th>
            <th className={styles.num}>Match</th>
            <th className={styles.num}>Mismatch</th>
            <th className={styles.num}>Error/other</th>
            <th className={styles.num}>Match rate</th>
            <th className={styles.num}>Coverage</th>
            <th className={styles.num}>Mismatch rate</th>
            <th>Top mismatch kinds</th>
          </tr>
        </thead>
        <tbody>
          {primary.map(([stage, s]) => {
            const kinds = Object.entries(s.by_mismatch_kind || {})
              .sort((a, b) => b[1] - a[1])
              .slice(0, 3)
              .map(([k, n]) => `${k}:${n}`)
              .join(" · ");
            return (
              <tr key={stage}>
                <td>
                  <strong>{STAGE_LABELS[stage] ?? stage}</strong>
                  <div className={styles.tax}>{stage}</div>
                </td>
                <td className={styles.num}>{s.total}</td>
                <td className={styles.num}>{s.match}</td>
                <td className={styles.num}>{s.mismatch}</td>
                <td className={styles.num}>{s.error_or_other}</td>
                <td className={styles.num}>{pct(s.match_rate)}</td>
                <td className={styles.num}>{pct(s.usable_coverage ?? null)}</td>
                <td
                  className={`${styles.num} ${
                    (s.mismatch_rate ?? 0) > 0.5 ? styles.errorCell : ""
                  }`}
                >
                  {pct(s.mismatch_rate)}
                </td>
                <td className={styles.tax}>{kinds || "—"}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
      {excluded.length > 0 && (
        <p className={styles.hint}>
          Excluded from primary (not scored for ranking):{" "}
          {excluded
            .map(([stage, s]) => {
              const skip = s.by_status?.skipped ?? 0;
              return `${STAGE_LABELS[stage] ?? stage} (total=${s.total}, skipped=${skip})`;
            })
            .join("; ")}
          . Implement real modrm/sib/disp/imm before promoting decode.
        </p>
      )}
      <p className={styles.hint}>
        Rows: {telemetry.total_rows}
        {telemetry.by_pair
          ? ` · pairs: ${Object.keys(telemetry.by_pair).join(", ")}`
          : ""}
        {telemetry.reliability
          ? ` · fetch_error_rate=${pct(telemetry.reliability.fetch_error_rate ?? null)}`
          : ""}
      </p>
    </div>
  );
}
