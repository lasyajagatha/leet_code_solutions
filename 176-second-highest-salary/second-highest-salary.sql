# Write your MySQL query statement belo
SELECT max(salary) AS SecondHighestSalary
FROM Employee
WHERE salary!=(SELECT max(salary) FROM Employee);

