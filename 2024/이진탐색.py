n, x = map(int, input().split())
graph = list(map(int, input().split()))

countA = -1
countB = -1
start = 0
end = len(graph) - 1

# 처음 등장하는 인덱스와 마지막으로 등장하는 인덱스

while(start <= end):
    mid = (start + end) // 2
    # print(mid)
    if ((mid == 0 or x > graph[mid - 1]) and graph[mid] == x): # 찾은 경우
        countA = mid
        break
    elif (graph[mid] >= x):
        end = mid - 1
    else:
        #  (graph[mid] <= x):
        start = mid + 1

# print(countArr)
start = 0
end = len(graph) - 1
while(start <= end):
    mid = (start + end) // 2
    # print(mid)
    if ((mid == len(graph) - 1 or x < graph[mid + 1]) and graph[mid] == x): # 찾은 경우
        countB = mid
        break
    elif (graph[mid] <= x):
        start = mid + 1
    else:
        #  (graph[mid] <= x):
        end = mid - 1

# print(countArr)
result = countB - countA + 1

if (countA == -1):
    print(-1)
elif (result == 0):
    print(-1)
else:
    print(result)