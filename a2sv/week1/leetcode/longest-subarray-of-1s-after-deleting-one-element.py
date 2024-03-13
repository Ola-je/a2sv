class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count0 = l = 0
        max_ = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                count0 +=1 
            while count0 == 2:
                if nums[l] == 0:
                    count0 -=1
                l +=1
            max_ = max(max_, r-l)
        return max_ 

