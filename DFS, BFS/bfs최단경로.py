# import sys
# from collections import deque

# INT_MAX = sys.maxsize

# # 변수 선언 및 입력
# n, m = tuple(map(int, input().split()))

# a = [
#     list(map(int, input().split()))
#     for _ in range(n)
# ]

# # bfs에 필요한 변수들 입니다.
# q = deque()
# visited = [
#     [False for _ in range(m)]
#     for _ in range(n)
# ]
# # step[i][j] : 시작점으로부터 (i, j) 지점에 도달하기 위한 
# # 최단거리를 기록합니다.
# step = [
#     [0 for _ in range(m)]
#     for _ in range(n)
# ]

# ans = INT_MAX

# def in_range(x, y):
#     return 0 <= x and x < n and 0 <= y and y < m


# # 격자를 벗어나지 않으면서, 뱀도 없고, 아직 방문한 적이 없는 곳이라면
# # 지금 이동하는 것이 최단거리임을 보장할 수 있으므로 가야만 합니다. 
# def can_go(x, y):
#     return in_range(x, y) and a[x][y] and not visited[x][y]


# # queue에 새로운 위치를 추가하고
# # 방문 여부를 표시해줍니다.
# # 시작점으로 부터의 최단거리 값도 갱신해줍니다.
# def push(new_x, new_y, new_step):
#     q.append((new_x, new_y))
#     visited[new_x][new_y] = True
#     step[new_x][new_y] = new_step
    
    
# # bfs를 통해 최소 이동 횟수를 구합니다.
# def find_min():
#     global ans
    
#     dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    
#     # queue에 남은 것이 없을때까지 반복합니다.
#     while q:
#         # queue에서 가장 먼저 들어온 원소를 뺍니다.
#         x, y = q.popleft()    
    
#         # queue에서 뺀 원소의 위치를 기준으로 4방향을 확인해봅니다.
#         for dx, dy in zip(dxs, dys):
#             new_x, new_y = x + dx, y + dy
        
#             # 아직 방문한 적이 없으면서 갈 수 있는 곳이라면
#             # 새로 queue에 넣어줍니다.
#             if can_go(new_x, new_y):
#                 # 최단 거리는 이전 최단거리에 1이 증가하게 됩니다.
#                 push(new_x, new_y, step[x][y] + 1)
    
#     # 우측 하단에 가는 것이 가능할때만 답을 갱신해줍니다.
#     if visited[n - 1][m - 1]:
#         ans = step[n - 1][m - 1]

# # bfs를 이용해 최소 이동 횟수를 구합니다.
# # 시작점을 queue에 넣고 시작합니다.
# push(0, 0, 0)
# find_min()

# # 불가능한 경우라면 -1을 답으로 넣어줍니다.
# if ans == INT_MAX:
#     ans = -1
    
# print(ans)




# from sys import stdin
# N, M = map(int, stdin.readline().split())
# # matrix 배열
# matrix = [list(map(int, input().split())) for _ in range(N)]
# # 방문경로 배열
# visited = [[0]*M for _ in range(N)]
# # 좌/우/위/아래 방향 이동
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# # BFS 경로 탐색
# # queue 방식 사용
# queue = [(0,0)]
# visited[0][0] = 1

# while queue:
#     x, y = queue.pop(0)

#     if x == N-1 and y == M-1:
#         # 최종 경로 도착
#         print(visited[x][y])
#         break

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < N and 0 <= ny < M:
#             if visited[nx][ny] == 0 and matrix[nx][ny] == '1':
#                 visited[nx][ny] = visited[x][y] + 1
#                 queue.append((nx,ny))


from collections import deque
import sys
INT_MAX = sys.maxsize
n, m = tuple(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[0 for _ in range(m) ] for _ in range(n)]

def in_range(x,y):
    return x >= 0 and y >= 0 and x < n and y < m

def can_go(x,y):
    return in_range(x,y) and graph[x][y] and not visited[x][y] 

count = 0

def bfs(x,y,graph):
    
    global count
    queue = deque()
    queue.append((x,y))

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while queue:
        queue.popleft()

        if x == n-1 and y == m-1:
            print(count)
            break

        for i,j in zip(dx,dy):
            nx = x + i
            ny = y + j
            if(can_go(nx,ny)):
                queue.append((nx,ny))
                visited[nx][ny] = 1
                count += 1