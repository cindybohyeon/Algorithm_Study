# 지그재그로 숫자 채우기 
n,m = map(int, input().split())
# 0 채울 때, [0] for in range
graph =[ [ 0 for _ in range(m) ] for _ in range(n)]

count = 0
# 처음에 n 의 값을 증가시키기 
for i in range(m) :
    if(i % 2 == 0):
        for j in range(n):        
            graph[j][i] = count
            count += 1
    else:
        # for j in range(n-1,-1,-1):
        for j in range[::-1]:
            graph[j][i] = count
            count += 1


for i in range(n):
    for j in range(m):
        print(graph[i][j],end=" ")
    print()