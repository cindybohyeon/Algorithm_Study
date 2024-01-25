# mirkovC4nizCC44
# C4 폭팔문자열

arr = list(input())
bom = input()
bomLength = len(bom)

ans = []

# FILO
for i in range(len(arr)):
    ans.append(arr[i])
    # 하나의 문자열로 만드는 것
    if(''.join(ans[-bomLength:]) == bom):
        for _ in range(bomLength):
            ans.pop()
# print(ans,"#")

if (ans == []):
    print("FRULA")
else:
    print(''.join(ans))



# # 빈 배열에서 넣는 경우
# # 먼저 그게 
# while(True):
#     if (arr[-bomLength:] ):
#         # 그 뒤에부터 그 다음까지 정말 맞는지 확인하기

#     else:
#         ans.append(arr[i])


