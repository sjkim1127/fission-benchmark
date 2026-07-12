"""rev.ng decompiler and parity diagnostic API server."""
import base64
import re
import subprocess
import tempfile
import time
from pathlib import Path
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import disasm_helper
from boundary import (
    address_hex_forms,
    extract_braced_unit,
    inject_address_anchor,
    parse_addr_int,
    rewrite_function_name,
    strip_leading_macros,
)

app = FastAPI(title="revng-decompiler", version="1.0")


class DecompileRequest(BaseModel):
    binary_b64: str
    addr: str


class DecompileResponse(BaseModel):
    decompiler: str = "revng"
    name: str
    code: str
    time_ms: int
    error: Optional[str] = None


class BatchDecompileRequest(BaseModel):
    binary_b64: str
    addresses: List[str]


class DecompileResultItem(BaseModel):
    addr: str
    name: str = "?"
    code: str = ""
    error: Optional[str] = None


class BatchDecompileResponse(BaseModel):
    decompiler: str = "revng"
    results: List[DecompileResultItem]
    time_ms: int


def _addr_hex(addr: str) -> str:
    try:
        return f"{parse_addr_int(addr):x}"
    except ValueError:
        return addr.lower().removeprefix("0x")


FUNCTION_DEF_RE = re.compile(
    r"(?m)(?:^_ABI[^\n]*\n)?^[^\n;{}]*\bfunction_0x([0-9a-fA-F]+)_[A-Za-z0-9_]+\s*\("
)
FUNCTION_NAME_RE = re.compile(
    r"\b(function_0x([0-9a-fA-F]+)_[A-Za-z0-9_]+)\s*\("
)


def _extract_function_at_match(code: str, match: re.Match[str]) -> str:
    start = match.start()
    brace = code.find("{", match.end())
    if brace < 0:
        nl = code.find("\n", match.end())
        return code[start : nl if nl >= 0 else match.end()].strip()
    return extract_braced_unit(code, start, brace)


def extract_revng_function(code: str, addr: str) -> tuple[str, str]:
    """Extract one function from revng plain C output by address-derived name.

    Returns (original_name, body).
    """
    addr_hex = _addr_hex(addr)
    target = int(addr_hex, 16)
    # Also try RVA forms if VA given
    targets = {target}
    for form in address_hex_forms(addr):
        try:
            targets.add(int(form.lower().removeprefix("0x"), 16))
        except Exception:
            pass

    definitions: list[tuple[int, str, re.Match[str]]] = []
    for match in FUNCTION_NAME_RE.finditer(code):
        try:
            fn_addr = int(match.group(2), 16)
        except Exception:
            continue
        definitions.append((fn_addr, match.group(1), match))
    definitions.sort(key=lambda item: item[0])

    for fn_addr, name, match in definitions:
        if fn_addr in targets:
            return name, _extract_function_at_match(code, match)

    # Containing-function fallback: nearest preceding entry
    for index, (fn_addr, name, match) in enumerate(definitions):
        next_addr = definitions[index + 1][0] if index + 1 < len(definitions) else None
        if any(
            fn_addr <= t and (next_addr is None or t < next_addr) for t in targets
        ):
            return name, _extract_function_at_match(code, match)

    return "", ""


def normalize_revng_unit(code: str, addr: str, original_name: str) -> tuple[str, str]:
    """Strip ABI noise, rename to stable symbol, inject address anchor."""
    if not code:
        return f"function_0x{_addr_hex(addr)}", ""
    text = strip_leading_macros(code, ("_ABI(", "_REG(", "// _ABI"))
    # Drop remaining single-line ABI/REG macros
    text = re.sub(r"(?m)^[ \t]*_ABI\([^\n]*\n", "", text)
    text = re.sub(r"(?m)^[ \t]*_REG\([^\n]*\n", "", text)
    text = re.sub(r"\b_STACK\b", "/*_STACK*/", text)
    stable = f"function_0x{_addr_hex(addr)}"
    if original_name:
        text = rewrite_function_name(text, original_name, stable)
    else:
        m = re.search(
            r"(?m)^\s*(?:[\w_][\w\s_*\(\),]*\s+)?([A-Za-z_][\w]*)\s*\([^;{}]*\)\s*\{",
            text,
        )
        if m and m.group(1) not in {"if", "for", "while", "switch"}:
            text = rewrite_function_name(text, m.group(1), stable)
    text = inject_address_anchor(text, addr, "revng")
    return stable, text


@app.get("/health")
def health():
    return {"status": "ok", "decompiler": "revng", "version": "latest"}


def resolve_binary(binary: str) -> str:
    if binary.startswith("corpus/"):
        return "/" + binary
    return binary


@app.get("/functions")
def functions(binary: str):
    return disasm_helper.get_functions(resolve_binary(binary))


@app.get("/disasm")
def disasm(binary: str, addr: str, arch: str = "x86_64"):
    return disasm_helper.disassemble(resolve_binary(binary), addr, arch)


@app.get("/decode")
def decode(binary: str, addr: str, arch: str = "x86_64"):
    disasm_data = disasm(binary, addr, arch)
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


@app.get("/pcode")
def pcode(binary: str, addr: str):
    return []


@app.get("/cfg")
def cfg(binary: str, addr: str):
    return {"blocks": [], "edges": []}


@app.post("/decompile", response_model=DecompileResponse)
def decompile(req: DecompileRequest):
    batch_req = BatchDecompileRequest(binary_b64=req.binary_b64, addresses=[req.addr])
    start = time.monotonic()
    try:
        resp = decompile_batch(batch_req)
        elapsed = int((time.monotonic() - start) * 1000)
        item = resp.results[0]
        if item.error:
            return DecompileResponse(name="?", code="", time_ms=elapsed, error=item.error)
        return DecompileResponse(name=item.name, code=item.code, time_ms=elapsed)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/decompile_batch", response_model=BatchDecompileResponse)
def decompile_batch(req: BatchDecompileRequest):
    binary_bytes = base64.b64decode(req.binary_b64)
    with tempfile.TemporaryDirectory() as tmpdir:
        binary_path = Path(tmpdir) / "target.bin"
        binary_path.write_bytes(binary_bytes)
        ptml_path = Path(tmpdir) / "decompiled.ptml"
        start = time.monotonic()
        results = []
        try:
            artifact = subprocess.run(
                [
                    "revng",
                    "artifact",
                    "--analyze",
                    "decompile-to-single-file",
                    str(binary_path),
                    "-o",
                    str(ptml_path),
                ],
                capture_output=True,
                text=True,
                timeout=240,
            )
            if artifact.returncode != 0:
                detail = artifact.stderr or artifact.stdout or "revng artifact failed"
                results = [
                    DecompileResultItem(addr=addr, name=f"func_{addr}", error=detail)
                    for addr in req.addresses
                ]
            else:
                plain = subprocess.run(
                    ["revng", "ptml", str(ptml_path)],
                    capture_output=True,
                    text=True,
                    timeout=60,
                )
                if plain.returncode != 0:
                    detail = plain.stderr or plain.stdout or "revng ptml conversion failed"
                    results = [
                        DecompileResultItem(addr=addr, name=f"func_{addr}", error=detail)
                        for addr in req.addresses
                    ]
                else:
                    code = plain.stdout
                    for addr in req.addresses:
                        original, fn_code = extract_revng_function(code, addr)
                        if fn_code:
                            name, normalized = normalize_revng_unit(
                                fn_code, addr, original
                            )
                            results.append(
                                DecompileResultItem(
                                    addr=addr, name=name, code=normalized
                                )
                            )
                        else:
                            results.append(
                                DecompileResultItem(
                                    addr=addr,
                                    name=f"func_{addr}",
                                    error=f"revng output did not contain function {addr}",
                                )
                            )
        except Exception as e:
            results = [
                DecompileResultItem(addr=addr, name=f"func_{addr}", error=str(e))
                for addr in req.addresses
            ]
        elapsed = int((time.monotonic() - start) * 1000)
        return BatchDecompileResponse(results=results, time_ms=elapsed)
