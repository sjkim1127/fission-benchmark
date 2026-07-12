"""Strip-track function discovery: Ghidra vs Fission on stripped PE."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

import typer

from benchmark.common.http_providers import ensure_fission_port, fetch_parity_json
from benchmark.common.io import write_jsonl
from benchmark.function_discovery.run import compare_functions, function_addresses
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject

app = typer.Typer(pretty_exceptions_enable=False)

STAGE = "strip_discovery"
MANIFEST = Path("corpus/realworld/manifests/strip_from_dev.json")


def _load_subjects() -> list[BenchmarkSubject]:
    if not MANIFEST.is_file():
        return []
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    out: list[BenchmarkSubject] = []
    for row in data.get("functions") or []:
        if not isinstance(row, dict):
            continue
        binary = str(row.get("binary") or "")
        if not binary.startswith("corpus/"):
            binary = f"corpus/realworld/{binary}"
        out.append(
            BenchmarkSubject(
                binary=binary,
                function=str(row.get("name") or "unknown"),
                addr=str(row.get("addr") or "0x0"),
                arch=str(row.get("arch") or "x86_64"),
                compiler=str(row.get("compiler") or "unknown"),
                opt=str(row.get("opt") or "strip"),
                corpus_split="realworld",
            )
        )
    return out


@app.command()
def main(
    output: Path = typer.Option(Path("results/strip_discovery/latest.jsonl")),
    limit: Optional[int] = typer.Option(None),
    timeout: float = typer.Option(90.0),
):
    ensure_fission_port()
    subjects = _load_subjects()
    if limit is not None:
        subjects = subjects[:limit]

    rows: list[BenchmarkResult] = []
    if not subjects:
        dummy = BenchmarkSubject(
            binary="corpus/realworld/(none)",
            function="(no_strip_corpus)",
            addr="0x0",
            arch="unknown",
            compiler="unknown",
            opt="strip",
            corpus_split="realworld",
        )
        rows.append(
            BenchmarkResult(
                subject=dummy,
                stage=STAGE,  # type: ignore[arg-type]
                status="skipped",
                reference="ghidra",
                candidate="fission",
                mismatch_kind="strip_corpus_empty",
                error="Run scripts/build_strip_corpus.py first",
            )
        )
        write_jsonl(output, rows)
        typer.echo(f"Wrote {len(rows)} rows (empty corpus) to {output}")
        return

    # One inventory compare per unique stripped binary.
    by_bin: dict[str, list[BenchmarkSubject]] = {}
    for s in subjects:
        by_bin.setdefault(s.binary, []).append(s)

    for binary, group in by_bin.items():
        inv = BenchmarkSubject(
            binary=binary,
            function="(inventory)",
            addr="0x0",
            arch=group[0].arch,
            compiler=group[0].compiler,
            opt=group[0].opt,
            corpus_split="realworld",
        )
        try:
            try:
                ref = fetch_parity_json("ghidra", "function_discovery", inv, timeout=timeout)
            except Exception as exc:
                ref = []
                err = str(exc)
            else:
                err = None
            try:
                cand = fetch_parity_json("fission", "function_discovery", inv, timeout=timeout)
            except Exception as exc:
                cand = []
                err = (err or "") + f"; fission: {exc}"
            if err and not ref and not cand:
                rows.append(
                    BenchmarkResult(
                        subject=inv,
                        stage=STAGE,  # type: ignore[arg-type]
                        status="fetch_error",
                        reference="ghidra",
                        candidate="fission",
                        error=err,
                    )
                )
                continue
            row = compare_functions(inv, "ghidra", "fission", ref, cand)
            from benchmark.function_discovery.run import normalize_function_address

            m_norm = {
                normalize_function_address(s.addr)
                for s in group
                if normalize_function_address(s.addr)
            }
            cand_addrs = function_addresses(cand)
            ref_addrs = function_addresses(ref)
            metrics = dict(row.metrics or {})
            metrics["scored_as"] = "strip_ghidra_inventory"
            metrics["manifest_recall"] = (
                1.0
                if not m_norm
                else round(len(m_norm & cand_addrs) / len(m_norm), 4)
            )
            metrics["manifest_ref_recall"] = (
                1.0
                if not m_norm
                else round(len(m_norm & ref_addrs) / len(m_norm), 4)
            )
            metrics["manifest_addrs"] = len(m_norm)
            metrics["strip"] = 1
            rows.append(
                BenchmarkResult(
                    subject=row.subject,
                    stage=STAGE,  # type: ignore[arg-type]
                    status=row.status,
                    reference=row.reference,
                    candidate=row.candidate,
                    mismatch_kind=row.mismatch_kind,
                    expected=row.expected,
                    actual=row.actual,
                    metrics=metrics,
                    error=row.error,
                )
            )
        except Exception as exc:
            rows.append(
                BenchmarkResult(
                    subject=inv,
                    stage=STAGE,  # type: ignore[arg-type]
                    status="error",
                    reference="ghidra",
                    candidate="fission",
                    error=str(exc),
                )
            )

    write_jsonl(output, rows)
    typer.echo(f"Wrote {len(rows)} strip_discovery rows to {output}")


if __name__ == "__main__":
    app()
