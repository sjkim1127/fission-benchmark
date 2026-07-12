# Multi-ISA track

**Status:** partial — ELF x86_64 fixture built; arm64 needs cross sysroot.

| Fixture | Arch/Format | Notes |
|---------|-------------|-------|
| `hello_elf_x86_64` | x86_64 ELF | structural stages; no PE oracle |

```bash
python scripts/build_extension_corpora.py
```

Do not mix PE and ELF in one official matrix without `target_abi` tagging.
