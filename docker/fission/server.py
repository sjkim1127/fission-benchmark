"""Fission decompiler and parity diagnostic API server."""
import base64
import hashlib
import json
import os
import subprocess
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
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
_CAPABILITY_PROBE_ERROR: str | None = None


def _probe_capabilities() -> None:
    """Populate _CAPABILITY_CACHE from `fission_cli decomp --help` output."""
    global _CAPABILITY_PROBED, _CAPABILITY_PROBE_ERROR
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
        if r.returncode not in (0, 1):  # --help may exit 1 on some CLIs
            _CAPABILITY_PROBE_ERROR = (
                f"fission_cli decomp --help exited {r.returncode}: "
                f"{help_text[:200]}"
            )
            _CAPABILITY_CACHE["--layer"] = False
            _CAPABILITY_CACHE["--benchmark"] = False
            _CAPABILITY_CACHE["--timeout-ms"] = False
        else:
            _CAPABILITY_CACHE["--layer"] = "--layer" in help_text
            _CAPABILITY_CACHE["--benchmark"] = "--benchmark" in help_text
            _CAPABILITY_CACHE["--timeout-ms"] = "--timeout-ms" in help_text
    except Exception as exc:
        # If help fails, assume minimal capability set (no optional flags).
        _CAPABILITY_PROBE_ERROR = str(exc)
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
        # Probe diagnostics — allows contract tests to distinguish between
        # "probe ran but found no flags" vs "probe itself crashed".
        "capability_probe_ok": _CAPABILITY_PROBE_ERROR is None,
        "capability_probe_error": _CAPABILITY_PROBE_ERROR,
        "parity": {
            "multi_bundle": "/parity_multi_bundle",
            "cli_workers": _CLI_WORKERS,
            "mode": "tool_phased_multi_addr",
            "cache_key": "path+content_fingerprint",
        },
    }
    if git_sha:
        payload["git_sha"] = git_sha
    if source_fingerprint:
        payload["source_fingerprint"] = source_fingerprint
    return payload

# Cap concurrent fission_cli children so multi_bundle cannot thrash the host
# (default 8). Each CLI still reloads the PE; multi-addr batching below cuts
# peak concurrency and amortizes orchestration cost.
_CLI_WORKERS = max(1, int(os.environ.get("FISSION_CLI_WORKERS", "8")))
_CLI_SEM = threading.Semaphore(_CLI_WORKERS)


def run_fission_cli(args: List[str]):
    env = {
        **os.environ,
        "FISSION_SLEIGH_SPEC_DIR": SLEIGH_SPEC_DIR,
        "FISSION_RESOURCE_ROOT": RESOURCE_ROOT,
        "FISSION_GHIDRA_DATA_DIR": GHIDRA_DATA_DIR,
    }
    with _CLI_SEM:
        result = subprocess.run(
            [str(FISSION_BIN)] + args,
            env=env,
            capture_output=True,
            text=True,
            timeout=60,
        )
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

_PARITY_CACHE: Dict[tuple, object] = {}
_PARITY_CACHE_MAX = 1024
_FP_CACHE: Dict[str, tuple] = {}  # path -> (size, mtime_ns, fp)


def _binary_fingerprint(bin_path: str) -> str:
    """Content fingerprint so same path after corpus rebuild does not reuse stale cache."""
    try:
        st = os.stat(bin_path)
    except OSError:
        return "missing"
    cached = _FP_CACHE.get(bin_path)
    if cached and cached[0] == st.st_size and cached[1] == st.st_mtime_ns:
        return cached[2]
    h = hashlib.sha256()
    h.update(f"{st.st_size}:{st.st_mtime_ns}".encode("utf-8"))
    try:
        with open(bin_path, "rb") as fh:
            h.update(fh.read(65536))
            if st.st_size > 65536:
                fh.seek(max(0, st.st_size - 65536))
                h.update(fh.read(65536))
    except OSError:
        return f"err-{st.st_size}-{st.st_mtime_ns}"
    fp = h.hexdigest()[:16]
    _FP_CACHE[bin_path] = (st.st_size, st.st_mtime_ns, fp)
    return fp


def _cache_get(key: tuple):
    return _PARITY_CACHE.get(key)


def _cache_put(key: tuple, value: object) -> None:
    if len(_PARITY_CACHE) >= _PARITY_CACHE_MAX:
        try:
            del _PARITY_CACHE[next(iter(_PARITY_CACHE))]
        except StopIteration:
            pass
    _PARITY_CACHE[key] = value


def _normalize_addr_key(addr: str) -> str:
    text = addr.strip().lower()
    try:
        return f"0x{int(text, 16):x}"
    except ValueError:
        return text


@app.get("/functions")
def functions(binary: str):
    bin_path = resolve_binary(binary)
    fp = _binary_fingerprint(bin_path)
    cache_key = ("functions", fp, bin_path)
    cached = _cache_get(cache_key)
    if cached is not None:
        return cached
    data = run_fission_cli(["list", bin_path, "--json"])
    res = []
    for item in data:
        res.append({
            "address": item.get("address"),
            "name": item.get("name"),
            "size": item.get("size", 0),
            "kind": "function" if item.get("kind") == "code" else item.get("kind", "function")
        })
    _cache_put(cache_key, res)
    return res


def _normalize_hex_bytes(raw: object) -> str:
    """Normalize instruction bytes to compact lowercase hex without spaces."""
    text = str(raw or "").strip().lower().replace(" ", "").replace("0x", "")
    return text


def _as_int(value: object, default: int = 0) -> int:
    """Coerce CLI JSON fields that may be null/str into int without raising."""
    if value is None or value is False:
        return default
    try:
        if isinstance(value, str):
            text = value.strip().lower()
            if not text:
                return default
            return int(text, 16) if text.startswith("0x") else int(text, 0)
        return int(value)
    except (TypeError, ValueError):
        return default


def _ck(kind: str, bin_path: str, *parts: str) -> tuple:
    """Cache key including content fingerprint for the binary path."""
    return (kind, _binary_fingerprint(bin_path), bin_path, *parts)


def _disasm_impl(bin_path: str, addr: str) -> list:
    cache_key = _ck("disasm", bin_path, _normalize_addr_key(addr))
    cached = _cache_get(cache_key)
    if cached is not None:
        return cached  # type: ignore[return-value]
    data = run_fission_cli(["disasm", bin_path, "--addr", addr, "--function", "--json"])
    res = []
    for inst in data.get("instructions", []):
        byte_hex = _normalize_hex_bytes(inst.get("bytes"))
        text = (inst.get("instruction") or "").strip()
        parts = text.split(None, 1)
        res.append({
            "address": inst.get("address"),
            "bytes": byte_hex,
            "mnemonic": parts[0].lower() if parts else "",
            "operands": parts[1] if len(parts) > 1 else "",
            "length": len(byte_hex) // 2 if byte_hex else 0,
            "fallthrough": None,
            "branch_target": None,
        })
    _cache_put(cache_key, res)
    return res


def _disasm_to_decode(disasm_data: list) -> list:
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
            "immediate": None,
        })
    return res


@app.get("/disasm")
def disasm(binary: str, addr: str):
    validate_address(addr)
    return _disasm_impl(resolve_binary(binary), addr)


@app.get("/decode")
def decode(binary: str, addr: str):
    validate_address(addr)
    # Free: derived from disasm (no second CLI).
    return _disasm_to_decode(_disasm_impl(resolve_binary(binary), addr))


def _space_name(space_id: object) -> str:
    sid = _as_int(space_id, 0)
    return {
        0: "const",
        2: "unique",
        3: "ram",
        4: "register",
    }.get(sid, f"space_{sid}")


def _map_varnode(node: dict | None) -> dict | None:
    if not node:
        return None
    return {
        "space": _space_name(node.get("space_id", 0)),
        "offset": f"0x{_as_int(node.get('offset', 0)):x}",
        "size": _as_int(node.get("size", 0)),
    }


def _pcode_impl(bin_path: str, addr: str) -> list:
    cache_key = _ck("pcode", bin_path, _normalize_addr_key(addr))
    cached = _cache_get(cache_key)
    if cached is not None:
        return cached  # type: ignore[return-value]
    data = run_fission_cli(["raw-pcode", bin_path, "--addr", addr, "--json"])
    blocks = []
    if isinstance(data.get("pcode"), dict) and isinstance(data["pcode"].get("blocks"), list):
        blocks = data["pcode"]["blocks"]
    elif isinstance(data.get("raw_pcode_blocks"), list):
        blocks = data["raw_pcode_blocks"]

    res = []
    seq = 0
    for block in blocks:
        for op in block.get("ops", []):
            res.append({
                "seq": seq,
                "op": op.get("opcode") or op.get("asm_mnemonic") or "UNKNOWN",
                "output": _map_varnode(op.get("output")),
                "inputs": [
                    _map_varnode(node)
                    for node in (op.get("inputs") or [])
                    if isinstance(node, dict)
                ],
            })
            seq += 1
    _cache_put(cache_key, res)
    return res


def _cfg_impl(bin_path: str, addr: str) -> dict:
    cache_key = _ck("cfg", bin_path, _normalize_addr_key(addr))
    cached = _cache_get(cache_key)
    if cached is not None:
        return cached  # type: ignore[return-value]
    data = run_fission_cli(["pcode-topology", bin_path, "--addr", addr, "--json"])
    topo = data.get("raw_pcode_topology") if isinstance(data.get("raw_pcode_topology"), dict) else {}
    raw_blocks = topo.get("blocks") if isinstance(topo.get("blocks"), list) else data.get("raw_pcode_blocks")
    if not isinstance(raw_blocks, list):
        raw_blocks = []

    by_index = {_as_int(b.get("index", i), i): b for i, b in enumerate(raw_blocks)}
    blocks = []
    edges = []
    for block in raw_blocks:
        start_raw = _as_int(block.get("start_address", 0))
        end_raw = _as_int(block.get("terminal_address", start_raw), start_raw)
        start = f"0x{start_raw:x}"
        end = f"0x{end_raw:x}"
        blocks.append({"start": start, "end": end})
        for succ in block.get("successors") or []:
            target_block = by_index.get(_as_int(succ))
            if not target_block:
                continue
            edges.append({
                "source": start,
                "target": f"0x{_as_int(target_block.get('start_address', 0)):x}",
                "kind": "branch",
            })
    out = {"blocks": blocks, "edges": edges}
    _cache_put(cache_key, out)
    return out


@app.get("/pcode")
def pcode(binary: str, addr: str):
    validate_address(addr)
    return _pcode_impl(resolve_binary(binary), addr)


@app.get("/cfg")
def cfg(binary: str, addr: str):
    validate_address(addr)
    return _cfg_impl(resolve_binary(binary), addr)


def _assemble_bundle(key: str, dis, pc, cg) -> dict:
    out = {
        "schema": "fission-parity-bundle-v1",
        "address": key,
        "disasm": dis,
        "decode": _disasm_to_decode(dis if isinstance(dis, list) else []),
        "pcode": pc,
        "cfg": cg,
    }
    return out


def _bundle_one(bin_path: str, addr: str) -> dict:
    """disasm + pcode + cfg for one address (decode free from disasm)."""
    key = _normalize_addr_key(addr)
    cache_key = _ck("bundle", bin_path, key)
    cached = _cache_get(cache_key)
    if isinstance(cached, dict):
        return cached

    with ThreadPoolExecutor(max_workers=3) as pool:
        f_dis = pool.submit(_disasm_impl, bin_path, addr)
        f_pcode = pool.submit(_pcode_impl, bin_path, addr)
        f_cfg = pool.submit(_cfg_impl, bin_path, addr)
        dis = f_dis.result()
        pc = f_pcode.result()
        cg = f_cfg.result()

    out = _assemble_bundle(key, dis, pc, cg)
    _cache_put(cache_key, out)
    return out


def _map_addrs(impl, bin_path: str, addrs: List[str], workers: int) -> dict:
    """Run a single CLI-backed tool over many addresses (multi-addr batch)."""
    out: dict = {}
    if not addrs:
        return out
    w = min(max(1, workers), len(addrs))
    with ThreadPoolExecutor(max_workers=w) as pool:
        futures = {pool.submit(impl, bin_path, a): a for a in addrs}
        for fut in as_completed(futures):
            a = futures[fut]
            key = _normalize_addr_key(a)
            try:
                out[key] = fut.result()
            except Exception as exc:
                out[key] = exc
    return out


def _bundle_many(bin_path: str, addrs: List[str]) -> dict:
    """Multi-addr parity bundle for one binary.

    Strategy (process-spawn aware):
      1. Serve full bundles from in-memory cache when present.
      2. For misses, run *tool-phased* multi-addr batches:
         all disasm, all raw-pcode, all pcode-topology — three parallel
         address-maps with a global CLI semaphore. This caps peak
         fission_cli children at FISSION_CLI_WORKERS (not 3×N).
      3. Assemble per-address bundles; decode is free from disasm.
    """
    by_addr: dict = {}
    missing: List[str] = []
    for a in addrs:
        key = _normalize_addr_key(a)
        cached = _cache_get(_ck("bundle", bin_path, key))
        if isinstance(cached, dict):
            by_addr[key] = cached
        else:
            missing.append(a)

    if not missing:
        return by_addr

    # Split CLI budget across the three tools so they can run concurrently.
    per_tool = max(1, _CLI_WORKERS // 3)
    with ThreadPoolExecutor(max_workers=3) as pool:
        f_dis = pool.submit(_map_addrs, _disasm_impl, bin_path, missing, per_tool)
        f_pc = pool.submit(_map_addrs, _pcode_impl, bin_path, missing, per_tool)
        f_cfg = pool.submit(_map_addrs, _cfg_impl, bin_path, missing, per_tool)
        dis_map = f_dis.result()
        pc_map = f_pc.result()
        cfg_map = f_cfg.result()

    for a in missing:
        key = _normalize_addr_key(a)
        dis = dis_map.get(key)
        pc = pc_map.get(key)
        cg = cfg_map.get(key)
        tool_errors: dict = {}
        for label, val in (("disasm", dis), ("pcode", pc), ("cfg", cg)):
            if isinstance(val, Exception):
                tool_errors[label] = str(val)

        # Partial success: keep good surfaces. Full failure only if all tools died.
        if len(tool_errors) == 3:
            by_addr[key] = {"error": "; ".join(f"{k}: {v}" for k, v in tool_errors.items())}
            continue

        dis_ok = dis if not isinstance(dis, Exception) else None
        pc_ok = pc if not isinstance(pc, Exception) else None
        cg_ok = cg if not isinstance(cg, Exception) else None
        # Missing (None) without exception → empty, not a silent success cache of errors.
        if dis_ok is None:
            dis_ok = []
        if pc_ok is None:
            pc_ok = []
        if cg_ok is None:
            cg_ok = {"blocks": [], "edges": []}

        out = _assemble_bundle(key, dis_ok, pc_ok, cg_ok)
        if tool_errors:
            out["tool_errors"] = tool_errors
            # Do not cache partial/error results — retries should re-run tools.
        else:
            # Never cache fully empty multi-surface success (likely failed open).
            if dis_ok or pc_ok or (isinstance(cg_ok, dict) and cg_ok.get("blocks")):
                _cache_put(_ck("bundle", bin_path, key), out)
        by_addr[key] = out
    return by_addr


@app.get("/parity_bundle")
def parity_bundle(binary: str, addr: str):
    """One HTTP call → disasm/decode/pcode/cfg (CLI steps parallelized)."""
    validate_address(addr)
    t0 = time.monotonic()
    out = dict(_bundle_one(resolve_binary(binary), addr))
    out["time_ms"] = int((time.monotonic() - t0) * 1000)
    return out


@app.get("/parity_multi_bundle")
def parity_multi_bundle(binary: str, addrs: str):
    """Many addresses on one binary; tool-phased multi-addr batching."""
    t0 = time.monotonic()
    raw_list = [a.strip() for a in addrs.split(",") if a.strip()]
    if not raw_list:
        raise HTTPException(status_code=400, detail="addrs must be non-empty")
    for a in raw_list:
        validate_address(a)
    bin_path = resolve_binary(binary)
    by_addr = _bundle_many(bin_path, raw_list)

    return {
        "schema": "fission-parity-multi-bundle-v1",
        "by_addr": by_addr,
        "time_ms": int((time.monotonic() - t0) * 1000),
        "requested": len(raw_list),
        "cli_workers": _CLI_WORKERS,
        "mode": "tool_phased_multi_addr",
        "binary_fingerprint": _binary_fingerprint(bin_path),
    }

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
