# Write your MySQL query statement below
SELECT name as Employee
FROM Employee c
WHERE salary > (SELECT salary FROM Employee p WHERE p.id=c.managerId  );