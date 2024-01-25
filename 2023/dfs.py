# 깊이 우선 탐색으로 특정 노드 방문하고 연결된 모든 노드 방문
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 방문하지 않은 경우
    if graph[x][y] == 0:
        # 방문처리
        graph[x][y] = 1
        # 상하좌우 재귀적으로 호출
        dfs(x-1 , y)
        dfs(x , y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

