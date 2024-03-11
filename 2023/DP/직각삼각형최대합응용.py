import sys

INT_MIN = -sys.maxsize

n = int(input())
# 이중배열 어떻게 받지 

arr =[  list(map(int, input().split())) for _ in range(n)
        ]


dp = [
        [0 for _ in range(n)]
        for _ in range(n)
]

def initialize():
        dp[0][0] = arr[0][0]
        for i in range(1,n):
                dp[i][0] = dp[i-1][0] + arr[i][0]
        for i in range(1,n):
                dp[0][i] = dp[0][i-1] + arr[0][i]

initialize()

for i in range(1,n):
        for j in range(1,n):
                dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + arr[i][j]

print(dp[n-1][n-1])


# !dp의 중요 세가지!
# 1. 동적테이블 정의하기
# 2. 초기값찾기
# 3. 점화식찾기