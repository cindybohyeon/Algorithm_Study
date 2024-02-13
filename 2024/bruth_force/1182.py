from itertools import combinations
n, s = map(int, input().split())
graph = list(map(int, input().split()))
result = 0
# 하나씩 늘려가기
numLen = 1
while(numLen <= n):
    for x in combinations(graph, numLen):
        if sum(x) == s:
            result += 1
    numLen += 1

print(result)