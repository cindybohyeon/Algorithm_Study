select sum(course.credits) from course
join takes on course.course_id = takes.course_id
where takes.id = '45678'
