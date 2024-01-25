# 용액의 범위를 보면 완전탐색은 아닌 것이 확실하다.

N = int(input())
arr = list(map(int, input().split()))
# 이미 정렬된 arr

start = 0
end = len(arr) - 1
# print(arr, "arr")

answer = 200000000

def check(temp):
    global answer
    # print(temp,answer,"temp answer")
    if (abs(answer) > abs(temp)):
        # print(temp,"temp")
        answer = temp

while (start < end):
    temp = arr[start] + arr[end]
    # print(temp,"temp while")
    # temp 가 양수인 경우 음수쪽으로 가야 0에 더 가까워질 수 있음
    if (temp > 0):
        end -= 1
        # 해당 값에 대한 절댓값이 현재 값보다 작은 경우 정답대입
        # print(temp,"temp while 2")
        check(temp)
    # temp 가 음수인 경우 양수쪽으로 가야 0에 더 가까워질 수 있음
    elif (temp < 0):
        start += 1
        check(temp)
    elif (temp == 0):
        answer = temp
        break

print(answer)

