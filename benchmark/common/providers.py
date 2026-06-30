"""Command-template providers for parity stages."""
from __future__ import annotations

import json
import shlex
import subprocess
from dataclasses import asdict, is_dataclass
from typing import Any

from benchmark.common.schema import BenchmarkSubject


def render_command(template: str, subject: BenchmarkSubject) -> list[str]:
    values = asdict(subject)
    return shlex.split(template.format(**values))


def run_json_provider(template: str, subject: BenchmarkSubject, timeout: float) -> Any:
    cmd = render_command(template, subject)
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    if result.returncode != 0:
        stderr = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(stderr or f"provider exited with {result.returncode}")
    return json.loads(result.stdout)


def canonicalize(value: Any) -> Any:
    if is_dataclass(value):
        value = asdict(value)
    if isinstance(value, dict):
        return {str(k): canonicalize(v) for k, v in sorted(value.items())}
    if isinstance(value, list):
        return [canonicalize(v) for v in value]
    if isinstance(value, str):
        return value.strip().lower()
    return value
