# 재귀함수 주석 사용하기!
# 입출력 을 주석으로 쓰기.

N = 3
def Choose_first(x, string):
    '''
    :return : N까지 string을 채우고, 출력한다.
    단, 출력할 때의 string 내에서 0이 연속으로 등장하면 안된다
    '''
    global N
    if x == N+1:
        if '00' not in string:
            print(string)
        return

    Choose_first(x+1, string+'0')
    Choose_first(x+1, string+'1')

Choose_first(1,'')


def Choose_second(x, string):
    '''
    :return : N까지 string을 채우고, 출력한다.
    '''
    global N
    if x == N+1:
        print(string)
        return

    if x==1 or string[-1] != '0':
        # string안에서 0이 연속으로 등장하지 않도록 끝자리가 0이 아닌 경우
        # 처음 넣는 경우에 0을 넣어준다
        Choose_second(x+1, string+'0')  
    Choose_second(x+1, string+'1')

Choose_second(1,'')


'''
시간복잡도
choose_first는 모든 경우대로 다 채워넣고 출력할 것만 빼서 출력한다.
결국 n=3이라면 한자리당 0과 1의 경우 2가지를 n=3만큼 , 2^3만큼의 시간복잡도가 걸린다
=>O(2^n)
choose_second는 정답조건만큼 즉, 출력되는 개수만큼을 재귀한다.
왜냐면 재귀함수 호출시 조건을 걸었기 때문.
=>O(정답개수)
'''