# 특정조건이란 현재 캐릭터의 점수를 n이라고 할 때
import string


n_input = list((input()))
string_len = len(n_input)
first_sum = 0
second_sum = 0
for i in range(0, string_len//2):
    first_sum += int(n_input[i])
    second_sum += int(n_input[i+string_len//2])

if first_sum == second_sum:
    print("L")
else:
    print("R")

