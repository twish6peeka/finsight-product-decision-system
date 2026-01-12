-- Activation Funnel: Signup → First Dashboard View

WITH signup AS (
    SELECT business_id, signup_date
    FROM dim_business
),

first_dashboard AS (
    SELECT
        business_id,
        MIN(event_timestamp) AS first_dashboard_view
    FROM fact_product_events
    WHERE event_name = 'dashboard_view'
    GROUP BY business_id
)

SELECT
    COUNT(DISTINCT signup.business_id) AS total_signups,
    COUNT(DISTINCT first_dashboard.business_id) AS activated_businesses,
    ROUND(
        COUNT(DISTINCT first_dashboard.business_id) * 100.0 /
        COUNT(DISTINCT signup.business_id), 2
    ) AS activation_rate
FROM signup
LEFT JOIN first_dashboard
ON signup.business_id = first_dashboard.business_id;

