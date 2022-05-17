class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

#  nums = [1,7,3,6,5,6]


# choose the pivot -> O(n)
# checking leftsum == rightsum -> O(n)
-> O(n*2)

# total sum = leftsum + num[pivot] + rightsum -> O(n)
# # choose the pivot -> O(n)



        totalsum = sum(nums)
        leftsum = 0
        for i in range(len(nums)):
            rightsum = totalsum - leftsum - nums[i]
            if leftsum == rightsum:
                return i
            leftsum += nums[i]

        return -1