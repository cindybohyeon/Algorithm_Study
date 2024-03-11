from collections import deque

def bfs(graph, start, visited):
    # 큐에 삽입하고 방문처리 한다.
    queue = deque([start])
    visited[start] = True

    # 꺼내면서 인접 노드를 넣는다. 
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

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

bfs(graph,1,visited)