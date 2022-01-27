str = []
a,b = map(int, input().split())
str.append(a)
str.append(b)
c,d = map(int, input().split())
str.append(c)
str.append(d)

str.sort()
count = 0
if(str[0] == a):
    if(str[1] == b):
        count = b-a + d-c
        print(count)
    else:
        count = str[-1]-str[0]
        print(count)

elif(str[0] == c):
    if(str[1] == d):
        count = b-a + d-c
        print(count)
    else:
        count = str[-1]-str[0]
        print(count)

else:
    print(count+1)