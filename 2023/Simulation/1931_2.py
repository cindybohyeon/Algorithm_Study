from decimal import ROUND_DOWN


n = int(input())
room = []

for _ in range(n):
    a, b = list(map(int, input().split()))
    room.append([a,b])

# 회의실.. 최대 많이 하려면 
# 시작시간 종료시간에서 빨리 종료되는 것 먼저 찾기,, 
room.sort(key= lambda x:x[1])
# print(room)
end = room[0][1]
cnt = 1
for i in range(1,n):
    if room[i][0] >= end:
        cnt += 1
        
        end = room[i][1]
        # print(end)

print(cnt)