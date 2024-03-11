from collections import deque

n,m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
ans = 0

def in_range(x,y):
    if x>=0 and y>=0 and x<n and y<m:
        if graph[x][y] == 1:
            graph[x][y] = 0
            return True
        return False
    return False

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    global ans
    queue = deque()
    # 최단거리를 구할 때 왜 bfs를 쓰는거지?
    queue.append((x,y))
    while queue:
        a,b = queue.pop()
        print(a,b)
        ans += 1
        if(a == n-1 and b == m-1):
            break
        for i,j in zip(dx,dy):
            nx = a + i
            ny = b + j
            if in_range(nx,ny):
                graph[nx][ny] = graph[a][b] + 1
                queue.append((nx,ny))
                
bfs(0,0)
print(ans)
print(graph[n-1][m-1])



