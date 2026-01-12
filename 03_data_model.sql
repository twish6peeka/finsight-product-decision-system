CREATE TABLE dim_business (
    business_id SERIAL PRIMARY KEY,
    industry TEXT,
    country TEXT,
    signup_date DATE
);

CREATE TABLE fact_transactions (
    transaction_id SERIAL PRIMARY KEY,
    business_id INT,
    amount NUMERIC,
    transaction_date DATE
);
