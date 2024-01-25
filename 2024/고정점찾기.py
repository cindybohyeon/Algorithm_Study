n = input()
graph = list(map(int, input().split()))

result = -1
start = 0
end = len(graph) - 1

while(start <= end):
    mid = (start + end) // 2
    if (mid == graph[mid]):
        result = mid
        break
    elif (mid > graph[mid]):
        start = mid + 1
    else:
        end = mid - 1


print(result)