import { Suspense } from "react";
import { SiteChrome } from "@/components/SiteChrome";
import { ValidityBanner } from "@/components/ValidityBanner";
import { UnavailableData } from "@/components/UnavailableData";
import {
  MetaStrip,
  SkeletonMeta,
  SkeletonSection,
} from "@/components/DashboardShared";
import {
  getLatestBenchmarkOptional,
  extractQualityExtensions,
  buildReadabilityDiagnostics,
} from "@/lib/benchmark";
import { ReadabilityDiagnosticsPanel } from "@/components/ReadabilityDiagnosticsPanel";
import styles from "../dashboard.module.css";
import tableStyles from "@/components/SummaryTable.module.css";

export const revalidate = 900;

export const metadata = {
  title: "Quality extensions · Diagnostics",
  description:
    "Bare-compile rate, readability proxies, and track/ISA pivots — non-ranking diagnostics.",
};

async function BannerSection() {
  const data = await getLatestBenchmarkOptional();
  if (!data) return null;
  return <ValidityBanner validity={data.validity} run={data.run} />;
}

function RateCell({ value }: { value: number | null | undefined }) {
  if (value == null || Number.isNaN(value)) return <span>—</span>;
  return <span>{(value * 100).toFixed(1)}%</span>;
}

async function QualitySection() {
  const data = await getLatestBenchmarkOptional();
  if (!data) {
    return (
      <section className={styles.section}>
        <h2 className={styles.sectionTitle}>Quality extensions</h2>
        <UnavailableData />
      </section>
    );
  }

  const ext = extractQualityExtensions(data);
  const bareTools = Object.keys(ext.bareByDecompiler).sort((a, b) => {
    if (a === "fission") return -1;
    if (b === "fission") return 1;
    if (a === "ghidra") return -1;
    if (b === "ghidra") return 1;
    return a.localeCompare(b);
  });
  const readStats = buildReadabilityDiagnostics(data);
  const tracks = Object.keys(ext.byTrack);
  const isas = Object.keys(ext.byIsa);
  const formats = Object.keys(ext.byFormat);

  return (
    <>
      <section className={styles.section}>
        <h2 className={styles.sectionTitle}>Non-ranking diagnostics</h2>
        <p className={styles.sectionLead}>
          Semantic pass rate on the <strong>original_binary</strong> oracle
          remains the only ranking axis. The tables below are form quality,
          readability proxies (including source similarity and AST), and track
          pivots for investigation only.
        </p>
        <div className={styles.frame}>
          <div className={styles.frameTitle}>Policy</div>
          <p className={styles.frameBody}>
            Bare-compile uses minimal headers + <code>gcc -c</code>. Readability
            reports source similarity, AST tree-edit similarity, proxy score,
            generic naming, goto / nest / temp / flag density. For Fission,
            semantic rows use NIR; readability proxies prefer HIR when dual
            layers are present. Study pack:{" "}
            <code>benchmark/readability/</code>.
          </p>
        </div>
      </section>

      <section className={styles.section}>
        <h2 className={styles.sectionTitle}>EXT · Bare-compile rate</h2>
        {bareTools.length === 0 ? (
          <p className={styles.sectionLead}>
            No bare-compile field on this envelope yet (re-run runner after the
            quality-extensions ship).
          </p>
        ) : (
          <div className={tableStyles.wrap}>
            <table className={tableStyles.table}>
              <thead>
                <tr>
                  <th>Decompiler</th>
                  <th>Attempted</th>
                  <th>OK</th>
                  <th>Fail</th>
                  <th>OK rate</th>
                </tr>
              </thead>
              <tbody>
                {bareTools.map((tool) => {
                  const row = ext.bareByDecompiler[tool] || {};
                  return (
                    <tr
                      key={tool}
                      className={
                        tool === "fission" ? tableStyles.fissionRow : undefined
                      }
                    >
                      <td>{tool}</td>
                      <td className={tableStyles.num}>{row.attempted ?? "—"}</td>
                      <td className={tableStyles.num}>{row.ok ?? "—"}</td>
                      <td className={tableStyles.num}>{row.fail ?? "—"}</td>
                      <td className={tableStyles.num}>
                        <RateCell value={row.ok_rate as number | null} />
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        )}
      </section>

      <section className={styles.section}>
        <h2 className={styles.sectionTitle}>
          EXT · Readability · source sim · AST
        </h2>
        <ReadabilityDiagnosticsPanel
          stats={readStats}
          compact={false}
          showStudyNote
        />
      </section>

      <section className={styles.section}>
        <h2 className={styles.sectionTitle}>EXT · Tracks · ISA · format</h2>
        {tracks.length === 0 && isas.length === 0 ? (
          <p className={styles.sectionLead}>
            No track/ISA pivot data on this envelope.
          </p>
        ) : (
          <>
            {tracks.length > 0 ? (
              <div className={tableStyles.wrap}>
                <h3 className={styles.sectionTitle}>By track</h3>
                <table className={tableStyles.table}>
                  <thead>
                    <tr>
                      <th>Track</th>
                      <th>Rows</th>
                      <th>Tested</th>
                      <th>Mean pass</th>
                      <th>Perfect</th>
                      <th>Timeouts</th>
                    </tr>
                  </thead>
                  <tbody>
                    {tracks.map((name) => {
                      const row = ext.byTrack[name] || {};
                      return (
                        <tr key={name}>
                          <td>{name}</td>
                          <td className={tableStyles.num}>{row.rows ?? "—"}</td>
                          <td className={tableStyles.num}>
                            {row.semantic_tested ?? "—"}
                          </td>
                          <td className={tableStyles.num}>
                            <RateCell
                              value={row.mean_pass_rate as number | null}
                            />
                          </td>
                          <td className={tableStyles.num}>
                            {row.perfect_rows ?? "—"}
                          </td>
                          <td className={tableStyles.num}>
                            {row.timeout_rows ?? "—"}
                          </td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>
            ) : null}
            {isas.length > 0 ? (
              <div className={tableStyles.wrap}>
                <h3 className={styles.sectionTitle}>By ISA</h3>
                <table className={tableStyles.table}>
                  <thead>
                    <tr>
                      <th>ISA</th>
                      <th>Rows</th>
                      <th>Mean pass</th>
                      <th>Timeouts</th>
                    </tr>
                  </thead>
                  <tbody>
                    {isas.map((name) => {
                      const row = ext.byIsa[name] || {};
                      return (
                        <tr key={name}>
                          <td>{name}</td>
                          <td className={tableStyles.num}>{row.rows ?? "—"}</td>
                          <td className={tableStyles.num}>
                            <RateCell
                              value={row.mean_pass_rate as number | null}
                            />
                          </td>
                          <td className={tableStyles.num}>
                            {row.timeout_rows ?? "—"}
                          </td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>
            ) : null}
            {formats.length > 0 ? (
              <div className={tableStyles.wrap}>
                <h3 className={styles.sectionTitle}>By format</h3>
                <table className={tableStyles.table}>
                  <thead>
                    <tr>
                      <th>Format</th>
                      <th>Rows</th>
                      <th>Mean pass</th>
                    </tr>
                  </thead>
                  <tbody>
                    {formats.map((name) => {
                      const row = ext.byFormat[name] || {};
                      return (
                        <tr key={name}>
                          <td>{name}</td>
                          <td className={tableStyles.num}>{row.rows ?? "—"}</td>
                          <td className={tableStyles.num}>
                            <RateCell
                              value={row.mean_pass_rate as number | null}
                            />
                          </td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>
            ) : null}
          </>
        )}
      </section>
    </>
  );
}

export default function QualityPage() {
  return (
    <SiteChrome
      active="quality"
      subtitle="Quality extensions — diagnostics only, never ranking"
    >
      <Suspense fallback={<SkeletonMeta />}>
        <BannerSection />
      </Suspense>
      <Suspense fallback={<SkeletonMeta />}>
        <MetaStrip />
      </Suspense>
      <Suspense fallback={<SkeletonSection />}>
        <QualitySection />
      </Suspense>
    </SiteChrome>
  );
}
