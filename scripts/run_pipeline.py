#!/usr/bin/env python3
"""Run the auditable ActiveTrust data pipeline.

Examples:
  python scripts/run_pipeline.py validate --input data/raw/raw_runs.csv
  python scripts/run_pipeline.py summarize --input data/raw/raw_runs.csv --output results/summary.csv
  python scripts/run_pipeline.py plot --input data/raw/raw_runs.csv --output-dir figures
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from activetrust_analysis.metrics import write_summary
from activetrust_analysis.plots import generate_all
from activetrust_analysis.validate import load_and_validate, write_report


def validate_command(args: argparse.Namespace) -> int:
    frame, issues = load_and_validate(args.input)
    write_report(args.report, args.input, frame, issues)
    for issue in issues:
        location = f"row={issue.row} " if issue.row is not None else ""
        print(f"{issue.severity.upper()}: {location}{issue.column or ''} {issue.message}")
    if frame.empty:
        print("PENDING: raw dataset contains zero rows; add the real experiment archive before reporting regenerated results")
    return 1 if any(issue.severity == "error" for issue in issues) else 0


def summarize_command(args: argparse.Namespace) -> int:
    frame, issues = load_and_validate(args.input)
    if any(issue.severity == "error" for issue in issues):
        print("ERROR: validation failed; summary was not generated", file=sys.stderr)
        return 1
    if frame.empty:
        print("PENDING: raw dataset is empty; no summary was generated", file=sys.stderr)
        return 2
    write_summary(args.input, args.output)
    print(f"WROTE: {args.output}")
    return 0


def plot_command(args: argparse.Namespace) -> int:
    frame, issues = load_and_validate(args.input)
    if any(issue.severity == "error" for issue in issues):
        print("ERROR: validation failed; figures were not generated", file=sys.stderr)
        return 1
    if frame.empty:
        print("PENDING: raw dataset is empty; no experimental figures were generated", file=sys.stderr)
        return 2
    for output in generate_all(frame, args.output_dir):
        print(f"WROTE: {output}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    validate = sub.add_parser("validate")
    validate.add_argument("--input", required=True)
    validate.add_argument("--report", default="results/validation_report.json")
    validate.set_defaults(func=validate_command)
    summarize = sub.add_parser("summarize")
    summarize.add_argument("--input", required=True)
    summarize.add_argument("--output", default="results/raw_run_summary.csv")
    summarize.set_defaults(func=summarize_command)
    plot = sub.add_parser("plot")
    plot.add_argument("--input", required=True)
    plot.add_argument("--output-dir", default="figures")
    plot.set_defaults(func=plot_command)
    return parser


if __name__ == "__main__":
    args = build_parser().parse_args()
    raise SystemExit(args.func(args))
