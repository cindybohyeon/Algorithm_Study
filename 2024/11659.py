n, m = map(int, input().split())
graph = list(map(int, input().split()))
indexList = []
for _ in range(m):
    indexList.append(list(map(int, input().split())))

dp = [0 for _ in range(n+1)]
for i in range(-1,n-1):#0~n-1
    dp[i+1] = dp[i] + graph[i+1]

# print(dp)
# print(indexList)  
for a, b in indexList:
    if a == 1:
        print(dp[b-1])
    else:

        print(dp[b-1] - dp[a-2])