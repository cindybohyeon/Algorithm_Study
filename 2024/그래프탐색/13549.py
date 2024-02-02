from collections import deque
n, m = map(int, input().split())
# 수빈이가 있는 위치, 동생이 있는 위치
result = 0

visited = [-1 for _ in range(100001)]
print(visited)
queue = deque()
queue.append(n)
visited[n] = 0

while queue:
    x = queue.popleft()
    if x == m:
        print(visited[x])
        break

    # 방문을 어떤 걸 해야하는거지? 
    # 너비 탐색을 하려면 인접노드로 가야하는데
    if 0 <= x-1 <= 100000 and visited[x-1] == -1:
        visited[x-1] = visited[x] + 1
        queue.append(x-1)
    if 0 <= x*2 <= 100000 and visited[2*x] == -1:
        queue.appendleft(x*2)
        visited[2*x] = visited[x]
    if 0 <= x+1 <= 100000 and visited[x+1] == -1:
        visited[x+1] = visited[x] + 1
        queue.append(x+1)






# while True:
#     if (n == m):
#         break
#     else:
#         if (n*2 <= m):
#             n = n*2
#             continue
#         if (n < m):
#             n += 1
#         else:
#             n -= 1
#         result += 1
                
# print(result)