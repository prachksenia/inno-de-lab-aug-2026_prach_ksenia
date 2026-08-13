
-- Count of orders and everage items' counts

SELECT item, COUNT(*) AS count, ROUND(AVG(amount), 2) AS avg_amount
FROM orders
GROUP BY item;