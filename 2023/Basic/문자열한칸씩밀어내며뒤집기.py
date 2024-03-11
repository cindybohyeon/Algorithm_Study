# 문자열 입력하기 
# input()은 기본적으로 string형으로 입력받는다
# string indexing : string [a:b] : a부터 b indexing까지
# string[-1] : 맨 마지막 글자 

# for문 뒤로 읽기
# range (처음인덱싱, 마지막인덱싱, 인덱싱의 폭)
# ex : range(len(rd_list), 0, -1)
string,num = input().split()
num = int(num)
for i in range(num):
	type = int(input())
	if(type == 1):
		# 앞으로 당기기
		string = string[1:]+string[0]
		print(string)
	elif(type == 2):
		# 뒤로 당기기
		string = string[-1]+string[0:-1]
		# string[0:-1] 는 -1 전까지 출력된다. 
		print(string)
	elif(type == 3):
		# 좌우 뒤집기 = 반대로 출력되는 것. 
		# 1번째 방법 : 모듈 사용 [::-1]
		string = string[::-1]
		print(string)
		# 2번째 방법 : for 문 사용 -> 런타임 에러
		# for i in range(len(string), -1, -1):
		# 	print(string[i],end='')