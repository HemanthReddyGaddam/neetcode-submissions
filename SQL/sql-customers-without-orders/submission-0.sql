-- Write your query below
SELECT name 
FROM customers as c
WHERE c.id NOT IN (SELECT customer_id 
                FROM orders);