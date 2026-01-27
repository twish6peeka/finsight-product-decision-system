# Decision Insights & Execution Notes

This document demonstrates how product, revenue, and risk dashboards translate into **explicit business decisions and operational actions**, rather than passive reporting.

The system is designed to identify **leading behavioral failures** and trigger corrective action *before* those failures appear as churn or revenue loss.

---

## Insight 1 — The Activation Crisis is the Root Cause of Downstream Churn

### What We Observed
- Activation Rate is critically low at **6.67%**
- A large share of signups (**67 accounts**) became *zombie accounts* — users who logged in but never reached the **Key Activation Event**
- Retention declined sharply as a downstream effect of failed early value delivery

### What This Tells Us
Acquisition success is not translating into **Value Realization**.  
The current funnel functions as a **leaky bucket**, where ~93% of new users drop off before reaching the **Critical Conversion Point**.

This is not a retention problem — it is an **activation design failure**.

### Decisions Taken
- **Stop Acquisition Spend:** Pause further acquisition investment and prioritize onboarding redesign
- **Milestone Tracking:** Introduce explicit activation milestones within the first **14 days**
- **Onboarding Audit:** Redefine onboarding success around **First Value Delivered (FVD)**, not account creation or login events

### Metrics Used
- Activation Rate  
- Zombie Account Count  
- Avg Days to Activate (Time-to-Value / FVD)

---

## Insight 2 — The 25-Day Time-to-Value Wall Predicts Retention Quality

### What We Observed
- Average Time-to-Value (TTV) is **25 days**
- Businesses activating within ~20 days show materially stronger retention
- The current average pushes users into a **high-risk disengagement zone**
- Longer TTV strongly correlates with the **112 currently inactive businesses**

### What This Tells Us
Reaching value quickly matters more than feature breadth.  
For an SMB audience, a 25-day path to **First Value Delivered** is too slow, resulting in disengagement before commitment forms.

TTV functions as a **leading indicator of retention quality**, not just efficiency.

### Decisions Taken
- **Friction Reduction:** Simplify early product paths to reduce cognitive and setup load
- **In-App Guidance:** Introduce contextual walkthroughs to accelerate the `forecast_used` **Key Activation Event**
- **Metric Reweighting:** Treat TTV breaches as an early churn risk signal

### Metrics Used
- Avg Days to Activate (TTV / FVD)  
- Activation → Retention Rate  
- Retained Activated Businesses  

---

## Insight 3 — High Net MRR Churn Signals a Premium-Tier Revenue Leak

### What We Observed
- At-Risk MRR reached **$5.03K**
- Net MRR Churn is elevated at **17.25%**
- SaaS and Retail industries contribute disproportionately to revenue risk

### What This Tells Us
Churn is a **lagging indicator**.  
At-Risk MRR surfaces revenue exposure **before** customers formally churn.

The system reveals that **high-value customers are more likely to disengage**, signaling a Premium-tier experience gap.

### Decisions Taken
- **Segmented Rescue Playbooks:** Launch CS intervention workflows for high-risk SaaS and Retail accounts
- **Proactive Outreach:** Trigger CS contact for any account inactive for **>7 days post-activation**
- **Revenue-Weighted Prioritization:** Rank outreach based on MRR exposure, not account count

### Metrics Used
- At-Risk MRR  
- Net MRR Churn %  
- Industry-Level Risk Contribution  

---

## Insight 4 — Feature Adoption Does Not Equal Value Realization

### What We Observed
- 115 users logged in
- 85 viewed dashboards
- Only **51 reached the `forecast_used` event**, the product’s core value output
- High login frequency did not reliably translate into the **25.00% retention rate**

### What This Tells Us
Value is created through **sequenced behavior**, not surface-level engagement.  
Random logins without reaching the **Critical Conversion Point** fail to drive retention.

The `forecast_used` event is the true indicator of **Value Realization**, not activity volume.

### Decisions Taken
- **Redefine Success:** Reposition `forecast_used` as an early activation milestone
- **Path Optimization:** Focus product improvements on the  
  `Login → Connect Data → Forecast` conversion path
- **Deprioritize Vanity Metrics:** Reduce emphasis on login frequency as a success signal

### Metrics Used
- Key Activation Event Completion (`forecast_used`)  
- Path Conversion Rates  
- Retained Activated Businesses  

---

## Terminology Reference

| Term | Contextual Use |
|-----|---------------|
| **Value Realization** | The point at which a user experiences the core utility of the product |
| **Key Activation Event** | The specific action (e.g., first forecast generated) that correlates with long-term retention |
| **First Value Delivered (FVD)** | Time elapsed between signup and first successful value output |
| **Critical Conversion Point** | Behavioral milestone transitioning a user from evaluation to activation |

---

## System Outcome

This decision framework shifts conversations from **reporting outcomes** to **preventing failure**.

By operationalizing leading indicators such as **Time-to-Value**, **activation quality**, and **revenue-weighted risk**, the system enables earlier, more precise intervention — before churn becomes irreversible.


### Metrics Used
- Feature Adoption Post-Activation  
- Retained Activated Businesses  
- Activation Path Analysis


