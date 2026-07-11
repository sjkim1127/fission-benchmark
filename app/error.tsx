"use client";

import styles from "./page.module.css";

export default function ErrorState() {
  return (
    <main className={styles.page}>
      <section className={styles.errorState}>
        <h1>No publishable benchmark result is currently available.</h1>
        <p>The validation pipeline is under reconstruction. Unverified results are not displayed.</p>
      </section>
    </main>
  );
}
