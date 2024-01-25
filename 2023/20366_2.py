n = int(input())
snow = list(map(int, input().split()))

snow.sort()
result = 120000000000
for i in range(n-3):
    for j in range(i+3, n):
        elsa = snow[i] + snow[j]
        # 엘사 사이에서 투 포인터
        left, right = i+1, j-1
        while(left < right):
            anna = snow[left] + snow[right]
            difference = abs(elsa - anna)
            realDiff = elsa - anna
            if (difference < result):
                result = difference
            if (realDiff > 0):
                right -= 1
            elif (realDiff < 0):
                left += 1
            elif (realDiff == 0):
                break

print(result)


