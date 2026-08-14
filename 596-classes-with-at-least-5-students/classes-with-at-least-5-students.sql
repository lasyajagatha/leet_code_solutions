/* Write your PL/SQL query statement below */
SELECT class as class
From Courses
group by class
having count(class)>=5;
