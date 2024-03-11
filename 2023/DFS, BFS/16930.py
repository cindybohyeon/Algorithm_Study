
from collections import deque

# 시작점과 도착점이 주어진다. 
# 최소 시간을 구하기 
# k는 1초에 이동할 수 있는 칸의 최대 개수 ..

n,m,k = map(int, input().split())

graph = [list(input().strip()) for _ in range(n)]
# strip은 불필요한 화이트 스페이스를 없애준다.
# 빈 칸은 . 벽은 #
x1,y1,x2,y2 = map(int, input().split())
vis=[[-1]*m for _ in range(n)]
print(graph)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def in_range(x,y):
    if x >=0 and y >=0 and x < n and y < m:
        return True
    else:
        return False
count = 0
def bfs(x1,y1):
    global count
    queue = deque()
    queue.append((x1,y1))
    vis[x1][y1]=0
    while queue:
        x1,y1 = queue.popleft()
        # count += 1
        if x1==x2-1 and y1==y2-1:
            print(vis[x1][y1])
            exit()
        for i in range(4):
            for num in range(1,k+1):
                nx = dx[i]*num + x1
                ny = dy[i]*num + y1
                if in_range(nx,ny) and graph[nx][ny] == '.':
                    if vis[nx][ny] == -1:
                        queue.append((nx,ny))
                        vis[nx][ny] = vis[x1][y1] + 1
                    elif vis[nx][ny] == vis[x1][y1] + 1:
                        continue
                    else:
                        break
bfs(x1-1,y1-1)
# print(count)


# 맨 끝이  아닌 원하는 곳으로 가려면 ?

