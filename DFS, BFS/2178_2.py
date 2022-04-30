# 집중 . 이게 시험이라고 생각하기
from collections import deque
import queue
n,m = map(int, input().split())
graph = []
for i in range(n):
    # list로 묶지 않으면 map의 이상한 것이 출력된다 
    graph.append(list(map(int, input())))

# print(graph)
global visited 
visited = [[False for _ in range(m)] for _ in range(n)]


def in_range(x,y):
    if x >=0 and y >=0 and x < n and y < m:
        return True
    else:
        return False
global count
count = 0


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    global count
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if in_range(nx,ny) and graph[nx][ny] == 1:
                queue.append((nx,ny))
                



def bfs(x,y):
    # vistied[x][y] = True
    queue = deque()
    queue.append((x,y))
    # count += 1
    global count
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if in_range(nx,ny) and graph[nx][ny] == 1:
                queue.append((nx,ny))
                visited[nx][ny] = True
                # bfs(nx,ny)
                count += 1
                graph[nx][ny] = graph[x][y] + 1


bfs(0,0)
print(graph[n-1][m-1])