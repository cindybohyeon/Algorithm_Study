select distinct ins.ID, ins.name from instructor ins
left outer join teaches on teaches.ID = ins.ID
where teaches.ID is null

1
SELECT name FROM instructor WHERE dept_name = 'Finance'

2
SELECT title FROM course WHERE dept_name = 'Biology' and credits = 4

3
SELECT distinct course.course_id, title FROM takes,course WHERE takes.course_id = course.course_id and ID = '45678'

4
SELECT sum(credits) FROM takes,course WHERE takes.course_id = course.course_id and ID = '45678'

5
SELECT ID, sum(credits) FROM takes,course WHERE takes.course_id = course.course_id GROUP BY ID

6
SELECT distinct name
FROM student
WHERE ID in (SELECT ID FROM takes,course WHERE takes.course_id = course.course_id and dept_name = 'Comp. Sci.')

7
SELECT ID FROM instructor except SELECT ID FROM teaches

8
SELECT ID, name
FROM instructor
WHERE ID in (SELECT ID FROM instructor except SELECT ID FROM teaches)