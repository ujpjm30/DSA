# Write your MySQL query statement below
select Department.name as Department, Ranked.name as Employee, Ranked.salary as Salary
from (select name, salary, departmentId, dense_rank() over (partition by departmentId order by salary desc) as salary_rank from Employee) Ranked
join Department on Ranked.departmentId = Department.id
where Ranked.salary_rank <= 3;