"""Fission decompiler and parity diagnostic API server."""
import base64
import json
import os
import subprocess
import tempfile
import time
from pathlib import Path
from typing import Dict, List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="fission-decompiler", version="1.0")
FISSION_BIN = Path("/usr/local/bin/fission_cli")
SLEIGH_SPEC_DIR = os.environ.get("FISSION_SLEIGH_SPEC_DIR", "/sleigh-specs")
RESOURCE_ROOT = os.environ.get("FISSION_RESOURCE_ROOT", "/opt/fission-utils/utils")
GHIDRA_DATA_DIR = os.environ.get("FISSION_GHIDRA_DATA_DIR", "/opt/fission-utils/utils/ghidra-data")
DECOMP_TIMEOUT_MS = os.environ.get("FISSION_DECOMP_TIMEOUT_MS", "30000")
RELEASE_VERSION_FILE = Path("/opt/fission-release-version")
SOURCE_FILE = Path("/opt/fission-source")
GIT_SHA_FILE = Path("/opt/fission-git-sha")

# ---------------------------------------------------------------------------
# Capability probe — checked once per process lifetime and cached.
# We inspect `fission_cli decomp --help` to discover supported flags so that
# older CLI releases that do not have `--layer` still work correctly.
# ---------------------------------------------------------------------------
_CAPABILITY_CACHE: Dict[str, bool] = {}
_CAPABILITY_PROBED: bool = False


def _probe_capabilities() -> None:
    """Populate _CAPABILITY_CACHE from `fission_cli decomp --help` output."""
    global _CAPABILITY_PROBED
    if _CAPABILITY_PROBED:
        return
    _CAPABILITY_PROBED = True
    try:
        r = subprocess.run(
            [str(FISSION_BIN), "decomp", "--help"],
            capture_output=True,
            text=True,
            timeout=10,
        )
        help_text = r.stdout + r.stderr
        _CAPABILITY_CACHE["--layer"] = "--layer" in help_text
        _CAPABILITY_CACHE["--benchmark"] = "--benchmark" in help_text
        _CAPABILITY_CACHE["--timeout-ms"] = "--timeout-ms" in help_text
    except Exception:
        # If help fails, assume minimal capability set (no optional flags).
        _CAPABILITY_CACHE["--layer"] = False
        _CAPABILITY_CACHE["--benchmark"] = False
        _CAPABILITY_CACHE["--timeout-ms"] = False


def supports(flag: str) -> bool:
    """Return True if the CLI binary supports the given flag."""
    _probe_capabilities()
    return _CAPABILITY_CACHE.get(flag, False)

class DecompileRequest(BaseModel):
    binary_b64: str
    addr: str

class DecompileResponse(BaseModel):
    decompiler: str = "fission"
    name: str
    code: str
    # Dual surfaces from Fission CLI (optional; older CLIs omit them).
    code_nir: Optional[str] = None
    code_hir: Optional[str] = None
    layer: Optional[str] = None
    time_ms: int
    error: Optional[str] = None

class BatchDecompileRequest(BaseModel):
    binary_b64: str
    addresses: List[str]

class DecompileResultItem(BaseModel):
    addr: str
    name: str = "?"
    # Primary code stays NIR-faithful for semantic oracle compatibility.
    code: str = ""
    code_nir: Optional[str] = None
    code_hir: Optional[str] = None
    layer: Optional[str] = None
    error: Optional[str] = None

class BatchDecompileResponse(BaseModel):
    decompiler: str = "fission"
    results: List[DecompileResultItem]
    time_ms: int

def _read_text_file(path: Path, default: str = "") -> str:
    try:
        return path.read_text(encoding="utf-8").strip() or default
    except Exception:
        return default


@app.get("/health")
def health():
    """Health probe with provenance for release vs local quality-loop bundles."""
    version = "unknown"
    release_version = os.environ.get("FISSION_RELEASE_VERSION", "unknown")
    source = os.environ.get("FISSION_SOURCE") or _read_text_file(SOURCE_FILE, "release")
    git_sha = os.environ.get("FISSION_GIT_SHA") or _read_text_file(GIT_SHA_FILE, "")
    source_fingerprint = os.environ.get("FISSION_SOURCE_FINGERPRINT", "")
    try:
        r = subprocess.run(
            [str(FISSION_BIN), "--version"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        version = r.stdout.strip() or r.stderr.strip()
    except Exception:
        pass
    release_version = _read_text_file(RELEASE_VERSION_FILE, release_version)
    # Probe capabilities so they are available immediately on first health call.
    _probe_capabilities()
    payload = {
        "status": "ok",
        "decompiler": "fission",
        "version": version,
        "release_version": release_version,
        # "release" = GitHub Release bake (CI contract). "local" = host bundle mount.
        "source": source if source in ("release", "local") else "release",
        # Capabilities discovered from `fission_cli decomp --help`.
        # Consumers can use this to understand which optional flags are available
        # without re-probing the CLI.
        "capabilities": {
            k: v for k, v in _CAPABILITY_CACHE.items()
        },
    }
    if git_sha:
        payload["git_sha"] = git_sha
    if source_fingerprint:
        payload["source_fingerprint"] = source_fingerprint
    return payload

def run_fission_cli(args: List[str]):
    env = {
        **os.environ,
        "FISSION_SLEIGH_SPEC_DIR": SLEIGH_SPEC_DIR,
        "FISSION_RESOURCE_ROOT": RESOURCE_ROOT,
        "FISSION_GHIDRA_DATA_DIR": GHIDRA_DATA_DIR,
    }
    result = subprocess.run([str(FISSION_BIN)] + args, env=env, capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        raise HTTPException(status_code=500, detail=result.stderr or result.stdout)
    return json.loads(result.stdout)

def validate_address(addr: str) -> int:
    if not addr or not addr.strip():
        raise HTTPException(status_code=400, detail="Address cannot be empty")
    try:
        if addr.lower().startswith("0x"):
            return int(addr, 16)
        try:
            return int(addr, 10)
        except ValueError:
            return int(addr, 16)
    except ValueError:
        raise HTTPException(status_code=400, detail=f"Invalid address format: {addr}")

def resolve_binary(binary: str) -> str:
    if not binary or not binary.strip():
        raise HTTPException(status_code=400, detail="Binary path cannot be empty")
    resolved = "/" + binary if binary.startswith("corpus/") else binary
    if not os.path.exists(resolved):
        raise HTTPException(status_code=404, detail=f"Binary not found: {resolved}")
    return resolved

def decompile_batch_command(binary_path: str, addresses_path: str) -> List[str]:
    """Build CLI command for batch decompilation.

    Optional flags (``--layer``, ``--benchmark``, ``--timeout-ms``) are added
    only when the capability probe confirms the current CLI version supports
    them.  This prevents hard failures on older release bundles that predate
    these flags.
    """
    cmd = [
        str(FISSION_BIN),
        "decomp",
        binary_path,
        "--addresses-file",
        addresses_path,
        "--json",
    ]
    # --benchmark and --timeout-ms are optional quality-of-life flags.
    if supports("--benchmark"):
        cmd.append("--benchmark")
    if supports("--timeout-ms"):
        cmd += ["--timeout-ms", DECOMP_TIMEOUT_MS]
    # --layer nir: only add when the CLI explicitly supports it.
    # Older releases output NIR by default anyway, so omitting is safe.
    if supports("--layer"):
        cmd += ["--layer", "nir"]
    return cmd

def normalize_decompile_results(payload: object) -> list[dict]:
    if isinstance(payload, dict):
        functions = payload.get("functions", [])
        return functions if isinstance(functions, list) else []
    if isinstance(payload, list):
        return payload
    return []


def decompile_result_from_cli_item(item: dict, fallback_addr: Optional[str] = None) -> DecompileResultItem:
    """Map Fission CLI JSON function row → adapter result (preserves dual layers)."""
    code = item.get("code") or ""
    code_nir = item.get("code_nir")
    code_hir = item.get("code_hir")
    # Older CLIs only have `code`; treat it as NIR when dual fields are absent.
    if not code_nir and code:
        code_nir = code
    if not code_hir and code:
        code_hir = code
    return DecompileResultItem(
        addr=item.get("addr") or item.get("address") or (fallback_addr or ""),
        name=item.get("name", "?"),
        code=code,
        code_nir=code_nir,
        code_hir=code_hir,
        layer=item.get("layer"),
        error=item.get("error"),
    )

@app.get("/functions")
def functions(binary: str):
    bin_path = resolve_binary(binary)
    data = run_fission_cli(["list", bin_path, "--json"])
    res = []
    for item in data:
        res.append({
            "address": item.get("address"),
            "name": item.get("name"),
            "size": item.get("size", 0),
            "kind": "function" if item.get("kind") == "code" else item.get("kind", "function")
        })
    return res

@app.get("/disasm")
def disasm(binary: str, addr: str):
    validate_address(addr)
    bin_path = resolve_binary(binary)
    data = run_fission_cli(["disasm", bin_path, "--addr", addr, "--function", "--json"])
    res = []
    for inst in data.get("instructions", []):
        res.append({
            "address": inst.get("address"),
            "bytes": inst.get("bytes"),
            "mnemonic": inst.get("instruction", "").split()[0].lower() if inst.get("instruction") else "",
            "operands": inst.get("instruction", "").split(None, 1)[1] if len(inst.get("instruction", "").split(None, 1)) > 1 else "",
            "length": len(inst.get("bytes", "")) // 2,
            "fallthrough": None, # Fission raw instruction JSON doesn't expose fallthrough easily
            "branch_target": None
        })
    return res

@app.get("/decode")
def decode(binary: str, addr: str):
    validate_address(addr)
    # Decode is mapped from disassembly in same manner
    disasm_data = disasm(binary, addr)
    res = []
    for inst in disasm_data:
        res.append({
            "address": inst.get("address"),
            "bytes": inst.get("bytes"),
            "length": inst.get("length"),
            "mnemonic": inst.get("mnemonic"),
            "prefixes": [],
            "modrm": None,
            "sib": None,
            "displacement": None,
            "immediate": None
        })
    return res

@app.get("/pcode")
def pcode(binary: str, addr: str):
    validate_address(addr)
    bin_path = resolve_binary(binary)
    data = run_fission_cli(["raw-pcode", bin_path, "--addr", addr, "--json"])
    # Map raw-pcode output to schema
    res = []
    seq = 0
    for block in data.get("raw_pcode_blocks", []):
        for op in block.get("ops", []):
            output = None
            out_node = op.get("output")
            if out_node:
                # Map space_id to string representation
                space_id = out_node.get("space_id", 0)
                space_name = "unique" if space_id == 2 else "register" if space_id == 4 else "ram" if space_id == 3 else "const" if space_id == 0 else f"space_{space_id}"
                output = {
                    "space": space_name,
                    "offset": f"0x{out_node.get('offset', 0):x}",
                    "size": out_node.get("size", 0)
                }

            inputs = []
            for node in op.get("inputs", []):
                space_id = node.get("space_id", 0)
                space_name = "unique" if space_id == 2 else "register" if space_id == 4 else "ram" if space_id == 3 else "const" if space_id == 0 else f"space_{space_id}"
                inputs.append({
                    "space": space_name,
                    "offset": f"0x{node.get('offset', 0):x}",
                    "size": node.get("size", 0)
                })

            res.append({
                "seq": seq,
                "op": op.get("asm_mnemonic", op.get("opcode")),
                "output": output,
                "inputs": inputs
            })
            seq += 1
    return res

@app.get("/cfg")
def cfg(binary: str, addr: str):
    validate_address(addr)
    bin_path = resolve_binary(binary)
    data = run_fission_cli(["pcode-topology", bin_path, "--addr", addr, "--json"])
    # Map pcode-topology to schema
    blocks = []
    edges = []
    for block in data.get("raw_pcode_blocks", []):
        start = f"0x{block.get('start_address', 0):x}"
        # Estimate end address using terminal instruction size or approximation
        blocks.append({
            "start": start,
            "end": start # keep simple
        })
        for succ in block.get("successors", []):
            # Resolve successor address from index
            target_block = next((b for b in data.get("raw_pcode_blocks", []) if b.get("index") == succ), None)
            if target_block:
                edges.append({
                    "source": start,
                    "target": f"0x{target_block.get('start_address', 0):x}",
                    "kind": "branch"
                })
    return {"blocks": blocks, "edges": edges}

@app.post("/decompile", response_model=DecompileResponse)
def decompile(req: DecompileRequest):
    validate_address(req.addr)
    batch_req = BatchDecompileRequest(binary_b64=req.binary_b64, addresses=[req.addr])
    start = time.monotonic()
    try:
        resp = decompile_batch(batch_req)
        elapsed = int((time.monotonic() - start) * 1000)
        item = resp.results[0]
        if item.error:
            return DecompileResponse(name="?", code="", time_ms=elapsed, error=item.error)
        return DecompileResponse(
            name=item.name,
            code=item.code,
            code_nir=item.code_nir,
            code_hir=item.code_hir,
            layer=item.layer,
            time_ms=elapsed,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/decompile_batch", response_model=BatchDecompileResponse)
def decompile_batch(req: BatchDecompileRequest):
    try:
        binary_bytes = base64.b64decode(req.binary_b64, validate=True)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid base64 payload")
        
    with tempfile.NamedTemporaryFile(suffix=".bin", delete=False) as f_bin:
        f_bin.write(binary_bytes)
        tmp_bin_path = f_bin.name
    with tempfile.NamedTemporaryFile(suffix=".txt", mode="w", delete=False) as f_addrs:
        for addr in req.addresses:
            f_addrs.write(f"{addr}\n")
        tmp_addrs_path = f_addrs.name

    env = {
        **os.environ,
        "FISSION_SLEIGH_SPEC_DIR": SLEIGH_SPEC_DIR,
        "FISSION_RESOURCE_ROOT": RESOURCE_ROOT,
        "FISSION_GHIDRA_DATA_DIR": GHIDRA_DATA_DIR,
    }
    start = time.monotonic()
    try:
        batch_failed = False
        try:
            result = subprocess.run(
                decompile_batch_command(tmp_bin_path, tmp_addrs_path),
                env=env, capture_output=True, text=True, timeout=120
            )
            if result.returncode != 0:
                batch_failed = True
            else:
                res_list = normalize_decompile_results(json.loads(result.stdout))
                results = [decompile_result_from_cli_item(item) for item in res_list]
        except Exception:
            batch_failed = True

        if batch_failed:
            results = []
            for addr in req.addresses:
                with tempfile.NamedTemporaryFile(suffix=".txt", mode="w", delete=False) as f_single:
                    f_single.write(f"{addr}\n")
                    tmp_single_path = f_single.name
                try:
                    res_single = subprocess.run(
                        decompile_batch_command(tmp_bin_path, tmp_single_path),
                        env=env, capture_output=True, text=True, timeout=60
                    )
                    if res_single.returncode != 0:
                        results.append(DecompileResultItem(
                            addr=addr,
                            error=f"Batch fallback failed with exit code {res_single.returncode}: {res_single.stderr or res_single.stdout}"
                        ))
                    else:
                        res_list = normalize_decompile_results(json.loads(res_single.stdout))
                        if res_list:
                            results.append(decompile_result_from_cli_item(res_list[0], fallback_addr=addr))
                        else:
                            results.append(DecompileResultItem(
                                addr=addr,
                                error="No decompile result returned for address"
                            ))
                except Exception as e:
                    results.append(DecompileResultItem(
                        addr=addr,
                        error=f"Batch fallback failed with exception: {str(e)}"
                    ))
                finally:
                    try:
                        os.unlink(tmp_single_path)
                    except Exception:
                        pass
        elapsed = int((time.monotonic() - start) * 1000)
        return BatchDecompileResponse(results=results, time_ms=elapsed)
    finally:
        try:
            os.unlink(tmp_bin_path)
        except Exception:
            pass
        try:
            os.unlink(tmp_addrs_path)
        except Exception:
            pass
