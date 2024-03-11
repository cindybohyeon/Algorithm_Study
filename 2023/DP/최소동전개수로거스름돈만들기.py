import sys
INT_MIN = -sys.maxsize
n,m = map(int, input().split())
arr = list(map(int, input().split()))
coin = [0 for _ in range(n+1)]
# 새로 배우는 코드 .
coin[1:] = arr[:]

# 동전의 합 i 일 때 가능한 최소 동전 회수.
dp = [10001 for _ in range(m+1)]
dp[0] = 0


def initialize():
    for i in range(m+1):
        dp[i] = INT_MIN
    dp[0] = 0

# initialize()

for i in range(1,m+1):
    for j in range(1,n+1):
        if i >= coin[j]:
            dp[i] =min(dp[i], dp[i - coin[j]] + 1)

ans = dp[m]

if ans == 10001:
    ans = -1

print(ans)


