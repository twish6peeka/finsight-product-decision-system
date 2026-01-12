SELECT
    plan_type,
    COUNT(DISTINCT business_id) AS businesses,
    SUM(monthly_price) AS monthly_revenue
FROM fact_subscription
GROUP BY plan_type;
