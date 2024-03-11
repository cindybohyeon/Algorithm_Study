def solution(answers):

#     1번 수포자
    one_ans = []
    two_ans = []
    thr_ans = []
    for i in range(2000):
        one_ans.append(1)
        one_ans.append(2)
        one_ans.append(3)
        one_ans.append(4)
        one_ans.append(5)
    # one_ans = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
        two_ans.append(2)
        two_ans.append(1)
        two_ans.append(2)
        two_ans.append(3)
        two_ans.append(2)
        two_ans.append(4)
        two_ans.append(2)
        two_ans.append(5)
    for i in range(1000):
        thr_ans.append(3)
        thr_ans.append(3)
        thr_ans.append(1)
        thr_ans.append(1)
        thr_ans.append(2)
        thr_ans.append(2)
        thr_ans.append(4)
        thr_ans.append(4)
        thr_ans.append(5)
        thr_ans.append(5)



    ans_count = len(answers)
    one_count = 0
    two_count = 0
    thr_count = 0

    for i in range(ans_count):
        if answers[i] == one_ans[i]:
            one_count += 1
        if answers[i] == two_ans[i]:
            two_count += 1
        if answers[i] == thr_ans[i]:
            thr_count += 1


    answer = []     
    maxcount = max(one_count,two_count,thr_count)
    if maxcount == one_count:
        answer.append(1)
    if maxcount == two_count:
        answer.append(2)
    if maxcount == thr_count:
        answer.append(3)

    return answer

    # 정답코드

# 전체 리스트의 패턴만 저장한 뒤,
# %을 이용해서 사용한다. 


def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result

# 수정한 코드

def solution(answers):

    one_ans = [1,2,3,4,5]
    two_ans = [2,1,2,3,2,4,2,5]
    thr_ans = [3,3,1,1,2,2,4,4,5,5]
    
    ans_count = len(answers)
    one_count = 0
    two_count = 0
    thr_count = 0
    
    for i in range(ans_count):
        if answers[i] == one_ans[i%len(one_ans)]:
            one_count += 1
        if answers[i] == two_ans[i%len(two_ans)]:
            two_count += 1
        if answers[i] == thr_ans[i%len(thr_ans)]:
            thr_count += 1
            
            
    answer = []     
    maxcount = max(one_count,two_count,thr_count)
    if maxcount == one_count:
        answer.append(1)
    if maxcount == two_count:
        answer.append(2)
    if maxcount == thr_count:
        answer.append(3)

    return answer