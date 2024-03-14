class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count0 = 0
        result = 0
        l=0

        if k >= len(nums):
            return len(nums)
        for r in range(len(nums)):
            if nums[r]==0:
                count0 += 1
            while count0 > k:
                if nums[l] == 0:
                    count0 -=1
                l+=1
            result = max(result, r-l+1)
        return result