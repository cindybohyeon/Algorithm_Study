# 아름다운수 
# mgr566666666666666666666666666666666666666666666666666666666666666666666
# 아름다운수 
n = int(input())
# 한번에 아름다운 수를 만들어 내지 않고 1-4사이의 숫자로만 이루어진 모든 숫자를 만들어 낸 뒤
# 
ans = 0
seq = list()


def is_beautiful():
    # 연달아 같은 순자가 나오는 시작 위치를 잡는다
    i = 0
    while i < n :
        # 만약 연속하여 해당 숫자만큼 나올 수 없다면
        # n 의 값이 시작 위치 + 시작하려는 원소의 값 -1 보다 작아야 들어간다. 
        if i + seq[i] - 1 >= n :
            return False
        # 하나라도 들어갈 수 있는 경우
        # 하나라도 다른 숫자가 있으면 안된다. 
        for j in range(i, i+seq[i]):
            if seq[j] != seq[i]:
                return False
        i += seq[i]
    return True

def count_beautiful_seq(cnt):
    global ans

    if cnt == n:
        if is_beautiful():
            ans += 1
        return
    for i in range(1,5):
        seq.append(i)
        count_beautiful_seq(cnt + 1)
        seq.pop()

count_beautiful_seq(0)
print(ans)

