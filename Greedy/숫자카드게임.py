# 여러개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임.


# 행을 골라서 그 중 제일 작은 카드를 뽑을 수 있어서,
# 각 행들 중 제일 작은 카드들을 비교해서 제일 큰 카드가 있는 행을 골라야한다. 

n,m = map(int, input().split())

result = 0
min_value = 0

for _ in range(n):
    # 한 줄 씩 입력받아 확인 -> 한 행씩 입력받아 확인
    data = list(map(int, input().split()))
    if(min_value < min(data)):
        min_value = min(data)

print(min_value)