select distinct I.ID, I.name, I.dept_name from instructor I , teaches T  
where I.ID == T.ID  and T.course_id like 'CS-1%'
