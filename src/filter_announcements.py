"""Filter public corporate announcement files for auditor resignation candidates.

This script is designed for semi-automated data collection. It reads CSV files
exported from public NSE/BSE announcement search pages and filters rows that
likely relate to statutory auditor resignations.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd

AUDITOR_RESIGNATION_KEYWORDS = [
    "resignation of statutory auditor",
    "resignation of statutory auditors",
    "statutory auditor resignation",
    "resignation of auditor",
    "resignation of auditors",
    "auditor resignation",
    "change in statutory auditor",
    "regulation 30 auditor",
]


def load_announcement_csvs(input_dir: str | Path) -> pd.DataFrame:
    """Load all CSV files from a directory into one dataframe."""
    input_path = Path(input_dir)
    files = sorted(input_path.glob("*.csv"))
    if not files:
        raise FileNotFoundError(f"No CSV files found in {input_path}")

    frames = []
    for file in files:
        df = pd.read_csv(file)
        df["source_file"] = file.name
        frames.append(df)

    return pd.concat(frames, ignore_index=True)


def normalize_text(value) -> str:
    """Normalize a cell value for keyword matching."""
    if pd.isna(value):
        return ""
    return str(value).lower().strip()


def filter_auditor_resignation_candidates(
    df: pd.DataFrame,
    text_columns: Iterable[str] | None = None,
) -> pd.DataFrame:
    """Filter rows likely related to auditor resignation events.

    If text_columns is None, all object/string columns are searched.
    """
    data = df.copy()

    if text_columns is None:
        text_columns = [col for col in data.columns if data[col].dtype == "object"]

    combined_text = pd.Series("", index=data.index)
    for col in text_columns:
        if col in data.columns:
            combined_text = combined_text + " " + data[col].map(normalize_text)

    pattern = "|".join(AUDITOR_RESIGNATION_KEYWORDS)
    mask = combined_text.str.contains(pattern, regex=True, na=False)

    candidates = data.loc[mask].copy()
    candidates["matched_text"] = combined_text.loc[mask]
    candidates["manual_review_required"] = 1
    return candidates


def save_candidates(input_dir: str | Path, output_file: str | Path) -> pd.DataFrame:
    """Load raw announcement CSVs, filter candidates, and save output CSV."""
    raw = load_announcement_csvs(input_dir)
    candidates = filter_auditor_resignation_candidates(raw)
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    candidates.to_csv(output_path, index=False)
    return candidates


if __name__ == "__main__":
    save_candidates(
        input_dir="data/raw/announcements",
        output_file="data/processed/auditor_resignation_candidates.csv",
    )
