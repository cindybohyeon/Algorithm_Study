# 반복문으로 변경해서 풀어볼 것
# back tracking
answer = 0
def dfs(idx, tempSum, numbers, target):
    global answer
    if idx == len(numbers) - 1:
        if tempSum == target:
            answer += 1
            return
    else:
        # print(idx,"idx")
        dfs(idx + 1, tempSum + numbers[idx + 1], numbers,target)
        dfs(idx + 1, tempSum - numbers[idx + 1], numbers,target)

def solution(numbers, target):
    dfs(-1, 0, numbers, target)
    
    return answer