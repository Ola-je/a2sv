class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        l, r = 0, 1 

        while r < len(nums):
            if nums[l] == nums[r]:
                r += 1
            else:
                l += 1
                nums[l] = nums[r]
                r += 1
        return l+1
