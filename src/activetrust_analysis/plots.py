"""Publication-oriented plots generated from validated raw runs."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def _style() -> None:
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update({"font.size": 9, "axes.titlesize": 10, "axes.labelsize": 9, "legend.fontsize": 8})


def plot_metric(frame: pd.DataFrame, metric: str, ylabel: str, output: str | Path, title: str) -> Path:
    if frame.empty:
        raise ValueError("raw dataset is empty; no experimental plot can be generated")
    required = {"method", "bha_fraction", metric}
    missing = required - set(frame.columns)
    if missing:
        raise ValueError(f"missing columns for plot: {sorted(missing)}")
    _style()
    fig, ax = plt.subplots(figsize=(6.2, 3.7), constrained_layout=True)
    summary = frame.groupby(["method", "bha_fraction"], as_index=False)[metric].agg(["mean", "std", "count"]).reset_index()
    for method, group in summary.groupby("method"):
        x = group["bha_fraction"] * 100
        y = group["mean"]
        ax.plot(x, y, marker="o", linewidth=1.8, label=str(method))
        if group["count"].min() > 1:
            ax.fill_between(x, y - group["std"].fillna(0), y + group["std"].fillna(0), alpha=0.15)
    ax.set_xlabel("BHA node fraction (%)")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend(frameon=True)
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return output


def generate_all(frame: pd.DataFrame, output_dir: str | Path) -> list[Path]:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    return [
        plot_metric(frame, "pdr_percent", "Packet delivery ratio (%)", output_dir / "pdr_vs_bha.png", "PDR versus black-hole density"),
        plot_metric(frame, "detection_latency_s", "Detection latency (s)", output_dir / "detection_latency_vs_bha.png", "Detection latency versus black-hole density"),
        plot_metric(frame, "energy_overhead_percent_per_epoch", "Detection-route energy overhead (%/epoch)", output_dir / "energy_overhead_vs_bha.png", "Energy overhead versus black-hole density"),
    ]
