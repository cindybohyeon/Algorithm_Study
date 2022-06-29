select distinct(P.name), P.ID, PL.ID2, (select (name) from people_main where ID = PL.ID2) friend_name
from people_main P
left join people_likes PL on P.ID = PL.ID1
left join people_friends PF on P.ID = PF.ID1
where PL.ID2 <> PF.ID2
