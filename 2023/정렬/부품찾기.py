# 동빈이네 전자 매장에는 부품이 n개 , 부품은 정수 형태의 번호있다. 
# M개 정류를 구메히걌다.

n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))
mid = 0
mid_index = 0
def binarysearch(arr, target, start, end):   
    global mid, mid_index
    while start <= end:
        mid_index = (start + end) // 2
# 나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 수만 구함


        # mid = int( arr[mid_index])
        if(target == arr[mid_index]):
            return True
        if(target > arr[mid_index]):
            start = mid_index + 1
        else:
            end = mid_index - 1
    return False
        
n_arr.sort()
m_arr.sort()


for i in range(m):

    if binarysearch(n_arr, m_arr[i],0,n-1):
        print("yes")
    else: 
        print("no")