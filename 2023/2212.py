n = int(input())
k = int(input())
graph = list(map(int, input().split()))
graph.sort()

# 각 거리의 차를 가진 arr를 만든다.
lenGraph = []
for i in range(n-1):
    lenGraph.append(graph[i+1] - graph[i])

lenGraph.sort()
# 거리의 합이 큰 거를 뺀다. 
# 다시말해서 거리의 합이 작은 것부터 n-k를 고른다.
result = 0
for i in range(n-k):
    result += lenGraph[i]
print(result)


# n개의 센서를 설치하였다
# 집중국은 센서의 수신가능 영역 조절
# 하나의 집중국과는 통신이 가ㅡ능.
# 집중국의 유지비 문제로 인해 집중각의 수신 가ㅡㅇ 영어의 길이의 합

# 와 거리차가 큰게 있다고 구간을 나누는 거지?
# n-k 란 센서 - 



