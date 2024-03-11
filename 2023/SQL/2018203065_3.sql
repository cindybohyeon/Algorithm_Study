select distinct(takes.course_id) , course.title  from takes 
join course on takes.course_id = course.course_id where id = '45678' 
