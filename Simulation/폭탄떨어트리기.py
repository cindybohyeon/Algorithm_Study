# 폭탄 떨어트리기 문제 
a = [[i*5+j+1 for j in range(5)] for i in range(5)]
for i in range(5):
    for j in range(5):
        if a[i][j] % 2 == 0 or a[i][j] % 3 == 0:
            a[i][j] = 0

temp = [[0 for _ in range(5)] for _ in range(5)]

for col in range(5):
    last_row = 4
    for row in range(4,-1,-1):#맨아래층에서부터 시작
        if(a[row][col] != 0):
            temp[last_row][col] = a[row][col]
            last_row -= 1

a = temp
print(a)