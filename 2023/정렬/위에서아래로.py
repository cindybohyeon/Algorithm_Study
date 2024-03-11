# 하나의 수열에는 다양한 수가 존재한다. 
# 이러한 수는 크기에 상관없이 나열되어 잇다. 
# 큰수에서 작은수로 정렬해야한다. 내림차순으로 정렬하기

n = int(input())
arr = []
for _ in range(n):
    x = int(input())
    arr.append(x)
    # 두줄을 한줄로 가능
    # arr.append(int(input()))

arr.sort(reverse=True)

print(arr)