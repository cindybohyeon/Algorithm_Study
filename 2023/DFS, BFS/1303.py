# 하얀 옷과 파란 옷
# N명이 뭉쳐있을 때, N^2의 위력을 낼 수 있다.
# 
from collections import deque

a, b = map(int, input().split())

# a, b = input().split() 가능하다
# 하지만, 디폴트의 자료형은 문자열이기 때문에
# map (변환자료형, input().split())으로 int로 변환


# list이용해서 입력 받기 
graph = [list(input()) for _ in range(b)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y, team):
    queue = deque()
    queue.append((x,y))
    count = 0
    while queue:
        v = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>0 or ny<0 or nx>=a or ny>=b:
                continue
            if graph[nx][ny] != 0 and graph[nx][ny] == team:
                queue.append((nx,ny))
                graph[nx][ny] = 0 # visited 대신 사용 
                count += 1
    return (1 if count == 0 else count)

w = 0
bb = 0

for i in range(a):
    for j in range(b):
        if graph[i][j] != 0:
            if graph[i][j] == "W":
                w += bfs(i,j,graph[i][j])**2
            if graph[i][j] == "B":
                bb += bfs(i,j,graph[i][j])**2
            


print(w,bb)