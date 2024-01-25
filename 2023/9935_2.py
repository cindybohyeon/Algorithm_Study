array = list(input())
bom = input()

# print(len(bom))
answer = []
bomLen = len(bom)
arrayLen = len(array)
for i in range(arrayLen):
    # print("@")
    answer.append(array[i])
    # bom 의 길이 만큼 맨 뒤에서 가져온다
    temp = ''.join(answer[-bomLen:])
    # print(temp,"temp")
    if (temp == bom):
        for _ in range(bomLen):
            answer.pop()

print(''.join(answer))
