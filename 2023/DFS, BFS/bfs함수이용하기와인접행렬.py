
from collections import deque
from types import GeneratorType
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
# 주어진 위치가 격자를 벗어나는지 여부를 반환합니다.
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


# 주어진 위치로 이동할 수 있는지 여부를 확인합니다.
def can_go(x, y):
    return in_range(x, y) and graph[x][y] 

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
            # if(nx<0 or ny<0 or nx>= n or ny>=m):
            #     continue
            # if(graph[nx][ny] == 0):
            #     continue
            if(can_go(nx,ny)):
                # count += 1
                # graph[nx][ny] = count + 1
                queue.append((nx,ny))
                graph[nx][ny] = 0



a = bfs(0,0,graph)
answer = 0 if graph[n - 1][m - 1] else 1
print(answer)