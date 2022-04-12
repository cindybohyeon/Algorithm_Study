select distinct(stu.name) from student stu
join takes on stu.ID = takes.ID
join course on takes.course_ID = course.course_id
where course.dept_name = 'Comp. Sci.'
