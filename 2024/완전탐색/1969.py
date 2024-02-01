n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(str, input())))

# 모든 DNA와 비교를 해야한다....
# 만들 수 있는 거는 .. 4 *  4 * 4 000 이거 아니야?
# checkList = [[0] * 4 for _ in  range(m)]
checkList = []
# print(checkList)
for i in range(m):
    countT = 0
    countA = 0
    countG = 0
    countC = 0
    for j in range(n):
        if graph[j][i] == 'T':
            countT += 1
        if graph[j][i] == 'A':
            countA += 1
        if graph[j][i] == 'G':
            countG += 1
        if graph[j][i] == 'C':
            countC += 1
    # print(countT, countA, countG, countC)
    checkList.append([countA,countC,countG, countT])
# print(checkList)

alpha = ['A', 'C', 'G', 'T']
result = []
resultSum = 0
for check in checkList:
    tempNum = 0
    tempChar = ''
    tempCount = 0
    for i in range(4):
        if tempNum < check[i]:
            tempNum = check[i]
            tempChar = alpha[i]
            tempCount = n - check[i]
    resultSum += tempCount
    result.append(tempChar)

result = ''.join(result)
print(result)
print(resultSum)