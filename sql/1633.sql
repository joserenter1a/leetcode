# Write your MySQL query statement below
# Percentage will be number of user_id's attended contest_id / number of user_id's
with f as (
    select
        contest_id,
        round(count(distinct user_id) * 100 /( select count(distinct user_id) from users), 2) as percentage

    from
        register 
    group by 
        contest_id
    order by
        percentage desc, contest_id
)
select * from f;
