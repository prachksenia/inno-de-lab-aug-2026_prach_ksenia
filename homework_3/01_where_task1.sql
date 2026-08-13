
-- Clients from USA, age > 25

SELECT first_name, last_name, age, country
FROM customers
WHERE country = 'USA'
  AND age > 25;