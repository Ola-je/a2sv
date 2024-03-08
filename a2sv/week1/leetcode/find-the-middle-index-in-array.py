class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        
        for i in range(len(nums)):
            left += nums[i]
            if left == right:
                return i
            else:
                right -= nums[i]
        return -1