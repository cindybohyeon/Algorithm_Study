# 입력
n = int(input())
block = [0 for _ in range(n)] 
# temp = [0 for _ in range(n)]
for i in range(n):
    block[i] = int(input())
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

def cut_array(s,e):
    # 전역변수 이용해야 한다. 
    global block
    temp = []
    # 1. 빠지는 블록 0으로 설정
    for i in range(s,e+1):
        block[i-1] = 0

    # 2. 존재하는 블록들로 temp생성
    for i in range(len(block)):
        if(block[i] != 0):
            # append함수 기억하기
            temp.append(block[i])
            
    # 3. block 새로 생성
    block = temp
    

cut_array(s1,e1)
cut_array(s2,e2)

# 출력
print(len(block))
for i in range(len(block)):
    print(block[i])


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