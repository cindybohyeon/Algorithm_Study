# current = str(input())
# sodium = str(input())

# # 하나의 단위로 바꿔야한다.
# currentHour = int(current[:1]) * 60 * 60
# currentMin = int(current[3:4]) * 60
# curremtSec = int(current[6:])

# currentTotal = currentHour + currentMin + curremtSec

# # 하나의 단위로 바꿔야한다.
# currentHour2 = int(sodium[:1]) * 60 * 60
# currentMin2 = int(sodium[3:4]) * 60
# curremtSec2 = int(sodium[6:])

# currentTotal2 = currentHour2 + currentMin2 + curremtSec2

# waitingTotal = abs(currentTotal - currentTotal2)

# waitingHour = waitingTotal // 6
import sys
input = sys.stdin.readline

h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
total = h1*60*60 + m1*60 + s1
total2 = h2*60*60 + m2*60 + s2
t = total2 - total
if (total2 - total <= 0):
    t = t + 24*60*60

h = t//60//60
m = t//60 % 60
s = t % 60
print("%02d:%02d:%02d" % (h, m, s))