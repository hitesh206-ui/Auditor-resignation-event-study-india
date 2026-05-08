# Auditor Resignation Event Study in India

This repository supports a research project titled:

**The Information Content of Auditor Resignation Disclosures in India: Evidence from Stock Market Reactions**

## Research Objective

This project examines whether statutory auditor resignation announcements in Indian listed companies contain value-relevant information for investors, as reflected in abnormal stock returns around the announcement date.

## Research Question

Do auditor resignation announcements generate statistically significant abnormal returns in Indian equity markets?

## Planned Methodology

The study uses an event-study framework:

- Event date: statutory auditor resignation announcement date
- Primary estimation window: `[-250, -30]` trading days
- Robustness estimation window: `[-120, -20]` trading days
- Event windows: `[-1,+1]`, `[0,+1]`, `[-3,+3]`, `[-5,+5]`, and `[-10,+10]`
- Primary benchmark model: market model using a broad Indian equity index such as Nifty 500 or Nifty 50
- Robustness benchmarks: size index, sector index, and market-adjusted returns

## Planned Statistical Tests

- Average abnormal return and cumulative abnormal return tests
- t-tests for CAR significance
- sign tests
- Patell standardized test
- BMP test placeholder
- cross-sectional regressions using CAR as dependent variable

## Data Sources

The project is designed to use public internet data:

- NSE corporate announcements
- BSE corporate announcements
- Public stock price data
- Public market index data
- Company annual reports and financial websites for control variables

## Repository Structure

```text
├── data/
│   ├── raw/
│   ├── processed/
│   └── documentation/
├── notebooks/
├── src/
├── outputs/
│   ├── tables/
│   ├── charts/
│   └── excel/
├── paper/
│   ├── draft/
│   └── ssrn_submission/
└── docs/
```

## Current Status

The research design and Excel template have been revised. The next critical path items are:

1. Collect real auditor resignation events from NSE/BSE.
2. Complete the Python event-study pipeline.
3. Run the pilot analysis on approximately 20 events.
4. Expand the dataset to 100-200 events.
5. Generate results, regressions, charts, and the SSRN working paper.

## Disclaimer

This repository is for academic and educational research purposes only. It does not provide investment advice. Third-party source documents should be referenced through links rather than uploaded if redistribution rights are unclear.
