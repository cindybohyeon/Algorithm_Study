
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

dp[0][0] = graph[0][0]
def initialize():
    # 시작점의 경우 dp[0][0] = num[0][0]으로 초기값을 설정해줍니다
    dp[0][0] = graph[0][0]
    
    # 최좌측 열의 초기값을 설정해줍니다.
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + graph[i][0]
    
    # 최상단 행의 초기값을 설정해줍니다.
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + graph[0][j]
        
        
# 초기값 설정
initialize()

for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + graph[i][j]


print(dp[n-1][n-1])