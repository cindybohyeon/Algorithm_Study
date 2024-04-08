def solution(clothes):
    answer = 0
    
    dict1 = {}
    for v, t in clothes:
        if t not in dict1:
            dict1[t] = 2
            # 2로 초기화 하는 이유 : 해당 유형이 없는 경우의 수까지 포함하는 것.
        else:
            dict1[t] += 1
    
    temp = 1
    for i in dict1.values():
        temp *= i
    return temp -1 
    
#     cLen = len(clothes)
#     separate = []
#     for c in clothes:
#         if c[1] not in separate:
#             separate.append(c[1])
            
#     sLen = len(separate)
#     # 종류가 1개밖에 없는 경우
#     if sLen == 1:
#         answer = cLen
#         return answer
#     # 종류가 2개 이상인경우.
#     countS = [ 0 for _ in range(sLen)]
    
#     for i in range(sLen): # 종류별의 개수 세기
#         for c in clothes:
#             if c[1] == separate[i]:
#                 countS[i] += 1
#     print(countS)
#     tempCount = 1
#     for i in countS:
#         tempCount = tempCount * i 
#     answer = tempCount + cLen
    
    
#    clothes_type = {}

#     for c, t in clothes:
#         if t not in clothes_type:
#             clothes_type[t] = 2
#         else:
#             clothes_type[t] += 1

#     cnt = 1
#     for num in clothes_type.values():
#         cnt *= num

#     return cnt - 1
    
    return answer