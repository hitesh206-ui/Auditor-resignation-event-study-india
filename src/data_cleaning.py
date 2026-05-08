"""Data cleaning utilities for the auditor resignation event study."""

from __future__ import annotations

import pandas as pd


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Convert column names to snake_case style."""
    cleaned = df.copy()
    cleaned.columns = (
        cleaned.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace("-", "_", regex=False)
    )
    return cleaned


def remove_duplicate_events(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate auditor resignation events by company and announcement date."""
    required = {"company_name", "announcement_date"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    return df.drop_duplicates(subset=["company_name", "announcement_date"], keep="first")


def flag_valid_events(df: pd.DataFrame) -> pd.DataFrame:
    """Create a valid_event_flag based on minimum required event information."""
    cleaned = df.copy()
    required_cols = ["company_name", "announcement_date", "reason_text"]
    cleaned["valid_event_flag"] = cleaned[required_cols].notna().all(axis=1).astype(int)
    return cleaned
