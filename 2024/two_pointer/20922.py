n, k = map(int, input().split())
graph = list(map(int, input().split()))

# 같은 원소과 k개 이하로 들어있는 최장 연속 부분수열의 길이.
end = 0
count = 0
result = 0
maxsu = 0

for start in range(n):
    count = 0
    end = start
    temp = []
    while (end < n and count <= k):
        # print("$")
        if graph[start] == graph[end]:
            print(graph[start], graph[end], "#")
            count += 1
            if count > k:
                break
        temp.append(graph[end])
        end += 1
    if maxsu < count:
        maxsu = count
        result = max(len(temp), result)

print(result)