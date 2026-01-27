# FinSight — Product Decision System for a B2B SaaS

An end-to-end product analytics and decision framework that models how leadership teams **actually run a SaaS business using data**.

---

## Why This Project Exists

Over the last ~2 years working across analytics, operations, and product-adjacent roles, I noticed a recurring gap:

> Most dashboards explain what happened.  
> Very few help teams decide what to do next.

Metrics like MRR, churn, retention, and activation are often tracked in isolation.  
In reality, they are deeply connected through product behavior, customer value realization, and business strategy.

This project was built to simulate a **real-world SaaS decision system**, not just a reporting layer.

---

## Business Context

- **Product:** Hypothetical B2B SaaS (Analytics / HealthTech / HR Tech)
- **ICP:** SMBs and mid-market businesses across SaaS, Retail, Healthcare, Manufacturing
- **Revenue Model:** Subscription-based (Free, Standard, Premium)
- **Primary Goals:**
  - Improve activation and retention quality
  - Reduce churn and revenue risk
  - Enable proactive, data-driven decision-making

---

## Metrics Philosophy

Metrics are designed to connect **activation → retention → long-term value**, enabling action rather than vanity reporting.

**Key principles**
- Leading indicators over lagging outcomes
- Behavioral metrics over surface-level usage
- Revenue risk visibility before churn occurs

**North Star Metric**  
**Retained Activated Businesses**

---

## What This System Does

This project models a complete SaaS analytics pipeline that:

- Tracks activation and Time-to-Value as leading indicators
- Measures retention quality, not just user counts
- Quantifies churn risk and at-risk MRR before revenue is lost
- Separates insights by decision owner (Exec, Product, CS)
- Enables intervention-ready decision-making

---

## Dashboards & Decision Owners

| Dashboard | Primary User | Decisions Enabled |
|--------|-------------|------------------|
| Enterprise Growth & Portfolio Health | CEO / Leadership | Revenue health, growth sustainability, segment-level risk |
| Product Health Scorecard | Product Manager | Activation gaps, Time-to-Value, value-driven feature adoption |
| Retention & Risk Dashboard | CS / Operations | Churn prevention, at-risk accounts, intervention prioritization |

Each dashboard is intentionally scoped to avoid metric overload and support a specific decision context.

---

## Key Insights Uncovered

- Low activation penetration created downstream churn and revenue risk despite stable acquisition
- Time-to-Value showed stronger correlation with retention than raw feature usage
- A small number of segments contributed disproportionately to at-risk MRR
- Zombie accounts represented silent churn hidden behind top-line metrics
- Revenue risk surfaced weeks before actual churn events

---

## Tech Stack & Skills Demonstrated

- **Python:** Time-aware synthetic SaaS data generation (activation, churn, MRR dynamics)
- **SQL:** Funnel analysis, retention cohorts, churn & revenue modeling
- **Power BI:** Executive, product, and operations dashboards with KPI-driven storytelling
- **GitHub:** Version-controlled analytics pipeline and documentation

---

## Repository structure
| 01_business_overview.md       |   # Business model, ICP, goals |         
| 02_metrics_framework/         |    # North Star & KPI definitions |
| 03_data_model.sql             |   # Star schema & table design |
| 04_data_generation.py         |    # Synthetic SaaS data generation (Python) |
| 05_sql_*.sql                  |     # Analytics queries (activation, churn, retention, revenue) |
| 06_dashboards                 |   # Screenshots of the dashboard |
| 07_decisions_and_execution.md |  # Decision framework |
| 08_insights/                  | # Decision simulations & insights |
| README.md                     |                            |


---

## How to use this project

* Review the business context to understand why metrics were chosen
* Explore SQL queries to see how activation, churn, and revenue are modeled
* Use dashboards to simulate real SaaS decisions
* Refer to /08_insights for example decision narratives

---


> This project was built end-to-end from scratch, simulating a real-world SaaS analytics workflow.
