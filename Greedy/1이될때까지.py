# 어떠한 수 N이 1이 될 때까지 두 과정 중 하나를 반복적으로 선택.
# 두번째는 N이 K로 떨어질 때만 선택가능.

# n에서 1을 뺀다. / N을 K로 나눈다.

n,k = map(int, input().split())
result = 0
# while True:
#     if n == 1:
#         break
#     if n%k == 0:
#         n = n/k
#         result += 1
#     else:
#         n -= 1
#         result += 1

while True:
    # N==K 로 나누어 떨어지는 수 가 될 때까지 1씩 빼기
    target = (n/k)* k
    result += (n-target)
    n = target
    # n이 k 보다 작을 때 즉 더이상 나눌 수 없을 때까지
    if n<k:
        break
    # k로 나누기
    result += 1
    n = n/k

# 마지막으로 남은 수에 대하여 1씩 빼기 : n-1한 이유는 n==1이 될 때까지 빼는거니까.
result += (n-1)

print(result)