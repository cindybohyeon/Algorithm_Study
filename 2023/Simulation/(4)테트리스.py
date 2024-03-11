# 떨어지는 1자 블록 
# 4 3 1
# 0 0 0 0
# 0 0 0 1
# 1 0 0 1
# 1 1 1 1

# 0 0 0 0
# 1 1 1 1
# 1 0 0 1
# 1 1 1 1
n, m, k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
cnt = 0


# 해당 row에 [col_s, col_e] 열에
# 전부 블럭이 없는지를 확인합니다.
def all_blank(row, col_s, col_e):
    return all([
        not grid[row][col]
        for col in range(col_s, col_e + 1)
    ])

    # 최종적으로 도달하게 될 위치는
# 그 다음 위치에 최초로 블럭이 존재하는 순간임을 이용합니다.
def get_target_row():
    for row in range(n - 1):
        if not all_blank(row + 1, k, k + m - 1):
            return row

    return 0

k -= 1

# 최종적으로 멈추게 될 위치를 구합니다.
target_row = get_target_row()

for col in range(k, k + m):
    grid[target_row][col] = 1


# 내 풀이
# 아래부터, m 개수만큼의 0이 있는지 확인했다. 

def is_range(m,k):
    for i in range(n-1,-1,-1):
        global cnt
        cnt = 0
        for j in range(k,k+m):
            if(grid[i][j] == 0):
                cnt += 1
            
        if(cnt >= m):
            for j in range(k,k+m):
                grid[i][j] = 1
            return

# is_range(m,k-1)

for i in range(n):
    for j in range(n):
        print(grid[i][j],end = " ")
    print()
