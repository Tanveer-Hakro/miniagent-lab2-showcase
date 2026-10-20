# Verification and Observed Results

[← Repository overview](../README.md)

The following counts are derived from the completed project's verification output, not an automated test running in this public repository. Source counts are recorded in [`data/metrics.json`](../data/metrics.json).

## Acceptance verifier

![Verification metrics](../assets/verification-metrics.svg)

| Metric | Variant A | Variant B |
|---|---:|---:|
| Checks passed | **11/11** | **11/11** |
| Interaction rounds | **8** | **7** |
| Structured JSONL audit created | Yes | Yes |
| Tools `read_file`, `write_file`, `run_bash` genuinely invoked | Yes | Yes |
| Write approval recorded | Yes | Yes |
| Normal finish | Yes | Yes |
| Matrix generated and checker passed | Yes | Yes |
| Layer swap remained correct | Yes | Yes |

These 11 checks are the teacher's full verifier totals. The individual yes/no rows above summarize selected verification dimensions; they are **not** additional independent tests.

## Matrix checker

The task requires shape `10×10×10`, cell values `100i + 10j + k + 1`, and valid XY, YZ, XZ views. A separate generated run passed **5/5** checks both with `layer=0` and `layer=5`.

![Matrix planes](../assets/matrix-planes.svg)

The colored cells are calculated directly from the target formula. This visualization is a clean representation of the underlying numeric task, not a captured runtime screenshot.

## Evidence boundaries

- The verifier results and 5/5 layer checks are **observed**, not synthetic metrics.
- The diagrams and charts are **reconstructed from those observed counts**. They do not imply full source-code reproducibility.
- The public showcase intentionally omits grader code, teacher fixture files, raw agent traces, personal data, and API credentials.

[How the feedback experiment was conducted →](feedback-experiment.md)
