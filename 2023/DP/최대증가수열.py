import sys

INT_MIN = -sys.maxsize

n = int(input())
arr = list(map(int, input().split()))
array = [0 for _ in range(n+1)]
array[1:] = arr[:]

dp = [INT_MIN for _ in range(n+1)]

dp[0] = 0
array[0] = 0
# N개의 숫자가 주어졌을 때 가장 긴 증가 부분 수열의 길이를 구하는 것..


# i번째 보다 앞에 있는 원소들 중
# array[i] 보다는 작은 값들만 비교하기.
for i in range(1,n+1):
    for j in range(0,i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j]+1)

answer = 0
for i in range(1,n+1):
    answer = max(answer, dp[i])

print(answer)

# import sys

# INT_MIN = -1 * sys.maxsize

# n = int(input())

# # dp[i] : 마지막으로 고른 원소의 위치가 i인
# # 부분 수열 중 최장 부분 수열의 길이
# # 최대를 구하는 문제이므로, 초기에는 전부 INT_MIN을 넣어줍니다.
# dp = [INT_MIN for _ in range(n + 1)]
# a = [0 for _ in range(n + 1)]

# given_seq = list(map(int, input().split()))
# a[1:] = given_seq[:]

# # 0번째 index와 비교했을 때 항상 갱신될 수 있는 값을 넣어줍니다.
# dp[0], a[0] = 0, 0

# for i in range(1, n + 1):
#     # i번째 보다 앞에 있는 원소들 중 
#     # a[i]보다는 값이 작은 곳에 새로운 원소인 a[i]를 추가했을 때의 
#     # 부분 수열 중 최대 부분 수열의 길이를 계산합니다.
#     for j in range(0, i):
#         if a[j] < a[i]:
#             dp[i] = max(dp[i], dp[j] + 1)
            
# # 마지막 원소의 위치가 i일 때의 부분 수열들 중
# # 가장 길이가 긴 부분 수열을 고릅니다.
# answer = 0
# for i in  range(n + 1):
#     answer = max(answer, dp[i])
    
# print(answer)