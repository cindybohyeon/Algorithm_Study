select count(PL.ID2) count, name from people_main P
join people_likes PL on P.ID = PL.ID1
join people_likes PL2 on PL2.ID1 = PL.ID2
where PL2.ID2 = PL.ID1
group by P.ID 
order by count desc
