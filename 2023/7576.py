import copy
m, n = map(int, input().split())
graph = []
for _ in range(n):
    tomatos = list(map(int, input().split()))
    graph.append(tomatos)

# 0 인 경우는 1인접 이면 1로 변한다.

date = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def in_range(x, y):
    if x >= 0 and x < n and y >= 0 and y < m:
        return True
    return False

def checkTomato(x, y):
    global graph
    for a,b in zip(dx, dy):
        nx = a + x
        ny = b + y
        if in_range(nx, ny) and graph[nx][ny] == 0:
            graph[nx][ny] = 1
 
def isAllTomato():
    # 0이 한 개라도 있으면 False
    global graph
    global date
    global n, m
    for i in range(n):
        for j in range(m):
            if (graph[i][j] == 0):
                return False
    return True

while(1):
    if isAllTomato() == True: # n*m
        break
    date += 1
    initgraph = copy.deepcopy(graph)
    oneTomato = []
    # 같은 날에 토마토 1인 좌표들 저장
    for i in range(n): # n*m
        for j in range(m):
            if graph[i][j] == 1:
                oneTomato.append((i,j))
    # n*m*4
    for i,j in oneTomato:
        checkTomato(i, j)
    tempgraph = copy.deepcopy(graph)
    # 변한게 없으면 모두 익지는 못하는 상황
    if (initgraph == tempgraph):
        date = -1
        break

print(date)