
-- Shippings with customers' status and names

SELECT s.status, c.first_name, c.last_name
FROM shippings s
JOIN customers c ON s.customer = c.customer_id;