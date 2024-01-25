import sys
input = sys.stdin.readline
from collections import deque

graph = []
n,l,r = map(int, input().split())
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]
def bfs(a,b):
    q = deque()
    temp = []
    q.append((a,b))
    temp.append((a,b))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny]==0:
                # 국경선을 공유하는 두 나라의 인구 차이를 비교하고 공유가능이면 temp
                visited[nx][ny] = 1
                q.append((nx,ny))
                temp.append((nx,ny))
    return temp                

result = 0
while 1:
    visited = [[0]*(n+1) for _ in range(n+1)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i,j)
                # 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면 인구 이동 시작
                if len(country) > 1:
                    flag = 1
                    # 연합을 이루고 있는 각 칸의 인구수 / 칸의 개수
                    number = sum([graph[x][y] for x,y in country]) // len(country)
                    for x,y in country:
                        graph[x][y] = number
    if flag == 0:
        break
    result += 1

