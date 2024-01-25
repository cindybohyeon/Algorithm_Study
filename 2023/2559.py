# 7:40 시작

n, k = map(int, input().split())
graph = input().split()
for i in range(len(graph)):
    graph[i] = int(graph[i])
graphLen = len(graph)
forLen = graphLen - k  # 제일 마지막 원소

# 처음 더한 값
ans = []
ans.append(sum(graph[:k]))

for i in range(forLen):
    tempSum = ans[i] - graph[i] + graph[i+k]
    ans.append(tempSum)

print(max(ans))