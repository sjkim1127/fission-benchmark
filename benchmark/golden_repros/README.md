# Golden Repros

Runs fixed regression canaries outside the broad corpus. Use this for narrow
bugs that must never regress, such as shared-token displacement cursoring or
COPY-before-STORE p-code materialization.

Manifest format:

```json
{
  "cases": [
    {
      "name": "sib_stack_disp8_copy_store",
      "binary": "corpus/dev/binaries/example",
      "function": "example",
      "addr": "0x401000",
      "arch": "x86_64",
      "compiler": "gcc",
      "opt": "-O2",
      "command": "python tools/fission_pcode.py {binary} {addr}",
      "expected": [{"op": "INT_ADD"}, {"op": "COPY"}, {"op": "STORE"}]
    }
  ]
}
```
