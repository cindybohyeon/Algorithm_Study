class Solution:
    import copy
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = list(map(int, input().split()))
        # target = int(input())
        result = []
        OriginNums = copy.deepcopy(nums)
        nums.sort()
        # [2, 7, 11, 15]
        start = 0
        end = len(nums) - 1
        while(start <= end):
            temp = nums[start] + nums[end]
            if temp > target:
                end -= 1
            elif temp < target:
                start += 1
            else:
                # 기존의 index 값을 가져와야한다.
                # 다른 경우
                for i in range(len(nums)):
                    if nums[start] == OriginNums[i] or nums[end] == OriginNums[i]:
                        result.append(i)                    
                break
        return result
