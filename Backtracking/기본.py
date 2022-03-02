# 1. 함수의 입력과 출력을 정확히 명시
# 2. 재귀함수의 종료 조건(문제가 가장 쉬울 때)을 올바르게 작성
# 3. 문제가 클 경우에는 함수의 역할을 믿고 재귀호출로 문제를 해결

# def sum( x :int) -> int:
#     '''
#     return : 1부터 x까지의 합
#     '''
#     if x < 1: #종료 조건
#         return 0
 
N = 4
string = ''
def Choose(curr_num : int, string: str):
    '''
    :param: string: str = 이전(1~curr_num-1)에 만들어진 이진수
    :return:    curr_num 번째 부터 N번째 자리까지
                모든 가능한 경우를 찾아주는 함수
    '''
    global N
    global string
    if curr_num == N+1:
        print(string)
        return
    # 전역변수를 사용해도 된다
    # string = string + '0'
    Choose(curr_num + 1, string + '0')
    # string = string[:-1]

    # string = string + '1'
    Choose(curr_num + 1, string + '1')
    # string = string[:-1]
    
Choose(1,'')



# 0302
import sys
si = sys.stdin.readline

k,n = map(int, si().split())

# 둘 중 하나를 N 번 선택하기 
# k개 중 하나를 N번 선택하기
ans = []

def Choose(curr_num):
    global n
    if curr_num == n:
        for a in ans:
            print(a, end = ' ')
        print()
        return

    
    ans.append(0)
    Choose(curr_num+1)
    ans.pop()

    ans.append(1)
    Choose(curr_num+1)
    ans.pop()

    return

Choose(0)
