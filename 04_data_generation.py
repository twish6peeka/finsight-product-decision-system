import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

random.seed(42)
np.random.seed(42)

START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2026, 12, 31)
NUM_BUSINESSES = 120

industries = ["Retail", "SaaS", "Healthcare", "Manufacturing"]
countries = ["Australia", "India", "US"]
plans = ["Free", "Standard", "Premium"]
plan_price = {"Free": 0, "Standard": 49, "Premium": 99}

# =========================
# QUARTER BEHAVIOR CONFIG
# =========================
quarter_rules = {
    1: {"usage": 0.8, "churn": 0.10, "revenue": 0.9},
    2: {"usage": 1.2, "churn": 0.08, "revenue": 1.1},
    3: {"usage": 0.5, "churn": 0.30, "revenue": 0.8},
    4: {"usage": 1.4, "churn": 0.15, "revenue": 1.3},
}

def get_quarter(dt):
    return (dt.month - 1) // 3 + 1

output_dir = "quarter_aware_data"
os.makedirs(output_dir, exist_ok=True)

# =====================
# DIM_DATE
# =====================
dates = pd.date_range(START_DATE, END_DATE)
df_date = pd.DataFrame({
    "date": dates,
    "year": dates.year,
    "quarter": "Q" + dates.to_series().dt.quarter.astype(str),
    "month": dates.month
})

# =====================
# DIM_BUSINESS
# =====================
businesses = []
for i in range(1, NUM_BUSINESSES + 1):
    signup = START_DATE + timedelta(days=random.randint(0, 365))
    plan = random.choices(plans, weights=[0.4, 0.35, 0.25])[0]

    businesses.append({
        "business_id": i,
        "business_name": f"Business_{i}",
        "industry": random.choice(industries),
        "country": random.choice(countries),
        "signup_date": signup,
        "plan_type": plan
    })

df_business = pd.DataFrame(businesses)

# =====================
# FACT_SUBSCRIPTIONS (QUARTER-BASED CHURN)
# =====================
subs = []
for _, b in df_business.iterrows():
    start = b.signup_date
    plan = b.plan_type
    end = None

    if plan != "Free":
        q = get_quarter(start)
        churn_chance = quarter_rules[q]["churn"]
        if random.random() < churn_chance:
            churn_months = random.randint(3, 12)
            end = start + pd.DateOffset(months=churn_months)
            if end > END_DATE:
                end = None

    subs.append({
        "business_id": b.business_id,
        "plan_type": plan,
        "monthly_price": plan_price[plan],
        "start_date": start,
        "end_date": end
    })

df_subs = pd.DataFrame(subs)

# =====================
# FACT_EVENTS (USAGE VARIES BY QUARTER)
# =====================
events = []

for _, sub in df_subs.iterrows():
    start = sub.start_date
    end = sub.end_date or END_DATE

    if random.random() < 0.85:  # activation probability
        current = start + timedelta(days=random.randint(1, 10))

        while current < end:
            q = get_quarter(current)
            usage_factor = quarter_rules[q]["usage"]

            if random.random() < 0.4 * usage_factor:
                events.append({"business_id": sub.business_id, "event_name": "login", "event_timestamp": current})

            if random.random() < 0.3 * usage_factor:
                events.append({"business_id": sub.business_id, "event_name": "dashboard_view", "event_timestamp": current})

            if random.random() < 0.2 * usage_factor:
                events.append({"business_id": sub.business_id, "event_name": "forecast_used", "event_timestamp": current})

            current += timedelta(days=random.randint(4, 10))

df_events = pd.DataFrame(events)

# =====================
# FACT_TRANSACTIONS (REVENUE BY QUARTER)
# =====================
transactions = []

for _, sub in df_subs.iterrows():
    if sub.monthly_price == 0:
        continue

    current = sub.start_date
    end = sub.end_date or END_DATE

    while current < end:
        q = get_quarter(current)
        rev_factor = quarter_rules[q]["revenue"]

        inflow = int(random.randint(8000, 40000) * rev_factor)
        outflow = -int(random.randint(3000, 25000) * rev_factor)

        transactions.append({
            "business_id": sub.business_id,
            "amount": inflow,
            "transaction_type": "inflow",
            "transaction_date": current
        })
        transactions.append({
            "business_id": sub.business_id,
            "amount": outflow,
            "transaction_type": "outflow",
            "transaction_date": current
        })

        current += pd.DateOffset(months=1)

df_txn = pd.DataFrame(transactions)

# =====================
# EXPORT
# =====================
df_business.to_csv(f"{output_dir}/dim_business.csv", index=False)
df_date.to_csv(f"{output_dir}/dim_date.csv", index=False)
df_subs.to_csv(f"{output_dir}/fact_subscriptions.csv", index=False)
df_events.to_csv(f"{output_dir}/fact_events.csv", index=False)
df_txn.to_csv(f"{output_dir}/fact_transactions.csv", index=False)

print("QUARTER-DIFFERENT DATA GENERATED (2024–2026)")

