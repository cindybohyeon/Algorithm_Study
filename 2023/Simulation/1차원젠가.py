# (1) 변수 선언 및 입력
n = int(input())
# a = [0 for _ in range(n)]
# for i in range(n):
#     a[i] = int(input())
numbers = [ int(input()) for _ in range(n)]



end_of_array = n

# (2) 입력받은 자르는 구간을 제외한 새로운 temp 배열 생성
# [:]이용하여, temp없이 배열 생성
def cut_array(start_idx, end_idx):
    global end_of_array, numbers
    temp_arr = []

    # (2) 구간 외의 부분만 temp배열에 순서대로 저장
    # 0이 아닌 곳만 저장
    # for i in range(end_of_array):
    #     if(i < start_idx or i > end_idx):
    #         temp_arr.append(numbers[i])
    numbers = numbers[:start_idx] + numbers[end_idx+1:]

    # temp배열을 다시 number배열로 옮겨준다
    # end_of_array = len(temp_arr)
    # for i in range(end_of_array):
    #     numbers[i] = temp_arr[i]


for _ in range(2):
    s, e = map(int, input().split())
    cut_array(s-1,e-1)

print(len(numbers))
for i in range(len(numbers)):
    print(numbers[i])