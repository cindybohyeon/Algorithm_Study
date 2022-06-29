select name, occupation
from
(
select ID1, num
from 
(select ID1, count(ID1) num
from people_friends PF
group by ID1)
where num >= 3
) PP
join people_main P on P.ID = PP.ID1
