class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summation = 0
        max_ = float('-inf')
        for i in range(len(nums)):
            summation += nums[i]
            max_ = max(max_, summation)
            if summation < 0:
                summation = 0
        return max_