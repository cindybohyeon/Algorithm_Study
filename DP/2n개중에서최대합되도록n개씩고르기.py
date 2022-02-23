import sys

INT_MIN = -sys.maxsize

# 변수 선언 및 입력
n = int(input())
red = [
    0
    for _ in range(2 * n + 1)
]
blue = [
    0
    for _ in range(2 * n + 1)
]

# dp[i][j][k] :
# i번째 카드 쌍까지 고려해봤을 때
# 지금까지 빨간색 카드는 정확히 j장 뽑았고
# 지금까지 파란색 카드는 정확히 k장 뽑았다 했을 때
# 얻을 수 있는 뽑힌 숫자들의 최대 합
dp = [
    [
        [0 for _ in range(2 * n + 1)]
        for _ in range(2 * n + 1)
    ]
    for _ in range(2 * n + 1)
]


def initialize():
    # 최대를 구하는 문제이므로, 
    # 초기에는 전부 INT_MIN을 넣어줍니다.
    for i in range(2 * n + 1):
        for j in range(2 * n + 1):
            for k in range(2 * n + 1):
                dp[i][j][k] = INT_MIN
    
    # 0번째 카드 쌍까지 고려해봤을 때에는
    # 아직 고른 카드가 없기 때문에
    # 빨간색, 파란색 카드 모두 0개를 뽑은 상황에
    # 뽑은 숫자들의 합은 0입니다.
    dp[0][0][0] = 0


for i in range(1, 2 * n + 1):
    red[i], blue[i] = tuple(map(int, input().split()))
    
initialize()

for i in range(1, 2 * n + 1):
    # i개의 카드 쌍에 대해 전부 카드 선택을 완료했을 때
    # 지금까지 뽑은 빨간색 카드 수가 j이고
    # 지금까지 뽑은 파란색 카드 수가 k였을 때
    # 가능한 선택한 카드 숫자의 최대합을 계산합니다.

    # 이러한 상황을 만들기 위한 선택지는 크게 2가지 입니다.
    for j in range(i + 1):
        for k in range(i + 1):
            # Case 1
            # i번째 카드 쌍에서 빨간색 카드를 선택하여 
            # 최종적으로 빨간색이 j개, 파란색이 k개가 된 경우입니다.
            # 따라서 i - 1번째 카드 쌍 까지는 빨간색을 j - 1개, 파란색을 k개 뽑았어야 비로소
            # i번째에 빨간색 카드를 선택하게 되므로서 빨간색이 j개, 파란색이 k개가 될 수 있습니다.
            # 이 경우 dp[i - 1][j - 1][k] 에 i번째 카드 쌍 중 빨간색 카드에 적혀있는 숫자인
            # red[i]를 더한 것이 한 가지 경우가 됩니다.
            # 당연히 j가 0보다 커야지만이 만들어질 수 있는 경우입니다.
            if j > 0:
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k] + red[i])

            # Case 2
            # i번째 카드 쌍에서 파란색 카드를 선택하여
            # 최종적으로 빨간색이 j개, 파란색이 k개가 된 경우입니다.
            # 따라서 i - 1번째 카드 쌍 까지는 빨간색을 j개, 파란색을 k - 1개 뽑았어야 비로소
            # i번째에 파란색 카드를 선택하게 되므로서 빨간색이 j개, 파란색이 k개가 될 수 있습니다.
            # 이 경우 dp[i - 1][j][k - 1] 에 i번째 카드 쌍 중 파란색 카드에 적혀있는 숫자인
            # blue[i]를 더한 것이 한 가지 경우가 됩니다.
            # 당연히 k가 0보다 커야지만이 만들어질 수 있는 경우입니다.
            if k > 0:
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k - 1] + blue[i])

# 총 2 * n개의 카드 쌍에 대해 전부 카드 선택을 완료했을 때
# 빨간색 카드, 파란색 카드 모두 각각 n개씩 뽑았다 했을 때
# 가능한 최대 합에 해당하는 dp 값을 출력합니다.
print(dp[2 * n][n][n])





import sys
INT_MIN = -sys.maxsize

n = int(input())
red = [0 for _ in range(2*n+1)]
blue = [0 for _ in range(2*n+1)]

for i in range(1,2*n+1):
    red[i], blue[i] = map(int, input().split())

# red 를 n개 중에 몇개를 뽑았는지
# blue를 n개 중에 몇개를 뽑았는지
# dp [n]에서 합이 현재 몇인자
dp =[
    [
        [0 for _ in range(2 * n + 1)]
        for _ in range(2 * n + 1)
    ]
    for _ in range(2 * n + 1)
]

def initialize():
    for i in range(1,2*n+1):
        for j in range(1,2*n+1):
            for k in range(1,2*n+1):
                dp[i][j][k] = INT_MIN

    dp[0][0][0] = 0

initialize()

# dp[n]은 

for i in range(1,2*n+1):
    for j in range(i+1):
        for k in range(i+1):
            # i개의 카드 쌍에 대해서
            if j > 0:
                # 
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][k] + red[i])
            if k > 0:
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1] +blue[i])


print(dp[2*n][n][n])