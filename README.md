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
- Estimation window: `[-120, -20]` trading days
- Event windows: `[-1,+1]`, `[0,+1]`, `[-3,+3]`, `[-5,+5]`, and `[-10,+10]`
- Benchmark model: market model using a broad Indian equity index such as Nifty 500 or Nifty 50

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

This repository is in the research-design and data-collection stage. The first empirical milestone is a pilot event study using approximately 20 auditor resignation announcements.

## Disclaimer

This repository is for academic and educational research purposes only. It does not provide investment advice. Third-party source documents should be referenced through links rather than uploaded if redistribution rights are unclear.
