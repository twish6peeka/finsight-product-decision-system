SELECT
    b.business_id,
    MAX(e.event_timestamp) AS last_activity,
    CURRENT_DATE - MAX(e.event_timestamp) AS days_inactive
FROM dim_business b
LEFT JOIN fact_product_events e
ON b.business_id = e.business_id
GROUP BY b.business_id
HAVING CURRENT_DATE - MAX(e.event_timestamp) > 30;
