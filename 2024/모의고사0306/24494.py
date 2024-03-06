import sys
input = sys.stdin.readline
graph = [list(map(str, input())) for _ in range(3)]
test = [list(map(str, input())) for _ in range(3)]
green, red = 0, 0
new_graph = []
new_test = []
for i in range(len(graph)):
    for j in range(3):
        if graph[i][j] == test[i][j]:
            # 같은 것은 green을 더해준다.
            # print(i, j, "D")
            green += 1
        else:
            # 같지 않은 경우 우선 일차원 배열에 넣는다.
            new_graph.append(graph[i][j])
            new_test.append(test[i][j])

# 여기서 2차원으로 돌려서, 위치는 달라도 값이 같은 것을 카운팅한다.
for i in range(len(new_graph)):
    for j in range(len(new_test)):
        if new_graph[i] == new_test[j]:
            # print(new_graph[i], new_test[j], i, j, "#")
            red += 1
            new_graph[i] = 0
            new_test[j] = ' '

print(green)
print(red)