# n개의 숫자가 공백 없이 쓰여있다
result = 0
n = int(input())
ans = str(input())

for i in range(len(ans)):
    result += int(ans[i])
print(result)