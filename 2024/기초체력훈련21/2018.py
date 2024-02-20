n = int(input())
# 연속된 자연수로.
result = 0
count = n // 2 + n % 2

# temp = 0
# for i in range(count, 1, -1):
#     temp += i
#     if temp == n:
#         result += 1

dp = [0 for _ in range(n + 1)]
for i in range(1, n):
    dp[i] = dp[i - 1] + i

# print(dp)

for i in range(count, 0, -1):
    for j in range(count):
        temp = dp[i] - dp[j] + j
        if temp == n:
            result += 1


start = 0
end = count

while(start <= end):
    temp = dp[end] - dp[start] + start
    if temp == n:
        result += 1
        print(start, end, "@@")
        start += 1
        end -= 1

    elif temp > n:
        end -= 1
    else:
        start += 1

print(result)
