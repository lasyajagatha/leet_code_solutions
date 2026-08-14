/* Write your PL/SQL query statement below */
SELECT max(num) as num
from MyNumbers 
where num  in(
SELECT  num 
FROM MyNumbers
group by num
having count(num)=1
);