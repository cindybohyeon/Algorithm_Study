# # 주어진 수들을 M 번 더하여 가장 큰 수를 만드는 법칙이다. 
# # 하지만 하나의 배열의 원소가 연속해서 K번을 초과하여 더해질 수 없다.

# # 문제 풀이 : 제일 큰 값 K 번 + 그 다음 큰 값 1번 + 제일 큰 값 K 번 + 그 다음 큰 값 1번 ...

# # n,m,k 공백구분하여 한줄로 입력받기 
# n,m,k = map(int, input().split())
# # 
# array = list(map(int, input().split()))

# # array  정렬하기. 가장 큰 수를 먼저 선택할 수 있도록
# array.sort()
# first = array[n-1]
# second = array[n-2]

# ans = 0

# while True:

#     for _ in range(k):
#         if m == 0:
#             break
#         ans += first
#         m -= 1
#     if m == 0:
#         break
    
#     ans += second
#     m -= 1

# print(ans)
    

n,m,k = map(int, input().split())
# 배열의 크기, 숫자가 더해지는 횟수, 연속으로 더해질 수 있는 횟수
num = list(map(int, input().split()))

# 제일 큰 수를 k 번 더하고 다음 큰 수 한번 더하고 ---
# 수열의  길이 k+1
list_len = m/(k+1) + m%(k+1)
num.sort()
max_len = m/(k+1) * k + m%(k+1)
next_len = m - max_len
ans = 0
ans = num[n-1] * max_len + num[n-2] * next_len
print(ans)