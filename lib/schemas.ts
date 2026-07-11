import { z } from "zod";

export const CoverageSchema = z.object({
  attempted: z.number(),
  clean: z.number(),
  ratio: z.number(),
});

export const ValiditySchema = z.object({
  valid: z.boolean(),
  publishable: z.boolean(),
  matrix_valid: z.boolean().optional(),
  adapter_output_valid: z.boolean().optional(),
  semantic_harness_valid: z.boolean().optional(),
  semantic_coverage_valid: z.boolean().optional(),
  semantic_result_valid: z.boolean().optional(),
  provenance_valid: z.boolean().optional(),
  artifact_valid: z.boolean().optional(),
  official_profile_valid: z.boolean().optional(),
  holdout_valid: z.boolean().optional(),
  fission_coverage: z.number().optional(),
  fission_attempted: z.number().optional(),
  fission_clean: z.number().optional(),
  backend_coverage: z.number().optional(),
  backend_attempted: z.number().optional(),
  backend_clean: z.number().optional(),
  reasons: z.array(z.string()).optional().default([]),
  publish_reasons: z.array(z.string()).optional().default([]),
});

export const RunMetaSchema = z.object({
  started_at: z.string().optional(),
  finished_at: z.string().optional(),
  duration_ms: z.number().optional(),
  runner_commit: z.string().optional(),
  corpus: z.string().optional(),
  official: z.boolean().optional(),
  run_id: z.string().optional(),
  fission_version: z.string().optional(),
  fission_source: z.string().optional(),
  legacy_source: z.boolean().optional(),
});

export const MatrixSchema = z.object({
  expected_decompilers: z.array(z.string()).optional(),
  expected_cells: z.array(z.record(z.string(), z.unknown())).optional(),
  expected_rows: z.number().optional(),
  observed_rows: z.number().optional(),
});

export const RowSchema = z.object({
  decompiler: z.string(),
  function_name: z.string(),
  compiler_variant: z.string().optional().default(""),
  binary: z.string().optional(),
  addr: z.string().optional(),
  source_similarity: z.number().default(0),
  semantic_score: z.number().nullable().default(null),  // null = no_wrapper (untestable)
  correctness_score: z.number().nullable().default(null),  // null = no_wrapper
  correctness_rank: z.number().int().nullable().optional(),
  goto_count: z.number().default(0),
  nesting_depth: z.number().default(0),
  time_ms: z.number().default(0),
  error: z.string().nullable().optional(),
  fail_category: z.string().nullable().optional(),
  decompiled_code: z.string().optional(),
  semantic_error: z.string().nullable().optional(),
  uses_intrinsics: z.boolean().optional(),
});

export const ToolchainSchema = z.object({
  fission_version: z.string().optional(),
  runner_commit: z.string().optional(),
  runner_os: z.string().optional(),
  python_version: z.string().optional(),
  ci: z.string().optional(),
  github_run_id: z.string().optional(),
  github_actor: z.string().optional(),
});

export const BenchmarkEnvelopeSchema = z.object({
  schema_version: z.number().optional(),
  run: RunMetaSchema.optional(),
  toolchain: ToolchainSchema.optional(),
  matrix: MatrixSchema.optional(),
  validity: ValiditySchema.optional(),
  rows: z.array(RowSchema),
});

export type BenchmarkEnvelope = z.infer<typeof BenchmarkEnvelopeSchema>;
export type Row = z.infer<typeof RowSchema>;
export type Validity = z.infer<typeof ValiditySchema>;
export type RunMeta = z.infer<typeof RunMetaSchema>;
export type Toolchain = z.infer<typeof ToolchainSchema>;
