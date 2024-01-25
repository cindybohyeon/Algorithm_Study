from collections import deque
m, n = map(int, input().split())
graph = []
for _ in range(n):
    tomatos = list(map(int, input().split()))
    graph.append(tomatos)

queue = deque([])
date = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i,j])

def in_range(x, y):
    if x >= 0 and x < n and y >= 0 and y < m:
        return True
    return False

def bfs():
    while queue:
        x, y = queue.popleft()
        for a,b in zip(dx, dy):
            nx = a + x
            ny = b + y
            if in_range(nx, ny) and graph[nx][ny] == 0:
                queue.append([nx, ny])
                # 0 인것들만 +1 해주니까 겹치지 않는다.
                # +1 하는게 날짜가 하나씩 올라가는 것.
                graph[nx][ny] = graph[x][y] + 1
                

bfs()
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit(0)
        result = max(result, graph[i][j])
print(result-1)
# print(graph)


