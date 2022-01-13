import sys
si = sys.stdin.readline

k,n = map(int, si().split())

def Choose(curr_num : int, string:list):
    global n
    # 배열원소 n개까지 만들고 그만 
    if curr_num == n+1:
        for i in string:
            print(i, end=" ")
        print()
        return
    
    for i in range(1,k+1):
        Choose(curr_num+1, string+[i])
        # string형이라면, str()함수에 i를 넣어서 정수i를 문자열로 변환한다
        # string+str(i)
    


Choose(1,[])