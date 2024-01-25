N = int(input())
arr = [list(input().split()) for _ in range(N)]

# for i in range(N):
#     arr[i][0] = ord(arr[i][0])


arr.sort(key=lambda arr: (-int(arr[1]), int(arr[2]), -int(arr[3]), (arr[0])))
print(arr)
