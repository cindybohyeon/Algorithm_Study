# n = int(input())
# graph = [ list(map(int, input().split())) for _ in range(n)]

# sum = 0

# def threemap(x1,y1,x2,y2):
#     sum = 0
#     for i in range(x1,x2+1):
#         for j in range(y1,y2+1):
#             sum += graph[i][j]
#     return sum

# # 정답을 담는 변수 생성 -> 그래야 나중에 코드볼 때 편하다!
# max_count = 0
# for row in range(n):
#     for col in range(n):
#         if(row+2 >= n or col+2 >= n):
#             continue
#         # max 함수 사용
#         max_count = max(max_count,threemap(row, col, row+2, col+2))

# print(max_count)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


def sum_three(low, col):
    sum = 0
    for i in range(low, low+3):
        for j in range(col, col+3):
            sum += arr[i][j]
    return sum

max_result = 0

for low in range(n):
    for col in range(n):
        if(col+2 >= n or low+2 >= n):
            continue
        result = sum_three(low, col)
        max_result = max(max_result, result)

print(max_result)