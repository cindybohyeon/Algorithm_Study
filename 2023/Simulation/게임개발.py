# 게임캐릭터가 맵 안에서 움직이는 시스템 개발.
# 캐릭터가 있는 장소는 1*1크기의 정사각형으로 이뤄진 NM직사각형..
# (A,B)로 나타낼 때 A는 북쪽으로부터 떨아진 칸의 개수 B는 서쪽으로 떨어진 칸의 개수

# 현재 위치에서 현재 방향을 기준으로 왼쪽 방향 부터 차례대로 갈 곳을 정한다. 
# 

n,m = map(int, input().split())
a,b,d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 1
turn_time = 0
# 방향 d에 따라서 왼쪽틀어서 한 칸 이동하는 거
dx_position = [-1,0,1,0]
dy_position = [0,1,0,-1]

def in_range(x,y):
    if x>=0 and y>=0 and x<n and y<m:
        if graph[x][y] == 0:
            graph[x][y] = 1
            return True
        return False
    return False


while True:
    nx = a + dx_position[d]
    ny = b + dy_position[d]
    # 왼쪽으로 회전
    if d == 3:
        d = 0
    else:
        d += 1
    # 회전한 이후 그 위치가 방문안하고 육지인 경우
    if in_range(nx,ny):
        result += 1
        a = nx
        b = ny
        turn_time = 0
        print(a,b)
        continue
    else:
        # 회전한 이후 방문했거나 육지 아닌 경우
        turn_time += 1
    if turn_time == 4:
        # 네 방향 모두 갈 수 없는 경우
        
        # 뒤로 이동
        nx = a - dx_position[d]
        ny = b - dy_position[d]
        if(graph[nx][ny] == 1):
            break
        else:
            turn_time = 0

print(result)
    
    


