


def binary(arr, target):
    left = 0
    right = len(arr)-1
    mid = (left + right) / 2
    while left <= right:
        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# upper bound : 최초로 초과하는 것
# lower bound : 같거나 큰 경우 

# lower bound

    def lower_bound(arr, target):
        left = 0
        right = len(arr)-1
        min_idx = arr.size
        while left <= right:
            mid = (left + right)/2
            if arr[mid] >= target:
                right = mid - 1
                min_idx = min(min_idx, mid)
                //같거나 큰 값들 중 최소값을 넣어준다. 
            else:
                left = mid + 1

        return min_idx
                