select distinct(P.name), P.birth_year from people_main P
join people_likes PL on P.ID = PL.ID2
join people_main P2 on P2.ID = PL.ID1
where P.birth_year < P2.birth_year
