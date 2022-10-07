--*********1.Question
SELECT country FROM country
WHERE country LIKE 'A%a';

--*********2.Question
SELECT country FROM country
WHERE country LIKE '_____%n';

--*********3.Question
SELECT title FROM film
WHERE title ILIKE '%T%T%T%T%';

--*********4.Question
SELECT * FROM film
WHERE title LIKE 'C%' AND length > 90 AND rental_rate = 2.99;
