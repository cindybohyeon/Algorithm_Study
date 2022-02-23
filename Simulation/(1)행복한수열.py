n,m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
seq = [0 for _ in range(n)]

# 한 줄의 수열의 연속되는 원소개수 = count
def happy():
    count, max_count = 1,1
    for i in range(1,n):
        if(seq[i-1] == seq[i]):
            count += 1
        else:
            count = 1
        # 한 줄의 연속되는 원소개수의 최댓값을 한곳에 저장
        max_count = max(count, max_count)
    
    return (max_count >= m)

ans = 0

# 가로줄부터 함수적용
for i in range(n):
    seq = grid[i][:]
    if happy():
        ans += 1
# 세로줄
for i in range(n):
    for j in range(n):
        seq[j] = grid[j][i]
    if happy():
        ans += 1

print(ans)