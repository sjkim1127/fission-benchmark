"""Function discovery benchmark — inventory parity (primary quality stage).

Contract
--------
* Unit of analysis: **one binary variant** (compiler × opt), not one function.
* Request: full function inventory from each tool's ``GET /functions``.
* Primary equality: **normalized address sets** (names are metadata).
* Dual metrics (always emitted for reliability gates):
  - ``presence_recall``  = |R ∩ C| / |R|
  - ``presence_precision`` = |R ∩ C| / |C|
  - ``presence_f1`` / ``presence_jaccard``
  - ``manifest_recall`` when corpus subject VAs are known

References
----------
* Default: **Ghidra** full inventory (tool-relative reference).
* Optional: **PE COFF/export symbols** (unstripped ground truth).
* Optional: **corpus manifest** entry VAs only (subject coverage).

This is the "function finding" benchmark — distinct from same-function matrix
(which checks that decompile requests hit a single requested entry).
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable, Optional

import typer

from benchmark.common.binaries import load_binary_subjects
from benchmark.common.compare_guards import empty_pair_result
from benchmark.common.http_providers import fetch_parity_json
from benchmark.common.io import write_jsonl
from benchmark.common.providers import canonicalize, normalize_address, run_json_provider
from benchmark.common.result import error_result
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject
from benchmark.common.subjects import load_subjects
from benchmark.function_discovery.pe_oracle import (
    inventory_from_addresses,
    pe_symbol_inventory,
)

app = typer.Typer(pretty_exceptions_enable=False, help="Function discovery inventory parity")

STAGE = "function_discovery"
SCORED_AS = "ghidra_inventory"  # modern inventory scoring (telemetry gate)


def normalize_function_address(value: object) -> str:
    text = str(value or "").strip()
    if not text:
        return ""
    try:
        return normalize_address(text)
    except Exception:
        return text.lower()


def function_addresses(functions: object) -> set[str]:
    if not isinstance(functions, list):
        return set()
    addresses: set[str] = set()
    for fn in functions:
        if isinstance(fn, dict) and fn.get("address") is not None:
            key = normalize_function_address(fn["address"])
            if key:
                addresses.add(key)
    return addresses


def inventory_dual_metrics(
    ref_addrs: set[str],
    cand_addrs: set[str],
    *,
    manifest_addrs: set[str] | None = None,
) -> dict[str, Any]:
    """Set-level dual metrics for function inventories."""
    shared = ref_addrs & cand_addrs
    missing = ref_addrs - cand_addrs
    extra = cand_addrs - ref_addrs
    recall = (
        1.0 if not ref_addrs else round(len(shared) / len(ref_addrs), 4)
    )
    precision = (
        1.0 if not cand_addrs else round(len(shared) / len(cand_addrs), 4)
    )
    if recall + precision > 0:
        f1 = round(2 * precision * recall / (precision + recall), 4)
    else:
        f1 = 0.0 if ref_addrs or cand_addrs else 1.0
    union = ref_addrs | cand_addrs
    jaccard = 1.0 if not union else round(len(shared) / len(union), 4)

    metrics: dict[str, Any] = {
        "scored_as": SCORED_AS,
        "expected_function_count": len(ref_addrs),
        "actual_function_count": len(cand_addrs),
        "shared_function_count": len(shared),
        "missing_function_count": len(missing),
        "extra_function_count": len(extra),
        "presence_recall": recall,
        "presence_precision": precision,
        "presence_f1": f1,
        "presence_jaccard": jaccard,
    }
    if manifest_addrs is not None:
        m_found = manifest_addrs & cand_addrs
        metrics["manifest_subject_count"] = len(manifest_addrs)
        metrics["manifest_found_count"] = len(m_found)
        metrics["manifest_recall"] = (
            1.0
            if not manifest_addrs
            else round(len(m_found) / len(manifest_addrs), 4)
        )
        metrics["manifest_missing_count"] = len(manifest_addrs - cand_addrs)
    return metrics


def _name_map(functions: object) -> dict[str, str]:
    out: dict[str, str] = {}
    if not isinstance(functions, list):
        return out
    for fn in functions:
        if not isinstance(fn, dict) or fn.get("address") is None:
            continue
        key = normalize_function_address(fn["address"])
        if key:
            out[key] = str(fn.get("name") or "").lower()
    return out


def compare_functions(
    subject: BenchmarkSubject,
    reference_name: str,
    candidate_name: str,
    expected: object,
    actual: object,
    *,
    manifest_addrs: set[str] | None = None,
    scored_as: str = SCORED_AS,
) -> BenchmarkResult:
    """Compare function inventories (address-set primary, dual metrics always)."""
    guarded = empty_pair_result(
        subject, STAGE, reference_name, candidate_name, expected, actual
    )
    if guarded is not None:
        # Still attach dual metrics when one side is empty for triage.
        exp_addrs = function_addresses(expected)
        act_addrs = function_addresses(actual)
        dual = inventory_dual_metrics(
            exp_addrs, act_addrs, manifest_addrs=manifest_addrs
        )
        dual["scored_as"] = scored_as
        return BenchmarkResult(
            subject=guarded.subject,
            stage=guarded.stage,
            status=guarded.status,
            reference=guarded.reference,
            candidate=guarded.candidate,
            mismatch_kind=guarded.mismatch_kind,
            expected=guarded.expected,
            actual=guarded.actual,
            metrics={**(guarded.metrics or {}), **dual},
            error=guarded.error,
        )

    expected_norm = canonicalize(expected)
    actual_norm = canonicalize(actual)
    expected_addrs = function_addresses(expected_norm)
    actual_addrs = function_addresses(actual_norm)

    exp_names = _name_map(expected_norm)
    act_names = _name_map(actual_norm)
    name_mismatches = sum(
        1
        for addr in expected_addrs & actual_addrs
        if exp_names.get(addr, "") != act_names.get(addr, "")
    )

    if expected_addrs == actual_addrs and name_mismatches == 0:
        status = "match"
        mismatch_kind = None
    elif expected_addrs != actual_addrs:
        status = "mismatch"
        mismatch_kind = "function_set"
    else:
        status = "mismatch"
        mismatch_kind = "function_metadata"

    metrics = inventory_dual_metrics(
        expected_addrs, actual_addrs, manifest_addrs=manifest_addrs
    )
    metrics["scored_as"] = scored_as
    metrics["name_mismatch_count"] = name_mismatches

    return BenchmarkResult(
        subject=subject,
        stage=STAGE,
        status=status,
        reference=reference_name,
        candidate=candidate_name,
        mismatch_kind=mismatch_kind,
        expected=expected,
        actual=actual,
        metrics=metrics,
    )


def _manifest_addrs_for_binary(
    binary: str, corpus: str, all_subjects: list[BenchmarkSubject] | None = None
) -> set[str]:
    subjects = all_subjects if all_subjects is not None else load_subjects(corpus)
    out: set[str] = set()
    # Match on basename — paths may be absolute vs corpus-relative.
    target = Path(binary).name
    for s in subjects:
        if Path(s.binary).name != target and s.binary != binary:
            continue
        key = normalize_function_address(s.addr)
        if key and key not in {"0x0", "0"}:
            out.add(key)
    return out


def _resolve_reference(
    *,
    mode: str,
    subject: BenchmarkSubject,
    reference_http: str | None,
    reference_command: str | None,
    timeout: float,
) -> tuple[str, object]:
    """Return (label, inventory)."""
    if mode == "pe_symbols":
        inv = pe_symbol_inventory(subject.binary)
        if not inv:
            raise RuntimeError(f"no PE COFF/export symbols for {subject.binary}")
        return "pe_symbols", inv
    if mode == "manifest":
        # Inventory = corpus subject entries only (minimal ground truth).
        addrs = []
        for s in load_subjects(subject.corpus_split or "dev"):
            if Path(s.binary).name == Path(subject.binary).name or s.binary == subject.binary:
                addrs.append(s.addr)
        return "manifest", inventory_from_addresses(addrs)
    if reference_command:
        return "command", run_json_provider(reference_command, subject, timeout)
    tool = reference_http or "ghidra"
    return tool, fetch_parity_json(tool, STAGE, subject, timeout=timeout)


@app.command()
def main(
    reference_http: Optional[str] = typer.Option(
        "ghidra", "--reference-http", help="HTTP adapter for reference inventory"
    ),
    candidate_http: Optional[str] = typer.Option(
        "fission",
        "--candidate-http",
        help="Single candidate (ignored if --candidates set)",
    ),
    candidates: Optional[str] = typer.Option(
        None,
        "--candidates",
        help="Comma-separated candidate adapters (e.g. fission,radare2,snowman)",
    ),
    reference_command: Optional[str] = typer.Option(None),
    candidate_command: Optional[str] = typer.Option(None),
    reference_name: str = typer.Option("ghidra"),
    candidate_name: str = typer.Option("fission"),
    reference_mode: str = typer.Option(
        "http",
        "--reference-mode",
        help="http | pe_symbols | manifest",
    ),
    corpus: str = typer.Option("dev"),
    output: Path = typer.Option(Path("results/function_discovery/latest.jsonl")),
    summary_json: Optional[Path] = typer.Option(
        Path("results/function_discovery/summary.json"),
        "--summary-json",
        help="Write aggregate discovery report JSON",
    ),
    summary_md: Optional[Path] = typer.Option(
        Path("results/function_discovery/summary.md"),
        "--summary-md",
        help="Write Markdown discovery report",
    ),
    limit: Optional[int] = typer.Option(None),
    timeout: float = typer.Option(90.0),
    with_manifest_recall: bool = typer.Option(
        True,
        "--with-manifest-recall/--no-manifest-recall",
        help="Attach corpus subject VA recall on each row",
    ),
):
    """Compare whole-binary function inventories (one row per binary × candidate)."""
    if reference_command:
        reference_http = None
    if candidate_command and not candidates:
        candidate_http = None
    if not reference_http and not reference_command and reference_mode == "http":
        reference_http = "ghidra"

    cand_list: list[tuple[str, str | None, str | None]] = []
    # (label, http_tool|None, command|None)
    if candidates:
        for name in [c.strip() for c in candidates.split(",") if c.strip()]:
            cand_list.append((name, name, None))
    elif candidate_command:
        cand_list.append((candidate_name, None, candidate_command))
    else:
        tool = candidate_http or "fission"
        cand_list.append((tool, tool, None))

    all_function_subjects = load_subjects(corpus) if with_manifest_recall else []
    binary_subjects = load_binary_subjects(corpus)
    if limit is not None:
        binary_subjects = binary_subjects[:limit]

    rows: list[BenchmarkResult] = []
    for subject in binary_subjects:
        try:
            ref_label, expected = _resolve_reference(
                mode=reference_mode,
                subject=subject,
                reference_http=reference_http,
                reference_command=reference_command,
                timeout=timeout,
            )
        except Exception as exc:
            for label, _, _ in cand_list:
                rows.append(
                    error_result(subject, STAGE, reference_mode, label, str(exc))
                )
            continue

        manifest_addrs = (
            _manifest_addrs_for_binary(
                subject.binary, corpus, all_function_subjects
            )
            if with_manifest_recall
            else None
        )
        scored_as = (
            "pe_symbol_inventory"
            if reference_mode == "pe_symbols"
            else "manifest_inventory"
            if reference_mode == "manifest"
            else SCORED_AS
        )

        for label, http_tool, command in cand_list:
            try:
                if command:
                    actual = run_json_provider(command, subject, timeout)
                else:
                    assert http_tool
                    actual = fetch_parity_json(
                        http_tool, STAGE, subject, timeout=timeout
                    )
                rows.append(
                    compare_functions(
                        subject,
                        ref_label if reference_mode == "http" else reference_mode,
                        label,
                        expected,
                        actual,
                        manifest_addrs=manifest_addrs,
                        scored_as=scored_as,
                    )
                )
            except Exception as exc:
                rows.append(
                    error_result(
                        subject,
                        STAGE,
                        ref_label if reference_mode == "http" else reference_mode,
                        label,
                        str(exc),
                    )
                )

    write_jsonl(output, rows)
    typer.echo(
        f"Wrote {len(rows)} function discovery rows to {output} "
        f"(binaries={len(binary_subjects)}, candidates={len(cand_list)}, "
        f"ref_mode={reference_mode})"
    )

    if summary_json or summary_md:
        try:
            from runner.function_discovery_report import (
                build_discovery_report,
                render_markdown,
            )
        except ImportError:
            from function_discovery_report import (  # type: ignore
                build_discovery_report,
                render_markdown,
            )

        report = build_discovery_report(rows)
        report["source"] = str(output)
        report["corpus"] = corpus
        report["reference_mode"] = reference_mode
        if summary_json:
            summary_json.parent.mkdir(parents=True, exist_ok=True)
            summary_json.write_text(
                json.dumps(report, indent=2, default=str) + "\n", encoding="utf-8"
            )
            typer.echo(f"Wrote summary JSON {summary_json}")
        if summary_md:
            summary_md.parent.mkdir(parents=True, exist_ok=True)
            summary_md.write_text(render_markdown(report), encoding="utf-8")
            typer.echo(f"Wrote summary Markdown {summary_md}")


if __name__ == "__main__":
    app()
