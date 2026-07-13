# Program metadata parity baseline

Date: 2026-07-13
Reference: Ghidra 12.0.3
Candidate: local Fission main after v0.1.2
Corpus row: `control_flow_gcc_O0.exe`

This is a diagnostic baseline, not a quality ranking. Both adapters loaded the
same PE and exported whole-program metadata directly.

| Fact family | Fission | Ghidra | Agreement |
|---|---:|---:|---:|
| Binary identity | 1 | 1 | 100.00% |
| Memory block exact span + permissions | 19 | 20 | 95.00% Jaccard |
| Memory block start + permissions | 19 | 20 | 95.00% Jaccard |
| Function entry addresses | 107 | 84 | 59.17% Jaccard |
| Symbol addresses | 144 | 864 | 16.67% Jaccard |
| Relocation addresses | 46 | 47 | 93.75% Jaccard |

The initial memory-span score was 2.63% because Fission exposed PE
`VirtualSize` while Ghidra exposed mapped size. Defining mapped size as
`max(VirtualSize, SizeOfRawData)` raised exact span agreement to 95%. The
remaining difference is Ghidra's explicit header block, which belongs to the
loader rather than the parity normalizer.

The function and symbol differences are real analysis-input gaps or policy
differences and should be triaged before broad CFG structuring changes. The next
implementation slices are:

1. expose the PE header block from the loader;
2. classify Ghidra/Fission function provenance before removing false positives;
3. recover imported/debug/source symbols into typed symbol records;
4. close the single remaining relocation-address gap.
