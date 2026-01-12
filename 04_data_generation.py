import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

# -------------------------
# CONFIG
# -------------------------
random.seed(42)
NUM_BUSINESSES = 120
START_DATE = datetime(2023, 1, 1)

industries = ["Retail", "SaaS", "Healthcare", "Manufacturing"]
countries = ["Australia", "India", "US"]
plans = ["Free", "Standard", "Premium"]
events = ["login", "dashboard_view", "forecast_used"]

# -------------------------
# Ensure export folder exists
# -------------------------
output_dir = "05_data_exports"
os.makedirs(output_dir, exist_ok=True)

# -------------------------
# DIM_BUSINESS
# -------------------------
businesses = []

for i in range(1, NUM_BUSINESSES + 1):
    signup_date = START_DATE + timedelta(days=random.randint(0, 400))
    plan = random.choices(plans, weights=[0.4, 0.4, 0.2])[0]

    businesses.append({
        "business_id": i,
        "business_name": f"Business_{i}",
        "industry": random.choice(industries),
        "country": random.choice(countries),
        "company_size": random.choice(["Small", "Medium"]),
        "signup_date": signup_date.date(),
        "plan_type": plan
    })

df_business = pd.DataFrame(businesses)

# -------------------------
# DIM_USER
# -------------------------
users = []
user_id = 1

for b in businesses:
    num_users = random.randint(1, 4)
    for _ in range(num_users):
        users.append({
            "user_id": user_id,
            "business_id": b["business_id"],
            "role": random.choice(["Founder", "Finance Manager"]),
            "created_at": b["signup_date"]
        })
        user_id += 1

df_users = pd.DataFrame(users)

# -------------------------
# FACT_PRODUCT_EVENTS
# -------------------------
events_data = []

for user in users:
    active_days = random.randint(30, 300)
    for day in range(active_days):
        if random.random() < 0.3:
            event_date = datetime.strptime(str(user["created_at"]), "%Y-%m-%d") + timedelta(days=day)
            events_data.append({
                "business_id": user["business_id"],
                "user_id": user["user_id"],
                "event_name": random.choice(events),
                "event_timestamp": event_date
            })

df_events = pd.DataFrame(events_data)

# -------------------------
# FACT_TRANSACTIONS
# -------------------------
transactions = []

for b in businesses:
    months_active = random.randint(3, 18)
    for m in range(months_active):
        transactions.append({
            "business_id": b["business_id"],
            "amount": random.randint(5000, 50000),
            "transaction_type": "inflow",
            "transaction_date": (b["signup_date"] + timedelta(days=30*m))
        })
        transactions.append({
            "business_id": b["business_id"],
            "amount": -random.randint(2000, 30000),
            "transaction_type": "outflow",
            "transaction_date": (b["signup_date"] + timedelta(days=30*m))
        })

df_transactions = pd.DataFrame(transactions)

# -------------------------
# FACT_SUBSCRIPTIONS
# -------------------------
subscriptions = []

for b in businesses:
    price = 0 if b["plan_type"] == "Free" else (49 if b["plan_type"] == "Standard" else 99)
    subscriptions.append({
        "business_id": b["business_id"],
        "plan_type": b["plan_type"],
        "monthly_price": price,
        "start_date": b["signup_date"],
        "end_date": None
    })

df_subscriptions = pd.DataFrame(subscriptions)

# -------------------------
# DIM_DATE
# -------------------------
start_date = START_DATE
end_date = datetime.today()
date_range = pd.date_range(start=start_date, end=end_date)

df_date = pd.DataFrame({
    "date": date_range,
    "year": date_range.year,
    "month": date_range.month,
    "day": date_range.day,
    "weekday": date_range.weekday
})

# -----------------------------
# Export data for Power BI
# -----------------------------
df_business.to_csv(f"{output_dir}/dim_business.csv", index=False)
df_date.to_csv(f"{output_dir}/dim_date.csv", index=False)
df_events.to_csv(f"{output_dir}/fact_events.csv", index=False)
df_transactions.to_csv(f"{output_dir}/fact_transactions.csv", index=False)
df_subscriptions.to_csv(f"{output_dir}/fact_subscriptions.csv", index=False)

print("CSV files exported to 05_data_exports/")

