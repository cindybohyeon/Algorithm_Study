select distinct ins.ID, ins.name from instructor ins
left outer join teaches on teaches.ID = ins.ID
where teaches.ID is null
