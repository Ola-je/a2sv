class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        summation = 0
        count = float('inf')

        for r in range(len(nums)):
            summation += nums[r]
            while summation >= target:
                count = min(count, r-l+1)
                summation -= nums[l]
                l+=1
        return count if l>0 else 0