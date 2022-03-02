n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
x, y = map(int, input().split())

# 4
# 1 2 4 3
# 3 2 2 3
# 3 1 6 2
# 4 5 4 4
# 2 3

# 1 0 0 0
# 3 2 0 3
# 3 1 0 2
# 4 5 4 4
num = 0
def get_0(r,c):
    global num
    num = arr[r-1][c-1]

    for i in range(num):
        if(r-1-i >= 0 and r-1-i <n):
        # 상
            arr[r-1-i][c-1] = 0
        # 하
        if(r-1+i >= 0 and r-1+i <n):
            arr[r-1+i][c-1] = 0
        # 좌
        if(c-1-i >= 0 and c-1-i <n):
            arr[r-1][c-1-i] = 0
        # 우
        if(c-1+i >= 0 and c-1+i <n):
            arr[r-1][c-1+i] = 0

    # print(arr)
temp = [[0 for _ in range(n)] for _ in range(n)]
def new_arr(arr):
    for i in range(n):
        cnt = n-1
        for j in range(n-1,-1,-1):

            if(arr[j][i] != 0):
                temp[cnt][i] = arr[j][i]
                cnt -= 1
            


    for i in range(n):
        for j in range(n):
            print(temp[i][j], end = ' ')
        print()




get_0(x,y)
new_arr(arr)


# 해설
# 변수 선언 및 입력:

n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
next_grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]


def in_bomb_range(x, y, center_x, center_y, bomb_range):
    return (x == center_x or y == center_y) and \
           abs(x - center_x) + abs(y - center_y) < bomb_range


def bomb(center_x, center_y):
    bomb_range = grid[center_x][center_y]
    
    # Step1. 폭탄이 터질 위치는 0으로 채워줍니다.
    for i in range(n):
        for j in range(n):
            if in_bomb_range(i, j, center_x, center_y, bomb_range):
                grid[i][j] = 0
	
    # Step2. 폭탄이 터진 이후의 결과를 next_grid에 저장합니다.
    for j in range(n):
        next_row = n - 1
        for i in range(n - 1, -1, -1):
            if grid[i][j]:
                next_grid[next_row][j] = grid[i][j]
                next_row -= 1
                
    # Step3. grid로 다시 값을 옮겨줍니다.
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

            
r, c = tuple(map(int, input().split()))
bomb(r - 1, c - 1)

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()