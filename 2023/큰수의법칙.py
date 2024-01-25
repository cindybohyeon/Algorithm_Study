n, m, k = map(int, input().split())
graph = list(map(int, input().split()))
result = 0
graph.sort()
count = 0
# for i in range(m):
#     if (count < k):
#         result += graph[-1]
#         count += 1
#     else:
#         result += graph[-2]
#         count = 0

arrSum = graph[-1] * k + graph[-2]
arrlen = m // (k+1)
arrNo = m & (k+1)

result = arrSum * arrlen + arrNo

print(result)