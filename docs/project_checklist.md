# Project Checklist

## Priority 1: Critical Path

These items must be completed before the research paper can produce real empirical findings.

### 1. Build Python Event-Study Pipeline

- [ ] Read `Event_Master` from the Excel workbook or CSV export
- [ ] Pull tickers and adjusted event dates
- [ ] Download historical stock prices using `yfinance` or another public data source
- [ ] Download market index prices
- [ ] Compute stock and market returns
- [ ] Estimate market-model alpha and beta for each event
- [ ] Write alpha, beta, R-squared, and observation count to `Estimation_Window`
- [ ] Compute daily abnormal returns
- [ ] Compute CARs for `[-1,+1]`, `[0,+1]`, `[-3,+3]`, `[-5,+5]`, and `[-10,+10]`
- [ ] Run t-tests, sign tests, Patell test, and BMP placeholder
- [ ] Export results to Excel/CSV

### 2. Collect Real Event Data

- [ ] Search NSE and BSE corporate announcements for auditor resignation events
- [ ] Capture company name, ticker, exchange, announcement date, auditor name, reason text, and source URL
- [ ] Classify reason category manually
- [ ] Flag Big 4 / non-Big 4 auditor
- [ ] Manually flag confounding news around event date
- [ ] Target pilot sample: 20 events
- [ ] Target working paper sample: 100-200 events

### 3. Add Required Variables

- [ ] Add `post_2019_dummy`
- [ ] Add `confounding_news_flag`
- [ ] Add firm-level controls where available

## Priority 2: Important but Sequential

- [ ] Run full event-study analysis once data is ready
- [ ] Run cross-sectional regressions using CAR as dependent variable
- [ ] Perform robustness checks with alternative windows and benchmarks
- [ ] Generate publication charts
- [ ] Add `Regression_Output` and final tables

## Priority 3: Paper Development

- [ ] Draft abstract
- [ ] Draft introduction
- [ ] Draft institutional background
- [ ] Draft literature review
- [ ] Draft methodology section
- [ ] Insert empirical results
- [ ] Add robustness checks
- [ ] Draft limitations and conclusion
- [ ] Prepare SSRN submission package
