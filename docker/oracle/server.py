"""Target-ABI differential semantic oracle service."""
from __future__ import annotations

import base64
import hashlib
import os
import subprocess
import tempfile
import threading
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel, Field

from runner.differential_oracle import (
    ORACLE_SUBJECT_ORIGINAL_BINARY,
    ORACLE_SUBJECT_SOURCE_RECOMPILE,
    build_differential_translation_unit,
    build_original_binary_translation_unit,
    parse_differential_output,
    wrapper_sha256,
)

app = FastAPI(title="fission-differential-oracle", version="1.2")
_wine_locks = {"windows-x86_64": threading.Lock(), "windows-x86": threading.Lock()}
_native_lock = threading.Lock()


class VerifyRequest(BaseModel):
    function_name: str = Field(min_length=1)
    reference_code: str = Field(min_length=1)
    candidate_code: str = Field(min_length=1)
    cases: list[str] = Field(min_length=1)
    compiler_variant: str = Field(min_length=1)
    reference_binary_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    # Optional original-binary subject inputs. When both are present the oracle
    # anchors the reference side on the provided PE instead of recompiled C.
    reference_binary_b64: str | None = None
    function_addr: str | None = None
    # Optional ABI/format from corpus variant tags (ELF multi-isa path).
    target_abi: str | None = None
    binary_format: str | None = None


def is_pe_bytes(data: bytes | None) -> bool:
    return bool(data) and data[:2] == b"MZ"


def is_elf_bytes(data: bytes | None) -> bool:
    return bool(data) and data[:4] == b"\x7fELF"


def compiler_profile(
    variant: str,
    *,
    target_abi: str | None = None,
    binary_format: str | None = None,
    ref_bytes: bytes | None = None,
) -> tuple[str, str, str, str]:
    """Return (target_abi, compiler, wine_arch_or_empty, runner).

    runner is one of: wine | native | qemu
    """
    # Explicit ELF / linux ABI tags win.
    abi = (target_abi or "").strip()
    fmt = (binary_format or "").strip().lower()
    if fmt == "elf" or abi.startswith("linux-") or is_elf_bytes(ref_bytes):
        if abi == "linux-aarch64" or "aarch64" in variant or "arm64" in variant:
            return "linux-aarch64", "aarch64-linux-gnu-gcc", "", "qemu"
        return "linux-x86_64", "gcc", "", "native"
    if abi == "windows-x86" or "-m32" in variant:
        return "windows-x86", "i686-w64-mingw32-gcc", "win32", "wine"
    if abi == "windows-x86_64" or is_pe_bytes(ref_bytes) or True:
        return "windows-x86_64", "x86_64-w64-mingw32-gcc", "win64", "wine"


def command_version(command: str) -> str:
    try:
        return subprocess.check_output([command, "--version"], text=True).splitlines()[0]
    except Exception:
        return "unknown"


def compile_program(
    compiler: str,
    source: str,
    root: Path,
    *,
    runner: str,
) -> tuple[subprocess.CompletedProcess[str], Path]:
    source_path = root / "oracle.c"
    # Keep PE candidates as .exe for wine; ELF candidates as bare binary.
    binary_path = root / ("oracle.exe" if runner == "wine" else "oracle.bin")
    source_path.write_text(source, encoding="utf-8")
    cmd = [compiler, "-std=c11", "-O0", "-w", str(source_path), "-o", str(binary_path)]
    if runner == "qemu":
        # Static helps qemu-user without dynamic loader paths.
        cmd[1:1] = ["-static"]
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=60,
    )
    return result, binary_path


def execute_program(
    binary_path: Path,
    target_abi: str,
    wine_arch: str,
    *,
    runner: str,
) -> subprocess.CompletedProcess[str]:
    if runner == "native":
        with _native_lock:
            return subprocess.run(
                [str(binary_path)],
                capture_output=True,
                text=True,
                timeout=60,
                cwd=str(binary_path.parent),
            )
    if runner == "qemu":
        qemu = "qemu-aarch64-static"
        with _native_lock:
            return subprocess.run(
                [qemu, str(binary_path)],
                capture_output=True,
                text=True,
                timeout=60,
                cwd=str(binary_path.parent),
            )
    wine_prefix = f"/tmp/fission-wine-{wine_arch}"
    env = {
        **os.environ,
        "WINEARCH": wine_arch,
        "WINEPREFIX": wine_prefix,
        "WINEDEBUG": "-all",
    }
    with _wine_locks[target_abi]:
        return subprocess.run(
            ["wine", str(binary_path)],
            capture_output=True,
            text=True,
            timeout=60,
            env=env,
            cwd=str(binary_path.parent),
        )


def decode_reference_binary(req: VerifyRequest) -> bytes | None:
    if not req.reference_binary_b64:
        return None
    pe_bytes = base64.b64decode(req.reference_binary_b64, validate=True)
    digest = hashlib.sha256(pe_bytes).hexdigest()
    if digest != req.reference_binary_sha256:
        raise ValueError(
            f"reference_binary_sha256 mismatch: declared {req.reference_binary_sha256}, "
            f"actual {digest}"
        )
    return pe_bytes


def select_subject(req: VerifyRequest, pe_bytes: bytes | None) -> str:
    if pe_bytes is not None and req.function_addr:
        return ORACLE_SUBJECT_ORIGINAL_BINARY
    return ORACLE_SUBJECT_SOURCE_RECOMPILE


def probe_fixture(
    req: VerifyRequest,
    *,
    subject: str,
    pe_bytes: bytes | None,
    compiler: str,
    target_abi: str,
    wine_arch: str,
    runner: str,
    root: Path,
) -> bool:
    """Reference self-check: known-good candidate must score 1.0 under the same ABI.

    Used so candidate compile/runtime/timeout failures still produce *valid*
    harness identity evidence when the PE/wrapper fixture itself is sound.
    """
    try:
        if subject == ORACLE_SUBJECT_ORIGINAL_BINARY:
            # PE-anchored reference cannot be recompiled as C; probe via
            # source_recompile of the reference body as both sides.
            probe_source = build_source(
                req,
                subject=ORACLE_SUBJECT_SOURCE_RECOMPILE,
                pe_bytes=None,
                candidate_code=req.reference_code,
            )
        else:
            probe_source = build_source(
                req,
                subject=subject,
                pe_bytes=pe_bytes,
                candidate_code=req.reference_code,
            )
        probe_compile, probe_binary = compile_program(
            compiler, probe_source, root, runner=runner
        )
        if probe_compile.returncode != 0:
            return False
        probe_execution = execute_program(
            probe_binary, target_abi, wine_arch, runner=runner
        )
        if probe_execution.returncode != 0:
            return False
        probe_result = parse_differential_output(probe_execution.stdout, len(req.cases))
        return probe_result.score == 1.0
    except Exception:
        return False


def build_source(
    req: VerifyRequest,
    *,
    subject: str,
    pe_bytes: bytes | None,
    pe_path: str = "reference.exe",
    candidate_code: str | None = None,
) -> str:
    candidate = candidate_code if candidate_code is not None else req.candidate_code
    if subject == ORACLE_SUBJECT_ORIGINAL_BINARY:
        assert pe_bytes is not None and req.function_addr
        return build_original_binary_translation_unit(
            req.function_name,
            req.reference_code,
            candidate,
            req.cases,
            function_addr=req.function_addr,
            pe_bytes=pe_bytes,
            pe_path=pe_path,
        )
    return build_differential_translation_unit(
        req.function_name,
        req.reference_code,
        candidate,
        req.cases,
    )


def build_evidence(
    req: VerifyRequest,
    *,
    source: str,
    target_abi: str,
    compiler: str,
    subject: str,
    valid: bool,
    runner: str = "wine",
    function_rva: int | None = None,
) -> dict:
    runner_bin = {
        "wine": "wine",
        "native": "native",
        "qemu": "qemu-aarch64-static",
    }.get(runner, runner)
    evidence = {
        "mode": "differential",
        "valid": valid,
        "oracle_subject": subject,
        "target_abi": target_abi,
        "compiler": compiler,
        "compiler_version": command_version(compiler),
        "runner": runner,
        "runner_version": (
            command_version(runner_bin) if runner_bin not in {"native"} else "host-exec"
        ),
        "wrapper_sha256": wrapper_sha256(req.cases),
        "reference_binary_sha256": req.reference_binary_sha256,
        "translation_unit_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
    }
    if subject == ORACLE_SUBJECT_ORIGINAL_BINARY:
        evidence["function_addr"] = req.function_addr
        if function_rva is not None:
            evidence["function_rva"] = f"0x{function_rva:x}"
    return evidence


@app.get("/health")
def health() -> dict:
    profiles = {}
    for variant in ("gcc -O0", "gcc-m32 -O0", "gcc-elf -O0", "gcc-aarch64 -O0"):
        target, compiler, _, runner = compiler_profile(variant)
        profiles[target] = {
            "compiler": compiler,
            "version": command_version(compiler),
            "runner": runner,
        }
    return {
        "status": "ok",
        "decompiler": "oracle",
        "service": "differential-oracle",
        "runner": "wine+native+qemu",
        "subjects": [ORACLE_SUBJECT_ORIGINAL_BINARY, ORACLE_SUBJECT_SOURCE_RECOMPILE],
        "profiles": profiles,
    }


@app.post("/verify")
def verify(req: VerifyRequest) -> dict:
    try:
        ref_bytes = decode_reference_binary(req)
    except Exception as exc:
        return {
            "score": 0.0,
            "category": "fixture_error",
            "error": str(exc),
            "cases_passed": 0,
            "cases_total": len(req.cases),
            "evidence": {"valid": False},
        }

    target_abi, compiler, wine_arch, runner = compiler_profile(
        req.compiler_variant,
        target_abi=req.target_abi,
        binary_format=req.binary_format,
        ref_bytes=ref_bytes,
    )

    # PE original_binary loader only works for MZ PE. ELF falls back to source
    # recompile under native/qemu linux ABI (honest until ELF call harness exists).
    subject = select_subject(req, ref_bytes)
    if subject == ORACLE_SUBJECT_ORIGINAL_BINARY and not is_pe_bytes(ref_bytes):
        subject = ORACLE_SUBJECT_SOURCE_RECOMPILE

    function_rva = None
    source = ""
    try:
        if subject == ORACLE_SUBJECT_ORIGINAL_BINARY:
            from runner.differential_oracle import function_addr_to_rva

            assert ref_bytes is not None and req.function_addr
            function_rva = function_addr_to_rva(ref_bytes, req.function_addr)
        source = build_source(req, subject=subject, pe_bytes=ref_bytes)
        build_error: str | None = None
    except Exception as exc:
        # Candidate rename / TU assembly can fail on synthetic names. That is a
        # *quality/boundary* issue once the PE fixture itself is sound — not a
        # missing harness identity.
        source = f"/* build_source failed: {exc} */\n"
        build_error = str(exc)

    def _fail(category: str, error: str, *, source_text: str = "") -> dict:
        # Probe in a sibling dir so candidate debris cannot poison the fixture.
        with tempfile.TemporaryDirectory(prefix="fission-oracle-probe-") as probe_dir:
            fixture_valid = probe_fixture(
                req,
                subject=subject,
                pe_bytes=ref_bytes,
                compiler=compiler,
                target_abi=target_abi,
                wine_arch=wine_arch,
                runner=runner,
                root=Path(probe_dir),
            )
        # Prefer boundary_mismatch for rename failures when fixture is sound.
        cat = category
        if fixture_valid and "not found" in (error or "").lower():
            cat = "boundary_mismatch"
        elif not fixture_valid:
            cat = "fixture_error"
        return {
            "score": 0.0,
            "category": cat if fixture_valid else "fixture_error",
            "error": error,
            "cases_passed": 0,
            "cases_total": len(req.cases),
            "evidence": build_evidence(
                req,
                source=source_text or source or "/* empty */\n",
                target_abi=target_abi,
                compiler=compiler,
                subject=subject,
                valid=fixture_valid,
                runner=runner,
                function_rva=function_rva,
            ),
        }

    if build_error is not None:
        return _fail("boundary_mismatch", build_error, source_text=source)

    with tempfile.TemporaryDirectory(prefix="fission-oracle-") as directory:
        root = Path(directory)
        if ref_bytes is not None and subject == ORACLE_SUBJECT_ORIGINAL_BINARY:
            (root / "reference.exe").write_bytes(ref_bytes)

        try:
            compile_result, binary_path = compile_program(
                compiler, source, root, runner=runner
            )
        except subprocess.TimeoutExpired:
            return _fail("timeout", "oracle compile timed out")
        if compile_result.returncode != 0:
            error = (compile_result.stderr or compile_result.stdout)[-4000:]
            return _fail("compile_error", error)

        try:
            execution = execute_program(
                binary_path, target_abi, wine_arch, runner=runner
            )
        except subprocess.TimeoutExpired:
            return _fail("timeout", "oracle execution timed out")
        except FileNotFoundError as exc:
            return _fail("fixture_error", f"oracle runner missing: {exc}")
        if execution.returncode != 0:
            error = (execution.stderr or execution.stdout)[-4000:]
            return _fail("runtime_error", error)

        result = parse_differential_output(execution.stdout, len(req.cases))
        # Candidate crashes / empty CASE streams are decompiler failures when the
        # PE fixture self-check still scores 1.0 — keep harness identity valid.
        if result.category in {"fixture_error", "runtime_error"}:
            return _fail(result.category, result.error or result.category)
        evidence = build_evidence(
            req,
            source=source,
            target_abi=target_abi,
            compiler=compiler,
            subject=subject,
            valid=True,
            runner=runner,
            function_rva=function_rva,
        )
        return {
            "score": result.score,
            "category": result.category,
            "error": result.error,
            "cases_passed": result.cases_passed,
            "cases_total": result.cases_total,
            "evidence": evidence,
        }
