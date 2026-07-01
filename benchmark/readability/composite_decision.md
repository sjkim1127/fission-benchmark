# Readability Composite Decision Record

Status: not yet established.

The dashboard must not expose a final readability composite until the human
study in `human_study.md` is executed and analyzed.

## Phase 4 Rule

After the study:

1. Exclude proxies that have no useful correlation with comprehension accuracy
   or response time.
2. Exclude proxies whose direction is reversed under the study outcome.
3. Assign weights only to surviving proxies.
4. Set each weight proportional to the absolute validated effect size or
   correlation magnitude.
5. Publish the formula here before adding a `readability_score` field.

Correctness and readability remain separate dashboard axes:

- Correctness: `semantic_score` and the existing semantic-gated composite.
- Readability: future validated Phase 4 composite only.

## Phase 5 LLM Judge Gate

LLM judging is optional and can only be evaluated after the human gold set
exists. If attempted, it must use pairwise comparisons, A/B order reversal, and
agreement reporting against the human gold set. If agreement is weak, the LLM
judge is not adopted.
