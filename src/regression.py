"""Regression helpers for cross-sectional CAR analysis."""

from __future__ import annotations

from typing import Iterable

import pandas as pd
import statsmodels.api as sm


def run_ols_regression(
    df: pd.DataFrame,
    dependent_var: str,
    independent_vars: Iterable[str],
    add_constant: bool = True,
    robust: bool = True,
):
    """Run OLS regression for CAR cross-sectional analysis.

    Parameters
    ----------
    df:
        Regression dataset.
    dependent_var:
        Dependent variable, e.g. `car_m1_p1`.
    independent_vars:
        Explanatory variables.
    add_constant:
        Whether to add an intercept.
    robust:
        Whether to use heteroskedasticity-robust standard errors.
    """
    vars_needed = [dependent_var] + list(independent_vars)
    data = df[vars_needed].dropna()

    y = data[dependent_var]
    x = data[list(independent_vars)]
    if add_constant:
        x = sm.add_constant(x)

    model = sm.OLS(y, x).fit(cov_type="HC1" if robust else "nonrobust")
    return model


def regression_summary_table(model) -> pd.DataFrame:
    """Convert statsmodels regression output to a compact dataframe."""
    return pd.DataFrame(
        {
            "coef": model.params,
            "std_err": model.bse,
            "t_stat": model.tvalues,
            "p_value": model.pvalues,
        }
    )
