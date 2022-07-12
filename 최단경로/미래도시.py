# 공중 미래도시는 1번 n번까지 있다. 
# 특정 회사에 도착하기 위한 방법은 연결도로, 양방향 이동가능 ㅂ만큼으 ㅣ시간이동 A는 소개팅에서도 참석한다.
# 소개팅 ㅅㅇ태는 

INF = int(1e9)
# 회사의 개수 n 경로의 개수 m
n,m = map(int, input().split())
graph = []

# 모든 값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 경우는 0
for i in range(1,n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0
# 경로가 있는 경우는 1 값
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
# x와 k
x,k = map(int, input().split())

for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]
# 도달할 수 없는 경우 -1 출력
if distance >= INF:
    print("-1")
else:
    print(distance)

