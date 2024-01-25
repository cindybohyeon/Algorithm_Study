n, k = map(int, input().split())
graph = list(map(int, input().split()))
lenGraph = []
for i in range(n-1):
    lenGraph.append(graph[i+1]-graph[i])
lenGraph.sort()
result = 0
for i in range(n-k):
    result += lenGraph[i]
print(result)