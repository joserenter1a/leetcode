# Write your MySQL query statement below
with f as (
    select 
        t.teacher_id,
        count(distinct t.subject_id) as cnt
    from teacher t
    group by t.teacher_id
)

select * from f;