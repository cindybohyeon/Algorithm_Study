graph = [list(map(int, input().split())) for _ in range(5)]

mc = [list(map(int, input().split())) for _ in range(5)]

bingo = [[0 for _ in range(5)] for _ in range(5)]

answer = 0

def find_index(value):
    for i in range(5):
        for j in range(5):
            if graph[i][j] == value:
                return (i, j)
    

def count_bingo():
    global bingo
    # 가로
    count = 0
    for i in range(5):
        if sum(bingo[i]) == 5:
            # print("#########", i)
            # print(bingo)
            count += 1
    # 세로
    for i in range(5):
        tempSum = 0
        for j in range(5):
            tempSum += bingo[j][i]
            
        if tempSum == 5:
            # print("세로", bingo)
            count += 1
    # 대각선
    tempSum = 0
    for i in range(5):
        tempSum += bingo[i][i]
    if tempSum == 5:
        count += 1
    # 대각선 2
    tempSum = 0
    for i in range(5):
        tempSum += bingo[i][4 - i]
    if tempSum == 5:
        count += 1
    if count >= 3:
        print(bingo, "bingo")
    return count
real = 25

# mc의 값을 하나씩 순서대로 탐색하면서, 그 값이 어느 곳에 있는지 체크
for i in range(5):
    for j in range(5):
        answer += 1
        temp = mc[i][j]
        # 그 값이 어디있는지 인덱스 값 찾는다.
        ii, jj = find_index(temp)
        bingo[ii][jj] = 1
        # 값을 넣고, ... 또 다시 확인하기.....?
        count = count_bingo()
        if count >= 3:
            real = min(real, answer)
        
            

# print(bingo)
print(real)
        
# 11 12 2 24 10
# 16 1 13 3 25
# 6 20 5 21 17
# 19 4 8 14 9
# 22 15 7 23 18
# 11 12 2 24 10
# 16 6 19 22 1
# 5 14 9 13 3
# 25 20 21 17 4
# 8 15 7 23 18

# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 18 19 20
# 16 17 13 14 15
# 21 22 23 24 25