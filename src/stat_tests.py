"""Statistical tests for event-study outputs.

These functions provide first-pass tests for cumulative abnormal returns.
Some tests are simplified and should be reviewed before journal submission.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats


def one_sample_t_test(values: pd.Series, popmean: float = 0.0) -> dict:
    """Run a one-sample t-test against a population mean."""
    clean = pd.Series(values).dropna()
    if clean.empty:
        return {"n": 0, "mean": np.nan, "t_stat": np.nan, "p_value": np.nan}
    t_stat, p_value = stats.ttest_1samp(clean, popmean=popmean)
    return {
        "n": int(clean.shape[0]),
        "mean": float(clean.mean()),
        "t_stat": float(t_stat),
        "p_value": float(p_value),
    }


def sign_test(values: pd.Series, expected_positive_share: float = 0.5) -> dict:
    """Run a binomial sign test for whether positive/negative signs differ from 50/50."""
    clean = pd.Series(values).dropna()
    clean = clean[clean != 0]
    n = int(clean.shape[0])
    positives = int((clean > 0).sum())
    negatives = int((clean < 0).sum())

    if n == 0:
        return {"n": 0, "positives": 0, "negatives": 0, "p_value": np.nan}

    result = stats.binomtest(positives, n=n, p=expected_positive_share, alternative="two-sided")
    return {
        "n": n,
        "positives": positives,
        "negatives": negatives,
        "p_value": float(result.pvalue),
    }


def patell_placeholder() -> str:
    """Placeholder note for Patell standardized residual test implementation."""
    return "Patell test requires standardized abnormal returns and estimation-window residual variance."


def bmp_placeholder() -> str:
    """Placeholder note for BMP test implementation."""
    return "BMP test requires cross-sectional standardization of event-period abnormal returns."
