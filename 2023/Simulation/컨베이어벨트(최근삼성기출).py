# 완전탐색 생각하기
# 완전탐색할 때의 최대의 시간복잡도 계산부터 하기.

# 입력
n, t = map(int, input().split())
up = list(map(int, input().split()))
down = list(map(int, input().split()))

def change():
    # 위에서 가장 오른쪽 숫자 
    temp = up[n-1]

    # 윗줄 완성
    for i in range(n,1,-1):
        up[i-1] = up[i-2]
    up[0] = down[n-1]

    # 아랫줄 완성
    for i in range(n,1,-1):
        down[i-1] = down[i-2]
        # down[0]은 마지막에 넣어줘야한다. for문 앞에서 넣어주면 down[0]값이 사라지기 때문에,
    down[0] = temp     
   

for _ in range(t):
    change()


# 출력
for i in range(n):
    print(up[i], end = " ")
print()
for i in range(n):
    print(down[i], end = " ")


















# # 완전탐색 하기전에 시간복잡도를 생각하기. 
# n,t = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# # 밀고 당기기 
# for _ in range(t):
#     # step 1
#     # 위에서 가장 오른쪽에 있는 숫자를 따로 저장
#     temp = a[n-1]

#     # step 2 : 첫 줄 먼저 다 채워넣기 
#     # for문 순서는 오른쪽부터 즉 뒤에서부터 채워넣기.
#         # a[1~n-1]
#     for i in range(n-1, 0, -1):
#         a[i] = a[i-1]
#         # a[0]
#     a[0] = b[n-1]
#         # 여기서 a[0]를 먼저 저장하면 temp2 사용안해도된다

#     # step 3 : 두번째 줄 채워넣기
#     # temp2 = b[n-1]
#         # for문 순서는 오른쪽부터 즉 뒤에서부터 채워넣기.
#         # b[1~n-1]
#     # 156->563
#     for i in range(n-1,0,-1):
#         b[i] = b[i-1]
#     b[0] = temp
#     # a[0] = temp2

# for i in range(n):
#     print(a[i], end=" ")
# print()

# for i in range(n):
#     print(b[i], end=" ")