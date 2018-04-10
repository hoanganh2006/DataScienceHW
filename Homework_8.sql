USE sakila;
SHOW tables;
SELECT first_name, last_name FROM actor;
SELECT CONCAT(first_name, ' ', last_name) AS 'Actor Name'
FROM actor;
SELECT actor_id, first_name, last_name FROM actor WHERE first_name = "JOE"; 
SELECT first_name, last_name FROM actor WHERE last_name LIKE '%GEN%'; 
SELECT last_name, first_name FROM actor WHERE last_name LIKE '%LI%'; 
SELECT country_id, country FROM country WHERE country IN('Afghanistan', 'Bangladesh', 'China');
ALTER TABLE actor
ADD COLUMN middle_name VARCHAR(50) NOT NULL AFTER first_name; 
ALTER TABLE actor 
MODIFY COLUMN middle_name BLOB;
ALTER TABLE actor
DROP COLUMN middle_name;
SELECT COUNT(actor_id), last_name FROM actor GROUP BY last_name;
SELECT last_name, count(last_name) as num_last_name FROM actor GROUP BY last_name HAVING count(last_name) >= 2;
UPDATE actor SET first_name = "HARPO" WHERE first_name = "GROUCHO";
SELECT last_name, 
IF (first_name = "HARPO", "GROUCHO", "GROUCHO MUCHO") AS new_first_name FROM actor;
SHOW CREATE TABLE sakila.address;
SELECT * FROM address;
SELECT * FROM staff;
SELECT first_name, last_name, address
FROM staff
INNER JOIN address ON staff.address_id = address.address_id;
SELECT * FROM payment;
#6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.
SELECT first_name, last_name, SUM(amount)
FROM staff
INNER JOIN payment 
ON staff.staff_id = payment.staff_id
GROUP BY payment.staff_id
ORDER BY last_name ASC;
SELECT title, COUNT(actor_id)
FROM film 
INNER JOIN film_actor 
ON film.film_id = film_actor.film_id
GROUP BY title;
SELECT title, COUNT(inventory_id)
FROM film 
INNER JOIN inventory 
ON film.film_id = inventory.film_id
WHERE title = "Hunchback Impossible";
SELECT last_name, first_name, SUM(amount)
FROM payment p
INNER JOIN customer c
ON p.customer_id = c.customer_id
GROUP BY p.customer_id
ORDER BY last_name ASC;
SELECT title FROM film
WHERE language_id in
(SELECT language_id 
	FROM language
	WHERE name = "English" )
AND (title LIKE "K%") OR (title LIKE "Q%");
SELECT last_name, first_name
FROM actor
WHERE actor_id in
(SELECT actor_id FROM film_actor
	WHERE film_id in 
(SELECT film_id FROM film
	WHERE title = "Alone Trip"));
SELECT country, last_name, first_name, email
FROM country c
LEFT JOIN customer cu
ON c.country_id = cu.customer_id
WHERE country = 'Canada';
SELECT title, category
FROM film_list
WHERE category = 'Family';
SELECT i.film_id, f.title, COUNT(r.inventory_id)
FROM inventory i
INNER JOIN rental r
ON i.inventory_id = r.inventory_id
INNER JOIN film_text f 
ON i.film_id = f.film_id
GROUP BY r.inventory_id
ORDER BY COUNT(r.inventory_id) DESC;
SELECT store.store_id, SUM(amount)
FROM store
INNER JOIN staff
ON store.store_id = staff.store_id
INNER JOIN payment p 
ON p.staff_id = staff.staff_id
GROUP BY store.store_id
ORDER BY SUM(amount);
SELECT s.store_id, city, country
FROM store s
INNER JOIN customer cu
ON s.store_id = cu.store_id
INNER JOIN staff st
ON s.store_id = st.store_id
INNER JOIN address a
ON cu.address_id = a.address_id
INNER JOIN city ci
ON a.city_id = ci.city_id
INNER JOIN country coun
ON ci.country_id = coun.country_id;
SELECT name, SUM(p.amount)
FROM category c
INNER JOIN film_category fc
INNER JOIN inventory i
ON i.film_id = fc.film_id
INNER JOIN rental r
ON r.inventory_id = i.inventory_id
INNER JOIN payment p
GROUP BY name
LIMIT 5;
CREATE VIEW top_five_grossing_genres AS
SELECT name, SUM(p.amount)
FROM category c
INNER JOIN film_category fc
INNER JOIN inventory i
ON i.film_id = fc.film_id
INNER JOIN rental r
ON r.inventory_id = i.inventory_id
INNER JOIN payment p
GROUP BY name
LIMIT 5;
SELECT * FROM top_five_grossing_genres;
DROP VIEW top_five_grossing_genres;

