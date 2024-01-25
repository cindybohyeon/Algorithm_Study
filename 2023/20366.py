import sys
input = sys.stdin.readline
n = int(input())
# 눈덩이 지름을 의미하는 정수
graph = list(map(int, input().split()))

graph.sort()
ans = 4000000001
# 2 3 5 5 9
# 어떻게 탐색을 해야하는거지
# 두개를 고른 합의 값이 

for i in range(n-3):
    for j in range(i + 3, n):
        left, right = i + 1, j - 1
        elsa = graph[i] + graph[j]
        # 투 포인터를 여기서 한번 더
        while (left < right):
            tmp = (graph[i] + graph[j]) - (graph[left] + graph[right])
            # 둘의 차이가 현재 차이보다 더 작은 경우
            if (abs(tmp) > abs(ans)):
                ans = abs(tmp)
            # 투 포인터 이동은 양수음수에 따라서 다르게
            if tmp < 0: 
                right -= 1
            elif (tmp > 0): 
                left += 1
            elif (tmp == 0):
                print(0)
                sys.exit(0)


print(ans)

