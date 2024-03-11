def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]
# 그래프 문제는 노드의 번호가 1번부터 시작하는 경우가 많아서, graph[0] = []으로 지정
# graph[해당노드] = [인접한 노드1, 인접한 노드2, ...]

visited = [False] * 9

dfs(graph,1,visited)