import type { MvpDecompilerStats } from "@/lib/benchmark";
import { pct } from "@/lib/benchmark";
import dash from "@/app/dashboard.module.css";

function pick(
  stats: MvpDecompilerStats[],
  name: string
): MvpDecompilerStats | undefined {
  return stats.find((s) => s.decompiler === name);
}

function Card({
  name,
  s,
  variant,
}: {
  name: string;
  s: MvpDecompilerStats | undefined;
  variant: "fission" | "ghidra";
}) {
  return (
    <div
      className={`${dash.pairCard} ${
        variant === "fission" ? dash.pairCardFission : dash.pairCardGhidra
      }`}
    >
      <div
        className={`${dash.pairName} ${
          variant === "fission" ? dash.pairNameFission : dash.pairNameGhidra
        }`}
      >
        {name}
        {variant === "ghidra" ? " · reference" : " · candidate"}
      </div>
      {!s ? (
        <p className={dash.tileSub}>No rows for this decompiler in the envelope.</p>
      ) : (
        <>
          <div className={dash.pairStat}>
            <span>Semantic mean</span>
            <strong>{pct(s.meanSemantic)}</strong>
          </div>
          <div className={dash.pairStat}>
            <span>Perfect / tested</span>
            <strong>
              {s.perfectRows}/{s.semanticTested}
            </strong>
          </div>
          <div className={dash.pairStat}>
            <span>Adapter clean / attempted</span>
            <strong>
              {s.adapterClean}/{s.attempted}
            </strong>
          </div>
          <div className={dash.pairStat}>
            <span>Boundary invalid</span>
            <strong>{s.invalidBoundary}</strong>
          </div>
          <div className={dash.pairStat}>
            <span>Mean time</span>
            <strong>
              {s.meanTimeMs != null && s.meanTimeMs > 0
                ? `${Math.round(s.meanTimeMs)}ms`
                : "—"}
            </strong>
          </div>
        </>
      )}
    </div>
  );
}

/** Side-by-side semantic/coverage for Fission (candidate) vs Ghidra (reference). */
export function CorePairPanel({ stats }: { stats: MvpDecompilerStats[] }) {
  const fission = pick(stats, "fission");
  const ghidra = pick(stats, "ghidra");
  return (
    <div className={dash.pairRow}>
      <Card name="Fission" s={fission} variant="fission" />
      <div className={dash.pairVs}>VS</div>
      <Card name="Ghidra" s={ghidra} variant="ghidra" />
    </div>
  );
}
