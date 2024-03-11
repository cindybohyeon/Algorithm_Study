# 1. 입력
n,r,c = map(int, input().split())
# n+1으로 입력받는 것에 맞추기. 
graph = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]
for i in range(1, n + 1):
    given_row = list(map(int, input().split()))
    for j, elem in enumerate(given_row, start = 1):
        # for index, value in enumerate(리스트, start=숫자)
        # start index를 1로 한다. 
        graph[i][j] = elem

# 2. 결과값
visited_nums = []


# 3. 함수 이용하기
# def in_range(newx, newy):
#     #격자 안에 있다.
#     return 1 <= newx and newy >= 1 and newx =< n and newy =< n
def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n

def can_go(newx,newy,curr_num):#격자 안에 있고, 해당 원소 값보다 더 크다.
    return in_range(newx,newy) and graph[newx][newy] > curr_num

dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 해당 r,c에서, 상하좌우 중에 제일 큰 것으로 rc가 변한다. 
def findbig():
    global r
    global c
    for i in range(4):
        newx = r + dx[i]
        newy = c + dy[i]
        if can_go(newx,newy,graph[r][c]):
            r = newx
            c = newy
            return True
    # 한번 상하좌우 순회할 때 이동할 곳이 없는 경우
    return False


# 4.  여러번 순회하기. 
visited_nums.append(graph[r][c])
while True:
    big_exist = findbig()
    if not big_exist:
        break
    visited_nums.append(graph[r][c])

# 5. 출력하기
# leng = int(len(visited_nums))
# for i in leng:
#     print(visited_nums[i], end=" ")
# 이거는 이중배열일 때 하는것. 

for num in visited_nums:
    print(num, end=' ')
