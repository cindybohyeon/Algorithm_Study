restNum = int(input())
restPeople = list(map(int, input().split()))
leader, member = map(int, input().split())
result = 0
# 각 식당별로 체크를 해야한다.

for rest in range(restNum):
    # 식당의 개수만큼 체크한다.
    tempPeople = restPeople[rest] #현재 가게의 인원.
    tempResult = 0
    # 먼저 팀장의 최대인원으로.
    tempPeople -= leader
    tempResult += 1
    # 팀원이 필요한 경우
    if (tempPeople > 0):
        check = tempPeople // member
        # print(check, "#")
        tempResult += check
        remain = tempPeople % member
        if (remain != 0):
            tempResult += 1

    result += tempResult
        
print(result)