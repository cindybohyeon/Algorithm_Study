N, s = map(int, input().split())
graph = list(map(int, input().split()))
result = 0

def dfs(n, count):
    global result

    if n >= N:
        return
    
    count += graph[n]

    if count == s:
        # print(count, n)
        result += 1

    # temp = count + graph[n + 1]
    # 지금의 원소를 더하는 경우
    dfs(n+1, count)
    # 지금의 원소를 더하지 않는 경우
    dfs(n+1, count - graph[n])
dfs(0, 0)
print(result)
