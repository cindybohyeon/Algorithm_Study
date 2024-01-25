import sys
n, m = map(int, sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(int(sys.stdin.readline()))
graph.sort()

result = 0
# 시간으로 잡음, 가능한 모든 시간을 나열한다.
start = 1
end = graph[-1] * m

# if (n == m):
#     result = graph[-1]
# elif (n < m):
#     result = graph[]
# else:
while(start <= end):
    mid = (start + end) // 2
    # 해당 시간 동안 심사한 사람의 수
    people = 0
    for i in graph:
        people += mid // i
        if people >= m:
            break
    
    if people >= m:
        result = mid
        end = mid - 1
    elif people < m:
        start = mid + 1


print(result)