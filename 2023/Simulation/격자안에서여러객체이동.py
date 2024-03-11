#  숫자가 가장 큰 인접한 곳으로 동시에 이동!!
# 1. 입력 받기
n,m,t = map(int, input().split())
graph = [[ 0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    given_row = list(map(int, input().split()))
    for j, elnm in enumerate(given_row, start=1):
        graph[i][j] = elnm

count = [[ 0 for _ in range(n+1)] for _ in range(n+1)]
next_count = [[ 0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    count[x][y] = 1

# 2. 결과값 : 남아있는 구슬의 개수
remain_num = 0

# 3. 함수 사용
def in_range(x,y):
    return x>0 and y>0 and x<=n and y<=n

def can_move(x,y,cur_num):
    return in_range(x,y) and cur_num < graph[x][y]

def move(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    max_num, max_pos = 0, (x,y)
# 현재 값과 비교가 아니고, 상하좌우 중 제일큰수로 이동하는 것.
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if can_move(nx,ny,max_num):
            max_num = graph[nx][ny]
            max_pos = (nx,ny)
    return max_pos

def nextcoin(x,y):
    next_x, next_y = move(x,y)
    next_count[next_x][next_y] += 1

def move_all():
    # nextcount 초기화
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            next_count[i][j] = 0

    for i in range(1,n+1):
        for j in range(1,n+1):
            if count[i][j] == 1:
                nextcoin(i,j)

    for i in range(1,n+1):
        for j in range(1,n+1):
            count[i][j] = next_count[i][j]

def remove_duplicate_marbles():
    for i in range(1,n+1):
        for j in range(1,n+1):
            if count[i][j] >= 2:
                count[i][j] = 0
    
def simulate():
    move_all()
    remove_duplicate_marbles()

for _ in range(t):
    simulate()


for i in range(1,n+1):
    for j in range(1,n+1):
        if(count[i][j] == 1):
            remain_num += 1

print(remain_num)
