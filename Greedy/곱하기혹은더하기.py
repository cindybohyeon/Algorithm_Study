# 문자열
from unittest import result


n = list(input())

# *와 + 연산자....
# +를 선택하는 상황은 0이 있고나 1이 있거나. 그게 아니라면 곱하기.
# 두개를 다 봐여하는 것이지
num = 0
result = int(n[0])
for i in range(1, len(n)):
    num = int(n[i])
    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num

print(result)


