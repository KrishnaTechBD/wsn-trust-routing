# Migration from the original repository

## Recommended replacement workflow

1. Create a new branch or a new repository from the refined pack rather than overwriting the original history.
2. Copy the actual NS-3.40 ActiveTrust implementation into a dedicated `simulator/` directory.
3. Complete `configs/experiment_template.yaml` with the exact values used in the paper.
4. Add the seed manifest and raw per-run archive under `data/raw/` or link a persistent external artifact archive.
5. Add simulator-to-schema export code that produces `data/raw/raw_runs.csv` without collapsing runs into means.
6. Run unit tests and the validation command before generating figures.
7. Regenerate all tables and figures from raw data, and replace the source-derived images under `artifacts/source_figures/` with generated outputs under `figures/`.
8. Update the paper’s data-availability statement and repository commit in the Overleaf source.
9. Tag a versioned release and archive the exact code/data/configuration combination used for submission.

## Do not merge without resolving

The original README’s composite trust formula, SecLEACH/Standard LEACH result table, fixed seed policy, and claimed source paths must not be presented as the implementation of the ActiveTrust paper unless the authors can provide the corresponding code and experiments. Keep the repository README, manuscript terminology, baseline names, and dataset fields consistent.
