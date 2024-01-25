graph = []
n = int(input())
for _ in range(n):
    a = int(input())
    graph.append(a)

# 카드 묶음의 크기.
# ㅇㅏ무튼 2개로 묶는 경우의 수..

# 어떻게 해?
# 10, 20, 40
graph.sort()
result = 0

def fibi(n):
    if (n==0):
        return 0
    else:
        # print(n,"#")
        return (graph[n-1] + fibi(n-1))
sum = 0
for i in range(2,n+1):
    sum += fibi(i)
print(sum)

# def sumf(index):

#     if (index != 0):
#         sumf(index)


# sumf(n)