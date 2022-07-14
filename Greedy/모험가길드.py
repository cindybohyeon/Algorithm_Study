# 모험가 N명이 있다.
# 공포도가 높은 모험가는 능력 안좋음. 
# 공공포도가 X인 모험가는 난듸 X명 이상으로 구성한 모험가 그룹에 참여해야한다. 
# 3은 3명이상 그룹에 가야한다. 
# 그룹의 최댓값을 구하기. 
# 공포도를 정렬했어.
# 현재 그룹에 포함된 모험가의 수가 현재 확인하고 있는 공포도보다 크거나 같다면 

from unittest import result


n = int(input())
people = list(map(int, input().split()))

people.sort()


result = 0 #총 그룹의 수
count = 0 #현재 그룹에 포함된 모험가의 수
for i in people:
    # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1 #현재 그룹에 해당 모험가를 포함시키기
    if count >= i:
        result += 1
        count = 0 #현재 그룹에 포함된 모험가 수 초기화 

print(result)