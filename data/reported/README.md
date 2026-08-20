# Reported manuscript values

`reported_results_summary.csv` contains aggregate values transcribed from the supplied ActiveTrust PDF. Every row is marked `reported_not_regenerated`.

These values are retained for traceability and manuscript reconciliation only. They are not raw observations and must not be fed into the raw-run analysis pipeline as if they were 50 independent runs.

When the real archive is supplied, generated values should be written to `results/` with a separate provenance record containing the raw-data hash, code commit, configuration hash, and seed manifest.
