import heapq
import sys
input = sys.stdin.readline
n, e = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(e):
    x, y, cost = map(int, input().split())
    graph[x].append((y, cost))
    graph[y].append((x, cost))

x, y = map(int, input().split())

# s -> v1, v2 -> e
max_size = sys.maxsize
def di(start):
    # 시작위치에서 각 위치별의 최단 거리 배열
    distance = [max_size] * (n + 1)
    # 힙큐 생성
    q = []
    heapq.heappush(q, (0, start))
    # 현재 위치의 거리는 0이다.
    # 거리 값과 현재 위치의 값/
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        

        if distance[now] < dist:
            # dist 값보다 현재 값이 작으면 변경 하지 않ㄴ,ㅡㄴ다.
            continue

        for i in graph[now]:
            # now 까지의 거리들 중에서 
            cost = dist + i[1]


            if distance[i[0]] > cost:
                # i[0]는 이제 끝 점.
                distance[i[0]] = cost
                # 
                heapq.heappush(q, (cost, i[0]))

    # 반환값은 최단 거리 배열
    return distance


start0 = di(1)
startV1 = di(x)
startV2 = di(y)

firstR = start0[x] + startV1[y] + startV2[n]
secondR = start0[y] + startV2[x] + startV1[n]
ans = min(firstR, secondR)
if ans > max_size:
    print(-1)
else:
    print(ans)



# s -> v2, v1 -> e


