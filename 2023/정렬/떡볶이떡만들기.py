# 높이를 지저하면 줄지어진 떡을 한 번에 절단한다. 
# ㅈ19.14.10.17이 ㄴ있고 절단기 높이 15 지정하면

n,m = map(int, input().split())
n_arr = list(map(int, input().split()))
n_arr.sort()

start = 0
end = n_arr[n-1]

while start <= end:
    mid = (start + end) // 2
    sum = 0

    # 잘랐을 때 떡 계산 시, 뺀 값이 음수 양수인지 확인하고 더하기
    for i in range(n):
        if (n_arr[i] - mid) > 0:
            sum += n_arr[i] - mid
    
    if sum == m:
        break
    if sum > m:
        start += 1
    else:
        end -= 1

print(mid)


        