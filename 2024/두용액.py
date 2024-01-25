import sys
n = int(input())
graph = list(map(int, sys.stdin.readline().split()))
graph.sort()

start = 0
end = len(graph) - 1
ansS = 0
ansE = 0
ans = 2000000000
while(start < end):
    temp = graph[start] + graph[end]
    # mid = (start + end) // 2

    # 더 0에 가까운게 있는 경우
    if (abs(temp) < abs(ans)):
        ans = temp
        ansS = start
        ansE = end
        if temp == 0:
            break
    
    if temp > 0:
        end -= 1
    elif temp < 0:
        start += 1

    # if (temp > 0 and abs(ans) > abs(temp)):
    #     ansS = start
    #     ansE = end
    #     end -= 1
    #     ans = temp
    # elif (temp < 0 and abs(ans) > abs(temp)):
    #     ansS = start
    #     ansE = end
    #     start += 1
    #     ans = temp
    # else:
    #     ans = temp
    #     break

print(graph[ansS],graph[ansE])