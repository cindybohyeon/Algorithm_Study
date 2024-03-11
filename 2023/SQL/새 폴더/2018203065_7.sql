update instructor set salary =
( select
 case
 when count(sec_id) is not null then 50000 * count(sec_id)
 end
  from teaches 
 where instructor.ID = teaches.ID
 group by ID
 );
update instructor set salary = 30000
where salary is null
