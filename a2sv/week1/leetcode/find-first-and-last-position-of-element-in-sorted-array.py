class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:        
        left = -1
        right = len(nums)
        li = [-1, -1]

        if target not in nums:
            return li  

        while left+1 < right:
            mid = left + (right-left)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        li[0] = right

        left = -1
        right = len(nums)
        
        while left+1 < right:
            mid = left + (right-left)//2
            if nums[mid] <= target:
                left = mid 
            else:
                right = mid
        li[1]= left
        
        return li