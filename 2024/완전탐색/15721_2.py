# 계속 진행되는 대로 계쏙 더하면서
# 개수를 센다...

a = int(input())
t = int(input())
say = int(input())

graph = []
bunCount = 1
degiCount = 1
while True:

    for _ in range(2):
        graph.append([bunCount, 0])
        bunCount += 1
        graph.append([degiCount, 1])
        degiCount += 1
        