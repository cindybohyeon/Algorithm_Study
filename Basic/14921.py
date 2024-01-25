import math
n = input()
nums = list(map(int, input().split()))

result = 20000000
ans = 0
left = 0
right = n - 1

def difference(check):
    return math.fabs(check)

while (left < right):
    tmp = nums[left] + nums[right]
    # print(tmp, "tmp")
    if (tmp < 0): # 음수인 경우는 앞에거를 앞으로 땡긴다
        left += 1
        tmpResult = difference(tmp)
        if (tmpResult < result):
            result = tmpResult
            ans = tmp
    elif (tmp > 0):
        right -= 1
        tmpResult = difference(tmp)
        if (tmpResult < result):
            result = tmpResult
            ans = tmp
    elif (tmp == 0):
        ans = tmp
        break

print(ans)


