n = int(input())
result = 0
# 생성자가 생길 수 있는 경우의 수 = n의 작은 자연수들.
# 생성자를 정하고 각 자리 수를 하나씩 더하고 비교한다.

for i in range(1, n+1):
    # 각자리수를 더해야한다...
    # map(int, str(i)) = 문자열을 숫자로 변환한다. 그거를 리스트로..
    nums = sum(map(int, str(i)))
    tempNum = i + nums
    if (tempNum == n):
        # print(tempNum, nums,  "tempNu")
        result = i
        break

print(result)



# for i in range(1,10):
#     for j in range(1, 10):
#         for k in range(1, 10):
#             temp = 101 * i + 11 * j + 2 * k
#             if (temp == n):
#                 resultList.append(100 * i + 10*j + k)
# if len(resultList) == 0:
#     print(0)
# else:
#     resultList.sort()
#     print(resultList)
#     print(resultList[0])
