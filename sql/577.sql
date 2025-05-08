/* Write your T-SQL query statement below */
with bo as (
    select
    e.name name, 
    b.bonus bonus
    from Employee e
    left join Bonus b on e.empId = b.empId

)

select name, bonus from bo where bonus < 1000 or bonus is null;