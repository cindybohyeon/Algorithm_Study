n = int(input())
m = int(input())
graph = list(map(int, input().split()))
result = 0
graph.sort()

start = 0
end = n - 1

while(start < end):
    temp = graph[start] + graph[end]
    if temp == m:
        # print( graph[start], graph[end])
        result += 1
        start += 1
        end -= 1

    elif temp > m:
        end -= 1
    else:
        start += 1

print(result)