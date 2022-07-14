# NM 얼음틀이 있다.
n,m = map(int, input().split())
# 인접행렬
graph = [list(map(int, input())) for _ in range(n)]

def in_range(x,y):
    # 왜 x가 n이고 y가 m이야?
    if x>=0 and y>=0 and x<n and y<m:
        return True
    else:
        return False

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# dfs : 길이 즉 재귀함수를 이용한다. 
def dfs(x,y):
    if in_range(x,y) and graph[x][y] == 0:
        graph[x][y] = 1
        for a,b in zip(dx,dy):
            nx = x + a
            ny = y + b
            dfs(ny,nx)
        return True
    return False
# 모든 위치 즉 노드에 음료수 채우기
# 이 부분 다시 생각하기.
ans = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            ans += 1
print(ans)
 
    



