n, m = map(int, input().split())
graph = list(map(int, input().split()))
test = []
for _ in range(m):
    test.append(list(map(int, input().split())))

dp = [0 for _ in range(n+1)]
dp[1] = graph[0]
for i in range(1, n):
    dp[i + 1] = graph[i] + dp[i]
for i, j in test:
    print(dp[j] - dp[i] + graph[i - 1])

