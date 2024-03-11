# 입력
n, r, c = map(int, input().split())
    # arr 입력방식에서, 0부터 넣지 않고 1부터 넣게한다. [1][1]부터 넣게 한다.

arr = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]

for i in range(1, n + 1):
    given_row = list(map(int, input().split()))
    for j in range(1, n+1):
        arr[i][j] = given_row[j-1]

    # for j, elem in enumerate(given_row, start = 1):
    #     arr[i][j] = elem

visited = [arr[r][c]]

def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n

def can_go(x,y,cur_num):
    return in_range(x,y) and arr[x][y] > cur_num

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def find_big():
    global r,c
    for i in range(4):
        nx = dx[i] + r
        ny = dy[i] + c
        if(can_go(nx,ny,arr[r][c])):
            r,c = nx,ny
            # visited.append(arr[nx][ny])
            # 한번만 들어오면 끝나게 return 넣어줌
            return True
    return False


while True:
    # 조건에 맞춰 움직여봅니다.
    greater_number_exist = find_big()
    
    # 인접한 곳에 더 큰 숫자가 없다면 종료합니다.
    if not greater_number_exist:
        break
    
    # 움직이고 난 후의 위치를 답에 넣어줍니다.
    visited.append(arr[r][c])



# 출력
for i in range(len(visited)):
    print(visited[i], end=" ")

#     # 출력:
# for num in visited:
#     print(num, end=' ')

for i in visited:
    print(i , end=' ')




# # 1. 입력
# n,r,c = map(int, input().split())
# # n+1으로 입력받는 것에 맞추기. 
# graph = [
#     [0 for _ in range(n + 1)]
#     for _ in range(n + 1)
# ]
# for i in range(1, n + 1):
#     given_row = list(map(int, input().split()))
#     for j, elem in enumerate(given_row, start = 1):
#         # for index, value in enumerate(리스트, start=숫자)
#         # start index를 1로 한다. 
#         graph[i][j] = elem

# # 2. 결과값
# visited_nums = []


# # 3. 함수 이용하기
# # def in_range(newx, newy):
# #     #격자 안에 있다.
# #     return 1 <= newx and newy >= 1 and newx =< n and newy =< n
# def in_range(x, y):
#     return 1 <= x and x <= n and 1 <= y and y <= n

# def can_go(newx,newy,curr_num):#격자 안에 있고, 해당 원소 값보다 더 크다.
#     return in_range(newx,newy) and graph[newx][newy] > curr_num

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# # 해당 r,c에서, 상하좌우 중에 제일 큰 것으로 rc가 변한다. 
# def findbig():
#     global r
#     global c
#     for i in range(4):
#         newx = r + dx[i]
#         newy = c + dy[i]
#         if can_go(newx,newy,graph[r][c]):
#             r = newx
#             c = newy
#             return True
#     # 한번 상하좌우 순회할 때 이동할 곳이 없는 경우
#     return False


# # 4.  여러번 순회하기. 
# visited_nums.append(graph[r][c])
# while True:
#     big_exist = findbig()
#     if not big_exist:
#         break
#     visited_nums.append(graph[r][c])

# # 5. 출력하기
# # leng = int(len(visited_nums))
# # for i in leng:
# #     print(visited_nums[i], end=" ")
# # 이거는 이중배열일 때 하는것. 

# for num in visited_nums:
#     print(num, end=' ')
