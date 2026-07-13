import type { ParityTelemetry } from "@/lib/parity";
import { pct } from "@/lib/benchmark";
import dash from "@/app/dashboard.module.css";

/** Highlight p-code / CFG / function-discovery dual metrics from telemetry. */
export function DualMetricsTiles({
  telemetry,
}: {
  telemetry: ParityTelemetry | null;
}) {
  if (!telemetry?.stages) {
    return (
      <p style={{ color: "var(--text-dim)", fontSize: "0.85rem" }}>
        No parity telemetry loaded. Run{" "}
        <code>python -m runner.run_parity</code> then{" "}
        <code>python -m benchmark.telemetry.aggregate</code>.
      </p>
    );
  }

  const pcode =
    telemetry.publishable?.pcode_dual ||
    telemetry.stages.pcode_parity?.dual ||
    null;
  const cfg = telemetry.stages.cfg_parity?.dual || null;
  const fd = telemetry.stages.function_discovery?.dual || null;
  const asm = telemetry.stages.assembly_parity;
  const pcodeStage = telemetry.stages.pcode_parity;
  const cfgStage = telemetry.stages.cfg_parity;
  const fdStage = telemetry.stages.function_discovery;

  const tiles: {
    label: string;
    value: string;
    sub: string;
    tone?: "good" | "warn" | "fission" | "ghidra";
  }[] = [
    {
      label: "Assembly match",
      value: pct(asm?.match_rate),
      sub: asm
        ? `${asm.match}/${asm.match + asm.mismatch} comparable · coverage ${pct(asm.usable_coverage)}`
        : "absent",
      tone: "fission",
    },
    {
      label: "P-code opcode seq",
      value: pct(pcode?.opcode_sequence_match_rate ?? null),
      sub: "Dual · sequence agreement (not full IR eq)",
      tone: "good",
    },
    {
      label: "P-code loose full",
      value: pct(pcode?.loose_full_match_rate ?? null),
      sub: "Stub space-selector abstracted",
    },
    {
      label: "P-code strict full",
      value: pct(pcode?.strict_full_match_rate ?? pcodeStage?.match_rate),
      sub: pcodeStage
        ? `Primary status match ${pct(pcodeStage.match_rate)}`
        : "Primary status",
      tone: "warn",
    },
    {
      label: "CFG block starts",
      value: pct(cfg?.mean_block_start_jaccard ?? null),
      sub: cfgStage
        ? `Set match ${pct(cfgStage.match_rate)} · edge jaccard ${pct(cfg?.mean_edge_pair_jaccard ?? null)}`
        : "jaccard dual",
      tone: "ghidra",
    },
    {
      label: "Function discovery",
      value: pct(fd?.mean_presence_recall ?? null),
      sub: fdStage
        ? `Set match ${pct(fdStage.match_rate)} · manifest ${pct(fd?.mean_manifest_recall ?? null)}`
        : "presence recall vs Ghidra inventory",
    },
  ];

  return (
    <div className={dash.tileGrid}>
      {tiles.map((t) => (
        <div
          key={t.label}
          className={`${dash.tile} ${
            t.tone === "good"
              ? dash.tileGood
              : t.tone === "warn"
                ? dash.tileWarn
                : t.tone === "fission"
                  ? dash.tileFission
                  : t.tone === "ghidra"
                    ? dash.tileGhidra
                    : ""
          }`}
        >
          <div className={dash.tileLabel}>{t.label}</div>
          <div className={dash.tileValue}>{t.value}</div>
          <div className={dash.tileSub}>{t.sub}</div>
        </div>
      ))}
    </div>
  );
}
