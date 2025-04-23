/* Write your T-SQL query statement below */
with cte as (
    select
    p.product_name,
    s.year,
    s.price
    from Product p

    JOIN Sales s on s.product_id = p.product_id
)

select * from cte