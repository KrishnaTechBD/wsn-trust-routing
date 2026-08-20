# Reproducibility Protocol

## Artifact principle

The repository distinguishes code, configuration, raw data, derived data, and source-derived paper figures. A reproducible result must be generated from the code and the raw per-run archive, not from aggregate values copied from the PDF.

## Required author archive

The final archive should include the exact NS-3.40 source or a commit-pinned external repository, build instructions, `experiment_template.yaml` completed with actual values, `seed_manifest.csv`, topology/attack-placement files, raw per-run outputs, node-level trust/detection logs, and scripts that map raw outputs to manuscript tables and figures.

## Verification sequence

1. Run the unit tests with `pytest -q`.
2. Run raw-data validation and save `results/validation_report.json`.
3. Inspect every error and warning; do not silently drop rows.
4. Generate `results/raw_run_summary.csv` from the raw rows.
5. Generate figures in `figures/`.
6. Compare generated values with the manuscript table within a documented tolerance.
7. Record software versions, operating system, simulator commit, random seed manifest, and analysis commit.
8. Archive the final repository and raw data with a persistent version identifier.

## Data-availability statement template

> The code, exact experiment configuration, seed manifest, raw per-run outputs, and analysis scripts used to generate the tables and figures are available at [persistent URL] under release [version]. The repository records the simulator version, software dependencies, and excluded-run policy.

Do not use this statement until the listed artifacts are actually deposited.
