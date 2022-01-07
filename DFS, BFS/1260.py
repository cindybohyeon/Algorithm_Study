from collections import deque


# 정점의 개수, 간선의 개수, 탐색 시작할 정점의 번호
# 간선이 연결하는 두 정점의 번호

# map 함수로 입력 받기
# 보통 여러 개의 데이터를 한번에 다른 형태로 바꾸기 위해 사용
a, b, c = map(int, input().split())
graph = [[0]* (a+1) for _ in range(a+1)]

for _ in range(b):
    m1, m2 = map(int, input().split())
    graph[m1][m2] = graph[m2][m1] = 1

visited = [False] * (a+1)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in range(1, a+1):
        if not visited[i] and graph[v][i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, a+1):
            if not visited[i] and graph[v][i]:
                queue.append(i)
                visited[i] = True


dfs(graph, c, visited)
visited = [False] * (a+1)
print()
bfs(graph, c, visited)