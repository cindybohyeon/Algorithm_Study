select takes.id, sum(course.credits) from course
join takes on course.course_id = takes.course_id
group by takes.id
