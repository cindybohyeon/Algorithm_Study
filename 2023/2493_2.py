from typing import List, Union, Tuple

def find_a_b_combinations(fees: List[List[int]]) -> List[Union[Tuple[int, int], int]]:
    combinations = []

    for fee_info in fees:
        target_fee, paid_fee = fee_info
        found_combination = None

        for a in range(1, target_fee + 1):
            # 주차료 계산
            total_fee = 0
            for time in range(1, a * 2):
                if time % a == 0:
                    total_fee += b

            # 주차료가 목표 주차료와 일치하는 경우
            if total_fee == paid_fee:
                found_combination = (a, b)
                break

        combinations.append(found_combination if found_combination else -1)

    return combinations

# 예시 입력에 대한 호출
fees_input = [[4, 1000], [6, 1000], [21, 3000], [16, 2000], [26, 3000]]
result = find_a_b_combinations(fees_input)

print("Result:", result)
