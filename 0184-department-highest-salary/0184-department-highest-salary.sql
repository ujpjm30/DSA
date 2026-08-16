# Write your MySQL query statement below
select d.name as Department, e.name as Employee, e.salary as Salary

from Employee e

join (

    select departmentId, max(salary) as max_salary

    from Employee

    group by departmentId

) x

on e.departmentId = x.departmentId

and e.salary = x.max_salary

join Department d on e.departmentId = d.id;
