# from collections import deque


# n, m = map(int, input().split())
# # graph = [list(input()) for _ in range(m)]
# graph = [list(input().strip()) for _ in range(n)]

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def bfs(x,y,team):
#     queue = deque()
#     queue.append((x,y))
#     count = 0
#     nx = 0
#     ny = 0
#     while queue:
#         x,y=queue.popleft()
#         for i in range(4):
#             nx = dx[i] + x
#             ny = dy[i] + y
#             if nx<0 or ny<0 or nx >= n or ny >= n:
#                 continue # 아래의 if 넘어가서 for문 다음 i 로 이동
#             if graph[nx][ny] != 0 and graph[nx][ny] == team:
#                 queue.append((nx,ny))
#                 graph[nx][ny] = 0
#                 count += 1
#     return (1 if count == 0 else count)



# w = 0
# b = 0


# # 방문 표시를 하기 때문에 
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] != 0:
#             if graph[i][j] == "W":
#                 w += bfs(i,j,graph[i][j])**2
#             if graph[i][j] == 'B':
#                 b += bfs(i,j,graph[i][j])**2

# print(w,b)

from collections import deque
n,m = map(int, input().split())
# 이중 배열 입력 받기
graph = [list(input()) for _ in range(m)]
visited = [[0] * (n) for _ in range(m)]

def in_range(x,y):
    if x >= 0 and y >= 0 and x < n and y < n:
        return True
    else:
        return False


def bfs(x,y, team):
    count = 1
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    while queue:
        x,y = queue.popleft()
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]     
            if in_range(nx,ny) and not visited[nx][ny]:
                if graph[nx][ny] == team:
                    count += 1
                    queue.append((nx,ny))
                    visited[nx][ny] = 1
    if count == 0 : return 1
    else: return count


w = 0
b = 0

# 방문 표시를 하기 때문에 
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            if graph[i][j] == "W":
                w += bfs(i,j,graph[i][j])**2
            if graph[i][j] == 'B':
                b += bfs(i,j,graph[i][j])**2

# bfs(0,0,graph[0][0])
# print(bfs(0,0,graph[0][0]))
print(w,b)


