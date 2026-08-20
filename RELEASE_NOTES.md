# ActiveTrust GitHub  — Release Notes

## Included in version 0.1.0

This release replaces the original documentation-only repository layout with a reproducibility-oriented structure. It adds a canonical raw-run schema, strict validation rules, confidence-interval summary statistics, raw-data-only figure generation, unit tests, a CLI, experiment configuration template, CI workflow, citation metadata, provenance documentation, and the prior IEEE review/audit materials.

The paper-reported aggregate table is retained separately under `data/reported/` and marked `reported_not_regenerated`. The eight figures extracted from the supplied PDF are retained under `artifacts/source_figures/` only for provenance and manuscript comparison.

## Verification performed

| Check | Result |
|---|---|
| Unit tests | 4 passed |
| Editable install | Passed |
| Python compilation | Passed |
| Schema validation | Passed with pending-data warning |
| Raw experiment regeneration | Not performed; raw archive is absent |
| Public Git history audit | Completed; ActiveTrust implementation/data not found |

## Author actions before publication

The authors must add the actual NS-3.40 implementation, seed manifest, completed experiment configuration, raw per-run archive, attack state machines, node-level trust/detection logs, and scripts that regenerate every manuscript table and figure. After adding them, rerun validation, summary, plots, and the IEEE manuscript build. Replace the current source-derived figures with generated figures and update the data-availability statement with a persistent artifact URL.
