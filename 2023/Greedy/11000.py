# 수강신청 과제 주어짐
# 최소의 강의실을 사용해서 모든 수업을 가능하게

# n개의 수업. 

# n = int(input())
# room = []

# for _ in range(n):
#     a,b = map(int, input().split())
#     room.append([a,b])
# room.sort(key= lambda x:x[1])
# room.sort(key=lambda x : x[0])
# # room.sort(key= lambda x:x[1])



# # print(room)
# classnum = 1
# count = n
# last_room = room[0][1]
# for i in range(1,n):
#     if room[i][0] <= last_room:
#         count -= 1
#         last_room = room[i][0]
#     else:
#         classnum += 1

    

# print(classnum)

import heapq
import sys

n = int(input())
room = []
for _ in range(n):
    a, b = list(map(int, input().split()))
    room.append([a,b])

# 시작시간 정렬
room.sort(key = lambda x : x[0])

heap = []
for i in range(n):
    if len(heap) != 0 and heap[0] <= room[i][0]:
        heapq.heappop(heap)   
    heapq.heappush(heap,room[i][1])

print(len(heap))
# print(heap)
# cnt = 1
# end = room[0][1]
# print(end)
# for i in range(1,n):
#     if room[i][0] >= end:
#         cnt += 1
        
#         end = room[i][1]
#         print(end)


# print(cnt)