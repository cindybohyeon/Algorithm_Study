n = int(input())
arr = list(input().split() for _ in range(n))
# print(arr)

# arr.sort(key= lambda a: -(int(a[1]), int(a[2]), -int(a[3]), a[0]))
# arr.sort(key=)
arr.sort(key=lambda a:(-int(a[1]), int(a[2]), -int(a[3]), a[0]))

for i in range(n):
    print(arr[i][0])