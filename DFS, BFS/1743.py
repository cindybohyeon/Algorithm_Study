from collections import deque

n,m,k = map(int, input().split())

graph = [[0]* (m) for _ in range(n)]

for _ in range(k):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1
# 3 4 5
# \\\
# 2 2
# 3 1
# 2 3
# 1 1
dx = [-1,1,0,0]
dy = [0,0,-1,1]
nx=0
ny=0

# print(graph)
def bfs(x,y,graph):
    queue = deque()
    queue.append((x,y))
    global count
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            # 해당 좌표 상하좌우 살피기
            nx = x + dx[i]
            ny = y + dy[i]
            # 상하좌우 위치 아닌것 건너뛰기
            if(nx<0 or ny<0 or nx>= n or ny>=m):
                continue
            # 상하좌우 해당위치가 graph에 있는지 즉 똥이 있는지 확인하기
            if(graph[nx][ny] == 1):
                    count += 1
                    queue.append((nx,ny))
                    graph[nx][ny] = 0


result = 0
count = 0
for i in range(n):
    for j in range(m):
        if(graph[i][j] == 1):
            bfs(i,j,graph)
            result = max(result,count)
            count = 0


print(result)


# 전역변수 count 사용
# max 함수 사용
# 시작 위치 바꾸면서 bfs 진행하기 
