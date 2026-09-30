/* Write your PL/SQL query statement below */
select e.unique_id,t.name 
from Employees t
left join employeeUNI e
on t.id=e.id;
