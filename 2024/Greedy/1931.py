n = int(input())
graph = []
answer = 0
for _ in range(n):
    graph.append(list(map(int, input().split())))

    # 하고 싶은 회의들이 있고, 최대 회의할 수 있게

graph.sort(key= lambda x: (x[1], x[0]))
print(graph, "graph")
preEnd = 0
for s, e in graph:
    if preEnd <= s:
        # print(s, e, "s, e")
        answer += 1
        preEnd = e

print(answer)