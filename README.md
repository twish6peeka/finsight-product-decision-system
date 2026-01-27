# FinSight — Product Decision System for a B2B SaaS

FinSight is an end-to-end product analytics and decision framework that models how leadership teams actually run a SaaS business using data — not just dashboards.

This project connects **product behavior → revenue risk → operational action**, enabling proactive decision-making instead of reactive reporting.

---

## Why This Project Exists

Over the last ~2 years working across analytics, operations, and product-adjacent roles, a recurring gap became obvious:

- Most dashboards explain **what happened**
- Very few help teams decide **what to do next**

Core business metrics like activation, retention, churn, and MRR are often tracked in isolation.  
In reality, they are tightly connected through **Time-to-Value**, **customer behavior**, and **value realization**.

FinSight was built to simulate a **real-world SaaS decision system**, not a reporting layer.

---

## Business Context

- **Product:** Hypothetical B2B SaaS (Analytics / HealthTech / HR Tech)
- **ICP:** SMBs and mid-market businesses
- **Industries:** SaaS, Retail, Healthcare, Manufacturing
- **Revenue Model:** Subscription-based (Free, Standard, Premium)

### Primary Business Goals
- Improve activation quality
- Reduce churn and revenue risk
- Enable proactive, data-driven interventions

---

## 🛡️ Analytical Transparency: The “Rescue Mission”

This project intentionally models a **high-risk business environment** to prove that the analytics system can surface problems *before* they hit the balance sheet.

### What the Data Reveals

- **Activation Crisis:**  
  Only **6.67%** of signups reach activation — meaning 93% fail to realize initial value.

- **Revenue Leak:**  
  **17.25% Net MRR Churn**, driven primarily by Premium customers exiting faster than low-value users.

- **Zombie Accounts:**  
  67 accounts appear “active” but never use core value features — a silent churn risk invisible in top-line metrics.

These are not failures of the project.  
They are proof that the **decision system is working**.

---

## Metrics Philosophy

Metrics are designed to drive action, not vanity reporting.

**Core Principles**
- Leading indicators over lagging outcomes
- Behavioral signals over surface-level usage
- Revenue risk visibility before churn occurs

**North Star Metric**
> **Retained Activated Businesses**

---

## What This System Does

FinSight models a complete SaaS analytics and decision pipeline that:

- Tracks **Activation** and **Time-to-Value (TTV)** as leading indicators
- Measures **retention quality**, not just user counts
- Quantifies **at-risk MRR** before churn occurs
- Separates insights by **decision owner**
- Enables **intervention-ready** decision-making

---

## Dashboards & Decision Owners

| Dashboard            | Primary User        | Decisions Enabled                                  |
|----------------------|---------------------|----------------------------------------------------|
| Enterprise Growth    | CEO / Leadership    | Revenue health, growth sustainability, segment risk |
| Product Health       | Product Manager     | Activation gaps, TTV, value-driven adoption         |
| Retention & Risk     | CS / Operations     | Churn prevention, at-risk account prioritization    |

---

## Key Insights Uncovered

- Activation penetration remains below **3%**, creating downstream churn risk
- Time-to-Value correlates more strongly with retention than raw feature usage
- Feature usage frequency alone does not guarantee retention
- Zombie accounts hide churn risk behind misleading “active user” metrics
- Revenue risk surfaces **weeks before actual churn events**

---

## Tech Stack & Skills Demonstrated

- **Python:** Time-aware synthetic SaaS data generation (activation, churn, MRR)
- **SQL:** Funnel analysis, cohort retention, churn & revenue modeling
- **Power BI:** Executive, product, and operations dashboards with KPI-driven storytelling
- **GitHub:** Version-controlled analytics pipeline and documentation

---

## How to use this project
- **Weekly executive review:** Portfolio health and revenue risk monitoring
- **Product sprint planning:** Activation bottleneck diagnosis
- **CS risk review:** Proactive churn prevention and outreach prioritization

---


## Repository Structure
                
```plaintext
01_business_overview.md       # Strategic goals & ICP
02_metrics_framework/         # North Star & Input/Output metrics
03_data_model.sql             # Star schema relational design
04_data_generation.py         # Time-aware synthetic data engine
05_sql_*.sql                  # Advanced analytics & cohort queries
06_dashboards/                # Visualization logic & screenshots
07_decisions_and_execution.md # Actionable business playbooks
08_insights.md                # Turnaround simulation & findings
README.md                     # Project overview



> This project was built end-to-end from scratch, simulating a real-world SaaS analytics workflow.
