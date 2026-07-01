"""Helpers for binary-level benchmark subjects."""
from __future__ import annotations

from dataclasses import replace

from benchmark.common.schema import BenchmarkSubject
from benchmark.common.subjects import load_subjects


def load_binary_subjects(split: str) -> list[BenchmarkSubject]:
    seen: set[tuple[str, str, str]] = set()
    result: list[BenchmarkSubject] = []
    for subject in load_subjects(split):
        key = (subject.binary, subject.compiler, subject.opt)
        if key in seen:
            continue
        seen.add(key)
        result.append(replace(subject, function="*", addr="0x0"))
    return result
