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
    # 가로
    count = 0
    for i in range(5):
        if sum(bingo[i]) == 5:
            count += 1
    # 세로
    for i in range(5):
        tempSum = 0
        for j in range(5):
            tempSum += bingo[j][i]
        if tempSum == 5:
            count += 1
    # 대각선
    tempSum = 0
    for i in range(4, -1, -1):
        for j in range(5):
            tempSum += bingo[i][j]
        if tempSum == 5:
            count += 1
    # 대각선 2
        tempSum = 0
    for i in range(5):
        for j in range(4, -1, -1):
            tempSum += bingo[i][j]
        if tempSum == 5:
            count += 1
    return count


# mc의 값을 하나씩 순서대로 탐색하면서, 그 값이 어느 곳에 있는지 체크
for i in range(5):
    for j in range(5):
        answer += 1
        temp = mc[i][j]
        # 그 값이 어디있는지 인덱스 값 찾는다.
        I, J = find_index(temp)
        bingo[I][J] = 1
        # 값을 넣고, ... 또 다시 확인하기.....?
        count = count_bingo()
    if count >= 3:
        print(answer)
        break
            

print(bingo)
        
# 11 12 2 24 10
# 16 1 13 3 25
# 6 20 5 21 17
# 19 4 8 14 9
# 22 15 7 23 18
# 11 12 2 24 10
# 16 1 13 3 25
# 6 20 5 21 17
# 19 4 8 14 9
# 22 15 7 23 18
