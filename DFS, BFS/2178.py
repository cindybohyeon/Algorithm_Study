from collections import deque
from types import GeneratorType

# 최단경로 문제 bfs로 푸는지를 몰랐다 ㅠㅠㅠㅠㅠㅠ




# n,m = map(int, input().split())
# graph = [list(input().strip()) for _ in range(n)]


# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
def bfs(x,y,graph):
    queue = deque()
    queue.append((x,y))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    count=0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(nx<0 or ny<0 or nx>= n or ny>=m):
                continue
            if(graph[nx][ny] == 0):
                continue
            if(graph[nx][ny] == 1):
                # count += 1
                # graph[nx][ny] = count + 1
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1
                
    return graph[n-1][m-1]


a = bfs(0,0,graph)
print(a)

