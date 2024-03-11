N= 4 
M=3
def Choose(x, string, cnt_one):
    '''
    param : cnt_one 현재까지 사용한 1의 개수
    '''
    global N, M
    if x == N+1:
        if cnt_one == M:
            print(string)
        return
    
    Choose(x+1, string+'0', cnt_one)
    if cnt_one < M:
        Choose(x+1, string+'1',cnt_one+1)

Choose(1,'',0)