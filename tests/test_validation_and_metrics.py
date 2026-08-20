import pandas as pd

from activetrust_analysis.metrics import mean_ci, summarize
from activetrust_analysis.schema import REQUIRED_COLUMNS
from activetrust_analysis.validate import validate_dataframe


def minimal_frame() -> pd.DataFrame:
    row = {column: 0 for column in REQUIRED_COLUMNS}
    row.update({
        "method": "ActiveTrust",
        "attack_model": "black-hole",
        "attack_placement": "random",
        "bha_fraction": 0.10,
        "pdr_percent": 94.3,
        "auc": 0.983,
        "failed_run": 0,
    })
    return pd.DataFrame([row])


def test_valid_minimal_frame_has_no_errors():
    issues = validate_dataframe(minimal_frame())
    assert not any(issue.severity == "error" for issue in issues)


def test_percentage_range_is_checked():
    frame = minimal_frame()
    frame.loc[0, "pdr_percent"] = 120
    issues = validate_dataframe(frame)
    assert any(issue.column == "pdr_percent" and issue.severity == "error" for issue in issues)


def test_mean_ci_single_observation_is_explicitly_unestimated():
    mean, half_width, n = mean_ci(pd.Series([5.0]))
    assert mean == 5.0
    assert n == 1
    assert half_width != half_width  # NaN


def test_summary_groups_by_method_and_condition():
    frame = pd.concat([minimal_frame(), minimal_frame()], ignore_index=True)
    frame.loc[1, "seed"] = 2
    result = summarize(frame, metrics=["pdr_percent"])
    assert len(result) == 1
    assert result.iloc[0]["metric"] == "pdr_percent"
    assert result.iloc[0]["n"] == 2
