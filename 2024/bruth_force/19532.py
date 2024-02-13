from itertools import combinations
import sys
input = sys.stdin.readline
a, b, c, d, e, f = map(int, input().split())
realx, realy = 0, 0
for x in range(-999, 1000):
    for y in range(-999, 1000):
        # tempC = a * x + b * y
        # tempF = d * x + e * y
        # if (tempC == c and tempF == f):
            # print(x, y)
        if (a * x + b * y == c and d * x + e * y == f):
            print(x,y)

# graph = list(i for i in range(-999, 1000))
# for x,y in combinations(graph, 2)