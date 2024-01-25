n = int(input())
graph = list(map(int, input().split()))

graph.sort()

# 공포수는 큰 사람
count = 0
# 그룹 개수
group = 0

for g in graph:
    count += 1 # 그룹 인원 추가
    if count >= g: # 인원의 공포도가 그룹의 인원수보다 적으면
        group += 1
        count = 0

print(group)