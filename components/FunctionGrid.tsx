"use client";

import { useState, useMemo } from "react";
import type { Row } from "@/lib/schemas";
import styles from "./FunctionGrid.module.css";

interface Props {
  functionNames: string[];
  rows: Row[];
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

function StatusIcon({ row }: { row: Row }) {
  if (row.error) return <span className={styles.statusError} title={row.error}>✗</span>;
  if ((row.semantic_score ?? 0) >= 1.0) return <span className={styles.statusPass}>✓</span>;
  return <span className={styles.statusPartial}>◐</span>;
}

interface ModalProps {
  fnName: string;
  rows: Row[];
  onClose: () => void;
}

function CodeModal({ fnName, rows, onClose }: ModalProps) {
  const [selectedDec, setSelectedDec] = useState(rows[0]?.decompiler ?? "");
  const [selectedVariant, setSelectedVariant] = useState(rows[0]?.compiler_variant ?? "");

  const decompilers = [...new Set(rows.map((r) => r.decompiler))];
  const variants = [...new Set(rows.filter((r) => r.decompiler === selectedDec).map((r) => r.compiler_variant ?? ""))];
  const activeRow = rows.find((r) => r.decompiler === selectedDec && (r.compiler_variant ?? "") === selectedVariant);
  const color = DECOMPILER_COLORS[selectedDec] ?? "#94a3b8";

  return (
    <div className={styles.modalOverlay} onClick={onClose}>
      <div className={styles.modal} onClick={(e) => e.stopPropagation()}>
        <div className={styles.modalHeader}>
          <div className={styles.modalTitle}>
            <code>{fnName}</code>
          </div>
          <button className={styles.modalClose} onClick={onClose}>✕</button>
        </div>

        <div className={styles.modalTabs}>
          {decompilers.map((d) => (
            <button
              key={d}
              className={`${styles.tab} ${d === selectedDec ? styles.tabActive : ""}`}
              style={d === selectedDec ? { borderColor: DECOMPILER_COLORS[d] ?? "#94a3b8", color: DECOMPILER_COLORS[d] ?? "#94a3b8" } : {}}
              onClick={() => {
                setSelectedDec(d);
                const firstVariant = rows.find((r) => r.decompiler === d)?.compiler_variant ?? "";
                setSelectedVariant(firstVariant);
              }}
            >
              {d}
            </button>
          ))}
        </div>

        {variants.length > 1 && (
          <div className={styles.variantRow}>
            {variants.map((v) => (
              <button
                key={v}
                className={`${styles.variantBtn} ${v === selectedVariant ? styles.variantActive : ""}`}
                onClick={() => setSelectedVariant(v)}
              >
                {v || "(default)"}
              </button>
            ))}
          </div>
        )}

        {activeRow && (
          <div className={styles.modalBody}>
            <div className={styles.modalMeta}>
              <span style={{ color }}>●</span>
              <span>Correctness: <strong>{((activeRow.correctness_score ?? 0)).toFixed(3)}</strong></span>
              <span>Similarity: <strong>{activeRow.source_similarity.toFixed(3)}</strong></span>
              <span>Semantic: <strong>{activeRow.semantic_score == null ? '—' : (activeRow.semantic_score >= 1.0 ? '✓ pass' : activeRow.semantic_score.toFixed(2))}</strong></span>
              <span>{activeRow.time_ms}ms</span>
            </div>

            {activeRow.error ? (
              <div className={styles.errorBox}>{activeRow.error}</div>
            ) : (
              <pre className={styles.codeBlock}>
                <code>{activeRow.decompiled_code ?? "(no code)"}</code>
              </pre>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

function FunctionCard({ fnName, rows, onClick }: { fnName: string; rows: Row[]; onClick: () => void }) {
  const decompilers = [...new Set(rows.map((r) => r.decompiler))];
  const fissionRow = rows.find((r) => r.decompiler === "fission" && !r.error);
  const fissionScore = fissionRow ? (fissionRow.correctness_score ?? 0) : null;
  const allFail = rows.every((r) => !!r.error);
  const universallyLow = !allFail && rows.filter((r) => !r.error).every((r) => (r.correctness_score ?? 0) < 0.3);

  return (
    <button className={styles.card} onClick={onClick}>
      <div className={styles.cardHeader}>
        <code className={styles.fnName}>{fnName}</code>
        {universallyLow && <span className={styles.badge} title="Universally low — all decompilers struggle">⚪ hard</span>}
      </div>

      <div className={styles.cardScores}>
        {decompilers.map((d) => {
          const r = rows.find((row) => row.decompiler === d);
          const score = r?.correctness_score ?? 0;
          const color = DECOMPILER_COLORS[d] ?? "#94a3b8";
          return (
            <div key={d} className={styles.scoreItem}>
              <span className={styles.scoreDec} style={{ color }}>{d[0].toUpperCase()}</span>
              {r ? <StatusIcon row={r} /> : <span className={styles.statusMissing}>–</span>}
              <span className={styles.scoreVal}>{r?.error ? "err" : (r?.correctness_score ?? 0).toFixed(2)}</span>
            </div>
          );
        })}
      </div>

      {fissionScore !== null && (
        <div className={styles.cardBar}>
          <div
            className={styles.cardBarFill}
            style={{ width: `${Math.min(fissionScore * 100, 100)}%` }}
          />
        </div>
      )}
    </button>
  );
}

export function FunctionGrid({ functionNames, rows }: Props) {
  const [search, setSearch] = useState("");
  const [filter, setFilter] = useState<"all" | "pass" | "fail" | "gap">("all");
  const [modalFn, setModalFn] = useState<string | null>(null);

  const rowsByFn = useMemo(() => {
    const m = new Map<string, Row[]>();
    for (const r of rows) {
      if (!m.has(r.function_name)) m.set(r.function_name, []);
      m.get(r.function_name)!.push(r);
    }
    return m;
  }, [rows]);

  const filtered = useMemo(() => {
    return functionNames.filter((fn) => {
      if (!fn.toLowerCase().includes(search.toLowerCase())) return false;
      const fnRows = rowsByFn.get(fn) ?? [];
      const fissionRow = fnRows.find((r) => r.decompiler === "fission");
      if (filter === "pass" && (!fissionRow || fissionRow.error || (fissionRow.semantic_score ?? 0) < 1.0)) return false;
      if (filter === "fail" && (!fissionRow || (!fissionRow.error && (fissionRow.semantic_score ?? 0) >= 1.0))) return false;
      if (filter === "gap") {
        const fissionLow = !fissionRow || fissionRow.error || (fissionRow.correctness_score ?? 0) < 0.3;
        const othersOk = fnRows.filter((r) => r.decompiler !== "fission" && !r.error).some((r) => (r.correctness_score ?? 0) >= 0.3);
        if (!fissionLow || !othersOk) return false;
      }
      return true;
    });
  }, [functionNames, rowsByFn, search, filter]);

  const modalRows = modalFn ? (rowsByFn.get(modalFn) ?? []) : [];

  return (
    <div>
      <div className={styles.toolbar}>
        <input
          className={styles.search}
          type="search"
          placeholder="Search functions…"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
        <div className={styles.filters}>
          {(["all", "pass", "fail", "gap"] as const).map((f) => (
            <button
              key={f}
              className={`${styles.filterBtn} ${filter === f ? styles.filterActive : ""}`}
              onClick={() => setFilter(f)}
            >
              {f === "all" ? `All (${functionNames.length})` : f === "pass" ? "✓ Pass" : f === "fail" ? "✗ Fail" : "⚠ Gap"}
            </button>
          ))}
        </div>
        <span className={styles.count}>{filtered.length} functions</span>
      </div>

      <div className={styles.grid}>
        {filtered.map((fn) => (
          <FunctionCard
            key={fn}
            fnName={fn}
            rows={rowsByFn.get(fn) ?? []}
            onClick={() => setModalFn(fn)}
          />
        ))}
        {filtered.length === 0 && (
          <div className={styles.empty}>No functions match your filter.</div>
        )}
      </div>

      {modalFn && (
        <CodeModal fnName={modalFn} rows={modalRows} onClose={() => setModalFn(null)} />
      )}
    </div>
  );
}
