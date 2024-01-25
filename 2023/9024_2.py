t = int(input())

answer = []

def makeResult(n, k, graph):
    count = 0
    difference = 200000002 # 이거 때문에 틀림
    start, end = 0, n-1
    while(start < end):
        temp = graph[start] + graph[end]
        if (abs(temp - k) < difference):
            # 더 가까운 조합을 찾은 경우, 개수 초기화한다.
            count = 1
            difference = abs(temp-k)
        elif (abs(temp - k) == difference):
            # 같은 조합인 경우 더하기
            count += 1
        # 투 포인터 진행
        if (temp > k):
            end -= 1
        elif (temp < k):
            start += 1
        else: # k랑 같은 경우.
            # 이게 맞는지 모르겠음
            start += 1
            # count += 1
    return count

for _ in range(t):
    n, k = map(int, input().split())
    graph = list(map(int, input().split()))
    graph.sort()
    answer.append(makeResult(n, k, graph))

for a in answer:
    print(a)