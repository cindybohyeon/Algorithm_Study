from collections import deque
X, Y, d, t = map(int, input().split())

graph = [[0 for _ in range(Y + 1)]for _ in range(X + 1)]
print(graph)
def in_range(a, b):
    if a >= 0 and b >= 0 and a <= X and b <= Y:
        return True
    return False

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
queue.append((0,0))
while(len(queue) != 0):
    x, y = queue.pop()
    print(x, y, "x, y")
    for a, b in zip(dx, dy):
        nx = x + a
        ny = y + b
        print(nx, ny, "nx")
        if in_range(nx, ny) and graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1

            queue.append((nx, ny))

print(graph)
    