import sys
input = sys.stdin.readline

a, b, c, m = map(int, input().split())
tired = 0
work = 0
# 각 시간마다 피로도를 체크하고 안 넘었으면 계속 일하는게 최대인 것 같음 
for i in range(24):
    # print(work, tired,"work, tired")
    if (a > m):
        break
    # 일 더 해도 되는지 체크
    if (tired + a > m):
        # 더 할 경우 m 넘어간다
        if (tired - c < 0):
            tired = 0
        else:
            tired -= c
    else:
        tired += a
        work += b

print(work)
