select max(student_sum), min(student_sum)
from 
( select count(ID) student_sum from takes group by course_id, sec_id)
