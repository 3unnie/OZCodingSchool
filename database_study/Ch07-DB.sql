SELECT c.name, COUNT(fc.category_id) as film_num 
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
GROUP BY c.name;

SELECT r.rental_date,f.title 
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE customer_id = 5;
 
SELECT last_update, title 
FROM film
ORDER BY last_update DESC;

SELECT a.first_name, a.last_name
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
JOIN film f  ON fa.film_id = f.film_id
WHERE f.title = "ACADEMY DINOSAUR";

SELECT c.customer_id,c.first_name,c.last_name 
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE f.title = "ACADEMY DINOSAUR";

SELECT c.customer_id,c.first_name,c.last_name,f.title
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
GROUP BY c.customer_id, c.first_name, c.last_name;

SELECT f.title, AVG(DATEDIFF(r.return_date, r.rental_date)) AS avg_rental_date 
FROM rental r
JOIN inventory i ON i.inventory_id = r.inventory_id
JOIN film f ON i.film_id = f.film_id
GROUP BY f.film_id
ORDER BY avg_rental_date DESC;

SELECT f.title, COUNT(r.inventory_id) AS rental_count
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
GROUP BY f.title
ORDER BY rental_count DESC;


SELECT c.name, AVG(f.rental_rate)
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN film f ON fc.film_id = f.film_id
GROUP BY c.name;

SELECT YEAR(p.payment_date) as year, MONTH(p.payment_date) as month, SUM(p.amount) as total
FROM payment p
GROUP BY year, month;

SELECT a.first_name, COUNT(fa.film_id) AS fcount
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
GROUP BY a.actor_id
ORDER BY fcount DESC;

SELECT COUNT(*) 
FROM film 
WHERE rental_rate > (SELECT AVG(rental_rate) FROM film);

SELECT c.first_name, COUNT(r.rental_id) AS rental_count
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
GROUP BY c.customer_id
ORDER BY rental_count DESC;

SELECT f.title, COUNT(r.rental_id) AS rc
FROM film f 
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE a.first_name ="PENELOPE" AND a.last_name ="GUINESS"
GROUP BY f.film_id
ORDER BY rc;
