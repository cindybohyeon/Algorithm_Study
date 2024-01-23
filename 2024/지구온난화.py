import copy
import sys

r, c = map(int, sys.stdin.readline().split())

graph = [list(sys.stdin.readline().strip()) for _ in range(r)]
remove = []
aftergraph = []
land_count = 0
startR = 0
endR = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def in_range(x,y):
    if x < r and x >= 0 and y < c and y >= 0:
        return True
    return False

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'X':
            count = 0
            # 답에서 발취함
            land_count += 1
            for x, y in zip(dx, dy):
                nx = i + x
                ny = j + y
                if in_range(nx, ny) == False:
                # 모서리인 경우도 바다 count 
                    count += 1
                elif graph[nx][ny] == '.':
                # 바다인 경우 count
                    count += 1
            if count >= 3:
                remove.append([i,j])
                land_count -= 1

if land_count == 0:
    print("X")
else:
    aftergraph = graph
    for i,j in remove:
        aftergraph[i][j] = '.'
    
    for i in range(r):
        if 'X' in aftergraph[i]:
            startR = i
            break
    for i in range(r-1, 0, -1):
        # range(start, stop, step)
        if 'X' in aftergraph[i]:
            endR = i
            break
    idx = []
    for j in range(c):
        for i in range(startR, endR + 1):
            if 'X' == aftergraph[i][j]:
                idx.append(j)
                # 열에 하나라도 X가 있으면 되니까 그만 for문을 돌고 다음 열로 넘어감
                break
            
    for i in aftergraph[startR:endR+1]:
        print(''.join(i[idx[0]:idx[-1]+1]))






# answer = []
# # 행 자름
# for i in aftergraph:
#     if 'X' in i:
#         answer.append(i)

# final = []

# print(answer)

# for i in range(r):
#     dot = 0
#     for j in range(c):
#         if graph[i][j] == '.':
#             dot += 1
#     if dot == r:


