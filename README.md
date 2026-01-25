# FinSight-product-decision-system
End-to-end product strategy, analytics, and decision framework for a B2B SaaS Product

## Strategic Foundation

To ensure the data remained grounded in reality, the product's growth model was built on a **bottom-up market sizing approach**:

- Market sizing: TAM → SAM → SOM  
- Metrics and decisions are aligned with realistic business potential  
- Revenue, adoption, and churn outcomes simulate plausible SaaS dynamics  

---

## Why this project exists

Over the last ~2 years working across analytics, operations, and product-adjacent roles, I noticed a recurring gap: most dashboards answer *what happened*, but very few help teams decide *what to do next*.

Metrics like MRR, ARR, churn, retention, and activation are often tracked in isolation. In reality, these metrics are deeply connected through **product usage, customer behavior, and business strategy**.

This project was built to simulate how leadership and product teams actually run a SaaS business using data — by connecting **product activation → retention → revenue → churn risk** into a single decision system.

---

## Business Context

- **Product:** Hypothetical B2B SaaS product (Analytics / HealthTech / HR Tech)  
- **ICP:** Mid-to-large enterprises in SaaS, Retail, Healthcare, Manufacturing  
- **Revenue Model:** Subscription-based (Free, Standard, Premium tiers)  
- **Business Goals:**  
  - Drive adoption and retention  
  - Minimize churn and revenue risk  
  - Prioritize high-value interventions based on data  

---

## Metrics Philosophy

Metrics are designed to connect **activation → retention → long-term value**, enabling decision-making, not just reporting. Key highlights:

- **North Star Metric:** Retained Activated Businesses  
- **Activation & Retention Metrics:** Time-to-Value (TTV), Activation Rate, Activation → Retention Rate  
- **Revenue & Risk Metrics:** At-Risk MRR, Net MRR Churn %, Active Subscriptions, ARPB  

---

## What this system does

This project models a hypothetical B2B SaaS product and builds a complete analytics pipeline that:

* Tracks **activation and time-to-value (TTV)** as leading indicators  
* Measures **retention quality**, not just user counts  
* Quantifies **churn and at-risk MRR** before revenue is lost  
* Separates views for **Executives, Product Managers, and Operations / CS teams**  
* Enables **decision-making**, not just reporting  

---

## Dashboards & decision owners

| Dashboard                                | Primary User     | Key Decisions Enabled                                                         |
| ---------------------------------------- | ---------------- | ---------------------------------------------------------------------------- |
| **Enterprise Growth & Portfolio Health** | CEO / Leadership | Revenue health, growth sustainability, segment risk, MRR movement             |
| **Product Health Scorecard**             | Product Manager  | Activation gaps, feature adoption, time-to-value, zombie users                |
| **Retention & Risk Dashboard**           | CS / Ops         | Churn prevention, at-risk accounts, retention trends, intervention priorities |

Each dashboard is intentionally scoped to avoid metric overlap and support a specific decision-maker.

---

## Key insights uncovered

* **Low activation penetration created downstream churn risk** despite stable acquisition  
* **Time-to-value (TTV)** showed stronger correlation with retention than feature frequency  
* A small number of segments contributed disproportionately to **at-risk MRR**  
* Users that activated once but failed to re-engage (“zombies”) represented silent churn  
* Revenue risk appeared **weeks before actual churn events**  

---

## Tech stack & skills demonstrated

* **Python** – Synthetic SaaS data generation with time-aware churn, MRR, ARR, and activation behavior  
* **SQL** – Funnel analysis, retention cohorts, churn & risk modeling, revenue analytics  
* **Power BI** – Executive, product, and ops dashboards with KPI-driven storytelling  
* **GitHub** – Version-controlled analytics pipeline and documentation  


---

## Repository structure
* 01_business_overview.md        # Business model, ICP, goals
* 02_metrics_framework/          # North Star & KPI definitions
* 03_data_model.sql              # Star schema & table design
* 04_data_generation.py          # Synthetic SaaS data generation (Python)
* 05_sql_*.sql                   # Analytics queries (activation, churn, retention, revenue)
* 06_dashboards                  # Screenshots of the dashboard
* 07_decisions_and_execution.md  # Decision framework
* 08_insights/                   # Decision simulations & insights
* README.md


---

## How to use this project

* Review the business context to understand why metrics were chosen
* Explore SQL queries to see how activation, churn, and revenue are modeled
* Use dashboards to simulate real SaaS decisions
* Refer to /08_insights for example decision narratives

---


> This project was built end-to-end from scratch, simulating a real-world SaaS analytics workflow.
