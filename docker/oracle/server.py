"""Target-ABI differential semantic oracle service."""
from __future__ import annotations

import hashlib
import os
import subprocess
import tempfile
import threading
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel, Field

from runner.differential_oracle import (
    build_differential_translation_unit,
    parse_differential_output,
    wrapper_sha256,
)

app = FastAPI(title="fission-differential-oracle", version="1.0")
_wine_locks = {"windows-x86_64": threading.Lock(), "windows-x86": threading.Lock()}


class VerifyRequest(BaseModel):
    function_name: str = Field(min_length=1)
    reference_code: str = Field(min_length=1)
    candidate_code: str = Field(min_length=1)
    cases: list[str] = Field(min_length=1)
    compiler_variant: str = Field(min_length=1)
    reference_binary_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")


def compiler_profile(variant: str) -> tuple[str, str, str]:
    if "-m32" in variant:
        return "windows-x86", "i686-w64-mingw32-gcc", "win32"
    return "windows-x86_64", "x86_64-w64-mingw32-gcc", "win64"


def command_version(command: str) -> str:
    return subprocess.check_output([command, "--version"], text=True).splitlines()[0]


def compile_program(compiler: str, source: str, root: Path) -> tuple[subprocess.CompletedProcess[str], Path]:
    source_path = root / "oracle.c"
    binary_path = root / "oracle.exe"
    source_path.write_text(source, encoding="utf-8")
    result = subprocess.run(
        [compiler, "-std=c11", "-O0", "-w", str(source_path), "-o", str(binary_path)],
        capture_output=True,
        text=True,
        timeout=60,
    )
    return result, binary_path


def execute_program(binary_path: Path, target_abi: str, wine_arch: str) -> subprocess.CompletedProcess[str]:
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
        )


def build_evidence(
    req: VerifyRequest,
    *,
    source: str,
    target_abi: str,
    compiler: str,
    valid: bool,
) -> dict:
    return {
        "mode": "differential",
        "valid": valid,
        "oracle_subject": "source_recompile",
        "target_abi": target_abi,
        "compiler": compiler,
        "compiler_version": command_version(compiler),
        "runner": "wine",
        "runner_version": command_version("wine"),
        "wrapper_sha256": wrapper_sha256(req.cases),
        "reference_binary_sha256": req.reference_binary_sha256,
        "translation_unit_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
    }


@app.get("/health")
def health() -> dict:
    profiles = {}
    for variant in ("gcc -O0", "gcc-m32 -O0"):
        target, compiler, _ = compiler_profile(variant)
        profiles[target] = {"compiler": compiler, "version": command_version(compiler)}
    return {
        "status": "ok",
        "decompiler": "oracle",
        "service": "differential-oracle",
        "runner": "wine",
        "profiles": profiles,
    }


@app.post("/verify")
def verify(req: VerifyRequest) -> dict:
    target_abi, compiler, wine_arch = compiler_profile(req.compiler_variant)
    try:
        source = build_differential_translation_unit(
            req.function_name,
            req.reference_code,
            req.candidate_code,
            req.cases,
        )
    except ValueError as exc:
        return {"score": 0.0, "category": "fixture_error", "error": str(exc), "cases_passed": 0, "cases_total": len(req.cases), "evidence": {"valid": False}}

    with tempfile.TemporaryDirectory(prefix="fission-oracle-") as directory:
        root = Path(directory)
        try:
            compile_result, binary_path = compile_program(compiler, source, root)
        except subprocess.TimeoutExpired:
            return {"score": 0.0, "category": "timeout", "error": "oracle compile timed out", "cases_passed": 0, "cases_total": len(req.cases), "evidence": {"valid": False}}
        if compile_result.returncode != 0:
            error = (compile_result.stderr or compile_result.stdout)[-4000:]
            reference_probe = build_differential_translation_unit(
                req.function_name,
                req.reference_code,
                req.reference_code,
                req.cases,
            )
            try:
                probe_compile, probe_binary = compile_program(compiler, reference_probe, root)
                probe_execution = (
                    execute_program(probe_binary, target_abi, wine_arch)
                    if probe_compile.returncode == 0
                    else None
                )
            except subprocess.TimeoutExpired:
                probe_compile, probe_execution = None, None
            probe_result = (
                parse_differential_output(probe_execution.stdout, len(req.cases))
                if probe_execution is not None and probe_execution.returncode == 0
                else None
            )
            fixture_valid = bool(
                probe_compile is not None
                and probe_compile.returncode == 0
                and probe_result is not None
                and probe_result.score == 1.0
            )
            return {
                "score": 0.0,
                "category": "compile_error" if fixture_valid else "fixture_error",
                "error": error,
                "cases_passed": 0,
                "cases_total": len(req.cases),
                "evidence": build_evidence(
                    req,
                    source=source,
                    target_abi=target_abi,
                    compiler=compiler,
                    valid=fixture_valid,
                ),
            }

        try:
            execution = execute_program(binary_path, target_abi, wine_arch)
        except subprocess.TimeoutExpired:
            return {"score": 0.0, "category": "timeout", "error": "oracle execution timed out", "cases_passed": 0, "cases_total": len(req.cases), "evidence": {"valid": False}}
        if execution.returncode != 0:
            error = (execution.stderr or execution.stdout)[-4000:]
            return {"score": 0.0, "category": "runtime_error", "error": error, "cases_passed": 0, "cases_total": len(req.cases), "evidence": {"valid": False}}

    result = parse_differential_output(execution.stdout, len(req.cases))
    evidence_valid = result.category != "fixture_error" and result.category != "runtime_error"
    evidence = build_evidence(
        req,
        source=source,
        target_abi=target_abi,
        compiler=compiler,
        valid=evidence_valid,
    )
    return {
        "score": result.score,
        "category": result.category,
        "error": result.error,
        "cases_passed": result.cases_passed,
        "cases_total": result.cases_total,
        "evidence": evidence,
    }
