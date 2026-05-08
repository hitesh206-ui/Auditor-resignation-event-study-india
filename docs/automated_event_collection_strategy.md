# Automated and Semi-Automated Event Collection Strategy

## Why This Document Exists

The original plan required manual collection of 100-200 auditor resignation events from NSE/BSE announcements. If manual collection is not feasible, the project should use a semi-automated public-data workflow.

## Important Data Reality

Full corporate-announcement feeds from NSE/BSE are typically commercial data products. Public exchange websites provide search and download interfaces, but bulk historical data may not be as straightforward as a paid data feed.

Therefore, this project will use a transparent semi-automated approach:

1. Download or save public corporate announcement search results where possible.
2. Use Python to filter rows containing auditor-resignation keywords.
3. Manually review only the filtered candidate events.
4. Preserve all source URLs in `source_log.csv`.

## Public Search Keywords

Use these keywords in NSE/BSE corporate announcement search pages and public web search:

- resignation of statutory auditor
- resignation of statutory auditors
- statutory auditor resignation
- resignation of auditor
- resignation of auditors
- change in statutory auditor
- auditor resignation regulation 30
- announcement under regulation 30 resignation of statutory auditors

## Semi-Automated Workflow

### Step 1: Download Raw Search Results

Use NSE/BSE public corporate announcement search pages and export/download CSVs where available.

Save them into:

```text
data/raw/announcements/
```

Suggested filenames:

```text
nse_announcements_2019_2020.csv
nse_announcements_2021_2022.csv
nse_announcements_2023_2024.csv
nse_announcements_2025.csv
bse_announcements_2019_2020.csv
bse_announcements_2021_2022.csv
bse_announcements_2023_2024.csv
bse_announcements_2025.csv
```

### Step 2: Filter Candidate Auditor Resignation Events

Run a Python script to filter rows where the subject/headline/details contain auditor-resignation keywords.

Output:

```text
data/processed/auditor_resignation_candidates.csv
```

### Step 3: Manual Review of Candidate Rows Only

Instead of manually searching thousands of announcements, review only the filtered candidate rows.

For each candidate, confirm:

- It is a statutory auditor resignation, not only an appointment.
- It has a valid event date.
- It has a source URL or attachment link.
- The resignation reason can be extracted or classified.

### Step 4: Build Final Event Master

Cleaned and verified events should be saved as:

```text
data/processed/event_master_clean.csv
```

## Minimum Viable Dataset

If 100-200 events is not feasible initially, use a pilot working-paper version:

- 30-50 verified events
- clear data limitation disclosure
- transparent source log
- event-study pilot results

This can still be presented as an SSRN working paper, provided limitations are clearly disclosed.

## Research Integrity Rule

Do not fabricate events. Do not include events without source links. Do not treat unverified search-result snippets as final data.
