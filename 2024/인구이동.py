n, l, r = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
union = [[0]*n for _ in range(n)]

# 가로 친구들
for i in range(n):
    for j in range(n-1):
        first = graph[i][j]
        tempPerson = graph[i][j+1]
        checking = abs(first - tempPerson)
        if checking >= l and checking <= r:
            union[i][j] = 1
            union[i][j+1] = 1

union = [[0]*n for _ in range(n)]
# 세로 친구들
for i in range(n):
    for j in range(n-1):
        first = graph[j][i]
        tempPerson = graph[j+1][i]
        checking = abs(first - tempPerson)
        if checking >= l and checking <= r:
            union[j][i] = 1
            union[j+1][i] = 1
