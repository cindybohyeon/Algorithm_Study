import sys
input = sys.stdin.readline
from itertools import combinations
n, m = map(int, input().split())
graph = list(map(int, input().split()))

all = []
result = 1000000000

for a in range(1, n+1):
    if a in graph: continue
    for b in range(1, n+1):
        if b in graph: continue
        for c in range(1, n+2):
            if c in graph: continue
            result = min(abs(n - a*b*c), result)

# # 같은거 2개 + 다른거1개
# for a,b in combinations(all, 2):
#     result = min(abs(n - a*b*a), result)
#     result = min(abs(n - a*b*b), result)
# # 같은거 3개
# for a in all:
#     result = result = min(abs(n - a*a*a), result)

# # 중복으로 고를 수 있는거를 어떻게 해야하는가
    
print(result)