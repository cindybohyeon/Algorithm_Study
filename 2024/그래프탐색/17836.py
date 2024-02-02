from collections import deque

def in_range(x, y, nn, mm):
    if (x >= 0 and x < nn and y >= 0 and y < mm):
        return True
    return False

n, m, t = map(int, input().split())
graph = []
gun = -1
checkX, checkY = 0, 0
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 2:
            checkX = i + 1
            checkY = j + 1


def bfs(x, y, aa, bb):
    global graph, gun
    visited = [[-1] * bb for _ in range(aa)]
    # print(visited,"uv")
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        if (x == aa - 1 and y == bb - 1): # 공주에게 도착한 경우
            if gun != -1:
                return min(visited[x][y], gun)
            else:
                return visited[x][y]

        for a, b in zip(dx, dy):
            nx, ny = a + x, b + y
            if in_range(nx, ny, aa, bb) and graph[nx][ny] != 1 and visited[nx][ny] == -1:
                if graph[nx][ny] == 2:
                    # 검을 찾은 경우
                    gun = n - 1 - nx + m - 1 - ny + visited[x][y] + 1
                visited[nx][ny] = visited[x][y] + 1
                # print(nx, ny, "nx, ny")
                queue.append((nx, ny))
    # print(visited,"visites")
    
    return -1
    

# 검 찾는 최단거리를 구한다.
# gun = bfs(0, 0, checkX, checkY)
basic = bfs(0, 0, n, m)
# print(basic, "na")
if (basic == - 1 and -1 < gun <= t):
    print(gun)
elif (-1 < basic <= t):
    print(basic)
else:
    print("Fail")
    
#     # 검의 최단거리 값이 있을 경우
#     gun += (n - checkX) + (m - checkY)
#     realResult = min(gun, basic)
#     # 기본으로 최단거리 구하기
#     if (-1 < realResult <= t):
#         print(realResult)
#     else:
#         print("Fail")
# else:
#     if (-1 < basic <= t):
#         # print(basic)
#         print(basic)
#     else:
#         print("Fail")



