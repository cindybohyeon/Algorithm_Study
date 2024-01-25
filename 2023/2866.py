# 8:50 시작
r, c = map(int, input().split())
graph = list(input() for _ in range(r))
for i in range(r):
    graph[i] = list(graph[i])

def makeList(tempList):
    numLen = len(tempList[0])
    nums = []
    for i in range(numLen):
        nums.append(''.join(tempList[]))
        

# 이분탐색

for i in range(r):
    makeList(graph[i+1:])


print(graph)

