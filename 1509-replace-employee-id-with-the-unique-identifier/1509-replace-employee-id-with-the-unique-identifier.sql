# Write your MySQL query statement below
SELECT u.unique_id, e.name
FROM Employees AS e
LEFT JOIN EmployeeUNI as U
ON e.id = u.id;