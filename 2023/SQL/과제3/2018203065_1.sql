select movies.title, count(rolename) from actor_role AR 
left join actors A on AR.AID = A.AID 
join movies on AR.MID = movies.MID
where A.name = 'Tilda Swinton'
group by AR.MID