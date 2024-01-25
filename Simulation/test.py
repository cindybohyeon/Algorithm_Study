n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]

result = 0

#최대의 값은 합들 중에서 최대의 합
# 합을 구하는 방법
# 

def in_range(x,y):
    if x>=0 and y>=0 and x<n and y<n:
        return True
    else:
        return False
        # 격자에 들어있는 9개의 숫자의 합을 구한다
def get_sum(x,y):
    sum = 0
    for i in range(x,x+2):
        for j in range(y,y+2):
            if in_range(i,j):
                sum += graph[i][j]
    return sum





            
    