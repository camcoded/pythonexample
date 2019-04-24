use sakila;
 -- select distinct category from film_list 
 -- select count(*) from actor where substring(last_name,1,1)='B'
 -- select count(*), first_name, last_name from actor where first_name='FAY' or last_name='WOOD';
  -- select count(*), first_name from actor where first_name= 'TOM' or first_name= 'RAY' or 'GRETA' or 'JULIA';
  -- select customer.customer_id,customer.first_name,customer.last_name,sum(amount) from payment inner join customer on payment.customer_id = customer.customer_id group by customer_id;
-- select city, country from city inner join country on city.country_id = country.country_id;
 -- select address,address2,city from address inner join city on address.city_id = city.city_id;
 -- select actor.first_name, actor.last_name, film.title from film_actor inner join actor on film_actor.actor.id = actor.actor_id inner join film on film_actor.film_id = film.film_id;
  -- insert into language(name) values ('Polish');
 -- describe language
 -- insert into language(name) values ('Swaheli');
 -- select * from language
select * from film_text order by film_id;
insert into film_text values (1001, 'My title', 'Description 1')

