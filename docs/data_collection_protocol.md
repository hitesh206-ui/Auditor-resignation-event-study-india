# Data Collection Protocol

## Objective

Build a clean event dataset of statutory auditor resignation announcements by Indian listed companies.

## Primary Event Sources

- NSE corporate announcements
- BSE corporate announcements
- Company Regulation 30 disclosures

## Search Keywords

Use combinations of the following terms:

- resignation of statutory auditor
- resignation of auditors
- statutory auditor resignation
- change in statutory auditor
- auditor resignation regulation 30
- resignation of auditor of the company

## Event Inclusion Criteria

Include an event if:

1. The company is listed on NSE and/or BSE.
2. The announcement relates to resignation of a statutory auditor.
3. The disclosure date is available.
4. The company has sufficient stock price data around the event.
5. The event is not a duplicate of the same resignation disclosed on another exchange.

## Event Exclusion Criteria

Exclude an event if:

1. It relates only to appointment of an auditor without resignation.
2. The event date cannot be verified.
3. The stock was suspended or has insufficient price history.
4. The same firm has another major confounding announcement on the same date, if this cannot be controlled.

## Minimum Event Fields

- event_id
- company_name
- ticker_nse
- bse_code
- exchange_source
- announcement_date
- announcement_time
- event_date_adjusted
- auditor_name
- auditor_type
- reason_text
- reason_category
- pdf_url
- duplicate_flag
- valid_event_flag

## Price Data Requirement

For each valid event, collect daily prices from at least 150 trading days before the event to 20 trading days after the event.

## Source Log

Every manually collected event should be supported by a source link in `data/documentation/source_log.csv`.
