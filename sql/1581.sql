/* Write your T-SQL query statement below */
with cte as (

    select 
    v.customer_id,
    count(v.visit_id) as count_no_trans
    from visits v

    left join transactions t
    on v.visit_id = t.visit_id
    where transaction_id is null
    group by customer_id
) 
select * from cte