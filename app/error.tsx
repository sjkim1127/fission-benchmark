"use client";

import Link from "next/link";
import styles from "./dashboard.module.css";

export default function ErrorState() {
  return (
    <div className={styles.page}>
      <main className={styles.main}>
        <div className={styles.frame}>
          <div className={styles.frameTitle}>
            No publishable multi-decomp result available
          </div>
          <p className={styles.frameBody}>
            The multi-decompiler page requires an official publishable envelope.
            Layered Fission↔Ghidra parity may still load from telemetry alone.
          </p>
          <p className={styles.sectionLead} style={{ marginTop: "1rem" }}>
            <Link href="/fission-vs-ghidra">Open Fission ↔ Ghidra parity →</Link>
          </p>
        </div>
      </main>
    </div>
  );
}
