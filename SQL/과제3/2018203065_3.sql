select distinct(name), movies.title from actors A 
left join actor_role AR on A.AID = AR.AID
left join movies on AR.MID = movies.MID
