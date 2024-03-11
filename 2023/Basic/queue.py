# 변수 선언 및 입력:
n, k = tuple(map(int, input().split()))
q = Queue()

# 큐로 현재 남은 사람들을 관리합니다.
for i in range(1, n + 1):
    q.push(i)

while q.size() > 1:
    # k번째 사람을 찾습니다.
    # 이 과정에서 이미 탐색한 사람은 맨 뒤로 옮겨줍니다.
    for _ in range(k - 1):
        q.push(q.front())
        q.pop()
    # k번째 사람을 제거합니다.
    print(q.front(), end=" ")
    q.pop()

# 마지막 사람을 제거합니다.
print(q.front(), end=" ")