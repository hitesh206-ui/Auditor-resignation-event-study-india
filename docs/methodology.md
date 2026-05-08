# Methodology

## Research Design

This project uses an event-study methodology to examine the stock market reaction to statutory auditor resignation announcements in India.

## Event Definition

The event date is the date on which a listed company discloses the resignation of its statutory auditor through NSE or BSE corporate announcements.

If an announcement is released after market hours, the next trading day may be used as the adjusted event date.

## Estimation Window

The planned estimation window is:

```text
[-120, -20]
```

This window is used to estimate the normal relationship between the stock return and market return before the event.

## Event Windows

The planned event windows are:

```text
[-1,+1]
[0,+1]
[-3,+3]
[-5,+5]
[-10,+10]
```

## Market Model

Normal returns are estimated using the market model:

```text
R_i,t = alpha_i + beta_i * R_m,t + epsilon_i,t
```

Abnormal returns are calculated as:

```text
AR_i,t = R_i,t - (alpha_i + beta_i * R_m,t)
```

Cumulative abnormal returns are calculated as:

```text
CAR_i,[a,b] = sum(AR_i,t) from t=a to t=b
```

## Planned Tests

The project will test whether average CARs are statistically different from zero and whether CARs differ across resignation-reason categories, auditor reputation groups, and firm-condition groups.

## Key Hypotheses

1. Auditor resignation announcements are associated with negative abnormal returns.
2. Serious resignation reasons generate stronger negative abnormal returns than generic reasons.
3. Resignations by reputed or Big 4 auditors generate stronger market reactions.
4. Financially weaker firms experience larger negative abnormal returns.

## Data Sources

- NSE corporate announcements
- BSE corporate announcements
- Public stock price data
- Public market index data
- Company annual reports and public financial websites for control variables
