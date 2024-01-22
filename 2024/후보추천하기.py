# 학생회장 후보는 일정기간동안 전체학생의 추천에 의하여 정해진 수 만큼 선정
# 추천받은 학생의 사진을 후보의 수만큼.
# 추천받은 횟수를 표시하는 규칙
# 모든 사진틀은 비어있다
# 추천하면 게시되어야한다 없는 경우 횟수적은 학생삭제한다
# 2명이상이면 오래된 사진을 삭제
# 사진삭제되는 경우는 횟수 0으로 바뀐다

# 사진틀의 개수
n = int(input())
# 전체 학생의 총 추천횟수
recommend = int(input())
student = list(map(int,input().split()))

photolist = []

for s in student: # 입력된 학생 추천번호 for문
    # 아직 사진틀이 채워지지 않은 경우
    if len(photolist) < n: 
        # 입력된 학생을 넣는다
        # 이미 존재한 경우
        already = False
        for photo in photolist: # [추천학생번호, 횟수]
            if s == photo[0]:
                photo[1] += 1
                already = True
        if (already == False):
        # 존재하지 않은 경우
            photolist.append([s, 1])
    # 사진틀이 다 채워진 경우
    else:
        already = False
        for photo in photolist:
            if photo[0] == s:
                photo[1] += 1
                already = True
        if (already == False):
            # 횟수가 가장 적은 학생의 사진을 삭제한다
            # 이차원으로 하면 1번 배열의 값 최소를 못 구하나
            minScore = min(row[1] for row in photolist)
            for i in range(n):
                if photolist[i][1] == minScore:
                    del photolist[i]
                    break
            photolist.append([s,1])

photolist.sort(key= lambda x:x[0])
for photo in photolist:
    print(photo[0], end=" ")

    
            

# 추천받은 횟수도 있어야한다. (ㅁ,ㅁ)