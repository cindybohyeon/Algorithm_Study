n = int(input())
num = list(map(int, input().split()))

minnum = num[0]
count = 0
for i in range(0,n):
    # 두 조건문을 lf, else로 두개중 한 곳만 들어가도록 설정해야한다.
    # 그렇지 않으면 count+1이 출력된다.
    if(num[i] < minnum):
        minnum = num[i]
        count = 1
    elif(num[i] == minnum):
        count += 1

print(minnum,count)