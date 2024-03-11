n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m+1)] for _ in range(n)]

# 아래, 오른쪽 이동
dx = [1,0]
dy = [0,1]

count = 0

# 함수 이용
def in_range(nx,ny):
    return nx >= 0 or ny >= 0 or nx < n or ny < m
# def in_range(x, y):
#     return 0 <= x and x < n and 0 <= y and y < m

def can_go(x,y):
    return in_range(x,y) and graph[x][y] == 1 and visited[x][y] == 0

def dfs(x,y):
    for i in range(2):
        new_x = dx[i] + x
        new_y = dy[i] + y
        if can_go(new_x, new_y):
            visited[new_x][new_y] = 1
            dfs(new_x, new_y)

     
visited[0][0] = 1
dfs(0,0)
print(visited[n-1][m-1])

# visited = [False for _ in range(N+1)]
# def dfs(vertex, graph):
#     '''
#     :return : vertex 에서 갈 수 있는 모든 정점을 간다
#     '''
#     visited[vertex] = True
#     for adj in (vertex랑 연결된 모든 정점):
#         if not visited[adj]
#         # adj에서 다시 갈 수 있는 모든 정점을 확인
#         dfs(adj, graph)