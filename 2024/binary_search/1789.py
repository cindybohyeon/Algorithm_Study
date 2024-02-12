n = int(input())

# 이분탐색
graph = [0 for _ in range(n)]

start = 1
end = n
result = 0
while start <= end:
    mid = (start + end) // 2

    if mid * (mid + 1) // 2 == n:
        result = mid       
        break
    elif (mid * (mid + 1) // 2 < n):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)

def bs(target, data):
    data.sort()
    start = 0
    end = len(data) - 1
    

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return None

