"""HTTP providers that pull parity JSON from decompiler Docker adapters.

Default reference is Ghidra; candidates are typically Fission (or others).
This is the primary provider path for completed parity stages — command-template
providers remain available for custom tools.
"""
from __future__ import annotations

import os
from typing import Any
from urllib.parse import quote

import requests

from benchmark.common.schema import BenchmarkSubject

# Host ports mirror docker-compose.yml (overridable via env).
# Local quality-loop often maps fission to 8007 (see docker-compose.local.yml).
DEFAULT_PORTS: dict[str, int] = {
    "fission": int(os.environ.get("FISSION_HOST_PORT", "8000")),
    "ghidra": int(os.environ.get("GHIDRA_HOST_PORT", "8001")),
    "boomerang": int(os.environ.get("BOOMERANG_HOST_PORT", "8002")),
    "radare2": int(os.environ.get("RADARE2_HOST_PORT", "8003")),
    "angr": int(os.environ.get("ANGR_HOST_PORT", "8004")),
    "snowman": int(os.environ.get("SNOWMAN_HOST_PORT", "8005")),
    "revng": int(os.environ.get("REVNG_HOST_PORT", "8006")),
    "reko": int(os.environ.get("REKO_HOST_PORT", "8008")),
    "retdec": int(os.environ.get("RETDEC_HOST_PORT", "8009")),
}

_FISSION_PORT_PROBED = False


def ensure_fission_port() -> int:
    """Resolve live Fission adapter port (8000 vs 8007 overlay).

    Wrong default port is a reliability footgun: golden/stage CLIs hit another
    service on 8000 and report systematic HTTP 404 as quality errors.
    """
    global _FISSION_PORT_PROBED
    if "FISSION_HOST_PORT" in os.environ:
        port = int(os.environ["FISSION_HOST_PORT"])
        DEFAULT_PORTS["fission"] = port
        return port
    if _FISSION_PORT_PROBED:
        return DEFAULT_PORTS["fission"]
    _FISSION_PORT_PROBED = True
    host = os.environ.get("PARITY_HTTP_HOST", "localhost")
    for probe in (DEFAULT_PORTS["fission"], 8007, 8000):
        try:
            r = requests.get(f"http://{host}:{probe}/health", timeout=1.5)
            if r.ok and (r.json() or {}).get("decompiler") == "fission":
                DEFAULT_PORTS["fission"] = probe
                return probe
        except Exception:
            continue
    return DEFAULT_PORTS["fission"]

# stage -> HTTP path segment on each adapter
STAGE_ENDPOINT: dict[str, str] = {
    "assembly_parity": "disasm",
    "decode_parity": "decode",
    "pcode_parity": "pcode",
    "cfg_parity": "cfg",
    "function_discovery": "functions",
    "metadata_parity": "metadata",
    "parity_bundle": "parity_bundle",
    "abi_parity": "abi",
    "type_parity": "types",
    "callgraph_parity": "callgraph",
    "string_recovery": "strings",
    "dataflow_parity": "dataflow",
    "seh_parity": "seh",
}


def corpus_relative_binary(binary: str, corpus_split: str = "dev") -> str:
    """Normalize binary path to the form adapters expect: corpus/<split>/..."""
    text = binary.replace("\\", "/")
    if text.startswith("corpus/"):
        return text
    # Absolute path ending with corpus/...
    marker = f"/corpus/{corpus_split}/"
    idx = text.find(marker)
    if idx >= 0:
        return text[idx + 1 :]  # drop leading slash -> corpus/...
    if "/corpus/" in text:
        return text[text.find("/corpus/") + 1 :]
    # Path like binaries/foo.exe under a split
    if text.startswith("binaries/"):
        return f"corpus/{corpus_split}/{text}"
    return f"corpus/{corpus_split}/binaries/{text}" if not text.startswith("binaries") else f"corpus/{corpus_split}/{text}"


def base_url(decompiler: str) -> str:
    if decompiler == "fission":
        ensure_fission_port()
    port = DEFAULT_PORTS.get(decompiler)
    if not port:
        raise ValueError(f"unknown decompiler {decompiler!r}; known: {sorted(DEFAULT_PORTS)}")
    host = os.environ.get("PARITY_HTTP_HOST", "localhost")
    return f"http://{host}:{port}"


def fetch_parity_json(
    decompiler: str,
    stage: str,
    subject: BenchmarkSubject,
    *,
    timeout: float = 60.0,
) -> Any:
    """GET parity payload for one subject from a decompiler adapter."""
    endpoint = STAGE_ENDPOINT.get(stage)
    if not endpoint:
        raise ValueError(f"no HTTP endpoint for stage {stage!r}")

    if decompiler == "fission":
        ensure_fission_port()

    binary = corpus_relative_binary(subject.binary, subject.corpus_split)
    url = f"{base_url(decompiler)}/{endpoint}?binary={quote(binary, safe='/:')}"
    if endpoint not in {"functions", "metadata"} and subject.addr and subject.addr not in {"0x0", "0"}:
        url += f"&addr={quote(subject.addr, safe='')}"
    if subject.arch and subject.arch not in {"unknown", "arch_unknown"}:
        url += f"&arch={quote(subject.arch, safe='')}"

    response = requests.get(url, timeout=timeout)
    if response.status_code != 200:
        raise RuntimeError(
            f"{decompiler}/{endpoint} HTTP {response.status_code}: {response.text[:300]}"
        )
    return response.json()
