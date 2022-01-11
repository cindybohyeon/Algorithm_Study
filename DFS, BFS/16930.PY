#  아 모르겟다
from collections import deque

n,m,k = map(int, input().split())

graph = [list(input().strip()) for _ in range(n)]
# strip은 불필요한 화이트 스페이스를 없애준다.

x1,y1,x2,y2 = map(int, input().split())


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(graph, x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        
        x,y = queue.popleft()

