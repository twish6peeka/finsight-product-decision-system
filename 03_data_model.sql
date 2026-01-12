-- ===============================
-- DIMENSION TABLES
-- ===============================

CREATE TABLE dim_business (
    business_id SERIAL PRIMARY KEY,
    business_name TEXT,
    industry TEXT,
    country TEXT,
    company_size TEXT,
    signup_date DATE,
    plan_type TEXT
);

CREATE TABLE dim_user (
    user_id SERIAL PRIMARY KEY,
    business_id INT,
    role TEXT,
    created_at DATE
);

CREATE TABLE dim_date (
    date DATE PRIMARY KEY,
    month INT,
    quarter INT,
    year INT
);

-- ===============================
-- FACT TABLES
-- ===============================


CREATE TABLE fact_transactions (
    transaction_id SERIAL PRIMARY KEY,
    business_id INT,
    amount NUMERIC,
    transaction_type TEXT, -- inflow / outflow
    transaction_date DATE
);

CREATE TABLE fact_product_events (
    event_id SERIAL PRIMARY KEY,
    business_id INT,
    user_id INT,
    event_name TEXT,
    event_timestamp TIMESTAMP
);

CREATE TABLE fact_subscription (
    business_id INT,
    plan_type TEXT,
    monthly_price NUMERIC,
    start_date DATE,
    end_date DATE
);

