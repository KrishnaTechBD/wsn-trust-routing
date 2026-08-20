"""Statistics computed only from author-supplied raw runs."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

try:
    from scipy.stats import t
except ImportError:  # pragma: no cover
    t = None


def mean_ci(values: pd.Series, confidence: float = 0.95) -> tuple[float, float, int]:
    values = pd.to_numeric(values, errors="coerce").dropna().astype(float)
    n = len(values)
    if n == 0:
        return float("nan"), float("nan"), 0
    mean = float(values.mean())
    if n == 1:
        return mean, float("nan"), 1
    se = float(values.std(ddof=1) / np.sqrt(n))
    if t is not None:
        critical = float(t.ppf((1 + confidence) / 2, n - 1))
    else:
        critical = 1.96
    return mean, critical * se, n


def summarize(frame: pd.DataFrame, metrics: list[str] | None = None) -> pd.DataFrame:
    if frame.empty:
        return pd.DataFrame()
    metrics = metrics or [
        "pdr_percent", "detection_latency_s", "detection_rate_percent",
        "false_positive_rate_percent", "auc", "energy_overhead_percent_per_epoch",
        "first_node_death_epoch",
    ]
    group_columns = ["method", "N", "bha_fraction", "attack_model", "attack_placement"]
    rows: list[dict[str, object]] = []
    for keys, group in frame.groupby(group_columns, dropna=False):
        if not isinstance(keys, tuple):
            keys = (keys,)
        base = dict(zip(group_columns, keys))
        for metric in metrics:
            if metric not in group.columns:
                continue
            mean, half_width, n = mean_ci(group[metric])
            rows.append({**base, "metric": metric, "mean": mean, "ci95_half_width": half_width, "n": n})
    return pd.DataFrame(rows)


def write_summary(input_csv: str | Path, output_csv: str | Path) -> pd.DataFrame:
    frame = pd.read_csv(input_csv)
    result = summarize(frame)
    result.to_csv(output_csv, index=False)
    return result
