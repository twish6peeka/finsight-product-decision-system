SELECT
    DATE_TRUNC('week', event_timestamp) AS week,
    COUNT(DISTINCT business_id) AS weekly_active_businesses
FROM fact_product_events
GROUP BY week
ORDER BY week;
