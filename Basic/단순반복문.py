# 1부터 19까지 입력하기 위해서 (1.20)입력
# range(A,B)는 A부터 B-1까지를 의미한다.
for i in range(1,20):
    for j in range(1,20):
        # 처음의 조건문 비교 (홀짝)
        if(j%2 != 0):
            print(i , "*", j,"=",i*j,end=" ")
        else:
            print("/",i , "*", j,"=",i*j)
        # 두번째 조건문 비교 : 19번인 경우 줄바꿈하기
        if(j == 19):
            print()