a = int(input())
t = int(input())
say = int(input())

# T번째 번 또는 데기를 외치는 사람은 위 원에서 몇 번 사람인지를 구하라

bundegi = []
bun = degi = 1
n = 0

while True:
    prev_n = bun # 번이든 , 데기이든 한 번에 카운팅되는 수가 같음
    n += 1
    for _ in range(2):
        bundegi.append((bun, 0)) #왜 이렇게 넣는걸까 - 첫번째의. 0이다?
        bun += 1 # 몇번쨰의 번인지 카운팅
        bundegi.append((degi, 1))
        degi += 1
    for _ in range(n+1):
        bundegi.append((bun, 0)) #왜 이렇게 넣는걸까 - 첫번째의. 0이다?
        bun += 1 # 몇번쨰의 번인지 카운팅
    for _ in range(n+1):
        bundegi.append((degi, 1))
        degi += 1
    if prev_n < t <= bun:
        print(bundegi.index((t, say)) % a)
        break


