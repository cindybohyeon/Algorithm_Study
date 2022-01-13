k,n = map(int, input().split())
# string = []
def Choose(x : int, string:list):
    global n,k
    '''
    n의 배열크기 만큼의 string을 출력한다.
    '''
    if x == n+1:
        '''
        list 출력할 때 일차원일때 print(i)만 출력하면 된다 !!!!!!!
        계속 string[i]으로 출력해서 오류발생한다.
        '''
        for i in string:
            print(i, end=' ')
        print()
        return

    for i in range(1,k+1):
        if x <= 2 or i != string[-1] or i != string[-2]:
            Choose(x+1, string+[i]) 

        '''
        1. 여기서 x가 배열의 원소를 뜻하니까 len사용안해도 된다
        2. 조건문 작성이 어려울 때 반대로 생각하기 
        '''

Choose(1,[])
