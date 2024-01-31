n, kk = map(int, input().split())
# 모든 시각 중에서 K가 하나라도 포함되는 모든 시각?
# result = 0
# temp_result = 0
# if (k <= n):
#     # k시인 경우일 때 모든 분초
#     result += 60 * 60
#     # k시아닌 경우에서 분에서 3이 나온 경우
#     temp_result = ((6*k + 8) * 60) * (n) 
#     + (6*k + 8) * n - ((6*k + 8) * (6*k +8) * n)
#     result += temp_result
# print(result)
count = 0
strK = str(kk)
# 모든 시각
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if (i < 10):
                tempI = '0' + str(i)
            else:
                tempI = str(i)
            if (j < 10):
                tempJ = '0' + str(j)
            else:
                tempJ = str(j)
            if (k < 10):
                tempK = '0' + str(k)
            else:
                tempK = str(k)
            if (strK in tempI or strK in tempJ or strK in tempK):
                count+=1

print(count)