r, c = map(int, input().split())
graph = []
changedList = []
for i in range(r):
    graph.append(list(map(str, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def in_range(x,y):
    if x>= 0 and x<r and y>=0 and y<c:
        return True
    return False

for i in range(r):
    for j in range(c):
        # 섬인지 확인
        # print("check")
        if (graph[i][j] == "X"):
            count = 0
            # 사라지는 섬인지 확인
            for x,y in zip(dx, dy):
                nx, ny = i + x, j + y
                # 모서리인 경우
                if (in_range(nx,ny) == False):
                     count += 1
                # 인접노드에서 바다가 3개 이상인 경우
                elif (in_range(nx,ny) and graph[nx][ny] == "."):
                        count += 1
                if (count >= 3):
                     changedList.append([i,j])
        # 안 사라지는 경우 넘어가기   


for i,j in changedList:
     graph[i][j] = '.'
# print(graph, "changed")

# 행 다듬기
startR = 0
endR = 0
for i in range(r):
     if 'X' in graph[i]:
        startR = i
        break
for i in range(r-1, -1, -1):
    if 'X' in graph[i]:
        endR = i
        break


# 열 다듬기
    # 열을 먼저 도는 이중 포문에서 섬이 있는 모든 열의 index를 구한다. 
col = []
for j in range(c):
    for i in range(startR, endR+1):
        if (graph[i][j] == 'X'):
            col.append(j)
            break

if len(col) == 0:
    print("X")
else:
    for i in range(startR, endR+1):
        for j in range(col[0], col[-1]+1):
            print(graph[i][j], end = '')
        print()
# print(graph, changedList, startR, endR)