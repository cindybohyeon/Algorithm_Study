# N명의 학생정보가 있다. 학생정보는 이름과 성적으로 구분된다. 이름성적 주어질때 성적낮은순으로 이름 출력하기

n = int(input())
arr = []
# string과 int를 한 줄로 입력받기 
for _ in range(n):
    element = input().split()
    # append는 하나의 argument만 들어간다 이때 순서쌍은 ()로 이용한다. []는 불가함.
    arr.append((element[0], int(element[1])))

# 암기 암기 암기
arr.sort(key=lambda x : x[1])

for i in range(n):
    print(arr[i][0])