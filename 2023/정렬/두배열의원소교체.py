# 두개의 배열 n개의 원소로 구성. 
# 배열의 원소는 모두 자연수이다. k번의 바꿔치기 연산 가능.
# A원소합이 최대가 되도록 하기 

n,k = map(int, input().split())
Aarray = list(map(int, input().split()))
Barray = list(map(int, input().split()))

Aarray.sort()
Barray.sort(reverse=True)

for i in range(k):
    if Aarray[i] < Barray[i]:
        Aarray[i] = Barray[i]

ans = 0
for i in range(n):
    ans += Aarray[i]
# 아니면 
# sum(Aarray) 이용하기 

print(ans)