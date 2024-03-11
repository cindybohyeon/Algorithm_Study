문제이해를 못함. 다시 풀어야한다.

# n, m = map(int, input().split())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().split())))
# wanted = []
# chicken = []
# result = 0

# for j in range(m):
#     temp = 0
#     for i in range(n):
#         temp = max(temp, graph[i][j])
#     chicken.append(temp)
# print(chicken, "chi")



# for i in range(n):
#     temp = max(graph[i])
#     for j in range(m):
#         if temp == graph[i][j]:
#             wanted.append([temp, j])
# wanted.sort(key=lambda x:-x[0])

# for i in range(3):
    
#     result += wanted[i][0]

# print(result)