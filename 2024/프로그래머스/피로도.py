from itertools import permutations 
import copy
def solution(k, dungeons):
    answer = -1
    # 일정 피로도를 사용해서 던전을 탐험할 수 있다.
    # 각 던전마다 탐험을 시작하기 위해 필요한 
    
    # (1) 모든 순서의 경우의 수에 대해 check 한다. => 순열
    # (2) 나열된 한 경우에서, 순서대로 진행.
    dLen = len(dungeons)
    countArr = []
    for tempList in permutations(dungeons, dLen):
        tempList = list(tempList) # 하나의 순서 리스트
        tempCount = 0
        copyK = copy.deepcopy(k)
        for a, b in tempList: # 리스트 원소값 순서대로 던전들어가는지 센다.
            if copyK >= a and copyK >= b:
                copyK -= b
                tempCount += 1
            else:
                break
        countArr.append(tempCount)
    # print(countArr)
    if countArr != []:
        answer = max(countArr)
            
        
        
        # answer = max(tempCount, answer)
        
    return answer