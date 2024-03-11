'''
인접리스트 
'''

# n, m = map(int, input().split())
# visited = [ 0 for _ in range(n+1)]
# list_ = [[] for _ in range(n+1)]
# for i in range(m):
#     x, y = map(int, input().split())
#     list_[x].append(y)
#     list_[y].append(x)
    
# count = 0
# def dfs(v,visited,list_):
#     global count, n
#     visited[v] = 1

#     for i in list_[v]:
#         if visited[i] ==0:
#             count += 1
#             dfs(i,visited,list_)

# dfs(1,visited,list_)
# print(count)

n, m = map(int, input().split())
visited = [ 0 for _ in range(n+1)]
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1


count = 0
def dfs(v,visited,graph):
    global count, n
    visited[v] = 1

    for i in range(1,n+1):
        if visited[i] == 0 and graph[v][i]:
            dfs(i,visited,graph)
            count += 1
            

dfs(1,visited,graph)                      
print(count)
''''
인접행렬
''''