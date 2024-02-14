import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

test = []
for _ in range(m):
    test.append(list(map(int, input().split())))


# def findSum(x1, y1, x2, y2):
#     global graph
#     xLen = x2 - x1 + 1
#     yLen = y2 - y1 + 1
#     dp = [[0 for _ in range(yLen)] for _ in range(xLen)]
#     dp[0][0] = graph[x1][y1]
#     # print(dp)

#     # i
#     for i in range(1, xLen):
#         dp[i][0] = dp[i - 1][0] + graph[x1 + i][y1]

#     # j
#     for j in range(1, yLen):
#         dp[0][j] = dp[0][j - 1] + graph[x1][y1 + j]

#     # print(dp, "dd")
#     for i in range(xLen - 1):
#         for j in range(yLen - 1):
#             dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j] + graph[x1 + i + 1][y1 + j + 1] - dp[i][j]
    
#     # print(dp)
#     return dp[xLen - 1][yLen - 1]
    
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
# dp[0][0] = graph[0][0]
# for i in range(1, n):
#     dp[0][i] = graph[0][i] + dp[0][i-1]
#     dp[i][0] = graph[i][0] + dp[i-1][0]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + graph[i - 1][j - 1] - dp[i-1][j-1]

print(dp, "dp")
# dp2 = [[0]*(n+1) for i in range(n+1)]

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         dp2[i][j] = dp2[i][j-1] + dp2[i-1][j] - dp2[i-1][j-1] + graph[i-1][j-1]

# print(dp2,"dp2")
for x1, y1, x2, y2 in test:
    ans = 0

    ans = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    # print("a", ans)
    # for i in range(0, y1-1):
    #     ans -= dp[x2-1][i]
    # for i in range(0, x1-1):
    #     ans -= dp[i][y2-1]
    print(ans)

    

# dp 같다.
# dp[n]은 0부터 n까지 의 합.
    
