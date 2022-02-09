#  n번째 원소 구하기 DP 구현 


# 같은 크기에 대해서 같은 계산을 하지 않도록 기억
# memoization .

# n = 6;
# memo[7];

# def InitializeMemo():
#     for i in range(1,n+1):
#         memo[i] = -1;


# 피보나치 수. 

n = int(input())

def fibo(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


print(fibo(n))

