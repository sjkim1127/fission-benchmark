import Link from "next/link";
import styles from "@/app/dashboard.module.css";

/** Shown when results/latest.json is missing or not publishable (common at build). */
export function UnavailableData({
  title = "No publishable benchmark result",
  detail = "Official multi-decompiler results are not available yet. After a successful publication gate run, this page will populate from results/latest.json.",
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
        {" may still load from telemetry alone."}
      </p>
    </div>
  );
}
