select name from actors A left join actor_role AR on A.AID = AR.AID
where AR.MID is null