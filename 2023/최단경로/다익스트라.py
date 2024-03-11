import heapq
from sre_constants import RANGE_UNI_IGNORE
import sys
input = sys.stdin.readline
INF = int(1e9)
# 노드의 개수, 간선의 개수
n,m = map(int, input().split())
# 시작 노드 번호
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]
# 최단거리 테이블 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

def dijkstra(start):
    # 우선순위 큐 특징 ㅣ 우선순위가 가장 높은 데이터를 먼저 삭제. 즉 pop할 때 우선순위가 높은게 빠진다. 
    # 튜플 (0,1) 우선순위큐에 넣으면 튜플의 첫번째 원소 기준으로 정렬된다. 여기서는 그게 거리순.
    q = []
    # 시작 노드로 가기위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            # 처리가 안됬으면 초기값이 무한이라 무조건 dist보다 크니까.
            continue
        # 현재 노드와 연결된 다른 인접한 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF:
        print("-1")
    else:
        print(distance[i])

