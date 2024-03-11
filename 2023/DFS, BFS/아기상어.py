from collections import deque
import sys
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
babyshark = 2
bs_x = 0
bs_y = 0

# 아기상어의 위치 확인하기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9: #아기상어의 위치를 찾은 경우
            bs_x = i
            bs_y = j
            # 아기 상어의 초기위치는 좌표를 저장한 뒤 0으로 초기화 해야한다 -> 이유는?

def in_range(x,y):
    if x>=0 and y>=0 and x<n and y<n:
        return True
    return False

        
def check_eating(cur_value, shark_value):
    if cur_value <= shark_value:
        return True
    return False

#  현재 아기상어위치에서 이동. 초기 값이 아기상어 좌표.
def bfs():
    queue = deque()
    queue.append((bs_x, bs_y))
    # 방문여부
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    print(visited)
    visited[bs_x][bs_y] = 0

    while queue:
        a,b = queue.pop()
        # 현재 상어 위치에서 이동가능한 좌표들 확인하기
        for i,j in zip(dx, dy):
            nx = i + a
            ny = j + b
            
            if in_range(nx, ny) and check_eating(graph[nx][ny], graph[a][b]) and visited[nx][ny] == -1:
                print(graph[nx][ny],"nxny")
                visited[nx][ny] = visited[a][b] + 1 # ??
                queue.append((nx,ny))                
                
    return visited

def can_eat(visited, x, y):
    if visited[x][y] != -1 and 1 <= graph[x][y] < babyshark:
        return True
    return False

# 먹을 물고기 찾기
def solve(visited):
    x,y = 0,0
    min_distance = 999999999999
    for i in range(n):
        for j in range(n):
            # 아기 상어가 지날 수 있었던 경로들로만 확인.
            if can_eat(visited, i,j):
                if visited[i][j] < min_distance:
                    min_distance = visited[i][j]
                    x,y = i,j
    if min_distance == 999999999999:
        return False
    else:
        return x,y,min_distance


answer = 0
food = 0

while True:
    result = solve(bfs())
    if not result:
        print(answer)
        break
    else:
        