# while(True):
#     n = int(input())        
#     if n == 99999:
#         break
#     for i in range(1,n+1):
#         print(" "*(n - i) + "*" * i)



# for k in range(3):
#     for i in range(1, 10):
#         for j in range(1, 4):
#             print(j + 3*k, "x" , i , '=' , (j + 3*k)*i ,end= " ")
#         print()
#     print()


# nums = list(map(int, input().split()))
# n = int(input())

# print(nums[n-1])

# score = list(map(int, input().split()))
# lenS = len(score)
# sum, maxS = 0, score[0]
# for s in score:
#     sum += s
#     if maxS < s:
#         maxS = s
# print(sum // lenS, maxS)
# print(sum(score)//5, max(score))

from itertools import combinations
nums = list(map(int, input().split()))
target = int(input())
result = []
nums.sort()
# [2, 7, 11, 15]
start = 0
end = len(nums) - 1
while(start <= end):
    temp = nums[start] + nums[end]
    if temp > target:
        end -= 1
    elif temp < target:
        start += 1
    else:
        result = [start, end]
        print(result)
        break






# 객체지향 프로그래밍이 무엇인가
# deque/queue
#  complete 
# linked list
# 그리디, 탐욕 알고리즘.
# 시간복잡도
    

# for a,b in combinations(nums, 2):
#     if a + b == target:

#         result.append(nums.index(a))
#         # del nums[nums.index(a)]
#         result.append(nums.index(b))
#         # print(nums.find(a))
#         break
# print(result)


