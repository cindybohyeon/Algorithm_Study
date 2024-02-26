def solution(arr, query):
    answer = []
    qLen = len(query)
    for i in range(qLen):
        q = query[i]
        # print(q, "q")
        if i % 2 == 0: # 짝수 인덱스
            arr = arr[:q + 1]
        else:
            arr = arr[q:]
        # print(arr, "arr")
    return arr