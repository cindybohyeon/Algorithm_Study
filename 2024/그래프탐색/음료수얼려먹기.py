from collections import deque

n, m = map(int, input().split())
graph = []
result = 0
for i in range(n):
    graph.append(list(map(int, input().split())))

def in_range(x,y):
    if x >= 0 and x < n and y >= 0 and y < m:
        return True
    return False

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global graph, dx, dy
    q = deque()
    # visited = [[0] * m for _ in range(n)]
    q.append((x,y))
    graph[x][y] = 1

    while q:
        x,y = q.popleft()
        # 인접한 노드들 중에 갈 수 있는 거 확인하기, 갈 수만 있다면 다 넣는다 = 너비우선탐색
        for a, b in zip(dx, dy):
            nx, ny = x + a, y + b
            if in_range(nx, ny) and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append((nx,ny))
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            result += 1
            bfs(i,j)

print(result)



