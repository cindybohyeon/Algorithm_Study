import sys
from collections import deque
# input = sys.stdin.readline()
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [[0 for _ in range(n)] for _ in range(n)]

x1, y1 = map(int, input().split())
x1, y1 = x1-1, y1-1
x2, y2 = map(int, input().split())
x2, y2 = x2-1, y2-1
# 3초에 최대를 넣는다.
visited[x1][y1] = 1
visited[x2][y2] = 1
def in_range(x, y):
    if x >= 0 and y >= 0 and x < n and y < n:
        return True
    return False

# 각자 한번씩 넣어야 한다..
# 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append((x1, y1))
q.append((x2, y2))
count = 0
result = graph[x1][y1] + graph[x2][y2]
while len(q) != 0:
    x, y = q.pop()
    max_move = 0
    moveX, moveY = 0, 0
    for a, b in zip(dx, dy):
        nx = a + x
        ny = b + y
        if in_range(nx, ny) and visited[nx][ny] == 0:
            if max_move < graph[nx][ny]:
                max_move = graph[nx][ny]
                moveX, moveY = nx, ny
    # if count < 3:
    q.append((moveX, moveY))
    count += 1
    visited[moveX][moveY] = 1
    # print(max_move)
    result += max_move


# q = deque()
# q.append((x2, y2))
# count = 0
# result += graph[x2][y2]
# while len(q) != 0:
#     x, y = q.pop()
#     max_move = 0
#     moveX, moveY = 0, 0
#     for a, b in zip(dx, dy):
#         nx = a + x
#         ny = b + y
#         if in_range(nx, ny) and visited[nx][ny] == 0:
#             if max_move < graph[nx][ny]:
#                 max_move = graph[nx][ny]
#                 moveX, moveY = nx, ny
#     if count < 3:
#         q.append((moveX, moveY))
#         count += 1
#         visited[moveX][moveY] = 1
#         # print(max_move)
#         result += max_move
print(result)