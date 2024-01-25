n, c = map(int, input().split())
graph = []
for i in range(n):
    a = int(input())
    graph.append(a)
graph.sort()
start = 0
end = n - 1

# 배엵의 값을 따지는 것이 아니라 노드 사이의 거리
def bs(array, start, end):
    while(start <= end):
        mid = (start + end) // 2
        current = array[0]
        count = 1
        # 먼저 첫번째 집에 넣는다

        for i in range(1, len(array)):
            if (array[i] >= current + mid):
                count += 1
                current = array[i]
        
        if (count >= c):
            
# 가장 인접한 두 공유기 사이의 최대 거리

