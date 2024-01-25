n, m = map(int, input().split())
books = list(map(int, input().split()))

books.sort()
putBooks = []
result = 0

# 넣은 것들의 index를 봐서 안 넣은 것부터 m 까지의 배열을 가져온다
def grapBooks():
    global books, putBooks, m
    putLen = len(putBooks)
    grapBook = []
    for i in range(m):
        if (i + putLen >= len(books)):
            break
        grapBook.append(books[i + putLen])
    return grapBook

# 배열에서 이동거리를 가져온다
def tempResult(tempGrapBooks):
    global m
    result = 0

    if (len(tempGrapBooks) == 1):
        return tempGrapBooks[0]

    result += abs(tempGrapBooks[0]) + abs(tempGrapBooks[-1])
    for i in range(len(tempGrapBooks)-1):
        result += tempGrapBooks[i+1] - tempGrapBooks[i]
    return result

while(putBooks != books):
    tempGrapBooks = grapBooks()
    # print(tempGrapBooks, "tempBooks")
    temp = tempResult(tempGrapBooks)
    # print(temp, "tempTesult")
    result += temp

    for i in tempGrapBooks:
        putBooks.append(i)

print(result)
