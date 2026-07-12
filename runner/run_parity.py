"""Unified Parity Runner for Fission Benchmark infrastructure.

Coordinates assembly, decode, p-code, CFG, function discovery, and invariant parity checks.
"""
from __future__ import annotations

import argparse
import json
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
import requests

from benchmark.assembly_parity.run import compare_assembly
from benchmark.cfg_parity.run import compare_cfg
from benchmark.decode_parity.run import compare_decode
from benchmark.function_discovery.run import compare_functions, function_addresses
from benchmark.ir_invariants.run import compare_invariants
from benchmark.pcode_parity.run import compare_pcode
from benchmark.telemetry.aggregate import aggregate_rows
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject

# Port mapping of decompiler containers
PORT_MAPPING = {
    # Local quality-loop compose may map fission to 8007; override via FISSION_HOST_PORT.
    "fission": int(os.environ.get("FISSION_HOST_PORT", "8000")),
    "reko": int(os.environ.get("REKO_HOST_PORT", "8008")),
    "ghidra": int(os.environ.get("GHIDRA_HOST_PORT", "8001")),
    "boomerang": int(os.environ.get("BOOMERANG_HOST_PORT", "8002")),
    "radare2": int(os.environ.get("RADARE2_HOST_PORT", "8003")),
    "angr": int(os.environ.get("ANGR_HOST_PORT", "8004")),
    "snowman": int(os.environ.get("SNOWMAN_HOST_PORT", "8005")),
    "revng": int(os.environ.get("REVNG_HOST_PORT", "8006")),
}

# How many unique PE files to multi_bundle-prefetch concurrently.
# Matches Ghidra GHIDRA_HEADLESS_WORKERS default (3).
BINARY_WORKERS = max(1, int(os.environ.get("PARITY_BINARY_WORKERS", "3")))


@dataclass
class FetchResult:
    """Result of a single parity endpoint fetch.

    Distinguishes between successful data, empty data, and fetch errors so that
    callers can avoid treating a double-empty response as a valid match.

    status values:
      "ok"          — HTTP 200 with non-empty data
      "empty"       — HTTP 200 but data is empty ([] or {blocks:[], edges:[]})
      "fetch_error" — network error, timeout, or non-200 HTTP status
    """
    status: str  # "ok" | "empty" | "fetch_error"
    data: Any = field(default_factory=list)
    error: str | None = None

    def is_usable(self) -> bool:
        """Return True only when data was successfully fetched and is non-empty."""
        return self.status == "ok"


_EMPTY_LIST_FETCH = FetchResult(status="empty", data=[])
_EMPTY_CFG_FETCH  = FetchResult(status="empty", data={"blocks": [], "edges": []})


def _as_fetch(data: object, *, is_cfg: bool = False) -> FetchResult:
    if is_cfg:
        empty = (
            not data
            or not isinstance(data, dict)
            or (not data.get("blocks") and not data.get("edges"))
        )
        return FetchResult(
            status="empty" if empty else "ok",
            data=data if isinstance(data, dict) else {"blocks": [], "edges": []},
        )
    empty = not data
    return FetchResult(status="empty" if empty else "ok", data=data if data is not None else [])


def _normalize_addr_key(addr: str) -> str:
    text = (addr or "").strip().lower()
    try:
        if text.startswith("0x"):
            return f"0x{int(text, 16):x}"
        return f"0x{int(text, 16):x}"
    except ValueError:
        return text


def _bundle_dict_to_fetches(data: dict) -> tuple[FetchResult, FetchResult, FetchResult, FetchResult]:
    tool_errors = data.get("tool_errors") if isinstance(data.get("tool_errors"), dict) else {}
    disasm = data.get("disasm")
    decode = data.get("decode")
    if decode is None and isinstance(disasm, list):
        decode = [
            {
                "address": inst.get("address"),
                "bytes": inst.get("bytes"),
                "length": inst.get("length"),
                "mnemonic": inst.get("mnemonic"),
                "prefixes": [],
                "modrm": None,
                "sib": None,
                "displacement": None,
                "immediate": None,
            }
            for inst in disasm
            if isinstance(inst, dict)
        ]

    def _stage_fetch(surface: str, payload: object, *, is_cfg: bool = False) -> FetchResult:
        # Partial multi_bundle: tool_errors marks a failed CLI without killing others.
        if surface in tool_errors:
            return FetchResult(
                status="fetch_error",
                data={"blocks": [], "edges": []} if is_cfg else [],
                error=str(tool_errors[surface]),
            )
        return _as_fetch(payload, is_cfg=is_cfg)

    return (
        _stage_fetch("disasm", disasm),
        # decode is derived from disasm; inherit disasm tool failure
        _stage_fetch("disasm", decode)
        if "disasm" in tool_errors
        else _as_fetch(decode),
        _stage_fetch("pcode", data.get("pcode")),
        _stage_fetch("cfg", data.get("cfg"), is_cfg=True),
    )


def _fetch_ghidra_reference_bundle(
    binary: str,
    addr: str,
    arch: str,
    *,
    corpus: str,
    timeout: float,
) -> tuple[FetchResult, FetchResult, FetchResult, FetchResult]:
    """Prefer one /parity_bundle call; fall back to four separate endpoints."""
    bundle = fetch_parity_data(
        "ghidra", "parity_bundle", binary, addr, arch, corpus=corpus, timeout=timeout
    )
    if bundle.status == "ok" and isinstance(bundle.data, dict) and (
        "disasm" in bundle.data or "pcode" in bundle.data or "cfg" in bundle.data
    ):
        return _bundle_dict_to_fetches(bundle.data)

    # Legacy adapter path
    return (
        fetch_parity_data("ghidra", "disasm", binary, addr, arch, corpus=corpus, timeout=timeout),
        fetch_parity_data("ghidra", "decode", binary, addr, arch, corpus=corpus, timeout=timeout),
        fetch_parity_data("ghidra", "pcode", binary, addr, arch, corpus=corpus, timeout=timeout),
        fetch_parity_data("ghidra", "cfg", binary, addr, arch, corpus=corpus, timeout=timeout),
    )


def _multi_bundle_response_to_map(
    multi: FetchResult,
) -> dict[str, tuple[FetchResult, FetchResult, FetchResult, FetchResult]] | None:
    """Parse a parity_multi_bundle response into addr → stage fetches.

    Returns None when the response is not a usable multi_bundle payload
    (caller should fall back to per-address fetches).
    """
    if multi.status != "ok" or not isinstance(multi.data, dict):
        return None
    by_addr = multi.data.get("by_addr") or {}
    if not isinstance(by_addr, dict) or not by_addr:
        return None
    out: dict[str, tuple[FetchResult, FetchResult, FetchResult, FetchResult]] = {}
    for key, payload in by_addr.items():
        nk = _normalize_addr_key(str(key))
        if isinstance(payload, dict) and "error" not in payload:
            out[nk] = _bundle_dict_to_fetches(payload)
        else:
            err = (
                payload.get("error")
                if isinstance(payload, dict)
                else "missing payload"
            )
            err_fr = FetchResult(status="fetch_error", data=[], error=str(err))
            cfg_err = FetchResult(
                status="fetch_error",
                data={"blocks": [], "edges": []},
                error=str(err),
            )
            out[nk] = (err_fr, err_fr, err_fr, cfg_err)
    return out


def _prefetch_ghidra_multi_bundle(
    binary: str,
    addrs: list[str],
    arch: str,
    *,
    corpus: str,
    timeout: float,
) -> dict[str, tuple[FetchResult, FetchResult, FetchResult, FetchResult]]:
    """One headless call for many addresses on the same binary.

    Returns map: normalized_addr → (asm, decode, pcode, cfg) FetchResults.
    """
    if not addrs:
        return {}
    joined = ",".join(addrs)
    multi = fetch_parity_data(
        "ghidra",
        "parity_multi_bundle",
        binary,
        arch=arch,
        corpus=corpus,
        timeout=max(timeout, 120.0),
        addrs=joined,
    )
    parsed = _multi_bundle_response_to_map(multi)
    if parsed is not None:
        return parsed

    # Fallback: per-address bundle
    out: dict[str, tuple[FetchResult, FetchResult, FetchResult, FetchResult]] = {}
    for addr in addrs:
        out[_normalize_addr_key(addr)] = _fetch_ghidra_reference_bundle(
            binary, addr, arch, corpus=corpus, timeout=timeout
        )
    return out


def _prefetch_candidate_multi_bundle(
    decompiler: str,
    binary: str,
    addrs: list[str],
    arch: str,
    *,
    corpus: str,
    timeout: float,
) -> dict[str, tuple[FetchResult, FetchResult, FetchResult, FetchResult]]:
    """Batch-prefetch candidate (e.g. fission) via /parity_multi_bundle.

    Falls back to per-address /parity_bundle, then four legacy endpoints.
    Returns empty dict if the candidate has no bundle endpoints at all
    (caller falls back per-function).
    """
    if not addrs:
        return {}
    joined = ",".join(addrs)
    multi = fetch_parity_data(
        decompiler,
        "parity_multi_bundle",
        binary,
        arch=arch,
        corpus=corpus,
        timeout=max(timeout, 120.0),
        addrs=joined,
    )
    parsed = _multi_bundle_response_to_map(multi)
    if parsed is not None:
        return parsed

    out: dict[str, tuple[FetchResult, FetchResult, FetchResult, FetchResult]] = {}
    for addr in addrs:
        out[_normalize_addr_key(addr)] = _fetch_candidate_bundle(
            decompiler, binary, addr, arch, corpus=corpus, timeout=timeout
        )
    return out


def _fetch_candidate_bundle(
    decompiler: str,
    binary: str,
    addr: str,
    arch: str,
    *,
    corpus: str,
    timeout: float,
) -> tuple[FetchResult, FetchResult, FetchResult, FetchResult]:
    """Prefer one /parity_bundle call; fall back to four separate endpoints."""
    bundle = fetch_parity_data(
        decompiler, "parity_bundle", binary, addr, arch, corpus=corpus, timeout=timeout
    )
    if bundle.status == "ok" and isinstance(bundle.data, dict) and (
        "disasm" in bundle.data or "pcode" in bundle.data or "cfg" in bundle.data
    ):
        return _bundle_dict_to_fetches(bundle.data)

    return (
        fetch_parity_data(
            decompiler, "disasm", binary, addr, arch, corpus=corpus, timeout=timeout
        ),
        fetch_parity_data(
            decompiler, "decode", binary, addr, arch, corpus=corpus, timeout=timeout
        ),
        fetch_parity_data(
            decompiler, "pcode", binary, addr, arch, corpus=corpus, timeout=timeout
        ),
        fetch_parity_data(
            decompiler, "cfg", binary, addr, arch, corpus=corpus, timeout=timeout
        ),
    )


def fetch_parity_data(
    decompiler: str,
    endpoint: str,
    binary: str,
    addr: str = "",
    arch: str = "",
    corpus: str = "dev",
    timeout: float = 5.0,
    addrs: str = "",
) -> FetchResult:
    """Fetch data from a decompiler parity endpoint.

    Returns a :class:`FetchResult` with status ``"ok"``, ``"empty"``, or
    ``"fetch_error"``.  Callers must check ``FetchResult.status`` before
    treating the data as meaningful — an empty result must never be compared
    as a valid match.

    For ``parity_multi_bundle``, pass comma-separated ``addrs`` (not ``addr``).
    """
    is_cfg = endpoint == "cfg"
    is_bundle = endpoint in {"parity_bundle", "parity_multi_bundle"}
    port = PORT_MAPPING.get(decompiler)
    if not port:
        return FetchResult(
            status="fetch_error",
            data={"blocks": [], "edges": []} if is_cfg else ([] if not is_bundle else {}),
            error=f"No port configured for decompiler {decompiler!r}",
        )

    if not binary.startswith("corpus/"):
        binary = f"corpus/{corpus}/{binary}"
    url = f"http://localhost:{port}/{endpoint}?binary={binary}"
    if endpoint == "parity_multi_bundle" and addrs:
        url += f"&addrs={addrs}"
    elif addr:
        url += f"&addr={addr}"
    if arch:
        url += f"&arch={arch}"

    try:
        resp = requests.get(url, timeout=timeout)
        if resp.status_code != 200:
            return FetchResult(
                status="fetch_error",
                data={"blocks": [], "edges": []} if is_cfg else ([] if not is_bundle else {}),
                error=f"HTTP {resp.status_code}: {resp.text[:200]}",
            )
        data = resp.json()
        # Determine emptiness.
        if endpoint == "parity_multi_bundle":
            is_empty = not isinstance(data, dict) or not data.get("by_addr")
        elif is_bundle:
            is_empty = not isinstance(data, dict) or not any(
                data.get(k) for k in ("disasm", "pcode", "cfg")
            )
        elif is_cfg:
            is_empty = (
                not data
                or (not data.get("blocks") and not data.get("edges"))
            )
        else:
            is_empty = not data
        return FetchResult(
            status="empty" if is_empty else "ok",
            data=data,
        )
    except requests.Timeout:
        return FetchResult(
            status="fetch_error",
            data={"blocks": [], "edges": []} if is_cfg else ([] if not is_bundle else {}),
            error="Request timed out",
        )
    except Exception as exc:
        return FetchResult(
            status="fetch_error",
            data={"blocks": [], "edges": []} if is_cfg else ([] if not is_bundle else {}),
            error=str(exc),
        )


def _fetch_error_result(
    subj: BenchmarkSubject,
    stage: str,
    reference: str,
    candidate: str,
    ref_fetch: FetchResult,
    cand_fetch: FetchResult,
) -> BenchmarkResult | None:
    """Return a BenchmarkResult for invalid fetches, or None when both are ok."""
    if ref_fetch.status == "ok" and cand_fetch.status == "ok":
        return None

    # Both empty — definitively invalid, never a match.
    if ref_fetch.status == "empty" and cand_fetch.status == "empty":
        return BenchmarkResult(
            subject=subj,
            stage=stage,
            status="both_empty_invalid",
            reference=reference,
            candidate=candidate,
            error="Both reference and candidate returned empty data — not a valid match",
        )
    if ref_fetch.status != "ok":
        return BenchmarkResult(
            subject=subj,
            stage=stage,
            status="reference_empty" if ref_fetch.status == "empty" else "fetch_error",
            reference=reference,
            candidate=candidate,
            error=f"Reference fetch failed: {ref_fetch.error or ref_fetch.status}",
        )
    # candidate not ok
    return BenchmarkResult(
        subject=subj,
        stage=stage,
        status="candidate_empty" if cand_fetch.status == "empty" else "fetch_error",
        reference=reference,
        candidate=candidate,
        error=f"Candidate fetch failed: {cand_fetch.error or cand_fetch.status}",
    )

def run_parity_benchmarks(
    corpus: str,
    limit: int | None = None,
    decompilers: list[str] | None = None,
    request_timeout: float = 60.0,
) -> list[BenchmarkResult]:
    # Load subjects from corpus manifests (shared subject loader with arch inference)
    from benchmark.common.subjects import load_subjects

    subjects = []
    for subj in load_subjects(corpus):
        # Store corpus-relative binary for adapter URLs (corpus/<split>/binaries/...)
        parts = Path(subj.binary).resolve().parts
        if "corpus" in parts:
            idx = parts.index("corpus")
            rel = "/".join(parts[idx:])
        else:
            rel = f"corpus/{corpus}/{Path(subj.binary).name}"
        subjects.append({
            "name": subj.function,
            "binary": rel,
            "addr": subj.addr,
            "arch": subj.arch,
            "compiler": subj.compiler,
            "opt": subj.opt,
        })

    if limit is not None:
        subjects = subjects[:limit]

    print(f"Loaded {len(subjects)} subjects for parity testing.")

    results: list[BenchmarkResult] = []

    decompilers = decompilers or list(PORT_MAPPING.keys())
    if "ghidra" not in decompilers:
        decompilers = ["ghidra", *decompilers]

    # Group by binary so Ghidra does ONE multi_bundle headless per PE, not per function.
    from collections import defaultdict

    by_binary: dict[str, list[dict]] = defaultdict(list)
    for sub in subjects:
        by_binary[sub["binary"]].append(sub)

    candidates = [d for d in decompilers if d != "ghidra"]
    # Decompilers known to implement /parity_multi_bundle (batch + parallel CLI).
    # Others fall back to per-address endpoints.
    bundle_capable = {"fission"}
    print(
        f"Grouped into {len(by_binary)} unique binaries "
        f"(Ghidra multi-bundle + parallel candidate batch for "
        f"{sorted(bundle_capable & set(candidates)) or 'none'}; "
        f"binary_workers={BINARY_WORKERS})."
    )

    from concurrent.futures import ThreadPoolExecutor, as_completed

    def _prefetch_one_binary(
        binary: str, group: list[dict]
    ) -> tuple[
        dict[str, tuple[FetchResult, FetchResult, FetchResult, FetchResult]],
        dict[str, dict[str, tuple[FetchResult, FetchResult, FetchResult, FetchResult]]],
        dict[str, FetchResult],
        FetchResult,
    ]:
        arch = group[0].get("arch") or ""
        addrs = [s["addr"] for s in group]
        batch_cands = [c for c in candidates if c in bundle_capable]
        ghidra_map: dict[
            str, tuple[FetchResult, FetchResult, FetchResult, FetchResult]
        ] = {}
        cand_maps: dict[
            str, dict[str, tuple[FetchResult, FetchResult, FetchResult, FetchResult]]
        ] = {}
        cand_functions: dict[str, FetchResult] = {}
        ghidra_functions = FetchResult(status="empty", data=[])

        jobs: dict = {}
        with ThreadPoolExecutor(
            max_workers=3 + len(batch_cands) + len(candidates)
        ) as pool:
            jobs[
                pool.submit(
                    _prefetch_ghidra_multi_bundle,
                    binary,
                    addrs,
                    arch,
                    corpus=corpus,
                    timeout=request_timeout,
                )
            ] = ("ghidra_map", None)
            jobs[
                pool.submit(
                    fetch_parity_data,
                    "ghidra",
                    "functions",
                    binary,
                    corpus=corpus,
                    timeout=request_timeout,
                )
            ] = ("ghidra_functions", None)
            for cand in batch_cands:
                jobs[
                    pool.submit(
                        _prefetch_candidate_multi_bundle,
                        cand,
                        binary,
                        addrs,
                        arch,
                        corpus=corpus,
                        timeout=request_timeout,
                    )
                ] = ("cand_map", cand)
            for decompiler in candidates:
                jobs[
                    pool.submit(
                        fetch_parity_data,
                        decompiler,
                        "functions",
                        binary,
                        corpus=corpus,
                        timeout=request_timeout,
                    )
                ] = ("functions", decompiler)

            for fut in as_completed(jobs):
                kind, name = jobs[fut]
                try:
                    result = fut.result()
                except Exception as exc:
                    print(
                        f"    warn: prefetch {os.path.basename(binary)} "
                        f"{kind}/{name} failed: {exc}"
                    )
                    result = (
                        {}
                        if kind not in {"functions", "ghidra_functions"}
                        else FetchResult(status="fetch_error", data=[], error=str(exc))
                    )
                if kind == "ghidra_map":
                    ghidra_map = result  # type: ignore[assignment]
                elif kind == "ghidra_functions":
                    ghidra_functions = result  # type: ignore[assignment]
                elif kind == "cand_map" and name is not None:
                    cand_maps[name] = result  # type: ignore[assignment]
                elif kind == "functions" and name is not None:
                    cand_functions[name] = result  # type: ignore[assignment]
        return ghidra_map, cand_maps, cand_functions, ghidra_functions

    binary_items = list(by_binary.items())
    for wave_i in range(0, len(binary_items), BINARY_WORKERS):
        wave = binary_items[wave_i : wave_i + BINARY_WORKERS]
        names = ", ".join(os.path.basename(b) for b, _ in wave)
        print(
            f"Wave {wave_i // BINARY_WORKERS + 1}/"
            f"{(len(binary_items) + BINARY_WORKERS - 1) // BINARY_WORKERS}: "
            f"{len(wave)} PE(s) concurrent multi_bundle — {names}"
        )

        # Prefetch entire wave in parallel (Ghidra headless_workers + Fission).
        wave_prefetch: dict[str, tuple] = {}
        with ThreadPoolExecutor(max_workers=len(wave)) as pool:
            futs = {
                pool.submit(_prefetch_one_binary, binary, group): (binary, group)
                for binary, group in wave
            }
            for fut in as_completed(futs):
                binary, group = futs[fut]
                try:
                    wave_prefetch[binary] = fut.result()
                except Exception as exc:
                    print(f"    warn: wave prefetch {os.path.basename(binary)}: {exc}")
                    wave_prefetch[binary] = (
                        {},
                        {},
                        {},
                        FetchResult(status="fetch_error", data=[], error=str(exc)),
                    )

        for binary, group in wave:
            ghidra_map, cand_maps, cand_functions, ghidra_functions = wave_prefetch.get(
                binary,
                ({}, {}, {}, FetchResult(status="empty", data=[])),
            )
            print(
                f"Binary {os.path.basename(binary)}: {len(group)} functions "
                f"→ compare (prefetch ready)"
            )

            # 1. Function discovery once per PE: full Ghidra inventory vs candidate.
            inv_subj = BenchmarkSubject(
                binary=group[0]["binary"],
                function="(inventory)",
                addr="0x0",
                arch=group[0].get("arch") or "",
                compiler=group[0].get("compiler") or "",
                opt=group[0].get("opt") or "",
            )
            manifest_addrs = {
                _normalize_addr_key(str(s.get("addr") or "")) for s in group
            }
            manifest_addrs.discard("0x0")
            for decompiler, funcs_result in cand_functions.items():
                try:
                    if ghidra_functions.status != "ok":
                        results.append(
                            BenchmarkResult(
                                subject=inv_subj,
                                stage="function_discovery",
                                status="fetch_error"
                                if ghidra_functions.status == "fetch_error"
                                else "reference_empty",
                                reference="ghidra",
                                candidate=decompiler,
                                error=ghidra_functions.error
                                or f"ghidra functions {ghidra_functions.status}",
                            )
                        )
                        continue
                    if funcs_result.status != "ok":
                        results.append(
                            BenchmarkResult(
                                subject=inv_subj,
                                stage="function_discovery",
                                status="fetch_error"
                                if funcs_result.status == "fetch_error"
                                else "candidate_empty",
                                reference="ghidra",
                                candidate=decompiler,
                                error=funcs_result.error
                                or f"functions inventory {funcs_result.status}",
                            )
                        )
                        continue
                    ref_list = (
                        ghidra_functions.data
                        if isinstance(ghidra_functions.data, list)
                        else []
                    )
                    cand_list = (
                        funcs_result.data if isinstance(funcs_result.data, list) else []
                    )
                    row = compare_functions(
                        inv_subj, "ghidra", decompiler, ref_list, cand_list
                    )
                    # Extra reliability metrics: corpus-manifest subject coverage.
                    cand_addrs = function_addresses(cand_list)
                    metrics = dict(row.metrics or {})
                    metrics["scored_as"] = "ghidra_inventory"
                    metrics["manifest_subject_count"] = len(manifest_addrs)
                    metrics["manifest_found_count"] = len(manifest_addrs & cand_addrs)
                    metrics["manifest_recall"] = (
                        1.0
                        if not manifest_addrs
                        else round(
                            len(manifest_addrs & cand_addrs) / len(manifest_addrs), 4
                        )
                    )
                    results.append(
                        BenchmarkResult(
                            subject=row.subject,
                            stage=row.stage,
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
                    print(
                        f"  function_discovery ghidra→{decompiler}: "
                        f"{row.status} ({row.mismatch_kind or 'ok'}) "
                        f"ref={metrics.get('expected_function_count')} "
                        f"cand={metrics.get('actual_function_count')} "
                        f"manifest_recall={metrics.get('manifest_recall')}"
                    )
                except Exception as e:
                    results.append(
                        BenchmarkResult(
                            subject=inv_subj,
                            stage="function_discovery",
                            status="error",
                            reference="ghidra",
                            candidate=decompiler,
                            error=str(e),
                        )
                    )

            for sub in group:
                subj = BenchmarkSubject(
                    binary=sub["binary"],
                    function=sub["name"],
                    addr=sub["addr"],
                    arch=sub["arch"],
                    compiler=sub["compiler"],
                    opt=sub["opt"],
                )
                print(f"  Processing {subj.function} @ {subj.addr}...")

                nk = _normalize_addr_key(subj.addr)
                ref_tuple = ghidra_map.get(nk)
                if ref_tuple is None:
                    # try raw key
                    ref_tuple = ghidra_map.get(subj.addr) or ghidra_map.get(subj.addr.lower())
                if ref_tuple is None:
                    ref_asm_fetch, ref_dec_fetch, ref_pcode_fetch, ref_cfg_fetch = (
                        _fetch_ghidra_reference_bundle(
                            subj.binary,
                            subj.addr,
                            subj.arch,
                            corpus=corpus,
                            timeout=request_timeout,
                        )
                    )
                else:
                    ref_asm_fetch, ref_dec_fetch, ref_pcode_fetch, ref_cfg_fetch = ref_tuple

                for cand in candidates:
                    asm_res = dec_res = pcode_res = cfg_res = None
                    cand_tuple = None
                    cmap = cand_maps.get(cand)
                    if cmap:
                        cand_tuple = cmap.get(nk) or cmap.get(subj.addr) or cmap.get(
                            subj.addr.lower()
                        )
                    if cand_tuple is not None:
                        (
                            cand_asm_fetch,
                            cand_dec_fetch,
                            cand_pcode_fetch,
                            cand_cfg_fetch,
                        ) = cand_tuple
                    else:
                        (
                            cand_asm_fetch,
                            cand_dec_fetch,
                            cand_pcode_fetch,
                            cand_cfg_fetch,
                        ) = _fetch_candidate_bundle(
                            cand,
                            subj.binary,
                            subj.addr,
                            subj.arch,
                            corpus=corpus,
                            timeout=request_timeout,
                        )

                    invalid = _fetch_error_result(
                        subj, "assembly_parity", "ghidra", cand, ref_asm_fetch, cand_asm_fetch
                    )
                    if invalid is not None:
                        asm_res = invalid
                        results.append(asm_res)
                    else:
                        try:
                            asm_res = compare_assembly(
                                subj, "ghidra", cand, ref_asm_fetch.data, cand_asm_fetch.data
                            )
                            results.append(asm_res)
                        except Exception as e:
                            asm_res = BenchmarkResult(
                                subject=subj,
                                stage="assembly_parity",
                                status="error",
                                reference="ghidra",
                                candidate=cand,
                                error=str(e),
                            )
                            results.append(asm_res)

                    invalid = _fetch_error_result(
                        subj, "decode_parity", "ghidra", cand, ref_dec_fetch, cand_dec_fetch
                    )
                    if invalid is not None:
                        dec_res = invalid
                        results.append(dec_res)
                    else:
                        try:
                            dec_res = compare_decode(
                                subj, "ghidra", cand, ref_dec_fetch.data, cand_dec_fetch.data
                            )
                            results.append(dec_res)
                        except Exception as e:
                            dec_res = BenchmarkResult(
                                subject=subj,
                                stage="decode_parity",
                                status="error",
                                reference="ghidra",
                                candidate=cand,
                                error=str(e),
                            )
                            results.append(dec_res)

                    invalid = _fetch_error_result(
                        subj, "pcode_parity", "ghidra", cand, ref_pcode_fetch, cand_pcode_fetch
                    )
                    if invalid is not None:
                        pcode_res = invalid
                        results.append(pcode_res)
                    else:
                        try:
                            pcode_res = compare_pcode(
                                subj, "ghidra", cand, ref_pcode_fetch.data, cand_pcode_fetch.data
                            )
                            results.append(pcode_res)
                        except Exception as e:
                            pcode_res = BenchmarkResult(
                                subject=subj,
                                stage="pcode_parity",
                                status="error",
                                reference="ghidra",
                                candidate=cand,
                                error=str(e),
                            )
                            results.append(pcode_res)

                    invalid = _fetch_error_result(
                        subj, "cfg_parity", "ghidra", cand, ref_cfg_fetch, cand_cfg_fetch
                    )
                    if invalid is not None:
                        cfg_res = invalid
                        results.append(cfg_res)
                    else:
                        try:
                            cfg_res = compare_cfg(
                                subj, "ghidra", cand, ref_cfg_fetch.data, cand_cfg_fetch.data
                            )
                            results.append(cfg_res)
                        except Exception as e:
                            cfg_res = BenchmarkResult(
                                subject=subj,
                                stage="cfg_parity",
                                status="error",
                                reference="ghidra",
                                candidate=cand,
                                error=str(e),
                            )
                            results.append(cfg_res)

                    has_mismatch = any(
                        r and r.status == "mismatch"
                        for r in (asm_res, dec_res, pcode_res, cfg_res)
                    )
                    if has_mismatch:
                        mismatch_info_list = []
                        if asm_res and asm_res.status == "mismatch":
                            mismatch_info_list.append(f"assembly: {asm_res.mismatch_kind}")
                        if dec_res and dec_res.status == "mismatch":
                            mismatch_info_list.append(f"decode: {dec_res.mismatch_kind}")
                        if pcode_res and pcode_res.status == "mismatch":
                            mismatch_info_list.append(f"pcode: {pcode_res.mismatch_kind}")
                        if cfg_res and cfg_res.status == "mismatch":
                            mismatch_info_list.append(f"cfg: {cfg_res.mismatch_kind}")
                        try:
                            from runner.graph_utils import generate_mermaid
                        except ModuleNotFoundError:
                            from graph_utils import generate_mermaid
                        payload = {
                            "reference_cfg": ref_cfg_fetch.data,
                            "candidate_cfg": cand_cfg_fetch.data,
                            "reference_disasm": ref_asm_fetch.data,
                            "candidate_disasm": cand_asm_fetch.data,
                            "mismatch_info": "; ".join(mismatch_info_list),
                            "reference_mermaid": generate_mermaid(
                                ref_cfg_fetch.data, cand_cfg_fetch.data
                            ),
                            "candidate_mermaid": generate_mermaid(
                                cand_cfg_fetch.data, ref_cfg_fetch.data
                            ),
                        }
                        binary_name = os.path.basename(subj.binary)
                        PARITY_DIFFS_DIR = Path(
                            os.environ.get("PARITY_DIFFS_DIR", "results/parity_diffs")
                        )
                        diff_dir = PARITY_DIFFS_DIR / binary_name / subj.function
                        diff_dir.mkdir(parents=True, exist_ok=True)
                        diff_file = diff_dir / f"{cand}.json"
                        with open(diff_file, "w", encoding="utf-8") as f:
                            json.dump(payload, f, indent=2)
                        print(f"    [PARITY DIFF] {diff_file}")

                # IR invariants (Fission) — structural CFG checks + disasm consistency
                try:
                    from benchmark.common.compare_guards import cfg_invariant_violations

                    fission_cfg_fetch: FetchResult | None = None
                    fission_asm_fetch: FetchResult | None = None
                    fmap = cand_maps.get("fission")
                    if fmap:
                        ft = fmap.get(nk) or fmap.get(subj.addr) or fmap.get(
                            subj.addr.lower()
                        )
                        if ft is not None:
                            fission_asm_fetch = ft[0]
                            fission_cfg_fetch = ft[3]
                    if fission_cfg_fetch is None and "fission" in candidates:
                        fission_cfg_fetch = fetch_parity_data(
                            "fission",
                            "cfg",
                            subj.binary,
                            subj.addr,
                            subj.arch,
                            corpus=corpus,
                            timeout=request_timeout,
                        )
                    if fission_cfg_fetch is None:
                        fission_cfg_fetch = FetchResult(
                            status="empty", data={"blocks": [], "edges": []}
                        )
                    violations: list = []
                    if fission_cfg_fetch.status == "fetch_error":
                        violations.append(
                            {
                                "kind": "cfg_fetch_error",
                                "detail": fission_cfg_fetch.error or "fetch_error",
                            }
                        )
                    else:
                        violations.extend(
                            cfg_invariant_violations(fission_cfg_fetch.data)
                        )
                        if (
                            fission_asm_fetch is not None
                            and fission_asm_fetch.is_usable()
                            and isinstance(fission_asm_fetch.data, list)
                            and len(fission_asm_fetch.data) > 0
                            and any(
                                v.get("kind") == "empty_cfg_blocks" for v in violations
                            )
                        ):
                            violations.append(
                                {
                                    "kind": "empty_cfg_with_disasm",
                                    "disasm_count": len(fission_asm_fetch.data),
                                }
                            )
                    cfg_data = (
                        fission_cfg_fetch.data
                        if isinstance(fission_cfg_fetch.data, dict)
                        else {}
                    )
                    results.append(
                        compare_invariants(
                            subj,
                            "fission",
                            {
                                "violations": violations,
                                "metrics": {
                                    "block_count": len(cfg_data.get("blocks") or []),
                                    "edge_count": len(cfg_data.get("edges") or []),
                                },
                            },
                        )
                    )
                except Exception as e:
                    results.append(
                        BenchmarkResult(
                            subject=subj,
                            stage="ir_invariants",
                            status="error",
                            reference="none",
                            candidate="fission",
                            error=str(e),
                        )
                    )

    return results

def main():
    parser = argparse.ArgumentParser(description="Unified Parity Runner")
    parser.add_argument("--corpus", default="dev", help="Corpus split (dev/holdout)")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of subjects to run")
    parser.add_argument(
        "--decompilers",
        default=",".join(PORT_MAPPING.keys()),
        help="Comma-separated decompilers to include; ghidra is always included as reference",
    )
    parser.add_argument(
        "--request-timeout",
        type=float,
        default=float(os.environ.get("PARITY_REQUEST_TIMEOUT", "60")),
        help="HTTP timeout per parity endpoint request",
    )
    parser.add_argument(
        "--keep-payloads",
        action="store_true",
        help="Include full expected/actual payloads in JSONL (large; default omits them)",
    )
    args = parser.parse_args()

    decompilers = [name.strip() for name in args.decompilers.split(",") if name.strip()]
    # Ensure local fission port matches running compose (8007 overlay common).
    if "FISSION_HOST_PORT" not in os.environ:
        for probe in (8000, 8007):
            try:
                r = requests.get(f"http://localhost:{probe}/health", timeout=1.5)
                if r.ok and r.json().get("decompiler") == "fission":
                    PORT_MAPPING["fission"] = probe
                    break
            except Exception:
                continue

    results = run_parity_benchmarks(args.corpus, args.limit, decompilers, args.request_timeout)

    # Save results to respective output files
    output_dir = Path("results")
    output_dir.mkdir(exist_ok=True)

    stages = [
        "assembly_parity",
        "decode_parity",
        "pcode_parity",
        "cfg_parity",
        "function_discovery",
        "ir_invariants",
    ]

    def to_row(r: Any) -> dict:
        if not hasattr(r, "stage"):
            return r
        row = {
            "subject": {
                "binary": r.subject.binary,
                "function": r.subject.function,
                "addr": r.subject.addr,
                "arch": r.subject.arch,
                "compiler": r.subject.compiler,
                "opt": r.subject.opt,
            },
            "stage": r.stage,
            "status": r.status,
            "reference": r.reference,
            "candidate": r.candidate,
            "mismatch_kind": getattr(r, "mismatch_kind", None),
            "error": getattr(r, "error", None),
            "metrics": getattr(r, "metrics", None),
        }
        if args.keep_payloads:
            row["expected"] = getattr(r, "expected", None)
            row["actual"] = getattr(r, "actual", None)
        return row

    rows = [to_row(r) for r in results]

    for stage in stages:
        stage_rows = [r for r in rows if r["stage"] == stage]
        stage_dir = output_dir / stage
        stage_dir.mkdir(exist_ok=True)
        with open(stage_dir / "latest.jsonl", "w", encoding="utf-8") as f:
            for r in stage_rows:
                f.write(json.dumps(r) + "\n")
        print(f"Wrote {len(stage_rows)} rows to {stage_dir}/latest.jsonl")

    # Aggregate telemetry (+ dashboard static copy)
    summary = aggregate_rows(rows)
    telemetry_dir = output_dir / "telemetry"
    telemetry_dir.mkdir(exist_ok=True)
    telemetry_path = telemetry_dir / "latest.json"
    telemetry_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    dashboard_copy = Path("public/parity-telemetry.json")
    try:
        dashboard_copy.parent.mkdir(parents=True, exist_ok=True)
        dashboard_copy.write_text(telemetry_path.read_text(encoding="utf-8"), encoding="utf-8")
    except OSError as exc:
        print(f"warning: could not write {dashboard_copy}: {exc}")

    print("\n" + "=" * 40)
    print("        PARITY BENCHMARK SUMMARY")
    print("=" * 40)
    print(f"Total Rows: {summary.get('total_rows')}")
    rel = summary.get("reliability") or {}
    if rel:
        print("\nReliability (trustworthiness of rates):")
        print(
            f"  usable_coverage={rel.get('usable_coverage')} "
            f"match_rate_attempted={rel.get('match_rate_attempted')} "
            f"fetch_error_rate={rel.get('fetch_error_rate')} "
            f"skipped_rate={rel.get('skipped_rate')}"
        )
    print("\nBy Stage:")
    for k, v in summary.get("by_stage", {}).items():
        print(f"  {k}: {v}")
    print("\nBy Status:")
    for k, v in summary.get("by_status", {}).items():
        print(f"  {k}: {v}")
    print("\nStage rates (comparable | attempted | coverage):")
    for stage, detail in (summary.get("stages") or {}).items():
        print(
            f"  {stage}: match_rate={detail.get('match_rate')} "
            f"attempted={detail.get('match_rate_attempted')} "
            f"coverage={detail.get('usable_coverage')} "
            f"(match={detail.get('match')} mismatch={detail.get('mismatch')} "
            f"skip={detail.get('skipped')} fetch_err={detail.get('fetch_error')})"
        )
    print("\nBy Mismatch Kind:")
    for k, v in summary.get("by_mismatch_kind", {}).items():
        print(f"  {k}: {v}")
    print("=" * 40)


if __name__ == "__main__":
    main()
