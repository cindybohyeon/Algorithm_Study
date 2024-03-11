select distinct ins.ID from instructor ins
left outer join teaches on teaches.ID = ins.ID
where teaches.ID is null
