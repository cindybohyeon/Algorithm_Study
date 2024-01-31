# 카드의 합이 21을 넘지 않는 한도내에서 카드의 합을 최대한 크게 만드는 게임이다
# 첫째 줄에 카드의 개수
import sys
from itertools import combinations
# input = sys.stdin.readline()

n, m = map(int, input().split())
graph = list(map(int, input().split()))
graph.sort()
result = 0
# 합이 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다
# N 개 중에 서로다른 3장을 구하는 경우의 수 = 조합 nC3
# 모든 경우의 합을 다 구한다.
resultList = []
for cards in combinations(graph, 3):
    tempSum = sum(cards)
    differ = m - tempSum
    if (differ >= 0):
        resultList.append([tempSum, differ])
    # if (differ < (m - result)):
    #     result = tempSum
    #     print(cards)
resultList.sort(key=lambda x:x[1])

print(resultList[0][0])
# 그 경우의 합을 구할 때 마다 차이값을 넣는다

