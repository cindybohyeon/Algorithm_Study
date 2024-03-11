import sys
INT_MAX = sys.maxsize

# n가지 종류의 화폐
# 개수를 최소화해서 합이 m원이 되도록 한다. 
n,m = map(int, input().split())
coin = []
for _ in range(n):
    a = int(input())
    coin.append(a)

# i원이 되는 최소개수
dp = [ 0 ] * (m+1)

def initialize():
    for i in range(m+1):
        dp[i] = INT_MAX
    dp[0] = 0

initialize()

for i in range(1,m+1):
    for j in range(n):
        if i >= coin[j]:
            dp[i] = min((dp[i-coin[j]] + 1), dp[i])

if dp[m] == INT_MAX:
    print(-1)
else:
    print(dp[m])