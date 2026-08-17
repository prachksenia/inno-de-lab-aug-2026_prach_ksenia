
-- Count of clients in every country

SELECT country, COUNT(*) AS count
FROM customers
GROUP BY country;