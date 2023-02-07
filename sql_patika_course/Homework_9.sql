--*********1.Question

SELECT city, country FROM city
INNER JOIN  country ON country.country_id = city.country_id;

--*********2.Question
SELECT payment_id, first_name, last_name FROM payment
INNER JOIN customer ON payment.customer_id = customer.customer_id;

--*********3.Question
SELECT rental_id, first_name, last_name FROM rental
INNER JOIN customer ON rental.customer_id = customer.customer_id;
