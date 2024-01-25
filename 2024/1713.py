n = int(input())
count = int(input())
student = list(map(int, input().split()))
picture = []
exist = False
# 비어있는 사진틀이 없는 경우 추천받은 횟수 가장 적은 학생 삭제
# 두명이상인 경우 가장 오래된 사진 삭제
test = 0
for s in student:
    test += 1
    # 아직 자리가 있는 경우
    if (len(picture) < n):
        exist = False
        # 이미 존재하는 경우
        for i in range(len(picture)):
            if s == picture[i][0]:
                picture[i][1] += 1
                exist = True
                break
        # 신규인 경우
        if (exist == False):
            picture.append([s, 1])
    # 자리 없는 경우
    else:
        exist = False
        # 이미 존재하는 경우
        for i in range(len(picture)):
            if s == picture[i][0]:
                picture[i][1] += 1
                exist = True
                break
        # 신규인 경우
        if (exist == False):
            minscore = 1001
            for i in range(n):
                minscore = min(picture[i][1], minscore)
            for i in range(n):
                if (picture[i][1] == minscore):
                    del picture[i]
                    break

            picture.append([s, 1])
    # print(picture,  "test")
        
picture.sort(key=lambda x:x[0])
for p in picture:
    print(p[0], end=" ")