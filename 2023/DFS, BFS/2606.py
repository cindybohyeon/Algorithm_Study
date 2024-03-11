# 바이러스가 


# 한 컴에 걸리면, 연결되어 있는 모든 컴퓨터도 바이러스에 걸린다. 
# 1번이 걸리면 
# n = int(input())
# m = int(input())
# graph = [[]*n for _ in range(n+1)]

# # 1-2
# # 2-3, 1-5, 5,2 5,6 ,

# # 왜 두번째가 6이지?

# computer = map(int, input())
# connect = map(int, input())

# # graph = [list(map(int, input().split()))]
# graph = [list(input().strip()) for _ in range(computer)]


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
# print(graph)
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)

# print(graph)
# list 
# 라서 1이 들어가지않는다?
global count
count = 0
def dfs(v, visited, graph) :
    global count
    visited[v] = True
    for i in graph[v] :
        if visited[i] == False :
            count += 1
            dfs(i, visited, graph)

        # count += 1
        # graph[x][y] = 0
        # dfs(x-1,y)
        # dfs(x+1, y)
        # dfs(x,y-1)
        # dfs(x,y+1)
dfs(1,visited, graph)
print(count)

    # 인접한 노드를 방문해야 한다 




# 입력받기 연습하기 .. 파이썬
# DFS 의 그래프 위치들 잘 생각하기 