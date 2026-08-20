# Write your MySQL query statement below
select Department.name as Department, Employee.name as Employee, Employee.salary as Salary
from Employee
join (select departmentId, max(salary) as max_salary from Employee group by departmentId) x on Employee.departmentId = x.departmentId and Employee.salary = x.max_salary
join Department on Employee.departmentId = Department.id;
