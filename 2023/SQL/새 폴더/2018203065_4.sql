insert into student (ID, name, dept_name, tot_cred) 
select I.ID, I.name, I.dept_name, 0 from instructor I where I.ID <= 60000 