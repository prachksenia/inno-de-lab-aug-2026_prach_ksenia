
-- Client with order for maximum amount

SELECT c.first_name, c.last_name, o.amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.amount = (SELECT MAX(amount) FROM orders);