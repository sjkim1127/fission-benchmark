"use client";

import type { Validity, RunMeta } from "@/lib/schemas";
import styles from "./ValidityBanner.module.css";

interface Props {
  validity?: Validity;
  run?: RunMeta;
}

export function ValidityBanner({ validity, run }: Props) {
  if (!validity) {
    return (
      <div className={`${styles.banner} ${styles.legacy}`}>
        <span className={styles.icon}>⚠️</span>
        <div>
          <div className={styles.title}>LEGACY / UNVERIFIED</div>
          <div className={styles.sub}>Provenance incomplete — predates the envelope format.</div>
        </div>
      </div>
    );
  }

  const fissionPct = validity.fission_coverage != null
    ? `${(validity.fission_coverage * 100).toFixed(1)}%`
    : "—";
  const backendPct = validity.backend_coverage != null
    ? `${(validity.backend_coverage * 100).toFixed(1)}%`
    : "—";

  const covLine = `Fission ${validity.fission_clean ?? "?"}/${validity.fission_attempted ?? "?"} (${fissionPct}), all-backend ${validity.backend_clean ?? "?"}/${validity.backend_attempted ?? "?"} (${backendPct})`;

  if (!validity.valid) {
    return (
      <div className={`${styles.banner} ${styles.invalid}`}>
        <span className={styles.icon}>⛔</span>
        <div>
          <div className={styles.title}>INVALID MEASUREMENT</div>
          <div className={styles.sub}>{covLine}</div>
          {validity.reasons && validity.reasons.length > 0 && (
            <ul className={styles.reasons}>
              {validity.reasons.map((r) => <li key={r}>{r}</li>)}
            </ul>
          )}
        </div>
      </div>
    );
  }

  if (!validity.publishable) {
    const publishReasons = validity.publish_reasons ?? [];
    return (
      <div className={`${styles.banner} ${styles.smoke}`}>
        <span className={styles.icon}>✅</span>
        <div>
          <div className={styles.title}>VALID SMOKE MEASUREMENT</div>
          <div className={styles.sub}>{covLine}</div>
          {publishReasons.length > 0 && (
            <div className={styles.sub}>⚪ Not publishable — {publishReasons.join(", ")}</div>
          )}
        </div>
      </div>
    );
  }

  return (
    <div className={`${styles.banner} ${styles.valid}`}>
      <span className={styles.icon}>✅</span>
      <div>
        <div className={styles.title}>VALID RUN</div>
        <div className={styles.sub}>{covLine}</div>
        {run?.finished_at && (
          <div className={styles.sub}>Measured {new Date(run.finished_at).toLocaleString("en-US", { timeZone: "UTC", timeZoneName: "short" })}</div>
        )}
      </div>
    </div>
  );
}
