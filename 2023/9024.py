t = int(input())

answer = []

def makeResult(n, k, graph):
    count = 0
    difference = 20000000
    start, end = 0, n-1
    while(start < end):
        temp = graph[start] + graph[end]
        if (abs(temp - k) < difference):
            count = 1
            difference = abs(temp-k)
            if (temp > k):
                end -= 1
            elif (temp < k):
                start += 1
            else: # 왜 같은경우에는 둘다 움직이는 걸까?
                start += 1
                # end -= 1
        elif (abs(temp - k) > difference):
            if (temp > k):
                end -= 1
            elif (temp < k):
                start += 1
            else:
                start += 1
                # end -= 1
        elif (abs(temp - k) == difference):
            count += 1
            if (temp > k):
                end -= 1
            elif (temp < k):
                start += 1
            else:
                start += 1
                # end -= 1

    return count

for _ in range(t):
    n, k = map(int, input().split())
    graph = list(map(int, input().split()))
    graph.sort()
    answer.append(makeResult(n, k, graph))

for a in answer:
    print(a)