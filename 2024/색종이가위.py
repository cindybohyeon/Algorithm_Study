n, k = map(int, input().split())

# 색종이를 어떻게 자르는거지

rowS = 0
rowE = n // 2
result = False
while rowS <= rowE:
    mid = (rowS + rowE) // 2
    col = n - mid
    temp = (mid + 1) * (col + 1)
    if (k == temp):
        print("YES")
        result = True
        break
    if (k > temp):
        rowS = mid + 1
    else:
        rowE = mid - 1
        

if not result:
    print("NO")

# while(rowN <= colN):
#     temp = (rowN + 1) * (colN + 1)
#     if (temp == k):
#         result = True
#         break
#     if (temp > k):
#         rowN -= 1
#         colN += 1
#     if (temp < k):
#         colN -= 1
#         rowN += 1

