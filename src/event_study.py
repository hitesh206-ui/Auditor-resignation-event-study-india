"""Event study helper functions.

This module contains reusable functions for calculating returns,
estimating market-model parameters, abnormal returns, and cumulative
abnormal returns for auditor resignation event studies.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Tuple

import numpy as np
import pandas as pd
import statsmodels.api as sm


@dataclass
class MarketModelParams:
    alpha: float
    beta: float
    observations: int


def calculate_simple_returns(price_series: pd.Series) -> pd.Series:
    """Calculate simple percentage returns from a price series."""
    return price_series.pct_change()


def calculate_log_returns(price_series: pd.Series) -> pd.Series:
    """Calculate log returns from a price series."""
    return np.log(price_series / price_series.shift(1))


def estimate_market_model(
    stock_returns: pd.Series,
    market_returns: pd.Series,
) -> MarketModelParams:
    """Estimate market-model alpha and beta using OLS.

    Parameters
    ----------
    stock_returns:
        Stock return series for the estimation window.
    market_returns:
        Market return series for the estimation window.
    """
    data = pd.concat([stock_returns, market_returns], axis=1).dropna()
    data.columns = ["stock_return", "market_return"]

    if len(data) < 30:
        raise ValueError("Insufficient observations to estimate market model.")

    x = sm.add_constant(data["market_return"])
    y = data["stock_return"]
    model = sm.OLS(y, x).fit()

    return MarketModelParams(
        alpha=float(model.params["const"]),
        beta=float(model.params["market_return"]),
        observations=int(model.nobs),
    )


def calculate_abnormal_returns(
    stock_returns: pd.Series,
    market_returns: pd.Series,
    alpha: float,
    beta: float,
) -> pd.Series:
    """Calculate abnormal returns using estimated market-model parameters."""
    expected_returns = alpha + beta * market_returns
    return stock_returns - expected_returns


def calculate_car(abnormal_returns: pd.Series, event_window: Iterable[int]) -> float:
    """Calculate cumulative abnormal return for a specified event window.

    The abnormal_returns index should represent event time, e.g. -5, -4, ..., 0, ..., +5.
    """
    return float(abnormal_returns.loc[list(event_window)].sum())


def summarize_car(car_values: pd.Series) -> dict:
    """Return basic CAR summary statistics."""
    clean = car_values.dropna()
    return {
        "n": int(clean.shape[0]),
        "mean": float(clean.mean()),
        "median": float(clean.median()),
        "std": float(clean.std(ddof=1)),
        "min": float(clean.min()),
        "max": float(clean.max()),
    }
