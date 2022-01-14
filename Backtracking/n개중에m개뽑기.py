N,M = map(int, input().split())

# def Choose(x, string, cnt_one):
#     '''
#     param : cnt_one 현재까지 사용한 1의 개수
#     '''
#     global N, M
#     if x == N+1:
#         if cnt_one == M:
#             for i in range(N):
#                 if string[i] == '1':
#                     print(i+1, end = ' ')
#             print()
#         return

#     Choose(x+1, string+'1',cnt_one+1)
#     Choose(x+1, string+'0', cnt_one)


'''
먼저 이진수 string을 만든다. N개의 원소를 가진 이진수를 만든다.
그리고 그 이진수에서 1의 개수가 M인 이진수를 골라서
string[i] == 1인경우만 출력하도록 즉, M번 출력하도록 한다.
그리고 출력시에 [i]배열원소 위치 i+1를 출력한다.

출력 순서를 정할 때 
이진수 0을 먼저 넣으면(재귀), 0011이 처음 string이고 
34가 먼저 출력된다
즉 내림차순

이진수 1 먼저 넣으면 오름차순


'''

def Choose(x, string):
    '''
    param : cnt_one 현재까지 사용한 1의 개수
    '''
    global N, M
    if x == N+1:
        if len(string) == M:
            for i in string:
                print(i, end = ' ')
            print()
        return
    if len(string) < M:
        Choose(x+1, string+[x])
    Choose(x+1, string)
    
    
Choose(1,[])

'''
많이 나온다. 
암기해야한다!
'''

N,M = map(int, input().split())

def Choose(x, string):

    global N, M
    if len(string) == M:
        for i in string:
            print(i, end = ' ')
        print()
        return

    for i in range(1, N+1):
        if not string or i > string[-1]:
            Choose(i+1, string+[i])
            
    
    
Choose(1,[])
'''
출력할 때 string의 배열크기가 M일 때 출력하도록 한다. 
재귀를 N 만큼 조건끼고 돌려서
'''
