n, k = map(int, input().split())
graph = list(map(int, input().split()))

# 최대 K 번 원소를 삭제한 수열에서 짝수로 이뤄져 있는 연속한 부분
# 가장 긴 길이 출력..
result = 0
start = 0
end = 0
count = 0
for start in range(n):
    while count < k and end < n:
        if graph[end] % 2 == 1: #홀수인 경우 삭제가능
            count += 1
        end += 1
    
    temp = graph[start:end]
    result = max(result, len(temp) - count)

print(result)