# Write your MySQL query statement below
/* Write your T-SQL query statement below */
with p as (
    select
    s1.product_id,
    f2.first_year,
    s1.quantity,
    s1.price
 
    from Sales s1
    join (
    select
    # first year of the product
    min(s2.year) as first_year,
    s2.product_id

    from Sales s2
    group by s2.product_id
    ) f2
    # use a union in the group for both the equivalence of the product and the year it was sold.
    on s1.product_id = f2.product_id
    and s1.year = f2.first_year
)

select * from p;