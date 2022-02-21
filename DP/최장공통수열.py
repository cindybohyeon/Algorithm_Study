arr1 = list(input())
arr2 = list(input())

arr1_len, arr2_len = len(arr1), len(arr2)

# string 의 index 가 0부터 시작해서 1부터 시작하기 위해 앞에 #을 붙여준다


dp = [[0 for _ in range(arr2_len)] for _ in range(arr1_len)]


def initialize():
    if(arr1[0] == arr2[0]):
        dp[0][0] = 1
    for i in range(1,arr1_len):
        if(arr1[i] == arr2[0]):
            dp[i][0] = 1
        else:
            dp[i][0] = dp[i-1][0]

    for j in range(1,arr2_len):
        if(arr2[j] == arr1[0]):
            dp[0][j] = 1
        else:
            dp[0][j] = dp[0][j-1]

initialize()

for i in range(1,arr1_len):
    for j in range(1,arr2_len):
        if(arr1[i] == arr2[j]):
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]) 

print(dp[arr1_len-1][arr2_len-1])