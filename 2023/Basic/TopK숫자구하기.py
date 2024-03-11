n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr = sorted(arr)
print(arr[k-1])


# sort()는 새로운 정렬된 목록을 반환하여 원래 목록은 영향을 받지 않는다
# sort()는 list의 메서드이다 (즉 다른 string문자열에서는 사용할 수 없다)

# sorted는 list뿐만 아니라 모든 요소가 표함된 반복 가능한 객체를 정렬하여 반환한다. 