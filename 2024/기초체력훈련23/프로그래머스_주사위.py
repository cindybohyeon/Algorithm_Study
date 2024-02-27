from itertools import combinations
def solution(a, b, c, d):
    answer = 0
    
    # 모두 같은 경우
    if a == b and b == c and c == d:
        answer = 1111 * a
        return answer
    # 세 숫자가 같은 경우
    for x, y, z in combinations([a, b, c, d], 3):
        if x == y and y == z:
            answer = 10 * x
            for temp in [a, b, c, d]:
                if temp != x:
                    answer += temp
                    answer = answer ** 2
                    return answer
    # 두 숫자가 같은 경우
    for x, y in combinations([a, b, c, d], 2):
        if x == y:
            tempList = [a, b, c, d]
            tempList.remove(x)
            tempList.remove(y)
            # print(tempList)
            if tempList[0] == tempList[1]:
                answer = abs(x - tempList[0]) * (x + tempList[0])
                return answer
            else:
                answer = tempList[1] * tempList[0]
                return answer
            
            # for temp in [a, b, c, d]:
            #     if temp != x:
            #         answer += temp
            #         answer = answer ** 2
            #         return answer
    # 두 숫자랑, 서로 다른 숫자
    # 서로 다른 숫자

    # else:
    return min([a, b, c, d])

# array.count(var) 배열원소값을 가진 것들의 개수를 반환한다.

# def solution(a, b, c, d):
#     l = [a,b,c,d]
#     c = [l.count(x) for x in l]
#     if max(c) == 4:
#         return 1111*a
#     elif max(c) == 3:
#         return (10*l[c.index(3)]+l[c.index(1)])**2
#     elif max(c) == 2:
#         if min(c) == 1:
#             return eval('*'.join([str(l[i]) for i, x in enumerate(c) if x == 1]))
#         else:
#             return (max(l) + min(l)) * abs(max(l) - min(l))
#     else:
#         return min(l)