
-- Orders with clients' names

SELECT c.first_name, c.last_name, o.item, o.amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id;