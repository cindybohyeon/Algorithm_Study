# 한 줄에 하나의 암호가 주어진다.
codeList = []

while(True):
    code = str(input())
    if (code == 'END'):
        break
    codeList.append(code)

codeLen = len(codeList)
for c in codeList:
    for i in range(len(c)-1, -1, -1):
        print(c[i], end='')
    print()