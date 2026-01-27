# System Architecture — FinSight Product Decision System

This diagram illustrates the end-to-end flow from business strategy to
data-driven decisions.

### Architecture Philosophy

- Strategy (TAM → SAM → SOM) defines *what* the business optimizes for
- Metrics translate strategy into measurable success criteria
- Data and analytics are designed around decision-driving signals (activation, TTV, risk)
- Dashboards are scoped by persona to avoid metric overload
- The decision layer ensures insights lead to concrete product, revenue, and CS actions


```mermaid
flowchart TD
    A["Business Strategy & Goals
(TAM → SAM → SOM)"] --> B["Metrics Framework
North Star & KPIs"]

    B --> C["Data Model
Star Schema"]
    
    C --> D["Python Data Generation
Time-aware SaaS Simulation"]
    D --> E["Analytics Data Layer
Fact & Dimension Tables (CSV / SQL)"]

    E --> F["SQL Analytics Layer"]
    F --> F1["Activation & Funnel Analysis"]
    F --> F2["Retention & Engagement Analysis"]
    F --> F3["Churn & Risk Modeling"]
    F --> F4["Revenue & MRR Analysis"]

    F --> G["Power BI Dashboards"]

    G --> G1["Executive Dashboard
Growth & Portfolio Health"]
    G --> G2["Product Dashboard
Activation & Engagement"]
    G --> G3["Ops Dashboard
Retention & Risk"]

    G --> H["Decision Layer
(Metric-triggered actions & playbooks)"]
    H --> H1["Product Decisions
(Onboarding, Feature Focus)"]
    H --> H2["Revenue Decisions
(Risk Mitigation, Expansion)"]
    H --> H3["CS / Ops Actions
(Proactive Intervention)"]

    H --> I["Insights & Decision Notes
08_insights"]

