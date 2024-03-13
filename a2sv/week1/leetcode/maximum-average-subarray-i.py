class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k
        window = sum(nums[:k]) 
        max_ = window

        while right < len(nums):
            window -= nums[left]
            left += 1
            window += nums[right]
            max_ = max(max_, window)
            right +=1
        return max_/k
            