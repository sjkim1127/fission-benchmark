"""Unified Parity Runner for Fission Benchmark infrastructure.

Coordinates assembly, decode, p-code, CFG, function discovery, and invariant parity checks.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import requests

from benchmark.assembly_parity.run import compare_assembly
from benchmark.cfg_parity.run import compare_cfg
from benchmark.decode_parity.run import compare_decode
from benchmark.function_discovery.run import compare_functions
from benchmark.ir_invariants.run import compare_invariants
from benchmark.pcode_parity.run import compare_pcode
from benchmark.telemetry.aggregate import aggregate_rows
from benchmark.common.schema import BenchmarkResult, BenchmarkSubject

# Port mapping of decompiler containers
PORT_MAPPING = {
    "fission": int(os.environ.get("FISSION_HOST_PORT", "8000")),
    "reko": int(os.environ.get("REKO_HOST_PORT", "8008")),
    "ghidra": int(os.environ.get("GHIDRA_HOST_PORT", "8001")),
    "boomerang": int(os.environ.get("BOOMERANG_HOST_PORT", "8002")),
    "radare2": int(os.environ.get("RADARE2_HOST_PORT", "8003")),
    "angr": int(os.environ.get("ANGR_HOST_PORT", "8004")),
    "snowman": int(os.environ.get("SNOWMAN_HOST_PORT", "8005")),
    "revng": int(os.environ.get("REVNG_HOST_PORT", "8006")),
}

def fetch_data(
    decompiler: str,
    endpoint: str,
    binary: str,
    addr: str = "",
    arch: str = "",
    corpus: str = "dev",
    timeout: float = 5.0,
):
    port = PORT_MAPPING.get(decompiler)
    if not port:
        return [] if endpoint != "cfg" else {"blocks": [], "edges": []}
    
    if not binary.startswith("corpus/"):
        binary = f"corpus/{corpus}/{binary}"
    url = f"http://localhost:{port}/{endpoint}?binary={binary}"
    if addr:
        url += f"&addr={addr}"
    if arch:
        url += f"&arch={arch}"
        
    try:
        resp = requests.get(url, timeout=timeout)
        if resp.status_code == 200:
            return resp.json()
    except Exception:
        pass
    
    return [] if endpoint != "cfg" else {"blocks": [], "edges": []}

def run_parity_benchmarks(
    corpus: str,
    limit: int | None = None,
    decompilers: list[str] | None = None,
    request_timeout: float = 5.0,
) -> list[BenchmarkResult]:
    # Load subjects from corpus manifests
    manifests_dir = Path(f"corpus/{corpus}/manifests")
    subjects = []
    
    # Iterate through all manifest files
    for manifest_path in sorted(manifests_dir.glob("*.json")):
        try:
            with open(manifest_path) as f:
                data = json.load(f)
                for entry in data.get("functions", []):
                    name = entry.get("name")
                    for var in entry.get("compiler_variants", []):
                        subjects.append({
                            "name": name,
                            "binary": var.get("binary"),
                            "addr": var.get("addr"),
                            "arch": var.get("arch", "x86_64"),
                            "compiler": var.get("compiler"),
                            "opt": var.get("opt"),
                        })
        except Exception as e:
            print(f"Error loading manifest {manifest_path}: {e}")

    if limit is not None:
        subjects = subjects[:limit]

    print(f"Loaded {len(subjects)} subjects for parity testing.")
    
    results: list[BenchmarkResult] = []
    
    decompilers = decompilers or list(PORT_MAPPING.keys())
    if "ghidra" not in decompilers:
        decompilers = ["ghidra", *decompilers]
    
    for sub in subjects:
        subj = BenchmarkSubject(
            binary=sub["binary"],
            function=sub["name"],
            addr=sub["addr"],
            arch=sub["arch"],
            compiler=sub["compiler"],
            opt=sub["opt"]
        )
        
        print(f"Processing {subj.function} in {subj.binary} at {subj.addr}...")
        
        # 1. Function Discovery (compared vs expected function in manifest)
        # We query /functions for each decompiler and check if it discovered our function
        for decompiler in decompilers:
            if decompiler == "ghidra":
                continue # ghidra is usually reference
            try:
                funcs = fetch_data(decompiler, "functions", subj.binary, corpus=corpus, timeout=request_timeout)
                expected = [{"address": subj.addr, "name": subj.function}]
                actual = [{"address": f.get("address"), "name": f.get("name")} for f in funcs if f.get("address") == subj.addr]
                res = compare_functions(subj, "manifest", decompiler, expected, actual)
                results.append(res)
            except Exception as e:
                results.append(BenchmarkResult(subject=subj, stage="function_discovery", status="error", reference="manifest", candidate=decompiler, error=str(e)))

        # Fetch reference (ghidra) data once
        ref_asm = []
        try:
            ref_asm = fetch_data("ghidra", "disasm", subj.binary, subj.addr, subj.arch, corpus=corpus, timeout=request_timeout)
        except Exception:
            pass

        ref_dec = []
        try:
            ref_dec = fetch_data("ghidra", "decode", subj.binary, subj.addr, subj.arch, corpus=corpus, timeout=request_timeout)
        except Exception:
            pass

        ref_pcode = []
        try:
            ref_pcode = fetch_data("ghidra", "pcode", subj.binary, subj.addr, subj.arch, corpus=corpus, timeout=request_timeout)
        except Exception:
            pass

        ref_cfg = {"blocks": [], "edges": []}
        try:
            ref_cfg = fetch_data("ghidra", "cfg", subj.binary, subj.addr, subj.arch, corpus=corpus, timeout=request_timeout)
        except Exception:
            pass

        # Check other stages and generate diff files if mismatches occur
        for cand in decompilers:
            if cand == "ghidra":
                continue
            
            cand_asm = []
            cand_dec = []
            cand_pcode = []
            cand_cfg = {"blocks": [], "edges": []}

            asm_res = None
            dec_res = None
            pcode_res = None
            cfg_res = None

            # 2. Assembly Parity
            try:
                cand_asm = fetch_data(cand, "disasm", subj.binary, subj.addr, subj.arch, corpus=corpus, timeout=request_timeout)
                asm_res = compare_assembly(subj, "ghidra", cand, ref_asm, cand_asm)
                results.append(asm_res)
            except Exception as e:
                asm_res = BenchmarkResult(subject=subj, stage="assembly_parity", status="error", reference="ghidra", candidate=cand, error=str(e))
                results.append(asm_res)

            # 3. Decode Parity
            try:
                cand_dec = fetch_data(cand, "decode", subj.binary, subj.addr, subj.arch, corpus=corpus, timeout=request_timeout)
                dec_res = compare_decode(subj, "ghidra", cand, ref_dec, cand_dec)
                results.append(dec_res)
            except Exception as e:
                dec_res = BenchmarkResult(subject=subj, stage="decode_parity", status="error", reference="ghidra", candidate=cand, error=str(e))
                results.append(dec_res)

            # 4. P-code Parity
            try:
                cand_pcode = fetch_data(cand, "pcode", subj.binary, subj.addr, subj.arch, corpus=corpus, timeout=request_timeout)
                pcode_res = compare_pcode(subj, "ghidra", cand, ref_pcode, cand_pcode)
                results.append(pcode_res)
            except Exception as e:
                pcode_res = BenchmarkResult(subject=subj, stage="pcode_parity", status="error", reference="ghidra", candidate=cand, error=str(e))
                results.append(pcode_res)

            # 5. CFG Parity
            try:
                cand_cfg = fetch_data(cand, "cfg", subj.binary, subj.addr, subj.arch, corpus=corpus, timeout=request_timeout)
                cfg_res = compare_cfg(subj, "ghidra", cand, ref_cfg, cand_cfg)
                results.append(cfg_res)
            except Exception as e:
                cfg_res = BenchmarkResult(subject=subj, stage="cfg_parity", status="error", reference="ghidra", candidate=cand, error=str(e))
                results.append(cfg_res)

            # Detect mismatch
            has_mismatch = (
                (asm_res and asm_res.status == "mismatch") or
                (dec_res and dec_res.status == "mismatch") or
                (pcode_res and pcode_res.status == "mismatch") or
                (cfg_res and cfg_res.status == "mismatch")
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
                
                mismatch_info = "; ".join(mismatch_info_list)

                # Generate Mermaids
                try:
                    from runner.graph_utils import generate_mermaid
                except ModuleNotFoundError:
                    from graph_utils import generate_mermaid
                ref_mermaid = generate_mermaid(ref_cfg, cand_cfg)
                cand_mermaid = generate_mermaid(cand_cfg, ref_cfg)

                payload = {
                    "reference_cfg": ref_cfg,
                    "candidate_cfg": cand_cfg,
                    "reference_disasm": ref_asm,
                    "candidate_disasm": cand_asm,
                    "mismatch_info": mismatch_info,
                    "reference_mermaid": ref_mermaid,
                    "candidate_mermaid": cand_mermaid,
                }

                # Save static JSON files
                binary_name = os.path.basename(subj.binary)
                PARITY_DIFFS_DIR = Path(os.environ.get("PARITY_DIFFS_DIR", "results/parity_diffs"))
                diff_dir = PARITY_DIFFS_DIR / binary_name / subj.function
                diff_dir.mkdir(parents=True, exist_ok=True)
                diff_file = diff_dir / f"{cand}.json"
                with open(diff_file, "w") as f:
                    json.dump(payload, f, indent=2)
                print(f"  [PARITY DIFF] Mismatch detected. Saved static diff dump to: {diff_file}")

        # 6. IR Invariants (Only checked for Fission)
        try:
            # For invariants, we check if fission had any major normalization errors or empty output
            violations = []
            fission_cfg = fetch_data("fission", "cfg", subj.binary, subj.addr, subj.arch, corpus=corpus, timeout=request_timeout)
            if not fission_cfg or not fission_cfg.get("blocks"):
                violations.append({"kind": "empty_cfg_blocks"})
            
            res = compare_invariants(subj, "fission", {
                "violations": violations,
                "metrics": {"block_count": len(fission_cfg.get("blocks", [])) if fission_cfg else 0}
            })
            results.append(res)
        except Exception as e:
            results.append(BenchmarkResult(subject=subj, stage="ir_invariants", status="error", reference="none", candidate="fission", error=str(e)))
            
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
        default=5.0,
        help="HTTP timeout per parity endpoint request",
    )
    args = parser.parse_args()
    
    decompilers = [name.strip() for name in args.decompilers.split(",") if name.strip()]
    results = run_parity_benchmarks(args.corpus, args.limit, decompilers, args.request_timeout)
    
    # Save results to respective output files
    output_dir = Path("results")
    output_dir.mkdir(exist_ok=True)
    
    stages = ["assembly_parity", "decode_parity", "pcode_parity", "cfg_parity", "function_discovery", "ir_invariants"]
    
    # Convert BenchmarkResult dataclasses to dicts for output
    rows = []
    for r in results:
        if hasattr(r, "stage"):
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
            }
        else:
            row = r
        rows.append(row)
        
    for stage in stages:
        stage_rows = [r for r in rows if r["stage"] == stage]
        stage_dir = output_dir / stage
        stage_dir.mkdir(exist_ok=True)
        with open(stage_dir / "latest.jsonl", "w") as f:
            for r in stage_rows:
                f.write(json.dumps(r) + "\n")
        print(f"Wrote {len(stage_rows)} rows to {stage_dir}/latest.jsonl")
        
    # Aggregate telemetry
    summary = aggregate_rows(rows)
    telemetry_dir = output_dir / "telemetry"
    telemetry_dir.mkdir(exist_ok=True)
    
    with open(telemetry_dir / "latest.json", "w") as f:
        json.dump(summary, f, indent=2)
        
    print("\n" + "="*40)
    print("        PARITY BENCHMARK SUMMARY")
    print("="*40)
    print(f"Total Rows: {summary.get('total_rows')}")
    print("\nBy Stage:")
    for k, v in summary.get("by_stage", {}).items():
        print(f"  {k}: {v}")
    print("\nBy Status:")
    for k, v in summary.get("by_status", {}).items():
        print(f"  {k}: {v}")
    print("\nBy Mismatch Kind:")
    for k, v in summary.get("by_mismatch_kind", {}).items():
        print(f"  {k}: {v}")
    print("="*40)

if __name__ == "__main__":
    main()
