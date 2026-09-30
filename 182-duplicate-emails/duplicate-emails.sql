/* Write your PL/SQL query statement below */
 SELECT distinct p.email as Email
FROM Person p
where email  in (select email from person where id!=p.id);