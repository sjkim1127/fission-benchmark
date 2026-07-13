import Link from "next/link";
import styles from "@/app/dashboard.module.css";

/** Shown when results/latest.json is missing or not publishable (common at build). */
export function UnavailableData({
  title = "No publishable benchmark result",
  detail = "Could not load a multi-decompiler envelope. Sources tried: public/benchmark-latest.json, results/latest.json, results/dev_latest.json on main.",
}: {
  title?: string;
  detail?: string;
}) {
  return (
    <div className={styles.frame}>
      <div className={styles.frameTitle}>{title}</div>
      <p className={styles.frameBody}>{detail}</p>
      <p className={styles.sectionLead} style={{ marginTop: "0.75rem" }}>
        <Link href="/fission-vs-ghidra">Fission ↔ Ghidra parity</Link>
        {" may still load from telemetry alone. Smoke/valid runs show with a "}
        <strong>VALID SMOKE</strong>
        {" banner until a full publication gate produces publishable=true."}
      </p>
    </div>
  );
}
