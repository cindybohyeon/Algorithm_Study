# 0과 1로 이뤄진 문자열 S
# 모든 숫자를 전부 같게 만드는 것. 
n = list(input())
# 어떤 숫자가 많이 들어 있는지 알수있을까
len_n = len(n)

# def check(n, len(n)):
#     sum_n = sum(n)
#     if sum_n >= len(n)/2:
#         return True
#     else:
#         return False
change1 = 0
change0 = 0
num = int(n[0])
if num == 0:
    change0 = 1
else:
    change1 = 1

for i in range(1, len(n)):
    if int(n[i]) == num:
        continue
    else:
        if num == 0:
            change0 += 1
        else:
            change1 += 1
        num = int(n[i])

print(min(change0, change1))

