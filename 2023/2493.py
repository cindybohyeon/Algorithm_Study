# 탑...
# 일직선위에 N개의 높이가 서로 다른 탑을 수평 직선의 왼쪽부터 오른쪽 방향으로 세우고
# 각 탑의 꼭대기에 레이저 송신기를 설치
# 하나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 하나의 탑에서 수신이 가능

n = int(input())
tops = list(map(int, input().split()))

# 왼쪽 그러니까 자기 값보다 작은 인덱스 중에서, 내 크기보다 크거나 같은거를 찾는다.
result = [0 for _ in range(n)]

def findSend(index):
    global tops, result
    for i in range(index-1, -1, -1):
        if(tops[index] <= tops[i]):
            result[index] = i+1
            break

for i in range(n):
    findSend(i)

print(result)
