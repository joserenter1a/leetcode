/* Write your T-SQL query statement below */
/*
Cartesian product or cross join. Creates every possible pairing as a join
*/
with cte as (
    select
    today.id
    from weather yesterday
    cross join weather today
    where datediff(day, yesterday.recorddate, today.recorddate) = 1
    and today.temperature > yesterday.temperature

)
select * from cte;