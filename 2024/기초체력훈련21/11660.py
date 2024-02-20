n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
test = []
for _ in range(m):
    test.append(list(map(int, input().split())))

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

# 양 끝 대각선 채우기

for i in range(n):
    dp[0][i + 1] = dp[0][i] + graph[0][i]
for j in range(n - 1):
    dp[j + 1][1] = dp[j][1] + graph[j + 1][0]
# print(dp)
for i in range(n - 1):
    for j in range(1, n):
        dp[i + 1][j + 1] = dp[i + 1][j] + dp[i][j + 1] - dp[i][j] + graph[i + 1][j]
# print(dp)
        
for x1, y1, x2, y2 in test:
    # print(dp[x2 - 1][y2], dp[x1 - 2][y2], "@")
    print(dp[x2 - 1][y2] - dp[x1 - 1 - 1][y2] - dp[x2 - 1][y1 - 1] + dp[x1 -1 - 1][y1 - 1])        