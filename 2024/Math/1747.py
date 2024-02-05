n = int(input())

# 어떤 수와 그 수의 숫자 순서를 뒤집은 수가 일치하는 수
# n 보다 크거나 같고, 소수이면서 펠린드롬인 수...

def checkP(n):
    # print(n)
    strN = str(n)
    lenN = len(strN)
    if lenN == 2:
        if strN[0] == strN[1]:
            return True
        return False

    for i in range(lenN // 2):
        # for j in range(-1, ,-1):
        # print(n)
        if strN[i] != strN[lenN - 1 - i]:
            # print(n, "nnn")
            return False
    return True
# 소수인 거는 어떻게 판단하지? 

def checkSosu(n):
    for i in range(2, n):
        if n % i == 0:
            # print(n, "sosu")
            return False
    return True
    # if n % 2 == n % 3 == n % 5 == n:
        # return True
    # return False

while(True):
    if n == 1:
        print(2)
        break
    if checkP(n) and checkSosu(n):
        print(n)
        break
    n += 1
