import sys
n, c = map(int, input().split())
graph = []
for i in range(n):
    a = int(sys.stdin.readline())
    graph.append(a)

graph.sort()

result = 0
start = 1 #공유기 거리 최소?
end = graph[-1] - graph[0] #공유기 거리 최대

while(start <= end):
    mid = (start + end) // 2 #현재 공유기 거리.?
    current = graph[0]
    count = 1

    # 공유기 몇 대 설치할 수 있는지 체크
    for i in range(1, len(graph)):
        if graph[i] >= current + mid:
            count += 1
            current = graph[i]
    #공유기 설치 수가 목표보다 많이 세울 수 있으면 거리를 늘린다? 
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)


# 가장 인접한 두 공유기 사이의 최대 거리

