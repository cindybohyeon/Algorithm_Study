class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        # 1,2,3,4,5
        nums.sort()
        result = 0
        for i in range(k):
            result += nums[-1] + i
        return result