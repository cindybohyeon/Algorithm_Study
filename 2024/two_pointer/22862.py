n, k = map(int, input().split())
s = list(map(int, input().split()))

# 수열에서 원하는 위치에 있는 수를 골라 최대 K번 삭제를 할 수 있다.
result = 0
# K번 원소를 삭제한 수열에서 짝수로 이뤄져있는 연속부분 중 가장 긴 길이
count = 0
end = 0
tmp = 0
# 투 포인터는 인덱스를 2개 이용해서 인덱스를 이동시키면서 찾는거

# start를 N까지 증가시키면서 반복한다..
for start in range(n):
    while(count <= k and end < n):
        if s[end] % 2 == 1:
            count += 1
        else:
            tmp += 1
        end += 1
        
        if start == 0 and end == n:
            result = tmp
            break
    if count == k+1:
        result = max(tmp, result)
    if s[start] % 2 == 1:
        count -= 1
    else:
        tmp -= 1

print(result)

# 홀수의 개수