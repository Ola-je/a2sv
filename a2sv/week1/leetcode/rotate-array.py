class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        start = 0
        end = len(nums)-k
        nums[start:end] = reversed(nums[start:end])

        start = end
        end = len(nums)
        nums[start:end] = reversed(nums[start:end])

        nums.reverse()
        