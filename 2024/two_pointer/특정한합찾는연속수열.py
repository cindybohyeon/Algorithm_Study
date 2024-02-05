n, m = map(int, input().split())
graph = list(map(int, input().split()))

end = 0
result = 0
count = 0
for start in range(n):
    # 동일한 인덱스를 잡고
    # 조건과 end의 인덱스 범위에 맞는 경우 반복.
    while result < m and end < n:
        # 연속되는 수열의 합을 만든다
        result += graph[end]
        end += 1

    # 정해진 start 부터 end까지 조건에 맞게 만든 값이 예측값과 같으면
    if result == m:
        count += 1
    
    # start를 한 칸 옮기기 전에 결과값에서도 start이전의 값을 뺌
    result -= graph[start]

print(count)