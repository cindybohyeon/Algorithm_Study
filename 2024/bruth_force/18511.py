# n보다 작거나 같은 자연수 중에서, 집합 k의 원소로만 구성된 가장 큰 수
# K의 모든 원소는 1부터 9까지의 자연수로만 구성된다
# n = 657, 집한 k의 원소 1, 5, 7dlaus
from itertools import product
# 중복순열..

n, countK = map(int, input().split())
graph = list(map(int, input().split()))
result = 0
graph.sort()
# 하나 또는 n의 자릿수만큼 graph의 원소를 구한다.
maxLen = len(str(n))

num = list(product(graph, repeat = maxLen))

# print(num)
# print(''.join(list(map(str, num[0]))))
# # 뭘까..?
while 1:
    # 최대길이로 먼저 중복순열을 돌린다
    num = list(product(graph, repeat = maxLen))
    for a in num:
        print(a, "a")
        print(list(map(str, a)), "list")
        tempA = int(''.join(list(map(str, a))))
        if (tempA <= n):
            result = max(result, tempA)
    if result == 0:
        maxLen -= 1
    else:
        print(result)
        break
