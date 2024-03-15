class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        ps = list(accumulate(nums))
        ssum = [0]*len(nums)
        ssum[-1] = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            ssum[i] = ssum[i+1] + nums[i]

        for i in range(len(nums)):
            result[i] = nums[i]*i - ps[i] + ssum[i] - nums[i]*(len(nums)-i-1)
        return result