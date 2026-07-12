"""Function discovery parity — default: Ghidra vs Fission over HTTP."""
from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer

from benchmark.common.binaries import load_binary_subjects
from benchmark.common.compare_guards import empty_pair_result
from benchmark.common.http_providers import fetch_parity_json
from benchmark.common.io import write_jsonl
from benchmark.common.providers import canonicalize, normalize_address, run_json_provider
from benchmark.common.result import error_result
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject

app = typer.Typer(pretty_exceptions_enable=False)


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


def compare_functions(
    subject: BenchmarkSubject,
    reference_name: str,
    candidate_name: str,
    expected: object,
    actual: object,
) -> BenchmarkResult:
    """Compare function inventories.

    Presence (address set) is the primary reliability signal. Name-only
    differences are reported as ``function_metadata`` and still count as
    mismatch for inventory equality, but metrics separate the two.
    """
    guarded = empty_pair_result(
        subject, "function_discovery", reference_name, candidate_name, expected, actual
    )
    if guarded is not None:
        return guarded

    expected_norm = canonicalize(expected)
    actual_norm = canonicalize(actual)
    expected_addrs = function_addresses(expected_norm)
    actual_addrs = function_addresses(actual_norm)

    # Name map for metadata (normalized addresses).
    def name_map(functions: object) -> dict[str, str]:
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

    exp_names = name_map(expected_norm)
    act_names = name_map(actual_norm)
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

    return BenchmarkResult(
        subject=subject,
        stage="function_discovery",
        status=status,
        reference=reference_name,
        candidate=candidate_name,
        mismatch_kind=mismatch_kind,
        expected=expected,
        actual=actual,
        metrics={
            "expected_function_count": len(expected_addrs),
            "actual_function_count": len(actual_addrs),
            "missing_function_count": len(expected_addrs - actual_addrs),
            "extra_function_count": len(actual_addrs - expected_addrs),
            "name_mismatch_count": name_mismatches,
            # Presence-only rate signal for dashboards (1 if all expected addrs found).
            "presence_recall": (
                1.0
                if not expected_addrs
                else round(len(expected_addrs & actual_addrs) / len(expected_addrs), 4)
            ),
        },
    )


@app.command()
def main(
    reference_http: Optional[str] = typer.Option("ghidra", "--reference-http"),
    candidate_http: Optional[str] = typer.Option("fission", "--candidate-http"),
    reference_command: Optional[str] = typer.Option(None),
    candidate_command: Optional[str] = typer.Option(None),
    reference_name: str = typer.Option("ghidra"),
    candidate_name: str = typer.Option("fission"),
    corpus: str = typer.Option("dev"),
    output: Path = typer.Option(Path("results/function_discovery/latest.jsonl")),
    limit: Optional[int] = typer.Option(None),
    timeout: float = typer.Option(90.0),
):
    """Compare whole-binary function inventories (one row per binary variant)."""
    if reference_command:
        reference_http = None
    if candidate_command:
        candidate_http = None
    if not reference_http and not reference_command:
        reference_http = "ghidra"
    if not candidate_http and not candidate_command:
        candidate_http = "fission"

    def ref_provider(subject: BenchmarkSubject) -> object:
        if reference_http:
            return fetch_parity_json(reference_http, "function_discovery", subject, timeout=timeout)
        assert reference_command
        return run_json_provider(reference_command, subject, timeout)

    def cand_provider(subject: BenchmarkSubject) -> object:
        if candidate_http:
            return fetch_parity_json(candidate_http, "function_discovery", subject, timeout=timeout)
        assert candidate_command
        return run_json_provider(candidate_command, subject, timeout)

    ref_label = reference_http or reference_name
    cand_label = candidate_http or candidate_name

    rows: list[BenchmarkResult] = []
    subjects = load_binary_subjects(corpus)
    if limit is not None:
        subjects = subjects[:limit]

    for subject in subjects:
        try:
            expected = ref_provider(subject)
            actual = cand_provider(subject)
            rows.append(compare_functions(subject, ref_label, cand_label, expected, actual))
        except Exception as exc:
            rows.append(
                error_result(subject, "function_discovery", ref_label, cand_label, str(exc))
            )

    write_jsonl(output, rows)
    typer.echo(f"Wrote {len(rows)} function discovery rows to {output}")


if __name__ == "__main__":
    app()
