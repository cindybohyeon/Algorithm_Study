import heapq
import sys
from turtle import distance

input = sys.stdin.readline
INF = int(1e9)

n,m, c = map(int, input().split())
# 도시의 개수 통로의 개수 메시지보내는도시숫자
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    x,y,z = map(int, input().split())
    # x번 노드에서 y번 노드로 가는 비용이 z라는 의미
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    # (거리, 노드) 로 넣는다.
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(c)
# 도달할 수 있는 노드의 개수
count = 0
# 도달할 수 있는 노드 중에서 가장 멀리 있는 최단거리
max_distance = 0
for d in distance:
    # 도달할 수 잇는 노드읜 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count-1, max_distance)
