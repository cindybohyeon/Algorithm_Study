import sys
def in_range(x, y):
    if x>=0 and y>=0 and x<n and y<n:
        return True
    return False
def findEmpty(student):
    global room
    available = []
    # 일단 비어있는거 찾기
    for i in range(n):
        for j in range(n):
            if room[i][j] == 0:
                available.append([i, j])
    if available == []:
        return 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 비어있는 좌표의 인접노드 중에 친한 친구 개수 세기
    for a in available:
        count = 0
        emptycount = 0
        for x, y in zip(dx, dy):
            nx = a[0] + x
            ny = a[1] + y
            if (in_range(nx, ny)):
                if (room[nx][ny] == 0):
                    emptycount += 1
                else:
                    # 학생의 인접한 학생들있는지 확인
                    for i in range(4):
                        if (room[nx][ny] == student[i+1]):
                            count += 1
        a.append(count)
        a.append(emptycount)
    return available
    

def satisify(graph):
    global room
    result = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(n):
        for j in range(n):
            count = 0
            num = room[i][j]
            for s in graph:
                if s[0] == num:
                    for x,y in zip(dx, dy):
                        nx = i + x
                        ny = j + y
                        if in_range(nx, ny):
                            if room[nx][ny] in s[1:]:
                                print(num, room[nx][ny],"@")
                                count += 1
            if (count > 0):
                result += 10 ** (count-1)
    return result



n = int(input())
graph = []
room = [[0 for _ in range(n)] for _ in range(n)]
# ans = [[0]*n for _ in range(n)]
for i in range(n*n):
    graph.append(list(map(int, sys.stdin.readline().split())))

for student in graph:
    number = student[0]
    # 비어있는 칸 중에서 좋아하는 학생이 인접한 칸
    # 1, 비어있는 칸 확인, 그 칸의 인접한 칸에 친구개수세기
    arr = findEmpty(student)
    arr.sort(key=lambda x:(-x[2], -x[3], x[0], x[1]))
    # print(arr)
    # 친구의 max값이 있는지 그리고 그것이 
    # 인접한 칸 중에서 비어있는 칸이 가장 많은 칸...
    room[arr[0][0]][arr[0][1]] = number

print(room)

ans = satisify(graph)
print(ans)



