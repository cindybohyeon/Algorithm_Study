n, t = map(int, input().split())
one = list(map(int, input().split()))
two = list(map(int, input().split()))
three = list(map(int, input().split()))

# 124
# 593
# 651

# 112
# 459
# 365

def change():
    temp = one[n-1] 
    temp2 = two[n-1]
    temp3 = three[n-1]
    for i in range(n,1,-1):
        one[i-1] = one[i-2]
        two[i-1] = two[i-2]
        three[i-1] = three[i-2]
    one[0] = temp3
    two[0] = temp
    three[0] = temp2

for _ in range(t):
    change()

for i in range(n):
    print(one[i], end = ' ')
print()
for i in range(n):
    print(two[i], end = ' ')
print()
for i in range(n):
    print(three[i], end = ' ')