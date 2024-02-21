class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        for left in range(n):
            for right in range(n-1, left,-1):
                if nums[left]== nums[right] and left*right % k == 0:
                    count += 1 
        return count