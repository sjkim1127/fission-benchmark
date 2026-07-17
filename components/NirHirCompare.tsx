"use client";

import { useMemo, useState } from "react";
import type { Row } from "@/lib/schemas";
import type { FunctionSourceEntry } from "@/lib/source";
import styles from "./NirHirCompare.module.css";

type Props = {
  fissionRows: Row[];
  sources: Record<string, FunctionSourceEntry>;
};

function countToken(code: string, token: string): number {
  if (!code) return 0;
  const re = new RegExp(`\\b${token}\\b`, "g");
  return (code.match(re) || []).length;
}

function nestingDepth(code: string): number {
  let depth = 0;
  let max = 0;
  for (const ch of code) {
    if (ch === "{") {
      depth += 1;
      if (depth > max) max = depth;
    } else if (ch === "}") {
      depth = Math.max(0, depth - 1);
    }
  }
  return max;
}

function Panel({
  title,
  subtitle,
  className,
  code,
  stats,
}: {
  title: string;
  subtitle: string;
  className: string;
  code: string;
  stats?: { label: string; value: string }[];
}) {
  return (
    <div className={`${styles.panel} ${className}`}>
      <div className={styles.panelHead}>
        <span className={styles.panelTitle}>{title}</span>
        <span className={styles.panelSub}>{subtitle}</span>
      </div>
      {stats && stats.length > 0 ? (
        <div className={styles.panelStats}>
          {stats.map((s) => (
            <span key={s.label}>
              {s.label}: <strong>{s.value}</strong>
            </span>
          ))}
        </div>
      ) : null}
      <pre className={styles.code}>
        <code className={!code ? styles.empty : undefined}>
          {code || "(no code for this surface)"}
        </code>
      </pre>
    </div>
  );
}

export function NirHirCompare({ fissionRows, sources }: Props) {
  const functionNames = useMemo(() => {
    return [...new Set(fissionRows.map((r) => r.function_name))].sort();
  }, [fissionRows]);

  const [fnName, setFnName] = useState(functionNames[0] ?? "");
  const variants = useMemo(() => {
    return [
      ...new Set(
        fissionRows
          .filter((r) => r.function_name === fnName)
          .map((r) => r.compiler_variant || ""),
      ),
    ].sort();
  }, [fissionRows, fnName]);

  const [variant, setVariant] = useState(variants[0] ?? "");
  // Keep variant valid when function changes.
  const activeVariant = variants.includes(variant)
    ? variant
    : (variants[0] ?? "");

  const row = useMemo(() => {
    return fissionRows.find(
      (r) =>
        r.function_name === fnName &&
        (r.compiler_variant || "") === activeVariant,
    );
  }, [fissionRows, fnName, activeVariant]);

  const sourceEntry = sources[fnName];
  const sourceCode = sourceEntry?.code || "";

  const nir =
    (row?.decompiled_code_nir || "").trim() ||
    (row?.pseudocode_layer === "nir" ? (row?.decompiled_code || "").trim() : "") ||
    "";
  const hir =
    (row?.decompiled_code_hir || "").trim() ||
    "";
  // When HIR missing, show primary if it is not already shown as NIR-only path.
  const hirDisplay =
    hir ||
    (row?.decompiled_code &&
    row.decompiled_code.trim() !== nir
      ? row.decompiled_code.trim()
      : hir);

  const layersDiffer =
    Boolean(nir) && Boolean(hirDisplay) && nir.trim() !== hirDisplay.trim();

  const proxyPrimary =
    row?.readability_proxy_score == null
      ? "—"
      : row.readability_proxy_score.toFixed(3);
  const proxyHir =
    row?.readability_proxy_score_hir == null
      ? "—"
      : Number(row.readability_proxy_score_hir).toFixed(3);

  return (
    <div>
      <div className={styles.fnList}>
        {functionNames.map((name) => (
          <button
            key={name}
            type="button"
            className={`${styles.fnChip} ${
              name === fnName ? styles.fnChipActive : ""
            }`}
            onClick={() => {
              setFnName(name);
            }}
          >
            {name}
          </button>
        ))}
      </div>

      <div className={styles.toolbar}>
        <label>
          <span className={styles.panelSub}>Function</span>{" "}
          <select
            className={styles.select}
            value={fnName}
            onChange={(e) => setFnName(e.target.value)}
          >
            {functionNames.map((name) => (
              <option key={name} value={name}>
                {name}
              </option>
            ))}
          </select>
        </label>
        <label>
          <span className={styles.panelSub}>Variant</span>{" "}
          <select
            className={styles.select}
            value={activeVariant}
            onChange={(e) => setVariant(e.target.value)}
          >
            {variants.map((v) => (
              <option key={v} value={v}>
                {v || "(default)"}
              </option>
            ))}
          </select>
        </label>
        <span
          className={`${styles.diffBadge} ${
            layersDiffer ? styles.diffDifferent : styles.diffSame
          }`}
        >
          {layersDiffer ? "NIR ≠ HIR" : "NIR ≡ HIR (or missing)"}
        </span>
      </div>

      <div className={styles.metaBar}>
        <span>
          Source file:{" "}
          <strong>
            {sourceEntry?.sourcePath || "—"}
            {sourceEntry && !sourceEntry.extracted ? " (whole file)" : ""}
          </strong>
        </span>
        <span>
          Semantic:{" "}
          <strong>
            {row?.semantic_score == null
              ? "—"
              : row.semantic_score >= 1
                ? "✓ pass"
                : row.semantic_score.toFixed(2)}
          </strong>{" "}
          <span className={styles.panelSub}>(always NIR)</span>
        </span>
        <span>
          Taxonomy: <strong>{row?.fail_taxonomy || row?.fail_category || "—"}</strong>
        </span>
        <span>
          Src sim:{" "}
          <strong>
            {typeof row?.source_similarity === "number"
              ? row.source_similarity.toFixed(3)
              : "—"}
          </strong>
        </span>
        <span>
          Proxy (primary): <strong>{proxyPrimary}</strong>
        </span>
        <span>
          Proxy HIR: <strong>{proxyHir}</strong>
        </span>
        <span>
          Layer tag: <strong>{row?.pseudocode_layer || "—"}</strong>
        </span>
      </div>

      <div className={styles.grid}>
        <Panel
          title="Source"
          subtitle="Original C"
          className={styles.panelSource}
          code={sourceCode}
          stats={[
            { label: "LOC", value: String(sourceCode ? sourceCode.split("\n").length : 0) },
            { label: "goto", value: String(countToken(sourceCode, "goto")) },
          ]}
        />
        <Panel
          title="NIR"
          subtitle="Semantic surface"
          className={styles.panelNir}
          code={nir || (row?.error ? `// error: ${row.error}` : "")}
          stats={[
            { label: "LOC", value: String(nir ? nir.split("\n").length : 0) },
            { label: "goto", value: String(countToken(nir, "goto")) },
            { label: "nest", value: String(nestingDepth(nir)) },
            {
              label: "proxy",
              value: proxyPrimary,
            },
          ]}
        />
        <Panel
          title="HIR"
          subtitle="Readability surface"
          className={styles.panelHir}
          code={
            hirDisplay ||
            (nir
              ? "// HIR not provided separately — same as NIR or absent"
              : "")
          }
          stats={[
            {
              label: "LOC",
              value: String(hirDisplay ? hirDisplay.split("\n").length : 0),
            },
            { label: "goto", value: String(countToken(hirDisplay, "goto")) },
            { label: "nest", value: String(nestingDepth(hirDisplay)) },
            { label: "proxy HIR", value: proxyHir },
          ]}
        />
      </div>

      <p className={styles.note}>
        Policy: semantic / recompile / oracle use <strong>NIR</strong> only.
        Readability proxies prefer <strong>HIR</strong> when dual printers
        emit both. This page is diagnostic — it never ranks tools. Source is
        loaded from <code>corpus/&lt;split&gt;/source</code> via manifests.
      </p>
    </div>
  );
}
