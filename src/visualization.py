"""Visualization helper functions for the auditor resignation event study."""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd


def plot_average_abnormal_returns(aar: pd.Series, title: str = "Average Abnormal Returns"):
    """Plot average abnormal returns by event time."""
    fig, ax = plt.subplots(figsize=(8, 5))
    aar.plot(ax=ax, marker="o")
    ax.axvline(0, linestyle="--")
    ax.set_title(title)
    ax.set_xlabel("Event Time")
    ax.set_ylabel("Average Abnormal Return")
    fig.tight_layout()
    return fig, ax


def plot_car_by_group(df: pd.DataFrame, group_col: str, car_col: str):
    """Plot average CAR by group."""
    grouped = df.groupby(group_col)[car_col].mean().sort_values()
    fig, ax = plt.subplots(figsize=(8, 5))
    grouped.plot(kind="bar", ax=ax)
    ax.set_title(f"Average {car_col} by {group_col}")
    ax.set_xlabel(group_col)
    ax.set_ylabel(f"Average {car_col}")
    fig.tight_layout()
    return fig, ax
