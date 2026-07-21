import type { VersionTrendPoint } from "@/lib/history";
import { pct } from "@/lib/benchmark";
import styles from "./VersionTrendChart.module.css";

interface Props {
  points: VersionTrendPoint[];
}

const WIDTH = 720;
const HEIGHT = 240;
const PAD_LEFT = 44;
const PAD_RIGHT = 20;
const PAD_TOP = 20;
const PAD_BOTTOM = 36;

function xFor(index: number, count: number): number {
  if (count <= 1) return PAD_LEFT + (WIDTH - PAD_LEFT - PAD_RIGHT) / 2;
  const span = WIDTH - PAD_LEFT - PAD_RIGHT;
  return PAD_LEFT + (span * index) / (count - 1);
}

function yFor(rate: number): number {
  const span = HEIGHT - PAD_TOP - PAD_BOTTOM;
  return PAD_TOP + span * (1 - Math.max(0, Math.min(1, rate)));
}

function dotRadius(rows: number, maxRows: number): number {
  if (maxRows <= 0) return 4;
  const scale = Math.sqrt(Math.max(rows, 1) / maxRows);
  return 3 + scale * 7;
}

export function VersionTrendChart({ points }: Props) {
  if (points.length === 0) {
    return (
      <p className={styles.empty}>
        No archived releases with multi-decomp data yet.
      </p>
    );
  }

  const scored = points.filter((p) => p.meanSemantic !== null);
  const maxRows = Math.max(1, ...points.map((p) => p.totalRows));
  const gridLines = [0, 0.25, 0.5, 0.75, 1];

  const linePath = scored
    .map((p, i) => {
      const idx = points.indexOf(p);
      const x = xFor(idx, points.length);
      const y = yFor(p.meanSemantic ?? 0);
      return `${i === 0 ? "M" : "L"}${x.toFixed(1)},${y.toFixed(1)}`;
    })
    .join(" ");

  return (
    <div className={styles.wrap}>
      <svg
        viewBox={`0 0 ${WIDTH} ${HEIGHT}`}
        className={styles.svg}
        role="img"
        aria-label="Fission semantic pass rate by release"
      >
        {gridLines.map((g) => (
          <g key={g}>
            <line
              x1={PAD_LEFT}
              x2={WIDTH - PAD_RIGHT}
              y1={yFor(g)}
              y2={yFor(g)}
              className={styles.gridLine}
            />
            <text x={PAD_LEFT - 8} y={yFor(g) + 4} className={styles.axisLabel} textAnchor="end">
              {Math.round(g * 100)}%
            </text>
          </g>
        ))}

        {linePath && <path d={linePath} className={styles.line} fill="none" />}

        {points.map((p, idx) => {
          const x = xFor(idx, points.length);
          const prev = idx > 0 ? points[idx - 1] : null;
          const corpusChanged = prev !== null && prev.totalRows !== p.totalRows;
          return (
            <g key={p.version}>
              <text
                x={x}
                y={HEIGHT - PAD_BOTTOM + 18}
                className={styles.axisLabel}
                textAnchor="middle"
              >
                {p.version}
              </text>
              {corpusChanged && (
                <text
                  x={x}
                  y={HEIGHT - PAD_BOTTOM + 30}
                  className={styles.corpusChangedLabel}
                  textAnchor="middle"
                >
                  corpus {prev!.totalRows}→{p.totalRows}
                </text>
              )}
              {p.meanSemantic !== null ? (
                <circle
                  cx={x}
                  cy={yFor(p.meanSemantic)}
                  r={dotRadius(p.totalRows, maxRows)}
                  className={p.official ? styles.dotOfficial : styles.dot}
                >
                  <title>
                    {p.version}: {pct(p.meanSemantic)} semantic pass rate,{" "}
                    {p.perfectRows}/{p.totalRows} perfect rows
                    {p.official ? " (official run)" : " (smoke run)"}
                  </title>
                </circle>
              ) : (
                <text x={x} y={HEIGHT / 2} className={styles.noData} textAnchor="middle">
                  no data
                </text>
              )}
            </g>
          );
        })}
      </svg>
      <p className={styles.hint}>
        Dot size ∝ corpus size measured at that release (
        {Math.min(...points.map((p) => p.totalRows))}–{maxRows} Fission rows). Hollow dots are
        smoke-profile runs; filled dots are official publications.
      </p>
    </div>
  );
}
