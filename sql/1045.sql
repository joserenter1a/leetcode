with c as (
    
    select 
    customer_id
    from Customer
    group by customer_id
/*group by unique product ids and compare counts*/

    /*Only add distinct product keys to the count and compare the count to the count of product keys  in the product table*/
    having count(distinct product_key) = (
    select
    count(*) as pct
    from Product
    ) 
    )


select * from c;