from itertools import permutations

def is_sosu(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
    
def solution(numbers):
    all_per = []
    len_num = len(numbers)
    answer = []
    
    for i in range(1,len_num+1):
        result = list(map(''.join,permutations(numbers, i)))
        for j in list(set(result)):
            # print(j)
            if is_sosu(int(j)):
                answer.append(int(j))
                
    answer = set(answer)
    answer = len(answer)
    return answer

    # 순열 함수
    # set 함수 : 중복 원소 제거