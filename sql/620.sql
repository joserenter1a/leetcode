# Write your MySQL query statement below
with o as (
    select *
    from cinema c
    where mod(id, 2) = 1
    and description <> 'boring'
    order by rating desc
)
select * from o;