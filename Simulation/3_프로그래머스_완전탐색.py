def solution(brown, yellow):
    answer = []
#   브라운은 2a+2b - 4 = 10
#   옐로우는 a-2 * b-2 = 2
    mat = int((brown + 4) / 2)

    if yellow == 1:
        answer.append(3)
        answer.append(3)
        return answer
        
    for i in range(3,mat-3):
        if mat-i > 2:
            a = mat-i
            b = i
            if(yellow == (a-2)*(b-2)):
                answer.append(a)
                answer.append(b)
                return answer