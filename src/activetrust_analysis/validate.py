"""Validation for author-supplied ActiveTrust raw-run CSV files."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd

from .schema import NONNEGATIVE_COLUMNS, PERCENT_COLUMNS, REQUIRED_COLUMNS, ValidationIssue, missing_columns


def validate_dataframe(frame: pd.DataFrame) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    missing = missing_columns(frame.columns)
    for column in missing:
        issues.append(ValidationIssue("error", None, column, "required column is missing"))
    if missing:
        return issues

    for column in NONNEGATIVE_COLUMNS:
        values = pd.to_numeric(frame[column], errors="coerce")
        for idx in frame.index[values.isna()]:
            issues.append(ValidationIssue("error", int(idx), column, "value is not numeric"))
        for idx in frame.index[values < 0]:
            issues.append(ValidationIssue("error", int(idx), column, "value must be non-negative"))

    for column in PERCENT_COLUMNS:
        values = pd.to_numeric(frame[column], errors="coerce")
        for idx in frame.index[values.notna() & ((values < 0) | (values > 100))]:
            issues.append(ValidationIssue("error", int(idx), column, "percentage must be in [0, 100]"))

    auc = pd.to_numeric(frame["auc"], errors="coerce")
    for idx in frame.index[auc.notna() & ((auc < 0) | (auc > 1))]:
        issues.append(ValidationIssue("error", int(idx), "auc", "AUC must be in [0, 1]"))

    for column in ["alpha_T", "tau", "p_hat"]:
        values = pd.to_numeric(frame[column], errors="coerce")
        for idx in frame.index[values.notna() & ((values < 0) | (values > 1))]:
            issues.append(ValidationIssue("error", int(idx), column, "probability/weight must be in [0, 1]"))

    failed = frame["failed_run"].astype(str).str.lower().str.strip()
    valid_failed = {"0", "1", "true", "false", "yes", "no", "y", "n"}
    for idx in frame.index[~failed.isin(valid_failed)]:
        issues.append(ValidationIssue("error", int(idx), "failed_run", "use 0/1, true/false, yes/no, or y/n"))

    duplicates = frame.duplicated(subset=["seed", "method", "N", "bha_fraction", "attack_model", "attack_placement"], keep=False)
    for idx in frame.index[duplicates]:
        issues.append(ValidationIssue("warning", int(idx), None, "duplicate run identity; check whether repeated rows are intentional"))

    if frame["seed"].nunique(dropna=True) < 2:
        issues.append(ValidationIssue("warning", None, "seed", "fewer than two unique seeds are present"))
    return issues


def load_and_validate(path: str | Path) -> tuple[pd.DataFrame, list[ValidationIssue]]:
    path = Path(path)
    frame = pd.read_csv(path)
    return frame, validate_dataframe(frame)


def issues_to_dict(issues: list[ValidationIssue]) -> list[dict[str, Any]]:
    return [issue.__dict__ for issue in issues]


def write_report(path: str | Path, source: str | Path, frame: pd.DataFrame, issues: list[ValidationIssue]) -> None:
    payload = {
        "source": str(source),
        "rows": int(len(frame)),
        "columns": list(frame.columns),
        "status": "pass" if not any(issue.severity == "error" for issue in issues) else "fail",
        "pending_raw_data": len(frame) == 0,
        "issues": issues_to_dict(issues),
    }
    Path(path).write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
