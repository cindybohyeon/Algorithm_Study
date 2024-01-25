from collections import deque
n, k, r = map(int, input().split())

road = [[[] for _ in range(n)] for _ in range(n)]
cow_visit = [[False] * n for _ in range(n)]
count = 0

def in_range(x, y):
    if x >= 0 and y >= 0 and x < n and y < n:
        return True
    return False
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(r1, c1):
    dq = deque()
    dq.append((r1, c1))
    cow_visit[r1][c1] = True
    while dq:
        x, y = dq.popleft()
        for a, b in zip(dx,dy):
            nx = x + a
            ny = y + b
            if (in_range(nx, ny) and cow_visit[nx][ny] == False):
               if (nx, ny) not in road[x][y]:
                  dq.append((nx, ny))
                  cow_visit[nx][ny] = True
               # 지나지 않았고 범위내에 있고 길은 없는
               


# 길 위치 담기
for _ in range(r):
    r1, c1, r2, c2 = map(int, input().split())
    road[r1-1][c1-1].append((r2-1, c2-1))
    road[r2-1][c2-1].append((r1-1, c1-1))

# 소의 위치 담기
cow_list = list()
for _ in range(k):
    a, b = map(int, input().split())
    cow_list.append((a-1, b-1))

# 소를 한마리씩 돌려가면서 방문 여부 탐색?
for i, cow in enumerate(cow_list):
    cow_visit = [[False] * n for _ in range(n)]
    # 소가 정해진 길없이 가는 경로를 탐색
    bfs(cow[0], cow[1])
    for r2, c2 in cow_list[i + 1 :]:
        # 다른 소들의 방문을 완료하지 못 한 경우 +1
        if cow_visit[r2][c2] == False:
            count += 1

print(count)