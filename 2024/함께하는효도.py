import copy
import sys
from itertools import combinations, permutations
# input = sys.stdin.readline()
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [[0 for _ in range(n)] for _ in range(n)]
friends = []
sumR = 0
for _ in range(m):
    x1, y1 = map(int, input().split())
    x1, y1 = x1-1, y1-1
    friends.append([x1, y1])
for a,b in friends:
    visited[a][b] = 1

# 3초 안에 수확량의 총 합을 구해야한다.
# (1) 각 친구의 위치에서 구할 수 있는 모든 경우의 수를 구한다.
# (2) 각 친구의 최대 값을 구했다고 가정했을 때 겹치는 것이 있는지 확인해야한다. How? 좌표값을 가지고 있다고 가정하자.

def in_range(x, y):
    if x >= 0 and y >= 0 and x < n and y < n:
        return True
    return False

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# print(visited, "vis")

def allCount(x, y, count, visited, resultList, result):
    global graph
    global friendResult, friendResultGraph
    if count == 3:
        friendResult.append(result)
        friendResultGraph.append(resultList)
        
        
        # print(result, resultList)
        return result

    for a, b in zip(dx, dy):
        R = copy.deepcopy(result)
        V = copy.deepcopy(visited)
        C = copy.deepcopy(count)
        RL = copy.deepcopy(resultList)
        nx = x + a
        ny = y + b
        if in_range(nx, ny) and visited[nx][ny] == 0:
            # 지나갈 수 있는 것.
            R += graph[nx][ny]
            V[nx][ny] = 1
            RL.append([nx, ny])

            allCount(nx, ny, C + 1, V, RL, R)

T_friendResult = []
T_friendResultGraph = []

for a,b in friends:
    friendResult = []
    friendResultGraph = []
    allCount(a, b, 0, visited, [], graph[a][b])
    # print(friendResultGraph, "##", len(friendResultGraph))
    T_friendResult.append(max(friendResult))
    tempIndex = friendResult.index(max(friendResult))
    T_friendResultGraph.append(friendResultGraph)


# 친구가 1명인 경우
if m == 1:
    print(T_friendResult[0])

# 친구가 2명인 경우
if m == 2:
    twoR = []
    fristSum = 0
    for a,b in friends:
        fristSum += graph[a][b]
        
    for F1 in T_friendResultGraph[0]:
        for F2 in T_friendResultGraph[1]:
            # 모든 경우의 수.
            tempList = F1 + F2
            tempList.sort()
            # 겹치는 것을 뺀다.
            realList = []
            # print(tempList, "TEmp")
            for i in range(len(tempList)):
                if i < len(tempList) - 1 and tempList[i] == tempList[i + 1]:
                    continue
                realList.append(tempList[i])
            # print(realList, "Real")
            realResult = 0
            for i, j in realList:
                realResult += graph[i][j]
                
            # print(realResult, "RR")
            twoR.append(realResult)
    print(max(twoR) + fristSum)
# for i in range(len(friends)):
#     combi = list(combinations(T_friendResultGraph[i], 1))
#     print(combi, "EE")

    
if m == 3:
    thirdR = []
    fristSum = 0
    for a,b in friends:
        fristSum += graph[a][b]
        
    for F1 in T_friendResultGraph[0]:
        for F2 in T_friendResultGraph[1]:
            for F3 in T_friendResultGraph[2]:
                # 모든 경우의 수.
                tempList = F1 + F2 + F3
                tempList.sort()
            # 겹치는 것을 뺀다.
                realList = []
            # print(tempList, "TEmp")
                for i in range(len(tempList)):
                    if i < len(tempList) - 1 and tempList[i] == tempList[i + 1]:
                        continue
                    realList.append(tempList[i])
            # print(realList, "Real")
                realResult = 0
                for i, j in realList:
                    realResult += graph[i][j]
                
            # print(realResult, "RR")
                thirdR.append(realResult)
    print(max(thirdR) + fristSum)
