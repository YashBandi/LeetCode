# Write your MySQL query statement below
select e.name, b.bonus from Employee e left join Bonus b on e.empId = b.empId where b.bonus < 1000 or b.bonus is null
-- select e.name, b.bonus from Bonus b right join Employee e on e.empId = b.empId where b.bonus < 1000