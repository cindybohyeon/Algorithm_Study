# 에너지 드링크 ~~
# 두 에너지 드링크 고르기
# 한쪽을 다른쪽에 붓기, 1/2을 붓기
# a의 양을 xa + (xb / 2)로 만들고, b를 버리기
from collections import deque
n = int(input())
energy_list = list(map(int, input().split()))

#  최대의 양을 원한다면, 버리는 양을 정할 때 적은 드링크를 선택해야지
energy_list.sort()
# print(energy_list)
len_energy = len(energy_list)
first = energy_list[0]
second = energy_list[len_energy-1]
sum = 0

for i in range(0,n-1):
    sum += energy_list[i] / 2 

sum += second
sum = round(sum)
# print('%g'%sum)
print(sum)
