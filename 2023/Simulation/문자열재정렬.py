# 알파벳대문자와 숫자로만 구성된 문자열이 입력으로 주어진다. 
n = list(input())
# 알파벳을 오름차순으로 정렬헌더 그리고 숫자의 합을 출력, 
alphalist = []
sum = 0
for i in n:
    if i.isalpha():
        alphalist.append(i)
    else:
        sum += int(i)

alphalist.sort()
alphalist.append(str(sum))

print(alphalist)

# 리스트를 문자열로 변환하기
# 이 ㄸㅐ sum을 넣을 때 str로 변환해서 넣어줘야 join 사용가능하다.
print(''.join(alphalist))