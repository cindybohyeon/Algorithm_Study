# 왕실정원의 특정한 한 칸에 나이트가 서있다.
# 나이트는 L자 형태로만 이동. => 수평으로 두 칸 + 수직으로 한 칸 아님 그 반대로 . 
# 8*8좌표 펴안에서 나이트 위치에 따른 이동 경우의 수

import re


position = list(input())
result = 0

# 움직일 수 있는 경우의 수는 최대 8가지 이다. 
dx = [-1,1,2,2,1,-1,-2,-2]
dy = [2,2,1,-1,-2,-2,-1,1]

def in_range(x,y):
    if x >= 0 and y >= 0 and x <8 and y <8:
        return True
    else:
        return False


def move(n,m):
    global result
    for i,j in zip(dx,dy):
        nx = n + i
        ny = m + j
        if in_range(nx,ny):
            result += 1


hang = ['a','b','c','d','e','f','g','h']
for i in range(8):
    if position[0] == hang[i]:
        position[0] = i
        position[1] = int(position[1]) -1

move(position[0],position[1])

print(result)

