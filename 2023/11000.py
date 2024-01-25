import heapq, sys
n = int(sys.stdin.readline())
result = 0
graph = []
que = []
for _ in range(n):
    s, t = map(int, sys.stdin.readline().split())
    graph.append([s,t])

# 처음 시작값으로 sorting하기
graph.sort(key=lambda a: (a[0]))

heapq.heappush(que, graph[0][1])

for i in range(1, n):
    if (que[0] > graph[i][0]):
        heapq.heappush(que, graph[i][1])
    else:
        # 지금 회의실 시간을 빼고 다음 수업의 끝나는 시간으로 바꾼다.
        heapq.heappop(que)
        heapq.heappush(que, graph[i][1])
# print(que)
print(len(que))

# index = 0
# while(graph.count != 0):
#     answerArr[index].append(graph[index])
#     for i in range(index+1, n):
#         if (graph[index][1] <= graph[i][0]):
#             first = graph[index]
#             second = graph[i]
#             answerArr[index].append(second)
#             print(graph, "pop")
#             graph.remove(first)
#             print(graph, "pop")
#             graph.remove(second)
#             break
#     index += 1
# print(answerArr)




    

