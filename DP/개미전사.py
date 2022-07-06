# 메뚜기 식량창고는 일직선으로 이어져있다.
# 정해진 식량을 저장. 선택적으로 약탈.
# 일직선상에 존재하는 식량창고 중에서 서로 인접한 식량창고가 공격하면 안된다. 최소 한 칸 이상 떨어진 것을 약탈해야한다. 

n = int(input())
container = list(map(int, input().split()))

dp = [0] * 101

dp[1] = container[0]

for i in range(1,n):
    dp[i] = max(dp[i-1], (dp[i-2]+container[i]))

print(dp[n-1])