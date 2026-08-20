# Raw experiment archive

Add the real ActiveTrust per-run archive here as `raw_runs.csv`. The required columns are defined in `raw_run_dataset_schema.csv`.

Each row must represent one independent run for one method, seed, topology/attack configuration, and BHA density. Do not replace run-level rows with aggregate means. The archive must preserve failed runs and exclusions using `failed_run` and `exclusion_reason`.

At minimum, the final archive must be sufficient to regenerate every paper table and figure, including ROC/AUC. Therefore, the authors should also provide node-level or decision-level score logs separately when a single aggregate `auc` value cannot reproduce the ROC curve.

The current directory intentionally contains no fabricated raw rows.
