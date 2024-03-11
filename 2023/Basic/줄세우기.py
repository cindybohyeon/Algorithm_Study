# class Fruit:
#     def __init__(self, fresh, price):
#         self.fresh = fresh
#         self.price = price

# fresh = [3,5,3,2,1]
# price = [5,4,3,6,2]

# fruits = [
#     Fruit(fresh[i], price[i])
#     for i in range(5)
# ]
# fruits.sort(key = lambda x: (x.fresh, x.price))

# 튜플 람다 정렬하기
# list.sort(key = lambda x : (x.a1, x.a2))
# list.sort(key = lambda x : (x.a1, -x.a2)) : a1같으면 a2 내림차순.
# 오름차순으로 정렬된다 a1의 오름차순으로 정렬되는데 a1이 같으면, a2의 오름차순 정렬. 

class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

n = int(input())
# graph = [ list(map(int, input().split())) for _ in range(n)]
students = []
for i in range(1,n+1):
    h, w = map(int, input().split())
    Student(h,w,i)
    students.append(Student(h,w,i))

students.sort(
    key = lambda x :
    (-x.height,-x.weight,x.number) 
)

for i in range(n):
    print(students[i].height, students[i].weight, students[i].number)
