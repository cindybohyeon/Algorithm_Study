# from collections import deque

# n,m,k = map(int, input().split())

# graph = [[0]* (m) for _ in range(n)]

# for _ in range(k):
#     a,b = map(int,input().split())
#     graph[a-1][b-1] = 1
# # 3 4 5
# # \\\
# # 2 2
# # 3 1
# # 2 3
# # 1 1
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# nx=0
# ny=0

# # print(graph)
# def bfs(x,y,graph):
#     queue = deque()
#     queue.append((x,y))
#     global count
#     while queue:
#         x,y = queue.popleft()
#         for i in range(4):
#             # 해당 좌표 상하좌우 살피기
#             nx = x + dx[i]
#             ny = y + dy[i]
#             # 상하좌우 위치 아닌것 건너뛰기
#             if(nx<0 or ny<0 or nx>= n or ny>=m):
#                 continue
#             # 상하좌우 해당위치가 graph에 있는지 즉 똥이 있는지 확인하기
#             if(graph[nx][ny] == 1):
#                     count += 1
#                     queue.append((nx,ny))
#                     graph[nx][ny] = 0


# result = 0
# count = 0
# for i in range(n):
#     for j in range(m):
#         if(graph[i][j] == 1):
#             bfs(i,j,graph)
#             result = max(result,count)
#             count = 0


# print(result)


# 전역변수 count 사용
# max 함수 사용
# 시작 위치 바꾸면서 bfs 진행하기 


from collections import deque
n, m, k = map(int, input().split())
graph = [[0] * (m+1) for _ in range(n+1)]
for _ in range(k):
    a,b = map(int, input().split())
    graph[a][b] = 1


def in_range(x,y):
    if x > 0 and y > 0 and x <= n and y <= m:
        return True
    else:
        return False

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    count = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if in_range(nx,ny) and int(graph[nx][ny]):
                graph[nx][ny] = 0
                count += 1
                queue.append((nx,ny))
    return count
max_count = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if int(graph[i][j]):
            bfs_ = bfs(i,j)
            max_count = max(bfs_,max_count)
print(max_count)
# print(graph)
# print(bfs(2,2))