# atm 이 1대 밖에 없다 .
n = int(input())
people = list(map(int, input().split()))
people.sort()
sum = 0
for i in range(1,n+1):
    for j in range(i):
        sum += people[j]

print(sum)